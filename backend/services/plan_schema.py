# backend/services/plan_schema.py  (Pydantic v2 only)

from __future__ import annotations
from enum import Enum
from typing import Any, Dict, List, Sequence, Union

from pydantic import BaseModel, Field, ConfigDict, field_validator, model_validator


class RiskLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Check(BaseModel):
    model_config = ConfigDict(extra="allow")
    name: str = Field(..., description="Short label for the check")
    ok: bool = True
    details: str | None = None

    @model_validator(mode="before")
    @classmethod
    def _coerce_from_str(cls, v: Any) -> Any:
        # allow "bank<30" -> {"name":"bank<30","ok":True}
        if isinstance(v, str):
            return {"name": v, "ok": True}
        return v


class Plan(BaseModel):
    """Canonical plan payload for SSE/UI/safety gate."""
    model_config = ConfigDict(extra="allow")

    id: str = "plan"
    action: str
    reasoning: str = ""
    risk: RiskLevel = RiskLevel.medium
    confidence: float = 0.5
    phase: str = "descent"
    references: List[str] = Field(default_factory=list)   # ["lessons","facts","qa","docs"]
    checks: List[Check] = Field(default_factory=list)
    callouts: List[str] | None = None

    # ---- field validators (v2) ----

    @field_validator("confidence", mode="before")
    @classmethod
    def _clamp_conf(cls, v: Any) -> float:
        try:
            x = float(v)
        except Exception:
            return 0.5
        return 0.0 if x < 0 else 1.0 if x > 1 else x

    @field_validator("reasoning", mode="before")
    @classmethod
    def _trim_reason(cls, v: Any) -> str:
        s = (str(v or "")).strip()
        return s if len(s) <= 400 else (s[:397] + "…")

    @field_validator("action", mode="before")
    @classmethod
    def _norm_action(cls, v: Any) -> str:
        s = (str(v or "")).strip() or "Hold pattern"
        return s if len(s) <= 160 else (s[:157] + "…")

    @field_validator("references", mode="before")
    @classmethod
    def _dedupe_refs(cls, v: Any) -> List[str]:
        if not isinstance(v, list):
            return []
        seen, out = set(), []
        for x in v:
            if isinstance(x, str) and x not in seen:
                seen.add(x); out.append(x)
        return out[:8]

    @field_validator("risk", mode="before")
    @classmethod
    def _norm_risk(cls, v: Any) -> RiskLevel | str:
        r = str(v or "").lower()
        if "low" in r or "green" in r:
            return "low"
        if "high" in r or "red" in r:
            return "high"
        return "medium"

    # optional whole-model pre-clean (runs once)
    @model_validator(mode="before")
    @classmethod
    def _pre_clean(cls, data: Any) -> Any:
        # ensure we always have a string action; keep short
        if isinstance(data, dict):
            act = (str(data.get("action") or "")).strip()
            if not act:
                data["action"] = "Hold pattern"
        return data


# ---------- helpers (v2) ----------

def ensure_plan(raw: Union[Plan, Dict[str, Any]]) -> Dict[str, Any]:
    """Validate/normalize a raw plan dict to a stable payload."""
    if isinstance(raw, Plan):
        return raw.model_dump()
    return Plan(**(raw or {})).model_dump()

def summarize_plan(plan: Union[Plan, Dict[str, Any]]) -> str:
    p = plan if isinstance(plan, dict) else plan.model_dump()
    action = (p.get("action") or "").strip()
    conf = p.get("confidence")
    phase = p.get("phase") or ""
    risk = p.get("risk") or "medium"
    try:
        c = float(conf); conf_txt = f"{c:.2f}"
    except Exception:
        conf_txt = "0.50"
    return f"{action} | phase={phase} risk={risk} conf={conf_txt}"

def dump(model: BaseModel) -> Dict[str, Any]:
    return model.model_dump()