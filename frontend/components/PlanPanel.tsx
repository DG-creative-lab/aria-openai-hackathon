"use client";

import React from "react";
import { connectSSE, type PlanEvent } from "../lib/events";

type Plan = {
  id: string;
  phase: string;
  action: string;
  parameters?: Record<string, number>;
  checks?: string[];
  risk: "low" | "medium" | "high" | string;
  confidence: number;
  references?: string[];
  reasoning?: string;
  rationale?: string;
  created_at?: number;
};

type Props = { plan?: Plan | null; backendBase?: string };

export default function PlanPanel({
  plan,
  backendBase = process.env.NEXT_PUBLIC_API_BASE || "",
}: Props) {
  const [livePlan, setLivePlan] = React.useState<PlanEvent | null>(null);

  React.useEffect(() => {
    if (plan) return;
    const off = connectSSE({ plan_proposed: (p) => setLivePlan(p) });
    return off;
  }, [plan]);

  const effectivePlan: Plan | null =
    plan ?? (livePlan as unknown as Plan | null) ?? null;

  // --- Ablations ---
  const [useDocs, setUseDocs] = React.useState(() =>
    typeof window !== "undefined"
      ? localStorage.getItem("aria.useDocs") === "1"
      : true
  );
  const [useLessons, setUseLessons] = React.useState(() =>
    typeof window !== "undefined"
      ? localStorage.getItem("aria.useLessons") === "1"
      : true
  );
  const [useGate, setUseGate] = React.useState(() =>
    typeof window !== "undefined"
      ? localStorage.getItem("aria.useGate") === "1"
      : true
  );

  React.useEffect(() => {
    if (typeof window === "undefined") return;
    localStorage.setItem("aria.useDocs", useDocs ? "1" : "0");
    localStorage.setItem("aria.useLessons", useLessons ? "1" : "0");
    localStorage.setItem("aria.useGate", useGate ? "1" : "0");
    void fetch(`${backendBase}/api/admin/flags`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        use_docs: useDocs,
        use_lessons: useLessons,
        use_gate: useGate,
      }),
    }).catch(() => {});
  }, [useDocs, useLessons, useGate, backendBase]);

  // --- Risk badge ---
  const riskColor =
    effectivePlan?.risk === "low"
      ? "bg-green-100 text-green-800 border-green-300 dark:bg-green-950/30 dark:text-green-300 dark:border-green-700"
      : effectivePlan?.risk === "high"
      ? "bg-red-100 text-red-800 border-red-300 dark:bg-red-950/30 dark:text-red-300 dark:border-red-700"
      : "bg-yellow-100 text-yellow-800 border-yellow-300 dark:bg-yellow-950/30 dark:text-yellow-300 dark:border-yellow-700";

  const reasoning = effectivePlan?.reasoning ?? effectivePlan?.rationale ?? "";

  // --- Actions ---
  const approve = async () => {
    if (!effectivePlan) return;
    await fetch(`${backendBase}/api/plan/approve`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        plan_id: effectivePlan.id,
        human_action: "approved",
      }),
    });
  };

  const modify = async () => {
    if (!effectivePlan) return;
    const newAction = prompt("Modify action:", effectivePlan.action);
    if (newAction === null) return;
    await fetch(`${backendBase}/api/plan/approve`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        plan_id: effectivePlan.id,
        human_action: "modified",
        modification: { action: newAction },
      }),
    });
  };

  const reject = async () => {
    if (!effectivePlan) return;
    const note = prompt("Reason for rejection?", "");
    await fetch(`${backendBase}/api/plan/reject`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        plan_id: effectivePlan.id,
        human_action: "rejected",
        note,
      }),
    });
  };

  return (
    <div className="flex h-full w-full flex-col">
      {/* toggle row only */}
      <div className="flex items-center justify-end gap-3 border-b px-4 py-2">
        <Toggle label="Docs" checked={useDocs} onChange={setUseDocs} />
        <Toggle label="Lessons" checked={useLessons} onChange={setUseLessons} />
        <Toggle label="Gate" checked={useGate} onChange={setUseGate} />
      </div>

      {/* content */}
      <div className="flex-1 overflow-y-auto p-4">
        {!effectivePlan ? (
          <div className="text-sm text-muted-foreground">
            No plan yet. Waiting for next tick…
          </div>
        ) : (
          <>
            <div className={`mb-3 rounded-xl border px-3 py-2 ${riskColor}`}>
              <div className="flex items-center justify-between">
                <div className="text-sm font-medium">
                  Phase: {effectivePlan.phase}
                </div>
                <div className="text-sm">
                  Risk: <b>{effectivePlan.risk}</b> · Conf:{" "}
                  <b>{(effectivePlan.confidence ?? 0).toFixed(2)}</b>
                </div>
              </div>
              <div className="mt-1 text-sm">
                <span className="font-medium">Action:</span>{" "}
                {effectivePlan.action}
              </div>
            </div>

            {effectivePlan.parameters &&
              Object.keys(effectivePlan.parameters).length > 0 && (
                <div className="mb-2">
                  <div className="text-xs uppercase text-muted-foreground">
                    Parameters
                  </div>
                  <div className="text-sm">
                    {Object.entries(effectivePlan.parameters).map(([k, v]) => (
                      <span
                        key={k}
                        className="mr-2 inline-block rounded bg-muted px-2 py-0.5 text-xs"
                      >
                        {k}:{" "}
                        {typeof v === "number" ? v.toFixed(2) : String(v)}
                      </span>
                    ))}
                  </div>
                </div>
              )}

            {effectivePlan.checks?.length ? (
              <div className="mb-2">
                <div className="text-xs uppercase text-muted-foreground">
                  Checks
                </div>
                <ul className="list-disc pl-5 text-sm">
                  {effectivePlan.checks.map((c, i) => (
                    <li key={i}>{c}</li>
                  ))}
                </ul>
              </div>
            ) : null}

            {reasoning && (
              <div className="mb-2">
                <div className="text-xs uppercase text-muted-foreground">
                  Reasoning
                </div>
                <p className="text-sm">{reasoning}</p>
              </div>
            )}

            {effectivePlan.references?.length ? (
              <div className="mb-2">
                <div className="text-xs uppercase text-muted-foreground">
                  References
                </div>
                <div className="flex flex-wrap gap-2">
                  {effectivePlan.references.map((r) => (
                    <span
                      key={r}
                      className="rounded border border-blue-300 bg-blue-50 px-2 py-0.5 text-xs text-blue-700 dark:border-blue-700 dark:bg-blue-950/30 dark:text-blue-300"
                    >
                      {r}
                    </span>
                  ))}
                </div>
              </div>
            ) : null}
          </>
        )}
      </div>

      {/* footer */}
      {effectivePlan && (
        <div className="flex gap-2 border-t px-4 py-3">
          <button
            onClick={approve}
            className="rounded-xl border border-green-300 bg-green-50 px-3 py-1.5 text-sm font-medium text-green-800 hover:bg-green-100 dark:border-green-700 dark:bg-green-950/30 dark:text-green-300"
          >
            Approve
          </button>
          <button
            onClick={modify}
            className="rounded-xl border border-amber-300 bg-amber-50 px-3 py-1.5 text-sm font-medium text-amber-800 hover:bg-amber-100 dark:border-amber-700 dark:bg-amber-950/30 dark:text-amber-300"
          >
            Modify
          </button>
          <button
            onClick={reject}
            className="rounded-xl border border-red-300 bg-red-50 px-3 py-1.5 text-sm font-medium text-red-800 hover:bg-red-100 dark:border-red-700 dark:bg-red-950/30 dark:text-red-300"
          >
            Reject
          </button>
        </div>
      )}
    </div>
  );
}

function Toggle({
  label,
  checked,
  onChange,
}: {
  label: string;
  checked: boolean;
  onChange: (v: boolean) => void;
}) {
  return (
    <label className="flex items-center gap-1.5 text-xs text-muted-foreground">
      <input
        type="checkbox"
        className="h-4 w-4 accent-blue-600"
        checked={checked}
        onChange={(e) => onChange(e.target.checked)}
      />
      {label}
    </label>
  );
}


