import os
import uuid
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.ingestion.ingest import ingest_document
from app.ingestion.pdf_reader import PDFReader

router = APIRouter(
    prefix="/documents",
    tags=["documents"],
)

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload-pdf")
def upload_pdf(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    # Save file to disk (company-style)
    file_id = f"{uuid.uuid4()}.pdf"
    file_path = os.path.join(UPLOAD_DIR, file_id)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # Extract text
    text = PDFReader.extract_text(file_path)

    if not text.strip():
        raise HTTPException(status_code=400, detail="No text could be extracted from PDF")

    # Ingest document (reuse pipeline)
    document = ingest_document(
        db=db,
        title=file.filename,
        filename=file.filename,
        text=text,
    )

    return {
        "document_id": document.id,
        "filename": document.filename,
        "message": "PDF ingested successfully",
    }
