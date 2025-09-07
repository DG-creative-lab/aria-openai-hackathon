-- episodic log (current run)
CREATE TABLE IF NOT EXISTS episodic_log (
  id INTEGER PRIMARY KEY,
  ts REAL,                 -- seconds since scenario start
  kind TEXT,               -- 'event' | 'decision' | 'outcome' | 'note'
  text TEXT,               -- human-readable summary or rationale
  data JSON                -- structured payload (telemetry snapshot, plan JSON, etc.)
);
CREATE VIRTUAL TABLE IF NOT EXISTS episodic_fts USING fts5(text, content='episodic_log', content_rowid='id');

-- semantic lessons (cross-run distilled knowledge)
CREATE TABLE IF NOT EXISTS lessons (
  id INTEGER PRIMARY KEY,
  title TEXT,
  body TEXT,               -- concise lesson
  tags TEXT,               -- comma-separated tags (e.g. 'crosswind,flare')
  meta JSON,               -- {scenario: "...", metrics: {...}}
  embedding BLOB           -- vector bytes (optional: store as JSON if simpler)
);
CREATE VIRTUAL TABLE IF NOT EXISTS lessons_fts USING fts5(title, body, tags, content='lessons', content_rowid='id');

-- docs (RAG) from processed manuals
CREATE TABLE IF NOT EXISTS docs (
  id INTEGER PRIMARY KEY,
  doc_id TEXT,             -- e.g. 'SRSAOUsersGuide'
  chunk_ix INTEGER,
  text TEXT,
  source TEXT,             -- filename#page:span
  embedding BLOB
);
CREATE VIRTUAL TABLE IF NOT EXISTS docs_fts USING fts5(text, content='docs', content_rowid='id');

-- Rephrased artifacts derived from docs (BeyondWeb-style)
CREATE TABLE IF NOT EXISTS docs_rephrased (
  id INTEGER PRIMARY KEY,
  kind TEXT NOT NULL,              -- 'lesson' | 'qa' | 'fact'
  text TEXT NOT NULL,              -- compact content (lesson bullets, QA, fact line)
  meta JSON,                       -- original JSON block (for QA/facts detail)
  source_id TEXT,                  -- e.g. 'SRSAOUsersGuide.md#part12'
  doc_id TEXT,                     -- normalized doc id (e.g., 'SRSAOUsersGuide')
  chunk_ix INTEGER,                -- optional: numeric chunk index if known
  tags TEXT,                       -- comma-separated tags
  embedding BLOB,                  -- optional: stored vector (float32 bytes)
  created_at REAL DEFAULT (strftime('%s','now'))
);

-- FTS index for full-text search
CREATE VIRTUAL TABLE IF NOT EXISTS docs_rephrased_fts
USING fts5(text, content='docs_rephrased', content_rowid='id');

-- Triggers to keep FTS in sync
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

-- Helpful indexes
CREATE INDEX IF NOT EXISTS idx_docs_rephrased_kind ON docs_rephrased(kind);
CREATE INDEX IF NOT EXISTS idx_docs_rephrased_doc ON docs_rephrased(doc_id, chunk_ix);
CREATE INDEX IF NOT EXISTS idx_docs_rephrased_tags ON docs_rephrased(tags);
CREATE INDEX IF NOT EXISTS idx_docs_rephrased_source ON docs_rephrased(source_id);