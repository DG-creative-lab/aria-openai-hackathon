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
├─ .gitignore
├─ .env.example
├─ Makefile
├─ data/
│  ├─ telemetry/                              # pre-recorded, small CSVs for playback
│  │  ├─ landing_crosswind_baseline.csv
│  │  ├─ landing_crosswind_lesson.csv
│  │  └─ landing_blackout_window.csv
│  └─ docs/                                   # local docs you ingest (kept out of git)
│     └─ space_rider_manual/                  # PDFs go here (ignored by .gitignore)
│
├─ backend/
│  ├─ requirements.txt
│  ├─ app.py                                  # FastAPI app + startup hooks
│  ├─ settings.py                             # env & config
│  ├─ api/
│  │  ├─ routes_playback.py                   # start/stop/list scenarios
│  │  ├─ routes_plan.py                       # approve/modify/reject endpoints
│  │  └─ routes_admin.py                      # reset memory, ingest docs
│  ├─ services/
│  │  ├─ playback.py                          # streams CSV at realtime (20 Hz) + events
│  │  ├─ events.py                            # anomaly/phase detectors (1 Hz triggers)
│  │  ├─ planner.py                           # calls agent, returns JSON plan
│  │  ├─ plan_schema.py                       # Pydantic models (Plan, Decision, Metrics)
│  │  ├─ safety_gate.py                       # redlines & confidence fusion
│  │  └─ metrics.py                           # peak force proxy, touchdown stats, before/after
│  ├─ aria/
│  │  ├─ agent.py                             # Groq OpenAI-compatible call_model()
│  │  ├─ prompts.py                           # system and few-shot templates
│  │  └─ memory/
│  │     ├─ schema.sql
│  │     ├─ store.py                          # SQLite + FTS5 (episodic/semantic/docs, wm)
│  │     ├─ retriever.py                      # hybrid retrieval (docs + recent + lessons)
│  │     ├─ composer.py                       # builds compact prompt from context
│  │     ├─ governor.py                       # token budget & distill triggers
│  │     └─ distill.py                        # turns episodic → lessons (semantic)
│  └─ tools/
│     ├─ docs_ingest.py                       # chunk PDFs into docs_fts
│     └─ seed_from_csv.py                     # sanity-check telemetry files
│
├─ frontend/
│  ├─ package.json
│  ├─ next.config.mjs
│  ├─ app/
│  │  ├─ layout.tsx
│  │  └─ page.tsx                             # HUD + PlanPanel + Timeline
│  └─ components/
│     ├─ PlanPanel.tsx                        # plan card (risk, confidence, checks)
│     ├─ Timeline.tsx                         # anomalies/decisions stream
│     └─ Gauges.tsx                           # altitude, vspeed, airspeed, L/D, wind
└─ scripts/
   └─ record_demo.sh                          # optional: screen-record / trim helper
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