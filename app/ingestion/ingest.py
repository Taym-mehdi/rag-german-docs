#app/ingestion/ingest.py

from sqlalchemy.orm import Session

from app.db.models import Document, Chunk
from app.ingestion.chunker import chunk_sentences


def ingest_document(
    db: Session,
    title: str | None,
    filename: str | None,
    text: str,
) -> Document:
    """
    Day 3 ingestion:
    - Store document
    - Sentence-based chunking
    - Store chunks
    """

    document = Document(
        title=title,
        filename=filename,
        text=text,
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    chunks = chunk_sentences(text)

    for c in chunks:
        chunk = Chunk(
            document_id=document.id,
            text=c["text"],
            start_sentence=c["start_sentence"],
            end_sentence=c["end_sentence"],
        )
        db.add(chunk)

    db.commit()
    db.refresh(document)

    return document
