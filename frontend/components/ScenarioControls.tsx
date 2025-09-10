// frontend/components/ScenarioControls.tsx
"use client";

import React from "react";

type Scenario = { key: string; description?: string | null; seconds?: number | null };

export default function ScenarioControls() {
  const base = process.env.NEXT_PUBLIC_API_BASE || "";
  const [scenarios, setScenarios] = React.useState<Scenario[]>([]);
  const [selected, setSelected] = React.useState<string>("normal_descent");
  const [running, setRunning] = React.useState(false);
  const [busy, setBusy] = React.useState(false);

  React.useEffect(() => {
    (async () => {
      const r = await fetch(`${base}/api/scenarios`);
      const data = await r.json();
      setScenarios(data);
      const def = data.find((s: Scenario) => s.key === "normal_descent")?.key || data[0]?.key;
      if (def) setSelected(def);
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
    <div className="flex items-center gap-2">
      <select
        className="rounded-md border bg-background px-2 py-1 text-sm"
        value={selected}
        onChange={(e) => setSelected(e.target.value)}
        disabled={running || busy}
      >
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
    </div>
  );
}