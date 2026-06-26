import os
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from app.rag.chain import rag_chain
from app.rag.vectorstore import create_vectorstore

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/ask")
def ask_question(request: QueryRequest):
    answer = rag_chain.invoke(request.question)
    return {
        "question": request.question,
        "answer": answer
    }

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    resume_dir = "app/data/resumes"
    os.makedirs(resume_dir, exist_ok=True)
    
    file_path = os.path.join(resume_dir, file.filename)
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")
        
    try:
        # Re-run ingestion in sequence
        create_vectorstore()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to run ingestion: {str(e)}")
        
    return {"filename": file.filename, "status": "Successfully ingested and indexed"}

@router.get("/documents")
def list_documents():
    resume_dir = "app/data/resumes"
    if not os.path.exists(resume_dir):
        return []
    try:
        files = [f for f in os.listdir(resume_dir) if f.endswith(".pdf")]
        return sorted(files)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list documents: {str(e)}")