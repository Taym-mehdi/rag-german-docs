from pydantic import BaseModel
from typing import List


class ContextBlock(BaseModel):
    document_id: int
    text: str


class SearchResponse(BaseModel):
    query: str
    answer: str
    sources: List[ContextBlock]
