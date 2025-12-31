from app.retrieval.embeddings import EmbeddingService
from app.retrieval.vector_store import VectorStore


class SemanticSearcher:
    def __init__(self):
        self.embedder = EmbeddingService()
        self.vector_store = VectorStore()

    def search(self, query: str, k: int = 5) -> list[dict]:
        query_embedding = self.embedder.embed([query])[0]

        raw_results = self.vector_store.search(
            query_embedding=query_embedding,
            k=k,
        )

        documents = raw_results["documents"][0]
        metadatas = raw_results["metadatas"][0]
        distances = raw_results["distances"][0]

        results = []
        for doc, meta, dist in zip(documents, metadatas, distances):
            results.append(
                {
                    "text": doc,
                    "score": float(1 - dist),  # cosine similarity
                    "metadata": meta,
                }
            )

        return results
