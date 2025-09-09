import { NextRequest } from "next/server";

export async function POST(req: NextRequest) {
  const base = process.env.NEXT_PUBLIC_API_BASE!;
  const body = await req.json();

  // Forward to your backend chat endpoint
  const r = await fetch(`${base}/api/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  // Backend returns { reply: string } (non-streaming)
  if (!r.ok) {
    return new Response(JSON.stringify({ error: await r.text() }), {
      status: r.status,
      headers: { "Content-Type": "application/json" },
    });
  }
  const data = await r.json();
  return Response.json(data);
}