# backend/api/routes_knowledge.py
from fastapi import APIRouter, Query
import sqlite3, json

router = APIRouter(prefix="/api/knowledge", tags=["knowledge"])

def _connect(db_path: str):
    return sqlite3.connect(db_path)

DB_PATH = "data/aria.sqlite"  # or from settings

@router.get("/rephrased/search")
def search_rephrased(q: str = Query(..., min_length=1), k: int = 20):
    with _connect(DB_PATH) as cx:
        rows = cx.execute("""
          SELECT id, kind, text, source_id, tags
          FROM docs_rephrased_fts
          JOIN docs_rephrased ON docs_rephrased_fts.rowid = docs_rephrased.id
          WHERE docs_rephrased_fts MATCH ?
          LIMIT 64
        """, (q,)).fetchall()
        # simple rank by length and match density: FTS is already good; keep top-k
        rows = rows[:k]
        out = []
        for (rid, kind, text, sid, tags) in rows:
            # fetch source excerpt
            src = cx.execute("SELECT text FROM docs WHERE doc_id=? LIMIT 1", (sid.split("#")[0].replace(".md",""),)).fetchone()
            excerpt = (src[0][:400] + "…") if src else None
            out.append({
                "id": rid, "kind": kind, "text": text,
                "source_id": sid, "tags": tags, "source_excerpt": excerpt
            })
    return {"q": q, "results": out}

@router.get("/rephrased/by_id")
def rephrased_by_id(id: int):
    with _connect(DB_PATH) as cx:
        r = cx.execute("SELECT id, kind, text, source_id, tags, meta FROM docs_rephrased WHERE id=?", (id,)).fetchone()
        if not r: return {"error": "not_found"}
        rid, kind, text, sid, tags, meta = r
        src = cx.execute("SELECT text FROM docs WHERE doc_id=? LIMIT 1", (sid.split("#")[0].replace(".md",""),)).fetchone()
        return {
            "id": rid, "kind": kind, "text": text,
            "source_id": sid, "tags": tags, "meta": json.loads(meta or "{}"),
            "source_text": src[0] if src else None
        }