# backend/aria/memory/composer.py
from __future__ import annotations
from typing import Dict, List
import os, json, time

from .retriever import Retriever, RetrievalResult
from . import governor

# ----- logging knobs -----
LOG_RETR          = os.getenv("LOG_RETRIEVAL", "1") == "1"
LOG_RETR_TOPN     = int(os.getenv("LOG_RETRIEVAL_TOPN", "3"))
LOG_RETR_SAMPLE_N = int(os.getenv("LOG_RETRIEVAL_SAMPLE_N", "1"))
LOG_RETR_TEXT     = os.getenv("LOG_RETRIEVAL_TEXT", "0") == "1"
LOG_RETR_PREFIX   = int(os.getenv("LOG_RETRIEVAL_TEXT_PREFIX", "80"))
LOG_GOV           = os.getenv("LOG_GOVERNOR", "1") == "1"

_tick_counter = 0

def _fmt(card: RetrievalResult) -> str:
    # Attach provenance for debugging/audit
    return f"{card.text}\n(SOURCE: {card.source}, score={card.score:.3f})"

def _log_section(name: str, items: List[RetrievalResult]):
    if not LOG_RETR or not items:
        return
    show = items[:LOG_RETR_TOPN]
    payload = []
    for r in show:
        e = {"kind": r.kind, "source": r.source, "score": round(r.score, 4)}
        if LOG_RETR_TEXT:
            e["text"] = (r.text[:LOG_RETR_PREFIX] + "…") if len(r.text) > LOG_RETR_PREFIX else r.text
        payload.append(e)
    print(f"[retrieval:{name}]", json.dumps(payload, ensure_ascii=False))

def build_working_memory(db_path: str, state_summary: str, query: str) -> Dict[str, List[str]]:
    """
    Compose working memory sections from:
      - state (caller-provided summary string)
      - episodic (recent log)
      - semantic lessons (cross-run distilled)
      - rephrased cards (lesson/fact/qa) with NLI guard
      - optional raw docs fallback
    Then apply the governor to fit within the context budget.
    """
    global _tick_counter
    _tick_counter += 1
    t0 = time.perf_counter()

    R = Retriever(db_path=db_path)

    # 1) Semantic lessons (distilled, cross-run)
    sem_lessons = R.lessons(query, k=2)

    # 2) Rephrased (guarded) → fallback to raw docs
    cards = R.rephrased_guarded(query, k=6)
    if not cards:
        cards = R.docs(query, k=3)

    # 3) Group rephrased by kind
    repr_lessons = [c for c in cards if c.kind == "repr_lesson"]
    facts        = [c for c in cards if c.kind == "repr_fact"]
    qas          = [c for c in cards if c.kind == "repr_qa"]
    docs_fallback= [c for c in cards if c.kind == "doc"]

    # 4) Episodic (recent)
    recent = R.episodic_recent(seconds=20, k=8)

    # 5) Assemble sections (lessons = semantic + rephrased; fallback to docs if empty)
    lessons_section = (sem_lessons + repr_lessons) or docs_fallback
    facts_section   = facts
    qa_section      = qas

    # --- sampled retrieval logging (every N ticks) ---
    if LOG_RETR and (_tick_counter % max(1, LOG_RETR_SAMPLE_N) == 0):
        dt_ms = (time.perf_counter() - t0) * 1000.0
        print(f"[retrieval:stats] k={{'sem':{len(sem_lessons)}, 'repr':{len(cards)}, 'recent':{len(recent)}}}, {dt_ms:.1f} ms")
        _log_section("lessons", lessons_section)
        _log_section("facts", facts_section)
        _log_section("qa", qa_section)

    # 6) Build raw sections dict for the governor
    sections = {
        "state":   [state_summary],
        "recent":  [r.text for r in recent],
        "lessons": [_fmt(c) for c in lessons_section],
        "facts":   [_fmt(c) for c in facts_section],
        "qa":      [_fmt(c) for c in qa_section],
    }
    # Include docs explicitly so the governor can allocate a small slice if present
    if docs_fallback and not lessons_section:  # only if we truly fell back
        sections["docs"] = [_fmt(c) for c in docs_fallback]

    # 7) Apply governor (token budgeting, compression, truncation)
    trimmed, stats = governor.apply_budget(sections)

    if LOG_GOV and (_tick_counter % max(1, LOG_RETR_SAMPLE_N) == 0):
        print("[governor:stats]", json.dumps(stats, ensure_ascii=False))

    return trimmed