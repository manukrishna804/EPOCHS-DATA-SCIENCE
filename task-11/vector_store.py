import os
import shutil

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# Embedding Model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def create_vector_store(chunks):
    """
    Create a fresh Chroma vector database.
    """

    if os.path.exists("chroma_db"):
        shutil.rmtree("chroma_db")

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chroma_db"
    )

    return vector_db


def load_vector_store():
    """
    Load existing Chroma database.
    """

    return Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding_model
    )


def get_retriever():
    """
    Return an MMR retriever.
    """

    db = load_vector_store()

    retriever = db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10
        }
    )

    return retriever