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