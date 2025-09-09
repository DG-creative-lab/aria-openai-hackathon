"use client";
import { useState, FormEvent } from "react";

type Msg = { role: "user" | "assistant"; content: string };

export default function ChatPanel() {
  const [messages, setMessages] = useState<Msg[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    if (!input.trim() || loading) return;

    const next = [...messages, { role: "user", content: input }];
    setMessages(next);
    setInput("");
    setLoading(true);

    try {
      const r = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: next }),
      });
      const data = await r.json();
      const reply = (data.reply ?? "").toString();
      setMessages((m) => [...m, { role: "assistant", content: reply }]);
    } catch (err: any) {
      setMessages((m) => [
        ...m,
        { role: "assistant", content: `⚠️ Chat error: ${err?.message ?? err}` },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="rounded-2xl border flex flex-col h-full">
      <div className="p-3 border-b text-sm font-medium">ARIA Chat</div>
      <div className="p-3 space-y-3 overflow-auto flex-1">
        {messages.length === 0 && (
          <div className="text-sm text-gray-500">
            Ask anything about procedures, flare windows, crosswind limits…
          </div>
        )}
        {messages.map((m, i) => (
          <div key={i} className="text-sm">
            <span className="font-semibold">{m.role === "user" ? "You" : "ARIA"}: </span>
            <span className="whitespace-pre-wrap">{m.content}</span>
          </div>
        ))}
        {loading && <div className="text-xs text-gray-400">thinking…</div>}
      </div>
      <form onSubmit={onSubmit} className="p-3 border-t flex gap-2">
        <input
          className="flex-1 border rounded-lg px-3 py-2 text-sm outline-none"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="e.g., crosswind flare guidance at 7 m/s?"
        />
        <button
          className="px-3 py-2 text-sm rounded-lg bg-black text-white disabled:opacity-50"
          disabled={loading || !input.trim()}
        >
          Send
        </button>
      </form>
    </div>
  );
}