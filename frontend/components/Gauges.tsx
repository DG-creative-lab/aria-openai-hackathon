// frontend/components/Gauges.tsx
"use client";

import React from "react";
import { connectSSE, TickEvent } from "../lib/events";
import {
  LineChart, Line, XAxis, YAxis, ResponsiveContainer, Tooltip, CartesianGrid,
} from "recharts";
import { useTelemStore } from "../lib/telemetryStore";

type Props = { backendBase?: string };
type Point = { t: number; alt: number; vz: number };

// How much history to show (seconds). 30s keeps things smooth & readable.
const WINDOW_SEC = 30;

// Hard safety rails to avoid y-axis explosions from bad data/outliers.
const ALT_HARD: [number, number] = [0, 200];   // meters AGL
const VZ_HARD:  [number, number] = [-12, 2];   // m/s (down is negative)

function computeDomain(values: number[], pad = 2, hard?: [number, number]) {
  if (!values.length) return [0, 1] as const;
  let min = Math.min(...values);
  let max = Math.max(...values);
  if (!Number.isFinite(min) || !Number.isFinite(max)) return [0, 1] as const;

  // Clamp into a sensible range
  if (hard) {
    min = Math.max(hard[0], min);
    max = Math.min(hard[1], max);
  }
  if (min === max) { min -= 1; max += 1; }
  return [min - pad, max + pad] as const;
}

export default function Gauges({ backendBase = process.env.NEXT_PUBLIC_API_BASE || "" }: Props) {
  const [latest, setLatest] = React.useState<TickEvent["telem"] | null>(null);
  const [series, setSeries] = React.useState<Point[]>([]);
  const startedAtRef = React.useRef<number>(performance.now());
  const setTelem = useTelemStore((s) => s.setTelem);

  React.useEffect(() => {
    const stop = connectSSE(
      {
        tick: ({ telem }) => {
        const tsec = (performance.now() - startedAtRef.current) / 1000;

        setLatest(telem);
        setSeries(prev => {
          // Append and trim by time (not just length) to keep a strict window.
          const next = [...prev, {
            t: tsec,
            alt: telem.altitude_agl_m ?? 0,
            vz: telem.vertical_speed_mps ?? 0,
          }];
          const cutoff = tsec - WINDOW_SEC;
          // Keep points within the last WINDOW_SEC (20 Hz ≈ 600 points)
          let i = 0;
          while (i < next.length && next[i].t < cutoff) i++;
          return i > 0 ? next.slice(i) : next;
        });

        setTelem({
          t: telem.t ?? Date.now() / 1000,
          altitude_agl_m: telem.altitude_agl_m ?? 0,
          vertical_speed_mps: telem.vertical_speed_mps ?? 0,
          wind_x_mps: telem.wind_x_mps ?? 0,
          wind_y_mps: telem.wind_y_mps ?? 0,
          phase: telem.phase ?? "",
        });
        },
      },
      { base: backendBase }
    );
    return () => stop();
  }, [setTelem, backendBase]);

  // Only render the window we keep
  const data = series;

  const altVals = data.map(p => p.alt);
  const vzVals  = data.map(p => p.vz);
  const [altMin, altMax] = computeDomain(altVals, 5, ALT_HARD);
  const [vzMin,  vzMax ] = computeDomain(vzVals, 0.2, VZ_HARD);

  const alt = latest?.altitude_agl_m ?? 0;
  const vz  = latest?.vertical_speed_mps ?? 0;
  const vx  = latest?.vx_mps ?? 0;
  const vy  = latest?.vy_mps ?? 0;
  const gs  = Math.sqrt(vx * vx + vy * vy);
  const wx  = latest?.wind_x_mps ?? 0;
  const wy  = latest?.wind_y_mps ?? 0;
  const xwind = Math.abs(wy);

  const riskBadge =
    alt < 20 && vz < -6 ? "text-red-700 bg-red-50 border-red-200"
    : xwind > 8        ? "text-amber-800 bg-amber-50 border-amber-200"
                       : "text-green-800 bg-green-50 border-green-200";

  return (
    <div className="flex h-full min-h-0 flex-col space-y-3 overflow-hidden">
      {/* Stats */}
      <div className="grid grid-cols-2 xl:grid-cols-4 gap-2 md:gap-3 shrink-0">
        <Stat label="Altitude (AGL)" value={`${alt.toFixed(1)} m`} />
        <Stat label="VSpeed"        value={`${vz.toFixed(2)} m/s`} />
        <Stat label="Ground Speed"  value={`${gs.toFixed(1)} m/s`} />
        <div className={`rounded-xl border px-3 py-2 ${riskBadge}`}>
          <div className="text-xs uppercase text-gray-600">Crosswind</div>
          <div className="text-lg font-semibold">{xwind.toFixed(1)} m/s</div>
          <div className="text-[11px] text-gray-600">Wind: ({wx.toFixed(1)}, {wy.toFixed(1)}) m/s</div>
        </div>
      </div>

      {/* Chart fills remaining panel height; internal overflow prevented */}
      <div className="flex-1 min-h-[160px] overflow-hidden">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data} margin={{ top: 5, right: 10, left: 6, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis
              dataKey="t"
              tickFormatter={v => `${Math.floor(v)}s`}
              stroke="#6b7280"
              fontSize={12}
            />
            <YAxis
              yAxisId="alt"
              stroke="#3b82f6"
              domain={[altMin, altMax]}
              allowDataOverflow
              width={60}
              fontSize={12}
            />
            <YAxis
              yAxisId="vz"
              orientation="right"
              stroke="#ef4444"
              domain={[vzMin, vzMax]}
              allowDataOverflow
              width={50}
              fontSize={12}
            />
            <Tooltip
              formatter={(val: number, name: string) =>
                name === "alt" ? [`${val.toFixed(1)} m`, "Altitude"] : [`${val.toFixed(2)} m/s`, "VSpeed"]}
              labelFormatter={(l) => `${Math.floor(Number(l))} s`}
            />
            <Line
              yAxisId="alt"
              type="monotone"
              dataKey="alt"
              name="Altitude (m)"
              stroke="#3b82f6"
              dot={false}
              isAnimationActive={false}
            />
            <Line
              yAxisId="vz"
              type="monotone"
              dataKey="vz"
              name="VSpeed (m/s)"
              stroke="#ef4444"
              dot={false}
              isAnimationActive={false}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl border px-3 py-2 bg-white dark:bg-slate-900/40">
      <div className="text-xs uppercase text-gray-600 dark:text-gray-400">{label}</div>
      <div className="text-base md:text-lg font-semibold leading-tight">{value}</div>
    </div>
  );
}
