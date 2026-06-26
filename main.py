from dotenv import load_dotenv
from app.rag.chain import rag_chain

load_dotenv()

if __name__ == "__main__":
    print("Resume Search RAG CLI Client. Type 'exit' or 'quit' to stop.")
    while True:
        query = input("\nAsk a question about the resume: ")
        if query.strip().lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        if not query.strip():
            continue
        try:
            response = rag_chain.invoke(query)
            print("\nAnswer:::\n")
            print(response)
        except Exception as e:
            print(f"Error invoking chain: {e}")