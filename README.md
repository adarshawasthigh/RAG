# Gemini-powered RAG System (Game of Thrones)

A Retrieval-Augmented Generation (RAG) pipeline using **Google Gemini** for
both embeddings and generation.

## Architecture
Data → Cleaning → Chunking → Gemini Embeddings → ChromaDB → Gemini LLM

## Models Used
- Embeddings: `models/embedding-001`
- LLM: `gemini-2.5-flash`

## How to Run
```bash
pip install -r requirements.txt
python src/load_docs.py
python src/clean_docs.py
python src/chunk_docs.py
python src/create_embeddings.py
python src/rag_query.py
