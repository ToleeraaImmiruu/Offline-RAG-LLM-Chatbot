from config import CHUNK_SIZE, CHUNK_OVERLAP


def chunk_text(text: str):
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + CHUNK_SIZE
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - CHUNK_OVERLAP

        if start < 0:
            start = 0

    return chunks
