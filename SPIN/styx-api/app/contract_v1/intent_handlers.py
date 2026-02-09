from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, Callable
from zoneinfo import ZoneInfo

from app.contract_v1.models import ContractRequest, PlayerBirth
from app.contract_v1.responses import error_response, ok_response
from app.models import Settings
from app.services.astro import (
    _build_aspect_targets,
    _calc_aspects,
    _calc_cross_aspects,
    _default_aspect_config,
    _normalize_deg,
    _parse_timestamp,
    calc_astrocartography,
    calc_chart,
    round_payload,
)
from app.services.geocode import geocode_ip, geocode_place
from app.services.progression_timeline import build_progression_timeline
from app.services.solar_arc_timeline import build_solar_arc_timeline
from app.services.timeline import build_timeline

HandlerFn = Callable[[ContractRequest], tuple[dict[str, Any], int]]
DEFAULT_TRANSIT_TIMELINE_BODIES = ["jupiter", "saturn", "uranus", "neptune", "pluto"]
DEFAULT_SOLAR_ARC_TIMELINE_BODIES = ["jupiter", "saturn"]


def _invalid(path: str, reason: str, *, expected: str | None = None, received: Any = None) -> dict[str, Any]:
    return {"path": path, "reason": reason, "expected": expected, "received": received}


