# ARIA Mission Control — GPT-OSS Edition 🛩️

[Project Paper Lik](docs/aria-context-and-memory.md)

A real-time mission UI that plans, reasons, and chats using open-weights LLMs.

---

## ✨ What it is

ARIA is a tiny autonomy stack with a clean UI:

- **Backend (FastAPI)** streams synthetic telemetry and emits plans via SSE.
- **A planner** builds a compact working-memory (recent events + distilled lessons + rephrased docs) and asks an OSS model for a JSON Plan.
- **A safety gate** vets actions.
- **A Next.js/React frontend** renders Gauges, Plan, Timeline, and a Chat (Vercel AI SDK v5) that also hits the GPT-OSS model.

Everything is open and swappable; the only paid thing is your LLM key.

---

## 🧠 Why GPT-OSS

- **Open weights & portability** – run on OpenRouter (default), or your own vLLM/llama.cpp server.
- **Cost control** – small JSON plans + retrieval keep token usage tiny.
- **Auditable plans** – models output a strict JSON plan that we validate; working memory is logged.

**Default model (demo):** `openai/gpt-oss-120b`.
**Automatic fallback model:** `openrouter/aurora-alpha` (experimental, via OpenRouter).  
You can substitute any OSS model exposed through an OpenAI-compatible endpoint.

---

## 🗺️ Architecture (at a glance)

```
FastAPI  ──────────────▶  /api/events/stream (SSE) ───▶  Frontend UI
   │
   ├─ /api/start?scenario=… ──► telemetry playback
   ├─ /api/admin/flags      ──► {use_docs,use_lessons,use_gate}
   └─ planner.tick()
        ├─ composer.build_working_memory()
        │    ├─ Retriever.lessons (SQLite FTS5 + vectors)
        │    ├─ Rephrased cards (QA/facts/lessons, guarded)
        │    ├─ Raw docs fallback
        │    └─ Episodic recent log
        ├─ governor.apply_budget()  (token budget)
        ├─ prompts.build_messages() (system+user)
        ├─ OSS model (JSON plan)
        ├─ safety_gate.vet_plan()
        └─ episodic log + emit "plan_proposed"
```

---

## 🚀 Quick start

### 0) Requirements

- Python 3.11+ (we used 3.13)
- Node 18+ / PNPM
- SQLite3 with FTS5 (macOS Homebrew default is fine)

### 1) Configure keys

Copy env templates and fill your OSS LLM key:

```bash
# Backend
cp .env.example .env
# set LLM_PROVIDER=openrouter
# set OPENROUTER_API_KEY=...
# set MODEL_NAME=openai/gpt-oss-120b
# optional fallback: FALLBACK_MODEL_NAME=openrouter/aurora-alpha

# Frontend
cp frontend/.env.local.example frontend/.env.local
# set NEXT_PUBLIC_API_BASE=http://localhost:8000
# optional: NEXT_PUBLIC_MODEL_NAME="GPT-OSS 120B"
```

### 2) Install

```bash
# frontend deps
cd frontend && pnpm i && cd ..

# (first time) python deps
cd backend
# we used uv/uvicorn in scripts, but pip works too
pip install -r requirements.txt  # or: uv pip install -r ...
```

### 3) Run both (monorepo helper)

From repo root:

```bash
pnpm dev
```

This runs:
- API at http://localhost:8000
- Web at http://localhost:3000

If port conflicts happen: kill with `lsof -i :3000 | awk 'NR>1 {print $2}' | xargs kill -9` (same for 8000), then retry.

---

## 🧪 Demo flow (60s smoke test)

1. Open http://localhost:3000.
2. Start a scenario:

```bash
curl -X POST 'http://localhost:8000/api/start?scenario=normal_descent'
```

3. You should see gauges move, timeline events arrive, and a Plan card appear (risk + confidence).
4. Toggle Docs / Lessons / Gate in the Plan panel and watch the next plan adjust.

If the stream looks idle:

```bash
curl -X POST http://localhost:8000/api/events/test-ping
```

---

## 🧩 How GPT-OSS is used

- **JSON Plans** — We call the model in JSON mode (`response_format="json_object"`) for a Plan with:
  - phase, action, risk, confidence, optional parameters, checks, references, rationale.
- **Small prompts** — A governor shapes the working memory to ~under 1k tokens typical.
- **Light tool-use** — If the model returns a tool directive (e.g., `{"tool":"doc_search","query":"flare timing"}`), we run the tool once and do one short follow-up call.
- **Safety gate** — A rule-based pass clamps or nudges risky outputs before UI.

### Swap models easily

- **OpenRouter (recommended for demo)**
  - Set `LLM_PROVIDER=openrouter`
  - Set `OPENROUTER_API_KEY`
  - Set `MODEL_NAME=openai/gpt-oss-120b`
  - Optional fallback: `FALLBACK_MODEL_NAME=openrouter/aurora-alpha`
- **Other OpenAI-compatible endpoints (vLLM / local llama.cpp / hosted APIs)**
  - Set `LLM_PROVIDER=openai`
  - Set `OPENAI_API_KEY` + `OPENAI_BASE_URL`
  - Set `MODEL_NAME` to a model your endpoint exposes.

All calls route through the centralized LLM client (`backend/llm/client.py`), with `aria/agent.py` as a compatibility facade.

---

## 🗃️ Data layer (SQLite + FTS5)

