from typing import Dict, List

def rough_tokens(s: str) -> int:
    # fast estimate ≈ 4 chars/token
    return max(1, len(s) // 4)

def trim_sections(sections: Dict[str, List[str]], budget_tokens: int) -> Dict[str, List[str]]:
    order = ["state", "recent", "lessons", "docs"]  # priority
    out = {k: [] for k in sections}
    total = 0
    for k in order:
        for item in sections.get(k, []):
            t = rough_tokens(item)
            if total + t > budget_tokens:
                break
            out[k].append(item); total += t
    return out