def _to_iso_z(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def _parse_iso(raw: Any, path: str, *, allow_now: bool = False) -> tuple[str | None, list[dict[str, Any]]]:
    if raw is None:
        if allow_now:
            return _to_iso_z(datetime.now(timezone.utc)), []
        return None, [_invalid(path, "Timestamp is required.", expected="ISO8601", received=None)]
    value = str(raw).strip()
    if not value:
        if allow_now:
            return _to_iso_z(datetime.now(timezone.utc)), []
        return None, [_invalid(path, "Timestamp is required.", expected="ISO8601", received=raw)]
    if allow_now and value.lower() == "now":
        return _to_iso_z(datetime.now(timezone.utc)), []
    try:
        parsed = _parse_timestamp(value)
    except Exception:
        return None, [_invalid(path, "Invalid timestamp format.", expected="ISO8601", received=raw)]
    return _to_iso_z(parsed), []


def _resolve_settings(parsed: ContractRequest) -> Settings:
    settings = parsed.request.settings
    return Settings(
        house_system=settings.house_system or "placidus",
        zodiac=settings.zodiac or "tropical",
        coordinate_system="ecliptic",
    )


def _resolve_datetime_utc(
    birth: PlayerBirth,
    timezone_name: str | None,
    *,
    date_path: str,
    time_path: str,
    timezone_path: str,
    require_time: bool,
) -> tuple[str | None, list[dict[str, Any]]]:
    date_raw = (birth.date or "").strip()
    time_raw = (birth.time or "").strip()
    invalid: list[dict[str, Any]] = []
    if not date_raw:
        invalid.append(_invalid(date_path, "Birth date is required.", expected="YYYY-MM-DD", received=birth.date))
    if require_time and not time_raw:
        invalid.append(_invalid(time_path, "Birth time is required.", expected="HH:MM", received=birth.time))
    if invalid:
        return None, invalid
    if not time_raw:
        time_raw = "12:00"
    try:
        local_dt = datetime.strptime(f"{date_raw} {time_raw}", "%Y-%m-%d %H:%M")
    except Exception:
        return None, [_invalid(f"{date_path}|{time_path}", "Invalid date/time format.", expected="YYYY-MM-DD and HH:MM", received=f"{date_raw} {time_raw}")]

    zone_name = (timezone_name or "UTC").strip() or "UTC"
    try:
        tz = ZoneInfo(zone_name)
    except Exception:
        return None, [_invalid(timezone_path, "Unknown timezone.", expected="IANA timezone", received=timezone_name)]
    return _to_iso_z(local_dt.replace(tzinfo=tz).astimezone(timezone.utc)), []


def _resolve_location(
    parameters: dict[str, Any],
    birth_place: str | None,
    *,
    path_prefix: str,
    require_location: bool,
    allow_geoip: bool,
) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
    location = parameters.get("location")
    lat = None
    lon = None
    alt_m = 0.0
    place = birth_place

    if isinstance(location, dict):
        lat = location.get("lat")
        lon = location.get("lon")
        if "alt_m" in location:
            try:
                alt_m = float(location.get("alt_m", 0.0))
            except Exception:
                return None, [_invalid(f"{path_prefix}.location.alt_m", "Invalid altitude.", expected="number", received=location.get("alt_m"))]
        if location.get("place"):
            place = str(location["place"])
    else:
        lat = parameters.get("lat")
        lon = parameters.get("lon")
        if "alt_m" in parameters:
            try:
                alt_m = float(parameters.get("alt_m", 0.0))
            except Exception:
                return None, [_invalid(f"{path_prefix}.alt_m", "Invalid altitude.", expected="number", received=parameters.get("alt_m"))]

    if lat is not None and lon is not None:
        try:
            return {
                "lat": float(lat),
                "lon": float(lon),
                "alt_m": float(alt_m),
                "place": place,
            }, []
        except Exception:
            return None, [_invalid(f"{path_prefix}.location", "Invalid location coordinates.", expected="numeric lat/lon/alt_m", received={"lat": lat, "lon": lon, "alt_m": alt_m})]

    if birth_place:
        try:
            geo = geocode_place(birth_place)
            return {"lat": geo.lat, "lon": geo.lon, "alt_m": geo.alt_m, "place": geo.place or birth_place}, []
        except ValueError as exc:
            return None, [_invalid(f"{path_prefix}.location", f"Failed to geocode place: {exc}", expected="Resolvable place or explicit lat/lon", received=birth_place)]

    if allow_geoip:
        try:
            geo = geocode_ip("")
            return {"lat": geo.lat, "lon": geo.lon, "alt_m": geo.alt_m, "place": geo.place or "auto"}, []
        except ValueError as exc:
            return None, [_invalid(f"{path_prefix}.location", f"Failed to infer location: {exc}", expected="Resolvable place or explicit lat/lon", received=None)]

    if require_location:
        return None, [_invalid(f"{path_prefix}.location.lat|{path_prefix}.location.lon", "Location is required.", expected="location.lat and location.lon", received={"lat": lat, "lon": lon})]
    return None, []


def _build_natal_chart(
    parsed: ContractRequest,
    birth: PlayerBirth,
    parameters: dict[str, Any],
    *,
    require_time: bool,
    path_prefix: str,
    date_path: str,
    time_path: str,
    timezone_path: str,
) -> tuple[dict[str, Any] | None, str | None, dict[str, Any] | None, list[dict[str, Any]]]:
    dt_utc, dt_invalid = _resolve_datetime_utc(
        birth,
        parsed.metadata.timezone,
        date_path=date_path,
        time_path=time_path,
        timezone_path=timezone_path,
        require_time=require_time,
    )
    if dt_invalid:
        return None, None, None, dt_invalid
    location, loc_invalid = _resolve_location(
        parameters,
        birth.place,
        path_prefix=path_prefix,
        require_location=True,
        allow_geoip=False,
    )
    if loc_invalid:
        return None, None, None, loc_invalid
    try:
        payload = calc_chart(
            chart_type="natal",
            timestamp_utc=dt_utc or "",
            location=location or {},
            settings=_resolve_settings(parsed),
        )
    except Exception as exc:
        raise RuntimeError(f"natal_compute_failed: {exc}") from exc
    return payload, dt_utc, location, []


def _build_moment_chart(
    parsed: ContractRequest,
    parameters: dict[str, Any],
    *,
    at_path: str,
    allow_now: bool,
) -> tuple[dict[str, Any] | None, str | None, dict[str, Any] | None, list[dict[str, Any]]]:
    at_utc, at_invalid = _parse_iso(parameters.get("at"), at_path, allow_now=allow_now)
    if at_invalid:
        return None, None, None, at_invalid
    location, loc_invalid = _resolve_location(
        parameters,
        parsed.player.birth.place,
        path_prefix="request.parameters",
        require_location=True,
        allow_geoip=True,
    )
    if loc_invalid:
        return None, None, None, loc_invalid
    try:
        payload = calc_chart(
            chart_type="moment",
            timestamp_utc=at_utc or "",
            location=location or {},
            settings=_resolve_settings(parsed),
        )
    except Exception as exc:
        raise RuntimeError(f"moment_compute_failed: {exc}") from exc
    return payload, at_utc, location, []


def _cross_aspects(chart_a: dict[str, Any], chart_b: dict[str, Any], prefix_a: str, prefix_b: str) -> list[dict[str, Any]]:
    _, aspect_angles, aspect_orbs, aspect_classes = _default_aspect_config()
    return _calc_cross_aspects(
        _build_aspect_targets(chart_a),
        _build_aspect_targets(chart_b),
        aspect_angles,
        aspect_orbs,
        aspect_classes,
        prefix_a,
        prefix_b,
    )


def _sign_and_degree(lon: float) -> tuple[str, float]:
    signs = [
        "Aries",
        "Taurus",
        "Gemini",
        "Cancer",
        "Leo",
        "Virgo",
        "Libra",
        "Scorpio",
        "Sagittarius",
        "Capricorn",
        "Aquarius",
        "Pisces",
    ]
    normalized = _normalize_deg(lon)
    return signs[int(normalized // 30)], normalized % 30.0


def _shift_angle_payload(payload: dict[str, Any], arc: float) -> dict[str, Any]:
    shifted = dict(payload)
    lon = _normalize_deg(float(payload["lon"]) + arc)
    sign, deg_in_sign = _sign_and_degree(lon)
    shifted["lon"] = lon
    shifted["sign"] = sign
    shifted["deg_in_sign"] = deg_in_sign
    return shifted


def _shift_body_payload(payload: dict[str, Any], arc: float) -> dict[str, Any]:
    shifted = dict(payload)
    lon = _normalize_deg(float(payload["lon"]) + arc)
    sign, deg_in_sign = _sign_and_degree(lon)
    shifted["lon"] = lon
    shifted["sign"] = sign
    shifted["deg_in_sign"] = deg_in_sign
    return shifted


def _build_solar_arc_chart_payload(frame_a_chart: dict[str, Any], frame_b_chart: dict[str, Any], arc: float) -> dict[str, Any]:
    chart = dict(frame_a_chart)
    chart["bodies"] = {name: _shift_body_payload(body, arc) for name, body in frame_a_chart["bodies"].items()}
    chart["asteroids"] = {name: _shift_body_payload(body, arc) for name, body in frame_a_chart.get("asteroids", {}).items()}
    chart["angles"] = {name: _shift_angle_payload(payload, arc) for name, payload in frame_a_chart["angles"].items()}
    houses = dict(frame_a_chart["houses"])
    cusps = houses.get("cusps", {})
    houses["cusps"] = {name: _shift_angle_payload(payload, arc) for name, payload in cusps.items()}
    chart["houses"] = houses
    points = dict(frame_a_chart.get("points", {}))
    for key in ("nn", "sn", "lilith (black moon)"):
        if key in points:
            points[key] = _shift_body_payload(points[key], arc)
    if isinstance(points.get("lots"), dict):
        points["lots"] = {name: _shift_body_payload(payload, arc) for name, payload in points["lots"].items()}
    chart["points"] = points
    _, aspect_angles, aspect_orbs, aspect_classes = _default_aspect_config()
    chart["aspects"] = _calc_aspects(_build_aspect_targets(chart), aspect_angles, aspect_orbs, aspect_classes)
    chart["stars"] = []
    meta = dict(chart.get("meta", {}))
    meta["output_type"] = "solar_arc_chart"
    meta["mode"] = "chart"
    meta["chart_type"] = "solar_arc_chart"
    meta["source_timestamp_utc"] = frame_a_chart["meta"]["timestamp_utc"]
    meta["target_timestamp_utc"] = frame_b_chart["meta"]["timestamp_utc"]
    meta["timestamp_utc"] = frame_b_chart["meta"]["timestamp_utc"]
    meta["solar_arc_deg"] = arc
    chart["meta"] = meta
    return chart


def _safe_int(raw: Any, path: str, *, minimum: int = 1) -> tuple[int | None, list[dict[str, Any]]]:
    try:
        value = int(raw)
    except Exception:
        return None, [_invalid(path, "Value must be integer.", expected=f"int >= {minimum}", received=raw)]
    if value < minimum:
        return None, [_invalid(path, "Value is too small.", expected=f"int >= {minimum}", received=raw)]
    return value, []


def _handle_moment(parsed: ContractRequest) -> tuple[dict[str, Any], int]:
    params = parsed.request.parameters or {}
    chart, at_utc, _, invalid = _build_moment_chart(parsed, params, at_path="request.parameters.at", allow_now=True)
    if invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "moment"}, invalid=invalid, http_status=422)
    return ok_response(intent="moment", summary={"at": at_utc}, data={"moment": {"at": at_utc, "moment_chart": chart}})


def _handle_natal(parsed: ContractRequest) -> tuple[dict[str, Any], int]:
    params = parsed.request.parameters or {}
    chart, dt_utc, _, invalid = _build_natal_chart(
        parsed,
        parsed.player.birth,
        params,
        require_time=False,
        path_prefix="request.parameters",
        date_path="player.birth.date",
        time_path="player.birth.time",
        timezone_path="metadata.timezone",
    )
    if invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "natal"}, invalid=invalid, http_status=422)
    return ok_response(intent="natal", summary={"datetime_utc": dt_utc}, data={"natal": chart})


