# backend/aria/memory/nli_guard.py
from __future__ import annotations
import os, re, sqlite3
from functools import lru_cache
from typing import Optional, Tuple
import numpy as np

from .embeddings import embed_texts  # your existing CPU-friendly embeddings

# Optional CrossEncoder NLI (small) if available
_USE_CE = os.getenv("USE_CROSS_ENCODER_NLI", "0") == "1"
_CE_MODEL_NAME = os.getenv("CROSS_ENCODER_NLI_MODEL", "cross-encoder/nli-deberta-v3-small")

_ce = None
def _try_load_cross_encoder():
    global _ce
    if _USE_CE and _ce is None:
        try:
            from sentence_transformers import CrossEncoder
            _ce = CrossEncoder(_CE_MODEL_NAME, device="cpu")
        except Exception:
            _ce = None
    return _ce

_NEG_WORDS = {"no","not","never","none","cannot","can't","won't","without","lack","absent","forbid","forbidden"}

def _negation_flip(a: str, b: str) -> bool:
    """Detect crude negation mismatch between texts."""
    def has_neg(s: str) -> bool:
        toks = {w.lower().strip(".,;:!?()[]") for w in s.split()}
        return any(t in toks for t in _NEG_WORDS)
    return has_neg(a) ^ has_neg(b)

def _jaccard(a: str, b: str) -> float:
    A = {w for w in re.findall(r"[A-Za-z0-9\-]+", a.lower()) if len(w) >= 3}
    B = {w for w in re.findall(r"[A-Za-z0-9\-]+", b.lower()) if len(w) >= 3}
    if not A or not B: return 0.0
    return len(A & B) / float(len(A | B))

def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))

def heuristic_entailment(premise: str, hypothesis: str) -> Tuple[bool, float]:
    """Cheap guard: cosine + jaccard + negation check."""
    # Embed once (normalize is done in embed_texts)
    vecs = embed_texts([premise, hypothesis])
    cos = _cosine(vecs[0], vecs[1])
    jac = _jaccard(premise, hypothesis)
    neg_flip = _negation_flip(premise, hypothesis)
    # thresholds tuned to be conservative
    score = 0.7 * cos + 0.3 * jac - (0.15 if neg_flip else 0.0)
    ok = (cos >= 0.48 and jac >= 0.08 and not neg_flip) or score >= 0.50
    return ok, score

def ce_entailment(premise: str, hypothesis: str) -> Tuple[bool, float]:
    """Optional cross-encoder NLI: return True if ENTAILMENT."""
    ce = _try_load_cross_encoder()
    if ce is None:
        return heuristic_entailment(premise, hypothesis)
    # CrossEncoder returns logits over [contradiction, neutral, entailment]
    logits = ce.predict([(premise, hypothesis)], convert_to_numpy=True)[0]
    # softmax
    exps = np.exp(logits - np.max(logits))
    probs = exps / np.sum(exps)
    entail_p = float(probs[2])
    return entail_p >= 0.55, entail_p

@lru_cache(maxsize=4096)
def fetch_source_text(db_path: str, source_id: str) -> Optional[str]:
    with sqlite3.connect(db_path) as cx:
        cx.row_factory = lambda cur, row: row[0]
        # 1) exact match on filename#partN (how you created source)
        r = cx.execute("SELECT text FROM docs WHERE source = ? LIMIT 1", (source_id,)).fetchone()
        if r: 
            return r
        # 2) relaxed fallback: same file, any part
        base = source_id.split("#", 1)[0]
        r = cx.execute("SELECT text FROM docs WHERE source LIKE ? LIMIT 1", (f"{base}#part%",)).fetchone()
        return r

def guard_rephrased_text(db_path: str, source_id: str, rephrased_text: str) -> Tuple[bool, float]:
    """Return (ok, score). If no source found, be lenient but not reckless."""
    src = fetch_source_text(db_path, source_id)
    if not src:
        # no source found: only do self-consistency (very lenient)
        ok, score = heuristic_entailment(rephrased_text, rephrased_text)
        return ok, score
    # Ensure hypothesis (rephrased) is entailed by premise (source)
    return ce_entailment(src, rephrased_text)