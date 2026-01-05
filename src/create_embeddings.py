import os
import google.generativeai as genai
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

CHUNK_DIR = "data/chunks"
DB_DIR = "chroma_db"

docs = []
for file in os.listdir(CHUNK_DIR):
    with open(os.path.join(CHUNK_DIR, file), encoding="utf-8") as f:
        docs.append(Document(page_content=f.read(), metadata={"source": file}))

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"
)

db = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory=DB_DIR
)

db.persist()
print("✅ Gemini embeddings stored in ChromaDB")
