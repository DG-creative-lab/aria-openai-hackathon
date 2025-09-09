"use client";

import { useState, useEffect, useRef } from "react";
import { useChat } from "@ai-sdk/react";
import { DefaultChatTransport, UIMessage } from "ai";

export default function ChatPanel() {
  const { messages, sendMessage, status, stop, error, setMessages } = useChat({
    transport: new DefaultChatTransport({ api: "/api/chat" }),
  });

  const [input, setInput] = useState("");
  const listRef = useRef<HTMLDivElement>(null);

  // auto-scroll on new messages
  useEffect(() => {
    const el = listRef.current;
    if (el) el.scrollTo({ top: el.scrollHeight, behavior: "smooth" });
  }, [messages.length]);

  // manual retry of last user message
  const retryLast = () => {
    const lastUser = [...messages].reverse().find((m) => m.role === "user");
    if (!lastUser) return;
    const idx = messages.findIndex((m) => m.id === lastUser.id);
    setMessages(messages.slice(0, idx + 1) as UIMessage[]);
    const text = lastUser.parts.map((p) => (p.type === "text" ? p.text : "")).join("");
    if (text) sendMessage({ text });
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
            {status === "streaming" ? "Streaming…" : "Submitting…"}
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
          if (!input.trim()) return;
          sendMessage({ text: input });
          setInput("");
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
        {status === "streaming" || status === "submitted" ? (
          <button
            type="button"
            onClick={() => stop()}
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
  role: string;
  parts: { type: string; text?: string }[];
}) {
  const isUser = role === "user";
  const base = "max-w-[85%] break-words rounded-2xl px-3 py-2 border text-sm";
  const user = "ml-auto bg-primary/15 border-primary/20 text-foreground";
  const bot = "mr-auto bg-card border-border text-foreground";
  const system = "mx-auto bg-secondary/40 border-border text-muted-foreground";

  return (
    <div className={isUser ? "text-right" : ""}>
      <div
        className={`${base} ${
          role === "user" ? user : role === "assistant" ? bot : system
        }`}
      >
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