def _handle_progressed_chart(parsed: ContractRequest) -> tuple[dict[str, Any], int]:
    params = parsed.request.parameters or {}
    at_utc, at_invalid = _parse_iso(params.get("at"), "request.parameters.at", allow_now=False)
    if at_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "progressed_chart"}, invalid=at_invalid, http_status=422)
    natal_chart, natal_utc, _, invalid = _build_natal_chart(
        parsed,
        parsed.player.birth,
        params,
        require_time=False,
        path_prefix="request.parameters",
        date_path="player.birth.date",
        time_path="player.birth.time",
        timezone_path="metadata.timezone",
    )
    if invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "progressed_chart"}, invalid=invalid, http_status=422)
    try:
        natal_dt = _parse_timestamp(natal_utc or "")
        target_dt = _parse_timestamp(at_utc or "")
        delta_years = (target_dt - natal_dt).total_seconds() / (365.25 * 86400.0)
        progressed_ts = _to_iso_z(natal_dt + timedelta(days=delta_years))
        payload = calc_chart(
            chart_type="natal",
            timestamp_utc=progressed_ts,
            location=natal_chart["meta"]["location"],
            settings=_resolve_settings(parsed),
            round_output=False,
        )
    except Exception as exc:
        raise RuntimeError(f"progressed_chart_compute_failed: {exc}") from exc
    meta = dict(payload.get("meta", {}))
    meta["output_type"] = "progressed_chart"
    meta["chart_type"] = "progressed_chart"
    meta["target_timestamp_utc"] = at_utc
    payload["meta"] = meta
    payload = round_payload(payload, 2)
    return ok_response(intent="progressed_chart", summary={"at": at_utc}, data={"progressed_chart": {"at": at_utc, "chart": payload}})


def _handle_solar_arc_chart(parsed: ContractRequest) -> tuple[dict[str, Any], int]:
    params = parsed.request.parameters or {}
    at_utc, at_invalid = _parse_iso(params.get("at"), "request.parameters.at", allow_now=False)
    if at_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "solar_arc_chart"}, invalid=at_invalid, http_status=422)
    natal_chart, _, location, invalid = _build_natal_chart(
        parsed,
        parsed.player.birth,
        params,
        require_time=False,
        path_prefix="request.parameters",
        date_path="player.birth.date",
        time_path="player.birth.time",
        timezone_path="metadata.timezone",
    )
    if invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "solar_arc_chart"}, invalid=invalid, http_status=422)
    try:
        target_chart = calc_chart(
            chart_type="moment",
            timestamp_utc=at_utc or "",
            location=location or {},
            settings=_resolve_settings(parsed),
            round_output=False,
        )
        arc = _normalize_deg(target_chart["bodies"]["sun"]["lon"] - natal_chart["bodies"]["sun"]["lon"])
        payload = round_payload(_build_solar_arc_chart_payload(natal_chart, target_chart, arc), 2)
    except Exception as exc:
        raise RuntimeError(f"solar_arc_chart_compute_failed: {exc}") from exc
    return ok_response(intent="solar_arc_chart", summary={"at": at_utc}, data={"solar_arc_chart": {"at": at_utc, "chart": payload}})


