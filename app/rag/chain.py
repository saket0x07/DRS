from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

from app.rag.llm import get_llm
from app.rag.retriever import get_retriever
from app.rag.prompts import resume_prompt

load_dotenv()
llm = get_llm()

def retrieve_context(question: str):
    """     RETRIEVE REAVANT DOC AND CONVERT THAT INTO A DOC STRING """
    # Instantiate retriever dynamically so it loads the latest index on disk
    docs = get_retriever().invoke(question)
    context=[]
    for doc in docs:
        candidate = doc.metadata.get("candidate_name","Unknown")
        source = doc.metadata.get("source","Unknown")

        context.append(f"""Candidate: {candidate}
        Source: {source}
        Context: {doc.page_content}
        """)
    return "\n\n".join(context)
    
rag_chain = (
    {"context": RunnableLambda(retrieve_context),    
    "question": RunnablePassthrough()
    }
    | resume_prompt
    | llm
    | StrOutputParser()
    
)