from __future__ import annotations

import json
from typing import Any

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.contract_v1.dispatcher import dispatch_universal_request
from app.contract_v1.models import UniversalRequest
from app.contract_v1.responses import error_response

router = APIRouter()


def _loc_to_path(loc: tuple[Any, ...] | list[Any]) -> str:
    if not loc:
        return "/"
    return ".".join(str(part) for part in loc)


@router.post("/v1/contract")
async def contract_endpoint(request: Request) -> JSONResponse:
    raw_bytes = await request.body()
    try:
        payload = json.loads(raw_bytes.decode("utf-8"))
    except Exception:
        body, http_status = error_response(
            error_code="INVALID_REQUEST",
            invalid=[
                {
                    "path": "/",
                    "reason": "Request body must be valid JSON object.",
                    "expected": "JSON object",
                    "received": "invalid_json",
                }
            ],
            http_status=400,
        )
        return JSONResponse(status_code=http_status, content=body)

    if not isinstance(payload, dict):
        body, http_status = error_response(
            error_code="INVALID_REQUEST",
            invalid=[
                {
                    "path": "/",
                    "reason": "Top-level payload must be an object.",
                    "expected": "JSON object",
                    "received": type(payload).__name__,
                }
            ],
            http_status=400,
        )
        return JSONResponse(status_code=http_status, content=body)

    missing_top = [key for key in ("metadata", "player", "request") if key not in payload]
    if missing_top:
        body, http_status = error_response(
            error_code="INVALID_REQUEST",
            missing=missing_top,
            http_status=400,
        )
        return JSONResponse(status_code=http_status, content=body)

    try:
        parsed = UniversalRequest.model_validate(payload)
    except ValidationError as exc:
        invalid_items: list[dict[str, Any]] = []
        for err in exc.errors():
            invalid_items.append(
                {
                    "path": _loc_to_path(err.get("loc", [])),
                    "reason": err.get("msg", "Validation error"),
                    "expected": err.get("type"),
                    "received": None,
                }
            )
        intent = None
        if isinstance(payload.get("metadata"), dict):
            intent = payload["metadata"].get("intent")
        summary = {"intent": intent} if intent is not None else {}
        body, http_status = error_response(
            error_code="VALIDATION_ERROR",
            invalid=invalid_items,
            summary=summary,
            http_status=422,
        )
        return JSONResponse(status_code=http_status, content=body)

    try:
        body, http_status = dispatch_universal_request(parsed, payload)
    except Exception:
        body, http_status = error_response(
            error_code="INTERNAL_ERROR",
            http_status=500,
        )
    return JSONResponse(status_code=http_status, content=body)

