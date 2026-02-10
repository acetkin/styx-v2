from importlib.metadata import PackageNotFoundError, version
import os
from pathlib import Path
import tomllib

SCHEMA_VERSION = "1.0"
DEFAULT_STYX_VERSION = "3.0.0"
ENGINE_VERSION = "0.1.0"
EPHEMERIS_PROVIDER = "swisseph"


def _read_pyproject_version() -> str | None:
    pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
    if not pyproject_path.exists():
        return None
    try:
        payload = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))
    except Exception:
        return None
    project = payload.get("project")
    if not isinstance(project, dict):
        return None
    value = project.get("version")
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def _resolve_styx_version() -> str:
    pyproject_version = _read_pyproject_version()
    if pyproject_version:
        return pyproject_version
    try:
        return version("styx-api")
    except PackageNotFoundError:
        pass
    except Exception:
        pass
    env_version = os.getenv("STYX_VERSION")
    if env_version:
        return env_version
    return DEFAULT_STYX_VERSION


STYX_VERSION = _resolve_styx_version()
API_VERSION = STYX_VERSION
