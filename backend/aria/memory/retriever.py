# backend/aria/memory/retriever.py
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Sequence, Tuple
import sqlite3
import time
import numpy as np

from .embeddings import embed_texts
from .nli_guard import guard_rephrased_text


@dataclass
class RetrievalResult:
    text: str
    source: str          # e.g., "doc:SRSAOUsersGuide#12" or "repr_lesson:SRSAOUsersGuide.md#p12"
    score: float
    kind: str            # 'doc' | 'lesson' | 'repr_lesson' | 'repr_qa' | 'repr_fact' | 'episodic'


class Retriever:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _connect(self) -> sqlite3.Connection:
        cx = sqlite3.connect(self.db_path)
        cx.row_factory = sqlite3.Row
        return cx

    # ---------- helpers ----------

    @staticmethod
    def _blank(query: Optional[str]) -> bool:
        return not query or not query.strip()

    def _materialize_vectors(
        self,
        rows: Sequence[sqlite3.Row],
        text_field: str = "text",
    ) -> np.ndarray:
        """
        Build an [N, D] matrix of vectors using stored embeddings when present;
        otherwise encode the provided text field.
        """
        vectors: List[Optional[np.ndarray]] = []
        missing_texts: List[str] = []
        missing_idx: List[int] = []

        for i, r in enumerate(rows):
            blob = r["embedding"] if "embedding" in r.keys() else None
            if blob is not None:
                # Stored as float32 bytes
                v = np.frombuffer(blob, dtype="float32")
                vectors.append(v)
            else:
                vectors.append(None)
                # Fallback to a text field (default 'text')
                txt = (r[text_field] or "") if text_field in r.keys() else ""
                missing_texts.append(txt)
                missing_idx.append(i)

        if missing_texts:
            enc = embed_texts(missing_texts)  # returns list[np.ndarray], normalized
            for i, v in zip(missing_idx, enc):
                vectors[i] = v

        if any(v is None for v in vectors):
            raise ValueError("Retriever._materialize_vectors: some vectors are still None")

        # Ensure consistent shapes and stack
        return np.vstack([np.asarray(v, dtype=np.float32) for v in vectors])

    # ---------- LESSONS (distilled, cross-run) ----------

    def lessons(self, query: str, k: int = 3, prefer_recent: bool = True) -> List[RetrievalResult]:
        """
        Hybrid: FTS prefilter + vector rerank over lessons (title+body).
        Optionally gives a light recency boost.
        """
        # Avoid FTS5 MATCH '' which throws: "fts5: syntax error near "" "
        if self._blank(query):
            return []

        with self._connect() as cx:
            rows = cx.execute(
                """
                SELECT l.id, l.title, l.body, l.tags, l.embedding, l.created_at
                FROM lessons_fts f
                JOIN lessons l ON l.id = f.rowid
                WHERE lessons_fts MATCH ?
                ORDER BY bm25(lessons_fts)
                LIMIT 50
                """,
                (query,),
            ).fetchall()

            # If no lexical hits, take most-recent candidates and let vectors do the work
            if not rows:
                rows = cx.execute(
                    "SELECT id, title, body, tags, embedding, created_at "
                    "FROM lessons ORDER BY created_at DESC LIMIT 32"
                ).fetchall()

        if not rows:
            return []

        # Vectorize (use stored embedding when present, else encode BODY)
        M = self._materialize_vectors(rows, text_field="body")

        qv = embed_texts([query])[0]  # normalized
        sims = M @ qv                 # cosine == dot (normalized vectors)

        # Optional recency boost (0..1 scaled → *0.05)
        boost = np.zeros(len(rows), dtype=np.float32)
        if prefer_recent:
            ts = np.array([float(r["created_at"] or 0.0) for r in rows], dtype=np.float32)
            if ts.size > 0 and ts.ptp() > 0:
                rec = (ts - ts.min()) / (ts.ptp() + 1e-6)
                boost = 0.05 * rec

        scored: List[Tuple[sqlite3.Row, float]] = [
            (r, float(s) + float(b)) for r, s, b in zip(rows, sims, boost)
        ]
        ranked = sorted(scored, key=lambda x: x[1], reverse=True)[:k]

        out: List[RetrievalResult] = []
        for r, s in ranked:
            title = (r["title"] or "").strip()
            body = (r["body"] or "").strip()
            text = (title + "\n" + body) if title else body
            out.append(
                RetrievalResult(
                    text=text,
                    source=f"lesson:{r['id']}",
                    score=float(s),
                    kind="lesson",
                )
            )
        return out

    # ---------- RAW DOCS (manual chunks) ----------

    def docs(self, query: str, k: int = 3) -> List[RetrievalResult]:
        if self._blank(query):
            return []

        with self._connect() as cx:
            # Backward-compatible query:
            # some shipped DBs have docs.embedding, older ones do not.
            try:
                rows = cx.execute(
                    """
                    SELECT d.id, d.text, d.source, d.embedding
                    FROM docs_fts f
                    JOIN docs d ON d.id = f.rowid
                    WHERE docs_fts MATCH ?
                    ORDER BY bm25(docs_fts)
                    LIMIT 50
                    """,
                    (query,),
                ).fetchall()
            except sqlite3.OperationalError as e:
                if "no such column: d.embedding" not in str(e):
                    raise
                rows = cx.execute(
                    """
                    SELECT d.id, d.text, d.source, NULL AS embedding
                    FROM docs_fts f
                    JOIN docs d ON d.id = f.rowid
                    WHERE docs_fts MATCH ?
                    ORDER BY bm25(docs_fts)
                    LIMIT 50
                    """,
                    (query,),
                ).fetchall()

        if not rows:
            return []

        # Use stored vectors or encode text
        M = self._materialize_vectors(rows, text_field="text")
        qv = embed_texts([query])[0]
        sims = M @ qv

        ranked = sorted(zip(rows, sims), key=lambda x: float(x[1]), reverse=True)[:k]
        return [
            RetrievalResult(
                text=r["text"],
                source=f"doc:{r['source']}",
                score=float(s),
                kind="doc",
            )
            for (r, s) in ranked
        ]

    # ---------- REPHRASED (preferred: lessons/qa/facts) ----------

    def _rephrased_candidates(self, query: str, limit: int = 64) -> List[sqlite3.Row]:
        if self._blank(query):
            return []
        with self._connect() as cx:
            rows = cx.execute(
                """
                SELECT r.id, r.kind, r.text, r.source_id, r.tags, r.embedding
                FROM docs_rephrased_fts f
                JOIN docs_rephrased r ON r.id = f.rowid
                WHERE docs_rephrased_fts MATCH ?
                ORDER BY bm25(docs_rephrased_fts)
                LIMIT ?
                """,
                (query, limit),
            ).fetchall()
        return rows

    def rephrased(self, query: str, k: int = 5) -> List[RetrievalResult]:
        rows = self._rephrased_candidates(query, limit=64)
        if not rows:
            return []

        qv = embed_texts([query])[0]  # normalized
        M = self._materialize_vectors(rows, text_field="text")
        sims = M @ qv

        # Prefer rephrased lessons > QA > facts slightly
        kind_w = {"lesson": 1.15, "qa": 1.05, "fact": 1.0}
        scored: List[Tuple[sqlite3.Row, float]] = []
        for r, s in zip(rows, sims):
            w = kind_w.get(r["kind"], 1.0)
            scored.append((r, float(s) * w))

        ranked = sorted(scored, key=lambda x: x[1], reverse=True)[:k]
        out: List[RetrievalResult] = []
        for r, s in ranked:
            out.append(
                RetrievalResult(
                    text=r["text"],
                    source=f"repr_{r['kind']}:{r['source_id']}",
                    score=float(s),
                    kind=f"repr_{r['kind']}",
                )
            )
        return out

    def rephrased_guarded(self, query: str, k: int = 5) -> List[RetrievalResult]:
        cand = self._rephrased_candidates(query, limit=64)
        if not cand:
            return []

        qv = embed_texts([query])[0]
        M = self._materialize_vectors(cand, text_field="text")
        sims = M @ qv

        kind_w = {"lesson": 1.15, "qa": 1.05, "fact": 1.0}
        ranked = sorted(
            [(r, float(s) * kind_w.get(r["kind"], 1.0)) for r, s in zip(cand, sims)],
            key=lambda x: x[1],
            reverse=True,
        )

        kept: List[RetrievalResult] = []
        for r, s in ranked:
            sid = r["source_id"] or ""
            ok, _ = guard_rephrased_text(self.db_path, sid, r["text"])
            if ok:
                kept.append(
                    RetrievalResult(
                        text=r["text"],
                        source=f"repr_{r['kind']}:{sid}",
                        score=float(s),
                        kind=f"repr_{r['kind']}",
                    )
                )
            if len(kept) >= k:
                break

        return kept

    # ---------- Episodic (recent run log) ----------

    def episodic_recent(self, seconds: float = 15.0, k: int = 8) -> List[RetrievalResult]:
        now = time.time()
        tmin = now - seconds
        with self._connect() as cx:
            rows = cx.execute(
                """
                SELECT id, ts, kind, text
                FROM episodic_log
                WHERE ts >= ?
                ORDER BY ts DESC
                LIMIT ?
                """,
                (tmin, k),
            ).fetchall()
        return [
            RetrievalResult(
                text=r["text"],
                source=f"episodic:{r['id']} {r['kind']}@{r['ts']:.1f}s",
                score=1.0,
                kind="episodic",
            )
            for r in rows
        ]
