#!/usr/bin/env bash
# EDU Standalone — Setup del entorno Python (portable)
# =====================================================
# Compatible con: Linux, macOS, Windows (Git Bash / WSL)
# Funciona tanto en el repo completo (paradigmas2026) como en deploy standalone.
#
# Uso (desde cualquier directorio):
#   bash path/to/edu-standalone/scripts/setup.sh
#   bash setup.sh                  # desde scripts/
#   bash ../scripts/setup.sh       # desde edu-standalone/

set -euo pipefail

# ── Utilidades (sin depender de echo -e ni colores de terminal) ───────────────
_print() { printf '%s\n' "$*"; }
ok()     { printf '\033[0;32m✅ %s\033[0m\n' "$*"; }
warn()   { printf '\033[1;33m⚠️  %s\033[0m\n' "$*"; }
err()    { printf '\033[0;31m❌ %s\033[0m\n' "$*" >&2; exit 1; }

# ── Rutas base ────────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EDU_MODULE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"     # .../edu-standalone/

# ── Detectar PROJECT_ROOT (portable: embebido en repo o standalone) ────────────
# Estrategia: buscar .git hacia arriba desde SCRIPT_DIR.
# Si no hay .git en ningún nivel → edu-standalone/ ES la raíz (modo standalone).
find_project_root() {
  local cur="$1"
  local depth=0
  while [[ "$cur" != "/" && $depth -lt 8 ]]; do
    if [[ -d "$cur/.git" ]]; then
      printf '%s' "$cur"
      return 0
    fi
    cur="$(dirname "$cur")"
    depth=$((depth + 1))
  done
  # No se encontró .git → modo standalone: la raíz es edu-standalone/ misma
  printf '%s' "$EDU_MODULE_DIR"
}

PROJECT_ROOT="$(find_project_root "$SCRIPT_DIR")"

# ── Detectar sistema operativo (para ruta del venv) ───────────────────────────
case "$(uname -s 2>/dev/null || echo Windows)" in
  MINGW*|MSYS*|CYGWIN*|Windows) OS_TYPE="windows" ;;
  Darwin)                         OS_TYPE="macos"   ;;
  *)                              OS_TYPE="linux"   ;;
esac

# ── Rutas del venv (Windows usa Scripts/, Unix usa bin/) ──────────────────────
VENV_DIR="$PROJECT_ROOT/.venv"
if [[ "$OS_TYPE" == "windows" ]]; then
  VENV_BIN="$VENV_DIR/Scripts"
else
  VENV_BIN="$VENV_DIR/bin"
fi
VENV_ACTIVATE="$VENV_BIN/activate"
PIP="$VENV_BIN/pip"
PYTHON_VENV="$VENV_BIN/python"

REQUIREMENTS="$SCRIPT_DIR/requirements.txt"
ENV_EXAMPLE="$EDU_MODULE_DIR/.env.example"
ENV_FILE="$PROJECT_ROOT/.env"

# ── Detectar modo de despliegue ───────────────────────────────────────────────
if [[ "$PROJECT_ROOT" == "$EDU_MODULE_DIR" ]]; then
  DEPLOY_MODE="standalone"
  PIPELINE_REL="scripts/slides_pipeline.py"
else
  DEPLOY_MODE="embedded"
  PIPELINE_REL="$(realpath --relative-to="$PROJECT_ROOT" "$SCRIPT_DIR/slides_pipeline.py" 2>/dev/null \
    || python3 -c "import os; print(os.path.relpath('$SCRIPT_DIR/slides_pipeline.py','$PROJECT_ROOT'))")"
fi

_print ""
_print "╔══════════════════════════════════════════════╗"
_print "║   EDU Standalone — Setup del entorno Python  ║"
_print "╚══════════════════════════════════════════════╝"
_print "   OS:        $OS_TYPE"
_print "   Modo:      $DEPLOY_MODE"
_print "   Raíz repo: $PROJECT_ROOT"
_print "   Módulo:    $EDU_MODULE_DIR"
_print "   Venv:      $VENV_DIR"
_print ""

# ── 0. Crear .env desde .env.example si no existe ────────────────────────────
if [[ ! -f "$ENV_FILE" && -f "$ENV_EXAMPLE" ]]; then
  # Reemplazar EDU_PIPELINE_SCRIPT con la ruta real en este entorno
  sed "s|EDU_PIPELINE_SCRIPT=.*|EDU_PIPELINE_SCRIPT=$PIPELINE_REL|" \
    "$ENV_EXAMPLE" > "$ENV_FILE"
  ok ".env creado en $ENV_FILE"
