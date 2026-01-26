from typing import Dict

from app.retrieval.vector_store import VectorStore
from app.retrieval.retriever import Retriever
from app.retrieval.context_builder import ContextBuilder
from app.llm.client import LLMClient, LLMUnavailable
from app.llm.prompt import PromptBuilder


class QueryService:
    """
    Orchestrates retrieval + context building + LLM answering.
    """

    def __init__(self):
        self.vector_store = VectorStore()
        self.retriever = Retriever(self.vector_store)
        self.context_builder = ContextBuilder(max_chars=2000)
        self.prompt_builder = PromptBuilder()

    def query(self, question: str, top_k: int = 5) -> Dict:
        # 1. Retrieve relevant chunks
        hits = self.retriever.search(query=question, top_k=top_k)

        # 2. Build LLM context
        context = self.context_builder.build(hits)

        # 3. Generate answer
        try:
            prompt = self.prompt_builder.build(
                query=question,
                context_blocks=context,
            )
            llm = LLMClient()
            answer = llm.generate(prompt)

        except LLMUnavailable:
            answer = (
                "Relevant documents were found, but the language model "
                "is currently unavailable."
            )

        return {
            "query": question,
            "answer": answer,
            "sources": context,
        }
