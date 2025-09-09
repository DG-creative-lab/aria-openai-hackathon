# backend/aria/memory/prompts.py
from __future__ import annotations
from typing import Dict, List
import os

# ---- knobs (env) ----
PLAN_JSON_KEYS = os.getenv(
    "PLAN_JSON_KEYS",
    "action,reasoning,risk,confidence"
).split(",")

# System prompt kept short to reduce tokens but very explicit on JSON output.
SYSTEM = """You are ARIA, a mission-control copilot for parafoil landing.
Return a SINGLE JSON object with keys: action, reasoning, risk, confidence.
- Be concise. Reasoning ≤ 2 sentences.
- Ground your answer only on the provided STATE/RECENT/LESSONS/FACTS/QA.
- If you used a snippet, include its source_id(s) inline in reasoning like [EUCASS2019-0633.md#part0].
- If information is insufficient or conflicting, say so and propose 'tool:doc_search' with a short query in the action.
- No Markdown, no extra text—JSON only."""

# A tiny few-shot keeps shape + tone stable
FEWSHOT: List[Dict[str, str]] = [
    {
        "role": "user",
        "content": (
            "STATE:\n"
            "  Altitude: 60 m AGL\n  VSpeed: -4.2 m/s\n  Wind: 5 m/s crosswind\n"
            "RECENT:\n  anomaly: crosswind_high\n"
            "LESSONS:\n  - Flare 5–10 m earlier in strong crosswinds. (SOURCE: repr_lesson:Manual.md#part12)\n"
            "FACTS:\n  - Flare window: 40–60 m for approach speed 20 m/s. (SOURCE: repr_fact:Guide.md#part4)\n"
        )
    },
    {
        "role": "assistant",
        "content": (
            '{"action":"Initiate flare now",'
            '"reasoning":"Within 40–60 m window; early flare offsets crosswind [Manual.md#part12].",'
            '"risk":"Moderate (premature stall if flare too early)",'
            '"confidence":0.82}'
        )
    },
]

def _join_block(title: str, lines: List[str]) -> str:
    if not lines:
        return ""
    out = [f"{title}:"]
    # lines are already truncated by governor; keep as-is
    for ln in lines:
        out.append(f"  {ln}")
    return "\n".join(out)

def render_sections(sections: Dict[str, List[str]]) -> str:
    """Turn composer/governor sections into a compact single user message."""
    parts: List[str] = []
    parts.append(_join_block("STATE", sections.get("state", [])))
    parts.append(_join_block("RECENT", sections.get("recent", [])))
    parts.append(_join_block("LESSONS", sections.get("lessons", [])))
    parts.append(_join_block("FACTS", sections.get("facts", [])))
    parts.append(_join_block("QA", sections.get("qa", [])))
    # optional raw docs if composer added them
    if sections.get("docs"):
        parts.append(_join_block("DOCS", sections.get("docs", [])))
    # filter empty blocks and join
    return "\n\n".join(p for p in parts if p and p.strip())

def build_messages(sections: Dict[str, List[str]]) -> List[Dict[str, str]]:
    """Assemble the final chat messages for call_model(..., response_format='json_object')."""
    user = render_sections(sections)
    messages: List[Dict[str, str]] = [{"role": "system", "content": SYSTEM}]
    messages.extend(FEWSHOT)
    messages.append({"role": "user", "content": user})
    return messages