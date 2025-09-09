# backend/api/routes_knowledge.py
from __future__ import annotations
import os, sqlite3, json
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Query, HTTPException

router = APIRouter(prefix="/api/knowledge", tags=["knowledge"])

DB_PATH = os.getenv("ARIA_DB_PATH", "data/aria.sqlite")

def _connect(db_path: str) -> sqlite3.Connection:
    cx = sqlite3.connect(db_path)
    cx.row_factory = sqlite3.Row
    return cx

def _excerpt(text: Optional[str], max_chars: int = 300) -> Optional[str]:
    if not text:
        return None
    t = text.strip()
    return (t[:max_chars] + "…") if len(t) > max_chars else t

@router.get("/rephrased/search")
def search_rephrased(
    q: str = Query(..., min_length=1, description="FTS5 query, e.g. 'flare window' OR crosswind"),
    k: int = Query(20, ge=1, le=100),
    include_source: bool = Query(False, description="Include full source chunk text"),
    excerpt_chars: int = Query(300, ge=80, le=1200),
):
    """
    Search rephrased artifacts (lesson/qa/fact) via FTS5, reranked by FTS bm25.
    Also LEFT JOIN to raw docs by 'source_id' == docs.source to provide an excerpt.
    """
    sql = """
        SELECT
            r.id, r.kind, r.text, r.source_id, r.tags, r.meta,
            bm25(f) AS score,
            d.text AS source_text
        FROM docs_rephrased_fts f
        JOIN docs_rephrased r ON r.id = f.rowid
        LEFT JOIN docs d ON d.source = r.source_id
        WHERE docs_rephrased_fts MATCH ?
        ORDER BY bm25(f)        -- lower is better in SQLite's bm25()
        LIMIT ?
    """
    with _connect(DB_PATH) as cx:
        rows = cx.execute(sql, (q, min(k, 100))).fetchall()

    results: List[Dict[str, Any]] = []
    for r in rows:
        meta = {}
        try:
            meta = json.loads(r["meta"] or "{}")
        except Exception:
            meta = {}

        src_txt = r["source_text"]
        results.append({
            "id": r["id"],
            "kind": r["kind"],               # 'lesson' | 'qa' | 'fact'
            "text": r["text"],
            "source_id": r["source_id"],     # e.g. 'EUCASS2019-0633.md#part0'
            "tags": r["tags"] or "",
            "score": float(r["score"]) if r["score"] is not None else None,
            "meta": meta,
            "source_excerpt": (src_txt if include_source else _excerpt(src_txt, excerpt_chars)),
        })
    return {"q": q, "k": k, "results": results}

@router.get("/rephrased/by_id")
def rephrased_by_id(id: int = Query(..., ge=1)):
    """
    Fetch one rephrased row + its source doc chunk text.
    """
    sql = """
        SELECT
            r.id, r.kind, r.text, r.source_id, r.tags, r.meta,
            d.text AS source_text
        FROM docs_rephrased r
        LEFT JOIN docs d ON d.source = r.source_id
        WHERE r.id = ?
        LIMIT 1
    """
    with _connect(DB_PATH) as cx:
        row = cx.execute(sql, (id,)).fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="not_found")

    meta = {}
    try:
        meta = json.loads(row["meta"] or "{}")
    except Exception:
        meta = {}

    return {
        "id": row["id"],
        "kind": row["kind"],
        "text": row["text"],
        "source_id": row["source_id"],
        "tags": row["tags"] or "",
        "meta": meta,
        "source_text": row["source_text"],  # full chunk; client can truncate
    }