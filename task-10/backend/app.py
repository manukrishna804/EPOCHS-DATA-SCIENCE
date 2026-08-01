from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Request model
class ChatRequest(BaseModel):
    message: str

# Health check
@app.get("/")
def home():
    return {"message": "AI Study Assistant Backend Running"}

# Chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
    {
        "role": "system",
        "content": """
You are StudyMate AI, a friendly AI Study Assistant.

Rules:
- Explain concepts in simple language.
- If the topic is technical, provide a real-world example.
- Use bullet points whenever appropriate.
- If asked for notes, provide concise revision notes.
- If asked to compare topics, use a table.
- End every explanation with a short summary.
- If you don't know something, say so instead of making up information.
"""
    },
    {
        "role": "user",
        "content": request.message
    }
],
        temperature=0.5,
        max_tokens=500,
    )

    return {
        "response": response.choices[0].message.content
    }