def _handle_astrocartographic(parsed: ContractRequest) -> tuple[dict[str, Any], int]:
    params = parsed.request.parameters or {}
    natal_chart, dt_utc, _, invalid = _build_natal_chart(
        parsed,
        parsed.player.birth,
        params,
        require_time=False,
        path_prefix="request.parameters",
        date_path="player.birth.date",
        time_path="player.birth.time",
        timezone_path="metadata.timezone",
    )
    if invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "astrocartographic"}, invalid=invalid, http_status=422)
    limit_lines, limit_invalid = _safe_int(params.get("limit_lines", 50), "request.parameters.limit_lines", minimum=1)
    if limit_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "astrocartographic"}, invalid=limit_invalid, http_status=422)
    scope = str(params.get("scope", "world")).lower()
    if scope not in {"world", "region"}:
        return error_response(
            error_code="VALIDATION_ERROR",
            summary={"intent": "astrocartographic"},
            invalid=[_invalid("request.parameters.scope", "Invalid scope.", expected="world|region", received=scope)],
            http_status=422,
        )
    try:
        ac = calc_astrocartography(natal_chart, _resolve_settings(parsed).house_system, top_n=limit_lines or 50)
    except Exception as exc:
        raise RuntimeError(f"astrocartography_compute_failed: {exc}") from exc

    lines: list[dict[str, Any]] = []
    for item in ac.get("results", []):
        line_type = f"{item.get('body','')}_{item.get('angle_line','')}".strip("_").lower() or "line"
        lines.append(
            {
                "type": line_type,
                "label": f"{item.get('body', '')} {item.get('angle_line', '')}".strip(),
                "points": [{"lat": float(item.get("lat", 0.0)), "lon": float(item.get("lon", 0.0))}],
                "city": item.get("city"),
                "country": item.get("country"),
            }
        )
    data = {"astrocartographic": {"scope": scope, "lines": lines, "crossings": ac.get("crossings", [])}}
    return ok_response(intent="astrocartographic", summary={"datetime_utc": dt_utc, "line_count": len(lines)}, data=data)


def _handle_transit_to_natal(parsed: ContractRequest) -> tuple[dict[str, Any], int]:
    params = parsed.request.parameters or {}
    overlay = params.get("overlay") if isinstance(params.get("overlay"), dict) else {}
    at_utc, at_invalid = _parse_iso(overlay.get("at"), "request.parameters.overlay.at", allow_now=True)
    if at_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "transit_to_natal"}, invalid=at_invalid, http_status=422)
    natal_chart, _, location, invalid = _build_natal_chart(
        parsed,
        parsed.player.birth,
        params,
        require_time=False,
        path_prefix="request.parameters",
        date_path="player.birth.date",
        time_path="player.birth.time",
        timezone_path="metadata.timezone",
    )
    if invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "transit_to_natal"}, invalid=invalid, http_status=422)
    try:
        transit_chart = calc_chart(
            chart_type="moment",
            timestamp_utc=at_utc or "",
            location=location or {},
            settings=_resolve_settings(parsed),
        )
        aspects = _cross_aspects(natal_chart, transit_chart, "natal_", "tr_")
    except Exception as exc:
        raise RuntimeError(f"transit_to_natal_compute_failed: {exc}") from exc
    data = {
        "transit_to_natal": {
            "at": at_utc,
            "base": {"natal": natal_chart},
            "overlay": {"transit": transit_chart},
            "aspects": aspects,
        }
    }
    return ok_response(intent="transit_to_natal", summary={"at": at_utc}, data=data)


def _handle_progressed_to_natal(parsed: ContractRequest) -> tuple[dict[str, Any], int]:
    params = parsed.request.parameters or {}
    overlay = params.get("overlay") if isinstance(params.get("overlay"), dict) else {}
    at_utc, at_invalid = _parse_iso(overlay.get("at"), "request.parameters.overlay.at", allow_now=False)
    if at_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "progressed_to_natal"}, invalid=at_invalid, http_status=422)
    natal_chart, natal_utc, _, invalid = _build_natal_chart(
        parsed,
        parsed.player.birth,
        params,
        require_time=False,
        path_prefix="request.parameters",
        date_path="player.birth.date",
        time_path="player.birth.time",
        timezone_path="metadata.timezone",
    )
    if invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "progressed_to_natal"}, invalid=invalid, http_status=422)
    try:
        natal_dt = _parse_timestamp(natal_utc or "")
        target_dt = _parse_timestamp(at_utc or "")
        delta_years = (target_dt - natal_dt).total_seconds() / (365.25 * 86400.0)
        progressed_ts = _to_iso_z(natal_dt + timedelta(days=delta_years))
        progressed_chart = calc_chart(
            chart_type="natal",
            timestamp_utc=progressed_ts,
            location=natal_chart["meta"]["location"],
            settings=_resolve_settings(parsed),
            round_output=False,
        )
        progressed_chart = round_payload(progressed_chart, 2)
        aspects = _cross_aspects(progressed_chart, natal_chart, "sp_", "natal_")
    except Exception as exc:
        raise RuntimeError(f"progressed_to_natal_compute_failed: {exc}") from exc
    data = {
        "progressed_to_natal": {
            "at": at_utc,
            "base": {"natal": natal_chart},
            "overlay": {"progressed": progressed_chart},
            "aspects": aspects,
        }
    }
    return ok_response(intent="progressed_to_natal", summary={"at": at_utc}, data=data)


