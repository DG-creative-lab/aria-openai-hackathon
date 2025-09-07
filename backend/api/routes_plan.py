# backend/api/routes_plan.py
# accept approve/modify/reject (emit SSE):
from __future__ import annotations
from fastapi import APIRouter
from pydantic import BaseModel
from ..api.routes_events import publish_event

router = APIRouter(prefix="/api/plan", tags=["plan"])

class DecisionIn(BaseModel):
    plan_id: str
    human_action: str  # "approved"|"modified"|"rejected"
    modification: dict | None = None
    note: str | None = None

@router.post("/approve")
async def approve(d: DecisionIn):
    await publish_event("plan_decided", {"plan_id": d.plan_id, "action": d.human_action, "mod": d.modification})
    return {"ok": True}

@router.post("/reject")
async def reject(d: DecisionIn):
    await publish_event("plan_decided", {"plan_id": d.plan_id, "action": d.human_action, "note": d.note})
    return {"ok": True}