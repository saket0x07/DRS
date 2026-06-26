import uvicorn
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Document Retrieval Search RAG API", version="1.0")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
