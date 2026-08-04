"""Lightweight in-memory vector store — no Chroma, no torch."""

from __future__ import annotations

import numpy as np

_embedding_model = None
_store = {
    "texts": [],
    "metadatas": [],
    "embeddings": None,
}


def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        from fastembed import TextEmbedding

        # Small ONNX model — fits Render free-tier memory
        _embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
    return _embedding_model


def _embed_documents(texts: list[str]) -> np.ndarray:
    model = get_embedding_model()
    return np.asarray(list(model.embed(texts)), dtype=np.float32)


def _embed_query(query: str) -> np.ndarray:
    model = get_embedding_model()
    return np.asarray(next(model.query_embed(query)), dtype=np.float32)


def create_vector_store(chunks: list[dict]):
    texts = [c["page_content"] for c in chunks]
    metadatas = [c["metadata"] for c in chunks]
    embeddings = _embed_documents(texts)

    _store["texts"] = texts
    _store["metadatas"] = metadatas
    _store["embeddings"] = embeddings
    return _store


def search(query: str, k: int = 4) -> list[dict]:
    embeddings = _store["embeddings"]
    if embeddings is None or len(_store["texts"]) == 0:
        return []

    q = _embed_query(query)
    # cosine similarity
    norms = np.linalg.norm(embeddings, axis=1) * (np.linalg.norm(q) + 1e-9)
    scores = (embeddings @ q) / (norms + 1e-9)
    top = np.argsort(scores)[::-1][:k]

    results = []
    for i in top:
        results.append(
            {
                "page_content": _store["texts"][int(i)],
                "metadata": _store["metadatas"][int(i)],
                "score": float(scores[int(i)]),
            }
        )
    return results


def is_ready() -> bool:
    return _store["embeddings"] is not None and len(_store["texts"]) > 0


def clear_store():
    _store["texts"] = []
    _store["metadatas"] = []
    _store["embeddings"] = None
