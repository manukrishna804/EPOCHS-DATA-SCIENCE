---
title: Folio PDF Chat
emoji: 📄
colorFrom: teal
colorTo: blue
sdk: gradio
sdk_version: 5.29.0
app_file: app.py
pinned: false
short_description: PDF RAG chatbot with Groq + FastEmbed
---

# Folio — PDF Question Answering (RAG)

## Participant Details

- **Name:** Manukrishna CK
- **MUID:** manukrishnack-1@mulearn

---

## Project Overview

**Folio** is a PDF question-answering app built with Retrieval-Augmented Generation (RAG). Upload a PDF, ask questions, and get answers grounded in the document — with conversation memory for natural follow-ups.

---

## Features

- Upload and process PDF documents
- Text chunking and semantic retrieval
- Groq Llama 3.3 answers grounded in retrieved context
- Conversation memory for follow-up questions
- Clean white Gradio UI

---

## Technologies Used

- Python
- Gradio
- FastEmbed (ONNX embeddings)
- NumPy in-memory vector store
- PyPDF
- Groq API (Llama 3.3)

---

## Memory Implementation

Conversation memory keeps recent user questions and assistant answers in a session list. Each new query is sent to the LLM together with that history and the retrieved PDF chunks, so follow-up questions work without repeating earlier context. History is capped (last 12 turns) to keep memory usage low.

---

## How It Works

1. Upload a PDF
2. Extract and chunk text
3. Embed chunks with FastEmbed
4. Store vectors in memory
5. On each question, retrieve top matching chunks
6. Send context + chat history to Groq
7. Show the grounded answer (with source pages when available)

---

## Project Structure

```
task-11/
├── app.py
├── chatbot.py
├── pdf_loader.py
├── vector_store.py
├── rag.py
├── memory.py
├── requirements.txt
└── .env.example
```

---

## Local Setup

```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

Create `.env`:

```env
GROQ_API_KEY=your_groq_api_key_here
```

```bash
python app.py
```

Open **http://127.0.0.1:7860/**

---

## Deployment

**Platform:** Hugging Face Spaces (Gradio) — Render free tier (512MB) OOMs with embedding models.

**Deployment Link:** https://huggingface.co/spaces/manukrishna804/folio-pdf-chat

### Space secrets

In the Space → **Settings** → **Variables and secrets**, add:

- `GROQ_API_KEY` = your Groq API key

---

## Challenges Faced

- Render free instances (512MB) crash when loading embedding runtimes
- Balancing retrieval quality with a lightweight stack suitable for free hosting
- Keeping conversation memory useful without unbounded RAM growth

---

## Future Improvements

- Multi-PDF support
- Persistent vector store across restarts
- Document summarization
- Auth for private documents

---

## License

Built for **Epochs '26 – Assignment 11** (educational use).
