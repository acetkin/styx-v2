from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from zoneinfo import ZoneInfo

from app.contract_v1.contract_store import load_contract
from app.contract_v1.models import ContractRequest
from app.contract_v1.responses import contract_response, error_response, ok_response
from app.models import Settings
from app.services.astro import calc_chart


def _path_exists(payload: dict[str, Any], path: str) -> bool:
    current: Any = payload
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return False
        current = current[part]
    return current is not None


def _missing_required_paths(payload: dict[str, Any], required_paths: list[str]) -> list[str]:
    return [path for path in required_paths if not _path_exists(payload, path)]


def _resolve_datetime_utc(parsed: ContractRequest) -> tuple[str | None, list[dict[str, Any]]]:
    birth = parsed.player.birth
    timezone_name = parsed.metadata.timezone
    invalid: list[dict[str, Any]] = []

    if not birth.time:
        invalid.append(
            {
                "path": "player.birth.time",
                "reason": "Birth time is required for natal intent in the current implementation.",
                "expected": "HH:MM",
                "received": None,
            }
        )
    if not timezone_name:
        invalid.append(
            {
                "path": "metadata.timezone",
                "reason": "Timezone is required for natal intent in the current implementation.",
                "expected": "IANA timezone (e.g. Europe/Istanbul)",
                "received": None,
            }
        )
    if invalid:
        return None, invalid

    date_raw = birth.date or ""
    time_raw = birth.time or ""
    try:
        local_dt = datetime.strptime(f"{date_raw} {time_raw}", "%Y-%m-%d %H:%M")
    except ValueError:
        return None, [
            {
                "path": "player.birth.date|player.birth.time",
                "reason": "Invalid date/time format.",
                "expected": "YYYY-MM-DD and HH:MM",
                "received": f"{date_raw} {time_raw}",
            }
        ]

    try:
        tz = ZoneInfo(timezone_name or "")
    except Exception:
        return None, [
            {
                "path": "metadata.timezone",
                "reason": "Unknown timezone.",
                "expected": "Valid IANA timezone",
                "received": timezone_name,
            }
        ]

    dt_utc = local_dt.replace(tzinfo=tz).astimezone(timezone.utc)
    return dt_utc.isoformat().replace("+00:00", "Z"), []


def _resolve_location(parsed: ContractRequest) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
    params = parsed.request.parameters or {}
    invalid: list[dict[str, Any]] = []
    location_value = params.get("location")
    lat = None
    lon = None
    alt_m = 0.0
    place = parsed.player.birth.place

    if isinstance(location_value, dict):
        lat = location_value.get("lat")
        lon = location_value.get("lon")
        alt_m = float(location_value.get("alt_m", 0.0))
        place = location_value.get("place", place)
    else:
        lat = params.get("lat")
        lon = params.get("lon")
        if "alt_m" in params:
            alt_m = float(params.get("alt_m", 0.0))

    if lat is None or lon is None:
        invalid.append(
            {
                "path": "request.parameters.location.lat|request.parameters.location.lon",
                "reason": "Explicit location coordinates are required for natal intent. Geocoding is not used in contract-first mode.",
                "expected": "numeric lat/lon",
                "received": {"lat": lat, "lon": lon},
            }
        )
        return None, invalid

    try:
        location = {
            "lat": float(lat),
            "lon": float(lon),
            "alt_m": float(alt_m),
            "place": place,
        }
    except (TypeError, ValueError):
        return None, [
            {
                "path": "request.parameters.location",
                "reason": "Invalid location coordinate types.",
                "expected": "numeric lat/lon/alt_m",
                "received": location_value if isinstance(location_value, dict) else {"lat": lat, "lon": lon, "alt_m": alt_m},
            }
        ]
    return location, []


def _resolve_settings(parsed: ContractRequest) -> Settings:
    settings = parsed.request.settings
    house_system = settings.house_system or "placidus"
    zodiac = settings.zodiac or "tropical"
    return Settings(house_system=house_system, zodiac=zodiac, coordinate_system="ecliptic")


def _handle_natal(parsed: ContractRequest) -> tuple[dict[str, Any], int]:
    datetime_utc, dt_invalid = _resolve_datetime_utc(parsed)
    if dt_invalid:
        return error_response(
            error_code="VALIDATION_ERROR",
            summary={"intent": "natal"},
            invalid=dt_invalid,
            http_status=422,
        )

    location, loc_invalid = _resolve_location(parsed)
    if loc_invalid:
        return error_response(
            error_code="VALIDATION_ERROR",
            summary={"intent": "natal"},
            invalid=loc_invalid,
            http_status=422,
        )

    try:
        payload = calc_chart(
            chart_type="natal",
            timestamp_utc=datetime_utc or "",
            location=location or {},
            settings=_resolve_settings(parsed),
        )
    except Exception as exc:
        # Bubble up as INTERNAL_ERROR at router level.
        raise RuntimeError(f"natal_compute_failed: {exc}") from exc

    return ok_response(
        intent="natal",
        summary={"datetime_utc": datetime_utc},
        data={"natal": payload},
    )


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

    if intent == "natal":
        return _handle_natal(parsed)

    # Not implemented yet: intent handlers will be connected here incrementally.
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
