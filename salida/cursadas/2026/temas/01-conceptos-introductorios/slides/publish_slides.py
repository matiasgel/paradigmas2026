#!/usr/bin/env python3
"""
Publicador de filminas — Tema 01
=================================
Wrapper que delega al pipeline principal del módulo EDU.

Uso:
  python publish_slides.py
  python publish_slides.py --plan-only
  python publish_slides.py --publish-only

El plan YAML (plan-filminas-01-conceptos-introductorios.yaml) queda en esta
carpeta para revisión antes de publicar.

Requiere (desde la raíz del proyecto):
  pip install -r salida/edu-standalone/scripts/requirements.txt
"""

import sys
from pathlib import Path

# ── Localizar el pipeline principal ──────────────────────────────────────────
_SLIDES_DIR   = Path(__file__).resolve().parent          # .../slides/
_TOPIC_DIR    = _SLIDES_DIR.parent                       # .../01-conceptos-introductorios/
_PROJECT_ROOT = _TOPIC_DIR.parents[3]                    # raíz del repo
_PIPELINE     = _PROJECT_ROOT / "salida" / "edu-standalone" / "scripts" / "slides_pipeline.py"

if not _PIPELINE.exists():
    print(f"❌ No se encontró el pipeline en:\n   {_PIPELINE}")
    print("   Verificar que salida/edu-standalone/scripts/slides_pipeline.py existe.")
    sys.exit(1)

# Inyectar el directorio del pipeline en sys.path
sys.path.insert(0, str(_PIPELINE.parent))

# Pasar el directorio del tema como argumento y delegar
sys.argv = [str(_PIPELINE)] + [str(_TOPIC_DIR)] + sys.argv[1:]

from slides_pipeline import main  # noqa: E402
main()
