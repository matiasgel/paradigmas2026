from __future__ import annotations

import runpy
import sys
from pathlib import Path


def run_root_script(script_name: str) -> None:
    current = Path(__file__).resolve()
    project_root = current.parents[3]
    target = project_root / "scripts" / script_name
    if not target.exists():
        raise FileNotFoundError(f"No se encontró el script canónico: {target}")

    sys.path.insert(0, str(target.parent))
    runpy.run_path(str(target), run_name="__main__")