from __future__ import annotations
import os
from dataclasses import dataclass
from typing import Dict, Any, List, Optional

@dataclass
class Redlines:
    # Crosswind (m/s)
    crosswind_warn_mps: float = float(os.getenv("GATE_CROSSWIND_WARN", "6.0"))
    crosswind_max_mps:  float = float(os.getenv("GATE_CROSSWIND_MAX",  "10.0"))
    # Sink near ground (m/s) — vz is negative down; require vz >= this
    sink_near_ground_min_mps: float = float(os.getenv("GATE_SINK_NEAR_GROUND_MIN", "-6.0"))
    sink_near_ground_alt_m:   float = float(os.getenv("GATE_SINK_NEAR_GROUND_ALT",  "50"))
    # Bank limits at low altitude (deg)
    bank_low_alt_max_deg: float = float(os.getenv("GATE_BANK_LOW_ALT_MAX_DEG", "25"))
    bank_low_alt_m:       float = float(os.getenv("GATE_BANK_LOW_ALT",         "30"))
    # Flare window (m)
    flare_min_alt_m: float = float(os.getenv("GATE_FLARE_MIN_ALT", "8"))
    flare_max_alt_m: float = float(os.getenv("GATE_FLARE_MAX_ALT", "18"))

SAFE_FALLBACK_ACTION = os.getenv(
    "GATE_SAFE_FALLBACK_ACTION",
    "Stabilize approach: reduce sink ≤3 m/s, align crab, prepare flare within window."
)

def _check(name: str, ok: bool, value: Optional[float|str]=None,
           limit: Optional[float|str]=None, detail: Optional[str]=None) -> Dict[str, Any]:
    d = {"name": name, "ok": bool(ok)}
    if value is not None: d["value"] = value
    if limit is not None: d["limit"] = limit
    if detail: d["detail"] = detail
    return d

def vet_plan(plan: Dict[str, Any], state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Apply redlines/warnings to the proposed plan and adjust risk/confidence.
    If severe limits are exceeded, override to a safe fallback action.
    """
    thr = Redlines()
    checks: List[Dict[str, Any]] = list(plan.get("checks", []))

    # --- read state ---
    alt   = float(state.get("altitude_agl_m", 0.0) or 0.0)
    vz    = float(state.get("vertical_speed_mps", 0.0) or 0.0)  # negative down
    wind  = state.get("wind_xy_mps") or [0.0, 0.0]
    wind_y = float(wind[1] if len(wind) > 1 else 0.0)
    bank  = float(state.get("bank_deg", 0.0) or 0.0)
    phase = (state.get("phase") or "").lower()

    # --- crosswind ---
    xw = abs(wind_y)
    checks.append(_check("crosswind_warn",    xw <= thr.crosswind_warn_mps, round(xw,2), thr.crosswind_warn_mps))
    checks.append(_check("crosswind_redline", xw <= thr.crosswind_max_mps,  round(xw,2), thr.crosswind_max_mps))

    # --- sink near ground ---
    if alt < thr.sink_near_ground_alt_m:
        checks.append(_check(
            "sink_near_ground",
            vz >= thr.sink_near_ground_min_mps,
            round(vz,2),
            thr.sink_near_ground_min_mps,
            detail=f"alt={alt:.1f} m"
        ))

    # --- bank at low altitude ---
    if alt < thr.bank_low_alt_m:
        checks.append(_check(
            "bank_low_alt",
            abs(bank) <= thr.bank_low_alt_max_deg,
            round(bank,1),
            thr.bank_low_alt_max_deg,
            detail=f"alt={alt:.1f} m"
        ))

    # --- flare window if action/phase suggests flare ---
    action_txt = (plan.get("action") or "").lower()
    wants_flare = ("flare" in action_txt) or (phase in ("final_approach", "flare"))
    if wants_flare:
        ok_window = (thr.flare_min_alt_m <= alt <= thr.flare_max_alt_m) or phase == "flare"
        checks.append(_check(
            "flare_window",
            ok_window,
            round(alt,1),
            f"{thr.flare_min_alt_m}-{thr.flare_max_alt_m} m"
        ))

    # --- severity & adjustments ---
    severe = any((c["name"] in ("crosswind_redline","sink_near_ground","bank_low_alt")) and not c["ok"] for c in checks)
    warn   = any((c["name"] in ("crosswind_warn","flare_window")) and not c["ok"] for c in checks)

    # risk / confidence shaping
    risk = (plan.get("risk") or "").lower()
    conf = float(plan.get("confidence", 0.5))

    if severe:
        risk = "high"
        conf = max(0.2, conf * 0.6)
        # override action to safe fallback (no go-around on parafoil)
        plan["action"] = SAFE_FALLBACK_ACTION
        plan["reasoning"] = (plan.get("reasoning") or "")
        if "redline" not in plan["reasoning"].lower():
            plan["reasoning"] = (plan["reasoning"] + " Safety gate override due to redline.").strip()
    elif warn:
        if risk != "high":
            risk = "medium"
        conf = max(0.3, conf * 0.8)
    else:
        conf = min(0.95, conf * 1.05)  # small boost if all green

    plan["risk"] = risk or "medium"
    plan["confidence"] = round(conf, 2)
    plan["checks"] = checks
    return plan