elif [[ -f "$ENV_FILE" ]]; then
  ok ".env ya existe en $ENV_FILE"
fi

# ── 1. Verificar Python >= 3.10 ───────────────────────────────────────────────
MIN_MAJOR=3; MIN_MINOR=10

# Versión sin grep -P (compatible macOS BSD grep y GNU grep)
python_ver() {
  "$1" --version 2>&1 | awk '{print $2}'
}
python_ok() {
  local ver
  ver=$(python_ver "$1" 2>/dev/null) || return 1
  local major minor
  major=$(printf '%s' "$ver" | cut -d. -f1)
  minor=$(printf '%s' "$ver" | cut -d. -f2)
  [[ "$major" -gt "$MIN_MAJOR" || ( "$major" -eq "$MIN_MAJOR" && "$minor" -ge "$MIN_MINOR" ) ]]
}

PYTHON=""
for cmd in python3 python python3.13 python3.12 python3.11 python3.10; do
  if command -v "$cmd" &>/dev/null && python_ok "$cmd"; then
    PYTHON="$cmd"
    break
  fi
done

[[ -n "$PYTHON" ]] || err "No se encontró Python >= ${MIN_MAJOR}.${MIN_MINOR}.\n   Linux:  sudo apt install python3.12\n   macOS:  brew install python@3.12\n   Windows: https://python.org/downloads"
ok "Python: $PYTHON ($(python_ver "$PYTHON"))"

# ── 2. Crear / verificar venv ─────────────────────────────────────────────────
if [[ -f "$VENV_ACTIVATE" ]]; then
  ok "Venv ya existe en $VENV_DIR"
else
  warn "Creando venv en $VENV_DIR …"
  "$PYTHON" -m venv "$VENV_DIR"
  ok "Venv creado."
fi

# ── 3. Actualizar pip ─────────────────────────────────────────────────────────
_print ""
_print "📦 Actualizando pip …"
"$PIP" install --upgrade pip --quiet
ok "pip actualizado."

# ── 4. Instalar dependencias ──────────────────────────────────────────────────
_print ""
_print "📦 Instalando dependencias desde requirements.txt …"
"$PIP" install -r "$REQUIREMENTS" --quiet
ok "Todas las dependencias instaladas."

# ── 5. Verificar paquetes ─────────────────────────────────────────────────────
_print ""
_print "🔍 Verificando paquetes clave …"

check_pkg() {
  local import_name="$1" dist_name="${2:-$1}"
  if "$PYTHON_VENV" -c "import $import_name" 2>/dev/null; then
    local ver
    ver=$("$PIP" show "$dist_name" 2>/dev/null | awk '/^Version:/{print $2}')
    ok "$dist_name ${ver:-instalado}"
  else
    warn "$dist_name no se pudo importar — revisar: $PIP install $dist_name"
  fi
}

check_pkg googleapiclient  google-api-python-client
check_pkg google.auth      google-auth-oauthlib
check_pkg yaml             PyYAML
check_pkg requests         requests
check_pkg matplotlib       matplotlib
check_pkg PIL              Pillow

# ── 6. Instrucciones finales ──────────────────────────────────────────────────
_print ""
_print "╔══════════════════════════════════════════════════════════════╗"
_print "║  Entorno listo.                                              ║"
_print "╚══════════════════════════════════════════════════════════════╝"
_print ""
if [[ "$OS_TYPE" == "windows" ]]; then
  _print "  Activar venv:  .venv\\Scripts\\activate"
else
  _print "  Activar venv:  source .venv/bin/activate"
fi
_print ""
_print "  Publicar filminas de un tema:"
_print "    $PYTHON_VENV $PIPELINE_REL \\"
_print "      <ruta-tema>"
_print ""
_print "  Ejemplo:"
if [[ "$DEPLOY_MODE" == "standalone" ]]; then
  _print "    $PYTHON_VENV scripts/slides_pipeline.py \\"
  _print "      temas/01-conceptos-introductorios"
else
  _print "    $PYTHON_VENV $PIPELINE_REL \\"
  _print "      salida/cursadas/2026/temas/01-conceptos-introductorios"
fi
_print ""