def _handle_solar_arc_to_natal(parsed: ContractRequest) -> tuple[dict[str, Any], int]:
    params = parsed.request.parameters or {}
    overlay = params.get("overlay") if isinstance(params.get("overlay"), dict) else {}
    at_utc, at_invalid = _parse_iso(overlay.get("at"), "request.parameters.overlay.at", allow_now=False)
    if at_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "solar_arc_to_natal"}, invalid=at_invalid, http_status=422)
    natal_chart, _, location, invalid = _build_natal_chart(
        parsed,
        parsed.player.birth,
        params,
        require_time=False,
        path_prefix="request.parameters",
        date_path="player.birth.date",
        time_path="player.birth.time",
        timezone_path="metadata.timezone",
    )
    if invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "solar_arc_to_natal"}, invalid=invalid, http_status=422)
    try:
        target_chart = calc_chart(
            chart_type="moment",
            timestamp_utc=at_utc or "",
            location=location or {},
            settings=_resolve_settings(parsed),
            round_output=False,
        )
        arc = _normalize_deg(target_chart["bodies"]["sun"]["lon"] - natal_chart["bodies"]["sun"]["lon"])
        arc_bodies = {name: {**body, "lon": _normalize_deg(body["lon"] + arc)} for name, body in natal_chart["bodies"].items()}
        _, aspect_angles, aspect_orbs, aspect_classes = _default_aspect_config()
        aspects = _calc_cross_aspects(
            [(name, arc_bodies[name]) for name in arc_bodies.keys()],
            _build_aspect_targets(natal_chart),
            aspect_angles,
            aspect_orbs,
            aspect_classes,
            "sa_",
            "natal_",
        )
    except Exception as exc:
        raise RuntimeError(f"solar_arc_to_natal_compute_failed: {exc}") from exc
    data = {
        "solar_arc_to_natal": {
            "at": at_utc,
            "base": {"natal": natal_chart},
            "overlay": {"solar_arc": {"arc_deg": round(float(arc), 2)}},
            "aspects": aspects,
        }
    }
    return ok_response(intent="solar_arc_to_natal", summary={"at": at_utc}, data=data)


def _handle_synastry(parsed: ContractRequest) -> tuple[dict[str, Any], int]:
    params = parsed.request.parameters or {}
    overlay = params.get("overlay")
    other = overlay.get("other") if isinstance(overlay, dict) else None
    if not isinstance(other, dict):
        return error_response(
            error_code="VALIDATION_ERROR",
            summary={"intent": "synastry"},
            invalid=[_invalid("request.parameters.overlay.other", "Other profile is required.", expected="object", received=other)],
            http_status=422,
        )

    other_birth = other.get("birth")
    if not isinstance(other_birth, dict):
        return error_response(
            error_code="VALIDATION_ERROR",
            summary={"intent": "synastry"},
            invalid=[_invalid("request.parameters.overlay.other.birth", "Birth block is required.", expected="object", received=other_birth)],
            http_status=422,
        )

    base_chart, _, _, base_invalid = _build_natal_chart(
        parsed,
        parsed.player.birth,
        params,
        require_time=False,
        path_prefix="request.parameters",
        date_path="player.birth.date",
        time_path="player.birth.time",
        timezone_path="metadata.timezone",
    )
    if base_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "synastry"}, invalid=base_invalid, http_status=422)

    other_birth_model = PlayerBirth(
        date=other_birth.get("date"),
        time=other_birth.get("time"),
        place=other_birth.get("place"),
        country_code=other_birth.get("country_code"),
    )
    other_dt, other_dt_invalid = _resolve_datetime_utc(
        other_birth_model,
        parsed.metadata.timezone,
        date_path="request.parameters.overlay.other.birth.date",
        time_path="request.parameters.overlay.other.birth.time",
        timezone_path="metadata.timezone",
        require_time=False,
    )
    if other_dt_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "synastry"}, invalid=other_dt_invalid, http_status=422)

    other_params: dict[str, Any] = {}
    if isinstance(other.get("location"), dict):
        other_params["location"] = other["location"]
    other_location, other_loc_invalid = _resolve_location(
        other_params,
        other_birth_model.place,
        path_prefix="request.parameters.overlay.other",
        require_location=True,
        allow_geoip=False,
    )
    if other_loc_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "synastry"}, invalid=other_loc_invalid, http_status=422)

    try:
        other_chart = calc_chart(
            chart_type="natal",
            timestamp_utc=other_dt or "",
            location=other_location or {},
            settings=_resolve_settings(parsed),
        )
        aspects = _cross_aspects(base_chart, other_chart, "base_", "other_")
    except Exception as exc:
        raise RuntimeError(f"synastry_compute_failed: {exc}") from exc

    data = {"synastry": {"base": {"natal": base_chart}, "overlay": {"natal": other_chart}, "aspects": aspects}}
    return ok_response(intent="synastry", data=data)


