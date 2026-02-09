from __future__ import annotations

from typing import Any

from app.contract_v1.contract_store import styx_version


ERROR_CODES = {
    "INVALID_REQUEST",
    "VALIDATION_ERROR",
    "UNSUPPORTED_INTENT",
    "INTERNAL_ERROR",
}


def _base_response(status: str, summary: dict[str, Any] | None = None, data: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "status": status,
        "metadata": {"styx_version": styx_version()},
        "response": {
            "summary": summary or {},
            "data": data or {},
        },
    }


def contract_response(contract: dict[str, Any]) -> tuple[dict[str, Any], int]:
    body = _base_response(
        status="contract",
        summary={"intent": "contract"},
        data={"contract": contract},
    )
    return body, 200


def ok_response(*, intent: str, summary: dict[str, Any] | None = None, data: dict[str, Any] | None = None) -> tuple[dict[str, Any], int]:
    merged_summary = {"intent": intent}
    if summary:
        merged_summary.update(summary)
    body = _base_response(status="ok", summary=merged_summary, data=data or {})
    return body, 200


def error_response(
    *,
    error_code: str,
    missing: list[str] | None = None,
    invalid: list[dict[str, Any]] | None = None,
    summary: dict[str, Any] | None = None,
    http_status: int = 400,
) -> tuple[dict[str, Any], int]:
    if error_code not in ERROR_CODES:
        error_code = "INTERNAL_ERROR"
    payload = {
        "error_code": error_code,
        "missing": missing or [],
        "invalid": invalid or [],
    }
    body = _base_response(
        status="error",
        summary=summary or {},
        data={"error": payload},
    )
    return body, http_status

