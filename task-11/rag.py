import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

_client = None


def get_client() -> Groq:
    global _client
    if _client is None:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError("GROQ_API_KEY is not set.")
        _client = Groq(api_key=api_key)
    return _client


def generate_answer(context: str, history: str, question: str) -> str:
    prompt = f"""You are a helpful document assistant.

Use the previous conversation and the retrieved context to answer the user's question.

Previous Conversation:
{history or "(none)"}

Context:
{context or "(no context retrieved)"}

Current Question:
{question}

Instructions:
- Answer only using the provided context.
- If the answer is not found in the context, reply exactly:
I couldn't find that information in the uploaded PDF.
- Be clear and concise.
"""

    response = get_client().chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=1024,
    )

    return response.choices[0].message.content
