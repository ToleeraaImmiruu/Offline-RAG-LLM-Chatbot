def generate_answer(prompt: str):
    """
    Placeholder function for offline RAG.
    For now, it just returns the context.
    """
    # For learning purposes, just return combined context as 'answer'
    return prompt.split("Context:")[-1].strip()
