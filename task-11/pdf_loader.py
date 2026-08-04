from pypdf import PdfReader


def _split_text(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> list[str]:
    text = " ".join((text or "").split())
    if not text:
        return []

    if len(text) <= chunk_size:
        return [text]

    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))

        # Prefer breaking at a sentence/space boundary
        if end < len(text):
            window = text[start:end]
            break_at = max(window.rfind(". "), window.rfind(" "))
            if break_at > chunk_size // 3:
                end = start + break_at + 1

        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)

        if end >= len(text):
            break
        start = max(end - chunk_overlap, start + 1)

    return chunks


def load_and_split_pdf(pdf_path: str) -> list[dict]:
    reader = PdfReader(pdf_path)
    documents = []

    for page_index, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        for chunk in _split_text(text):
            documents.append(
                {
                    "page_content": chunk,
                    "metadata": {"page": page_index},
                }
            )

    if not documents:
        raise ValueError("No readable text found in this PDF.")

    return documents
