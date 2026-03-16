#!/usr/bin/env python3
"""
EDU Standalone — Publicar en rama production
============================================
Despliega salida/edu-standalone/ hacia las ramas de destino (production, lenguajes).

Dos modos de operación:
  trigger (defecto): hace commit+push a main → activa GitHub Actions automáticamente
  local:             deploy directo usando git worktree, sin pasar por GitHub Actions

Uso:
  python scripts/goproduction.py                            # trigger via GitHub Actions
  python scripts/goproduction.py --local                    # deploy local directo
  python scripts/goproduction.py --local --branches production   # solo una rama
  python scripts/goproduction.py --dry-run                  # mostrar qué se haría

Requiere:
  - git instalado y configurado
  - acceso de escritura al repositorio remoto (origin)
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

# ── Colores de terminal ────────────────────────────────────────────────────────

def _ok(msg: str)   -> None: print(f"\033[0;32m✅ {msg}\033[0m")
def _warn(msg: str) -> None: print(f"\033[1;33m⚠️  {msg}\033[0m")
def _err(msg: str)  -> None: print(f"\033[0;31m❌ {msg}\033[0m", file=sys.stderr); sys.exit(1)
def _info(msg: str) -> None: print(f"   {msg}")

# ── Utilidades git ────────────────────────────────────────────────────────────

def _run(cmd: list[str], cwd: Path | None = None, capture: bool = False) -> subprocess.CompletedProcess:
    """Ejecuta un comando; termina con error si el exit code no es 0."""
    result = subprocess.run(cmd, cwd=cwd, capture_output=capture, text=True)
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        _err(f"Falló: {' '.join(cmd)}\n{detail}")
    return result


def _git(args: list[str], cwd: Path | None = None, capture: bool = True) -> str:
    """Ejecuta git y retorna stdout como string limpio."""
    return _run(["git"] + args, cwd=cwd, capture=capture).stdout.strip()

# ── Rutas ─────────────────────────────────────────────────────────────────────

def find_project_root() -> Path:
    """Busca la raíz del repo (.git) desde la ubicación de este script."""
    cur = Path(__file__).resolve().parent
    for _ in range(8):
        if (cur / ".git").exists():
            return cur
        if cur == cur.parent:
            break
        cur = cur.parent
    _err("No se encontró la raíz del proyecto (.git). ¿Estás dentro de un repositorio git?")
    return Path()  # unreachable


def find_edu_src(project_root: Path) -> Path:
    """Retorna la carpeta fuente de edu-standalone."""
    embedded = project_root / "salida" / "edu-standalone"
    if embedded.exists():
        return embedded
    # Modo standalone: el script ya está dentro de edu-standalone/scripts/
    standalone = Path(__file__).resolve().parent.parent
    if (standalone / "_edu").exists():
        return standalone
    _err(f"No se encontró salida/edu-standalone/ en {project_root}.")
    return Path()  # unreachable

# ── Verificación de estado git ────────────────────────────────────────────────

def check_and_commit_changes(project_root: Path, edu_path: str, dry_run: bool) -> None:
    """Si hay cambios sin commitear, ofrece hacer commit automático."""
    status = _git(["status", "--porcelain", edu_path], cwd=project_root)
    if not status:
        return

    _warn("Hay cambios sin commitear en edu-standalone/:")
    print(status)
    if dry_run:
        _info("--dry-run: se haría commit automático de los cambios.")
        return

    resp = input("\n   ¿Hacer commit automático de estos cambios? [s/N] ").strip().lower()
    if resp != "s":
        _err("Abortado. Hacé commit de tus cambios antes de publicar.")

    _run(["git", "add", edu_path], cwd=project_root)
    _run(
        ["git", "commit", "-m", "deploy: actualizar edu-standalone antes de publicar"],
        cwd=project_root,
    )
    _ok("Commit realizado.")

# ── Modo trigger: push a main → GitHub Actions ───────────────────────────────

def trigger_via_push(project_root: Path, dry_run: bool) -> None:
    """Hace push a main para activar el workflow goproduction.yml de GitHub Actions."""
    print("\n🚀  Modo: Trigger GitHub Actions (push a main)")
    print("─" * 52)

    remote_url = _git(["remote", "get-url", "origin"], cwd=project_root)
    current_branch = _git(["branch", "--show-current"], cwd=project_root)
    _info(f"Remote:       {remote_url}")
    _info(f"Rama actual:  {current_branch}")

    if current_branch != "main":
        _warn(f"Estás en la rama '{current_branch}', no en 'main'.")
        resp = input("   ¿Hacer push igualmente? [s/N] ").strip().lower()
        if resp != "s":
            _err("Abortado.")

    if dry_run:
        _ok("--dry-run: se ejecutaría → git push origin main")
        return

    print("\n📤 Haciendo push a main …")
    _run(["git", "push", "origin", current_branch], cwd=project_root, capture=False)
    _ok("Push completado. GitHub Actions desplegará edu-standalone → production.")

    # Construir URL de Actions según formato SSH o HTTPS
    actions_url = (
        remote_url
        .replace("git@github.com:", "https://github.com/")
        .removesuffix(".git")
        + "/actions"
    )
    print(f"\n   Seguí el progreso en:\n   {actions_url}")

# ── Modo local: deploy directo con git worktree ──────────────────────────────

def local_deploy(
    project_root: Path,
    edu_src: Path,
    branches: list[str],
    dry_run: bool,
) -> None:
    """Deploy local usando git worktree: sin clonar ni pasar por GitHub Actions."""
    print(f"\n🏗️  Modo: Deploy local → {', '.join(branches)}")
    print("─" * 52)

    for branch in branches:
        print(f"\n  ▶ Preparando rama '{branch}' …")

        # Verificar si la rama ya existe en origin
        remote_refs = _git(["ls-remote", "--heads", "origin", branch], cwd=project_root)
        branch_exists_remote = bool(remote_refs.strip())

        if dry_run:
            _ok(f"--dry-run: se crearía worktree para '{branch}' y se copiarían artefactos.")
            continue

        with tempfile.TemporaryDirectory(prefix=f"edu-deploy-{branch}-") as tmpdir:
            wt_path = Path(tmpdir) / branch

            if branch_exists_remote:
                # Traer la rama remota si aún no está local
                subprocess.run(
                    ["git", "fetch", "origin", branch],
                    cwd=project_root, capture_output=True
                )
                # Crear worktree apuntando a la rama
                local_exists = _git(
                    ["branch", "--list", branch], cwd=project_root
                )
                if not local_exists:
                    _run(
                        ["git", "branch", branch, f"origin/{branch}"],
                        cwd=project_root, capture=True,
                    )
                _run(
                    ["git", "worktree", "add", str(wt_path), branch],
                    cwd=project_root, capture=True,
                )
            else:
                _warn(f"Rama '{branch}' no existe en origin. Se creará como rama huérfana.")
                _run(
                    ["git", "worktree", "add", "--orphan", "-B", branch, str(wt_path)],
                    cwd=project_root, capture=True,
                )
                # Limpiar worktree vacío
                subprocess.run(["git", "rm", "-rf", "."], cwd=wt_path, capture_output=True)

            try:
                _sync_edu_artifacts(edu_src, wt_path)
                _commit_and_push(wt_path, branch)
            finally:
                # Siempre limpiar el worktree
                subprocess.run(
                    ["git", "worktree", "remove", "--force", str(wt_path)],
                    cwd=project_root, capture_output=True,
                )
                # Borrar referencia local a la rama para no ensuciar el repo
                subprocess.run(
                    ["git", "branch", "-D", branch],
                    cwd=project_root, capture_output=True,
                )

# ── Sincronización de artefactos ──────────────────────────────────────────────

def _sync_edu_artifacts(edu_src: Path, target: Path) -> None:
    """Copia artefactos de edu-standalone/ al worktree destino.

    Replica la misma lógica del GitHub Actions goproduction.yml:
      4.1  _edu/agents/
      4.2  _edu/workflows/
      4.3  _edu/module-help.csv
      4.4  _edu/config.yaml (solo si no existe → preservar config del usuario)
      4.5  .github/agents/edu-*.agent.md
      4.6  .github/prompts/edu-*.prompt.md
      4.7  .github/copilot-instructions.md
           scripts/
    """
    print()
    _info("Sincronizando artefactos:")

    def cp_dir(src_rel: str, dst_rel: str) -> None:
        src = edu_src / src_rel
        dst = target / dst_rel
        if not src.exists():
            _warn(f"  No existe: {src_rel} — omitido")
            return
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        count = sum(1 for _ in dst.rglob("*") if _.is_file())
        _info(f"  {src_rel}/ → {dst_rel}/  ({count} archivos)")

    def cp_file(src_rel: str, dst_rel: str, *, skip_if_exists: bool = False) -> None:
        src = edu_src / src_rel
        dst = target / dst_rel
        if not src.exists():
            _warn(f"  No existe: {src_rel} — omitido")
            return
        if skip_if_exists and dst.exists():
            _info(f"  {dst_rel} preservado (configuración del usuario)")
            return
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        _info(f"  {src_rel} → {dst_rel}")

    # 4.1 Agentes
    cp_dir("_edu/agents", "_edu/agents")
    # 4.2 Workflows
    cp_dir("_edu/workflows", "_edu/workflows")
    # Tasks (si existen)
    if (edu_src / "_edu/tasks").exists():
        cp_dir("_edu/tasks", "_edu/tasks")
    # 4.3 Module help
    cp_file("_edu/module-help.csv", "_edu/module-help.csv")
    # 4.4 Config (preserved si ya existe)
    cp_file("_edu/config.yaml", "_edu/config.yaml", skip_if_exists=True)

    # 4.5 Agentes GitHub edu-*
    agents_src = edu_src / ".github/agents"
    if agents_src.exists():
        agents_dst = target / ".github/agents"
        agents_dst.mkdir(parents=True, exist_ok=True)
        for f in agents_dst.glob("edu-*.md"):
            f.unlink()
        copied = 0
        for f in agents_src.glob("edu-*.agent.md"):
            shutil.copy2(f, agents_dst / f.name)
            copied += 1
        _info(f"  .github/agents/edu-*  ({copied} archivos)")

    # 4.6 Prompts edu-*
    prompts_src = edu_src / ".github/prompts"
    if prompts_src.exists():
        prompts_dst = target / ".github/prompts"
        prompts_dst.mkdir(parents=True, exist_ok=True)
        for f in prompts_dst.glob("*.prompt.md"):
            f.unlink()
        copied = 0
        for f in prompts_src.glob("edu-*.prompt.md"):
            shutil.copy2(f, prompts_dst / f.name)
            copied += 1
        _info(f"  .github/prompts/edu-*  ({copied} archivos)")

    # 4.7 copilot-instructions.md
    cp_file(".github/copilot-instructions.md", ".github/copilot-instructions.md")

    # Scripts del pipeline
    cp_dir("scripts", "scripts")

    # README
    cp_file("README.md", "README.md")
    # requirements.txt raíz
    cp_file("requirements.txt", "requirements.txt")


def _commit_and_push(wt_path: Path, branch: str) -> None:
    """Hace commit y push desde el worktree."""
    _run(["git", "add", "-A"], cwd=wt_path, capture=True)

    diff = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=wt_path,
    )
    if diff.returncode == 0:
        _ok(f"'{branch}': sin cambios nuevos — nada que commitear.")
        return

    deploy_date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    _run(
        ["git", "commit", "-m", f"deploy: edu-standalone → {branch} [{deploy_date}]"],
        cwd=wt_path, capture=False,
    )
    _run(["git", "push", "origin", branch], cwd=wt_path, capture=False)
    _ok(f"'{branch}': deploy completado ✓")

# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Publicar edu-standalone → ramas de producción",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--local",
        action="store_true",
        help="Deploy local directo (sin GitHub Actions). Por defecto usa trigger via push a main.",
    )
    parser.add_argument(
        "--branches",
        nargs="+",
        default=["production", "lenguajes"],
        metavar="BRANCH",
        help="Ramas destino para --local (defecto: production lenguajes).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Mostrar qué se haría sin ejecutar ningún cambio real.",
    )
    args = parser.parse_args()

    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║   EDU Standalone — Publicar en rama production       ║")
    print("╚══════════════════════════════════════════════════════╝")

    if args.dry_run:
        _warn("Modo --dry-run: no se ejecutará ningún cambio real.")

    project_root = find_project_root()
    edu_src      = find_edu_src(project_root)

    # Ruta relativa de edu-standalone/ respecto al root (puede ser "." en standalone)
    try:
        edu_rel = str(edu_src.relative_to(project_root))
    except ValueError:
        edu_rel = str(edu_src)

    _info(f"Raíz del proyecto: {project_root}")
    _info(f"Fuente EDU:        {edu_src}  ({edu_rel})")

    check_and_commit_changes(project_root, edu_rel, args.dry_run)

    if args.local:
        local_deploy(project_root, edu_src, args.branches, args.dry_run)
    else:
        trigger_via_push(project_root, args.dry_run)

    print()
    _ok("Listo.")


if __name__ == "__main__":
    main()
