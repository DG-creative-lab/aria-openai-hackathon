from typing import Dict, List
from .retriever import Retriever, RetrievalResult

def build_working_memory(db_path: str, state_summary: str, query: str) -> Dict[str, List[str]]:
    R = Retriever(db_path)
    recent = R.episodic_recent(seconds=20, k=8)
    docs   = R.docs(query, k=2)
    lessons= R.lessons(query, k=1)
    docsR  = R.rephrased_guarded(query, db_path=self.db_path, k=4) or R.docs(query, k=2)

    return {
        "state": [state_summary],
        "recent": [r.text for r in recent],
        "docs": [f"{d.text}\n(SOURCE: {d.source})" for d in docs],
        "lessons": [l.text for l in lessons],
    }