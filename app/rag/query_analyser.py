import re
from pathlib import Path

RESUME_DIR = "app/data/resumes"


def load_candidate_names():
    """
    Load candidate names directly from resume filenames.
    Example:
    Saket-Resume.pdf -> Saket Resume
    Saloni_Gupta_Resume.pdf -> Saloni Gupta Resume
    """

    candidates = []

    for pdf in Path(RESUME_DIR).glob("*.pdf"):

        name = (
            pdf.stem
            .replace("_", " ")
            .replace("-", " ")
            .replace("Resume", "")
            .replace("resume", "")
            .strip()
        )

        candidates.append(name)

    return sorted(list(set(candidates)))


KNOWN_CANDIDATES = load_candidate_names()


def extract_candidates(query: str):
    """
    Find candidate names mentioned in the query.
    Supports:
    - Full name
    - First name
    """

    query = query.lower()

    found = []

    for candidate in KNOWN_CANDIDATES:

        candidate_lower = candidate.lower()

        # Full name
        if candidate_lower in query:
            found.append(candidate)
            continue

        # First name
        first_name = candidate_lower.split()[0]

        if re.search(rf"\b{re.escape(first_name)}\b", query):
            found.append(candidate)

    return list(set(found))


def analyze_query(query: str):

    query_lower = query.lower()

    candidates = extract_candidates(query)

    # ------------------------
    # Comparison Queries
    # ------------------------

    comparison_words = [
        "compare",
        "difference",
        "better",
        "vs",
        "versus",
    ]

    if any(word in query_lower for word in comparison_words) or len(candidates) >= 2:

        return {
            "intent": "comparison",
            "candidates": candidates,
        }

    # ------------------------
    # Candidate Search
    # ------------------------

    if len(candidates) == 1:

        return {
            "intent": "candidate_search",
            "candidate": candidates[0],
        }

    # ------------------------
    # Skill Search
    # ------------------------

    skills = [
        "python",
        "java",
        "sql",
        "c++",
        "javascript",
        "react",
        "node",
        "fastapi",
        "flask",
        "django",
        "langchain",
        "llm",
        "machine learning",
        "deep learning",
        "nlp",
        "ai",
        "aws",
        "azure",
        "docker",
        "kubernetes",
        "power bi",
        "excel",
        "tableau",
    ]

    for skill in skills:

        if skill in query_lower:

            return {
                "intent": "skill_search",
                "skill": skill,
            }

    # ------------------------
    # Company Search
    # ------------------------

    company_keywords = [
        "worked",
        "company",
        "organization",
        "internship",
        "experience at",
        "employee",
    ]

    if any(word in query_lower for word in company_keywords):

        return {
            "intent": "company_search",
        }

    # ------------------------
    # Project Search
    # ------------------------

    if any(word in query_lower for word in [
        "project",
        "projects",
        "built",
        "developed",
        "created",
    ]):

        return {
            "intent": "project_search",
        }

    # ------------------------
    # Experience Search
    # ------------------------

    if any(word in query_lower for word in [
        "experience",
        "years",
        "fresher",
        "senior",
    ]):

        return {
            "intent": "experience_search",
        }

    # ------------------------
    # Education Search
    # ------------------------

    if any(word in query_lower for word in [
        "education",
        "college",
        "university",
        "degree",
        "b.tech",
        "mba",
        "bca",
        "mca",
    ]):

        return {
            "intent": "education_search",
        }

    # ------------------------
    # Default
    # ------------------------

    return {
        "intent": "general_search",
    }


if __name__ == "__main__":

    print("\nCandidates Found:")
    print("---------------------------")

    for name in KNOWN_CANDIDATES:
        print(name)

    print("\n")

    queries = [

        "Tell me about Saket",
        "Give details of Saloni Gupta",
        "Compare Saket and Rahul",
        "Who knows Python?",
        "Who worked in Infosys?",
        "Who has HR experience?",
        "Who has Machine Learning skills?",
        "Who has 5 years of experience?",
        "Show Java developers",
        "Which candidate worked on FastAPI?",
    ]

    for q in queries:

        print(q)
        print(analyze_query(q))
        print("-" * 50)