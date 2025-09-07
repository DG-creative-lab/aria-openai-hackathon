#!/usr/bin/env python3
"""
Rephrase pre-chunked docs via Gemini CLI → JSONL.

INPUT JSONL (one per line):
  {
    "source_id": "SomeDoc.md#part12",
    "text": "cleaned chunk text...",
    "tags": ["spacerider","gnc"]   # optional
  }

OUTPUT JSONL (one per line, ready for ingest_rephrased.py):
  {
    "lesson_card": [...],
    "qa": [{"q":"...","a":"..."}, ...],
    "facts_json": [{"name":"...","value":"...","unit":"m/s",...}, ...],
    "source_id": "SomeDoc.md#part12",
    "tags": ["spacerider","gnc"]
  }

Usage:
  uv run python backend/tools/rephrase_with_gemini_cli.py \
  --chunks_jsonl data/docs/chunks.jsonl \
  --out_jsonl    data/docs/rephrased.jsonl \
  --resume \
  --tag spacerider --tag gnc \
  --model gemini-2.5-flash

Env (optional):
  GEMINI_MODEL=gemini-2.5-flash   # default if unset
"""

from __future__ import annotations
import argparse, json, os, re, shutil, subprocess, sys, time
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

JSON_BLOCK = re.compile(r"\{.*\}", re.DOTALL)

PROMPT_HEADER = """You are an aerospace/GNC editor. Rephrase the INPUT into:
1) LESSON_CARD: 3–7 imperative bullets (≤20 words each) for parafoil landing decisions.
2) QA: 5 targeted Q&A pairs a flight engineer would ask in real time.
3) FACTS_JSON: list of JSON objects {name, value, unit, condition(optional), source_hint}.

Rules:
- Preserve facts and units; NO invention.
- Ignore garbled math/figures; extract only operational implications (limits/procedures).
- Prefer concise, operational phrasing over academic prose.
- If a fact is unclear, omit it rather than guessing.

Return STRICT JSON ONLY with keys EXACTLY: lesson_card, qa, facts_json.
"""

def require_gemini_cli() -> str:
    exe = shutil.which("gemini")
    if not exe:
        raise RuntimeError("`gemini` CLI not found. Install with `npm i -g @google/gemini-cli` or `brew install gemini-cli`.")
    return exe

def iter_chunks(chunks_path: Path) -> Iterable[Dict]:
    with chunks_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)

def load_done_ids(out_jsonl: Path) -> set[str]:
    if not out_jsonl.exists():
        return set()
    done = set()
    with out_jsonl.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                obj = json.loads(line)
                sid = obj.get("source_id")
                if sid:
                    done.add(sid)
            except Exception:
                pass
    return done

def call_gemini_cli(prompt: str, model: str) -> dict:
    exe = require_gemini_cli()
    proc = subprocess.run([exe, "-m", model, "-p", prompt], capture_output=True, text=True)
    out = (proc.stdout or "").strip()
    if proc.returncode != 0:
        err = (proc.stderr or "").strip()
        raise RuntimeError(f"gemini CLI error (code {proc.returncode}): {err or out}")

    # Try strict parse; if not, extract first {...} block.
    try:
        return json.loads(out)
    except Exception:
        m = JSON_BLOCK.search(out)
        if not m:
            raise ValueError(f"Model did not return JSON; got:\n{out[:400]}...")
        return json.loads(m.group(0))

def normalize_payload(obj: dict) -> dict:
    # Ensure expected keys/types exist
    lc = obj.get("lesson_card") or []
    qa = obj.get("qa") or []
    fx = obj.get("facts_json") or []
    if not isinstance(lc, list): lc = []
    if not isinstance(qa, list): qa = []
    if not isinstance(fx, list): fx = []

    # Coerce QA entries to {q,a}
    norm_qa = []
    for item in qa:
        if isinstance(item, dict) and "q" in item and "a" in item:
            q, a = item.get("q","").strip(), item.get("a","").strip()
            if q and a:
                norm_qa.append({"q": q, "a": a})
        elif isinstance(item, (list, tuple)) and len(item) == 2:
            q, a = str(item[0]).strip(), str(item[1]).strip()
            if q and a:
                norm_qa.append({"q": q, "a": a})
        else:
            # ignore malformed entries
            continue

    # Trim/fuse lesson card bullets
    norm_lc = [str(b).strip() for b in lc if str(b).strip()]
    # Facts: ensure dicts with name/value (unit optional)
    norm_fx = []
    for f in fx:
        if isinstance(f, dict) and f.get("name"):
            norm_fx.append(f)
    return {"lesson_card": norm_lc, "qa": norm_qa, "facts_json": norm_fx}

def main():
    ap = argparse.ArgumentParser(description="Rephrase pre-chunked JSONL via Gemini CLI → rephrased.jsonl")
    ap.add_argument("--chunks_jsonl", type=Path, required=True, help="Input chunks JSONL")
    ap.add_argument("--out_jsonl",    type=Path, default=Path("data/docs/rephrased.jsonl"))
    ap.add_argument("--tag", action="append", default=[], help="Extra tag(s) to append to per-chunk tags")
    ap.add_argument("--model", default=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"), help="Gemini model id")
    ap.add_argument("--resume", action="store_true", help="Skip source_ids already present in out_jsonl")
    ap.add_argument("--max", type=int, default=0, help="Process at most N records (0 = all)")
    ap.add_argument("--sleep-ms", type=int, default=0, help="Sleep between calls to be gentle on rate limits")
    args = ap.parse_args()

    if not args.chunks_jsonl.exists():
        print(f"❌ Not found: {args.chunks_jsonl}", file=sys.stderr); sys.exit(1)

    args.out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    done_ids = load_done_ids(args.out_jsonl) if args.resume else set()
    failures_log = args.out_jsonl.with_suffix(".failures.log")

    processed = 0
    skipped = 0

    with args.out_jsonl.open("a", encoding="utf-8") as fout:
        for obj in iter_chunks(args.chunks_jsonl):
            sid = obj.get("source_id") or obj.get("id") or ""
            txt = obj.get("text", "").strip()
            tags = list(obj.get("tags", [])) + list(args.tag)

            if not sid or not txt:
                continue
            if args.resume and sid in done_ids:
                skipped += 1
                continue
            if args.max and processed >= args.max:
                break

            prompt = (
                PROMPT_HEADER
                + "\nSOURCE_ID: " + sid
                + "\nINPUT:\n" + txt
                + "\n\nReturn JSON only."
            )

            try:
                raw = call_gemini_cli(prompt, model=args.model)
                norm = normalize_payload(raw)
                norm["source_id"] = sid
                norm["tags"] = tags
                fout.write(json.dumps(norm, ensure_ascii=False) + "\n")
                processed += 1
                if args.sleep_ms:
                    time.sleep(args.sleep_ms / 1000.0)
                if processed % 10 == 0:
                    print(f"… processed {processed}")
            except Exception as e:
                with failures_log.open("a", encoding="utf-8") as flog:
                    flog.write(f"{sid}\nERROR: {e}\n\n")
                print(f"❌ {sid}: {e}")

    print(f"✅ Done → {args.out_jsonl} | processed={processed}, skipped={skipped} (resume={args.resume})")
    print("Next: uv run python backend/tools/ingest_rephrased.py --jsonl data/docs/rephrased.jsonl --db data/aria.sqlite")

if __name__ == "__main__":
    main()