def _resolve_timeline_range(parameters: dict[str, Any]) -> tuple[str | None, str | None, str | None, list[dict[str, Any]]]:
    time_range = parameters.get("time_range")
    if not isinstance(time_range, dict):
        return None, None, None, [_invalid("request.parameters.time_range", "time_range must be object.", expected="{start,end}", received=time_range)]
    start_utc, start_invalid = _parse_iso(time_range.get("start"), "request.parameters.time_range.start", allow_now=False)
    end_utc, end_invalid = _parse_iso(time_range.get("end"), "request.parameters.time_range.end", allow_now=False)
    invalid = list(start_invalid) + list(end_invalid)
    if invalid:
        return None, None, None, invalid
    try:
        start_dt = _parse_timestamp(start_utc or "")
        end_dt = _parse_timestamp(end_utc or "")
    except Exception:
        return None, None, None, [_invalid("request.parameters.time_range", "Invalid time range.", expected="ISO8601", received=time_range)]
    if end_dt <= start_dt:
        return None, None, None, [_invalid("request.parameters.time_range", "end must be after start.", expected="end > start", received={"start": start_utc, "end": end_utc})]
    step = time_range.get("step")
    return start_utc, end_utc, (str(step).strip() if step is not None else None), []


def _resolve_timeline_bodies(parameters: dict[str, Any], defaults: list[str]) -> list[str]:
    focus = parameters.get("focus")
    if isinstance(focus, str):
        tokens = [item.strip().lower() for item in focus.replace("|", ",").split(",") if item.strip()]
        if tokens:
            values: list[str] = []
            for token in tokens:
                if token == "nodes":
                    values.extend(["nn", "sn"])
                else:
                    values.append(token)
            return list(dict.fromkeys(values))
    return list(defaults)


def _limit_events(events: list[dict[str, Any]], parameters: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    limit_raw = parameters.get("limit_events")
    if limit_raw is None:
        return events, []
    limit, invalid = _safe_int(limit_raw, "request.parameters.limit_events", minimum=1)
    if invalid:
        return events, invalid
    return events[: limit or len(events)], []


def _handle_transit_timeline(parsed: ContractRequest) -> tuple[dict[str, Any], int]:
    params = parsed.request.parameters or {}
    start_utc, end_utc, step, range_invalid = _resolve_timeline_range(params)
    if range_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "transit_timeline"}, invalid=range_invalid, http_status=422)
    natal_chart, _, _, invalid = _build_natal_chart(
        parsed,
        parsed.player.birth,
        params,
        require_time=False,
        path_prefix="request.parameters",
        date_path="player.birth.date",
        time_path="player.birth.time",
        timezone_path="metadata.timezone",
    )
    if invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "transit_timeline"}, invalid=invalid, http_status=422)
    try:
        payload = build_timeline(
            natal_chart=natal_chart,
            start_utc=start_utc or "",
            end_utc=end_utc or "",
            level="custom",
            house_system=_resolve_settings(parsed).house_system,
            bodies=_resolve_timeline_bodies(params, DEFAULT_TRANSIT_TIMELINE_BODIES),
        )
    except Exception as exc:
        raise RuntimeError(f"transit_timeline_compute_failed: {exc}") from exc
    events, limit_invalid = _limit_events(payload.get("events", []), params)
    if limit_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "transit_timeline"}, invalid=limit_invalid, http_status=422)
    data = {"transit_timeline": {"time_range": {"start": start_utc, "end": end_utc, "step": step or "day"}, "events": events}}
    return ok_response(intent="transit_timeline", summary={"start": start_utc, "end": end_utc}, data=data)


def _handle_progressed_timeline(parsed: ContractRequest) -> tuple[dict[str, Any], int]:
    params = parsed.request.parameters or {}
    start_utc, end_utc, step, range_invalid = _resolve_timeline_range(params)
    if range_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "progressed_timeline"}, invalid=range_invalid, http_status=422)
    natal_chart, _, _, invalid = _build_natal_chart(
        parsed,
        parsed.player.birth,
        params,
        require_time=False,
        path_prefix="request.parameters",
        date_path="player.birth.date",
        time_path="player.birth.time",
        timezone_path="metadata.timezone",
    )
    if invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "progressed_timeline"}, invalid=invalid, http_status=422)
    try:
        payload = build_progression_timeline(
            natal_chart=natal_chart,
            start_utc=start_utc or "",
            end_utc=end_utc or "",
        )
    except Exception as exc:
        raise RuntimeError(f"progressed_timeline_compute_failed: {exc}") from exc
    events, limit_invalid = _limit_events(payload.get("events", []), params)
    if limit_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "progressed_timeline"}, invalid=limit_invalid, http_status=422)
    data = {"progressed_timeline": {"time_range": {"start": start_utc, "end": end_utc, "step": step or "month"}, "events": events}}
    return ok_response(intent="progressed_timeline", summary={"start": start_utc, "end": end_utc}, data=data)


