from dataclasses import dataclass
from typing import List, Tuple
import sqlite3, json, time
import numpy as np
from .embeddings import embed_texts, cos_sim
from .nli_guard import guard_rephrased_text

@dataclass
class RetrievalResult:
    text: str
    source: str
    score: float
    kind: str   # 'doc' | 'lesson' | 'episodic'

class Retriever:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def docs(self, query: str, k=3) -> List[RetrievalResult]:
        # FTS first
        with self._connect() as cx:
            rows = cx.execute("SELECT id, text, source FROM docs_fts WHERE docs_fts MATCH ? LIMIT 25", (query,)).fetchall()
        texts = [r[1] for r in rows]
        if not texts: return []
        qv = embed_texts([query])[0]; M = embed_texts(texts)
        sims = M @ qv
        scored = sorted(zip(rows, sims), key=lambda x: x[1], reverse=True)[:k]
        return [RetrievalResult(text=r[1], source=r[2], score=float(s), kind="doc") for (r, s) in scored]

    def lessons(self, query: str, k=2) -> List[RetrievalResult]:
        with self._connect() as cx:
            rows = cx.execute("SELECT id, title, body, tags FROM lessons_fts WHERE lessons_fts MATCH ? LIMIT 50", (query,)).fetchall()
        texts = [f"{r[1]} :: {r[2]}" for r in rows]
        if not texts: return []
        qv = embed_texts([query])[0]; M = embed_texts(texts)
        sims = M @ qv
        scored = sorted(zip(rows, sims), key=lambda x: x[1], reverse=True)[:k]
        out = []
        for (r, s) in scored:
            out.append(RetrievalResult(text=f"{r[1]} — {r[2]}", source=f"lesson:{r[0]} tags={r[3]}", score=float(s), kind="lesson"))
        return out

    def episodic_recent(self, seconds: float = 15.0, k: int = 8) -> List[RetrievalResult]:
        now = time.time()
        tmin = now - seconds
        with self._connect() as cx:
            rows = cx.execute("SELECT id, ts, kind, text FROM episodic_log WHERE ts >= ? ORDER BY ts DESC LIMIT ?", (tmin, k)).fetchall()
        return [RetrievalResult(text=r[3], source=f"episodic:{r[0]} {r[2]}@{r[1]:.1f}s", score=1.0, kind="episodic") for r in rows]
    
    def rephrased(self, query: str, k=5):
        with self._connect() as cx:
            rows = cx.execute("SELECT id, kind, text, source_id, tags FROM docs_rephrased_fts WHERE docs_rephrased_fts MATCH ? LIMIT 64", (query,)).fetchall()
        if not rows: return []
        texts = [r[2] for r in rows]
        qv = embed_texts([query])[0]; M = embed_texts(texts); sims = M @ qv
        # weight by kind: lesson > qa > fact
        kind_w = {"lesson":1.15, "qa":1.05, "fact":1.0}
        scored = sorted([(r, float(s)*kind_w.get(r[1],1.0)) for r,s in zip(rows,sims)], key=lambda x: x[1], reverse=True)[:k]
        return [RetrievalResult(text=r[2], source=f"{r[1]}:{r[3]}", score=s, kind=f"repr_{r[1]}") for (r,s) in scored]
    

def rephrased_guarded(self, query: str, db_path: str, k=5):
    cands = self.rephrased(query, k=12)  # over-sample
    kept = []
    for r in cands:
        # r.source format: 'repr_kind:SOURCE_ID'
        try:
            _, sid = r.source.split(":", 1)
        except:
            sid = r.source
        ok, score = guard_rephrased_text(db_path, sid, r.text)
        if ok:
            kept.append(r)
        if len(kept) >= k:
            break
    return kept