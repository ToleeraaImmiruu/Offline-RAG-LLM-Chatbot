import re


def classify_question(question: str):
    question_lower = question.lower()

    # Small talk
    if question_lower in ["hi", "hello", "hey"]:
        return "small_talk"

    # Opinion-based
    if any(word in question_lower for word in ["good", "bad", "better", "best"]):
        return "opinion"

    # Future-dated
    if re.search(r"\b(20\d{2})\b", question_lower):
        year = re.search(r"\b(20\d{2})\b", question_lower).group()
        if int(year) > 2023:
            return "future"

    # Default: document-based
    return "document"
