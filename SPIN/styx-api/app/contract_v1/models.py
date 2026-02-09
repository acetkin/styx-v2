from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class ContractModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class RequestMetadata(ContractModel):
    styx_version: str
    request_id: str
    intent: str
    timezone: str | None = None


class PlayerIdentity(ContractModel):
    id: str | None = None
    name: str | None = None


class PlayerBirth(ContractModel):
    date: str | None = None
    time: str | None = None
    place: str | None = None
    country_code: str | None = None


class Player(ContractModel):
    identity: PlayerIdentity = Field(default_factory=PlayerIdentity)
    birth: PlayerBirth = Field(default_factory=PlayerBirth)
    facts: dict[str, Any] = Field(default_factory=dict)


class RequestSettings(ContractModel):
    house_system: str | None = None
    zodiac: Literal["tropical", "sidereal"] | None = None


class RequestOutput(ContractModel):
    verbosity: Literal["minimal", "normal", "verbose"] | None = None
    astrological_objects: list[str] | None = None


class RequestBlock(ContractModel):
    settings: RequestSettings = Field(default_factory=RequestSettings)
    parameters: dict[str, Any] = Field(default_factory=dict)
    output: RequestOutput = Field(default_factory=RequestOutput)


class UniversalRequest(ContractModel):
    metadata: RequestMetadata
    player: Player
    request: RequestBlock


class ErrorInvalidItem(ContractModel):
    path: str
    reason: str | None = None
    expected: str | None = None
    received: Any | None = None


class ContractErrorPayload(ContractModel):
    error_code: Literal["INVALID_REQUEST", "VALIDATION_ERROR", "UNSUPPORTED_INTENT", "INTERNAL_ERROR"]
    missing: list[str] = Field(default_factory=list)
    invalid: list[ErrorInvalidItem] = Field(default_factory=list)


class ContractResponseMetadata(ContractModel):
    styx_version: str


class ContractResponseBody(ContractModel):
    summary: dict[str, Any] = Field(default_factory=dict)
    data: dict[str, Any] = Field(default_factory=dict)


class ContractResponse(ContractModel):
    status: Literal["contract", "ok", "error"]
    metadata: ContractResponseMetadata
    response: ContractResponseBody


class ContractRequest(UniversalRequest):
    """Named request model for the universal contract endpoint."""
