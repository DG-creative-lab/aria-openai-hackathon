// frontend/lib/api.ts
export type PlannerState = {
  altitude_agl_m: number;
  vertical_speed_mps: number;
  wind_xy_mps: [number, number];
  phase?: string;
};

export async function planNow(
  base: string,
  state: PlannerState,
  opts?: { query?: string; use_docs?: boolean; use_lessons?: boolean; use_gate?: boolean }
) {
  const res = await fetch(`${base}/api/plan/now`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ state, ...opts }),
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`plan/now failed (${res.status}): ${text}`);
  }
  // Backend also emits SSE `plan_proposed`; return body just in case you want it
  return res.json();
}