import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_to_speech_missing_text():
    resp = client.post("/api/to_speech", json={})
    assert resp.status_code == 400

def test_to_speech_ok():
    resp = client.post("/api/to_speech", json={"text": "Test"})
    assert resp.status_code == 200
    assert resp.headers["content-type"] == "audio/wav"

def test_set_parameter():
    resp = client.patch("/api/set_parameter", json={"name": "rate", "value": 180})
    assert resp.status_code == 200
    assert resp.json()["rate"] == 180