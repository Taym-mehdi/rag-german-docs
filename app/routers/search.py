from fastapi import APIRouter, Query

from app.retrieval.vector_store import VectorStore
from app.retrieval.retriever import Retriever
from app.retrieval.context_builder import ContextBuilder
from app.llm.client import LLMClient, LLMUnavailable
from app.llm.prompt import PromptBuilder
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
    vector_store = VectorStore()
    retriever = Retriever(vector_store)
    context_builder = ContextBuilder(max_chars=2000)

    hits = retriever.search(query=q, top_k=k)
    context = context_builder.build(hits)

    answer: str

    try:
        prompt = PromptBuilder().build(query=q, context_blocks=context)
        llm = LLMClient()
        answer = llm.generate(prompt)

    except LLMUnavailable:
        # Professional fallback
        answer = (
            "The relevant information was found in the documents below, "
            "but the language model is currently unavailable."
        )

    return SearchResponse(
        query=q,
        answer=answer,
        sources=context,
    )
