"""
Prepare Space Rider Markdown for LLM rephrasing:
- cleans noisy artifacts
- splits by Markdown headings (fallback to paragraphs/windows)
- enforces min/target/max sizes
- preserves provenance (filename + part index + section path)
- outputs JSONL (one chunk per line)

Usage:
  uv run python backend/tools/prepare_md_chunks.py \
    --input data/docs/processed \
    --out data/docs/chunks.jsonl \
    --target-chars 3500 --min-chars 600 --max-chars 6000 --overlap 120
"""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from typing import List, Dict

# ---------- cleaning rules ----------
_HEADING = re.compile(r"^(?P<hash>#{1,6})\s+(?P<title>.+?)\s*$", re.MULTILINE)
_PAGE_NUM = re.compile(r"^\s*\d+\s*$", re.MULTILINE)
_FIG_LINE = re.compile(r"^\s*(figure|fig\.)\s*\d+.*$", re.IGNORECASE | re.MULTILINE)
_TBL_LINE = re.compile(r"^\s*table\s*\d+.*$", re.IGNORECASE | re.MULTILINE)
_BRACKET_TAG = re.compile(r"_\[[a-zA-Z]\]_")         # e.g. _[b]_
_NOISY_MATH = re.compile(r"[^\w\s.,;:()/+\-×=*%<>\[\]]{6,}")
_DUP_SPACE = re.compile(r"[ \t]{2,}")

GREEK = {"ϕ":"phi","φ":"phi","θ":"theta","ψ":"psi","µ":"mu","α":"alpha","β":"beta"}

def clean(text: str) -> str:
    for k, v in GREEK.items(): text = text.replace(k, v)
    text = _PAGE_NUM.sub("", text)
    text = _FIG_LINE.sub("", text)
    text = _TBL_LINE.sub("", text)
    text = _BRACKET_TAG.sub("", text)

    kept = []
    for ln in text.splitlines():
        if _NOISY_MATH.search(ln) and len(ln.split()) < 4:
            continue
        kept.append(ln)
    text = "\n".join(kept)
    text = _DUP_SPACE.sub(" ", text)
    return text.strip()

# ---------- chunking ----------
def _split_by_headings(text: str) -> List[Dict]:
    """
    Returns a list of segments with:
      {"start": int, "end": int, "level": int, "title": str}
    Covering each heading-to-next region. If no headings, one segment 0..len(text).
    """
    matches = list(_HEADING.finditer(text))
    if not matches:
        return [{"start":0, "end": len(text), "level":0, "title":"(root)"}]

    segs = []
    for i, m in enumerate(matches):
        a = m.start()
        b = matches[i+1].start() if i+1 < len(matches) else len(text)
        segs.append({
            "start": a,
            "end": b,
            "level": len(m.group("hash")),
            "title": m.group("title").strip()
        })
    return segs

def _section_path_for(idx: int, segs: List[Dict]) -> List[str]:
    # Build hierarchical breadcrumb using previous headings.
    path: List[str] = []
    i = idx
    lvl = segs[i]["level"]
    # Walk backwards collecting parents of decreasing level
    for j in range(i, -1, -1):
        if segs[j]["level"] <= lvl:
            path.insert(0, segs[j]["title"])
            lvl = segs[j]["level"] - 1
            if lvl < 1: break
    return path

def _soft_wrap(text: str, max_chars: int) -> List[str]:
    """If a region is too large, split by blank lines, else by windows."""
    paras = [p for p in re.split(r"\n{2,}", text) if p.strip()]
    out: List[str] = []
    buf: List[str] = []
    cur = 0
    for p in paras:
        if cur + len(p) + 2 <= max_chars:
            buf.append(p); cur += len(p) + 2
        else:
            if buf: out.append("\n\n".join(buf))
            if len(p) <= max_chars:
                buf = [p]; cur = len(p)
            else:
                # hard windowing for giant paragraph
                for i in range(0, len(p), max_chars):
                    out.append(p[i:i+max_chars])
                buf, cur = [], 0
    if buf: out.append("\n\n".join(buf))
    return out

def chunk_markdown(
    text: str, *,
    min_chars: int = 600,
    target_chars: int = 3500,
    max_chars: int = 6000,
    overlap: int = 120
) -> List[str]:
    """
    Prefer heading boundaries; if a heading region exceeds max_chars,
    further split by paragraphs/windows. Ensure a little overlap.
    """
    segs = _split_by_headings(text)
    chunks: List[str] = []
    for i, seg in enumerate(segs):
        region = text[seg["start"]:seg["end"]].strip()
        if len(region) <= max_chars:
            chunks.append(region)
        else:
            chunks += _soft_wrap(region, max_chars=max_chars)

    # Coalesce very small chunks with neighbors, maintain slight overlap
    packed: List[str] = []
    buf = ""
    for i, ch in enumerate(chunks):
        if not buf:
            buf = ch
            continue
        if len(buf) < min_chars:
            buf = (buf + "\n\n" + ch)[:max_chars]
        else:
            if len(buf) > target_chars and len(ch) < min_chars:
                buf = (buf + "\n\n" + ch)[:max_chars]
            else:
                # emit buf with overlap from its tail into next
                tail = buf[-overlap:]
                packed.append(buf)
                buf = (tail + "\n" + ch)[:max_chars]
    if buf:
        packed.append(buf)
    # Ensure we don't emit empties
    return [p for p in (packed or chunks) if len(p.strip()) >= min_chars]

# ---------- main ----------
def main():
    ap = argparse.ArgumentParser(description="Prepare Markdown → cleaned, heading-aware chunks (JSONL).")
    ap.add_argument("--input", type=Path, default=Path("data/docs/processed"))
    ap.add_argument("--out",   type=Path, default=Path("data/docs/chunks.jsonl"))
    ap.add_argument("--target-chars", type=int, default=3500)
    ap.add_argument("--min-chars",    type=int, default=600)
    ap.add_argument("--max-chars",    type=int, default=6000)
    ap.add_argument("--overlap",      type=int, default=120)
    args = ap.parse_args()

    in_dir: Path = args.input
    out_path: Path = args.out
    out_path.parent.mkdir(parents=True, exist_ok=True)

    md_files = sorted(p for p in in_dir.glob("*.md"))
    if not md_files:
        print(f"⚠️  No .md files in {in_dir}")
        return

    written = 0
    with out_path.open("w", encoding="utf-8") as f:
        for md in md_files:
            raw = md.read_text(encoding="utf-8", errors="ignore")
            cleaned = clean(raw)
            # heading segments for section paths
            segs = _split_by_headings(cleaned)
            chunks = chunk_markdown(
                cleaned,
                min_chars=args.min_chars,
                target_chars=args.target_chars,
                max_chars=args.max_chars,
                overlap=args.overlap,
            )
            # emit JSONL
            for i, ch in enumerate(chunks):
                obj = {
                    "filename": md.name,
                    "part": i,
                    "source_id": f"{md.name}#part{i}",
                    "section_path": _section_path_for(min(i, len(segs)-1), segs) if segs else [],
                    "text": ch,
                    "char_len": len(ch),
                }
                f.write(json.dumps(obj, ensure_ascii=False) + "\n")
                written += 1

    print(f"✅ Wrote {written} chunks → {out_path}")

if __name__ == "__main__":
    main()