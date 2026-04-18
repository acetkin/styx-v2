# STYX Repository Analysis Handover

## Overview

STYX is a Python 3.11+ FastAPI service that exposes a deterministic astrology computation API backed by Swiss Ephemeris. The repository is not organized like a typical application monorepo: the executable service lives under `SPIN/styx-api`, while `SEED/` and `SPEC/` describe the intended product contract, restart/rebuild goals, and release governance.

The public design intent is contract-first. `POST /v1/contract` is positioned as the universal external interface, while the older envelope-style endpoints remain available for direct compute and diagnostics. Current target versioning is consistently documented as `3.0.0`.

## Structure

### Top-level layout

- `.github/workflows/ci.yml`: placeholder CI workflow.
- `SEED/`: product seed and reconstruction goals.
- `SPEC/`: living design, development, and distribution documents.
- `SPIN/docs/`: contract artifact and operating docs.
- `SPIN/styx-api/`: actual FastAPI application, tests, scripts, data, and ephemeris files.
- `handover/`: existing handover/output area in the source repo.

### Service layout under `SPIN/styx-api`

- `app/main.py`: FastAPI app creation and legacy envelope endpoints.
- `app/contract_v1/`: contract-first endpoint, models, dispatcher, handlers, and response builders.
- `app/core/`: envelope schema, middleware, exception handling, version resolution.
- `app/services/`: astrology computation, geocoding, timelines, lunations.
- `data/`: cities, country info, and lunation CSV.
- `ephe/`: bundled Swiss Ephemeris data files.
- `tests/`: API, contract, smoke, and fixture coverage.
- `scripts/`: smoke and measurement helpers.

## Tech Stack

- Language: Python 3.11+
- Web framework: FastAPI
- ASGI server: Uvicorn
- Validation/modeling: Pydantic v2
- Core compute: `pyswisseph`
- Geocoding: `geopy` with Nominatim
- Timezone lookup: `timezonefinder`, `tzdata`, stdlib `zoneinfo`
- Test stack: `pytest`, `httpx`, FastAPI `TestClient`
- Packaging: `pyproject.toml` with setuptools editable install

## Architecture

### High-level layers

1. `app/main.py` handles envelope endpoints and wires middleware, exception handling, and the contract router.
2. `app/contract_v1/` implements the universal request/response flow:
   - `router.py` exposes `POST /v1/contract`
   - `dispatcher.py` loads `SPIN/docs/contract.json`, validates required paths, and routes by intent
   - `intent_handlers.py` maps contract intents to compute functions
   - `responses.py` returns the contract response envelope
3. `app/core/` standardizes request IDs, timing, version metadata, and error envelopes.
4. `app/services/` performs chart, transit, timeline, lunation, astrocartography, and geocoding work.

### Response model split

- Contract endpoint responses use:
  - `status`
  - `metadata.styx_version`
  - `response.summary`
  - `response.data`
- Legacy endpoints use the envelope model from `app/core/envelope.py`:
  - `meta`
  - `settings`
  - `input_summary`
  - `data`
  - `timing`
  - `errors`

### Version handling

`app/core/version.py` centralizes version resolution:

1. Local `pyproject.toml`
2. Installed package metadata
3. `STYX_VERSION` environment variable
4. Fallback `3.0.0`

This version is reused for both `metadata.styx_version` in contract responses and `meta.api_version` in envelope responses.

## Entry Points

### Runtime entry point

- `uvicorn app.main:app`

### Application setup

`app/main.py`:

- creates the FastAPI app
- installs request ID and timing middleware
- registers validation, HTTP, and unhandled exception handlers
- mounts the contract router

### Operational entry points

- `SPIN/styx-api/README.md`: basic install/run/test commands
- `SPIN/styx-api/RUNBOOK.md`: local runbook and sample request
- `SPIN/styx-api/scripts/smoke_run_api.py`: local smoke script that calls key endpoints and writes samples
- `SPIN/styx-api/scripts/measure_endpoints.py`: endpoint measurement helper
- `SPIN/styx-api/scripts/export_all_features.py`
- `SPIN/styx-api/scripts/generate_transit_timelines.py`

## API Endpoints

### Envelope endpoints

- `GET /v1/health`
  - returns envelope with `data.status = ok`