def _handle_solar_arc_timeline(parsed: ContractRequest) -> tuple[dict[str, Any], int]:
    params = parsed.request.parameters or {}
    start_utc, end_utc, step, range_invalid = _resolve_timeline_range(params)
    if range_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "solar_arc_timeline"}, invalid=range_invalid, http_status=422)
    natal_chart, _, _, invalid = _build_natal_chart(
        parsed,
        parsed.player.birth,
        params,
        require_time=False,
        path_prefix="request.parameters",
        date_path="player.birth.date",
        time_path="player.birth.time",
        timezone_path="metadata.timezone",
    )
    if invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "solar_arc_timeline"}, invalid=invalid, http_status=422)
    try:
        payload = build_solar_arc_timeline(
            natal_chart=natal_chart,
            start_utc=start_utc or "",
            end_utc=end_utc or "",
            bodies=_resolve_timeline_bodies(params, DEFAULT_SOLAR_ARC_TIMELINE_BODIES),
        )
    except Exception as exc:
        raise RuntimeError(f"solar_arc_timeline_compute_failed: {exc}") from exc
    events, limit_invalid = _limit_events(payload.get("events", []), params)
    if limit_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "solar_arc_timeline"}, invalid=limit_invalid, http_status=422)
    data = {"solar_arc_timeline": {"time_range": {"start": start_utc, "end": end_utc, "step": step or "month"}, "events": events}}
    return ok_response(intent="solar_arc_timeline", summary={"start": start_utc, "end": end_utc}, data=data)


def _parse_hhmm(raw: Any, path: str) -> tuple[datetime | None, list[dict[str, Any]]]:
    if raw is None:
        return None, [_invalid(path, "Time is required.", expected="HH:MM", received=None)]
    value = str(raw).strip()
    try:
        return datetime.strptime(value, "%H:%M"), []
    except Exception:
        return None, [_invalid(path, "Invalid time format.", expected="HH:MM", received=raw)]


def _handle_rectification(parsed: ContractRequest) -> tuple[dict[str, Any], int]:
    params = parsed.request.parameters or {}
    time_range = params.get("time_range")
    events = params.get("events")
    invalid: list[dict[str, Any]] = []
    if not isinstance(time_range, dict):
        invalid.append(_invalid("request.parameters.time_range", "time_range must be object.", expected="{start,end,step_minutes}", received=time_range))
    if not isinstance(events, list) or not events:
        invalid.append(_invalid("request.parameters.events", "events must be non-empty list.", expected="[{type,date,confidence}]", received=events))
    if invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "rectification"}, invalid=invalid, http_status=422)

    start_hhmm, start_invalid = _parse_hhmm(time_range.get("start"), "request.parameters.time_range.start")
    end_hhmm, end_invalid = _parse_hhmm(time_range.get("end"), "request.parameters.time_range.end")
    step_minutes, step_invalid = _safe_int(time_range.get("step_minutes"), "request.parameters.time_range.step_minutes", minimum=1)
    invalid.extend(start_invalid)
    invalid.extend(end_invalid)
    invalid.extend(step_invalid)
    if invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "rectification"}, invalid=invalid, http_status=422)

    start_min = (start_hhmm or datetime(2000, 1, 1, 0, 0)).hour * 60 + (start_hhmm or datetime(2000, 1, 1, 0, 0)).minute
    end_min = (end_hhmm or datetime(2000, 1, 1, 0, 0)).hour * 60 + (end_hhmm or datetime(2000, 1, 1, 0, 0)).minute
    if end_min < start_min:
        return error_response(
            error_code="VALIDATION_ERROR",
            summary={"intent": "rectification"},
            invalid=[_invalid("request.parameters.time_range", "end must be >= start", expected="HH:MM range", received={"start": time_range.get("start"), "end": time_range.get("end")})],
            http_status=422,
        )

    ref_min = start_min + int((end_min - start_min) / 2)
    if parsed.player.birth.time:
        try:
            ref = datetime.strptime(parsed.player.birth.time, "%H:%M")
            ref_min = ref.hour * 60 + ref.minute
        except Exception:
            pass

    filters = params.get("filters") if isinstance(params.get("filters"), dict) else {}
    max_candidates, max_invalid = _safe_int(filters.get("max_candidates", 5), "request.parameters.filters.max_candidates", minimum=1)
    if max_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "rectification"}, invalid=max_invalid, http_status=422)

    method = "major_transits"
    methods = params.get("methods")
    if isinstance(methods, dict):
        for key, enabled in methods.items():
            if bool(enabled):
                method = str(key)
                break

    candidates: list[dict[str, Any]] = []
    minute = start_min
    step = step_minutes or 5
    while minute <= end_min:
        hh = int(minute / 60)
        mm = int(minute % 60)
        value = f"{hh:02d}:{mm:02d}"
        distance = abs(minute - ref_min)
        score = round(max(0.0, 10.0 - distance / 30.0) + len(events) * 0.5, 2)
        hits = [
            {
                "event_index": idx,
                "method": method,
                "description": f"Heuristic match for event '{event.get('type', 'event')}'.",
                "orb_deg": round(distance / 60.0, 2),
            }
            for idx, event in enumerate(events)
        ]
        candidates.append({"time": value, "score": score, "hits": hits})
        minute += step
    candidates.sort(key=lambda item: item["score"], reverse=True)
    candidates = candidates[: (max_candidates or len(candidates))]
    best = candidates[0] if candidates else None
    data = {
        "rectification": {
            "time_range": {"start": time_range.get("start"), "end": time_range.get("end"), "step_minutes": step},
            "events_used": events,
            "candidates": candidates,
        }
    }
    summary = {
        "candidate_count": len(candidates),
        "best_candidate_time": best.get("time") if best else None,
        "best_candidate_score": best.get("score") if best else None,
    }
    return ok_response(intent="rectification", summary=summary, data=data)


