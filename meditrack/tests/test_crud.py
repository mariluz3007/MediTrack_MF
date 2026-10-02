def test_dashboard_loads(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Panel de control".encode() in response.data
