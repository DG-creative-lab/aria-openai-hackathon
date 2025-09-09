# backend/api/routes_plan.py
from __future__ import annotations
from enum import Enum
from typing import Optional, List, Dict, Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

from .routes_events import publish_event
from ..services.playback import playback as playback_service  # to update MetricsTracker
from ..aria.memory.store import episodic_append               # episodic_log write

router = APIRouter(prefix="/api/plan", tags=["plan"])

# ---- schema (v2-friendly) ----
class HumanAction(str, Enum):
    approved = "approved"
    modified = "modified"
    rejected = "rejected"

class PlanPatch(BaseModel):
    # Optional partial overrides of the plan (UI-driven edits)
    action: Optional[str] = None
    reasoning: Optional[str] = None
    risk: Optional[str] = Field(None, pattern="^(low|medium|high)$")
    confidence: Optional[float] = Field(None, ge=0.0, le=1.0)
    checks: Optional[List[str]] = None
    references: Optional[List[str]] = None

class DecisionIn(BaseModel):
    plan_id: str = Field(..., min_length=1)
    human_action: HumanAction
    modification: Optional[PlanPatch] = None
    note: Optional[str] = None

# ---- unified endpoint ----
@router.post("/decision")
async def decide(d: DecisionIn):
    # 1) Update run metrics (approved vs not)
    try:
        playback_service.metrics.record_decision(approved=(d.human_action is HumanAction.approved))
    except Exception:
        # best-effort; don't fail the request
        pass

    # 2) Log to episodic memory
    try:
        episodic_append(
            db_path="data/aria.sqlite",  # keep in sync with playback
            kind="decision",
            text=f"human_{d.human_action.value}",
            data={
                "plan_id": d.plan_id,
                "modification": d.modification.model_dump() if d.modification else None,
                "note": d.note,
            },
        )
    except Exception:
        pass

    # 3) Notify UI via SSE
    payload: Dict[str, Any] = {
        "plan_id": d.plan_id,
        "action": d.human_action.value,
        "mod": d.modification.model_dump() if d.modification else None,
        "note": d.note,
    }
    await publish_event("plan_decided", payload)
    return {"ok": True}

# ---- compatibility shims (keep your current callers working) ----
@router.post("/approve")
async def approve(d: DecisionIn):
    if d.human_action not in (HumanAction.approved, HumanAction.modified, HumanAction.rejected):
        # if a caller sends arbitrary text here, force 'approved'
        d = DecisionIn(plan_id=d.plan_id, human_action=HumanAction.approved,
                       modification=d.modification, note=d.note)
    else:
        d = DecisionIn(plan_id=d.plan_id, human_action=HumanAction.approved,
                       modification=d.modification, note=d.note)
    return await decide(d)

@router.post("/reject")
async def reject(d: DecisionIn):
    d = DecisionIn(plan_id=d.plan_id, human_action=HumanAction.rejected,
                   modification=d.modification, note=d.note)
    return await decide(d)
