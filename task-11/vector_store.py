"""Lightweight TF-IDF vector store — no torch/onnx, fits Render 512MB."""

from __future__ import annotations

import re
import numpy as np

_store = {
    "texts": [],
    "metadatas": [],
    "matrix": None,  # sparse-like dense TF-IDF matrix (n_docs, vocab)
    "idf": None,
    "vocab": {},
}


_TOKEN = re.compile(r"[a-z0-9]+")


def _tokenize(text: str) -> list[str]:
    return _TOKEN.findall((text or "").lower())


def _build_tfidf(texts: list[str]):
    docs_tokens = [_tokenize(t) for t in texts]
    df: dict[str, int] = {}
    for tokens in docs_tokens:
        for tok in set(tokens):
            df[tok] = df.get(tok, 0) + 1

    # Cap vocabulary for memory
    vocab_items = sorted(df.items(), key=lambda x: (-x[1], x[0]))[:4000]
    vocab = {tok: i for i, (tok, _) in enumerate(vocab_items)}
    n_docs = max(len(texts), 1)
    idf = np.zeros(len(vocab), dtype=np.float32)
    for tok, i in vocab.items():
        idf[i] = np.log((1 + n_docs) / (1 + df[tok])) + 1.0

    matrix = np.zeros((len(texts), len(vocab)), dtype=np.float32)
    for row, tokens in enumerate(docs_tokens):
        if not tokens:
            continue
        counts: dict[int, int] = {}
        for tok in tokens:
            idx = vocab.get(tok)
            if idx is not None:
                counts[idx] = counts.get(idx, 0) + 1
        total = float(sum(counts.values()) or 1)
        for idx, c in counts.items():
            matrix[row, idx] = (c / total) * idf[idx]
        norm = np.linalg.norm(matrix[row])
        if norm > 0:
            matrix[row] /= norm

    return vocab, idf, matrix


def _embed_query(query: str) -> np.ndarray:
    vocab = _store["vocab"]
    idf = _store["idf"]
    vec = np.zeros(len(vocab), dtype=np.float32)
    tokens = _tokenize(query)
    if not tokens or not vocab:
        return vec

    counts: dict[int, int] = {}
    for tok in tokens:
        idx = vocab.get(tok)
        if idx is not None:
            counts[idx] = counts.get(idx, 0) + 1
    total = float(sum(counts.values()) or 1)
    for idx, c in counts.items():
        vec[idx] = (c / total) * idf[idx]
    norm = np.linalg.norm(vec)
    if norm > 0:
        vec /= norm
    return vec


def create_vector_store(chunks: list[dict]):
    texts = [c["page_content"] for c in chunks]
    metadatas = [c["metadata"] for c in chunks]
    vocab, idf, matrix = _build_tfidf(texts)

    _store["texts"] = texts
    _store["metadatas"] = metadatas
    _store["vocab"] = vocab
    _store["idf"] = idf
    _store["matrix"] = matrix
    return _store


def search(query: str, k: int = 4) -> list[dict]:
    matrix = _store["matrix"]
    if matrix is None or len(_store["texts"]) == 0:
        return []

    q = _embed_query(query)
    scores = matrix @ q
    top = np.argsort(scores)[::-1][:k]

    results = []
    for i in top:
        if scores[int(i)] <= 0:
            continue
        results.append(
            {
                "page_content": _store["texts"][int(i)],
                "metadata": _store["metadatas"][int(i)],
                "score": float(scores[int(i)]),
            }
        )
    return results


def is_ready() -> bool:
    return _store["matrix"] is not None and len(_store["texts"]) > 0


def clear_store():
    _store["texts"] = []
    _store["metadatas"] = []
    _store["matrix"] = None
    _store["idf"] = None
    _store["vocab"] = {}
