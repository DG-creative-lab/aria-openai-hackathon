# ARIA Mission Control: Portfolio Case Study

## Project Summary

ARIA is a real-time mission-control simulation for parafoil landing operations.  
It combines telemetry playback, retrieval-augmented planning, rule-based safety checks, and a human-in-the-loop UI.

This project demonstrates practical AI systems engineering across backend, frontend, data, and reliability concerns.

## Problem Statement

Hackathon prototypes usually prove ideas but leave architectural and reliability gaps:

- Tight coupling of model provider logic with domain logic.
- Inconsistent API/data contracts between backend and frontend.
- Schema drift risks in local databases.
- Weak fallback behavior when model outputs are empty or invalid.

Goal: stabilize and productionize the prototype without losing iteration speed.

## Solution Architecture

### Runtime Flow

1. Telemetry scenarios stream from CSV at 20 Hz.
2. Planner ticks at 1 Hz and assembles working memory:
   - state summary
   - recent episodic events
   - retrieved lessons and docs
3. LLM returns a structured JSON plan.
4. Safety gate validates/adjusts risky actions.
5. Plan and metrics are emitted via SSE and persisted to episodic memory.
6. End-of-run distillation writes semantic lessons for future retrieval.

### Key Components

- `backend/services/playback.py`: telemetry loop, planner invocation, SSE publishing
- `backend/services/planner.py`: planning orchestration
- `backend/services/safety_gate.py`: domain safety checks/redlines
- `backend/aria/memory/`: retrieval, schema, distillation, storage
- `backend/llm/`: provider abstraction, retry/fallback policy
- `frontend/components/`: mission chat, gauges, timeline, plan panel

## Engineering Improvements Implemented

### 1) LLM Provider Abstraction

Refactored provider logic into `backend/llm/`:

- `config.py`: environment-driven provider/model config
- `providers/openai_compatible.py`: OpenAI-compatible adapter
- `client.py`: retry policy, model fallback policy, health checks

Impact:

- Provider changes no longer require touching planner/chat logic.
- Cleaner testing surface and better maintainability.

### 2) Robust Fallback Behavior

Added failover behavior for empty model responses:

- Empty content is treated as a failure condition.
- Retry/fallback path is invoked automatically.
- Chat route guarantees a non-empty user-visible response string.

Impact:

- Eliminates silent `(no reply)` UX failures.

### 3) Backward-Compatible Retrieval

Fixed schema drift between code and local SQLite snapshots:

- Retriever now handles `docs` tables with or without an `embedding` column.

Impact:

- Prevents runtime crashes on older/dev database files.

### 4) API and UI Contract Fixes

- Mounted missing backend routers.
- Added missing `POST /api/plan/now` endpoint.
- Fixed frontend plan-check rendering for structured check objects.
- Corrected toggle defaults and SSE base handling.

Impact:

- End-to-end planning flow became stable and observable.

## Tradeoffs

- Kept `backend/aria/agent.py` as a compatibility facade during refactor to avoid widespread import churn.
- Used OpenAI-compatible adapter for both OpenRouter/OpenAI paths to minimize code duplication.
- Prioritized reliability patches over broad feature expansion.

## Reliability and Observability Notes

- Plan generation errors now surface clearly through API logs.
- Model fallback order is configurable in env.
- SSE stream includes run, plan, anomaly, and metrics events for operator visibility.

## What This Project Demonstrates

- Full-stack ownership (Python + TypeScript).
- Real-time distributed flow design (SSE + async services).
- AI application robustness patterns:
  - strict output shaping
  - safety-gated post-processing
  - retrieval grounding
  - fallback-oriented provider integration
- Pragmatic migration from hackathon code to maintainable architecture.

## Next Improvements (Roadmap)

1. Add automated integration tests for `start -> plan -> decide -> distill`.
2. Add structured logging/metrics dashboards for planner latency and fallback rates.
3. Move to explicit env loading per service directory to avoid `.env` ambiguity.
4. Add optional auth and role-based controls for multi-operator scenarios.

