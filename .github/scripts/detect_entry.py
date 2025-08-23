#!/usr/bin/env python3
from pathlib import Path

try:
    import tomllib  # Python 3.11+
except Exception:  # pragma: no cover
    import tomli as tomllib  # type: ignore


def main() -> None:
    pyproject = Path("pyproject.toml")
    if not pyproject.exists():
        return
    try:
        with pyproject.open("rb") as f:
            data = tomllib.load(f)
        scripts = data.get("project", {}).get("scripts", {})
        if scripts:
            first = next(iter(scripts.values()))
            print(first, end="")
    except Exception:
        pass


if __name__ == "__main__":
    main()
