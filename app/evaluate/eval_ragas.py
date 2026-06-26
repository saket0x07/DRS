import pandas as pd
# import matplotlib.pyplot as plt
from datasets import Dataset
from ragas.metrics import answer_relevancy, faithfulness, context_precision, context_recall
from ragas import evaluate

from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_huggingface import HuggingFaceEmbeddings

from app.rag.llm import get_llm
from app.rag.retriever import get_retriever

import os
current_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(current_dir, "rag_eval_dataset.csv"))

df["retrieved_contexts"] = df["retrieved_contexts"].fillna("").apply(lambda x: [x])
df["ground_truth"] = df["ground_truth"].fillna("")

dataset = Dataset.from_pandas(df[["question","answer","retrieved_contexts","ground_truth"]])

llm = LangchainLLMWrapper(get_llm())
embeddings = LangchainEmbeddingsWrapper(HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5"))

ragas_metrics = [answer_relevancy, faithfulness, context_precision, context_recall]

result = evaluate(
    dataset=dataset,
    metrics=ragas_metrics,
    llm=llm,
    embeddings=embeddings,
)

print(result)

scores = result.to_pandas()
scores.to_csv(os.path.join(current_dir, "rag_scores.csv"), index=False)

print("Evaluation Complete")
print(scores)