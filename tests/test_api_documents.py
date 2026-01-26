def test_create_document(client):
    payload = {
        "title": "Test Doc",
        "filename": "test.txt",
        "text": "FastAPI is a modern Python web framework."
    }

    response = client.post("/documents/", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "id" in data
    assert data["chunks"] > 0
