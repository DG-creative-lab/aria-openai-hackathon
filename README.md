# ARIA — Space Rider Mission Control Agent

*An offline, memory-augmented reasoning assistant for parafoil landing decision support — powered by GPT-OSS on Groq.*

**Category:** Best Local Agent (secondary: For Humanity)  
**Tagline:** Memory + safety gates + human-in-the-loop → measurably safer landings on the *second* run.

---

## Why this matters

Space missions face comms gaps, uncertainty, and time pressure. ARIA shows how a small open model (gpt-oss-20b) can:
- **Retrieve procedures & lessons**, reason over telemetry, and
- **Propose safe, auditable next actions** with **risk** and **confidence**, while
- **Improving across runs** via episodic→semantic memory — **no fine-tuning**.

We focus the demo on **AI reasoning, memory, and human-AI collaboration**. Telemetry is **pre-recorded** to keep the build reproducible and fully offline.

---

## What’s included

- **Playback Service** — streams CSV telemetry at real time (20 Hz) and emits 1 Hz “reasoning” ticks.
- **Memory Fabric** — SQLite + FTS5 (episodic log, semantic lessons, docs RAG, working memory).
- **Safety Gate** — redlines (bank, crosswind, flare window, descent rate) + confidence fusion.
- **ARIA Planner** — Groq OpenAI-compatible call to GPT-OSS (20B by default).
- **Human-AI UI** — Plan card (risk & confidence), Approve/Modify/Reject, Timeline, Before/After metrics.

---
## 📁 Repository Structure

```bash
aria-space-rider/
├─ README.md
├─ .env.example
├─ Makefile
├─ data/
│  ├─ telemetry/
│  └─ docs/
│     ├─ space_rider_manual/
│     └─ processed/                 # .md from PyMuPDF4LLM
│
├─ backend/
│  ├─ requirements.txt
│  ├─ app.py                        # FastAPI app + startup
│  ├─ settings.py                   # env & config
│  ├─ api/
│  │  ├─ routes_knowledge.py 
│  │  ├─ routes_playback.py         # start/stop/list scenarios
│  │  ├─ routes_plan.py             # approve/modify/reject; stream plan SSE
│  │  ├─ routes_events.py           # SSE: ticks, anomalies, decisions
│  │  └─ routes_admin.py            # reset memory, ingest docs
│  ├─ services/
│  │  ├─ playback.py                # 20Hz CSV stream; 1Hz ticks
│  │  ├─ events.py                  # anomaly/phase detectors
│  │  ├─ planner.py                 # 1Hz loop → compose → call model
│  │  ├─ plan_schema.py             # Pydantic models (Plan/Decision/Metrics)
│  │  ├─ safety_gate.py             # redlines, confidence fusion
│  │  └─ metrics.py                 # before/after, touchdown stats
│  ├─ aria/
│  │  ├─ agent.py                   # OpenAI-compatible client (Groq/local)
│  │  ├─ prompts.py                 # system & few-shot, Chain-of-Draft style
│  │  └─ memory/
│  │     ├─ schema.sql
│  │     ├─ store.py                # SQLite + FTS5 (episodic/semantic/docs)
│  │     ├─ embeddings.py           # local embeddings (e5-small / MiniLM)
│  │     ├─ retriever.py            # hybrid retrieval (FTS + embed + recency)
│  │     ├─ composer.py             # builds working memory; sections + weights
│  │     ├─ governor.py             # token budget, truncation, summarize
│  │     ├─ distill.py              # episodic → lessons (semantic)
│  │     └─ tools.py                # ReAct-lite: doc_search(), recall_lesson()
│  └─ tools/
│     ├─ pdf_to_markdown_pymupdf.py # ✅ your light, fast converter
│     ├─ docs_ingest.py             # chunk .md → docs_fts + embeddings
│     └─ seed_from_csv.py           # telemetry sanity checks
│
├─ frontend/
│  ├─ package.json
│  ├─ next.config.mjs
│  ├─ app/
│  │  ├─ layout.tsx
│  │  └─ page.tsx                   # HUD + PlanPanel + Timeline
│  ├─ components/
│  │  ├─ PlanPanel.tsx              # plan JSON card (risk, confidence)
│  │  ├─ Timeline.tsx               # SSE: anomalies/decisions
│  │  └─ Gauges.tsx                 # alt, vspeed, airspeed, L/D, wind
│  └─ lib/
│     ├─ ai.ts                      # Vercel AI SDK client helpers (stream)
│     └─ events.ts                  # SSE client for /events
└─ scripts/
   └─ record_demo.sh
```

---

## Quickstart

### 0) Prereqs
- Python 3.11+, Node 18+
- (Optional) Groq account + $25 promo: `OPENAIOSSGROQ2025`

### 1) Backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp ../.env.example .env
# Set GROQ_API_KEY in .env (or run fully offline to use stubbed responses)
```
**Run**:

```bash
uvicorn app:app --reload --port 8000
```

### 2) Frontend

```bash
cd ../frontend
npm i
npm run dev
# http://localhost:3000
```

### 3) Play a scenario

```bash
# list scenarios
curl http://localhost:8000/scenarios
# start one
curl -X POST "http://localhost:8000/start?scenario=crosswind_baseline"
# stop
curl -X POST http://localhost:8000/stop
```

##### Scenarios included

landing_crosswind_baseline.csv — late flare → hard landing (baseline)
landing_crosswind_lesson.csv — retrieved lesson → earlier flare/larger base → softer touchdown
landing_blackout_window.csv — lost-comms window; conservative hold/flare window
(You can generate these offline from a simulator and keep the CSVs small.)


## Environment

Create .env at repo root or backend/.env:

```bash

