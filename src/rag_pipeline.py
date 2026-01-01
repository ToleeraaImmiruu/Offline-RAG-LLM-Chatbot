import re
from src.retriever import retrieve
from src.prompt import build_prompt
from src.llm_gemini import generate_answer

# ----------------------------
# Simple rule-based question classifier
# ----------------------------


def classify_question(question: str):
    question_lower = question.lower()

    # Small talk
    if question_lower in ["hi", "hello", "hey"]:
        return "small_talk"

    # Opinion-based
    if any(word in question_lower for word in ["good", "bad", "better", "best"]):
        return "opinion"

    # Future-dated (any year > 2023)
    year_match = re.findall(r"\b(20\d{2})\b", question_lower)
    if year_match and any(int(y) > 2023 for y in year_match):
        return "future"

    # Otherwise, assume document-based
    return "document"

# ----------------------------
# Year safety check (optional extra guard)
# ----------------------------


def question_mentions_year(question: str):
    return re.findall(r"\b(19|20)\d{2}\b", question)


def context_contains_year(context: str, years: list):
    return any(year in context for year in years)


# ----------------------------
# Main ask function
# ----------------------------
def ask(question: str):
    # Step 1: classify the question
    question_type = classify_question(question)

    # Step 2: handle based on type
    if question_type == "small_talk":
        return "Hello! You can ask me questions about the RELX 2023 Annual Report."

    if question_type == "opinion":
        return "I can only answer factual questions based on the document."

    if question_type == "future":
        return "Information not available in the document."

    # Step 3: document-based question → RAG retrieval
    contexts = retrieve(question)
    combined_context = "\n\n".join(contexts)

    # Step 4: extra year check
    years = question_mentions_year(question)
    if years and not context_contains_year(combined_context, years):
        return "Information not available in the document."

    # Step 5: build prompt and generate answer
    prompt = build_prompt(combined_context, question)
    return generate_answer(prompt)
