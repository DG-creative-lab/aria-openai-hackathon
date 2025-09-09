// frontend/lib/events.ts
// Thin SSE client with typed handlers, heartbeat, and status callbacks.

export type TickEvent = {
  telem: {
    t: number;
    altitude_agl_m: number;
    vertical_speed_mps: number;
    vx_mps: number;
    vy_mps: number;
    wind_x_mps: number;
    wind_y_mps: number;
    contact_flag: number;
    contact_force_n: number;
    phase?: string;
  };
};

export type PlanEvent = {
  id: string;
  action: string;
  reasoning?: string;
  risk?: string;
  confidence?: number;
  checks?: string[];
  references?: string[];
  phase?: string;
  created_at?: number;
};

export type PlanDecidedEvent = {
  plan_id: string;
  action: "approved" | "modified" | "rejected" | string;
  mod?: Record<string, unknown> | null;
  note?: string | null;
};

export type MetricsEvent = Record<string, unknown>;
export type AnomalyEvent = { kind: string; [k: string]: unknown };

export type HelloEvent = { ok: boolean; ts: number };
export type HeartbeatEvent = { ts: number };

type EventMap = {
  // server emits these (see FastAPI routes_events.py)
  hello: HelloEvent;
  heartbeat: HeartbeatEvent;
  run_started: { scenario: string; dt: number };
  tick: TickEvent;
  anomaly: AnomalyEvent;
  plan_proposed: PlanEvent;
  plan_decided: PlanDecidedEvent;      // ← new
  metrics_update: MetricsEvent;
  run_finished: { scenario: string };
  distilled_lesson: { lesson_id: number; scenario: string };
};

export type SSEStatus = "open" | "retrying" | "closed";

type Handlers = Partial<{ [K in keyof EventMap]: (payload: EventMap[K]) => void }>;

export function connectSSE(
  handlers: Handlers,
  opts?: {
    base?: string;                    // default: NEXT_PUBLIC_API_BASE or same origin
    onStatus?: (s: SSEStatus) => void;
    heartbeatTimeoutMs?: number;      // default: 30000
  }
) {
  const base =
    opts?.base ??
    process.env.NEXT_PUBLIC_API_BASE ??
    ""; // relative URL if same origin/proxy

  const url = base ? `${base}/api/events/stream` : `/api/events/stream`;
  const es = new EventSource(url);

  // connection status (handy for HUD indicator)
  es.onopen = () => opts?.onStatus?.("open");
  es.onerror = () => opts?.onStatus?.("retrying");

  let lastBeat = Date.now();
  const hbMs = opts?.heartbeatTimeoutMs ?? 30_000;

  const parse = (e: MessageEvent) => {
    try {
      return JSON.parse(e.data);
    } catch {
      return undefined;
    }
  };

  const add = <K extends keyof EventMap>(name: K) => {
    es.addEventListener(name as string, (e: MessageEvent) => {
      const data = parse(e);
      if (data === undefined) return;
      handlers[name]?.(data);
      if (name === "heartbeat") lastBeat = Date.now();
    });
  };

  // Register all known events (safe if some never arrive)
  ([
    "hello",
    "heartbeat",
    "run_started",
    "tick",
    "anomaly",
    "plan_proposed",
    "plan_decided",
    "metrics_update",
    "run_finished",
    "distilled_lesson",
  ] as const).forEach((ev) => add(ev));

  // Soft monitor for stale connections (EventSource auto-reconnects itself)
  const monitor = typeof window !== "undefined"
    ? window.setInterval(() => {
        if (Date.now() - lastBeat > hbMs) opts?.onStatus?.("retrying");
      }, Math.min(5000, hbMs))
    : undefined;

  // keep your previous API: return a disposer function
  return () => {
    es.close();
    if (monitor) window.clearInterval(monitor);
    opts?.onStatus?.("closed");
  };
}