from pdf_loader import load_and_split_pdf
from vector_store import create_vector_store

chunks = load_and_split_pdf("uploads/sample.pdf")

create_vector_store(chunks)

print("Vector DB Created Successfully!")