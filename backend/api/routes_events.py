# backend/api/routes_events.py
from __future__ import annotations
import asyncio, json, time, contextlib
from typing import Any, AsyncGenerator, Dict, Set
from fastapi import APIRouter, Request, Response, status
from sse_starlette.sse import EventSourceResponse

router = APIRouter(prefix="/api/events", tags=["events"])

# ---------- Fan-out bus (unchanged behavior) ----------
class EventBus:
    def __init__(self) -> None:
        self._subs: Set[asyncio.Queue[Dict[str, Any]]] = set()
        self._lock = asyncio.Lock()

    async def publish(self, type_: str, payload: Dict[str, Any]) -> None:
        msg = {"type": type_, "payload": payload, "ts": time.time()}
        async with self._lock:
            subs = list(self._subs)
        for q in subs:
            try:
                q.put_nowait(msg)
            except asyncio.QueueFull:
                # drop for slow subscriber
                pass

    # Async generator subscription (used internally by a pump task)
    async def subscribe(self) -> AsyncGenerator[Dict[str, Any], None]:
        q: asyncio.Queue[Dict[str, Any]] = asyncio.Queue(maxsize=1024)
        async with self._lock:
            self._subs.add(q)
        try:
            while True:
                item = await q.get()
                yield item
        finally:
            async with self._lock:
                self._subs.discard(q)


event_bus = EventBus()


async def publish_event(type_: str, payload: Dict[str, Any]) -> None:
    await event_bus.publish(type_, payload)


# ---------- SSE stream (robust) ----------
@router.get("/stream")
async def stream(request: Request) -> EventSourceResponse:
    """
    Stable SSE stream:
      - pumps the bus into a local queue
      - yields heartbeats when idle
      - closes cleanly on client disconnect
    """
    async def event_generator():
        # initial hello so clients know we're up
        yield {"event": "hello", "data": json.dumps({"ok": True, "ts": time.time()})}

        # pump bus -> queue; keep it isolated from the HTTP generator
        queue: asyncio.Queue[Dict[str, Any]] = asyncio.Queue(maxsize=2048)

        async def pump():
            async for item in event_bus.subscribe():
                with contextlib.suppress(asyncio.QueueFull):
                    await queue.put(item)

        pump_task = asyncio.create_task(pump())

        try:
            while True:
                if await request.is_disconnected():
                    break
                try:
                    item = await asyncio.wait_for(queue.get(), timeout=10.0)
                    yield {"event": item["type"], "data": json.dumps(item["payload"])}
                except asyncio.TimeoutError:
                    # no events: send heartbeat to keep proxies happy
                    yield {"event": "heartbeat", "data": json.dumps({"ts": time.time()})}
        finally:
            pump_task.cancel()
            with contextlib.suppress(Exception):
                await pump_task

    return EventSourceResponse(event_generator(), media_type="text/event-stream")

@router.get("/health")
async def health() -> Response:
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Optional: tiny debug emitter so you can poke the stream without playback
@router.post("/test-ping")
async def test_ping():
    await publish_event("tick", {"telem": {"altitude_agl_m": 12.3, "vertical_speed_mps": -1.1}})
    return {"ok": True}