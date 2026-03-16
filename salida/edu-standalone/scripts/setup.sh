#!/usr/bin/env bash
# EDU Standalone — Setup del entorno Python
# ==========================================
# Verifica Python, crea el venv si no existe e instala todas las dependencias.
#
# Uso desde la raíz del repositorio:
#   bash salida/edu-standalone/scripts/setup.sh
#
# O desde la carpeta scripts/:
#   bash setup.sh

set -euo pipefail

# ── Colores ────────────────────────────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'
ok()   { echo -e "${GREEN}✅ $*${NC}"; }
warn() { echo -e "${YELLOW}⚠️  $*${NC}"; }
err()  { echo -e "${RED}❌ $*${NC}" >&2; exit 1; }

# ── Resolver raíz del proyecto ──────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Subir hasta encontrar el repo: scripts/ → edu-standalone/ → salida/ → repo-root
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"

if [[ ! -f "$PROJECT_ROOT/.git/config" && ! -f "$PROJECT_ROOT/module.yaml" ]]; then
  # Fallback: buscar .git hacia arriba
  cur="$SCRIPT_DIR"
  while [[ "$cur" != "/" ]]; do
    if [[ -f "$cur/.git/config" || -d "$cur/.git" ]]; then
      PROJECT_ROOT="$cur"
      break
    fi
    cur="$(dirname "$cur")"
  done
fi

REQUIREMENTS="$SCRIPT_DIR/requirements.txt"
VENV_DIR="$PROJECT_ROOT/.venv"
ENV_EXAMPLE="$SCRIPT_DIR/../.env.example"
ENV_FILE="$PROJECT_ROOT/.env"

echo ""
echo "╔══════════════════════════════════════════════╗"
echo "║   EDU Standalone — Setup del entorno Python  ║"
echo "╚══════════════════════════════════════════════╝"
echo "   Raíz del proyecto: $PROJECT_ROOT"
echo "   Venv: $VENV_DIR"
echo ""

# ── 0. Crear .env desde .env.example si no existe ──────────────────────────
if [[ ! -f "$ENV_FILE" && -f "$ENV_EXAMPLE" ]]; then
  cp "$ENV_EXAMPLE" "$ENV_FILE"
  ok ".env creado desde .env.example en $ENV_FILE"
elif [[ -f "$ENV_FILE" ]]; then
  ok ".env ya existe."
fi

# ── 1. Verificar Python ─────────────────────────────────────────────────────
MIN_MAJOR=3; MIN_MINOR=10

find_python() {
  for cmd in python3 python python3.12 python3.11 python3.10; do
    if command -v "$cmd" &>/dev/null; then
      ver=$("$cmd" --version 2>&1 | grep -oP '\d+\.\d+' | head -1)
      major=$(echo "$ver" | cut -d. -f1)
      minor=$(echo "$ver" | cut -d. -f2)
      if (( major > MIN_MAJOR || (major == MIN_MAJOR && minor >= MIN_MINOR) )); then
        echo "$cmd"
        return 0
      fi
    fi
  done
  return 1
}

PYTHON=$(find_python) || err "No se encontró Python >= ${MIN_MAJOR}.${MIN_MINOR}. Instalalo con: sudo apt install python3.12"
ok "Python encontrado: $PYTHON ($($PYTHON --version))"

# ── 2. Crear / verificar venv ───────────────────────────────────────────────
if [[ -f "$VENV_DIR/bin/activate" ]]; then
  ok "Venv ya existe en $VENV_DIR"
else
  warn "Creando venv en $VENV_DIR …"
  "$PYTHON" -m venv "$VENV_DIR"
  ok "Venv creado."
fi

PIP="$VENV_DIR/bin/pip"
PYTHON_VENV="$VENV_DIR/bin/python"

# ── 3. Actualizar pip ───────────────────────────────────────────────────────
echo ""
echo "📦 Actualizando pip …"
"$PIP" install --upgrade pip --quiet
ok "pip actualizado."

# ── 4. Instalar dependencias ────────────────────────────────────────────────
echo ""
echo "📦 Instalando dependencias desde requirements.txt …"
"$PIP" install -r "$REQUIREMENTS" --quiet
ok "Todas las dependencias instaladas."

# ── 5. Verificar instalación ────────────────────────────────────────────────
echo ""
echo "🔍 Verificando paquetes clave …"

# check_pkg <import_name> <dist_name>
check_pkg() {
  local import_name="$1"
  local dist_name="${2:-$1}"
  if "$PYTHON_VENV" -c "import $import_name" 2>/dev/null; then
    local ver
    ver=$("$PIP" show "$dist_name" 2>/dev/null | grep '^Version:' | awk '{print $2}')
    ok "$dist_name ${ver:-instalado}"
  else
    warn "$dist_name no se pudo importar — intentá: pip install $dist_name"
  fi
}

check_pkg googleapiclient   google-api-python-client
check_pkg google.auth       google-auth-oauthlib
check_pkg yaml              PyYAML
check_pkg requests          requests
check_pkg matplotlib        matplotlib
check_pkg PIL               Pillow

# ── 6. Mostrar instrucciones finales ────────────────────────────────────────
echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║   Entorno listo. Para activar manualmente:                   ║"
echo "║   source .venv/bin/activate                                  ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "Para publicar filminas de un tema:"
echo "  $PYTHON_VENV salida/edu-standalone/scripts/slides_pipeline.py \\"
echo "              salida/cursadas/2026/temas/01-conceptos-introductorios"
echo ""
echo "O desde la carpeta del tema:"
echo "  $PYTHON_VENV slides/publish_slides.py"
echo ""
