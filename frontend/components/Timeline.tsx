// frontend/components/Timeline.tsx
"use client";

import React from "react";
import { connectSSE, PlanEvent, AnomalyEvent } from "../lib/events";

type Row =
  | { at: number; kind: "run"; text: string }
  | { at: number; kind: "plan"; text: string; conf?: number }
  | { at: number; kind: "anomaly"; text: string }
  | { at: number; kind: "distill"; text: string };

type Props = { backendBase?: string };

// Keep the list bounded for perf & UX
const MAX_ROWS = 200;

export default function Timeline(_props: Props) {
  const [rows, setRows] = React.useState<Row[]>([]);
  const scrollRef = React.useRef<HTMLDivElement | null>(null);

  React.useEffect(() => {
    const stop = connectSSE({
      run_started: (d) => push({ kind: "run", text: `Run started (${d.scenario})`, at: Date.now() }),
      run_finished: (d) => push({ kind: "run", text: `Run finished (${d.scenario})`, at: Date.now() }),
      plan_proposed: (p) => {
        const pe = p as PlanEvent;
        const label = pe.action || "(no action)";
        push({ kind: "plan", text: label, conf: pe.confidence, at: Date.now() });
      },
      anomaly: (a) => {
        const an = a as AnomalyEvent;
        const desc =
          an.kind === "crosswind_high"
            ? `Anomaly: Crosswind high (${String(an["wind_y"] ?? "")} m/s)`
            : an.kind === "descent_rate_high_near_ground"
            ? `Anomaly: High sink near ground (${String(an["vz"] ?? "")} m/s)`
            : `Anomaly: ${an.kind}`;
        push({ kind: "anomaly", text: desc, at: Date.now() });
      },
      distilled_lesson: (x) =>
        push({ kind: "distill", text: `Lesson distilled (#${x.lesson_id})`, at: Date.now() }),
    });
    return () => stop();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  function push(r: Row) {
    setRows((prev) => {
      const next = [r, ...prev];
      return next.slice(0, MAX_ROWS);
    });
    // keep scroll pinned to top (newest at top); no-op if user scrolled
    if (scrollRef.current) {
      // If the user is near the top (within ~20px), pin to top after update
      if (scrollRef.current.scrollTop <= 20) {
        queueMicrotask(() => { if (scrollRef.current) scrollRef.current.scrollTop = 0; });
      }
    }
  }

  return (
    <div className="h-full min-h-0 flex flex-col rounded-2xl border bg-card shadow-soft glass">
      {/* Optional header row could go here */}
      <div
        ref={scrollRef}
        className="flex-1 min-h-0 overflow-auto overscroll-contain px-4 py-4"
      >
        <ul className="space-y-2">
          {rows.map((r, i) => (
            <li key={i} className="flex items-start gap-2">
              <Badge kind={r.kind} />
              <div className="flex-1">
                <div className="text-sm">{r.text}</div>
                <div className="text-xs text-gray-500">
                  {new Date(r.at).toLocaleTimeString()}
                  {r.kind === "plan" && typeof r.conf === "number" ? (
                    <span className="ml-2">• conf {r.conf.toFixed(2)}</span>
                  ) : null}
                </div>
              </div>
            </li>
          ))}
          {rows.length === 0 && (
            <li className="text-sm text-gray-500">No events yet — start a scenario to see activity.</li>
          )}
        </ul>
      </div>
    </div>
  );
}

function Badge({ kind }: { kind: Row["kind"] }) {
  const styles =
    kind === "plan"
      ? "bg-blue-50 text-blue-700 border-blue-200"
      : kind === "anomaly"
      ? "bg-red-50 text-red-700 border-red-200"
      : kind === "distill"
      ? "bg-emerald-50 text-emerald-700 border-emerald-200"
      : "bg-gray-50 text-gray-700 border-gray-200";
  const label =
    kind === "plan" ? "Plan" : kind === "anomaly" ? "Anomaly" : kind === "distill" ? "Lesson" : "Run";
  return <span className={`mt-0.5 inline-block rounded-full border px-2 py-0.5 text-xs ${styles}`}>{label}</span>;
}