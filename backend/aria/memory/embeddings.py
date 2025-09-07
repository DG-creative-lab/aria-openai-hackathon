from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer

# choose a small CPU model (configurable via env)
_MODEL_NAME = "intfloat/e5-small-v2"  # or sentence-transformers/all-MiniLM-L6-v2
_model = None

def load_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(_MODEL_NAME)
    return _model

def embed_texts(texts: List[str]) -> np.ndarray:
    model = load_model()
    return np.array(model.encode(texts, normalize_embeddings=True), dtype="float32")

def cos_sim(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b))