from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from src.embeddings import embeddings
from config import CHUNK_SIZE, CHUNK_OVERLAP, VECTOR_DB

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
)

def create_vector_store(text):

    chunks = text_splitter.split_text(text)

    db = FAISS.from_texts(
        chunks,
        embeddings
    )

    db.save_local(VECTOR_DB)


def load_vector_store():

    return FAISS.load_local(
        VECTOR_DB,
        embeddings,
        allow_dangerous_deserialization=True
    )