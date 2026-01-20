from fastapi import APIRouter, Query

from app.services.query_service import QueryService
from app.schemas.search import SearchResponse

router = APIRouter(
    prefix="/search",
    tags=["search"],
)


@router.get("", response_model=SearchResponse)
def search(
    q: str = Query(..., min_length=2),
    k: int = Query(5, ge=1, le=20),
):
    service = QueryService()
    result = service.query(question=q, top_k=k)

    return SearchResponse(**result)
