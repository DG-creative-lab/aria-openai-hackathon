# backend/aria/memory/tools.py
"""
ReAct-lite tools for ARIA memory:
- doc_search(): prefer rephrased+guarded, fall back to raw docs
- recall_lesson(): search distilled lessons
- tool_router(): parse "tool:XYZ ..." strings and return an observation block

Use cases:
  from backend.aria.memory import tools
  obs_text = tools.doc_search("data/aria.sqlite", "crosswind flare window", k=5)
  # -> add obs_text to the next LLM turn as an observation

CLI:
  uv run python backend/aria/memory/tools.py doc_search --db data/aria.sqlite -q "flare window" -k 5
  uv run python backend/aria/memory/tools.py recall_lesson --db data/aria.sqlite -q "crosswind"
"""
from __future__ import annotations
import argparse, json, re
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

from .retriever import Retriever, RetrievalResult

# -------- format helpers --------

def _pack(items: List[RetrievalResult], label: str) -> str:
    """
    Produce a compact observation block suitable to append to the next prompt.
    """
    lines = [f"[TOOL:{label}] {len(items)} result(s)"]
    for i, r in enumerate(items, 1):
        # Keep lines short; callers can change k if they want more
        text = r.text.strip().replace("\n", " ")
        if len(text) > 260:
            text = text[:257] + "…"
        lines.append(f"{i}) {text}")
        lines.append(f"   (source: {r.source}; score={r.score:.3f})")
    return "\n".join(lines)

def _to_dicts(items: List[RetrievalResult]) -> List[Dict[str, Any]]:
    return [
        {"text": r.text, "source": r.source, "score": r.score, "kind": r.kind}
        for r in items
    ]

# -------- public tools --------

def doc_search(db_path: str, query: str, k: int = 6, prefer_rephrased: bool = True,
               as_json: bool = False) -> str | List[Dict[str, Any]]:
    """
    Search docs: prefer rephrased (lesson/qa/fact) with NLI guard; fall back to raw doc chunks.
    Returns an observation string (default) or JSON list if as_json=True.
    """
    R = Retriever(db_path=db_path)
    items = R.rephrased_guarded(query, k=k) if prefer_rephrased else []
    if not items:
        items = R.docs(query, k=min(3, k))
    return _to_dicts(items) if as_json else _pack(items, "DOC_SEARCH")

def recall_lesson(db_path: str, query: str, k: int = 3, as_json: bool = False) -> str | List[Dict[str, Any]]:
    """
    Search distilled semantic lessons table and return compact bullets.
    """
    R = Retriever(db_path=db_path)
    items = R.lessons(query, k=k)
    return _to_dicts(items) if as_json else _pack(items, "LESSON_RECALL")

# -------- simple router for "tool:..." strings --------

_TOOL_RE = re.compile(r"^\s*tool\s*:\s*([a-zA-Z_]+)\s*(.*)$")

def _parse_kv(rest: str) -> Dict[str, str]:
    """
    Parse 'q="some text" k=5' or 'query=abc k=3' into a dict of strings.
    Supports quoted values.
    """
    out: Dict[str, str] = {}
    # key="quoted value" | key='quoted' | key=bare
    for m in re.finditer(r'(\w+)\s*=\s*("([^"]*)"|\'([^\']*)\'|(\S+))', rest):
        k = m.group(1)
        v = m.group(3) or m.group(4) or m.group(5) or ""
        out[k] = v
    return out

def tool_router(db_path: str, request: str) -> Tuple[str, str]:
    """
    Parse a free-form 'tool:doc_search q="flare window" k=5' string and run the tool.
    Returns (label, observation_text). Unknown tool → ("UNKNOWN", notice).
    """
    m = _TOOL_RE.match(request or "")
    if not m:
        return "UNKNOWN", "[TOOL:UNKNOWN] Could not parse tool request."

    name = m.group(1).lower()
    kv = _parse_kv(m.group(2) or "")
    q = kv.get("q") or kv.get("query") or ""
    k = int(kv.get("k", "5"))

    if name == "doc_search":
        return "DOC_SEARCH", doc_search(db_path, q, k=k, prefer_rephrased=True, as_json=False)
    if name == "lesson" or name == "recall_lesson":
        return "LESSON_RECALL", recall_lesson(db_path, q, k=min(k, 5), as_json=False)

    return "UNKNOWN", f"[TOOL:UNKNOWN] {name} is not supported."

# -------- CLI --------

def _cli():
    ap = argparse.ArgumentParser(description="ARIA ReAct-lite tools (doc search / lesson recall)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    ap_doc = sub.add_parser("doc_search", help="Search rephrased/docs")
    ap_doc.add_argument("--db", required=True)
    ap_doc.add_argument("-q", "--query", required=True)
    ap_doc.add_argument("-k", type=int, default=6)
    ap_doc.add_argument("--json", action="store_true")

    ap_lsn = sub.add_parser("recall_lesson", help="Search distilled lessons")
    ap_lsn.add_argument("--db", required=True)
    ap_lsn.add_argument("-q", "--query", required=True)
    ap_lsn.add_argument("-k", type=int, default=3)
    ap_lsn.add_argument("--json", action="store_true")

    ap_rt = sub.add_parser("router", help='Parse & run: e.g. tool:doc_search q="flare window" k=5')
    ap_rt.add_argument("--db", required=True)
    ap_rt.add_argument("--request", required=True)

    args = ap.parse_args()
    if args.cmd == "doc_search":
        out = doc_search(args.db, args.query, k=args.k, as_json=args.json)
    elif args.cmd == "recall_lesson":
        out = recall_lesson(args.db, args.query, k=args.k, as_json=args.json)
    else:
        _, out = tool_router(args.db, args.request)

    if isinstance(out, str):
        print(out)
    else:
        print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    _cli()