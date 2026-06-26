import os
from dotenv import load_dotenv
# from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI

load_dotenv()

def get_llm():
    return ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        model="openai/gpt-oss-120b:free"
    )

