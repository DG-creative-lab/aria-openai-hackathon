# backend/api/routes_playback.py
# (list/start/stop/status)
from __future__ import annotations
from fastapi import APIRouter, HTTPException, Query
from .routes_events import publish_event
from ..services.playback import playback

router = APIRouter(prefix="/api", tags=["playback"])

@router.get("/scenarios")
def scenarios():
    return playback.list_scenarios()

@router.post("/start")
async def start(scenario: str = Query(..., description="scenario key, e.g., normal_descent")):
    try:
        await playback.start(scenario)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return {"ok": True, "scenario": scenario}

@router.post("/stop")
async def stop():
    await playback.stop()
    return {"ok": True}

@router.get("/status")
def status():
    return playback.status()