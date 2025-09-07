# backend/aria/memory/store.py
from __future__ import annotations
import sqlite3, json, time
from pathlib import Path

SCHEMA_PATH = Path(__file__).with_name("schema.sql")

def ensure_db(db_path: Path | str):
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as cx:
        schema_sql = SCHEMA_PATH.read_text()
        cx.executescript(schema_sql)
        cx.commit()

def episodic_append(db_path: str, kind: str, text: str, data: dict):
    with sqlite3.connect(db_path) as cx:
        cx.execute("INSERT INTO episodic_log(ts,kind,text,data) VALUES(?,?,?,?)",
                   (time.time(), kind, text, json.dumps(data)))
        rowid = cx.execute("SELECT last_insert_rowid()").fetchone()[0]
        cx.execute("INSERT INTO episodic_fts(rowid, text) VALUES(?,?)", (rowid, text))
        cx.commit()