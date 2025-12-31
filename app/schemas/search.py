from pydantic import BaseModel
from typing import Any


class SearchResult(BaseModel):
    text: str
    score: float
    metadata: dict[str, Any]


class SearchResponse(BaseModel):
    query: str
    results: list[SearchResult]
