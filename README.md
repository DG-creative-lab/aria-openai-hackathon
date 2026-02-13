# ARIA Mission Control

Real-time mission-control simulation with safety-gated LLM planning, retrieval-augmented memory, and a live operator UI.

[Architecture paper](docs/aria-context-and-memory.md)  
[Portfolio case study](docs/portfolio-case-study.md)

## Portfolio Snapshot

ARIA is a full-stack AI system, not just a chat demo:

- Simulates parafoil landing scenarios from telemetry CSV streams.
- Generates structured plans at 1 Hz using an LLM + retrieval + safety gate.
- Stores episodic decisions and distills cross-run lessons in SQLite/FTS.
- Supports operator-in-the-loop controls: approve, modify, reject.

Primary model is `openai/gpt-oss-120b` with automatic fallback to `openrouter/aurora-alpha`.

## System Architecture

```text
Telemetry CSVs (20 Hz)
  -> Playback service (FastAPI)
  -> SSE stream (/api/events/stream)
  -> Next.js UI (gauges, timeline, plan panel)

Planner tick (1 Hz)
  -> Working memory composer (recent events + lessons + docs)
  -> Token budget governor
  -> LLM JSON plan
  -> Safety gate checks
  -> plan_proposed SSE + episodic log write
```

Main modules:

- Backend API: `backend/api/`
- Planner/services: `backend/services/`
- Memory/retrieval: `backend/aria/memory/`
- LLM abstraction: `backend/llm/`
- Frontend app: `frontend/`
- Scenario data: `data/telemetry/`, `data/aria.sqlite`

## Tech Stack

- Backend: FastAPI, SQLite (FTS5), pandas, async SSE
- Frontend: Next.js (App Router), React, Tailwind, Recharts
- LLM routing: OpenAI-compatible client with provider/fallback policy
- Memory: episodic log + distilled semantic lessons + doc retrieval

## Quick Start

### 1) Prerequisites

- Python 3.11+
- Node 20+ (recommended) and pnpm

### 2) Configure environment files

Backend (`backend/.env`):

```bash
cp backend/.env.example backend/.env
```

Set at minimum:

```bash
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=...
OPENAI_BASE_URL=https://openrouter.ai/api/v1
MODEL_NAME=openai/gpt-oss-120b
FALLBACK_MODEL_NAME=openrouter/aurora-alpha
```

Frontend (`frontend/.env.local`):

```bash
cp frontend/.env.local.example frontend/.env.local
```

Typical value:

```bash
NEXT_PUBLIC_API_BASE=http://localhost:8000
```

### 3) Install dependencies

```bash
cd frontend && pnpm i && cd ..
cd backend && pip install -r requirements.txt && cd ..
```

### 4) Run both apps

```bash
pnpm dev
```

Services:

- API: `http://localhost:8000`
- Web: `http://localhost:3000`

## Demo Flow

1. Open `http://localhost:3000`.
2. Click `Start` on any scenario.
3. Verify:
   - Gauges update in real time.
   - Timeline receives run events.
   - ARIA Plan populates and updates each second.
4. Use Plan actions (`Approve`, `Modify`, `Reject`) to simulate operator decisions.
5. Use Mission Chat to query lessons/docs.

## Key Endpoints

- `GET /api/events/stream`: SSE telemetry, plans, metrics, anomalies
- `POST /api/start?scenario=<key>`: start playback
- `POST /api/stop`: stop playback
- `GET /api/status`: playback status
- `POST /api/admin/flags`: ablations (`use_docs`, `use_lessons`, `use_gate`)
- `POST /api/plan/now`: one-shot planning call
- `POST /api/chat`: mission chat

## Notable Engineering Decisions

- Isolated LLM layer (`backend/llm/`) with provider and retry/fallback policy.
- Backward-compatible retriever behavior for schema drift in existing SQLite files.
- Safety-gate enforcement before plan display.
- Thin compatibility facade in `backend/aria/agent.py` to avoid breaking imports during refactor.

## Troubleshooting

- `OPENROUTER_API_KEY is not set`
  - Put key in `backend/.env`, not frontend env.
  - Restart API after edits.
- Plan panel shows `No plan yet`
  - Check API logs for planner/retriever exceptions.
  - Test `POST /api/plan/now` directly.
- Tokenizers fork warning on shutdown
  - Set `TOKENIZERS_PARALLELISM=false` in `backend/.env`.

## License

MIT for code in this repository.  
Files under `data/docs` retain their original licenses/sources.

