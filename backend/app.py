from fastapi import FastAPI
from backend.api.routes_events import router as events_router
from backend.api.routes_admin import router as admin_router
from backend.api.routes_plan import router as plan_router
from backend.api.routes_playback import router as playback_router
from api.routes_knowledge import router as knowledge_router



app = FastAPI()
app.include_router(events_router)
app.include_router(admin_router)
app.include_router(plan_router)
app.include_router(playback_router)
app.include_router(knowledge_router)