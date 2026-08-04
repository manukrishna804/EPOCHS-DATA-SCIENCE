from pdf_loader import load_and_split_pdf
from vector_store import create_vector_store, search, is_ready, clear_store
from rag import generate_answer
from memory import add_to_history, get_history, chat_history


def process_pdf(pdf_path: str) -> str:
    chunks = load_and_split_pdf(pdf_path)
    create_vector_store(chunks)
    chat_history.clear()
    return f"Processed {len(chunks)} text chunks. You can start asking questions."


def ask_question(question: str) -> str:
    question = (question or "").strip()
    if not question:
        return "Please enter a question."

    if not is_ready():
        return "Please upload and process a PDF first."

    docs = search(question, k=4)

    context_parts = []
    pages = []
    for doc in docs:
        context_parts.append(doc["page_content"])
        page = doc["metadata"].get("page")
        if page is not None:
            pages.append(page + 1)

    context = "\n\n".join(context_parts)
    history = get_history()
    answer = generate_answer(context=context, history=history, question=question)
    add_to_history(question, answer)

    if pages:
        page_text = ", ".join(map(str, sorted(set(pages))))
        answer += f"\n\nSource page(s): {page_text}"

    return answer


def clear_memory():
    chat_history.clear()


def reset_session():
    """Clear chat and vector store (new document session)."""
    chat_history.clear()
    clear_store()