- `GET /v1/config`
  - returns defaults, catalogs, aspect settings, transit orbs, and provenance
- `POST /v1/chart`
  - supports `natal`, `moment`, `solar_arc`, `secondary_progression`
- `POST /v1/transit`
  - supports `transit`, `synastry`, `astrocartography`, `solar_arc`, `secondary_progression`, `lunations`
- `POST /v1/timeline`
  - supports `transit`, `secondary_progression`, `solar_arc`
  - also special-cases lunation-style body tokens

### Contract endpoint

- `POST /v1/contract`
  - universal request format: `metadata`, `player`, `request`
  - supported intents from `SPIN/docs/contract.json`:
    - `contract`
    - `moment`
    - `natal`
    - `progressed_chart`
    - `solar_arc_chart`
    - `astrocartographic`
    - `transit_to_natal`
    - `progressed_to_natal`
    - `solar_arc_to_natal`
    - `synastry`
    - `transit_timeline`
    - `progressed_timeline`
    - `solar_arc_timeline`
    - `rectification`
    - `node_axis_timeline`

### Endpoint behavior notes

- Contract responses are explicit and intent-oriented.
- Envelope endpoints expose lower-level compute behavior and settings.
- `/v1/contract` validates required dotted paths from `SPIN/docs/contract.json` before handler dispatch.
- Error handling differs by interface:
  - contract returns `status=error` with contract-specific error payloads
  - envelope endpoints return HTTP errors plus stable `errors[]` entries

## Config/Dependencies

### Python dependencies

Declared in `SPIN/styx-api/pyproject.toml`:

- `fastapi`
- `uvicorn`
- `pydantic`
- `geopy`
- `pyswisseph`
- `timezonefinder`
- `tzdata`

Dev extras:

- `pytest`
- `httpx`

### Environment variables in use

- `SE_EPHE_PATH`
- `STYX_VERSION`
- `STYX_GEOCODE_STUB`
- `STYX_GEOCODE_USER_AGENT`
- `STYX_GEOCODE_TIMEOUT`
- `STYX_GEOCODE_DOMAIN`
- `STYX_GEOCODE_COUNTRY_CODES`
- `STYX_GEOCODE_LANGUAGE`
- `STYX_GEOIP_STUB`
- `STYX_GEOIP_URL`
- `STYX_GEOIP_TIMEOUT`
- `STYX_CITIES_PATH`
- `STYX_COUNTRIES_PATH`
- `STYX_ASTRO_MAX_ORB`
- `STYX_ASTRO_CROSS_TOP_N`

### Data/config artifacts

- `SPIN/docs/contract.json`: source-of-truth contract artifact
- `SPIN/styx-api/data/cities5000.txt`: astrocartography city dataset
- `SPIN/styx-api/data/countryInfo.txt`: country mapping dataset
- `SPIN/styx-api/data/lunations_100y.csv`: lunation/timeline data
- `SPIN/styx-api/ephe/*`: Swiss Ephemeris runtime data

## Deployment/Runtime

### What is present

- Local run instructions for editable install + `uvicorn`
- Local Swagger/OpenAPI access through FastAPI
- A documented runbook
- Bundled ephemeris and data files inside the repo
- A release playbook under `SPIN/docs/release-playbook-v2.md`

### What is not present

- No Dockerfile
- No container orchestration manifests
- No Terraform or infrastructure code
- No production process manager config
- No meaningful CI build/test pipeline yet

### CI/CD state

`.github/workflows/ci.yml` only checks out the repo and runs `echo "ci ok"`. This means the repository currently has almost no automated protection around installability, tests, contract drift, or runtime health.

### Branch/release context

- `SEED/` and `SPEC/` frame STYX as stable `v3.0.0`
- `SPIN/docs/release-playbook-v2.md` is explicitly a hotfix flow for `release/v2`

That suggests the documented release operational flow is at least partially legacy relative to the current v3 codebase.

## Tests

### Test inventory

- `tests/test_api.py`
  - envelope endpoint behavior
  - schema assertions
  - config assertions
  - validation behavior
- `tests/test_contract_v1.py`
  - contract OpenAPI schema presence
  - happy-path fixtures for each intent
  - unsupported-intent handling
  - required-path validation
  - internal error envelope behavior
  - version invariants
- `tests/test_smoke.py`
  - basic smoke checks for health/config/chart and unknown field handling

