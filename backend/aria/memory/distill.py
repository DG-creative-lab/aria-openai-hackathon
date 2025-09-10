# backend/aria/memory/distill.py
from __future__ import annotations
import math
from typing import Dict, Any, List
from . import store as mem_store

def _fmt(val, nd=1):
    try: return f"{float(val):.{nd}f}"
    except Exception: return str(val)

def _coalesce(*vals, default=None):
    for v in vals:
        if v is None: continue
        try:
            if isinstance(v, float) and math.isnan(v): continue
        except Exception:
            pass
        return v
    return default

def _build_title(meta: Dict[str, Any]) -> str:
    sc = meta.get("scenario") or meta.get("scenario_key") or "run"
    wind = meta.get("max_crosswind_mps") or meta.get("wind", {}).get("max_crosswind_mps")
    return f"{sc}: crosswind {_fmt(wind)} m/s — distilled lesson" if wind is not None else f"{sc}: distilled lesson"

def _derive_tags(meta: Dict[str, Any]) -> List[str]:
    tags: List[str] = ["spacerider", "lesson"]
    sc = meta.get("scenario") or meta.get("scenario_key")
    if sc: tags.append(sc)
    mxw = meta.get("max_crosswind_mps") or meta.get("wind", {}).get("max_crosswind_mps")
    if mxw is not None:
        tags.append("crosswind_high" if float(mxw) >= 6.0 else "crosswind_low")
    if meta.get("comm_blackout"): tags.append("comm_blackout")
    if meta.get("power_anomaly"): tags.append("power_anomaly")
    # de-dupe / normalize
    out = sorted({t.strip() for t in tags if t and t.strip()})
    return out

def _bullets_from_metrics(meta: Dict[str, Any]) -> List[str]:
    m = meta.get("metrics") or {}
    peak_xwind = _coalesce(m.get("wind", {}).get("max_crosswind_mps"),
                           meta.get("max_crosswind_mps"),
                           m.get("max_crosswind_mps"))
    td_vz = _coalesce(m.get("touchdown", {}).get("vz_mps"),
                      m.get("final_vertical_speed_mps"),
                      meta.get("final_vertical_speed_mps"))
    td_force = _coalesce(m.get("touchdown", {}).get("contact_force_n"),
                         meta.get("final_contact_force_n"))
    flare_alt = _coalesce(m.get("min_flare_altitude_m"),
                          meta.get("min_flare_altitude_m"), 11.0)

    redlines = m.get("redlines", {}) if isinstance(m.get("redlines"), dict) else {}
    exceeded = [k for k, v in redlines.items() if v]

    bullets: List[str] = []
    if peak_xwind is not None:
        if float(peak_xwind) >= 6.0:
            bullets.append(f"Fly extended base; align crab; verify flare window ≥{_fmt(flare_alt,0)} m in crosswind {_fmt(peak_xwind)} m/s.")
            bullets.append("Prioritize runway alignment over speed build; avoid steep bank below 30 m AGL.")
        else:
            bullets.append(f"Maintain standard pattern; set flare at ~{_fmt(flare_alt,0)} m; monitor drift.")
    else:
        bullets.append("Maintain stabilized approach; confirm flare window and drift correction.")

    if td_vz is not None:
        bullets.append(f"Target touchdown vertical speed ≥{_fmt(td_vz)} m/s (less negative) by progressive flare.")
    else:
        bullets.append("Reduce sink rate during flare to achieve soft touchdown.")

    if td_force is not None:
        bullets.append(f"Keep contact force proxy under {_fmt(td_force)} N via timely flare and reduced ground speed.")

    if meta.get("power_anomaly"):
        bullets.append("Minimize electrical load after power anomaly; preserve essential nav and comms.")
    if meta.get("comm_blackout"):
        bullets.append("Switch to lost-comm procedure; continue stabilized approach; verify runway clear on short final.")
    if exceeded:
        bullets.append(f"Review exceeded redlines: {', '.join(exceeded)}; adjust decision gates next run.")

    bullets = [b if len(b) <= 120 else (b[:117] + "…") for b in bullets]
    if len(bullets) < 4:
        bullets.append("Crosscheck winds, flare altitude, and sink trend every 2 s on final.")
    return bullets[:7]

def distill_episode_to_lesson(db_path: str, scenario_meta: Dict[str, Any]) -> int:
    """Create a semantic lesson from a finished run and store it (with embedding) via store.py."""
    title = _build_title(scenario_meta)
    body = "\n".join(f"- {b}" for b in _bullets_from_metrics(scenario_meta))
    tags = _derive_tags(scenario_meta)
    # store.lessons_insert embeds title+body and writes to lessons (+FTS)
    lesson_id = mem_store.lessons_insert(
        db_path=db_path,
        title=title,
        body=body,
        tags=tags,
        meta=scenario_meta,
        do_embed=True,
    )
    return lesson_id


