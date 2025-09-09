# backend/app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes_events import router as events_router
from backend.api.routes_admin import router as admin_router
from backend.api.routes_plan import router as plan_router
from backend.api.routes_playback import router as playback_router
from backend.api.routes_knowledge import router as knowledge_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(events_router)
app.include_router(admin_router)
app.include_router(plan_router)
app.include_router(playback_router)
app.include_router(knowledge_router)