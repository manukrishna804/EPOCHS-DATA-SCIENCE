chat_history = []


def add_to_history(question, answer):
    chat_history.append({
        "question": question,
        "answer": answer
    })


def get_history():
    history = ""

    for chat in chat_history:
        history += f"""
User: {chat['question']}
Assistant: {chat['answer']}

"""

    return history