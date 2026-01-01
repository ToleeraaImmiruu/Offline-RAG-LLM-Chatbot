from sentence_transformers import SentenceTransformer
import numpy as np
from src.config import EMBEDDING_MODEL_NAME

# Load the local embedding model once
model = SentenceTransformer(EMBEDDING_MODEL_NAME)


def embed_texts(texts):
    """
    Convert a list of text chunks into embeddings using local SentenceTransformer.
    """
    embeddings = model.encode(
        texts, convert_to_numpy=True, normalize_embeddings=True)
    return np.array(embeddings).astype("float32")
