from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_inference_endpoint():

    response = client.post(
        "/infer",
        json={
            "prompt": "hello"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "response" in data
    assert "latency" in data
    assert "confidence" in data