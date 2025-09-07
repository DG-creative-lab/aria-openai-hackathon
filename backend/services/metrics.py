# backend/services/metrics.py
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional, Dict
import math, time

@dataclass
class RunMetrics:
    scenario: str = "unknown"
    started_at: float = 0.0
    finished_at: float = 0.0

    # core landing metrics
    peak_contact_force_n: float = 0.0
    touchdown_vz_mps: Optional[float] = None
    lateral_error_m: Optional[float] = None

    # runtime UX/ops
    time_to_first_plan_s: Optional[float] = None
    avg_plan_latency_ms: float = 0.0
    _plan_calls: int = 0
    _plan_latency_sum_ms: float = 0.0

    approval_rate: float = 0.0
    _decisions_total: int = 0
    _decisions_approved: int = 0

    def to_dict(self) -> Dict:
        d = asdict(self)
        # private counters not needed outside
        d.pop("_plan_calls", None)
        d.pop("_plan_latency_sum_ms", None)
        d.pop("_decisions_total", None)
        d.pop("_decisions_approved", None)
        return d


class MetricsTracker:
    """
    Real-time metrics aggregator. Call:
      - start_run(scenario)
      - update_from_telem(row_dict)
      - note_plan_latency(ms) and mark_first_plan()
      - record_decision(approved: bool)
      - finish_run()
    """
    def __init__(self) -> None:
        self.m = RunMetrics()
        self._touchdown_seen = False
        self._first_plan_marked = False

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
          - 'vz_mps' (vertical speed)
          - 'contact_force_n'
          - optional 'pos_y_m' for lateral error
        """
        # Peak contact force over the whole run
        cf = float(telem.get("contact_force_n", 0.0))
        if cf > self.m.peak_contact_force_n:
            self.m.peak_contact_force_n = cf

        # First touchdown record
        if not self._touchdown_seen and int(telem.get("contact_flag", 0)) == 1:
            self._touchdown_seen = True
            self.m.touchdown_vz_mps = float(telem.get("vz_mps", 0.0))
            if "pos_y_m" in telem:
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
        """Non-final snapshot (for SSE)."""
        return self.m.to_dict()
    

    """
    Usage notes:
	•	Instantiate one MetricsTracker per run (or keep a singleton and .reset() for each run).
	•	Emit SSE with snapshots periodically (e.g., every second or on key changes).
    
    """