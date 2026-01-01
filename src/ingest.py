import os
import pickle
import faiss
from pathlib import Path
from PyPDF2 import PdfReader

from src.config import RAW_PDF_DIR, FAISS_INDEX_PATH, METADATA_PATH
from src.chunking import chunk_text
from src.embedding import embed_texts


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def ingest():
    FAISS_INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)

    all_chunks = []
    metadata = []

    for pdf in RAW_PDF_DIR.glob("*.pdf"):
        text = extract_text_from_pdf(pdf)
        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            metadata.append({
                "source": pdf.name,
                "chunk_id": i
            })

    embeddings = embed_texts(all_chunks)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, str(FAISS_INDEX_PATH))

    with open(METADATA_PATH, "wb") as f:
        pickle.dump({
            "texts": all_chunks,
            "metadata": metadata
        }, f)

    print("✅ Offline ingestion completed")


if __name__ == "__main__":
    ingest()
