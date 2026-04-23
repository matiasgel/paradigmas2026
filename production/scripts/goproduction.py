#!/usr/bin/env python3
"""
EDU Standalone ÔÇö Publicar en rama production
============================================
Despliega salida/edu-standalone/ hacia las ramas de destino (production, lenguajes, lenguajes2026).

Dos modos de operaci├│n:
  trigger (defecto): hace commit+push a main ÔåÆ activa GitHub Actions autom├íticamente
  local:             deploy directo usando git worktree, sin pasar por GitHub Actions

Uso:
  python scripts/goproduction.py                            # trigger via GitHub Actions
  python scripts/goproduction.py --local                    # deploy local directo
  python scripts/goproduction.py --local --branches production   # solo una rama
  python scripts/goproduction.py --dry-run                  # mostrar qu├® se har├¡a

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

# ÔöÇÔöÇ Colores de terminal ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ

def _ok(msg: str)   -> None: print(f"\033[0;32mÔ£à {msg}\033[0m")
def _warn(msg: str) -> None: print(f"\033[1;33mÔÜá´©Å  {msg}\033[0m")
def _err(msg: str)  -> None: print(f"\033[0;31mÔØî {msg}\033[0m", file=sys.stderr); sys.exit(1)
def _info(msg: str) -> None: print(f"   {msg}")

# ÔöÇÔöÇ Utilidades git ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ

def _run(cmd: list[str], cwd: Path | None = None, capture: bool = False) -> subprocess.CompletedProcess:
    """Ejecuta un comando; termina con error si el exit code no es 0."""
    result = subprocess.run(cmd, cwd=cwd, capture_output=capture, text=True)
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        _err(f"Fall├│: {' '.join(cmd)}\n{detail}")
    return result


def _git(args: list[str], cwd: Path | None = None, capture: bool = True) -> str:
    """Ejecuta git y retorna stdout como string limpio."""
    return _run(["git"] + args, cwd=cwd, capture=capture).stdout.strip()

# ÔöÇÔöÇ Rutas ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ

def find_project_root() -> Path:
    """Busca la ra├¡z del repo (.git) desde la ubicaci├│n de este script."""
    cur = Path(__file__).resolve().parent
    for _ in range(8):
        if (cur / ".git").exists():
            return cur
        if cur == cur.parent:
            break
        cur = cur.parent
    _err("No se encontr├│ la ra├¡z del proyecto (.git). ┬┐Est├ís dentro de un repositorio git?")
    return Path()  # unreachable


def find_edu_src(project_root: Path) -> Path:
    """Retorna la carpeta fuente de edu-standalone."""
    embedded = project_root / "salida" / "edu-standalone"
    if embedded.exists():
        return embedded
    # Modo standalone: el script ya est├í dentro de edu-standalone/scripts/
    standalone = Path(__file__).resolve().parent.parent
    if (standalone / "_edu").exists():
        return standalone
    _err(f"No se encontr├│ salida/edu-standalone/ en {project_root}.")
    return Path()  # unreachable

# ÔöÇÔöÇ Verificaci├│n de estado git ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ

def check_and_commit_changes(project_root: Path, edu_path: str, dry_run: bool) -> None:
    """Si hay cambios sin commitear, ofrece hacer commit autom├ítico."""
    status = _git(["status", "--porcelain", edu_path], cwd=project_root)
    if not status:
        return

    _warn("Hay cambios sin commitear en edu-standalone/:")
    print(status)
    if dry_run:
        _info("--dry-run: se har├¡a commit autom├ítico de los cambios.")
        return

    resp = input("\n   ┬┐Hacer commit autom├ítico de estos cambios? [s/N] ").strip().lower()
    if resp != "s":
        _err("Abortado. Hac├® commit de tus cambios antes de publicar.")

    _run(["git", "add", edu_path], cwd=project_root)
    _run(
        ["git", "commit", "-m", "deploy: actualizar edu-standalone antes de publicar"],
        cwd=project_root,
    )
    _ok("Commit realizado.")

# ÔöÇÔöÇ Modo trigger: push a main ÔåÆ GitHub Actions ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ

def trigger_via_push(project_root: Path, dry_run: bool) -> None:
    """Hace push a main para activar el workflow goproduction.yml de GitHub Actions."""
    print("\n­ƒÜÇ  Modo: Trigger GitHub Actions (push a main)")
    print("ÔöÇ" * 52)

    remote_url = _git(["remote", "get-url", "origin"], cwd=project_root)
    current_branch = _git(["branch", "--show-current"], cwd=project_root)
    _info(f"Remote:       {remote_url}")
    _info(f"Rama actual:  {current_branch}")

    if current_branch != "main":
        _warn(f"Est├ís en la rama '{current_branch}', no en 'main'.")
        resp = input("   ┬┐Hacer push igualmente? [s/N] ").strip().lower()
        if resp != "s":
            _err("Abortado.")

    if dry_run:
        _ok("--dry-run: se ejecutar├¡a ÔåÆ git push origin main")
        return

    print("\n­ƒôñ Haciendo push a main ÔÇª")
    _run(["git", "push", "origin", current_branch], cwd=project_root, capture=False)
    _ok("Push completado. GitHub Actions desplegar├í edu-standalone ÔåÆ production, lenguajes y lenguajes2026.")

    # Construir URL de Actions seg├║n formato SSH o HTTPS
    actions_url = (
        remote_url
        .replace("git@github.com:", "https://github.com/")
        .removesuffix(".git")
        + "/actions"
    )
    print(f"\n   Segu├¡ el progreso en:\n   {actions_url}")

# ÔöÇÔöÇ Modo local: deploy directo con git worktree ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ

def local_deploy(
    project_root: Path,
    edu_src: Path,
    branches: list[str],
    dry_run: bool,
) -> None:
    """Deploy local usando git worktree: sin clonar ni pasar por GitHub Actions."""
    print(f"\n­ƒÅù´©Å  Modo: Deploy local ÔåÆ {', '.join(branches)}")
    print("ÔöÇ" * 52)

    for branch in branches:
        print(f"\n  ÔûÂ Preparando rama '{branch}' ÔÇª")

        # Verificar si la rama ya existe en origin
        remote_refs = _git(["ls-remote", "--heads", "origin", branch], cwd=project_root)
        branch_exists_remote = bool(remote_refs.strip())

        if dry_run:
            _ok(f"--dry-run: se crear├¡a worktree para '{branch}' y se copiar├¡an artefactos.")
            continue

        with tempfile.TemporaryDirectory(prefix=f"edu-deploy-{branch}-") as tmpdir:
            wt_path = Path(tmpdir) / branch

            if branch_exists_remote:
                # Traer la rama remota si a├║n no est├í local
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
                _warn(f"Rama '{branch}' no existe en origin. Se crear├í como rama hu├®rfana.")
                _run(
                    ["git", "worktree", "add", "--orphan", "-B", branch, str(wt_path)],
                    cwd=project_root, capture=True,
                )
                # Limpiar worktree vac├¡o
                subprocess.run(["git", "rm", "-rf", "."], cwd=wt_path, capture_output=True)

            try:
                _sync_edu_artifacts(project_root, edu_src, wt_path)
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

# ÔöÇÔöÇ Sincronizaci├│n de artefactos ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ

def _sync_edu_artifacts(project_root: Path, edu_src: Path, target: Path) -> None:
    """Sincroniza el root de edu-standalone en el worktree destino preservando runtime."""
    print()
    _info("Sincronizando artefactos:")

    def preserve_path(preserve_root: Path, rel_path: str) -> tuple[Path, Path] | None:
        current = target / rel_path
        if not current.exists():
            return None

        saved = preserve_root / rel_path
        saved.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(current), str(saved))
        _info(f"  preservado: {rel_path}")
        return current, saved

    def restore_path(saved_entry: tuple[Path, Path] | None) -> None:
        if not saved_entry:
            return

        destination, saved = saved_entry
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(saved), str(destination))

    def _display_rel(path: Path, base: Path) -> Path | str:
        try:
            return path.relative_to(base)
        except ValueError:
            return path.name

    def copy_tree(src: Path, dst: Path, *, ignore=None) -> None:
        shutil.copytree(src, dst, dirs_exist_ok=True, ignore=ignore)
        count = sum(1 for item in dst.rglob("*") if item.is_file())
        _info(f"  {_display_rel(src, edu_src)}/ ÔåÆ {dst.relative_to(target)}/  ({count} archivos)")

    def copy_file(src: Path, dst: Path) -> None:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        _info(f"  {_display_rel(src, edu_src)} ÔåÆ {dst.relative_to(target)}")

    with tempfile.TemporaryDirectory(prefix="edu-sync-") as tmpdir:
        preserve_root = Path(tmpdir)
        preserved = [
            preserve_path(preserve_root, "_edu/config.yaml"),
            preserve_path(preserve_root, "_edu/active-topic.yaml"),
            preserve_path(preserve_root, ".env"),
            preserve_path(preserve_root, "_edu-memory"),
            preserve_path(preserve_root, "salida"),
            preserve_path(preserve_root, "material"),
            preserve_path(preserve_root, "docs"),
        ]

        for item in target.iterdir():
            if item.name == ".git":
                continue
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()

        for saved_entry in preserved:
            restore_path(saved_entry)

        for item in edu_src.iterdir():
            if item.name in {".git", "_edu-memory", "salida", "material", "docs"}:
                continue

            destination = target / item.name
            if item.name == ".github":
                copy_tree(item, destination, ignore=shutil.ignore_patterns("copilot-instructions.md"))
                continue
            if item.name == "_edu":
                copy_tree(item, destination, ignore=shutil.ignore_patterns("config.yaml", "active-topic.yaml"))
                continue

            if item.is_dir():
                copy_tree(item, destination)
            else:
                copy_file(item, destination)

    workflows_src = project_root / ".github" / "workflows"
    workflows_dst = target / ".github" / "workflows"
    if workflows_src.exists():
        copy_tree(workflows_src, workflows_dst)

    base_instructions = project_root / ".github" / "copilot-instructions.md"
    edu_instructions = edu_src / ".github" / "copilot-instructions.md"
    target_instructions = target / ".github" / "copilot-instructions.md"
    if base_instructions.exists():
        target_instructions.parent.mkdir(parents=True, exist_ok=True)
        base_content = base_instructions.read_text(encoding="utf-8")
        start_marker = "<!-- EDU:START -->"
        end_marker = "<!-- EDU:END -->"
        if start_marker in base_content and end_marker in base_content:
            start_index = base_content.index(start_marker)
            base_content = base_content[:start_index].rstrip() + "\n"
        edu_block = edu_instructions.read_text(encoding="utf-8") if edu_instructions.exists() else ""
        target_instructions.write_text(base_content + "\n" + edu_block.lstrip("\n"), encoding="utf-8")
        _info("  .github/copilot-instructions.md recompuesto desde main + EDU")

    env_example = target / ".env.example"
    env_file = target / ".env"
    if env_example.exists() and not env_file.exists():
        shutil.copy2(env_example, env_file)
        _info("  .env generado desde .env.example")
    elif env_file.exists():
        _info("  .env preservado (configuraci├│n del usuario)")


def _commit_and_push(wt_path: Path, branch: str) -> None:
    """Hace commit y push desde el worktree."""
    _run(["git", "add", "-A"], cwd=wt_path, capture=True)

    diff = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=wt_path,
    )
    if diff.returncode == 0:
        _ok(f"'{branch}': sin cambios nuevos ÔÇö nada que commitear.")
        return

    deploy_date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    _run(
        ["git", "commit", "-m", f"deploy: edu-standalone ÔåÆ {branch} [{deploy_date}]"],
        cwd=wt_path, capture=False,
    )
    _run(["git", "push", "origin", branch], cwd=wt_path, capture=False)
    _ok(f"'{branch}': deploy completado Ô£ô")

# ÔöÇÔöÇ Entry point ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Publicar edu-standalone ÔåÆ ramas de producci├│n",
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
        default=["production", "lenguajes", "lenguajes2026"],
        metavar="BRANCH",
        help="Ramas destino para --local (defecto: production lenguajes lenguajes2026).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Mostrar qu├® se har├¡a sin ejecutar ning├║n cambio real.",
    )
    args = parser.parse_args()

    print()
    print("ÔòöÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòù")
    print("Ôòæ   EDU Standalone ÔÇö Publicar ramas de producci├│n      Ôòæ")
    print("ÔòÜÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòØ")

    if args.dry_run:
        _warn("Modo --dry-run: no se ejecutar├í ning├║n cambio real.")

    project_root = find_project_root()
    edu_src      = find_edu_src(project_root)

    # Ruta relativa de edu-standalone/ respecto al root (puede ser "." en standalone)
    try:
        edu_rel = str(edu_src.relative_to(project_root))
    except ValueError:
        edu_rel = str(edu_src)

    _info(f"Ra├¡z del proyecto: {project_root}")

    check_and_commit_changes(project_root, edu_rel, args.dry_run)

    if args.local:
        local_deploy(project_root, edu_src, args.branches, args.dry_run)
    else:
        trigger_via_push(project_root, args.dry_run)

    print()
    _ok("Listo.")


if __name__ == "__main__":
    main()