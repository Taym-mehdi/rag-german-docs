from fastapi import APIRouter, Query
from app.retrieval.search import SemanticSearcher
from app.schemas.search import SearchResponse

router = APIRouter(prefix="/search", tags=["search"])

searcher = SemanticSearcher()


@router.get("", response_model=SearchResponse)
def semantic_search(
    q: str = Query(..., min_length=3),
    k: int = Query(5, ge=1, le=20),
):
    results = searcher.search(query=q, k=k)

    return {
        "query": q,
        "results": results,
    }
