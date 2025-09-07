# backend/services/planner.py - minimum version, needs review and rewrite
from __future__ import annotations
import os, json
from typing import Dict, Any, List

from ..aria.agent import call_model
from ..aria.prompts import SYSTEM, FEWSHOT
from ..aria.memory.composer import build_working_memory
from ..aria.memory.governor import trim_sections
from .safety_gate import vet_plan
from ..aria.memory.store import episodic_append

TOKEN_BUDGET = 900  # rough prompt budget (tune)

def _messages_from_context(sections: Dict[str, List[str]]) -> List[Dict[str, str]]:
    msgs: List[Dict[str, str]] = [{"role": "system", "content": SYSTEM}]
    msgs += FEWSHOT
    ctx: List[str] = []
    if sections.get("state"):  ctx.append("STATE: " + sections["state"][0])
    for r in sections.get("recent", []):  ctx.append("RECENT: " + r)
    for l in sections.get("lessons", []): ctx.append("LESSON: " + l)
    for d in sections.get("docs", []):    ctx.append("DOC: " + d)
    msgs.append({"role": "user", "content": "\n".join(ctx)})
    return msgs

async def tick(db_path: str, state_summary: Dict[str, Any], query: str, ablations: Dict[str, bool]) -> Dict[str, Any]:
    """
    One planning cycle. Returns a JSON-serializable plan dict.
    """
    # Build working memory with ablations
    wm = build_working_memory(db_path, state_summary=(
        f"Alt={state_summary['altitude_agl_m']:.1f} m; Vz={state_summary['vertical_speed_mps']:.2f} m/s; "
        f"Wind=({state_summary['wind_xy_mps'][0]:.1f},{state_summary['wind_xy_mps'][1]:.1f}) m/s; "
        f"Phase={state_summary.get('phase','')}"
    ), query=(query if ablations.get("use_docs", True) else ""))

    if not ablations.get("use_lessons", True):
        wm["lessons"] = []

    if not ablations.get("use_docs", True):
        wm["docs"] = []

    wm = trim_sections(wm, TOKEN_BUDGET)
    msgs = _messages_from_context(wm)

    # Call model (OpenAI-compatible via aria.agent)
    raw = call_model(messages=msgs, response_format="json_object", max_tokens=256)
    try:
        plan = json.loads(raw)
    except Exception:
        plan = {"action": "Hold pattern", "rationale": "Parser fallback", "risk": "medium", "confidence": 0.4}

    # Attach phase & references if we had sources
    plan.setdefault("phase", state_summary.get("phase", "descent"))
    refs = []
    if wm.get("lessons"): refs.append("lesson:top")
    if wm.get("docs"):    refs.append("doc:top")
    plan["references"] = refs
    plan.setdefault("checks", [])

    # Safety gate
    if ablations.get("use_gate", True):
        plan = vet_plan(plan, state_summary)

    # Episodic log
    episodic_append(db_path, kind="decision", text=f"{plan['action']} ({plan.get('confidence',0)})", data=plan)

    # Ensure stable fields for UI
    plan.setdefault("id", "plan")
    plan["confidence"] = round(float(plan.get("confidence", 0.5)), 2)
    return plan

def make_prompt(sections: Dict[str, list]) -> list[Dict[str, str]]:
    msgs = [{"role":"system","content":SYSTEM}]
    for ex in FEWSHOT:
        msgs.append(ex)
    # add context
    ctx = []
    if sections.get("state"): ctx.append("STATE: " + sections["state"][0])
    if sections.get("recent"): ctx += [f"RECENT: {r}" for r in sections["recent"]]
    if sections.get("lessons"): ctx += [f"LESSON: {l}" for l in sections["lessons"]]
    if sections.get("docs"): ctx += [f"DOC: {d}" for d in sections["docs"]]
    msgs.append({"role":"user","content":"\n".join(ctx)})
    return msgs
