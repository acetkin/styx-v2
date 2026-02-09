from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import app


FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures" / "contract_v1"


def _client(monkeypatch: object | None = None) -> TestClient:
    if monkeypatch is not None:
        ephe_path = Path(__file__).resolve().parents[1] / "ephe"
        if ephe_path.exists():
            monkeypatch.setenv("SE_EPHE_PATH", str(ephe_path))
        monkeypatch.setenv("STYX_GEOCODE_STUB", "41.2795516,31.4229672,0,Karadeniz Eregli")
        monkeypatch.setenv("STYX_GEOIP_STUB", "41.2795516,31.4229672,0,Karadeniz Eregli")
    return TestClient(app)


def _contract_payload() -> dict:
    path = Path(__file__).resolve().parents[2] / "docs" / "contract.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _contract_version() -> str:
    return str(_contract_payload().get("styx_version") or "unknown")


def _load_fixture(intent: str) -> dict:
    path = FIXTURE_DIR / f"{intent}.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["metadata"]["styx_version"] = _contract_version()
    return payload


def _implemented_intents() -> list[str]:
    payload = _contract_payload()
    intents = payload.get("intents", {})
    if not isinstance(intents, dict):
        return []
    return sorted(str(key) for key in intents.keys())


def _required_path_cases() -> list[tuple[str, str]]:
    payload = _contract_payload()
    intents = payload.get("intents", {})
    if not isinstance(intents, dict):
        return []
    cases: list[tuple[str, str]] = []
    for intent, spec in intents.items():
        if not isinstance(spec, dict):
            continue
        req = spec.get("request", {})
        if not isinstance(req, dict):
            continue
        required_paths = req.get("required_paths", [])
        if isinstance(required_paths, list) and required_paths:
            cases.append((str(intent), str(required_paths[0])))
    return sorted(cases)


def _delete_path(payload: dict, dotted_path: str) -> None:
    parts = dotted_path.split(".")
    cur: object = payload
    for part in parts[:-1]:
        if not isinstance(cur, dict) or part not in cur:
            return
        cur = cur[part]
    if isinstance(cur, dict):
        cur.pop(parts[-1], None)


def test_contract_endpoint_happy_contract_payload(monkeypatch: object) -> None:
    client = _client(monkeypatch)
    resp = client.post("/v1/contract", json=_load_fixture("contract"))
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
    schema = post_spec["requestBody"]["content"]["application/json"]["schema"]
    assert schema["$ref"].endswith("/ContractRequest")
    responses = post_spec["responses"]
    assert "200" in responses
    assert responses["200"]["content"]["application/json"]["schema"]["$ref"].endswith("/ContractResponse")


@pytest.mark.parametrize("intent", _implemented_intents())
def test_contract_endpoint_invalid_request_shape(intent: str) -> None:
    client = _client()
    resp = client.post("/v1/contract", json={"metadata": {"intent": intent}})
    assert resp.status_code == 422
    payload = resp.json()
    assert payload["status"] == "error"
    assert payload["response"]["data"]["error"]["error_code"] == "VALIDATION_ERROR"
    assert payload["response"]["data"]["error"]["invalid"]


def test_contract_endpoint_unsupported_intent() -> None:
    client = _client()
    req = _load_fixture("natal")
    req["metadata"]["intent"] = "does_not_exist"
    resp = client.post("/v1/contract", json=req)
    assert resp.status_code == 400
    payload = resp.json()
    assert payload["status"] == "error"
    assert payload["response"]["data"]["error"]["error_code"] == "UNSUPPORTED_INTENT"


@pytest.mark.parametrize("intent", _implemented_intents())
def test_contract_endpoint_happy_paths(monkeypatch: object, intent: str) -> None:
    client = _client(monkeypatch)
    req = _load_fixture(intent)
    resp = client.post("/v1/contract", json=req)
    assert resp.status_code == 200
    payload = resp.json()
    if intent == "contract":
        assert payload["status"] == "contract"
        assert payload["response"]["data"]["contract"]
        return
    assert payload["status"] == "ok"
    assert payload["response"]["summary"]["intent"] == intent
    assert payload["response"]["data"][intent] is not None


@pytest.mark.parametrize("intent,required_path", _required_path_cases())
def test_contract_endpoint_validation_missing_required_paths(monkeypatch: object, intent: str, required_path: str) -> None:
    client = _client(monkeypatch)
    req = copy.deepcopy(_load_fixture(intent))
    _delete_path(req, required_path)
    resp = client.post("/v1/contract", json=req)
    assert resp.status_code == 422
    payload = resp.json()
    assert payload["status"] == "error"
    err = payload["response"]["data"]["error"]
    assert err["error_code"] == "VALIDATION_ERROR"
    assert required_path in err["missing"]


def test_contract_endpoint_internal_error_returns_envelope(monkeypatch: object) -> None:
    client = _client(monkeypatch)
    import app.contract_v1.router as router_module

    def _boom(*_args, **_kwargs):
        raise RuntimeError("Contract runtime failed")

    monkeypatch.setattr(router_module, "dispatch_universal_request", _boom)
    resp = client.post("/v1/contract", json=_load_fixture("contract"))
    assert resp.status_code == 500
    payload = resp.json()
    assert payload["status"] == "error"
    err = payload["response"]["data"]["error"]
    assert err["error_code"] == "INTERNAL_ERROR"
    assert payload["response"]["summary"]["message"] == "Unexpected server error. Check server logs."


def test_contract_fixture_smoke_suite(monkeypatch: object) -> None:
    client = _client(monkeypatch)
    paths = sorted(FIXTURE_DIR.glob("*.json"))
    assert paths, "contract fixture directory is empty"
    for path in paths:
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["metadata"]["styx_version"] = _contract_version()
        intent = payload["metadata"]["intent"]
        resp = client.post("/v1/contract", json=payload)
        assert resp.status_code == 200, f"{intent} failed with status {resp.status_code}"
        body = resp.json()
        if intent == "contract":
            assert body["status"] == "contract"
            assert body["response"]["data"]["contract"]
        else:
            assert body["status"] == "ok"
            assert body["response"]["data"][intent] is not None
