# Contract-First Rebuild Report

## Architecture
- Added a new isolated module: `SPIN/styx-api/app/contract_v1/`.
- Legacy endpoints were not modified in behavior; only one new route was added.
- New universal endpoint: `POST /v1/contract`.
- Flow:
  - Raw JSON parse and top-level shape checks (`metadata`, `player`, `request`).
  - Pydantic validation using contract-first request models.
  - Intent dispatch against `SPIN/docs/contract.json`.
  - Contract envelope response for success/error.

## File Tree (new/changed)
- `SPIN/docs/contract.json` (source-of-truth contract file in this branch)
- `SPIN/docs/contract-first-rebuild-report.md`
- `SPIN/styx-api/app/main.py` (router include only)
- `SPIN/styx-api/app/contract_v1/__init__.py`
- `SPIN/styx-api/app/contract_v1/contract_store.py`
- `SPIN/styx-api/app/contract_v1/models.py`
- `SPIN/styx-api/app/contract_v1/responses.py`
- `SPIN/styx-api/app/contract_v1/dispatcher.py`
- `SPIN/styx-api/app/contract_v1/router.py`
- `SPIN/styx-api/tests/test_contract_v1.py`

## How To Run Tests
From `SPIN/styx-api`:

```bash
python -m pytest -q tests/test_contract_v1.py
python -m pytest --collect-only -q
```

Observed output:

```text
....                                                                     [100%]
tests/test_api.py: 16
tests/test_contract_v1.py: 4
tests/test_smoke.py: 2
```

## How To Call The Endpoint

```bash
curl -X POST http://127.0.0.1:8000/v1/contract \
  -H "Content-Type: application/json" \
  -d '{
    "metadata": {
      "styx_version": "string",
      "request_id": "req-1",
      "intent": "contract"
    },
    "player": {
      "identity": { "id": "p1", "name": "Test" },
      "birth": {},
      "facts": {}
    },
    "request": {
      "settings": { "house_system": "placidus", "zodiac": "tropical" },
      "parameters": {},
      "output": { "verbosity": "normal", "astrological_objects": ["natal"] }
    }
  }'
```

Expected behavior:
- `intent=contract` returns `status=contract` and `response.data.contract`.
- Unknown intent returns `UNSUPPORTED_INTENT`.
- Missing required top-level blocks returns `INVALID_REQUEST`.
- Missing required intent paths returns `VALIDATION_ERROR`.
