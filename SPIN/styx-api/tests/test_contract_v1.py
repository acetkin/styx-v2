from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app


def _client() -> TestClient:
    return TestClient(app)


def _contract_version() -> str:
    path = Path(__file__).resolve().parents[2] / "docs" / "contract.json"
    text = path.read_text(encoding="utf-8")
    # Small and stable enough here; no extra dependency needed.
    marker = '"styx_version": "'
    start = text.find(marker)
    if start == -1:
        return "unknown"
    start += len(marker)
    end = text.find('"', start)
    if end == -1:
        return "unknown"
    return text[start:end]


def _base_payload(intent: str) -> dict:
    return {
        "metadata": {
            "styx_version": _contract_version(),
            "request_id": "req-1",
            "intent": intent,
        },
        "player": {
            "identity": {"id": "p1", "name": "Test"},
            "birth": {
                "date": "1982-05-08",
                "time": "06:39",
                "place": "Karadeniz Eregli",
                "country_code": "TR",
            },
            "facts": {},
        },
        "request": {
            "settings": {"house_system": "placidus", "zodiac": "tropical"},
            "parameters": {},
            "output": {"verbosity": "normal", "astrological_objects": ["natal"]},
        },
    }


def test_contract_endpoint_happy_contract_payload() -> None:
    client = _client()
    resp = client.post("/v1/contract", json=_base_payload("contract"))
    assert resp.status_code == 200
    payload = resp.json()
    assert payload["status"] == "contract"
    assert payload["metadata"]["styx_version"] == _contract_version()
    assert "contract" in payload["response"]["data"]
    assert "intents" in payload["response"]["data"]["contract"]


def test_contract_openapi_has_request_body_schema() -> None:
    client = _client()
    resp = client.get("/openapi.json")
    assert resp.status_code == 200
    payload = resp.json()
    post_spec = payload["paths"]["/v1/contract"]["post"]
    assert "requestBody" in post_spec
    assert "content" in post_spec["requestBody"]
    assert "application/json" in post_spec["requestBody"]["content"]


def test_contract_endpoint_invalid_request_shape() -> None:
    client = _client()
    resp = client.post("/v1/contract", json={"metadata": {"intent": "contract"}})
    assert resp.status_code == 422
    payload = resp.json()
    assert payload["status"] == "error"
    assert payload["response"]["data"]["error"]["error_code"] == "VALIDATION_ERROR"
    assert payload["response"]["data"]["error"]["invalid"]


def test_contract_endpoint_unsupported_intent() -> None:
    client = _client()
    resp = client.post("/v1/contract", json=_base_payload("does_not_exist"))
    assert resp.status_code == 400
    payload = resp.json()
    assert payload["status"] == "error"
    assert payload["response"]["data"]["error"]["error_code"] == "UNSUPPORTED_INTENT"


def test_contract_endpoint_validation_error_for_required_paths() -> None:
    client = _client()
    req = _base_payload("natal")
    req["player"]["birth"].pop("date", None)
    resp = client.post("/v1/contract", json=req)
    assert resp.status_code == 422
    payload = resp.json()
    assert payload["status"] == "error"
    assert payload["response"]["data"]["error"]["error_code"] == "VALIDATION_ERROR"
    assert "player.birth.date" in payload["response"]["data"]["error"]["missing"]


def test_contract_endpoint_internal_error_returns_envelope(monkeypatch: object) -> None:
    client = _client()
    import app.contract_v1.router as router_module

    def _boom(*_args, **_kwargs):
        raise RuntimeError("Contract file missing in runtime")

    monkeypatch.setattr(router_module, "dispatch_universal_request", _boom)
    resp = client.post("/v1/contract", json=_base_payload("contract"))
    assert resp.status_code == 500
    payload = resp.json()
    assert payload["status"] == "error"
    err = payload["response"]["data"]["error"]
    assert err["error_code"] == "INTERNAL_ERROR"
    assert payload["response"]["summary"]["message"] == "Contract file missing in runtime"
