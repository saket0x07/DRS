from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from app.rag.ingest import load_resume, chunk_documents

FAISS_PATH = "app/data/faiss_index"

def create_vectorstore():
    print("Loading resumes...")
    documents=load_resume()
    print("Documents loaded")

    print("Chunking documents...")
    chunks = chunk_documents(documents)
    print("Documents chunked")

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    print("Creating FAISS Index")
    vectorstore = FAISS.from_documents(documents= chunks,embedding=embeddings)
    Path(FAISS_PATH).mkdir(parents=True, exist_ok=True)
    print("FAISS Index created")
    vectorstore.save_local(FAISS_PATH)
    print("FAISS Index saved")
    return vectorstore

if __name__ == "__main__":
    create_vectorstore()

    