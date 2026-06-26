import os
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

RESUME_DIR = "app/data/resumes"

def load_resume():
    """ LOAD ALL RESUME FROM DIRECTORY """
    all_documents = []
    resume_path = Path(RESUME_DIR)

    pdf_files = list(resume_path.glob("*.pdf"))
    print (f"Found {len(pdf_files)} PDFs")

    for pdf_file in pdf_files:
        candidate_name = (pdf_file.stem.replace("_", " ").replace("-", " "))
        print (f"Processing {candidate_name}")
        loader = PyPDFLoader(file_path=str(pdf_file))
        documents=loader.load()

        for doc in documents:
            doc.metadata["candidate_name"]=candidate_name
            doc.metadata["source"]=str(pdf_file)

        all_documents.extend(documents)
    return all_documents


def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
    )
    chunks = splitter.split_documents(documents)
   
    print(f"Total chunks {len(chunks)}")
    return chunks

if __name__ == "__main__":
    documents = load_resume()
    chunks = chunk_documents(documents)
    print("\n Sample metadata::")
    print(chunks[0].metadata)
    print("\n Sample texts::")
    print(chunks[0].page_content[:500])

            
        