# Document Retrieval System (DRS)

A production-quality Document Retrieval-Augmented Generation (RAG) system using FAISS, LangChain, Gemini/OpenRouter, and FastAPI.

## Project Structure

```text
app/
├── main.py                  # FastAPI Entrypoint
├── api/
│   └── routes.py            # Upload, search, comparison, and JD matching routes
├── rag/
│   ├── ingest.py            # PDF loading and ingestion pipeline
│   ├── retriever.py         # Entity-aware vector retrieval
│   ├── llm.py               # LLM integration (Gemini/OpenRouter)
│   ├── vectorstore.py       # FAISS database helpers
│   └── prompts.py           # Prompt engineering templates
├── utils/
│   ├── parser.py            # Contact & skills parser
│   └── candidate_extractor.py # LLM parser to extract name and query
└── data/
    ├── resumes/             # Candidate resumes in PDF format
    └── faiss_index/         # Local FAISS index
```

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables in a `.env` file:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key
   ```

3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```
