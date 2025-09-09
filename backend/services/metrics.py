from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional, Dict
import time

@dataclass
class RunMetrics:
    scenario: str = "unknown"
    started_at: float = 0.0
    finished_at: float = 0.0

    # core landing metrics
    peak_contact_force_n: float = 0.0
    touchdown_vz_mps: Optional[float] = None
    lateral_error_m: Optional[float] = None

    # env/approach signals useful for distillation
    max_crosswind_mps: float = 0.0               # |wind_y_mps| max over run
    flare_entry_altitude_m: Optional[float] = None  # first alt where phase=='flare'

    # runtime UX/ops
    time_to_first_plan_s: Optional[float] = None
    avg_plan_latency_ms: float = 0.0
    _plan_calls: int = 0
    _plan_latency_sum_ms: float = 0.0

    approval_rate: float = 0.0
    _decisions_total: int = 0
    _decisions_approved: int = 0

    def to_public(self) -> Dict:
        """
        Export snapshot with a compatibility-friendly shape:
         - keep all top-level fields you already had
         - add nested 'wind' and 'touchdown'
         - expose flare_entry_altitude_m and a 'min_flare_altitude_m' alias
         - expose final_vertical_speed_mps alias
        """
        d = asdict(self)
        # remove private counters
        for k in ("_plan_calls", "_plan_latency_sum_ms", "_decisions_total", "_decisions_approved"):
            d.pop(k, None)

        # aliases / bundles expected by distiller
        d["wind"] = {"max_crosswind_mps": float(self.max_crosswind_mps)}
        d["touchdown"] = {
            "vz_mps": self.touchdown_vz_mps,
            "contact_force_n": self.peak_contact_force_n,
            "lateral_error_m": self.lateral_error_m,
        }
        # Compatibility shims
        d["min_flare_altitude_m"] = self.flare_entry_altitude_m
        d["final_vertical_speed_mps"] = self.touchdown_vz_mps
        return d


class MetricsTracker:
    """
    Real-time metrics aggregator. Call:
      - start_run(scenario)
      - update_from_telem(row_dict)
      - note_plan_latency(ms)
      - record_decision(approved: bool)
      - finish_run()
    """
    def __init__(self) -> None:
        self.m = RunMetrics()
        self._touchdown_seen = False
        self._first_plan_marked = False
        self._flare_seen = False

    def reset(self, scenario: str = "unknown") -> None:
        self.__init__()
        self.m.started_at = time.time()
        self.m.scenario = scenario

    def start_run(self, scenario: str) -> None:
        self.reset(scenario)

    def finish_run(self) -> None:
        self.m.finished_at = time.time()
        # finalize averages
        if self.m._plan_calls > 0:
            self.m.avg_plan_latency_ms = round(self.m._plan_latency_sum_ms / self.m._plan_calls, 1)
        if self.m._decisions_total > 0:
            self.m.approval_rate = round(self.m._decisions_approved / self.m._decisions_total, 3)

    # ------------ updates from pipeline ------------

    def update_from_telem(self, telem: Dict) -> None:
        """
        telem should include at least:
          - 'contact_flag' (0/1)
          - 'contact_force_n'
          - 'vertical_speed_mps' (preferred) or 'vz_mps' (fallback)
          - optional: 'pos_y_m' for lateral error
          - optional: 'wind_y_mps' for crosswind tracking
          - optional: 'altitude_agl_m' and 'phase' (to detect flare entry)
        """
        # Peak contact force over the whole run
        cf = float(telem.get("contact_force_n", 0.0) or 0.0)
        if cf > self.m.peak_contact_force_n:
            self.m.peak_contact_force_n = cf

        # Track max crosswind from wind_y
        wind_y = telem.get("wind_y_mps")
        if wind_y is not None:
            ay = abs(float(wind_y) or 0.0)
            if ay > self.m.max_crosswind_mps:
                self.m.max_crosswind_mps = ay

        # Detect flare entry altitude once
        phase = str(telem.get("phase") or "").lower()
        if not self._flare_seen and phase == "flare":
            alt = telem.get("altitude_agl_m")
            if alt is not None:
                self.m.flare_entry_altitude_m = float(alt)
                self._flare_seen = True

        # Touchdown record
        contact = int(telem.get("contact_flag", 0) or 0)
        if not self._touchdown_seen and contact == 1:
            self._touchdown_seen = True
            # preferred vertical speed key (with fallback)
            vz = telem.get("vertical_speed_mps")
            if vz is None:
                vz = telem.get("vz_mps", 0.0)
            self.m.touchdown_vz_mps = float(vz or 0.0)
            if "pos_y_m" in telem and telem["pos_y_m"] is not None:
                self.m.lateral_error_m = abs(float(telem["pos_y_m"]))

    def note_plan_latency(self, latency_ms: float) -> None:
        self.m._plan_calls += 1
        self.m._plan_latency_sum_ms += max(0.0, float(latency_ms))
        if not self._first_plan_marked:
            self._first_plan_marked = True
            self.m.time_to_first_plan_s = round(time.time() - self.m.started_at, 2)

    def record_decision(self, approved: bool) -> None:
        self.m._decisions_total += 1
        if approved:
            self.m._decisions_approved += 1

    # ------------ export ------------

    def snapshot(self) -> Dict:
        """Non-final snapshot (for SSE & distillation)."""
        return self.m.to_public()