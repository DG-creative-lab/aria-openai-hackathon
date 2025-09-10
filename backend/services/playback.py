# CSV → 20 Hz playback + 1 Hz planner + SSE + metrics
from __future__ import annotations

import asyncio, time, json, os, sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, Any, List

import pandas as pd

from ..api.routes_events import publish_event
from ..api.routes_admin import ABLATION_FLAGS
from .metrics import MetricsTracker
from . import planner as planner_mod  # expects planner.tick(...)
from ..aria.memory import store as mem_store
from ..aria.memory.distill import distill_episode_to_lesson

# NEW: event detector
from .events import EventDetector

DATA_DIR = Path("data/telemetry")
DB_PATH  = Path("data/aria.sqlite")

# Toggle: distill an episode into a lesson after each run
DISTILL_AFTER_RUN = os.getenv("DISTILL_AFTER_RUN", "1") != "0"


@dataclass
class RunState:
    scenario_key: str = ""
    task: Optional[asyncio.Task] = None
    running: bool = False
    started_at: float = 0.0


class PlaybackService:
    """
    Streams telemetry rows at realtime (20 Hz), fires 1 Hz planner ticks,
    updates MetricsTracker, and emits SSE events:
      - 'tick'            : telemetry row (sparse, per 50 ms)
      - 'plan_proposed'   : plan JSON once per second (or on anomaly)
      - 'metrics_update'  : snapshot periodically + final at end
      - 'anomaly'         : simple anomaly events (e.g., high crosswind)
    """
    def __init__(self):
        self.state = RunState()
        self.metrics = MetricsTracker()
        self._stop_evt = asyncio.Event()
        self.events = EventDetector()  # NEW

    # ---------- tiny episodic logger ----------
    def _elog(self, ts: float, kind: str, text: str, data: Optional[dict] = None) -> None:
        """Append a sparse episodic row via the central store helper."""
        try:
            mem_store.episodic_append(
                db_path=str(DB_PATH),
                kind=kind,
                text=text,
                data=data or {},
                ts=float(ts),
            )
        except Exception as e:
            print(f"[episodic_log] warn: {e}")

    def list_scenarios(self) -> List[Dict[str, Any]]:
        info_file = DATA_DIR / "scenario_info.json"
        rows = []
        if info_file.exists():
            try:
                meta = json.loads(info_file.read_text())
                for key, v in meta.items():
                    rows.append({"key": key, "description": v["description"], "seconds": v["duration_seconds"]})
            except Exception:
                pass

        # fallback to csv discovery
        for p in sorted(DATA_DIR.glob("landing_*.csv")):
            key = p.stem.replace("landing_", "")
            if not any(r["key"] == key for r in rows):
                rows.append({"key": key, "description": key.replace("_", " ").title(), "seconds": None})
        return rows

    async def start(self, scenario_key: str):
        if self.state.running:
            raise RuntimeError("Playback already running")
        csv_path = DATA_DIR / f"landing_{scenario_key}.csv"
        if not csv_path.exists():
            raise FileNotFoundError(f"Scenario CSV not found: {csv_path}")

        # ensure DB exists + initialized
        mem_store.ensure_db(DB_PATH)

        self._stop_evt = asyncio.Event()
        self.state = RunState(scenario_key=scenario_key, running=True, started_at=time.time())
        self.metrics.start_run(scenario_key)

        self.state.task = asyncio.create_task(self._run(csv_path))

    async def stop(self):
        # idempotent stop
        if not self.state.running:
            self.state = RunState()
            return
        self._stop_evt.set()
        if self.state.task:
            try:
                await self.state.task
            except asyncio.CancelledError:
                pass
            except Exception:
                # don't propagate; we'll reset state anyway
                pass
        self.state = RunState()

    def status(self) -> Dict[str, Any]:
        return {
            "running": self.state.running,
            "scenario": self.state.scenario_key,
            "started_at": self.state.started_at,
        }

    # ------------------ internal loop ------------------

    async def _run(self, csv_path: Path):
        # load CSV (expects columns from generator)
        df = pd.read_csv(csv_path)
        # infer dt from timestamps 't' if present; else assume 0.05
        dt = float(df["t"].diff().median()) if "t" in df.columns else 0.05
        last_tick_planner = -1.0

        # broadcast start
        await publish_event("run_started", {"scenario": self.state.scenario_key, "dt": dt})
        # episodic: run start
        self._elog(0.0, "event", f"run_started:{self.state.scenario_key}", {"dt": dt})

        started = time.perf_counter()
        for i, row in df.iterrows():
            if self._stop_evt.is_set():
                break

            # emit telemetry tick (subset for UI)
            telem = self._row_to_telem(row)
            await publish_event("tick", {"telem": telem})

            # update metrics from telemetry
            self.metrics.update_from_telem({**telem, "pos_y_m": row.get("pos_y_m", 0.0)})

            # NEW: unified event detection
            for ev in self.events.update(telem):
                # publish and log
                if ev["kind"] in ("crosswind_high", "descent_rate_high_near_ground"):
                    asyncio.create_task(publish_event("anomaly", ev))
                else:
                    asyncio.create_task(publish_event("event", ev))
                self._elog(telem["t"], "event", ev["kind"], ev)

            # planner tick @ 1 Hz (based on CSV 't' if exists)
            t_now = float(row["t"]) if "t" in row else (i * dt)
            if last_tick_planner < 0 or (t_now - last_tick_planner) >= 1.0:
                last_tick_planner = t_now
                # build state summary + query
                state_summary_dict, query = self._summarize_for_planner(row)
                t0 = time.perf_counter()
                plan = await planner_mod.tick(
                    db_path=str(DB_PATH),
                    state_summary=state_summary_dict,
                    query=query,
                    ablations=dict(ABLATION_FLAGS),
                )
                latency_ms = (time.perf_counter() - t0) * 1000.0
                self.metrics.note_plan_latency(latency_ms)
                await publish_event("plan_proposed", plan)
                # episodic: decision
                plan_text = (
                    plan.get("title")
                    or plan.get("summary")
                    or plan.get("decision_text")
                    or "plan_proposed"
                )
                self._elog(t_now, "decision", str(plan_text), plan)
                # periodic metrics snapshot
                await publish_event("metrics_update", self.metrics.snapshot())

            # maintain realtime cadence
            elapsed_wall = time.perf_counter() - started
            target_wall = (i + 1) * dt
            sleep_s = max(0.0, target_wall - elapsed_wall)
            await asyncio.sleep(sleep_s)

        # finalize
        snap = self.metrics.snapshot()
        self.metrics.finish_run()
        await publish_event("metrics_update", snap)
        await publish_event("run_finished", {"scenario": self.state.scenario_key})
        # episodic: outcome
        last_t = float(df["t"].iloc[-1]) if "t" in df.columns else (len(df) * dt)
        self._elog(last_t, "outcome", f"run_finished:{self.state.scenario_key}", snap)

        # optional distillation step
        if DISTILL_AFTER_RUN:
            try:
                meta_path = DATA_DIR / "scenario_info.json"
                scenario_meta = {"scenario_key": self.state.scenario_key, "metrics": snap}
                if meta_path.exists():
                    try:
                        info = json.loads(meta_path.read_text())
                        if self.state.scenario_key in info:
                            scenario_meta["scenario_info"] = info[self.state.scenario_key]
                    except Exception:
                        pass
                lesson_id = distill_episode_to_lesson(str(DB_PATH), scenario_meta)
                await publish_event("distilled_lesson", {"lesson_id": lesson_id, "scenario": self.state.scenario_key})
            except Exception as e:
                print(f"[distill] warn: {e}")

        self.state.running = False

    def _row_to_telem(self, row) -> Dict[str, Any]:
        def get(row, keys, default=0.0):
            for k in keys:
                if k in row and pd.notna(row[k]):
                    return row[k]
            return default

        return {
            "t": float(get(row, ["t", "timestamp"], 0.0)),
            "altitude_agl_m": float(get(row, ["alt_agl_m","altitude_agl_m","alt_m","altitude_m"], 0.0)),
            "vertical_speed_mps": float(get(row, ["vz_mps","vertical_speed_mps","descent_rate_mps"], 0.0)),
            "vx_mps": float(get(row, ["vx_mps","ground_speed_mps","airspeed_mps"], 0.0)),
            "vy_mps": float(get(row, ["vy_mps"], 0.0)),
            "wind_x_mps": float(get(row, ["wind_x_mps","wind_x"], 0.0)),
            "wind_y_mps": float(get(row, ["wind_y_mps","wind_y"], 0.0)),
            "contact_flag": int(get(row, ["contact_flag"], 0)),
            "contact_force_n": float(get(row, ["contact_force_n"], 0.0)),
            "phase": str(get(row, ["phase"], "")),
            # NEW: pass through comm status for eventing if present in CSV
            "comm_status": (str(row.get("comm_status", "")) or None),
        }

    def _summarize_for_planner(self, row) -> tuple[Dict[str, Any], str]:
        # Dict summary for safety gate and prompt composer
        state = {
            "altitude_agl_m": float(row["alt_agl_m"]),
            "vertical_speed_mps": float(row["vz_mps"]),
            "wind_xy_mps": [float(row["wind_x_mps"]), float(row["wind_y_mps"])],
            "phase": str(row.get("phase", "")),
        }
        # crude bank proxy if roll present
        if "roll_deg" in row:
            state["bank_deg"] = float(row["roll_deg"])
        # Query for retrieval based on phase & wind
        wind_abs = (abs(state["wind_xy_mps"][0]) + abs(state["wind_xy_mps"][1]))
        if state["phase"] in ("final_approach", "flare"):
            if wind_abs > 6.0:
                query = "crosswind landing flare window procedure"
            else:
                query = "final approach flare window procedure"
        else:
            query = "descent pattern and base leg wind limits"
        return state, query


# Singleton
playback = PlaybackService()
