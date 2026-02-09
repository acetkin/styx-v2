# STYX API Local Runbook

## Prerequisites
- Python 3.11+ (`pyproject.toml` requires `>=3.11`)
- Git

## 1) Create and activate a virtual environment
From `SPIN/styx-api`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

## 2) Install dependencies
This project is pyproject-based. Install dependencies with:

```powershell
python -m pip install -e ".[dev]"
```

If your environment uses requirements files, the equivalent pattern is:

```powershell
python -m pip install -r requirements.txt
```

## 3) Run the API locally
From `SPIN/styx-api`:

```powershell
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

## 4) Open local API docs
- Swagger UI: `http://127.0.0.1:8000/docs`
- OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`

## 5) Run tests
From `SPIN/styx-api`:

```powershell
python -m pytest -q
```

## 6) Run contract fixture smoke
From `SPIN/styx-api`:

```powershell
python -m pytest -q tests/test_contract_v1.py -k fixture_smoke_suite
```

## 7) Minimal working request example (`natal`)
Example request body:

```json
{
  "metadata": {
    "styx_version": "string",
    "request_id": "req-1",
    "intent": "natal",
    "timezone": "Europe/Istanbul"
  },
  "player": {
    "identity": { "id": "p1", "name": "Test" },
    "birth": {
      "date": "1982-05-08",
      "time": "06:39",
      "place": "Karadeniz Eregli",
      "country_code": "TR"
    },
    "facts": {}
  },
  "request": {
    "settings": { "house_system": "placidus", "zodiac": "tropical" },
    "parameters": {
      "location": { "lat": 41.2795516, "lon": 31.4229672, "alt_m": 0.0 }
    },
    "output": { "verbosity": "normal", "astrological_objects": ["natal"] }
  }
}
```

Expected response shape keys:
- `status` (`"ok"`)
- `response.summary.intent` (`"natal"`)
- `response.data.natal` (non-null object)

## Contract File Location
- Single source of truth: `SPIN/docs/contract.json`
