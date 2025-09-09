# backend/api/routes_admin.py
from __future__ import annotations
import os
from typing import Optional, Dict, Any
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/admin", tags=["admin"])

# --- State --------------------------------------------------------------------

# Simple in-memory flags (import in planner/composer, etc.)
ABLATION_FLAGS: Dict[str, bool] = {
    "use_docs": True,
    "use_lessons": True,
    "use_gate": True,
}

def _defaults() -> Dict[str, bool]:
    # If you ever want env overrides, flip these:
    # return {
    #     "use_docs": os.getenv("ABL_USE_DOCS", "1") != "0",
    #     "use_lessons": os.getenv("ABL_USE_LESSONS", "1") != "0",
    #     "use_gate": os.getenv("ABL_USE_GATE", "1") != "0",
    # }
    return {"use_docs": True, "use_lessons": True, "use_gate": True}

# --- Schemas ------------------------------------------------------------------

class FlagsState(BaseModel):
    use_docs: bool = True
    use_lessons: bool = True
    use_gate: bool = True

class FlagsPatch(BaseModel):
    # Optional fields allow partial updates
    use_docs: Optional[bool] = None
    use_lessons: Optional[bool] = None
    use_gate: Optional[bool] = None

# --- Routes -------------------------------------------------------------------

@router.get("/flags", response_model=FlagsState)
def get_flags():
    return FlagsState(**ABLATION_FLAGS)

@router.post("/flags", response_model=FlagsState)
def set_flags(patch: FlagsPatch):
    # Only apply fields the client actually sent
    updates: Dict[str, Any] = patch.model_dump(exclude_unset=True, exclude_none=True)
    ABLATION_FLAGS.update(updates)
    return FlagsState(**ABLATION_FLAGS)

@router.post("/flags/reset", response_model=FlagsState)
def reset_flags():
    ABLATION_FLAGS.clear()
    ABLATION_FLAGS.update(_defaults())
    return FlagsState(**ABLATION_FLAGS)