import pickle
import faiss
import numpy as np
from src.config import FAISS_INDEX_PATH, METADATA_PATH, TOP_K
from src.embedding import embed_texts


def retrieve(query: str):
    index = faiss.read_index(str(FAISS_INDEX_PATH))

    with open(METADATA_PATH, "rb") as f:
        store = pickle.load(f)

    query_embedding = embed_texts([query])[0]

    D, I = index.search(
        np.array([query_embedding]).astype("float32"),
        TOP_K
    )

    return [store["texts"][i] for i in I[0]]
