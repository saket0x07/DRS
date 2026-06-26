import csv

from app.rag.chain import rag_chain
from app.rag.retriever import get_retriever

retriever = get_retriever()


questions = [
    "Tell me about Saket Gupta.",
    "What are Saket's Technical Skills?",
    "What Project has Saket worked on?",
    "Who is Saloni Gupta?",
    "What HR experiences does Saloni have?",
    "Which candidate has experience in FastAPI?",
    "How many years of experience does Priya have?",
    "What is Priya's current role?",
    "Who knows Python?",
    "Who worked in 360DigiTMG?",
    "Who worked in Infosys?",
    "Which candidate knows Machine Learning?",
    "Who has HR experience?",
    "Who has worked with Java?",
    "Which candidate has experience in recruitment?",
    "Compare Saket Gupta and Saloni Gupta.",
]


def build_context(docs):
    """
    Convert retrieved Documents into a readable context.
    """

    contexts = []

    for i, doc in enumerate(docs, start=1):

        candidate = doc.metadata.get("candidate_name", "Unknown")
        source = doc.metadata.get("source", "Unknown")

        contexts.append(
            f"""
========== Document {i} ==========
Candidate : {candidate}
Source    : {source}

{doc.page_content}
"""
        )

    return "\n\n".join(contexts)




with open(
    "rag_eval_dataset.csv",
    "w",
    newline="",
    encoding="utf-8",
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "question",
        "answer",
        "retrieved_contexts",
        "candidate_names",
        "retriever_sources",
        "ground_truth",
    ])

    for question in questions:

        print(f"Processing : {question}")

        docs = retriever.invoke(question)

        context = build_context(docs)

        candidate_names = ", ".join(
            sorted(
                set(
                    doc.metadata.get("candidate_name", "Unknown")
                    for doc in docs
                )
            )
        )

        sources = ", ".join(
            sorted(
                set(
                    doc.metadata.get("source", "Unknown")
                    for doc in docs
                )
            )
        )

        
        print("="*50)
        print(context)
        print("="*50)

        answer = rag_chain.invoke(question)

        writer.writerow([
            question,
            answer,
            context,
            candidate_names,
            sources,
            "",
        ])

print("\nDataset generated successfully!")