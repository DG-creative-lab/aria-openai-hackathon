"use client";

import { useEffect, useState } from "react";

type Item = {
  id: number;
  kind: "lesson" | "qa" | "fact" | string;
  text: string;
  source_id: string;
  tags?: string;
  source_excerpt?: string | null;
};

export default function SemanticLessonViewer() {
  const [q, setQ] = useState("crosswind OR flare");
  const [items, setItems] = useState<Item[]>([]);
  const [loading, setLoading] = useState(false);
  const BACKEND = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

  const search = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${BACKEND}/api/knowledge/rephrased/search?q=${encodeURIComponent(q)}&k=20`);
      const js = await res.json();
      setItems(js.results || []);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { search(); /* initial */ }, []);

  return (
    <div className="w-full max-w-4xl mx-auto p-4 space-y-4">
      <div className="flex gap-2">
        <input
          className="w-full border rounded-xl px-3 py-2"
          value={q}
          onChange={(e) => setQ(e.target.value)}
          placeholder="Search lessons (e.g., crosswind, flare window, descent rate)"
        />
        <button
          onClick={search}
          className="px-4 py-2 rounded-xl border shadow-sm"
          disabled={loading}
        >
          {loading ? "Searching…" : "Search"}
        </button>
      </div>

      <div className="grid gap-3">
        {items.map((it) => (
          <div key={it.id} className="rounded-2xl border p-4 shadow-sm">
            <div className="text-xs opacity-70 mb-2">
              {it.kind.toUpperCase()} • {it.source_id} {it.tags ? `• ${it.tags}` : ""}
            </div>
            <pre className="whitespace-pre-wrap text-sm">{it.text}</pre>
            {it.source_excerpt && (
              <details className="mt-3">
                <summary className="cursor-pointer text-xs underline">Source excerpt</summary>
                <div className="mt-2 text-xs opacity-80 whitespace-pre-wrap">
                  {it.source_excerpt}
                </div>
              </details>
            )}
            <div className="mt-3 flex gap-2">
              <button
                className="px-3 py-1 text-xs border rounded-xl"
                onClick={() => navigator.clipboard.writeText(it.text)}
                title="Copy lesson text"
              >
                Copy
              </button>
            </div>
          </div>
        ))}
        {!loading && items.length === 0 && (
          <div className="text-sm opacity-70">No results. Try another query.</div>
        )}
      </div>
    </div>
  );
}