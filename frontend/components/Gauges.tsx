"use client";

import React from "react";
import { connectSSE, TickEvent } from "../lib/events";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  ResponsiveContainer,
  Tooltip,
  CartesianGrid,
  Legend,
} from "recharts";

type Props = { backendBase?: string };

type Point = { t: number; alt: number; vz: number };

export default function Gauges(_props: Props) {
  const [latest, setLatest] = React.useState<TickEvent["telem"] | null>(null);
  const [series, setSeries] = React.useState<Point[]>([]);
  const startedAtRef = React.useRef<number>(performance.now());

  React.useEffect(() => {
    const stop = connectSSE({
      tick: ({ telem }) => {
        setLatest(telem);
        setSeries((prev) => {
          const tsec = (performance.now() - startedAtRef.current) / 1000;
          const next = [
            ...prev,
            { t: tsec, alt: telem.altitude_agl_m, vz: telem.vertical_speed_mps },
          ];
          if (next.length > 1200) next.shift(); // keep ~60s @ 20Hz
          return next;
        });
      },
    });
    return () => stop();
  }, []);

  const alt = latest?.altitude_agl_m ?? 0;
  const vz = latest?.vertical_speed_mps ?? 0;
  const vx = latest?.vx_mps ?? 0;
  const vy = latest?.vy_mps ?? 0;
  const gs = Math.sqrt(vx * vx + vy * vy);
  const wx = latest?.wind_x_mps ?? 0;
  const wy = latest?.wind_y_mps ?? 0;
  const xwind = Math.abs(wy);

  const riskBadge =
    alt < 20 && vz < -6
      ? "text-red-400 bg-red-950/30 border-red-700"
      : xwind > 8
      ? "text-amber-400 bg-amber-950/30 border-amber-700"
      : "text-emerald-400 bg-emerald-950/30 border-emerald-700";

  return (
    <div className="space-y-3">
      {/* stat blocks */}
      <div className="grid grid-cols-2 gap-3 md:grid-cols-4">
        <Stat label="Altitude (AGL)" value={`${alt.toFixed(1)} m`} />
        <Stat label="VSpeed" value={`${vz.toFixed(2)} m/s`} />
        <Stat label="Ground Speed" value={`${gs.toFixed(1)} m/s`} />
        <div
          className={`rounded-xl border px-3 py-2 ${riskBadge}`}
        >
          <div className="text-xs uppercase text-muted-foreground">Crosswind</div>
          <div className="text-lg font-semibold">{xwind.toFixed(1)} m/s</div>
          <div className="text-[11px] text-muted-foreground">
            Wind: ({wx.toFixed(1)}, {wy.toFixed(1)}) m/s
          </div>
        </div>
      </div>

      {/* mini time-series */}
      <div className="h-56 w-full">
        <ResponsiveContainer>
          <LineChart data={series}>
            <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" />
            <XAxis
              dataKey="t"
              tickFormatter={(v) => `${Math.floor(v)}s`}
              stroke="hsl(var(--muted-foreground))"
              fontSize={12}
            />
            <YAxis
              yAxisId="alt"
              stroke="#3b82f6"
              domain={["dataMin - 10", "dataMax + 10"]}
              width={60}
              fontSize={12}
            />
            <YAxis
              yAxisId="vz"
              orientation="right"
              stroke="#ef4444"
              width={50}
              fontSize={12}
            />
            <Tooltip
              formatter={(val: number, name: string) =>
                name === "alt"
                  ? [`${val.toFixed(1)} m`, "Altitude"]
                  : [`${val.toFixed(2)} m/s`, "VSpeed"]
              }
              labelFormatter={(l) => `${Math.floor(Number(l))} s`}
              contentStyle={{
                background: "hsl(var(--card))",
                border: "1px solid hsl(var(--border))",
                borderRadius: "0.75rem",
                fontSize: "12px",
              }}
            />
            <Legend />
            <Line
              yAxisId="alt"
              type="monotone"
              dataKey="alt"
              name="Altitude (m)"
              stroke="#3b82f6"
              dot={false}
            />
            <Line
              yAxisId="vz"
              type="monotone"
              dataKey="vz"
              name="VSpeed (m/s)"
              stroke="#ef4444"
              dot={false}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl border border-border bg-card px-3 py-2">
      <div className="text-xs uppercase text-muted-foreground">{label}</div>
      <div className="text-lg font-semibold text-foreground">{value}</div>
    </div>
  );
}