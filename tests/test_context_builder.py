from app.retrieval.context_builder import ContextBuilder


def test_context_builder_merging():
    hits = [
        {
            "text": "FastAPI is a web framework.",
            "metadata": {"document_id": 1, "chunk_id": 1},
            "score": 0.9,
        },
        {
            "text": "It is built on Starlette.",
            "metadata": {"document_id": 1, "chunk_id": 2},
            "score": 0.8,
        },
    ]

    builder = ContextBuilder(max_chars=2000)
    context = builder.build(hits)

    assert len(context) == 1
    assert "FastAPI" in context[0]["text"]
