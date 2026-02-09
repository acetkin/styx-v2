from __future__ import annotations

import logging

from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from app.contract_v1.dispatcher import dispatch_universal_request
from app.contract_v1.models import ContractRequest, ContractResponse
from app.contract_v1.responses import error_response

router = APIRouter()
_contract_logger = logging.getLogger("styx.contract_v1")


@router.post("/v1/contract", response_model=ContractResponse)
async def contract_endpoint(
    req: ContractRequest = Body(..., description="Universal contract request envelope."),
) -> ContractResponse | JSONResponse:
    payload = req.model_dump(exclude_none=True)
    try:
        body, http_status = dispatch_universal_request(req, payload)
        validated = ContractResponse.model_validate(body)
        if http_status == 200:
            return validated
    except Exception as exc:
        _contract_logger.exception("contract_v1_internal_error intent=%s", req.metadata.intent)
        message = "Unexpected server error. Check server logs."
        body, http_status = error_response(
            error_code="INTERNAL_ERROR",
            summary={"intent": req.metadata.intent, "message": message},
            invalid=[{"path": "/", "reason": message, "expected": "valid request", "received": None}],
            http_status=500,
        )
        validated = ContractResponse.model_validate(body)
    return JSONResponse(status_code=http_status, content=validated.model_dump(exclude_none=True))
