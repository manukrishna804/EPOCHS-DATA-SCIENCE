# Folio — PDF Question Answering (RAG)

## Participant Details

- **Name:** Manukrishna CK
- **MUID:** manukrishnack-1@mulearn

---

## Overview

**Folio** is a PDF question-answering app built with Retrieval-Augmented Generation (RAG). Upload a PDF, ask questions, and get answers grounded in the document — with short conversation memory for follow-ups.

Optimized for **Render free tier** (lightweight ONNX embeddings, no PyTorch/CUDA).

---

## Features

- Upload and process PDF documents
- Text chunking and semantic retrieval
- Groq Llama 3.3 answers grounded in retrieved context
- Conversation memory for follow-up questions
- Clean white Gradio UI

---

## Stack

- Python
- Gradio
- FastEmbed (ONNX embeddings)
- NumPy in-memory vector search
- PyPDF
- Groq API

---

## Project structure

```
task-11/
├── app.py              # Gradio UI
├── chatbot.py          # Orchestration
├── pdf_loader.py       # PDF load + chunk
├── vector_store.py     # Embeddings + search
├── rag.py              # Groq LLM
├── memory.py           # Chat history
├── requirements.txt
├── render.yaml
├── runtime.txt
└── .env.example
```

---

## Local setup

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

Create `.env`:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Run:

```bash
python app.py
```

Open **http://127.0.0.1:7860/**

---

## Deploy on Render

1. Push this folder to GitHub.
2. On [Render](https://dashboard.render.com) → **New** → **Blueprint**.
3. Select the repo and confirm `task-11/render.yaml` (or set root directory to `task-11`).
4. Add env var `GROQ_API_KEY`.
5. Deploy.

Manual web service settings if not using Blueprint:

- **Root Directory:** `task-11`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python app.py`
- **Python version:** `3.11.9`

---

## License

Built for **Epochs '26 – Assignment 11** (educational use).
