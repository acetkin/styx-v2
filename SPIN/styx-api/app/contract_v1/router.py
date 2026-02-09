from __future__ import annotations

from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from app.contract_v1.dispatcher import dispatch_universal_request
from app.contract_v1.models import UniversalRequest
from app.contract_v1.responses import error_response

router = APIRouter()


@router.post("/v1/contract")
async def contract_endpoint(
    req: UniversalRequest = Body(..., description="Universal contract request envelope."),
) -> JSONResponse:
    payload = req.model_dump(exclude_none=True)
    try:
        body, http_status = dispatch_universal_request(req, payload)
    except Exception as exc:
        message = str(exc) or "Internal server error"
        body, http_status = error_response(
            error_code="INTERNAL_ERROR",
            summary={"intent": req.metadata.intent, "message": message},
            invalid=[{"path": "/", "reason": message, "expected": None, "received": None}],
            http_status=500,
        )
    return JSONResponse(status_code=http_status, content=body)
