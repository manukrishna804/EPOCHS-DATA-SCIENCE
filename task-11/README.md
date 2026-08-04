# 📄 PDF Question Answering Application using RAG

## Participant Details

- **Name:** Manukrisha CK
- **MUID:** manukrishnack-1@mulearn

---

# 📖 Project Overview

This project is a **PDF Question Answering Application** built using **Retrieval-Augmented Generation (RAG)**. It enables users to upload any PDF document and ask questions related to its content. The system retrieves the most relevant information from the uploaded document using semantic search and generates accurate, context-aware answers using a Large Language Model (LLM).

The application also supports **conversation memory**, allowing users to ask follow-up questions naturally without repeating previous context.

---

# 🚀 Features

- 📄 Upload PDF documents
- ✂️ Automatic text chunking
- 🔎 Semantic search using vector embeddings
- 🧠 Retrieval-Augmented Generation (RAG)
- 🤖 Groq Llama 3 LLM integration
- 💬 Conversation memory for follow-up questions
- 🌐 Interactive Gradio web interface
- ⚡ Fast and accurate document question answering

---

# 🛠️ Technologies Used

- Python
- LangChain
- ChromaDB
- PyPDFLoader
- Sentence Transformers
- Groq API
- Gradio
- Python Dotenv

---

# 🏗️ Project Architecture

```
                Upload PDF
                     │
                     ▼
            PyPDFLoader
                     │
                     ▼
        Recursive Character Splitter
                     │
                     ▼
     Sentence Transformer Embeddings
                     │
                     ▼
               ChromaDB
                     │
─────────────────────────────────────────
User Question
        │
        ▼
Retrieve Relevant Chunks
        │
        ▼
Conversation Memory
        │
        ▼
Groq Llama 3
        │
        ▼
Generated Answer
```

---

# 📂 Project Structure

```
PDF-RAG-Chatbot/
│
├── app.py
├── chatbot.py
├── pdf_loader.py
├── vector_store.py
├── rag.py
├── memory.py
├── requirements.txt
├── README.md
├── .env.example
├── uploads/
└── chroma_db/
```

---

# 🧠 Memory Implementation

Conversation memory is implemented by maintaining the previous user questions and assistant responses during the session. Each new query is combined with the previous conversation before sending it to the LLM, allowing the chatbot to understand follow-up questions and maintain context throughout the interaction.

---

# ⚙️ How It Works

1. Upload a PDF document.
2. Extract text using PyPDFLoader.
3. Split the text into smaller chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in ChromaDB.
6. Ask questions about the uploaded PDF.
7. Retrieve the most relevant chunks.
8. Send the retrieved context and conversation history to the Groq LLM.
9. Display the generated answer to the user.

---

# ▶️ Installation

Clone the repository:

```bash
git clone <your-github-repository>
```

Navigate into the project:

```bash
cd PDF-RAG-Chatbot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Run the application:

```bash
python app.py
```

---

# 🎯 Challenges Faced

- Selecting appropriate chunk size and overlap for better retrieval.
- Managing semantic search efficiently using ChromaDB.
- Integrating Groq API for context-aware responses.
- Maintaining conversation history for follow-up questions.
- Building an interactive and user-friendly Gradio interface.

---

# 🚀 Future Improvements

- Support multiple PDF uploads.
- Display source page references for answers.
- Add PDF summarization.
- Support DOCX and TXT files.
- Enable persistent chat history.
- Deploy with authentication for secure access.

---

# 🌐 Deployment

**Deployment Link:**

_Add your Hugging Face Spaces or Render deployment link here._

---



# 📜 License

This project was developed as part of **Epochs '26 – Assignment 11** for educational purposes.