### Fixtures

- Contract fixtures live under `tests/fixtures/contract_v1/`
- Geocode/country test fixtures live under `tests/fixtures/`

### Observed status from repository docs

`SPIN/styx-api/STATUS.md` reports on 2026-02-09:

- `pytest: 64 passed`
- `fixture_smoke_suite: 1 passed`

### Verification performed for this handover

I did not execute the test suite during this handover analysis. The repository contains tests that may write local log artifacts, and the request constrained modifications to the handover repository only.

## Environment Expectations

### Required runtime assumptions

- Python 3.11+
- Swiss Ephemeris available through bundled `ephe/` files or `SE_EPHE_PATH`
- Network access if using live Nominatim geocoding or GeoIP lookup
- Writable local environment for normal development workflows

### Runtime behavior expectations

- If ephemeris files are missing, core compute paths fail early
- If geocoding is not stubbed, place lookup depends on external Nominatim availability
- If GeoIP is used, location inference depends on an external HTTP service
- Tests commonly stub both geocoding and GeoIP to remain deterministic

### Repository expectations

- The app is expected to be reconstructible from `SEED/ + SPEC/`
- `SPIN/docs/contract.json` is treated as the contract source of truth
- The working service root is `SPIN/styx-api`, not the repo root

## Risks

### Operational risks

- CI is effectively non-existent, so regressions can merge without install or test execution.
- There is no production deployment definition in the repo.
- Release documentation is partly centered on `v2`, while the codebase is `v3.0.0`.

### Runtime dependency risks

- Core functionality depends on Swiss Ephemeris files being present and readable.
- Live geocoding and GeoIP introduce external-network fragility, rate limiting, and nondeterminism if stubs are not used.
- Large bundled data files increase repo/runtime coupling.

### Code/design risks

- `app/main.py` is very large and mixes routing, validation, orchestration, and business logic.
- Contract and envelope interfaces implement overlapping capabilities through separate code paths, increasing maintenance cost and drift risk.
- A number of behaviors are heuristic rather than deeply domain-modeled, especially `rectification`.

## Gaps

### Documentation gaps

- No root README for repository orientation.
- No explicit architecture diagram.
- No deployment architecture or infrastructure documentation for v3.
- No compatibility/deprecation policy document yet, although `SPEC/B_Develop.md` lists it as pending.

### Engineering gaps

- No real CI test gate.
- No packaging/release automation.
- No obvious linting, formatting, or static type checking configuration.
- No auth, rate limiting, or multi-tenant concerns visible in the current API.

### Handover-relevant ambiguity

- The repo contains both governance docs and runnable code, so new contributors may not immediately know that `SPIN/styx-api` is the real service root.
- Contract-first is the stated external strategy, but legacy envelope endpoints remain extensive and heavily featured.

## Recommended Next Steps

1. Add a root README that explains repository purpose, where the runnable service lives, and which interface is the primary public API.
2. Replace the placeholder GitHub Action with at least editable install plus `pytest -q tests/test_contract_v1.py tests/test_smoke.py`.
3. Split `app/main.py` into smaller route modules or service orchestrators to reduce routing/business-logic coupling.
4. Decide whether envelope endpoints are internal-only, partner-facing, or permanent public surface, then document that explicitly.
5. Produce a v3 deployment document or manifests; the current repo does not show how production is actually run.
6. Add a compatibility/deprecation policy document to match the pending item in `SPEC/B_Develop.md`.
7. Audit contract and envelope feature parity regularly, because both surfaces currently evolve in parallel.
8. Document all required environment variables and default behaviors in one place, ideally in `SPIN/styx-api/README.md` and the root README.

## Source Pointers

- Runtime: `SPIN/styx-api/app/main.py`
- Contract layer: `SPIN/styx-api/app/contract_v1/`
- Shared envelope/versioning: `SPIN/styx-api/app/core/`
- Compute services: `SPIN/styx-api/app/services/`
- Contract artifact: `SPIN/docs/contract.json`
- Local operations: `SPIN/styx-api/README.md`, `SPIN/styx-api/RUNBOOK.md`
- Governance: `SEED/STYX.md`, `SPEC/A_Design.md`, `SPEC/B_Develop.md`, `SPEC/C_Distribute.md`
