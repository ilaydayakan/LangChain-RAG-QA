from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline

from transformers import pipeline

# HuggingFace pipeline (LLM)
qa_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=512,
    temperature=0.7,
    repetition_penalty=1.2
)
llm = HuggingFacePipeline(pipeline=qa_pipeline)

def setup_rag_system():
    loader = TextLoader("my_document.txt")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(chunks, embeddings)

    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    return retriever

async def get_rag_response(query: str):
    retriever = setup_rag_system()
    retrieved_docs = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in retrieved_docs])
    prompt = f"""
You are a helpful assistant that answers questions using the provided context only.

Provide accurate, factually correct answers based strictly on the given text. Do not make assumptions or add information. If the answer is not in the context, say "Not found in the document."

Context:
{context}

Question: {query}

Answer:
"""

    response = llm.invoke(prompt)
    return response












