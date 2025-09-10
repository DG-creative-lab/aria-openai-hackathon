// frontend/components/Gauges.tsx
"use client";

import React from "react";
import { connectSSE, TickEvent } from "../lib/events";
import {
  LineChart, Line, XAxis, YAxis, ResponsiveContainer, Tooltip, CartesianGrid, Legend,
} from "recharts";
// NEW: import the store
import { useTelemStore } from "../lib/telemetryStore";

type Props = { backendBase?: string };
type Point = { t: number; alt: number; vz: number };

export default function Gauges(_props: Props) {
  const [latest, setLatest] = React.useState<TickEvent["telem"] | null>(null);
  const [series, setSeries] = React.useState<Point[]>([]);
  const startedAtRef = React.useRef<number>(performance.now());

  // NEW: get the setter from the store
  const setTelem = useTelemStore((s) => s.setTelem);

  React.useEffect(() => {
    const stop = connectSSE({
      tick: ({ telem }) => {
        setLatest(telem);
        setSeries(prev => {
          const tsec = (performance.now() - startedAtRef.current) / 1000;
          const next = [...prev, { t: tsec, alt: telem.altitude_agl_m, vz: telem.vertical_speed_mps }];
          if (next.length > 1200) next.shift(); // ~60s @20Hz
          return next;
        });

        // NEW: publish latest tick to the global telemetry store
        setTelem({
          t: telem.t ?? Date.now() / 1000,
          altitude_agl_m: telem.altitude_agl_m ?? 0,
          vertical_speed_mps: telem.vertical_speed_mps ?? 0,
          wind_x_mps: telem.wind_x_mps ?? 0,
          wind_y_mps: telem.wind_y_mps ?? 0,
          phase: telem.phase ?? "",
        });
      },
    });
    return () => stop();
  }, [setTelem]);

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
    <div className="flex h-full min-h-0 flex-col space-y-3">
      {/* Stats */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
        <Stat label="Altitude (AGL)" value={`${alt.toFixed(1)} m`} />
        <Stat label="VSpeed"        value={`${vz.toFixed(2)} m/s`} />
        <Stat label="Ground Speed"  value={`${gs.toFixed(1)} m/s`} />
        <div className={`rounded-xl border px-3 py-2 ${riskBadge}`}>
          <div className="text-xs uppercase text-gray-600">Crosswind</div>
          <div className="text-lg font-semibold">{xwind.toFixed(1)} m/s</div>
          <div className="text-[11px] text-gray-600">Wind: ({wx.toFixed(1)}, {wy.toFixed(1)}) m/s</div>
        </div>
      </div>

      {/* Chart fills remaining height */}
      <div className="flex-1 min-h-[220px]">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={series}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="t" tickFormatter={v => `${Math.floor(v)}s`} stroke="#6b7280" fontSize={12} />
            <YAxis yAxisId="alt" stroke="#3b82f6" domain={["dataMin - 10", "dataMax + 10"]} width={60} fontSize={12}/>
            <YAxis yAxisId="vz"  orientation="right" stroke="#ef4444" width={50} fontSize={12}/>
            <Tooltip
              formatter={(val: number, name: string) =>
                name === "alt" ? [`${val.toFixed(1)} m`, "Altitude"] : [`${val.toFixed(2)} m/s`, "VSpeed"]}
              labelFormatter={(l) => `${Math.floor(Number(l))} s`}
            />
            <Legend />
            <Line yAxisId="alt" type="monotone" dataKey="alt" name="Altitude (m)" stroke="#3b82f6" dot={false} />
            <Line yAxisId="vz"  type="monotone" dataKey="vz"  name="VSpeed (m/s)"  stroke="#ef4444" dot={false} />
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
      <div className="text-lg font-semibold">{value}</div>
    </div>
  );
}