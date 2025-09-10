# backend/aria/memory/governor.py
from __future__ import annotations
import os, json, re
from typing import Dict, List, Tuple

# Optional LLM summarizer (kept off by default to avoid token burn)
_SUMMARIZER_ENABLED = os.getenv("GOV_USE_LLM_SUMMARY", "0") == "1"
_MODEL_BUDGET_TOKENS = int(os.getenv("CONTEXT_BUDGET_TOKENS", "6000"))  # total prompt tokens
_LOG_GOV = os.getenv("LOG_GOVERNOR", "1") == "1"

# Section priority & soft quotas (percentages; order = importance)
SECTION_ORDER = os.getenv(
    "CONTEXT_SECTION_ORDER",
    "state,recent,lessons,facts,qa,docs"
).split(",")

SECTION_SOFT_QUOTA = {
    # % of total budget to “try” to give each section (flexible)
    "state":   float(os.getenv("BUDGET_PCT_STATE",   "10")),  # state is tiny
    "recent":  float(os.getenv("BUDGET_PCT_RECENT",  "10")),
    "lessons": float(os.getenv("BUDGET_PCT_LESSONS", "40")),
    "facts":   float(os.getenv("BUDGET_PCT_FACTS",   "20")),
    "qa":      float(os.getenv("BUDGET_PCT_QA",      "15")),
    "docs":    float(os.getenv("BUDGET_PCT_DOCS",    "5")),
}

# Hard per-item caps (tokens) before we try to compress/truncate
ITEM_HARD_CAP = {
    "state":   int(os.getenv("CAP_TOK_STATE", "400")),
    "recent":  int(os.getenv("CAP_TOK_RECENT", "220")),
    "lessons": int(os.getenv("CAP_TOK_LESSONS", "350")),
    "facts":   int(os.getenv("CAP_TOK_FACTS", "80")),
    "qa":      int(os.getenv("CAP_TOK_QA", "220")),
    "docs":    int(os.getenv("CAP_TOK_DOCS", "500")),
}

# Final truncate-at tokens if still over after compression
ITEM_ABS_MAX = {
    "state":   int(os.getenv("ABS_MAX_TOK_STATE", "600")),
    "recent":  int(os.getenv("ABS_MAX_TOK_RECENT", "280")),
    "lessons": int(os.getenv("ABS_MAX_TOK_LESSONS", "420")),
    "facts":   int(os.getenv("ABS_MAX_TOK_FACTS", "100")),
    "qa":      int(os.getenv("ABS_MAX_TOK_QA", "280")),
    "docs":    int(os.getenv("ABS_MAX_TOK_DOCS", "650")),
}

