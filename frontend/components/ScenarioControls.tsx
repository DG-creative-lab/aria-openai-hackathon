// frontend/components/ScenarioControls.tsx
"use client";

import React from "react";

type Scenario = { key: string; description?: string | null; seconds?: number | null };
const FALLBACK_SCENARIOS: Scenario[] = [
  { key: "normal_descent", description: "Normal descent" },
  { key: "crosswind_landing", description: "Crosswind landing" },
  { key: "comm_blackout", description: "Communication blackout" },
  { key: "power_anomaly", description: "Power anomaly" },
];

export default function ScenarioControls() {
  const base = process.env.NEXT_PUBLIC_API_BASE || "";
  const [scenarios, setScenarios] = React.useState<Scenario[]>(FALLBACK_SCENARIOS);
  const [selected, setSelected] = React.useState<string>("normal_descent");
  const [running, setRunning] = React.useState(false);
  const [busy, setBusy] = React.useState(false);
  const [loading, setLoading] = React.useState(false);
  const [loadError, setLoadError] = React.useState<string | null>(null);

  React.useEffect(() => {
    (async () => {
      setLoading(true);
      try {
        const ac = new AbortController();
        const timeout = setTimeout(() => ac.abort(), 4000);
        const r = await fetch(`${base}/api/scenarios`, { signal: ac.signal });
        clearTimeout(timeout);
        if (!r.ok) throw new Error(`scenarios_failed_${r.status}`);
        const data = await r.json();
        const list: Scenario[] = Array.isArray(data) ? data : [];
        if (!list.length) throw new Error("empty_scenarios");
        setScenarios(list);
        setLoadError(null);
        const def = list.find((s: Scenario) => s.key === "normal_descent")?.key || list[0]?.key;
        if (def) setSelected(def);
      } catch {
        // Keep fallback options; show warning only.
        setScenarios((prev) => (prev.length ? prev : FALLBACK_SCENARIOS));
        setSelected((prev) => prev || FALLBACK_SCENARIOS[0].key);
        setLoadError("Unable to load scenarios from API.");
      } finally {
        setLoading(false);
      }
    })();
    // small status poller so the button state matches reality
    const h = setInterval(async () => {
      try {
        const r = await fetch(`${base}/api/status`);
        const s = await r.json();
        setRunning(Boolean(s?.running));
      } catch {}
    }, 1000);
    return () => clearInterval(h);
  }, [base]);

  const start = async () => {
    setBusy(true);
    try {
      const r = await fetch(`${base}/api/start?scenario=${encodeURIComponent(selected)}`, { method: "POST" });
      if (!r.ok) {
        const err = await r.text();
        alert(`Start failed: ${err}`);
      }
    } finally {
      setBusy(false);
    }
  };

  const stop = async () => {
    setBusy(true);
    try {
      const r = await fetch(`${base}/api/stop`, { method: "POST" });
      if (!r.ok) {
        const err = await r.text();
        alert(`Stop failed: ${err}`);
      }
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="flex w-full sm:w-auto items-center justify-end gap-2 min-w-0">
      <select
        className="rounded-md border bg-background text-foreground px-2 py-1 text-sm w-full sm:w-[min(60vw,38rem)] min-w-[14rem] max-w-full truncate"
        value={selected}
        onChange={(e) => setSelected(e.target.value)}
        disabled={running || busy}
        title={selected}
      >
        {loading && !scenarios.length && <option value="normal_descent">Loading scenarios...</option>}
        {scenarios.map((s) => (
          <option key={s.key} value={s.key}>
            {s.description ? `${s.description} (${s.key})` : s.key}
          </option>
        ))}
      </select>

      {!running ? (
        <button
          onClick={start}
          disabled={busy || !selected}
          className="rounded-md bg-emerald-600 px-3 py-1.5 text-sm font-medium text-white hover:bg-emerald-500 disabled:opacity-50"
        >
          Start
        </button>
      ) : (
        <button
          onClick={stop}
          disabled={busy}
          className="rounded-md bg-rose-600 px-3 py-1.5 text-sm font-medium text-white hover:bg-rose-500 disabled:opacity-50"
        >
          Stop
        </button>
      )}
      {loadError && <span className="hidden lg:inline text-xs text-amber-400">{loadError}</span>}
    </div>
  );
}
