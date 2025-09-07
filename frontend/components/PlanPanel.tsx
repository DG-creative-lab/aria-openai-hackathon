// frontend/components/PlanPanel.tsx
"use client";

import React from "react";

type Plan = {
  id: string;
  phase: "descent" | "base_leg" | "final_approach" | "flare";
  action: string;
  parameters?: Record<string, number>;
  checks?: string[];
  risk: "low" | "medium" | "high" | string;
  confidence: number;
  references?: string[];
  rationale: string;
  created_at?: number;
};

type Props = {
  plan?: Plan | null;
  backendBase?: string; // e.g., process.env.NEXT_PUBLIC_BACKEND_URL
};

export default function PlanPanel({ plan, backendBase = "" }: Props) {
  const [useDocs, setUseDocs] = React.useState<boolean>(() => {
    const v = localStorage.getItem("aria.useDocs");
    return v ? v === "1" : true;
  });
  const [useLessons, setUseLessons] = React.useState<boolean>(() => {
    const v = localStorage.getItem("aria.useLessons");
    return v ? v === "1" : true;
  });
  const [useGate, setUseGate] = React.useState<boolean>(() => {
    const v = localStorage.getItem("aria.useGate");
    return v ? v === "1" : true;
  });

  React.useEffect(() => {
    localStorage.setItem("aria.useDocs", useDocs ? "1" : "0");
    localStorage.setItem("aria.useLessons", useLessons ? "1" : "0");
    localStorage.setItem("aria.useGate", useGate ? "1" : "0");
    // Persist flags to backend so planner can respect ablations
    void fetch(`${backendBase}/api/admin/flags`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ use_docs: useDocs, use_lessons: useLessons, use_gate: useGate }),
    });
  }, [useDocs, useLessons, useGate, backendBase]);

  const approve = async () => {
    if (!plan) return;
    await fetch(`${backendBase}/api/plan/approve`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ plan_id: plan.id, human_action: "approved" }),
    });
  };

  const modify = async () => {
    if (!plan) return;
    const newAction = prompt("Modify action:", plan.action);
    if (newAction === null) return;
    await fetch(`${backendBase}/api/plan/approve`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        plan_id: plan.id,
        human_action: "modified",
        modification: { action: newAction },
      }),
    });
  };

  const reject = async () => {
    if (!plan) return;
    const note = prompt("Reason for rejection?", "");
    await fetch(`${backendBase}/api/plan/reject`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ plan_id: plan.id, human_action: "rejected", note }),
    });
  };

  // Styling helpers
  const riskColor =
    plan?.risk === "low" ? "bg-green-100 text-green-800 border-green-300" :
    plan?.risk === "high" ? "bg-red-100 text-red-800 border-red-300" :
    "bg-yellow-100 text-yellow-800 border-yellow-300";

  return (
    <div className="w-full max-w-xl rounded-2xl border p-4 shadow-sm bg-white">
      <div className="mb-3 flex items-center justify-between">
        <h3 className="text-lg font-semibold">ARIA Plan</h3>
        {/* Ablation toggles */}
        <div className="flex items-center gap-3">
          <Toggle label="Docs" checked={useDocs} onChange={setUseDocs} />
          <Toggle label="Lessons" checked={useLessons} onChange={setUseLessons} />
          <Toggle label="Gate" checked={useGate} onChange={setUseGate} />
        </div>
      </div>

      {!plan ? (
        <div className="text-sm text-gray-500">No plan yet. Waiting for next tick…</div>
      ) : (
        <>
          <div className={`rounded-xl border ${riskColor} px-3 py-2 mb-3`}>
            <div className="flex items-center justify-between">
              <div className="text-sm font-medium">Phase: {plan.phase}</div>
              <div className="text-sm">
                Risk: <b>{plan.risk}</b> · Conf: <b>{(plan.confidence ?? 0).toFixed(2)}</b>
              </div>
            </div>
            <div className="mt-1 text-sm">
              <span className="font-medium">Action:</span> {plan.action}
            </div>
          </div>

          {plan.parameters && Object.keys(plan.parameters).length > 0 && (
            <div className="mb-2">
              <div className="text-xs uppercase text-gray-500">Parameters</div>
              <div className="text-sm">
                {Object.entries(plan.parameters).map(([k, v]) => (
                  <span key={k} className="mr-3 inline-block rounded bg-gray-100 px-2 py-0.5 text-xs">
                    {k}: {typeof v === "number" ? v.toFixed(2) : String(v)}
                  </span>
                ))}
              </div>
            </div>
          )}

          {plan.checks && plan.checks.length > 0 && (
            <div className="mb-2">
              <div className="text-xs uppercase text-gray-500">Checks</div>
              <ul className="list-disc pl-5 text-sm">
                {plan.checks.map((c, i) => <li key={i}>{c}</li>)}
              </ul>
            </div>
          )}

          <div className="mb-2">
            <div className="text-xs uppercase text-gray-500">Rationale</div>
            <p className="text-sm">{plan.rationale}</p>
          </div>

          {plan.references && plan.references.length > 0 && (
            <div className="mb-2">
              <div className="text-xs uppercase text-gray-500">References</div>
              <div className="flex flex-wrap gap-2">
                {plan.references.map((r) => (
                  <span key={r} className="rounded bg-blue-50 px-2 py-0.5 text-xs text-blue-700 border border-blue-200">
                    {r}
                  </span>
                ))}
              </div>
            </div>
          )}

          <div className="mt-4 flex gap-2">
            <button
              onClick={approve}
              className="rounded-xl border border-green-300 bg-green-50 px-3 py-1.5 text-sm font-medium text-green-800 hover:bg-green-100"
            >
              Approve
            </button>
            <button
              onClick={modify}
              className="rounded-xl border border-amber-300 bg-amber-50 px-3 py-1.5 text-sm font-medium text-amber-800 hover:bg-amber-100"
            >
              Modify
            </button>
            <button
              onClick={reject}
              className="rounded-xl border border-red-300 bg-red-50 px-3 py-1.5 text-sm font-medium text-red-800 hover:bg-red-100"
            >
              Reject
            </button>
          </div>
        </>
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
    <label className="flex items-center gap-1.5 text-xs text-gray-700">
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


//This component:
//	•	Persists Docs / Lessons / Gate flags to localStorage.
//	•	POSTs them to POST /api/admin/flags (so the backend planner can ablate features live).
//	•	Calls POST /api/plan/approve|reject with the current plan id.


