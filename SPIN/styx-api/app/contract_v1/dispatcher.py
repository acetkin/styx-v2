from __future__ import annotations

from typing import Any

from app.contract_v1.contract_store import load_contract
from app.contract_v1.models import ContractRequest
from app.contract_v1.responses import contract_response, error_response
from app.contract_v1.intent_handlers import HANDLERS


def _path_exists(payload: dict[str, Any], path: str) -> bool:
    current: Any = payload
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return False
        current = current[part]
    return current is not None


def _missing_required_paths(payload: dict[str, Any], required_paths: list[str]) -> list[str]:
    return [path for path in required_paths if not _path_exists(payload, path)]


def dispatch_universal_request(parsed: ContractRequest, raw_payload: dict[str, Any]) -> tuple[dict[str, Any], int]:
    contract = load_contract()
    intent = parsed.metadata.intent

    if intent == "contract":
        return contract_response(contract)

    intents = contract.get("intents", {})
    spec = intents.get(intent)
    if not isinstance(spec, dict):
        return error_response(
            error_code="UNSUPPORTED_INTENT",
            summary={"intent": intent},
            invalid=[
                {
                    "path": "metadata.intent",
                    "reason": "Intent is not recognized by this Styx version.",
                    "expected": "One of contract intents",
                    "received": intent,
                }
            ],
            http_status=400,
        )

    request_spec = spec.get("request", {})
    required_paths = request_spec.get("required_paths", [])
    missing = _missing_required_paths(raw_payload, [str(path) for path in required_paths])
    if missing:
        return error_response(
            error_code="VALIDATION_ERROR",
            summary={"intent": intent},
            missing=missing,
            http_status=422,
        )

    handler = HANDLERS.get(intent)
    if handler is None:
        return error_response(
            error_code="UNSUPPORTED_INTENT",
            summary={"intent": intent},
            invalid=[
                {
                    "path": "metadata.intent",
                    "reason": "Intent is recognized but not implemented yet.",
                    "expected": "Implemented contract intent",
                    "received": intent,
                }
            ],
            http_status=400,
        )
    return handler(parsed)
