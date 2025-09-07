"""
Rephrase pre-chunked Markdown (JSONL) into:
  - lesson_card (bullets)
  - qa (Q/A pairs)
  - facts_json (structured)

Reads chunks produced by prepare_md_chunks.py (one JSON per line):
{ "filename": "...", "part": 0, "source_id": "...#part0", "section_path": [...], "text": "...", "char_len": 1234 }

Usage (safe pace for free tier):
  uv run python backend/tools/rephrase_docs.py \
    --chunks_jsonl data/docs/chunks.jsonl \
    --out_jsonl data/docs/rephrased.jsonl \
    --tag spacerider --tag gnc \
    --sleep-ms 700

Resume behavior:
  - If out_jsonl exists, we skip any source_id already present there, and append new lines.
"""

from __future__ import annotations
import argparse, json, os, random, sys, time
from pathlib import Path
from typing import Dict, List, Iterable, Tuple

# load env from .env if present (so GROQ_API_KEY is visible when running directly)
try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv(override=False)
except Exception:
    pass

# Your OpenAI-compatible wrapper that now uses Groq's SDK internally
from backend.aria.agent import call_model

# -------- Prompt --------
PROMPT = """You are an aerospace/GNC editor. Rephrase the INPUT into:
1) LESSON_CARD: 3–7 imperative bullets (≤20 words each) focused on parafoil landing decisions.
2) QA: 5 targeted Q&A pairs a flight engineer would ask in real time.
3) FACTS_JSON: list of JSON objects with fields: name, value, unit, condition(optional), source_hint.

Rules:
- Preserve facts and units; NO invention.
- Ignore unreadable math/garbled LaTeX; extract only operational implications (limits, envelopes, procedures).
- Prefer concise, operational phrasing over academic prose.
- If a fact is unclear, omit it rather than guessing.

Return STRICT JSON with keys: lesson_card, qa, facts_json.
INPUT:
"""

# -------- helpers --------
def _jsonl_iter(path: Path) -> Iterable[dict]:
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)

def _load_done_ids(out_path: Path) -> set[str]:
    done: set[str] = set()
    if out_path.exists():
        try:
            for obj in _jsonl_iter(out_path):
                sid = obj.get("source_id")
                if sid:
                    done.add(str(sid))
        except Exception:
            # if file is partially written, we still keep whatever we could parse
            pass
    return done

def _retry_backoff(attempt: int, base: float = 0.6, cap: float = 8.0) -> None:
    # exponential backoff + jitter
    sleep_s = min(cap, base * (2 ** (attempt - 1)))
    time.sleep(sleep_s * (0.85 + 0.3 * random.random()))

def _force_json(txt: str) -> dict:
    try:
        return json.loads(txt)
    except Exception:
        # greedy brace fallback
        start, end = txt.find("{"), txt.rfind("}")
        if start >= 0 and end > start:
            return json.loads(txt[start:end+1])
        raise

def _messages_for(text: str) -> List[Dict[str, str]]:
    return [
        {"role": "system", "content": "You rephrase technical docs into compact, operational knowledge."},
        {"role": "user", "content": PROMPT + text},
    ]

# -------- main rephrase --------
def rephrase_one(
    text: str,
    source_id: str,
    tags: List[str],
    *,
    max_tokens: int,
    temperature: float,
    retries: int,
) -> dict:
    last_err: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            out = call_model(
                messages=_messages_for(text),
                response_format="json_object",
                max_tokens=max_tokens,
                temperature=temperature,
            )
            obj = _force_json(out)
            obj["source_id"] = source_id
            obj["tags"] = tags
            return obj
        except Exception as e:
            last_err = e
            _retry_backoff(attempt)
    raise RuntimeError(f"LLM call failed after {retries} attempts: {last_err}")

# -------- CLI --------
def main():
    ap = argparse.ArgumentParser(description="Rephrase chunks (JSONL) → lesson_card/qa/facts_json JSONL.")
    ap.add_argument("--chunks_jsonl", type=Path, required=True, help="Input chunks.jsonl from prepare_md_chunks.py")
    ap.add_argument("--out_jsonl",    type=Path, default=Path("data/docs/rephrased.jsonl"))
    ap.add_argument("--tag", action="append", default=[], help="Extra tag(s) to attach")
    ap.add_argument("--sleep-ms", type=int, default=650, help="Throttle between requests (ms)")
    ap.add_argument("--max-tokens", type=int, default=int(os.getenv("LLM_MAX_TOKENS", "900")))
    ap.add_argument("--temperature", type=float, default=float(os.getenv("LLM_TEMPERATURE", "0.2")))
    ap.add_argument("--retries", type=int, default=int(os.getenv("LLM_MAX_RETRIES", "5")))
    ap.add_argument("--sample", type=int, default=0, help="Process only first N chunks (0 = all)")
    ap.add_argument("--overwrite", action="store_true", help="Ignore existing out_jsonl and rewrite from scratch")
    args = ap.parse_args()

    in_path: Path = args.chunks_jsonl
    out_path: Path = args.out_jsonl
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not in_path.exists():
        print(f"❌ chunks_jsonl not found: {in_path}")
        sys.exit(1)

    done_ids: set[str] = set()
    if not args.overwrite:
        done_ids = _load_done_ids(out_path)
        if done_ids:
            print(f"↻ Resuming: {len(done_ids)} source_id already present in {out_path.name}")

    # open out file in append or write mode
    mode = "w" if args.overwrite else "a"
    processed = 0
    skipped = 0
    written = 0

    with out_path.open(mode, encoding="utf-8") as fout:
        for i, obj in enumerate(_jsonl_iter(in_path)):
            if args.sample and i >= args.sample:
                break

            src_id = str(obj.get("source_id", f"{obj.get('filename','?')}#part{obj.get('part','?')}"))
            if (not args.overwrite) and src_id in done_ids:
                skipped += 1
                continue

            text = obj.get("text", "")
            if not text or len(text) < 150:
                skipped += 1
                continue

            try:
                rep = rephrase_one(
                    text=text,
                    source_id=src_id,
                    tags=args.tag,
                    max_tokens=args.max_tokens,
                    temperature=args.temperature,
                    retries=args.retries,
                )
                # carry section_path through for convenience/audit
                if "section_path" in obj:
                    rep["section_path"] = obj["section_path"]
                fout.write(json.dumps(rep, ensure_ascii=False) + "\n")
                fout.flush()
                written += 1
            except Exception as e:
                print(f"❌ {src_id}: {e}")

            processed += 1
            # gentle pacing for free tier (TPM)
            time.sleep(max(0, args.sleep_ms) / 1000.0)

    print(f"✅ Done. processed={processed}  written={written}  skipped={skipped} → {out_path}")

if __name__ == "__main__":
    main()


# sanity check: uv run python -c "from backend.aria.agent import health_check; import json; print(json.dumps(health_check(), indent=2))"
"""
uv run python -m backend.tools.rephrase_docs \
  --chunks_jsonl data/docs/chunks.jsonl \
  --out_jsonl   data/docs/rephrased.jsonl \
  --tag spacerider --tag gnc \
  --sleep-ms 750 --sample 8

"""