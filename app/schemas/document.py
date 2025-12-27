from pydantic import BaseModel
from typing import Optional


class DocumentCreate(BaseModel):
    title: Optional[str] = None
    filename: Optional[str] = None
    text: str


class DocumentResponse(BaseModel):
    id: int
    title: Optional[str]
    filename: Optional[str]
    created_at: str
    chunks: int
