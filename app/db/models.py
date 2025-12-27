from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.db.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=True)
    filename = Column(String(255), nullable=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