# ---------- token estimator ----------
# Fast + consistent (≈ 4 chars/token heuristic)
def rough_tokens(s: str) -> int:
    if not s: return 1
    # tiny boost for lots of newlines / bullets
    nl = s.count("\n")
    return max(1, int(len(s) / 4) + nl // 4)

# ---------- cheap compressors (no LLM) ----------
_BULLET_RE = re.compile(r"^\s*[-*•]\s+")
_Q_RE = re.compile(r"^\s*Q:\s*", re.IGNORECASE)
_A_RE = re.compile(r"^\s*A:\s*", re.IGNORECASE)

def _squash_whitespace(s: str) -> str:
    s = re.sub(r"[ \t]+", " ", s).strip()
    # collapse multiple blank lines
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s

def compress_lesson_item(txt: str) -> str:
    # Keep first 5 bullets, strip long lines, force single-space bullets
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    bullets = []
    for l in lines:
        if _BULLET_RE.match(l):
            bullets.append(_BULLET_RE.sub("- ", l))
        else:
            # turn sentence to bullet if it reads imperative
            if len(bullets) < 1:
                bullets.append(f"- {l}")
    bullets = bullets[:5]
    # truncate very long bullets
    out = []
    for b in bullets:
        if len(b) > 180:
            out.append(b[:177].rstrip() + "…")
        else:
            out.append(b)
    return "\n".join(out) if out else txt

def compress_qa_item(txt: str) -> str:
    # Convert "Q:\nA:" to single line "Q… → A…"
    q = _Q_RE.split(txt, 1)
    if len(q) > 1:
        rest = q[1]
        a = _A_RE.split(rest, 1)
        qtext = a[0].strip()
        atext = a[1].strip() if len(a) > 1 else ""
        one = f"Q: {qtext} → A: {atext}"
        return one[:280] + ("…" if len(one) > 280 else "")
    # fallback: squash
    s = _squash_whitespace(txt)
    return s[:280] + ("…" if len(s) > 280 else "")

def compress_recent_item(txt: str) -> str:
    # recent items are already short; de-noise a bit
    s = _squash_whitespace(txt)
    return s[:240] + ("…" if len(s) > 240 else "")

def compress_fact_item(txt: str) -> str:
    # facts are one-liners; trim to 100 chars
    return txt.strip()[:100] + ("…" if len(txt) > 100 else "")

def compress_docs_item(txt: str) -> str:
    # keep first 3 lines / ~500 chars
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    s = "\n".join(lines[:3])
    if len(s) > 650:
        s = s[:647] + "…"
    return s or (txt[:650] + ("…" if len(txt) > 650 else ""))

def _compress_item(section: str, txt: str) -> str:
    if section == "lessons": return compress_lesson_item(txt)
    if section == "qa":      return compress_qa_item(txt)
    if section == "recent":  return compress_recent_item(txt)
    if section == "facts":   return compress_fact_item(txt)
    if section == "docs":    return compress_docs_item(txt)
    if section == "state":   return _squash_whitespace(txt)[:400]
    return txt

# ---------- optional LLM summarizer ----------
def _summarize_item_llm(section: str, txt: str) -> str:
    if not _SUMMARIZER_ENABLED:
        return txt
    try:
        from ..agent import call_model
        sys_prompt = "You compress technical content into short, lossless one-liners or concise bullet lists."
        user_prompt = (
            f"SECTION={section.upper()}.\n"
            "Rewrite the INPUT as concise bullets or a single one-liner keeping facts, units, and conditions.\n"
            "Avoid invented content; keep it operational.\n"
            "INPUT:\n" + txt
        )
        out = call_model(
            messages=[{"role":"system","content":sys_prompt},
                      {"role":"user","content":user_prompt}],
            response_format=None,
            max_tokens=220,
            temperature=0.0,
        )
        return out.strip() or txt
    except Exception:
        return txt

# ---------- core governor ----------

def apply_budget(
    sections: Dict[str, List[str]],
    total_budget_tokens: int | None = None
) -> Tuple[Dict[str, List[str]], Dict[str, int]]:
    budget = total_budget_tokens or _MODEL_BUDGET_TOKENS

    total_pct = sum(SECTION_SOFT_QUOTA.get(k, 0) for k in SECTION_ORDER) or 1
    soft_tokens = {k: int(budget * SECTION_SOFT_QUOTA.get(k,0) / total_pct) for k in SECTION_ORDER}

    out: Dict[str, List[str]] = {k: [] for k in SECTION_ORDER}  # ensure all canonical keys exist
    used_tokens = 0
    stats = {f"{k}_tok": 0 for k in SECTION_ORDER}

    # pass 1
    for k in SECTION_ORDER:
        items = sections.get(k, []) or []
        if not items:
            continue
        section_soft = max(80, soft_tokens.get(k, 0))
        sec_used = 0
        for item in items:
            if used_tokens >= budget:
                break
            if rough_tokens(item) > ITEM_HARD_CAP.get(k, 99999):
                item = _compress_item(k, item)
                if rough_tokens(item) > ITEM_HARD_CAP.get(k, 99999):
                    item = _summarize_item_llm(k, item)
            if rough_tokens(item) > ITEM_ABS_MAX.get(k, 99999):
                item = item[:ITEM_ABS_MAX[k]*4].rstrip() + "…"

            need = rough_tokens(item)
            if (sec_used + need) > section_soft and (used_tokens + need) > budget:
                break
            if used_tokens + need <= budget:
                out[k].append(item)
                used_tokens += need
                sec_used += need
        stats[f"{k}_tok"] = sec_used

    # pass 2 (spill)
    if used_tokens < budget:
        for k in SECTION_ORDER:
            already = len(out.get(k, []))
            items = (sections.get(k, []) or [])[already:]
            for item in items:
                need = rough_tokens(item)
                if used_tokens + need > budget:
                    break
                out[k].append(item)
                used_tokens += need
                stats[f"{k}_tok"] += need

    stats["total_tokens"] = used_tokens
    if _LOG_GOV:
        print("[governor]", json.dumps({
            "budget": budget,
            "used": used_tokens,
            "by_section": {k: stats.get(f"{k}_tok", 0) for k in SECTION_ORDER}
        }, ensure_ascii=False))
    return out, stats