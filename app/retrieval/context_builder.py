# app/retrieval/context_builder.py

from typing import List, Dict


class ContextBuilder:
    def __init__(self, max_chars: int = 2000):
        #Approximate size control before sending context to an LLM.
        self.max_chars = max_chars

    def build(self, hits: List[Dict]) -> List[Dict]:
        #Build clean context blocks from raw retrieval hits.
        
        grouped: dict[int, list[Dict]] = {}

        #Group by document_id
        for hit in hits:
            doc_id = hit["metadata"]["document_id"]
            grouped.setdefault(doc_id, []).append(hit)

        context_blocks: List[Dict] = []
        total_chars = 0

        #Process each document separately
        for doc_id, chunks in grouped.items():
            # Sort by sentence position
            chunks.sort(key=lambda c: c["metadata"]["chunk_id"])

            merged_texts: List[str] = []
            current_text = ""

            for chunk in chunks:
                text = chunk["text"]

                # Merge adjacent chunks
                if not current_text:
                    current_text = text
                else:
                    candidate = current_text + " " + text
                    if len(candidate) <= self.max_chars:
                        current_text = candidate
                    else:
                        merged_texts.append(current_text)
                        current_text = text

            if current_text:
                merged_texts.append(current_text)

            # Add to final context (respect global size limit)
            for block in merged_texts:
                if total_chars + len(block) > self.max_chars:
                    return context_blocks

                context_blocks.append({
                    "document_id": doc_id,
                    "text": block,
                })
                total_chars += len(block)

        return context_blocks
