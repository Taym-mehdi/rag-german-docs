#app\retrieval\retriever.py
from typing import List, Dict

from app.retrieval.vector_store import VectorStore
from app.retrieval.embeddings import EmbeddingService


class Retriever:
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store
        self.embedding_service = EmbeddingService()

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> List[Dict]:
        """
        Perform semantic search over document chunks.
        """

        # Embed query (EmbeddingService expects a list)
        query_embedding = self.embedding_service.embed([query])[0]

        results = self.vector_store.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=["documents", "metadatas", "distances"],
        )

        hits = []
        for i in range(len(results["documents"][0])):
            hits.append({
                "text": results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
                "score": float(results["distances"][0][i]),
            })

        return hits
