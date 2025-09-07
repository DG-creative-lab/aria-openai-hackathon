# backend/api/routes_events.py
from __future__ import annotations
import asyncio, json, time
from typing import Any, AsyncGenerator, Dict
from fastapi import APIRouter, Request, Response, status
from sse_starlette.sse import EventSourceResponse

router = APIRouter(prefix="/api/events", tags=["events"])

# --- Tiny in-process event bus (pub/sub via asyncio.Queue) --------------------

class EventBus:
    def __init__(self) -> None:
        self._q: "asyncio.Queue[Dict[str, Any]]" = asyncio.Queue()

    async def publish(self, type_: str, payload: Dict[str, Any]) -> None:
        await self._q.put({"type": type_, "payload": payload, "ts": time.time()})

    async def subscribe(self) -> AsyncGenerator[Dict[str, Any], None]:
        while True:
            item = await self._q.get()
            yield item

event_bus = EventBus()

# Helper for other modules:
async def publish_event(type_: str, payload: Dict[str, Any]) -> None:
    """Import this in playback/planner/metrics to emit events."""
    await event_bus.publish(type_, payload)

# --- SSE stream ---------------------------------------------------------------

@router.get("/stream")
async def stream(request: Request) -> EventSourceResponse:
    """
    Server-Sent Events stream that pushes tick/anomaly/plan/decision/metrics.
    """
    async def gen():
        # Immediately send a hello/heartbeat so the UI connects cleanly.
        yield {"event": "hello", "data": json.dumps({"ok": True, "ts": time.time()})}
        # Heartbeat cadence (s)
        heartbeat_every = 10
        last_beat = time.time()

        sub = event_bus.subscribe()
        while True:
            # Stop if client disconnected
            if await request.is_disconnected():
                break

            # Non-blocking heartbeat
            now = time.time()
            if now - last_beat >= heartbeat_every:
                yield {"event": "heartbeat", "data": json.dumps({"ts": now})}
                last_beat = now

            try:
                item = await asyncio.wait_for(sub.__anext__(), timeout=1.0)
                yield {
                    "event": item["type"],
                    "data": json.dumps(item["payload"]),
                }
            except asyncio.TimeoutError:
                # idle loop, keep connection alive
                continue

    return EventSourceResponse(gen(), media_type="text/event-stream")


# --- Optional: minimal health endpoint (handy for reverse proxy checks) -------

@router.get("/health")
async def health() -> Response:
    return Response(status_code=status.HTTP_204_NO_CONTENT)


"""

# How to use 
from backend.api.routes_events import publish_event
await publish_event("tick", {"t": t, "alt": alt})

"""