#app\routers\documents.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.ingestion.ingest import ingest_document
from app.schemas.document import DocumentCreate, DocumentResponse

router = APIRouter(
    prefix="/documents",
    tags=["documents"],
)


@router.post("", response_model=DocumentResponse)
def create_document(
    payload: DocumentCreate,
    db: Session = Depends(get_db),
):
    document = ingest_document(
        db=db,
        title=payload.title,
        filename=payload.filename,
        text=payload.text,
    )

    return DocumentResponse(
        id=document.id,
        title=document.title,
        filename=document.filename,
        created_at=document.created_at.isoformat(),
        chunks=len(document.chunks),
    )
