"use client";

import { useEffect, useRef, useState } from "react";

// --- local message shape (compatible with your Bubble)
type Role = "system" | "user" | "assistant";
type Part = { type: "text"; text: string };
type UiMsg = { id: string; role: Role; parts: Part[] };

export default function ChatPanel() {
  const [messages, setMessages] = useState<UiMsg[]>([]);
  const [input, setInput] = useState("");
  const [status, setStatus] =
    useState<"ready" | "submitted" | "streaming" | "stopped">("ready");
  const [error, setError] = useState<string | null>(null);
  const listRef = useRef<HTMLDivElement>(null);
  const abortRef = useRef<AbortController | null>(null);

  // auto-scroll on new messages
  useEffect(() => {
    const el = listRef.current;
    if (el) el.scrollTo({ top: el.scrollHeight, behavior: "smooth" });
  }, [messages.length]);

  function flattenParts(parts: Part[]) {
    return parts.map((p) => p.text).join("");
  }

  function toBackendPayload(msgs: UiMsg[]) {
    return {
      messages: msgs.map((m) => ({
        role: m.role,
        content: flattenParts(m.parts),
      })),
    };
  }

  async function callBackend(payload: any, signal?: AbortSignal) {
    const r = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
      signal,
    });
    if (!r.ok) {
      const t = await r.text();
      throw new Error(t || `HTTP ${r.status}`);
    }
    return (await r.json()) as { reply: string };
  }

  async function send(text: string) {
    setError(null);
    const userMsg: UiMsg = {
      id: crypto.randomUUID(),
      role: "user",
      parts: [{ type: "text", text }],
    };
    const next = [...messages, userMsg];
    setMessages(next);
    setInput("");
    setStatus("submitted");

    // enable Stop
    abortRef.current?.abort();
    const ac = new AbortController();
    abortRef.current = ac;

    try {
      const data = await callBackend(toBackendPayload(next), ac.signal);
      const assistantMsg: UiMsg = {
        id: crypto.randomUUID(),
        role: "assistant",
        parts: [{ type: "text", text: data.reply || "(no reply)" }],
      };
      setMessages((prev) => [...prev, assistantMsg]);
      setStatus("ready");
    } catch (e: any) {
      if (e?.name === "AbortError") {
        setStatus("stopped");
        return;
      }
      setError(e?.message || "Request failed");
      setStatus("ready");
    }
  }

  // manual retry of last user message
  const retryLast = () => {
    const lastUser = [...messages].reverse().find((m) => m.role === "user");
    if (!lastUser) return;
    const idx = messages.findIndex((m) => m.id === lastUser.id);
    setMessages(messages.slice(0, idx + 1));
    const text = flattenParts(lastUser.parts);
    if (text) void send(text);
  };

  const stop = () => {
    abortRef.current?.abort();
  };

  return (
    <div className="flex h-full flex-col">
      {/* Messages */}
      <div
        ref={listRef}
        className="flex-1 overflow-y-auto rounded-xl border border-input bg-muted/30 p-3 custom-scroll"
      >
        {messages.length === 0 ? (
          <EmptyState />
        ) : (
          <div className="space-y-3">
            {messages.map((m) => (
              <Bubble key={m.id} role={m.role} parts={m.parts} />
            ))}
          </div>
        )}

        {status !== "ready" && (
          <div className="mt-2 text-xs text-muted-foreground">
            {status === "submitted"
              ? "Submitting…"
              : status === "streaming"
              ? "Streaming…" // not used now, but kept for consistency
              : "Stopped"}
          </div>
        )}

        {error && (
          <div className="mt-2 flex items-center gap-2 text-xs text-destructive">
            Something went wrong.
            <button onClick={retryLast} className="underline">
              Retry
            </button>
          </div>
        )}
      </div>

      {/* Composer */}
      <form
        onSubmit={(e) => {
          e.preventDefault();
          const text = input.trim();
          if (text) void send(text);
        }}
        className="mt-3 flex gap-2"
      >
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          disabled={status !== "ready"}
          placeholder='Ask ARIA… (try: tool:doc_search q="flare window")'
          className="flex-1 rounded-xl border border-input bg-background px-3 py-2 text-sm
                     focus:outline-none focus:ring-2 focus:ring-primary/60"
        />
        {status === "submitted" ? (
          <button
            type="button"
            onClick={stop}
            className="rounded-xl border border-amber-300 bg-amber-50 px-4 text-sm font-medium text-amber-900
                       hover:bg-amber-100 dark:border-amber-400/40 dark:bg-amber-400/10 dark:text-amber-200"
          >
            Stop
          </button>
        ) : (
          <button
            type="submit"
            className="rounded-xl bg-primary px-4 py-2 text-sm font-medium text-primary-foreground shadow-soft
                       hover:opacity-90 disabled:opacity-50"
          >
            Send
          </button>
        )}
      </form>
    </div>
  );
}

function Bubble({
  role,
  parts,
}: {
  role: Role;
  parts: { type: string; text?: string }[];
}) {
  const base = "max-w-[85%] break-words rounded-2xl px-3 py-2 border text-sm";
  const user = "ml-auto bg-primary/15 border-primary/20 text-foreground";
  const bot = "mr-auto bg-card border-border text-foreground";
  const system = "mx-auto bg-secondary/40 border-border text-muted-foreground";
  return (
    <div className={role === "user" ? "text-right" : ""}>
      <div className={`${base} ${role === "user" ? user : role === "assistant" ? bot : system}`}>
        {parts.map((p, i) => (p.type === "text" ? <span key={i}>{p.text}</span> : null))}
      </div>
    </div>
  );
}

function EmptyState() {
  return (
    <div className="grid h-full place-items-center text-sm text-muted-foreground">
      <div className="text-center">
        <p className="font-medium">No messages yet</p>
        <p>Type a prompt to start the mission chat.</p>
      </div>
    </div>
  );
}