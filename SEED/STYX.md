# Seed
## Project Identity
name: STYX
output_family: Code

## One-Sentence Description
Contract-first deterministic astrology API (v3.0.0) powered by Swiss Ephemeris, with stable metadata/version semantics across all responses.

## Goals
- Keep `/v1/contract` as the universal public interface with deterministic intent routing.
- Preserve existing envelope endpoints for direct compute and diagnostics.
- Guarantee version invariants:
  - contract responses: `metadata.styx_version == "3.0.0"` (ok + error + contract status)
  - envelope responses: `meta.api_version == "3.0.0"`
- Keep tests and fixtures runnable for restart scenarios.

## Non-Goals
- Generating interpretive text or horoscope prose.
- Building frontend/UI or auth/billing systems.
- Breaking contract intent names or response field structure.
- Introducing non-deterministic payload ordering.

## Deliverables
- Universal contract endpoint:
  - `POST /v1/contract`
  - statuses: `contract | ok | error`
  - intent support:
    - CHART: `moment`, `natal`, `progressed_chart`, `solar_arc_chart`, `astrocartographic`
    - TRANSIT: `transit_to_natal`, `progressed_to_natal`, `solar_arc_to_natal`, `synastry`
    - TIMELINE: `transit_timeline`, `progressed_timeline`, `solar_arc_timeline`, `rectification`, `node_axis_timeline`
    - SYSTEM: `contract`
- Envelope endpoints:
  - `GET /v1/health`
  - `GET /v1/config`
  - `POST /v1/chart`
  - `POST /v1/transit`
  - `POST /v1/timeline`
- Versioned contract artifact:
  - `SPIN/docs/contract.json` with top-level `styx_version: "3.0.0"`
- Tests:
  - Contract fixture smoke and focused contract tests
  - Envelope smoke/basic API tests

## Constraints
- Runtime: Python 3.11+ with FastAPI/Uvicorn.
- Swiss Ephemeris is the compute source of truth.
- Determinism required for ordering and stable schema fields.
- Version source must be centralized (single source of truth in code).
- Restart requirement: with only `SEED/ + SPEC/`, Codex must be able to rebuild near-current API behavior and interfaces.

## Acceptance Criteria
- `POST /v1/contract` with valid `natal` payload returns:
  - `status: "ok"`
  - `metadata.styx_version: "3.0.0"`
- `POST /v1/contract` with invalid payload returns:
  - `status: "error"`
  - `metadata.styx_version: "3.0.0"`
- `GET /v1/health` returns envelope with:
  - `meta.api_version: "3.0.0"`
  - `data.status: "ok"`
- Contract fixtures and smoke paths pass with Tier 1 test policy.

## API Surface (Accepted Decisions)
- Primary contract endpoint:
  - `POST /v1/contract` with universal request form (`metadata/player/request`)
- Secondary compute endpoints:
  - `GET /v1/health`
  - `GET /v1/config`
  - `POST /v1/chart` (`natal | moment | solar_arc | secondary_progression`)
  - `POST /v1/transit` (`transit | synastry | astrocartography | solar_arc | secondary_progression | lunations`)
  - `POST /v1/timeline` (`transit | secondary_progression | solar_arc`)
- Contract source files:
  - `SPIN/docs/contract.json`
  - `SPIN/styx-api/app/contract_v1/*`

## Restart Reconstruction Profile
When rebuilding from only `SEED/ + SPEC/`, target this minimum structure:
- `SPIN/styx-api/pyproject.toml` with project version `3.0.0`
- `SPIN/styx-api/app/core/version.py` exporting centralized `STYX_VERSION`
- `SPIN/styx-api/app/contract_v1/`:
  - `router.py`, `dispatcher.py`, `intent_handlers.py`, `models.py`, `responses.py`, `contract_store.py`
- `SPIN/styx-api/app/main.py` exposing:
  - `/v1/health`, `/v1/config`, `/v1/chart`, `/v1/transit`, `/v1/timeline`
  - plus router include for `/v1/contract`
- `SPIN/docs/contract.json` with `styx_version: "3.0.0"` and intent matrix above
- tests covering `metadata.styx_version` and fixture smoke

## Stage & Plan Context (Accepted)
- Stage: S3 (Release / Stable)
- Next: NONE
- Focus:
  - Keep contract/envelope compatibility stable
  - Keep restart reproducibility high from `SEED/ + SPEC/`

## Suggested SPIN Output
deliverable_folder_name: styx-api
