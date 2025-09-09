# backend/api/routes_playback.py
# list/start/stop/status + metrics (with path aliases)
from __future__ import annotations
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

from ..services.playback import playback


router = APIRouter(prefix="/api", tags=["playback"])  # keep existing base paths


# ---------- Schemas (Pydantic v2) ----------
class ScenarioOut(BaseModel):
    key: str
    description: Optional[str] = None
    seconds: Optional[float] = None


class StatusOut(BaseModel):
    running: bool
    scenario: str
    started_at: float


class OkOut(BaseModel):
    ok: bool = True
    scenario: Optional[str] = None


# ---------- Helpers ----------
def _scenario_exists(s: str) -> bool:
    try:
        return any(row.get("key") == s for row in playback.list_scenarios())
    except Exception:
        return False


# ---------- Endpoints (original paths) ----------
@router.get("/scenarios", response_model=List[ScenarioOut])
def scenarios() -> List[ScenarioOut]:
    return playback.list_scenarios()


@router.post("/start", response_model=OkOut)
async def start(scenario: str = Query(..., description="scenario key, e.g., normal_descent")) -> OkOut:
    if not _scenario_exists(scenario):
        raise HTTPException(status_code=404, detail=f"Scenario not found: {scenario}")
    try:
        await playback.start(scenario)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except RuntimeError as e:
        # e.g., already running
        raise HTTPException(status_code=409, detail=str(e))
    return OkOut(ok=True, scenario=scenario)

@router.post("/stop", response_model=OkOut)
async def stop() -> OkOut:
    await playback.stop()
    return OkOut(ok=True)

@router.get("/status", response_model=StatusOut)
def status() -> StatusOut:
    return StatusOut(**playback.status())

@router.get("/metrics")
def metrics():
    """Current metrics snapshot for dashboards; mirrors what SSE emits periodically."""
    return playback.metrics.snapshot()


# ---------- Aliases under /api/playback/* (non-breaking) ----------
alias = APIRouter(prefix="/api/playback", tags=["playback"])

@alias.get("/scenarios", response_model=List[ScenarioOut])
def scenarios_alias():
    return scenarios()

@alias.post("/start", response_model=OkOut)
async def start_alias(scenario: str = Query(..., description="scenario key")):
    return await start(scenario)

@alias.post("/stop", response_model=OkOut)
async def stop_alias():
    return await stop()

@alias.get("/status", response_model=StatusOut)
def status_alias():
    return status()

@alias.get("/metrics")
def metrics_alias():
    return metrics()


# Expose the alias router so app.py can include it too
playback_router_alias = alias