PORT=8000
WS_PATH=/ws/telemetry
TICK_HZ=20                       # playback rate
REASON_HZ=1                      # reasoning cadence

# Groq / GPT-OSS
GROQ_API_KEY=your_key_here
OPENAI_BASE_URL=https://api.groq.com/openai/v1
GPT_MODEL=openai/gpt-oss-20b     # use 120b for final hero clip if desired
```
---
## API overview

GET /scenarios → available telemetry files
POST /start?scenario=NAME → begin playback
POST /stop → stop playback
WS /ws/telemetry → stream {telemetry, plan?, decision?, metrics} updates
POST /plan/approve → body: {plan_id, modification?}
POST /plan/reject → body: {plan_id, reason}
POST /admin/memory/reset → clear episodic/semantic (dev only)
POST /admin/docs/ingest → (optional) load PDFs into FTS5
Plan JSON (example)


## Memory & reasoning

Episodic: append-only events (anomaly/decision/outcome) sampled ~1 Hz.
Semantic: distilled “lessons learned” bullets by phase.
Docs RAG: local FTS5 over Space Rider procedures/checklists.
Composer: compact prompt = recent events + lessons + top doc chunks + current telemetry.
Governor: when episodic grows, trigger distillation → keep prompts lean.
Cadence: model called at 1 Hz or on anomaly; no chain-of-thought logged.

## Safety model

Redlines (tune to CSV): |bank| ≤ 20°, crosswind ≤ 8 m/s, flare 8–12 m AGL, vz@10m ≥ -2.5 m/s.
Safety Gate downgrades unsafe plans (e.g., “Hold Pattern”) and caps confidence.
HIL: humans Approve / Modify / Reject every plan; fallback Checklist Mode on LLM timeout.

## Notes

This repo ships with tiny CSVs; large media (PDFs/video) are ignored by git.
We used Groq’s OpenAI-compatible endpoint for GPT-OSS;
Not affiliated with ESA; telemetry is synthetic for research/demo.


### Data Flow 

```bash
CSV (data/telemetry/landing_*.csv)  ← your generator (20 Hz rows + t)
         │
         ▼ 20 Hz
PlaybackService._run()
  ├─ SSE "tick" → Frontend HUD
  ├─ MetricsTracker.update_from_telem()
  ├─ _maybe_emit_anomaly() → SSE "anomaly" (when needed)
  └─ every 1s:
        state_summary, query
           │
           ▼
        planner.tick()
           │
           ├─ composer.build_working_memory()
           │     ├─ episodic_recent(...)          (SQLite: episodic_log)
           │     ├─ rephrased_guarded(query,k=4)  (SQLite: docs_rephrased + NLI vs docs)
           │     │     └─ fallback docs(query)    (SQLite: docs)
           │     └─ lessons(query,k=1)            (SQLite: lessons)
           │        ↳ governor trims to token budget
           │
           ├─ prompts/system + few-shot + context
           ├─ agent.call_model()  (Groq GPT-OSS-20B)
           ├─ safety_gate.vet_plan()
           ├─ mem_store.episodic_append(kind="decision", data=plan)
           └─ SSE "plan_proposed" (with references + latency)
                 │
                 └─ Frontend (PlanPanel): Approve/Modify/Reject → POST /plan/...
                      ↳ mem_store.episodic_append(kind="decision", text="approved/...")
                      ↳ MetricsTracker may note result

... run continues until touchdown ...
  ├─ MetricsTracker.finish_run()
  ├─ SSE "metrics_update" (final)
  ├─ SSE "run_finished"
  └─ (optional) distill.episodic → lessons (SQLite)
        ↳ next run retrieves that new lesson automatically

```

SQLite roles
* docs — raw chunks from manuals/papers; FTS + embeddings; immutable.
* docs_rephrased — BeyondWeb-style lesson cards/Q&A/facts; preferred snippets; NLI-guarded vs docs.
* episodic_log — per-run timeline of events/decisions/outcomes; used for RECENT context.
* lessons — distilled, cross-run “what worked”; retrieved on future runs.

### What the model actually sees each second

state_summary (dict), ex:

```json
{
  "altitude_agl_m": 420.0,
  "vertical_speed_mps": -4.3,
  "wind_xy_mps": [2.1, 7.8],
  "phase": "final_approach",
  "bank_deg": 6.2
}
```
query (short string), ex:

"crosswind landing flare window procedure"

Working memory sections built by the composer:
* STATE: one-line summary
* RECENT: last few episodic events (anomalies/decisions)
* LESSON: top 1 long-term lesson if similar
* DOC: 1–4 rephrased snippets (NLI-guarded), else a couple of raw doc chunks

The governor trims that bundle to stay inside the token budget.
The LLM returns compact JSON: {action, reasoning, risk, confidence, references}.

⸻
### to run the frontend 

1. Frontend deps
```bash
cd frontend
corepack enable                     # turn on the shims
pnpm -v                             # Corepack fetches the pinned pnpm version
pnpm install                        # uses the pinned pnpm for this project
```
2. Run both
```bash
pnpm dev
```

