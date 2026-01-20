#app\retrieval\embeddings.py

from sentence_transformers import SentenceTransformer
from typing import List
import threading


class EmbeddingService:
    _model = None
    _lock = threading.Lock()

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name

    def _load_model(self):
        if self.__class__._model is None:
            with self.__class__._lock:
                if self.__class__._model is None:
                    self.__class__._model = SentenceTransformer(
                        self.model_name,
                        device="cpu",
                    )

    def embed(self, texts: List[str]) -> List[list[float]]:
        self._load_model()
        return self.__class__._model.encode(
            texts,
            normalize_embeddings=True,
        ).tolist()
