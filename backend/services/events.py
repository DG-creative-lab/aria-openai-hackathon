# backend/services/events.py
from __future__ import annotations
import os
from dataclasses import dataclass
from typing import Dict, Any, List, Optional

@dataclass
class Thresholds:
    crosswind_high: float = float(os.getenv("EVT_XWIND_HIGH", "8.0"))
    sink_near_ground: float = float(os.getenv("EVT_SINK_NEAR_GROUND", "-6.5"))
    sink_alt_limit_m: float = float(os.getenv("EVT_SINK_ALT_LIMIT_M", "50"))

class EventDetector:
    """
    Call update(telem) each tick; returns a list of event dicts.
    telem keys expected: t, altitude_agl_m, vertical_speed_mps, wind_y_mps,
                         phase, comm_status, contact_flag, contact_force_n.
    """
    def __init__(self, thresholds: Optional[Thresholds] = None):
        self.thr = thresholds or Thresholds()
        self._last_phase: Optional[str] = None
        self._last_comm: Optional[str]  = None
        self._last_contact: int = 0

    def update(self, telem: Dict[str, Any]) -> List[Dict[str, Any]]:
        events: List[Dict[str, Any]] = []

        # Crosswind anomaly
        wind_y = float(telem.get("wind_y_mps", 0.0))
        if abs(wind_y) > self.thr.crosswind_high:
            events.append({"kind": "crosswind_high", "wind_y": wind_y})

        # High sink near ground anomaly
        vz  = float(telem.get("vertical_speed_mps", 0.0))
        alt = float(telem.get("altitude_agl_m", 0.0))
        if vz < self.thr.sink_near_ground and alt < self.thr.sink_alt_limit_m:
            events.append({"kind": "descent_rate_high_near_ground", "vz": vz, "alt": alt})

        # Phase change
        phase = telem.get("phase")
        if phase and phase != self._last_phase:
            if self._last_phase is not None:
                events.append({"kind": "phase_change", "from": self._last_phase, "to": phase})
            self._last_phase = phase

        # Comm status change
        comm = telem.get("comm_status")
        if comm and comm != self._last_comm:
            if self._last_comm is not None:
                events.append({"kind": "comm_status", "from": self._last_comm, "to": comm})
            self._last_comm = comm

        # Touchdown moment
        contact = int(telem.get("contact_flag", 0))
        if contact and not self._last_contact:
            events.append({
                "kind": "touchdown",
                "contact_force_n": float(telem.get("contact_force_n", 0.0)),
            })
        self._last_contact = contact

        return events