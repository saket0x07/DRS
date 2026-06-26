import re
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from rank_bm25 import BM25Okapi

from app.rag.query_analyser import analyze_query

FAISS_PATH = "app/data/faiss_index"

embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

class ResumeRetriever:

    def __init__(self):
        self.db = FAISS.load_local(FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
        self.documents = list(self.db.docstore._dict.values())
        corpus = []
        for doc in self.documents:
            text = f"""
            {doc.metadata.get("candidate_name","")}
            {doc.page_content}
            """
            # Clean tokenization
            tokens = [word.lower() for word in re.findall(r'\w+', text)]
            corpus.append(tokens)
        self.bm25 = BM25Okapi(corpus)

    def semantic_search(self, query, k=5):
        return self.db.similarity_search(query, k=k)

    def keyword_search(self, query, k=5):
        tokens = [word.lower() for word in re.findall(r'\w+', query)]
        scores = self.bm25.get_scores(tokens)
        ranked = sorted(zip(scores, self.documents), key=lambda x: x[0], reverse=True)
        return [doc for _, doc in ranked[:k]]

    def reciprocal_rank_fusion(self, semantic_docs, keywords_docs, k=60):
        scores = {}
        
        # Helper to score documents from a list based on their rank
        def add_ranks(doc_list):
            for rank, doc in enumerate(doc_list):
                # Use a combination of page_content and candidate_name as key to uniquely identify the chunk
                key = (doc.page_content, doc.metadata.get("candidate_name", ""))
                if key not in scores:
                    scores[key] = {"doc": doc, "score": 0.0}
                scores[key]["score"] += 1.0 / (k + rank + 1)
        
        add_ranks(semantic_docs)
        add_ranks(keywords_docs)
        
        ranked = sorted(scores.values(), key=lambda x: x["score"], reverse=True)
        return [item["doc"] for item in ranked]

    def invoke(self, query):
        analysis = analyze_query(query)
        print("\n QUERY ANALYSIS:", analysis)
        
        intent = analysis["intent"]
        
        if intent == "comparison":
            candidates = analysis.get("candidates", [])
            if len(candidates) >= 2:
                all_docs = []
                for candidate in candidates:
                    # Search specifically for each candidate to guarantee coverage
                    sem_docs = self.semantic_search(candidate, k=10)
                    key_docs = self.keyword_search(candidate, k=10)
                    fused = self.reciprocal_rank_fusion(sem_docs, key_docs)
                    # Filter to candidate's docs
                    filtered_c = [
                        doc for doc in fused 
                        if candidate.lower() in doc.metadata.get("candidate_name", "").lower()
                    ]
                    all_docs.extend(filtered_c[:5]) # top 5 docs for each candidate
                return all_docs
            
        elif intent == "candidate_search":
            candidate = analysis.get("candidate", "")
            # Retrieve with a larger pool, then filter
            sem_docs = self.semantic_search(query, k=15)
            key_docs = self.keyword_search(query, k=15)
            fused = self.reciprocal_rank_fusion(sem_docs, key_docs)
            filtered = [
                doc for doc in fused 
                if candidate.lower() in doc.metadata.get("candidate_name", "").lower()
            ]
            return filtered[:10]
            
        # For other search intents (skill, company, project, experience, education, general),
        # we want a diverse search across all candidates in the corpus
        sem_docs = self.semantic_search(query, k=20)
        key_docs = self.keyword_search(query, k=20)
        final_docs = self.reciprocal_rank_fusion(sem_docs, key_docs)
        return final_docs[:12]

def get_retriever():
    return ResumeRetriever()
