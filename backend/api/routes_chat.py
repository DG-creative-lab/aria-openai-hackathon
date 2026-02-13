# backend/api/routes_chat.py
from __future__ import annotations
from typing import List, Literal, Optional, Dict, Any
from fastapi import APIRouter
from pydantic import BaseModel, Field

from ..aria.agent import call_model
from ..aria.memory import tools as mem_tools

router = APIRouter(prefix="/api/chat", tags=["chat"])

DEFAULT_SYSTEM = (
    "You are ARIA, a mission-control copilot. Be concise, cite sources when you use docs/lessons. "
    "If the user asks for references, you may request a tool using the pattern "
    "{\"tool\":\"doc_search\",\"query\":\"...\",\"k\":5} or "
    "{\"tool\":\"recall_lesson\",\"query\":\"...\",\"k\":3}."
)

class Msg(BaseModel):
    role: Literal["system","user","assistant"]
    content: str

class ChatIn(BaseModel):
    messages: List[Msg] = Field(default_factory=list)
    system: Optional[str] = None

class ChatOut(BaseModel):
    reply: str
    used_tool: Optional[str] = None
    observation: Optional[str] = None

def _maybe_run_tool(raw_text: str) -> tuple[Optional[str], Optional[str]]:
    """Allow quick inline tools like: tool:doc_search q=\"flare window\" k=5"""
    raw = (raw_text or "").strip()
    if not raw.lower().startswith("tool:"):
        return None, None
    label, obs = mem_tools.tool_router("data/aria.sqlite", raw)
    return label, obs

@router.post("")
def chat(body: ChatIn) -> ChatOut:
    # 1) assemble messages (prepend our default system if user didn't send one)
    messages: List[Dict[str,str]] = []
    messages.append({"role":"system", "content": body.system or DEFAULT_SYSTEM})
    for m in body.messages[-12:]:
        messages.append({"role": m.role, "content": m.content})

    # 2) first call
    raw = call_model(messages=messages, response_format=None, max_tokens=500)
    used_tool, observation = None, None

    # 3) tool pass (JSON tool or inline 'tool:' directive)
    import json
    plan_obj: Dict[str, Any] | None = None
    try:
        plan_obj = json.loads(raw) if raw.strip().startswith("{") else None
    except Exception:
        plan_obj = None

    # JSON tool
    if isinstance(plan_obj, dict) and "tool" in plan_obj:
        tname = str(plan_obj.get("tool","")).lower()
        q = str(plan_obj.get("query") or plan_obj.get("q") or "")
        k = int(plan_obj.get("k") or 5)
        if tname == "doc_search":
            used_tool = "doc_search"
            observation = mem_tools.doc_search("data/aria.sqlite", q, k=k, prefer_rephrased=True, as_json=False)
        elif tname in ("recall_lesson","lesson"):
            used_tool = "recall_lesson"
            observation = mem_tools.recall_lesson("data/aria.sqlite", q, k=min(k,5), as_json=False)

    # Inline tool
    if observation is None:
        lbl, obs = _maybe_run_tool(raw)
        if obs:
            used_tool, observation = lbl, obs

    # 4) follow-up if we ran a tool
    if observation:
        follow = messages + [
            {"role": "assistant", "content": observation},
            {"role": "user", "content": "Using the observation above, answer the original query with citations."},
        ]
        raw = call_model(messages=follow, response_format=None, max_tokens=500)

    reply = (raw or "").strip()
    if not reply:
        reply = "I couldn't generate a text reply from the model. Please try again or switch model settings."
    return ChatOut(reply=reply, used_tool=used_tool, observation=observation)
