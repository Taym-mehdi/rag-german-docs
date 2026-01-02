from typing import List, Dict


class PromptBuilder:
    def build(
        self,
        query: str,
        context_blocks: List[Dict],
    ) -> str:
        """
        Build a grounded RAG prompt.
        """

        context_text = "\n\n".join(
            f"[Document {c['document_id']}]\n{c['text']}"
            for c in context_blocks
        )

        prompt = f"""
You are an assistant answering questions using ONLY the provided context.
If the answer is not contained in the context, say you do not know.

Context:
{context_text}

Question:
{query}

Answer:
""".strip()

        return prompt
