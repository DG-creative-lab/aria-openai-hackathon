"""
Generate Space Rider parafoil landing telemetry for 4 scenarios at 20 Hz:
- normal_descent
- crosswind_landing
- power_anomaly
- comm_blackout

Outputs CSVs to data/telemetry/ + scenario_info.json
"""

from __future__ import annotations
import argparse, json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd


# --------------------------
# Config & helpers
# --------------------------

@dataclass
class VehicleConfig:
    mass_kg: float = 1200.0               # approximate SR vehicle mass
    area_m2: float = 180.0                # parafoil area estimate
    glide_ratio: float = 4.5              # L/D
    dt: float = 0.05                      # 20 Hz
    start_alt_m: float = 5000.0
    heading_deg: float = 90.0             # approach from West to East
    flare_alt_m: float = 11.0             # target flare altitude
    max_crosswind_mps: float = 8.0        # redline guide (used for warnings)


def ou_gust(prev: np.ndarray, rng: np.random.Generator,
            theta: float, sigma: float, dt: float) -> np.ndarray:
    """Ornstein–Uhlenbeck gust update (3D)."""
    return prev + dt * (-theta * prev) + np.sqrt(dt) * sigma * rng.standard_normal(3)


def clamp(v: float, lo: float, hi: float) -> float:
    return hi if v > hi else lo if v < lo else v


def horiz_components(airspeed: float, vz: float, heading_rad: float) -> Tuple[float, float]:
    """Resolve air-velocity into ground-projected x,y given vertical sink."""
    vx_air = max(0.0, airspeed**2 - vz**2)
    v_h = np.sqrt(vx_air)  # horizontal magnitude
    return v_h * np.cos(heading_rad), v_h * np.sin(heading_rad)


def contact_force_proxy(mass_kg: float, vz: float, gain: float = 0.35) -> float:
    """Cheap proxy for peak contact force ~ mass * decel (scaled)."""
    return abs(vz) * mass_kg * 9.81 * gain


# --------------------------
# Scenario generator
# --------------------------

