#app/db/models.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime , UTC 

from app.db.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=True)
    filename = Column(String(512), nullable=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now(UTC))

    chunks = relationship(
        "Chunk",
        back_populates="document",
        cascade="all, delete-orphan",
    )


class Chunk(Base):
    __tablename__ = "chunks"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)

    text = Column(Text, nullable=False)

    start_sentence = Column(Integer, nullable=False)
    end_sentence = Column(Integer, nullable=False)

    document = relationship("Document", back_populates="chunks")
