# Document Retrieval System (DRS)

A production-grade, multi-channel Document Retrieval-Augmented Generation (RAG) system. DRS allows you to ingest documents, perform semantic searches, compare files, and generate insights. It features a FastAPI backend, a clean Streamlit web application, and a Telegram bot interface.

---

## 🚀 Key Features

* **Multi-Channel Ingestion:** Upload PDF files via the REST API, Streamlit Web UI, or directly through the Telegram bot.
* **Semantic Search & Retrieval:** Uses **FAISS** (Facebook AI Similarity Search) and advanced embeddings to retrieve document sections with high accuracy.
* **Advanced RAG Pipeline:** Powered by **LangChain** with support for Gemini and OpenRouter models.
* **Streamlit Web Dashboard:** Interactive UI to upload files, query the knowledge base, review documents, and compare profiles.
* **Telegram Bot Integration:** Mobile-friendly bot to upload PDFs, list stored documents, and chat/search on the go.
* **Ragas Evaluation Suite:** Built-in tools to evaluate RAG performance metrics such as faithfulness, answer relevance, and retrieval precision.

---

## 📁 Project Structure

```text
├── app/
│   ├── main.py                  # FastAPI Entrypoint
│   ├── api/
│   │   └── routes.py            # API routes (Upload, search, compare, extract)
│   ├── rag/
│   │   ├── ingest.py            # PDF loading & text ingestion pipeline
│   │   ├── retriever.py         # Entity-aware vector retrieval
│   │   ├── llm.py               # LLM integration (Gemini/OpenRouter)
│   │   ├── vectorstore.py       # FAISS vector store helpers
│   │   ├── prompts.py           # Prompt engineering templates
│   │   └── chain.py             # End-to-end LangChain RAG pipeline
│   ├── telegram/
│   │   ├── bot.py               # Telegram bot main runner
│   │   └── handlers.py          # Command & message handlers for the bot
│   ├── evaluate/
│   │   ├── generate_dataset.py  # Synthetic Q&A evaluation dataset generator
│   │   └── eval_ragas.py        # Ragas evaluation executor
│   └── data/
│       ├── resumes/             # Uploaded documents (Git ignored, holds .gitkeep)
│       └── faiss_index/         # Local FAISS index (Git ignored)
├── streamlit_app.py             # Streamlit Web UI
├── requirements.txt             # Python dependencies
└── .gitignore                   # Git exclusion rules
```

---

## 🛠️ Getting Started

### 1. Prerequisites & Installation

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory and add the following:

```env
# Gemini API Key (Alternative OpenRouter Key)
GOOGLE_API_KEY=your_gemini_api_key
OPENROUTER_API_KEY=your_openrouter_api_key

# Telegram Bot Token (Get from @BotFather)
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

---

## 🏃 Running the Applications

You can run each component of the system separately depending on your use case:

### 1. Run the FastAPI Backend
Start the FastAPI server for REST API access:
```bash
uvicorn app.main:app --reload
```
API Documentation will be available at `http://127.0.0.1:8000/docs`.

### 2. Run the Streamlit Web Interface
Launch the interactive web dashboard:
```bash
streamlit run streamlit_app.py
```

### 3. Run the Telegram Bot
Run the background worker to start the Telegram bot:
```bash
python -m app.telegram.bot
```

---

## 🤖 Telegram Bot Commands

The Telegram Bot interacts with the same document database as the Streamlit app.
* `/start` - Welcome message and introduction.
* `/help` - Displays available bot instructions and command list.
* `/upload` - Puts the bot in **Upload Mode** to receive a PDF file.
* `/list_documents` - Lists all currently indexed PDFs.
* **Direct Messages** - Send any question in chat to search indexed documents and generate an AI response.

---

## 📊 RAG Evaluation

To run Ragas evaluation against your knowledge base:

1. Generate the evaluation dataset:
   ```bash
   python -m app.evaluate.generate_dataset
   ```
2. Run the Ragas scoring pipeline:
   ```bash
   python -m app.evaluate.eval_ragas
   ```
