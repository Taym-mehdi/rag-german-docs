# RAG German Docs — Production-Style Retrieval-Augmented Generation Backend

A production-oriented Retrieval-Augmented Generation (RAG) backend built with FastAPI, SQLAlchemy, ChromaDB, and Docker.
The system ingests documents, semantically indexes them, and answers user queries using grounded context retrieved from a
vector database and a Large Language Model (LLM).

This project was designed and implemented following industry best practices, with a strong focus on clean architecture,
maintainability, testability, and deployability. It is a portfolio project demonstrating backend engineering
and applied NLP skills.

---

## Overview

The application provides a complete RAG pipeline:
- Document ingestion (text and PDF)
- Sentence-level chunking
- Persistent storage of documents and chunks
- Embedding generation using sentence-transformers
- Vector-based semantic search with ChromaDB
- Context construction with size control
- Grounded prompt generation
- LLM-based answer generation with graceful fallback handling

---

## Architecture


The architecture follows separation of concerns:
- API layer handles HTTP and validation
- Service layer orchestrates business logic
- Retrieval layer handles embeddings and vector search
- Persistence layer manages relational data
- LLM layer is abstracted behind a clean interface

---

## Project Structure

rag-german-docs/

app/  
- main.py              FastAPI application entrypoint  
- config.py            Environment and settings  
- db/                  SQLAlchemy database setup and models  
- ingestion/           Chunking, ingestion logic, PDF reader  
- retrieval/           Embeddings, vector store, retriever, context builder  
- llm/                 LLM client and prompt construction  
- services/            High-level query orchestration  
- routers/             API routes  
- schemas/             Pydantic request/response models  

data/  
- SQLite database and ChromaDB persistence  

tests/  
- Automated tests  

Dockerfile  
docker-compose.yml  
requirements.txt  
README.md  

---

## Technology Stack

- Language: Python 3.11
- Web Framework: FastAPI
- ORM: SQLAlchemy
- Vector Database: ChromaDB
- Embeddings: sentence-transformers (MiniLM)
- LLM Provider: OpenAI API (abstracted client)
- Database: SQLite
- Containerization: Docker and docker-compose

---

## Running the Project (Recommended: Docker)

Prerequisites:
- Docker
- Docker Compose

Start the application:

docker compose up --build

The API will be available at:
http://127.0.0.1:8000

Interactive API documentation:
http://127.0.0.1:8000/docs

---

## Example API Usage

Create a document:

POST /documents

{
  "title": "FastAPI Introduction",
  "filename": "fastapi.txt",
  "text": "FastAPI is a modern Python web framework..."
}

Search documents:

GET /search?q=What is FastAPI?

The response includes:
- The generated answer
- The retrieved source context used for grounding

---

## Testing

The project includes a test structure designed for:
- API endpoint validation
- Ingestion pipeline correctness
- Retrieval and context building logic
- Error handling and fallback behavior

The codebase is structured to make unit and integration testing straightforward.

---

## Engineering Highlights

- Sentence-based chunking for semantic coherence
- Lazy-loaded embedding model to reduce startup cost
- Persistent vector storage for fast restarts
- Context size control to prevent LLM overflow
- Clean abstraction over LLM providers
- Graceful degradation when the LLM is unavailable
- Dockerized for reproducible deployments

---

## What This Project Demonstrates

This project demonstrates practical, job-relevant skills in:
- Backend API development
- Applied NLP and RAG systems
- Vector databases and semantic search
- Clean Python architecture
- Production-oriented error handling
- Containerization and deployment readiness

It reflects the type of system commonly built in real-world AI and backend engineering teams.

---

## Author

Developed as a portfolio and learning project to demonstrate backend engineering and applied AI skills suitable for
junior to mid-level backend or AI engineering roles.

---

## License

This project is provided for educational and portfolio purposes.
