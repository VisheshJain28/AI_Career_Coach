from langchain.chains import RetrievalQA

from src.vector_store import load_vector_store
from src.llm import get_llm


llm = get_llm()


def perform_qa(query):

    db = load_vector_store()

    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={"k":4}
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    return qa.invoke(query)["result"]