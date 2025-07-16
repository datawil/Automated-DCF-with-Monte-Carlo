from fastapi.testclient import TestClient
from api.fastapi_app import app

client = TestClient(app)

def test_dcf_endpoint():
    response = client.get("/dcf/AAPL?wacc=0.08")
    assert response.status_code == 200
    data = response.json()
    assert 'dcf' in data
    assert 'monte_carlo' in data