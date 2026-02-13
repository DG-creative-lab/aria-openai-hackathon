import { NextRequest } from "next/server";

function normalizeBase(u?: string | null) {
  if (!u) return null;
  return u.endsWith("/") ? u.slice(0, -1) : u;
}

export async function POST(req: NextRequest) {
  const body = await req.json();
  // Prefer NEXT_PUBLIC_API_BASE; allow API_BASE as a server-only override; fallback for local dev
  const rawBase =
    process.env.NEXT_PUBLIC_API_BASE ??
    process.env.API_BASE ??
    "http://127.0.0.1:8000";
  const base = normalizeBase(rawBase);

  if (!base) {
    return new Response(
      JSON.stringify({ error: "API base not configured" }),
      { status: 500, headers: { "Content-Type": "application/json" } }
    );
  }

  const r = await fetch(`${base}/api/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    // Abort in case backend hangs
    signal: AbortSignal.timeout(30000),
    body: JSON.stringify(body),
  });

  const text = await r.text();
  return new Response(text, {
    status: r.status,
    headers: { "Content-Type": r.headers.get("Content-Type") ?? "application/json" },
  });
}