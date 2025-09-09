# backend/api/routes_events.py
from __future__ import annotations
import asyncio, json, time, contextlib
from typing import Any, AsyncGenerator, Dict, Set
from fastapi import APIRouter, Request, Response, status
from sse_starlette.sse import EventSourceResponse

router = APIRouter(prefix="/api/events", tags=["events"])

# --- Fan-out Event Bus --------------------------------------------------------

class EventBus:
    """
    Fan-out pub/sub: each subscriber gets its own queue so all
    subscribers see every message.
    """
    def __init__(self) -> None:
        self._subs: Set[asyncio.Queue[Dict[str, Any]]] = set()
        self._lock = asyncio.Lock()

    async def publish(self, type_: str, payload: Dict[str, Any]) -> None:
        msg = {"type": type_, "payload": payload, "ts": time.time()}
        async with self._lock:
            subs = list(self._subs)  # snapshot to avoid holding the lock while pushing
        for q in subs:
            try:
                q.put_nowait(msg)
            except asyncio.QueueFull:
                # drop for this slow subscriber; keep others flowing
                pass

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

# Helper for other modules:
async def publish_event(type_: str, payload: Dict[str, Any]) -> None:
    await event_bus.publish(type_, payload)

# --- SSE stream ---------------------------------------------------------------

@router.get("/stream")
async def stream(request: Request) -> EventSourceResponse:
    async def gen():
        yield {"event": "hello", "data": json.dumps({"ok": True, "ts": time.time()})}
        heartbeat_every = 10
        last_beat = time.time()

        sub = event_bus.subscribe()
        try:
            while True:
                if await request.is_disconnected():
                    break

                now = time.time()
                if now - last_beat >= heartbeat_every:
                    yield {"event": "heartbeat", "data": json.dumps({"ts": now})}
                    last_beat = now

                try:
                    item = await asyncio.wait_for(sub.__anext__(), timeout=1.0)
                    yield {"event": item["type"], "data": json.dumps(item["payload"])}
                except asyncio.TimeoutError:
                    continue
        finally:
            # best-effort unsubscribe/close of the async generator
            with contextlib.suppress(Exception):
                aclose = getattr(sub, "aclose", None)
                if aclose:
                    await aclose()

    return EventSourceResponse(gen(), media_type="text/event-stream")


@router.get("/health")
async def health() -> Response:
    return Response(status_code=status.HTTP_204_NO_CONTENT)