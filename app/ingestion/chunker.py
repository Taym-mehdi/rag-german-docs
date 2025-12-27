#app/ingestion/chunker.py

from typing import List
import re


def split_into_sentences(text: str) -> List[str]:
    """
    Basic sentence splitter.
    Avoids heavy NLP deps for now.
    """
    if not text:
        return []

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in sentences if s.strip()]


def chunk_sentences(
    text: str,
    max_chars: int = 500,
    overlap_sentences: int = 1,
) -> List[dict]:
    """
    Sentence-aware chunking.

    Returns:
    [
        {
            "text": "...",
            "start_sentence": int,
            "end_sentence": int
        }
    ]
    """

    sentences = split_into_sentences(text)
    chunks = []

    current_chunk = []
    current_len = 0
    start_idx = 0

    for idx, sentence in enumerate(sentences):
        sentence_len = len(sentence)

        if current_len + sentence_len > max_chars and current_chunk:
            chunk_text = " ".join(current_chunk)

            chunks.append({
                "text": chunk_text,
                "start_sentence": start_idx,
                "end_sentence": idx - 1,
            })

            # overlap
            current_chunk = current_chunk[-overlap_sentences:]
            current_len = sum(len(s) for s in current_chunk)
            start_idx = idx - overlap_sentences

        current_chunk.append(sentence)
        current_len += sentence_len

    if current_chunk:
        chunks.append({
            "text": " ".join(current_chunk),
            "start_sentence": start_idx,
            "end_sentence": len(sentences) - 1,
        })

    return chunks
