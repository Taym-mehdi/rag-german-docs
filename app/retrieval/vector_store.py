#app\retrieval\vector_store.py
import chromadb
from chromadb.config import Settings
from typing import List
from typing import Optional


class VectorStore:
    def __init__(self, persist_dir: str = "data/chroma"):
        self.client = chromadb.PersistentClient(
            path=persist_dir,
            settings=chromadb.Settings(
                anonymized_telemetry=False
            )
        )

        self.collection = self.client.get_or_create_collection(
            name="document_chunks",
            metadata={"hnsw:space": "cosine"},
        )

    def add(
        self,
        ids: List[str],
        embeddings: List[list[float]],
        documents: List[str],
        metadatas: List[dict],
    ) -> None:
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )
    
    def search(
        self,
        query_embedding: list[float],
        k: int = 5,
    ) -> dict:
        """
        Semantic search in Chroma.
        Returns documents, metadata, and distances.
        """
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k,
            include=["documents", "metadatas", "distances"],
        )

        return results