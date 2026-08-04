import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(context, history, question):

    prompt = f"""
You are a helpful AI assistant.

Use the previous conversation and the retrieved context to answer the user's question.

Previous Conversation:
{history}

Context:
{context}

Current Question:
{question}

Instructions:
- Answer only using the provided context.
- If the answer is not found in the context, reply:
"I couldn't find that information in the uploaded PDF."

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content