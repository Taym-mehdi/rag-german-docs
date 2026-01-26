from app.ingestion.chunker import chunk_sentences


def test_chunking_basic_text():
    text = "FastAPI is great. It is fast. It is modern."
    chunks = chunk_sentences(text)

    assert len(chunks) > 0
    assert "FastAPI" in chunks[0]["text"]
