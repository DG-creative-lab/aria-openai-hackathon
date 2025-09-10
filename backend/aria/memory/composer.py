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
    return f"{card.text}\n(SOURCE: {card.source}, score={card.score:.3f})"

def _log_section(name: str, items: List[RetrievalResult]):
    # unchanged
    ...

def build_minimal_memory(state_summary: str) -> Dict[str, List[str]]:
    """Guaranteed-key minimal context for safe fallback."""
    return {
        "state":   [state_summary],
        "recent":  [],
        "lessons": [],
        "facts":   [],
        "qa":      [],
        "docs":    [],
    }

def build_working_memory(db_path: str, state_summary: str, query: str) -> Dict[str, List[str]]:
    global _tick_counter
    _tick_counter += 1
    t0 = time.perf_counter()

    R = Retriever(db_path=db_path)

    # 1) Semantic lessons
    sem_lessons = R.lessons(query, k=2)

    # 2) Rephrased guarded → fallback docs
    cards = R.rephrased_guarded(query, k=6)
    if not cards:
        cards = R.docs(query, k=3)

    # 3) Split kinds
    repr_lessons = [c for c in cards if c.kind == "repr_lesson"]
    facts        = [c for c in cards if c.kind == "repr_fact"]
    qas          = [c for c in cards if c.kind == "repr_qa"]
    docs_fallback= [c for c in cards if c.kind == "doc"]

    # 4) Episodic
    recent = R.episodic_recent(seconds=20, k=8)

    # 5) Build sections — ensure all keys exist
    lessons_section = (sem_lessons + repr_lessons) or []
    sections: Dict[str, List[str]] = {
        "state":   [state_summary],
        "recent":  [r.text for r in recent],
        "lessons": [_fmt(c) for c in lessons_section],
        "facts":   [_fmt(c) for c in facts],
        "qa":      [_fmt(c) for c in qas],
        "docs":    [],  # always present
    }
    if not lessons_section and docs_fallback:
        sections["docs"] = [_fmt(c) for c in docs_fallback]

    # logging (optional)
    if LOG_RETR and (_tick_counter % max(1, LOG_RETR_SAMPLE_N) == 0):
        dt_ms = (time.perf_counter() - t0) * 1000.0
        print(f"[retrieval:stats] k={{'sem':{len(sem_lessons)}, 'repr':{len(cards)}, 'recent':{len(recent)}}}, {dt_ms:.1f} ms")
        _log_section("lessons", sem_lessons + repr_lessons or docs_fallback)
        _log_section("facts", facts)
        _log_section("qa", qas)

    # 6) Budget with governor
    trimmed, stats = governor.apply_budget(sections)
    if LOG_GOV and (_tick_counter % max(1, LOG_RETR_SAMPLE_N) == 0):
        print("[governor:stats]", json.dumps(stats, ensure_ascii=False))
    return trimmed