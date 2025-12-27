from datetime import datetime
from pydantic import BaseModel, Field


class DocumentCreate(BaseModel):
    title: str | None = Field(default=None, max_length=255)
    filename: str | None = Field(default=None, max_length=255)
    text: str = Field(..., min_length=1)


class DocumentRead(BaseModel):
    id: int
    title: str | None
    filename: str | None
    text: str
    created_at: datetime

    class Config:
        from_attributes = True
