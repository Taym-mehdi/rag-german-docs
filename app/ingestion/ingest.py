#app\ingestion\ingest.py

from sqlalchemy.orm import Session

from app.db.models import Document, Chunk
from app.ingestion.chunker import chunk_sentences
from app.retrieval.embeddings import EmbeddingService
from app.retrieval.vector_store import VectorStore


def ingest_document(
    db: Session,
    title: str | None,
    filename: str | None,
    text: str,
) -> Document:
    """
    - Store document
    - Sentence chunking
    - Store chunks
    - Embed chunks
    - Store vectors
    """

    document = Document(
        title=title,
        filename=filename,
        text=text,
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    chunks_data = chunk_sentences(text)
    chunk_objects: list[Chunk] = []

    for c in chunks_data:
        chunk = Chunk(
            document_id=document.id,
            text=c["text"],
            start_sentence=c["start_sentence"],
            end_sentence=c["end_sentence"],
        )
        db.add(chunk)
        chunk_objects.append(chunk)

    db.commit()
    db.refresh(document)

    # --- Embeddings ---
    texts = [c.text for c in chunk_objects]

    embedder = EmbeddingService()
    embeddings = embedder.embed(texts)

    vector_store = VectorStore()

    ids = [str(c.id) for c in chunk_objects]
    metadatas = [
        {
            "document_id": document.id,
            "chunk_id": c.id,
            "filename": document.filename,
        }
        for c in chunk_objects
    ]

    vector_store.add(
        ids=ids,
        embeddings=embeddings,
        documents=texts,
        metadatas=metadatas,
    )

    return document
