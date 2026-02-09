from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any


def _contract_path() -> Path:
    # .../SPIN/styx-api/app/contract_v1/ -> .../SPIN/docs/contract.json
    return Path(__file__).resolve().parents[3] / "docs" / "contract.json"


@lru_cache(maxsize=1)
def load_contract() -> dict[str, Any]:
    path = _contract_path()
    if not path.exists():
        raise RuntimeError(f"Contract file missing: {path}")
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def styx_version() -> str:
    value = load_contract().get("styx_version")
    if isinstance(value, str) and value:
        return value
    return "unknown"

