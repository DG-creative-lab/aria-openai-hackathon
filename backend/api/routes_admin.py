# backend/api/routes_admin.py
# store ablation flags in memory
from __future__ import annotations
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/admin", tags=["admin"])

# Simple in-memory flags (import where planner builds context)
ABLATION_FLAGS = {"use_docs": True, "use_lessons": True, "use_gate": True}

class Flags(BaseModel):
    use_docs: bool = True
    use_lessons: bool = True
    use_gate: bool = True

@router.post("/flags")
def set_flags(f: Flags):
    ABLATION_FLAGS.update(f.model_dict())
    return {"ok": True, **ABLATION_FLAGS}

@router.get("/flags")
def get_flags():
    return ABLATION_FLAGS