`data/memory.sqlite` (checked in) ships with:

- `lessons` (+ `lessons_fts`) — distilled bullets
- `docs_rephrased` (+ `docs_rephrased_fts`) — compact QA/facts/lessons
- `docs` (+ `docs_fts`) — raw chunks fallback
- `episodic_log` (+ `episodic_fts`) — run-time events & decisions

Verify quickly:

```bash
sqlite3 data/memory.sqlite '.tables'
```

Want to rebuild? Run `sqlite3 data/memory.sqlite < aria/memory/schema.sql` then your own ingest pipeline (see `aria/memory/distill.py` and the `/data/docs` samples).

---

## 🖥️ Frontend

Next.js (App Router), Tailwind v3, dark theme.

### Components

- **Gauges.tsx** — Altitude / VSpeed / Ground speed / Crosswind + tiny trend chart.
- **PlanPanel.tsx** — Current plan, risk/confidence, ablations (Docs / Lessons / Gate), approve/modify/reject.
- **Timeline.tsx** — Streamed events (Run/Plan/Anomaly).
- **(ui)/chat/ChatPanel.tsx** — Vercel AI SDK v5 useChat with DefaultChatTransport → /api/chat (same OSS model).
- SSE client lives in `lib/events.ts` (`connectSSE(...)`).

---

## 🔌 API (minimal)

- `GET  /api/events/stream` — SSE: tick, plan_proposed, metrics_update, anomaly, run_started, run_finished, distilled_lesson
- `POST /api/start?scenario=normal_descent` — begin playback
- `POST /api/admin/flags` — `{use_docs,use_lessons,use_gate}` (booleans)
- `GET  /api/status` — health snapshot
- **Frontend chat route:** `POST /api/chat` → streams model text

---

## ⚙️ Key env knobs (backend)

```bash
# LLM wiring (default OpenRouter)
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=...
OPENAI_BASE_URL=https://openrouter.ai/api/v1
MODEL_NAME=openai/gpt-oss-120b
FALLBACK_MODEL_NAME=openrouter/aurora-alpha
# Optional OpenRouter attribution headers:
# OPENROUTER_APP_NAME=ARIA Mission Control
# OPENROUTER_APP_URL=https://your-app.example

# Planner
PLAN_TOKEN_BUDGET=900
PLAN_MAX_COMPLETION=256
ALLOW_TOOL_REQUESTS=1

# Governor (context budgeting)
CONTEXT_BUDGET_TOKENS=6000
CONTEXT_SECTION_ORDER=state,recent,lessons,facts,qa,docs
# ...see aria/memory/governor.py for per-section caps

# Logging
LOG_RETRIEVAL=1
LOG_RETRIEVAL_TOPN=3
LOG_RETRIEVAL_TEXT=0
LOG_GOVERNOR=1
```

**Frontend:**

```bash
NEXT_PUBLIC_API_BASE=http://localhost:8000
NEXT_PUBLIC_LLM_MODEL_LABEL="GPT-oss-20B"
```

---

## 🧪 Testing pieces independently

- **SSE only:**
  ```bash
  curl -N http://localhost:8000/api/events/stream
  ```

- **Planner only (REPL):**
  ```python
  import asyncio
  from backend.services import planner
  async def test():
      p = await planner.tick(
          db_path="data/memory.sqlite",
          state_summary={"phase":"descent","altitude_agl_m":1200,"vertical_speed_mps":-5.2,"wind_xy_mps":[1.1,-0.4]},
          query="Safe descent plan?",
          ablations={"use_docs":True,"use_lessons":True,"use_gate":True}
      )
      print(p)
  asyncio.run(test())
  ```

- **Chat only:** open UI and use the left chat; it streams via `/api/chat`.

---

## 🛡️ Safety

- `safety_gate.vet_plan()` enforces simple operational rules (e.g., no extreme actions).
- Plans are auditable: we append every decision to `episodic_log` with working-memory provenance flags.

---

## 🔧 Troubleshooting

- **Frontend runs, but no events**
  - Check the console of `pnpm dev` for `GET /api/events/stream 200`.
  - Hit `POST /api/events/test-ping` to verify SSE path.

- **405 Method Not Allowed on /api/admin/flags**
  - Use POST and send JSON: `{"use_docs":true,"use_lessons":true,"use_gate":true}`

- **Port already in use**
  ```bash
  lsof -i :3000 | awk 'NR>1 {print $2}' | xargs kill -9  # (repeat for 8000)
  ```

- **Model "Submitting…" but no answer**
  - Verify `OPENROUTER_API_KEY`, `MODEL_NAME`, and `FALLBACK_MODEL_NAME`.
  - If using a custom endpoint, set `LLM_PROVIDER=openai` and `OPENAI_BASE_URL`.

---

## 🛠️ Extending

- Swap models in one place (`backend/llm/config.py` + env) or just change env.
- Drop in your own docs (markdown/PDF→txt) and (re)distill to `docs_rephrased`.
- Add critics or a brand policy pass beside `safety_gate`.

---

## 📄 License

MIT for this demo code & prompts. Documents under `data/docs` retain their original licenses.


## TL;DR

- **One command:** `pnpm dev`
- **One key:** your OpenRouter key (or any OpenAI-compatible host key)
- **One UI:** Realtime gauges, JSON plans, and a mission chat — all powered by open models.
