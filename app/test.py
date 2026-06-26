import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="openai/gpt-oss-120b:free"
)

reponse=llm.invoke("who are you?")
print(reponse.content)