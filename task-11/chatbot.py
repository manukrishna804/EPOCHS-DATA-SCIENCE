from pdf_loader import load_and_split_pdf
from vector_store import create_vector_store, get_retriever
from rag import generate_answer
from memory import add_to_history, get_history, chat_history

retriever = None


def process_pdf(pdf_path):
    """
    Process uploaded PDF and create vector database.
    """
    global retriever

    chunks = load_and_split_pdf(pdf_path)

    create_vector_store(chunks)

    retriever = get_retriever()

    chat_history.clear()

    return "✅ PDF processed successfully."


def ask_question(question):
    """
    Ask a question about the uploaded PDF.
    """

    global retriever

    if retriever is None:
        return "Please upload a PDF first."

    # Retrieve relevant documents
    docs = retriever.invoke(question)

    context = ""
    pages = []

    for doc in docs:
        context += doc.page_content + "\n\n"

        page = doc.metadata.get("page")
        if page is not None:
            pages.append(page + 1)   # Convert from 0-based to 1-based page numbering

    # Previous conversation
    history = get_history()

    # Generate answer
    answer = generate_answer(
        context=context,
        history=history,
        question=question
    )

    # Save conversation
    add_to_history(question, answer)

    # Add source pages
    if pages:
        pages = sorted(set(pages))
        page_text = ", ".join(map(str, pages))
        answer += f"\n\n📄 Source Page(s): {page_text}"

    return answer


def clear_memory():
    """
    Clear conversation history.
    """
    chat_history.clear()