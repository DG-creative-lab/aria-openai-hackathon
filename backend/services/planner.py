# backend/services/planner.py
from __future__ import annotations
import os, json
from typing import Dict, Any, List, Tuple, Optional

from ..aria.agent import call_model
from ..aria.memory import composer, governor, prompts, tools
from .safety_gate import vet_plan
from ..aria.memory.store import episodic_append
from .plan_schema import Plan, ensure_plan  # ← schema-aligned

TOKEN_BUDGET = int(os.getenv("PLAN_TOKEN_BUDGET", "900"))
MAX_COMPLETION_TOKENS = int(os.getenv("PLAN_MAX_COMPLETION", "256"))
ALLOW_TOOL_REQUESTS = os.getenv("ALLOW_TOOL_REQUESTS", "1") != "0"


def _state_str(state_summary: Dict[str, Any] | str) -> str:
    if isinstance(state_summary, str):
        return state_summary
    return (
        f"Alt={state_summary.get('altitude_agl_m', 0):.1f} m; "
        f"Vz={state_summary.get('vertical_speed_mps', 0):.2f} m/s; "
        f"Wind=({state_summary.get('wind_xy_mps',[0,0])[0]:.1f},"
        f"{state_summary.get('wind_xy_mps',[0,0])[1]:.1f}) m/s; "
        f"Phase={state_summary.get('phase','')}"
    )


def _apply_budget(sections: Dict[str, List[str]], budget_tokens: int) -> Dict[str, List[str]]:
    """
    Safe budget wrapper. Uses governor.apply_budget if available and
    never raises. Ensures all canonical keys exist on fallback.
    """
    try:
        if hasattr(governor, "apply_budget"):
            trimmed, _stats = governor.apply_budget(
                sections,
                total_budget_tokens=budget_tokens,
            )
            return trimmed
    except Exception as e:
        print("[planner] governor failed; using raw sections:", e)

    # Fallback: make sure all keys exist so downstream code is stable
    for k in ("state", "recent", "lessons", "facts", "qa", "docs"):
        sections.setdefault(k, [])
    return sections


def _maybe_run_tool(db_path: str, raw: str, plan_obj: Optional[dict]) -> Tuple[Optional[str], Optional[str]]:
    """
    Detect tool requests and run them.
    Returns (label, observation_text) or (None, None).
    Supports:
      1) JSON: {"tool":"doc_search","query":"...","k":5}
      2) Bare text: "tool:doc_search q=\"...\" k=5"
    """
    if not ALLOW_TOOL_REQUESTS:
        return None, None

    # Case 1: JSON plan contains a tool request
    if isinstance(plan_obj, dict) and "tool" in plan_obj:
        tname = str(plan_obj.get("tool", "")).lower().strip()
        q = plan_obj.get("query") or plan_obj.get("q") or ""
        k = int(plan_obj.get("k", 5) or 5)
        if tname == "doc_search":
            return "DOC_SEARCH", tools.doc_search(db_path, q, k=k, prefer_rephrased=True, as_json=False)
        if tname in ("recall_lesson", "lesson"):
            return "LESSON_RECALL", tools.recall_lesson(db_path, q, k=min(k, 5), as_json=False)
        return None, None

    # Case 2: raw string begins with a tool directive
    text = (raw or "").strip()
    if text.lower().startswith("tool:"):
        label, obs = tools.tool_router(db_path, text)
        return label, obs

    return None, None


async def tick(db_path: str, state_summary: Dict[str, Any] | str, query: str, ablations: Dict[str, bool]) -> Dict[str, Any]:
    """
    One planning cycle. Returns a JSON-serializable plan dict (validated by Plan schema).
    """
    # 1) Compose working memory (retrieval happens inside composer)
    wm = composer.build_working_memory(
        db_path=db_path,
        state_summary=_state_str(state_summary),
        query=(query if ablations.get("use_docs", True) else "")
    )

    # 2) Apply ablations
    if not ablations.get("use_lessons", True):
        wm["lessons"] = []
    if not ablations.get("use_docs", True):
        wm["docs"] = []
        wm["facts"] = []
        wm["qa"] = []

    # 3) Governor: enforce token budget
    wm = _apply_budget(wm, TOKEN_BUDGET)

    # 4) Build messages using centralized prompts module
    messages = prompts.build_messages(wm)

    # 5) Call model (JSON mode, first attempt)
    raw = call_model(messages=messages, response_format="json_object", max_tokens=MAX_COMPLETION_TOKENS)
    try:
        plan_raw = json.loads(raw)
    except Exception:
        plan_raw = {}

    # 5b) ReAct-lite: allow one short tool hop then a follow-up call
    used_tool = False
    label, observation = _maybe_run_tool(db_path, raw, plan_raw)
    if observation:
        used_tool = True
        follow_messages = messages + [
            {"role": "assistant", "content": observation},
            {"role": "user", "content": "Using the observation above, return the final JSON plan."},
        ]
        raw2 = call_model(messages=follow_messages, response_format="json_object", max_tokens=MAX_COMPLETION_TOKENS)
        try:
            plan_raw = json.loads(raw2)
        except Exception:
            plan_raw = {
                "action": "Hold pattern",
                "reasoning": "Parser fallback after tool.",
                "risk": "medium",
                "confidence": 0.4,
            }

    # 6) Schema validation/normalization
    plan_dict = ensure_plan(plan_raw)             # clamps risk/confidence, trims text, defaults id/checks/etc.
    # ensure phase present from runtime state
    if isinstance(state_summary, dict):
        plan_dict.setdefault("phase", state_summary.get("phase", "descent"))
    else:
        plan_dict.setdefault("phase", "descent")

    # 6b) lightweight reference flags for UI
    refs: List[str] = []
    if wm.get("lessons"): refs.append("lessons")
    if wm.get("facts"):   refs.append("facts")
    if wm.get("qa"):      refs.append("qa")
    if wm.get("docs"):    refs.append("docs")
    if used_tool and label: refs.append(f"tool:{label.lower()}")
    # merge/unique w/ any model-provided references
    plan_dict["references"] = sorted(set((plan_dict.get("references") or []) + refs))

    # 7) Safety gate (may adjust action/risk/checks)
    if ablations.get("use_gate", True):
        plan_dict = vet_plan(plan_dict, state_summary if isinstance(state_summary, dict) else {})
        # re-validate to keep invariants (lengths, clamping)
        plan_dict = ensure_plan(plan_dict)

    # 8) Episodic log
    episodic_append(
        db_path,
        kind="decision",
        text=f"{plan_dict.get('action','(no action)')} ({plan_dict.get('confidence',0)})",
        data=plan_dict
    )

    # 9) Stable id (Plan already defaults but double-ensure)
    plan_dict.setdefault("id", "plan")
    return plan_dict
