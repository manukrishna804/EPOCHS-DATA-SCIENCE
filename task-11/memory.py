chat_history = []


def add_to_history(question: str, answer: str):
    chat_history.append({"question": question, "answer": answer})
    # Keep memory bounded for free-tier RAM
    if len(chat_history) > 12:
        del chat_history[:-12]


def get_history() -> str:
    if not chat_history:
        return ""

    parts = []
    for chat in chat_history:
        parts.append(f"User: {chat['question']}\nAssistant: {chat['answer']}")
    return "\n\n".join(parts)