class SpaceRiderTelemetryGenerator:
    def __init__(self, cfg: VehicleConfig, seed: int = 42):
        self.cfg = cfg
        self.rng = np.random.default_rng(seed)

    def _phase_params(self, alt: float, scenario: str, anomaly: Dict) -> Dict:
        """Return target vs/airspeed & phase label based on altitude and scenario flags."""
        if alt > 1000:
            phase, vs, aspd = "descent", -6.0, 25.0
        elif alt > 300:
            phase, vs, aspd = "base_leg", -5.0, 22.0
        elif alt > self.cfg.flare_alt_m:
            phase, vs, aspd = "final_approach", -4.0, 20.0
        else:
            phase = "flare"
            # flare law: reduce sink to ~-2.0 m/s near ground
            frac = clamp((alt / max(1.0, self.cfg.flare_alt_m)), 0.0, 1.0)
            vs = -2.0 - 2.0 * frac   # from ~-4 at 11 m to ~-2 near 0
            aspd = 18.0

        # Scenario-specific tweaks
        if scenario == "crosswind_landing":
            if phase in ("descent", "base_leg"):
                vs -= 0.5
                aspd += 3.0
        if scenario == "power_anomaly" and anomaly.get("power"):
            aspd -= 2.0
        # keep vs realistic, not faster than airspeed magnitude
        return {"phase": phase, "target_vs": vs, "airspeed": max(12.0, aspd)}

    def _wind_vector(self, base: np.ndarray, gust: np.ndarray) -> np.ndarray:
        return base + gust

    def _row_common(self, t: float, alt: float, pos_xy: np.ndarray, vel_xyz: np.ndarray,
                    wind: np.ndarray, phase: str, system_status: str, battery_pct: float,
                    gps_sats: int, flare: bool, comm_status: str,
                    lift_coeff: float, drag_coeff: float, contact_flag: int) -> Dict:
        # derive angles
        v_air = vel_xyz - wind
        airspeed = np.linalg.norm(v_air)
        heading_rad = np.arctan2(vel_xyz[1], vel_xyz[0] + 1e-9)
        heading_deg = np.degrees(heading_rad)
        # aoa proxy: compare -vertical component to magnitude
        aoa = np.degrees(np.arctan2(max(0.0, -v_air[2]), np.linalg.norm(v_air[:2]) + 1e-6))
        # roll/yaw proxies (small random walk + crosswind compensation)
        roll_deg = clamp((wind[1] * 1.5) + self.rng.normal(0, 2.0), -20, 20)
        yaw_rate_dps = clamp(self.rng.normal(0, 2.0) + (wind[1] * 0.5), -15, 15)

        return {
            # core fields our HUD/agent expect
            "t": round(t, 3),
            "alt_agl_m": round(alt, 2),
            "vz_mps": round(vel_xyz[2], 3),
            "vx_mps": round(vel_xyz[0], 3),
            "vy_mps": round(vel_xyz[1], 3),
            "wind_x_mps": round(wind[0], 2),
            "wind_y_mps": round(wind[1], 2),
            "wind_z_mps": round(wind[2], 2),
            "aoa_deg": round(aoa, 2),
            "roll_deg": round(roll_deg, 2),
            "yaw_rate_dps": round(yaw_rate_dps, 2),
            "contact_flag": int(contact_flag),

            # richer fields kept for reasoning & UI
            "airspeed_mps": round(airspeed, 2),
            "ground_speed_mps": round(np.linalg.norm(vel_xyz[:2]), 2),
            "pos_x_m": round(pos_xy[0], 2),
            "pos_y_m": round(pos_xy[1], 2),
            "heading_deg": round(heading_deg, 1),
            "battery_pct": round(battery_pct, 1),
            "gps_satellites": int(gps_sats),
            "phase": phase,
            "system_status": system_status,
            "comm_status": comm_status,
            "lift_coeff": round(lift_coeff, 3),
            "drag_coeff": round(drag_coeff, 3),
            "contact_force_n": 0.0  # filled at touchdown
        }

    def _simulate(self, scenario: str) -> pd.DataFrame:
        cfg, rng = self.cfg, self.rng
        dt = cfg.dt
        t = 0.0
        z = cfg.start_alt_m
        pos = np.array([0.0, 0.0], dtype=float)
        heading_rad = np.radians(cfg.heading_deg)

        # base winds per scenario (x along runway, y crosswind)
        base_wind = {
            "normal_descent":          np.array([ 3.0,  1.0, 0.0]),
            "crosswind_landing":       np.array([ 2.0,  8.0, 0.0]),
            "power_anomaly":           np.array([ 4.0,  2.0, 0.0]),
            "comm_blackout":           np.array([ 3.5, -1.5, 0.0]),
        }[scenario].astype(float)

        gust = np.zeros(3, dtype=float)
        theta = 1.5
        sigma = 1.0 if scenario != "crosswind_landing" else 1.5

        battery = 100.0
        comm_status = "active"
        anomaly = {"power": False}
        blackout_started = False
        blackout_ended = False

        rows: List[Dict] = []
        last_contact_force = 0.0

        while True:
            # phase parameters
            ph = self._phase_params(z, scenario, anomaly)
            phase = ph["phase"]
            target_vs = ph["target_vs"]
            airspeed = ph["airspeed"]

            # scenario events
            if scenario == "power_anomaly" and (z < 1200.0) and not anomaly["power"]:
                anomaly["power"] = True

            # comm blackout between 800m and 200m
            if scenario == "comm_blackout":
                in_blk = 800.0 >= z >= 200.0
                if in_blk and not blackout_started:
                    comm_status, blackout_started = "lost", True
                elif (not in_blk) and blackout_started and not blackout_ended:
                    comm_status, blackout_ended = "restored", True
                elif in_blk:
                    comm_status = "lost"
                else:
                    comm_status = "active" if not blackout_started else "restored"

            # target vs + turbulence
            vs_noise = rng.normal(0, 0.3 if scenario != "crosswind_landing" else 0.5)
            vz = target_vs + vs_noise

            # heading / pattern tweaks (extend base under crosswind)
            if scenario == "crosswind_landing" and phase == "base_leg" and 800 > z > 400:
                # drift right a little to show extended base
                heading_rad = np.radians(cfg.heading_deg)  # keep final orientation
                pos[0] += 0.6  # slow lateral drift in meters per tick

            # wind with gusts (stronger below ~1 km)
            gust = ou_gust(gust, rng, theta=theta, sigma=sigma * (1.0 + 0.3 * clamp((1000.0 - z) / 1000.0, 0, 1)), dt=dt)
            wind = self._wind_vector(base_wind, gust)

            # horizontal air components
            vx_air, vy_air = horiz_components(airspeed, vz, heading_rad)

            # ground velocity = air + wind
            vx = vx_air + wind[0]
            vy = vy_air + wind[1]

            # position integration
            pos += np.array([vx, vy]) * dt
            z += vz * dt
            t += dt

            # battery model
            drain_mult = 1.0
            if scenario == "crosswind_landing":
                drain_mult = 1.2
            if anomaly.get("power"):
                drain_mult += 0.6  # faster drain after anomaly

            battery = max(5.0, battery - (dt / 300.0) * 80.0 * drain_mult)  # ~5 min horizon baseline
            gps_sats = 8
            if anomaly.get("power") and battery < 25:
                gps_sats = max(4, 8 - int((25 - battery) // 3))

            # IMU proxies
            imu_accel = np.array([
                np.clip(0.2 + self.rng.normal(0, 0.1), -2, 2),
                np.clip((wind[1] / 10.0) + self.rng.normal(0, 0.08), -2, 2),
                np.clip(-9.81 + self.rng.normal(0, 0.2), -20, -5)
            ])
            imu_gyro = np.array([
                self.rng.normal(0.0, 0.03 if scenario != "crosswind_landing" else 0.06),
                self.rng.normal(0.0, 0.02),
                self.rng.normal(wind[1] / 20.0, 0.03)
            ])

            # aero coeffs (slightly higher CL in flare; higher CD in wind)
            lift_coeff = (0.8 if phase != "flare" else 1.2) - (0.1 if anomaly.get("power") else 0.0)
            drag_coeff = (0.15 if scenario != "crosswind_landing" else 0.18)

            # statuses
            system_status = "nominal"
            if scenario == "crosswind_landing" and np.linalg.norm(wind[:2]) > cfg.max_crosswind_mps:
                system_status = "wind_warning"
            if anomaly.get("power"):
                system_status = ("emergency_power" if battery <= 20 else
                                 "power_critical" if battery <= 40 else
                                 "power_reduced")

            # pack row
            row = self._row_common(
                t=t,
                alt=z,
                pos_xy=pos,
                vel_xyz=np.array([vx, vy, vz]),
                wind=wind,
                phase=phase,
                system_status=system_status,
                battery_pct=battery,
                gps_sats=gps_sats,
                flare=(phase == "flare"),
                comm_status=comm_status,
                lift_coeff=lift_coeff,
                drag_coeff=drag_coeff,
                contact_flag=0
            )

            # IMU fields (keep your originals; useful for agents)
            row.update({
                "imu_accel_x": round(float(imu_accel[0]), 3),
                "imu_accel_y": round(float(imu_accel[1]), 3),
                "imu_accel_z": round(float(imu_accel[2]), 3),
                "imu_gyro_x": round(float(imu_gyro[0]), 3),
                "imu_gyro_y": round(float(imu_gyro[1]), 3),
                "imu_gyro_z": round(float(imu_gyro[2]), 3),
            })

            # touchdown handling
            if z <= 0.0:
                row["alt_agl_m"] = 0.0
                row["contact_flag"] = 1
                row["contact_force_n"] = round(contact_force_proxy(self.cfg.mass_kg, row["vz_mps"]), 2)
                last_contact_force = row["contact_force_n"]
                rows.append(row)
                # a short settle window (~2 s) with decaying speeds
                settle_steps = int(2.0 / dt)
                for i in range(settle_steps):
                    t += dt
                    rows.append({
                        **row,
                        "t": round(t, 3),
                        "vz_mps": 0.0,
                        "vx_mps": round(row["vx_mps"] * (1.0 - (i + 1) / settle_steps), 3),
                        "vy_mps": round(row["vy_mps"] * (1.0 - (i + 1) / settle_steps), 3),
                        "ground_speed_mps": round(max(0.0, row["ground_speed_mps"] * (1.0 - (i + 1) / settle_steps)), 2)
                    })
                break

            rows.append(row)

        df = pd.DataFrame(rows)
        # metric convenience
        df["scenario"] = scenario
        df["ld_ratio"] = (df["ground_speed_mps"] / (np.abs(df["vz_mps"]) + 1e-6)).round(2)
        # ensure columns order (core first)
        core = ["t","alt_agl_m","vz_mps","vx_mps","vy_mps","wind_x_mps","wind_y_mps","wind_z_mps",
                "aoa_deg","roll_deg","yaw_rate_dps","contact_flag"]
        extras = [c for c in df.columns if c not in core]
        df = df[core + extras]
        # store last contact force for metadata
        df.attrs["final_contact_force_n"] = last_contact_force
        return df

    # Public scenarios
    def generate_normal_descent(self) -> pd.DataFrame:
        return self._simulate("normal_descent")

    def generate_crosswind_landing(self) -> pd.DataFrame:
        return self._simulate("crosswind_landing")

    def generate_power_anomaly(self) -> pd.DataFrame:
        return self._simulate("power_anomaly")

    def generate_comm_blackout(self) -> pd.DataFrame:
        return self._simulate("comm_blackout")


# --------------------------
# CLI
# --------------------------

SCENARIOS = [
    ("normal_descent",      "Nominal parafoil landing with light winds"),
    ("crosswind_landing",   "High crosswind approach requiring extended pattern"),
    ("power_anomaly",       "Power system failure during descent phase"),
    ("comm_blackout",       "Communication loss during critical approach"),
]


def main():
    parser = argparse.ArgumentParser(description="Generate Space Rider telemetry CSVs (20 Hz).")
    parser.add_argument("--outdir", default="data/telemetry", help="Output directory")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed")
    parser.add_argument("--start-alt", type=float, default=5000.0, help="Start altitude meters AGL")
    parser.add_argument("--dt", type=float, default=0.05, help="Timestep seconds (default 0.05 = 20 Hz)")
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    cfg = VehicleConfig(start_alt_m=args.start_alt, dt=args.dt)
    gen = SpaceRiderTelemetryGenerator(cfg, seed=args.seed)

    print("Generating Space Rider telemetry scenarios…")
    info = {}

    for key, desc in SCENARIOS:
        method = {
            "normal_descent": gen.generate_normal_descent,
            "crosswind_landing": gen.generate_crosswind_landing,
            "power_anomaly": gen.generate_power_anomaly,
            "comm_blackout": gen.generate_comm_blackout,
        }[key]

        df = method()
        fname = outdir / f"landing_{key}.csv"
        df.to_csv(fname, index=False)

        # metadata
        duration_s = float(df["t"].iloc[-1] - df["t"].iloc[0])
        key_events = sorted([s for s in df["system_status"].unique().tolist() if s != "nominal"])
        info[key] = {
            "description": desc,
            "duration_seconds": round(duration_s, 1),
            "rows": int(len(df)),
            "timestep_s": cfg.dt,
            "max_altitude_m": float(df["alt_agl_m"].max()),
            "final_contact_force_n": float(df.attrs.get("final_contact_force_n", 0.0)),
            "wind_summary_mps": {
                "max_abs_xy": float(np.max(np.abs(df[["wind_x_mps","wind_y_mps"]].values))),
                "mean_x": float(df["wind_x_mps"].mean()),
                "mean_y": float(df["wind_y_mps"].mean())
            },
            "non_nominal_states": key_events
        }

        print(f"  • {fname.name}: {desc}")
        print(f"    - rows: {len(df)}  (~{duration_s:.1f}s)")
        print(f"    - phases: {df['phase'].unique().tolist()}")
        print(f"    - states: {sorted(df['system_status'].unique().tolist())}")

    with open(outdir / "scenario_info.json", "w") as f:
        json.dump(info, f, indent=2)

    print(f"\nWrote metadata → {outdir/'scenario_info.json'}")
    print("Done.")

if __name__ == "__main__":
    main()