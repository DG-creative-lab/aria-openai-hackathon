# backend/tools/docs_ingest.py
"""
Ingest Space Rider Markdown docs into SQLite + FTS5 (flat schema expected by retriever/NLI).

Usage:
  uv run python backend/tools/docs_ingest.py \
    --input data/docs/processed \
    --db data/aria.sqlite
"""
from __future__ import annotations
import argparse, hashlib, os, sqlite3, sys
from pathlib import Path
from typing import Iterable, Tuple

# ---------- Paths ----------
BACKEND_DIR = Path(__file__).resolve().parents[1]   # .../backend
REPO_ROOT   = BACKEND_DIR.parent                    # repo root

DEFAULT_INPUT_MD = REPO_ROOT / "data" / "docs" / "processed"
DEFAULT_DB       = Path(os.getenv("ARIA_DB_PATH", REPO_ROOT / "data" / "aria.sqlite"))

# ---------- DB & schema (flat) ----------
SCHEMA_SQL = """
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;

-- one row per chunk (what retriever/nli_guard expect)
CREATE TABLE IF NOT EXISTS docs (
  id        INTEGER PRIMARY KEY,     -- rowid, stable handle
  doc_id    TEXT NOT NULL,           -- sha256 of full file contents
  chunk_ix  INTEGER NOT NULL,        -- 0..N-1
  text      TEXT NOT NULL,           -- chunk text
  source    TEXT,                    -- filename#partN
  added_at  DATETIME DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_docs_doc_chunk ON docs(doc_id, chunk_ix);
CREATE INDEX IF NOT EXISTS idx_docs_source ON docs(source);

-- FTS over docs.text; rowid == docs.id (content table)
CREATE VIRTUAL TABLE IF NOT EXISTS docs_fts USING fts5(
  text,
  content='docs',
  content_rowid='id',
  tokenize='unicode61'
);

-- keep FTS in sync
CREATE TRIGGER IF NOT EXISTS docs_ai AFTER INSERT ON docs BEGIN
  INSERT INTO docs_fts(rowid, text) VALUES (new.id, new.text);
END;
CREATE TRIGGER IF NOT EXISTS docs_ad AFTER DELETE ON docs BEGIN
  INSERT INTO docs_fts(docs_fts, rowid, text) VALUES ('delete', old.id, old.text);
END;
CREATE TRIGGER IF NOT EXISTS docs_au AFTER UPDATE ON docs BEGIN
  INSERT INTO docs_fts(docs_fts, rowid, text) VALUES ('delete', old.id, old.text);
  INSERT INTO docs_fts(rowid, text) VALUES (new.id, new.text);
END;
"""

def open_db(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.executescript(SCHEMA_SQL)
    return conn

# ---------- Helpers ----------
def sha256_bytes(data: bytes) -> str:
    h = hashlib.sha256(); h.update(data); return h.hexdigest()

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")

def chunk_text(text: str, chunk_chars: int = 1800, overlap: int = 200) -> Iterable[str]:
    n, i = len(text), 0
    while i < n:
        j = min(i + chunk_chars, n)
        yield text[i:j]
        if j >= n: break
        i = max(j - overlap, i + 1)

def upsert_doc(conn: sqlite3.Connection, path: Path, text: str,
               chunk_chars: int, overlap: int) -> Tuple[str, int]:
    data   = text.encode("utf-8", errors="ignore")
    doc_id = sha256_bytes(data)
    # Remove old rows for this doc_id (re-ingest case)
    conn.execute("DELETE FROM docs WHERE doc_id=?", (doc_id,))
    # Insert chunks
    count = 0
    src_prefix = path.name
    for idx, chunk in enumerate(chunk_text(text, chunk_chars, overlap)):
        conn.execute(
            "INSERT INTO docs(doc_id, chunk_ix, text, source) VALUES (?,?,?,?)",
            (doc_id, idx, chunk, f"{src_prefix}#part{idx}")
        )
        count += 1
    conn.commit()
    return doc_id, count

# ---------- Main ----------
def main():
    ap = argparse.ArgumentParser(description="Ingest Markdown into SQLite FTS5 (flat schema)")
    ap.add_argument("--input", type=Path, default=DEFAULT_INPUT_MD, help="File or folder of .md")
    ap.add_argument("--db",    type=Path, default=DEFAULT_DB,       help="SQLite database path")
    ap.add_argument("--chunk-chars", type=int, default=1800, help="Approx chars per chunk")
    ap.add_argument("--overlap",     type=int, default=200,  help="Char overlap between chunks")
    args = ap.parse_args()

    conn = open_db(args.db)
    print(f"📚 DB: {args.db}")

    # Collect .md inputs
    if args.input.is_file() and args.input.suffix.lower() == ".md":
        md_files = [args.input]
    elif args.input.is_dir():
        # non-recursive; switch to rglob if you want recursion
        md_files = sorted(args.input.glob("*.md"))
    else:
        print(f"❌ Input not found or not a .md: {args.input}"); sys.exit(1)

    if not md_files:
        print("⚠️  No Markdown files to ingest."); sys.exit(0)

    total_chunks = 0
    for md in md_files:
        try:
            txt = read_text(md)
            doc_id, n = upsert_doc(conn, md, txt, args.chunk_chars, args.overlap)
            total_chunks += n
            print(f"✅ {md.name}: chunks={n} doc_id={doc_id[:8]}…")
        except Exception as e:
            print(f"❌ Failed ingesting {md.name}: {e}")

    print(f"\n🎉 Ingestion complete. Files={len(md_files)}, Chunks={total_chunks}")
    conn.close()

if __name__ == "__main__":
    main()