from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager

from app.db.database import get_db, init_db
from app.db.models import Document
from app.schemas.document import DocumentCreate, DocumentRead


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="RAG German Docs",
    lifespan=lifespan,
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/documents", response_model=DocumentRead, status_code=201)
def create_document(
    doc: DocumentCreate,
    db: Session = Depends(get_db),
):
    document = Document(
        title=doc.title,
        filename=doc.filename,
        text=doc.text,
    )
    db.add(document)
    db.commit()
    db.refresh(document)
    return document


@app.get("/documents/{document_id}", response_model=DocumentRead)
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    document = db.get(Document, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document
