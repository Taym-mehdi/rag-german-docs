def test_search_endpoint(client):
    response = client.get("/search?q=FastAPI")

    assert response.status_code == 200
    data = response.json()

    assert "answer" in data
    assert "sources" in data