def _season_range(start_dt: datetime, end_dt: datetime, index: int, total_parts: int) -> tuple[datetime, datetime]:
    total_seconds = (end_dt - start_dt).total_seconds()
    part_start = start_dt + timedelta(seconds=(index - 1) * total_seconds / total_parts)
    part_end = start_dt + timedelta(seconds=index * total_seconds / total_parts)
    return part_start, part_end


def _handle_node_axis_timeline(parsed: ContractRequest) -> tuple[dict[str, Any], int]:
    params = parsed.request.parameters or {}
    start_utc, end_utc, step, range_invalid = _resolve_timeline_range(params)
    if range_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "node_axis_timeline"}, invalid=range_invalid, http_status=422)
    natal_chart, _, _, invalid = _build_natal_chart(
        parsed,
        parsed.player.birth,
        params,
        require_time=False,
        path_prefix="request.parameters",
        date_path="player.birth.date",
        time_path="player.birth.time",
        timezone_path="metadata.timezone",
    )
    if invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "node_axis_timeline"}, invalid=invalid, http_status=422)

    try:
        payload = build_timeline(
            natal_chart=natal_chart,
            start_utc=start_utc or "",
            end_utc=end_utc or "",
            level="custom",
            house_system=_resolve_settings(parsed).house_system,
            bodies=["nn", "sn"],
        )
    except Exception as exc:
        raise RuntimeError(f"node_axis_timeline_compute_failed: {exc}") from exc

    events, limit_invalid = _limit_events(payload.get("events", []), params)
    if limit_invalid:
        return error_response(error_code="VALIDATION_ERROR", summary={"intent": "node_axis_timeline"}, invalid=limit_invalid, http_status=422)

    start_dt = _parse_timestamp(start_utc or "")
    end_dt = _parse_timestamp(end_utc or "")
    parsed_events: list[tuple[datetime, dict[str, Any]]] = []
    for item in events:
        try:
            parsed_events.append((_parse_timestamp(item.get("transit_start", "")), item))
        except Exception:
            continue

    seasons: list[dict[str, Any]] = []
    previous_signs: tuple[str | None, str | None] = (None, None)
    for season_idx in range(1, 6):
        season_start, season_end = _season_range(start_dt, end_dt, season_idx, 5)
        chapters: list[dict[str, Any]] = []
        for chapter_idx in range(1, 13):
            absolute_idx = (season_idx - 1) * 12 + chapter_idx
            chapter_start, chapter_end = _season_range(start_dt, end_dt, absolute_idx, 60)
            chapter_start_iso = _to_iso_z(chapter_start)
            chapter_end_iso = _to_iso_z(chapter_end)
            try:
                chapter_chart = calc_chart(
                    chart_type="moment",
                    timestamp_utc=chapter_start_iso,
                    location=natal_chart["meta"]["location"],
                    settings=_resolve_settings(parsed),
                )
            except Exception as exc:
                raise RuntimeError(f"node_axis_chapter_compute_failed: {exc}") from exc
            nn_sign = chapter_chart["points"]["nn"]["sign"]
            sn_sign = chapter_chart["points"]["sn"]["sign"]
            sign_changed = previous_signs != (nn_sign, sn_sign)
            previous_signs = (nn_sign, sn_sign)
            chapter_events = [event for event_dt, event in parsed_events if chapter_start <= event_dt < chapter_end]
            chapters.append(
                {
                    "chapter_index": chapter_idx,
                    "slice_deg": chapter_idx * 30,
                    "chapter_start": chapter_start_iso,
                    "chapter_end": chapter_end_iso,
                    "node_axis_signs": {"north_node": nn_sign, "south_node": sn_sign},
                    "markers": {"slice_changed": absolute_idx > 1, "sign_changed": sign_changed},
                    "chapter_theme": f"Season {season_idx}, Chapter {chapter_idx}",
                    "events": chapter_events,
                }
            )
        seasons.append(
            {
                "season_index": season_idx,
                "season_start": _to_iso_z(season_start),
                "season_end": _to_iso_z(season_end),
                "chapters": chapters,
            }
        )

    data = {
        "node_axis_timeline": {
            "time_range": {"start": start_utc, "end": end_utc, "step": step or "month"},
            "seasons": seasons,
        }
    }
    return ok_response(intent="node_axis_timeline", summary={"start": start_utc, "end": end_utc}, data=data)


HANDLERS: dict[str, HandlerFn] = {
    "moment": _handle_moment,
    "natal": _handle_natal,
    "progressed_chart": _handle_progressed_chart,
    "solar_arc_chart": _handle_solar_arc_chart,
    "astrocartographic": _handle_astrocartographic,
    "transit_to_natal": _handle_transit_to_natal,
    "progressed_to_natal": _handle_progressed_to_natal,
    "solar_arc_to_natal": _handle_solar_arc_to_natal,
    "synastry": _handle_synastry,
    "transit_timeline": _handle_transit_timeline,
    "progressed_timeline": _handle_progressed_timeline,
    "solar_arc_timeline": _handle_solar_arc_timeline,
    "rectification": _handle_rectification,
    "node_axis_timeline": _handle_node_axis_timeline,
}
