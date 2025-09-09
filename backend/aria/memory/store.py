# backend/aria/memory/store.py
from __future__ import annotations
import json, sqlite3, time
from pathlib import Path
from typing import Any, Dict, Iterable, Optional

import numpy as np

# Embeddings are needed only for lessons insert (optional but recommended)
try:
    from .embeddings import embed_texts
except Exception:
    embed_texts = None  # type: ignore

HERE = Path(__file__).parent
SCHEMA_PATH = HERE / "schema.sql"

# ---------------- DB helpers ----------------

def _connect(db_path: str | Path) -> sqlite3.Connection:
    p = Path(db_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    cx = sqlite3.connect(str(p))
    cx.row_factory = sqlite3.Row
    # Pragmas tuned for app workload (safe defaults)
    cx.execute("PRAGMA journal_mode=WAL;")
    cx.execute("PRAGMA synchronous=NORMAL;")
    return cx

def ensure_db(db_path: str | Path) -> None:
    """Create/upgrade schema if needed."""
    with _connect(db_path) as cx:
        sql = SCHEMA_PATH.read_text(encoding="utf-8")
        cx.executescript(sql)
        cx.commit()

# ---------------- Episodic log ----------------

def episodic_append(
    db_path: str | Path,
    kind: str,
    text: str,
    data: Optional[Dict[str, Any]] = None,
    ts: Optional[float] = None,
) -> int:
    """
    Append one row to episodic_log.
    NOTE: We store wall-clock seconds (time.time()) for compatibility with retriever.episodic_recent().
    """
    ts = float(ts if ts is not None else time.time())
    payload = json.dumps(data or {}, ensure_ascii=False)
    with _connect(db_path) as cx:
        cur = cx.execute(
            "INSERT INTO episodic_log(ts, kind, text, data) VALUES (?,?,?,?)",
            (ts, kind, text, payload),
        )
        cx.commit()
        return int(cur.lastrowid)

def episodic_clear(db_path: str | Path, older_than: Optional[float] = None) -> int:
    """
    Delete episodic rows. If older_than is given (unix seconds), delete those with ts < older_than.
    Returns number of rows deleted.
    """
    with _connect(db_path) as cx:
        if older_than is None:
            cur = cx.execute("DELETE FROM episodic_log")
        else:
            cur = cx.execute("DELETE FROM episodic_log WHERE ts < ?", (float(older_than),))
        cx.commit()
        return cur.rowcount

# ---------------- Lessons (semantic memory) ----------------

def _to_blob(vec: np.ndarray) -> bytes:
    v = np.asarray(vec, dtype="float32")
    return v.tobytes(order="C")

def lessons_insert(
    db_path: str | Path,
    title: str,
    body: str,
    tags: Iterable[str] | str = "",
    meta: Optional[Dict[str, Any]] = None,
    do_embed: bool = True,
) -> int:
    """
    Insert a distilled lesson.
    - body: newline-separated imperative bullets
    - tags: list or comma-separated string
    - meta: provenance (scenario, stats, examples)
    """
    tag_str = ",".join(tags) if isinstance(tags, (list, tuple, set)) else str(tags or "")
    meta_json = json.dumps(meta or {}, ensure_ascii=False)

    emb_blob: Optional[bytes] = None
    if do_embed:
        if embed_texts is None:
            raise RuntimeError("embeddings.embed_texts not available; cannot embed lessons.")
        # Simple policy: embed title + body for a stronger signal
        vec = embed_texts([f"{title}\n{body}"])[0]
        emb_blob = _to_blob(vec)

    with _connect(db_path) as cx:
        cur = cx.execute(
            "INSERT INTO lessons(title, body, tags, meta, embedding) VALUES (?,?,?,?,?)",
            (title, body, tag_str, meta_json, emb_blob),
        )
        cx.commit()
        return int(cur.lastrowid)

def lessons_delete(db_path: str | Path, lesson_id: int) -> None:
    with _connect(db_path) as cx:
        cx.execute("DELETE FROM lessons WHERE id=?", (int(lesson_id),))
        cx.commit()

# ---------------- Maintenance & quick stats ----------------

def optimize_fts(db_path: str | Path) -> None:
    """
    Run FTS optimize statements. Harmless if indexes are already optimized.
    """
    with _connect(db_path) as cx:
        for tbl in ("docs_fts", "docs_rephrased_fts", "lessons_fts", "episodic_fts"):
            try:
                cx.execute(f"INSERT INTO {tbl}({tbl}) VALUES('optimize')")
            except Exception:
                pass
        cx.commit()

def counts(db_path: str | Path) -> Dict[str, int]:
    with _connect(db_path) as cx:
        def _cnt(table: str) -> int:
            try:
                return int(cx.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0])
            except Exception:
                return 0
        return {
            "docs": _cnt("docs"),
            "docs_rephrased": _cnt("docs_rephrased"),
            "lessons": _cnt("lessons"),
            "episodic_log": _cnt("episodic_log"),
        }

def reset_memory(db_path: str | Path, which: str = "episodic") -> None:
    """
    Quick local dev reset.
    which ∈ {'episodic','lessons','all'}
    """
    with _connect(db_path) as cx:
        if which in ("episodic", "all"):
            cx.execute("DELETE FROM episodic_log")
        if which in ("lessons", "all"):
            cx.execute("DELETE FROM lessons")
        cx.commit()