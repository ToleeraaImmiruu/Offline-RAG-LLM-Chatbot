from pathlib import Path

# ===============================
# Base Directories
# ===============================
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_PDF_DIR = DATA_DIR / "raw_pdfs"

PROCESSED_DIR = DATA_DIR / "processed"
TEXT_DIR = PROCESSED_DIR / "extracted_text"

VECTORSTORE_DIR = BASE_DIR / "vectorstore"

# ===============================
# Vector Store Files
# ===============================
FAISS_INDEX_PATH = VECTORSTORE_DIR / "faiss.index"
METADATA_PATH = VECTORSTORE_DIR / "metadata.pkl"

# ===============================
# Chunking Configuration
# ===============================
CHUNK_SIZE = 800        # characters per chunk
CHUNK_OVERLAP = 150     # overlap between chunks
TOP_K = 2          # number of retrieved chunks per query

MAX_CONTEXT_CHARS = 12000  # safety limit for prompt

# ===============================
# Offline Embedding Model
# ===============================
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"  # local sentence-transformers model

# ===============================
# LLM (Optional)
# ===============================
LLM_MODEL = "offline"  # Placeholder for now
