# A_Design

## OVERVIEW (Living)
- intent: Ship STYX API v3.0.0 with deterministic astrology computation and stable response contracts.
- scope: Keep both interfaces aligned:
  - Universal contract endpoint: `POST /v1/contract`
  - Envelope endpoints: `GET /v1/health`, `GET /v1/config`, `POST /v1/chart`, `POST /v1/transit`, `POST /v1/timeline`
- constraints: Swiss Ephemeris as compute source, deterministic ordering, stable field names, no breaking intent renames.
- success_definition: A restart from `SEED/ + SPEC/` can rebuild an API that returns the same contract/envelope shape and `3.0.0` version semantics.
- key_decisions:
  - Contract-first public behavior via `/v1/contract`.
  - Keep envelope endpoints for direct compute workflows and diagnostics.
  - Centralize runtime version in one source (`STYX_VERSION`) used by contract and envelope metadata.

## A1 - Features (Living)
- feature_list:
  - `POST /v1/contract` universal endpoint.
  - Contract statuses: `contract | ok | error`.
  - Contract response metadata invariant: `metadata.styx_version == "3.0.0"` for success and error responses.
  - `GET /v1/health` returns envelope with `meta.api_version == "3.0.0"`.
  - `GET /v1/config` returns defaults/catalogs/orbs/provenance.
  - `POST /v1/chart` supports: `natal | moment | solar_arc | secondary_progression`.
  - `POST /v1/transit` supports: `transit | synastry | astrocartography | solar_arc | secondary_progression | lunations`.
  - `POST /v1/timeline` supports: `transit | secondary_progression | solar_arc` timelines with lunations/eclipses tokens and node-axis logic.
- contract_intents:
  - CHART: `moment`, `natal`, `progressed_chart`, `solar_arc_chart`, `astrocartographic`
  - TRANSIT: `transit_to_natal`, `progressed_to_natal`, `solar_arc_to_natal`, `synastry`
  - TIMELINE: `transit_timeline`, `progressed_timeline`, `solar_arc_timeline`, `rectification`, `node_axis_timeline`
  - SYSTEM: `contract` (schema/intent map payload)

## A2 - Architecture (Living)
- boundaries:
  - API layer: FastAPI routes + request validation.
  - Contract layer: `app/contract_v1` dispatcher, handlers, and response builders.
  - Compute layer: chart/aspect/timeline/astrocartography services.
  - Envelope layer: shared response meta/settings/timing/errors.
- components:
  - `app/main.py`: envelope endpoints + router wiring.
  - `app/contract_v1/router.py`: `/v1/contract` endpoint.
  - `app/contract_v1/dispatcher.py`: intent dispatch and validation routing.
  - `app/contract_v1/intent_handlers.py`: intent implementations.
  - `app/contract_v1/responses.py`: universal contract response envelope.
  - `app/core/version.py`: `STYX_VERSION` resolution and API version source.
  - `SPIN/docs/contract.json`: contract schema, glossary, intents, response payload templates.
- data_flows:
  - contract flow: request -> parse/validate -> intent dispatch -> compute -> `ContractResponse`
  - envelope flow: request -> validate -> compute -> `envelope_response()`

## A3 - Interaction (Living)
- interaction_rules:
  - `/v1/contract` request body uses `metadata/player/request` form from `SPIN/docs/contract.json`.
  - Unknown/invalid contract input returns status `error` with structured `response.data.error`.
  - Error responses must still include `metadata.styx_version = "3.0.0"`.
  - Envelope endpoints return `{meta, settings, input_summary, data, timing, errors}`.
- versioning_rules:
  - Runtime version source order:
    1. local `pyproject.toml` version
    2. installed package metadata
    3. `STYX_VERSION` env var
    4. fallback `"3.0.0"`
  - Current target and default: `3.0.0`.
- error_handling:
  - Contract validation/runtime failures map to deterministic contract `error` shape.
  - Envelope validation failures return HTTP 422; unhandled failures return HTTP 500 with stable error payload.
