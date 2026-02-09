from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any


def _candidate_contract_paths() -> list[Path]:
    # Primary repo-relative path:
    # .../SPIN/styx-api/app/contract_v1/ -> .../SPIN/docs/contract.json
    module_relative = Path(__file__).resolve().parents[3] / "docs" / "contract.json"
    cwd_relative = Path.cwd() / "SPIN" / "docs" / "contract.json"
    return [module_relative, cwd_relative]


@lru_cache(maxsize=1)
def load_contract() -> dict[str, Any]:
    candidates = _candidate_contract_paths()
    for path in candidates:
        if path.exists():
            with path.open("r", encoding="utf-8") as fh:
                return json.load(fh)
    checked = ", ".join(str(path) for path in candidates)
    raise RuntimeError(f"Contract file missing. Checked: {checked}")


def styx_version() -> str:
    value = load_contract().get("styx_version")
    if isinstance(value, str) and value:
        return value
    return "unknown"
