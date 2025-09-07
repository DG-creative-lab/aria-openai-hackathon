"""
Ingest rephrased artifacts (lesson/qa/fact) into SQLite + FTS5.

Input JSONL lines (from rephrase_docs.py) look like:
{
  "source_id": "SomeDoc.md#part12",
  "tags": ["spacerider","gnc"],
  "section_path": ["3. Guidance", "3.1 Crosswind"],
  "lesson_card": [...],
  "qa": [{"q":"...","a":"..."}, ...],
  "facts_json": [{"name":"...","value":"...","unit":"m/s","condition":"...","source_hint":"..."}]
}

This script will:
  - upsert into docs_rephrased with kind ∈ {'lesson','qa','fact'}
  - link to original chunk via docs.source == source_id (if present) to fill (doc_id, chunk_ix)
  - store section_path for auditing
  - ensure FTS is updated
  - dedupe via UNIQUE(kind, source_id, text)

Usage:
 uv run python -m backend.tools.ingest_rephrased \
  --jsonl data/docs/rephrased.jsonl \
  --db data/aria.sqlite \
  --wipe \
  --store-embeddings \
  --batch 500

"""

from __future__ import annotations
import argparse, json, sqlite3, sys
from pathlib import Path
from typing import Dict, Tuple, List

def _as_bytes_float32(vec) -> bytes:
    import numpy as np
    arr = np.asarray(vec, dtype="float32")
    return arr.tobytes()

def _load_embedder():
    # loads only if --store-embeddings
    from backend.aria.memory.embeddings import embed_texts
    return embed_texts

SCHEMA_SQL = """
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;

-- Flat docs table should already exist (from docs_ingest.py):
--   docs(id INTEGER PK, doc_id TEXT, chunk_ix INT, text TEXT, source TEXT)
-- We will LEFT JOIN on docs.source = source_id to enrich (doc_id, chunk_ix).

CREATE TABLE IF NOT EXISTS docs_rephrased(
  id           INTEGER PRIMARY KEY,
  kind         TEXT NOT NULL CHECK(kind IN ('lesson','qa','fact')),
  text         TEXT NOT NULL,
  meta         JSON,                   -- original JSON (qa/fact/lesson_card block)
  source_id    TEXT,                   -- filename#partN (matches docs.source)
  doc_id       TEXT,                   -- from docs.doc_id when available
  chunk_ix     INTEGER,                -- from docs.chunk_ix when available
  tags         TEXT,                   -- comma-separated tags (normalized lowercase)
  section_path JSON,                   -- JSON array of headings (optional)
  embedding    BLOB,                   -- optional vector bytes (float32)
  created_at   REAL DEFAULT (strftime('%s','now'))
);

-- De-dupe safeguard: same kind + same source chunk + same content ⇒ unique
CREATE UNIQUE INDEX IF NOT EXISTS uq_docs_rephrased_uni
  ON docs_rephrased(kind, source_id, text);

-- FTS index
CREATE VIRTUAL TABLE IF NOT EXISTS docs_rephrased_fts
  USING fts5(text, content='docs_rephrased', content_rowid='id');

-- Triggers keep FTS in sync
CREATE TRIGGER IF NOT EXISTS docs_rephrased_ai AFTER INSERT ON docs_rephrased BEGIN
  INSERT INTO docs_rephrased_fts(rowid, text) VALUES (new.id, new.text);
END;
CREATE TRIGGER IF NOT EXISTS docs_rephrased_ad AFTER DELETE ON docs_rephrased BEGIN
  INSERT INTO docs_rephrased_fts(docs_rephrased_fts, rowid, text) VALUES ('delete', old.id, old.text);
END;
CREATE TRIGGER IF NOT EXISTS docs_rephrased_au AFTER UPDATE ON docs_rephrased BEGIN
  INSERT INTO docs_rephrased_fts(docs_rephrased_fts, rowid, text) VALUES ('delete', old.id, old.text);
  INSERT INTO docs_rephrased_fts(rowid, text) VALUES (new.id, new.text);
END;

-- Indices to speed link-backs and tag filters
CREATE INDEX IF NOT EXISTS idx_docs_rephrased_source ON docs_rephrased(source_id);
CREATE INDEX IF NOT EXISTS idx_docs_rephrased_tags   ON docs_rephrased(tags);
"""

def _open_db(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    cx = sqlite3.connect(str(db_path))
    cx.executescript(SCHEMA_SQL)
    return cx

def _load_source_map(cx: sqlite3.Connection) -> Dict[str, Tuple[str, int]]:
    """
    Build a map: source_id -> (doc_id, chunk_ix) from docs table.
    """
    src_map: Dict[str, Tuple[str, int]] = {}
    try:
        cur = cx.execute("SELECT source, doc_id, chunk_ix FROM docs")
        for source, doc_id, chunk_ix in cur.fetchall():
            if source:
                src_map[source] = (doc_id, int(chunk_ix))
    except sqlite3.OperationalError:
        # docs table may not exist yet; that's fine—linking stays NULL
        pass
    return src_map

def _rows_from_obj(obj: dict, src_map: Dict[str, Tuple[str,int]]) -> List[Tuple]:
    sid = str(obj.get("source_id", "") or "")
    # normalize tags to lowercase and join
    tags = ",".join([str(t).lower().strip() for t in (obj.get("tags") or []) if str(t).strip()])
    section_path_json = json.dumps(obj.get("section_path", []) or [], ensure_ascii=False)

    doc_id, chunk_ix = None, None
    if sid in src_map:
        doc_id, chunk_ix = src_map[sid]

    rows: List[Tuple] = []

    # LESSON_CARD
    lesson_card = obj.get("lesson_card") or []
    if isinstance(lesson_card, list) and any(str(b).strip() for b in lesson_card):
        text = "\n".join(b.strip() for b in lesson_card if str(b).strip())
        meta = json.dumps({"lesson_card": lesson_card}, ensure_ascii=False)
        rows.append(("lesson", text, meta, sid, doc_id, chunk_ix, tags, section_path_json, None))

    # QA
    for qa in obj.get("qa") or []:
        q = (qa.get("q", "") or "").strip()
        a = (qa.get("a", "") or "").strip()
        if not (q and a):
            continue
        text = f"Q: {q}\nA: {a}"
        meta = json.dumps(qa, ensure_ascii=False)
        rows.append(("qa", text, meta, sid, doc_id, chunk_ix, tags, section_path_json, None))

    # FACTS
    for fact in obj.get("facts_json") or []:
        name = (fact.get("name", "") or "").strip()
        if not name:
            continue
        val  = str(fact.get("value", "")).strip()
        unit = str(fact.get("unit", "") or "").strip()
        line_txt = f"{name}: {val}{(' ' + unit) if unit else ''}"
        meta = json.dumps(fact, ensure_ascii=False)
        rows.append(("fact", line_txt, meta, sid, doc_id, chunk_ix, tags, section_path_json, None))

    return rows

def main():
    ap = argparse.ArgumentParser(description="Ingest rephrased.jsonl → docs_rephrased (+ FTS, dedupe, linking).")
    ap.add_argument("--jsonl", type=Path, default=Path("data/docs/rephrased.jsonl"))
    ap.add_argument("--db",    type=Path, default=Path("data/aria.sqlite"))
    ap.add_argument("--batch", type=int, default=500, help="Insert in batches of N")
    ap.add_argument("--store-embeddings", action="store_true", help="Compute and store embedding for each row.text")
    ap.add_argument("--wipe", action="store_true", help="DELETE FROM docs_rephrased before inserting")
    args = ap.parse_args()

    if not args.jsonl.exists():
        print(f"❌ JSONL not found: {args.jsonl}"); sys.exit(1)

    cx = _open_db(args.db)

    if args.wipe:
        cx.execute("DELETE FROM docs_rephrased")
        cx.execute("DELETE FROM docs_rephrased_fts")
        cx.commit()
        print("↻ Wiped docs_rephrased and FTS")

    # Build source_id -> (doc_id, chunk_ix) map once
    src_map = _load_source_map(cx)
    have_linking = bool(src_map)

    # Optional embedder
    embed_fn = None
    if args.store_embeddings:
        try:
            embed_fn = _load_embedder()
            print("🔎 Embeddings: enabled (CPU)")
        except Exception as e:
            print(f"⚠️  Embeddings disabled (load failed): {e}")

    to_insert: List[Tuple] = []
    n_lines = 0
    n_rows  = 0

    with args.jsonl.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            n_lines += 1
            try:
                obj = json.loads(line)
            except Exception as e:
                print(f"⚠️  Skipping malformed JSON line {n_lines}: {e}")
                continue

            rows = _rows_from_obj(obj, src_map)
            if not rows:
                continue

            # If embedding enabled, compute per-row text embeddings for this small list
            if embed_fn is not None:
                try:
                    texts = [r[1] for r in rows]  # text at index 1
                    vecs = embed_fn(texts)       # returns np.ndarray [N, D] (normalized)
                    blobs = [_as_bytes_float32(v) for v in vecs]
                except Exception as e:
                    print(f"⚠️  Embedding failed for line {n_lines}: {e}")
                    blobs = [None] * len(rows)
            else:
                blobs = [None] * len(rows)

            # Append rows with embedding blobs replacing last field
            for row, blob in zip(rows, blobs):
                # row = (kind, text, meta, sid, doc_id, chunk_ix, tags, section_path_json, None)
                row = list(row)
                row[-1] = blob  # set embedding
                to_insert.append(tuple(row))
                n_rows += 1

            # batch insert
            if len(to_insert) >= args.batch:
                cx.executemany(
                    """
                    INSERT OR IGNORE INTO docs_rephrased
                      (kind, text, meta, source_id, doc_id, chunk_ix, tags, section_path, embedding)
                    VALUES (?,?,?,?,?,?,?,?,?)
                    """,
                    to_insert
                )
                cx.commit()
                to_insert.clear()

    # flush remaining
    if to_insert:
        cx.executemany(
            """
            INSERT OR IGNORE INTO docs_rephrased
              (kind, text, meta, source_id, doc_id, chunk_ix, tags, section_path, embedding)
            VALUES (?,?,?,?,?,?,?,?,?)
            """,
            to_insert
        )
        cx.commit()

    # Stats
    total = cx.execute("SELECT COUNT(*) FROM docs_rephrased").fetchone()[0]
    by_kind = dict(cx.execute("SELECT kind, COUNT(*) FROM docs_rephrased GROUP BY kind").fetchall() or [])
    linked = cx.execute("SELECT COUNT(*) FROM docs_rephrased WHERE doc_id IS NOT NULL").fetchone()[0]
    cx.close()

    print(f"✅ Ingested: lines={n_lines}, rows_inserted={n_rows} (dedup via UNIQUE)")
    print(f"   by kind: {by_kind}")
    print(f"   linked rows (doc_id/chunk_ix found): {linked}  [{'OK' if have_linking else 'no docs table found'}]")
    print(f"   total rows in docs_rephrased: {total}")

if __name__ == "__main__":
    main()