#!/usr/bin/env python3
"""
export_repo.py — Exporta el módulo edu-standalone a un nuevo repositorio GitHub
===============================================================================

Crea un repositorio en GitHub usando el contenido actual de `salida/edu-standalone` como
raíz del nuevo repo. Está pensado para clonar el curso base en un repo nuevo listo para
usar en un curso nuevo.

Uso:
    python scripts/export_repo.py --repo judiciales2026ush --visibility public
    python scripts/export_repo.py --repo judiciales2026ush --visibility public --description "Curso judicial 2026 USh" --force

Requisitos:
  - GitHub CLI (`gh`) instalado y autenticado
  - permisos `repo` en la cuenta activa

Salida:
  - Crea o actualiza el repo GitHub especificado
  - Empuja la rama `main`
  - Informa la URL del repo resultante
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run_command(cmd: list[str], cwd: Path | None = None) -> tuple[int, str]:
    result = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode, output.strip()


def check_gh() -> tuple[bool, str]:
    code, out = run_command(["gh", "auth", "status", "--show-token"])
    return code == 0, out


def get_current_user() -> str:
    code, out = run_command(["gh", "api", "user", "--jq", ".login"])
    if code != 0:
        raise RuntimeError(f"No se pudo obtener usuario GH: {out}")
    return out.strip()


def repo_exists(repo: str) -> bool:
    code, _ = run_command(["gh", "repo", "view", repo])
    return code == 0


def create_github_repo(repo: str, visibility: str, description: str, private: bool, confirm: bool) -> None:
    cmd = ["gh", "repo", "create", repo, f"--{visibility}" if visibility in ("public", "private") else "--public"]
    if description:
        cmd.extend(["--description", description])
    if confirm:
        cmd.append("--confirm")
    code, out = run_command(cmd)
    if code != 0:
        raise RuntimeError(f"No se pudo crear el repo {repo}: {out}")


def copy_edu_root(temp_dir: Path) -> None:
    src = ROOT
    dst = temp_dir
    ignore = shutil.ignore_patterns(".git", "__pycache__", "*.pyc", ".pytest_cache", "*.log", "error-registry.jsonl")
    shutil.copytree(src, dst, dirs_exist_ok=True, ignore=ignore)
    git_dir = dst / ".git"
    if git_dir.exists():
        shutil.rmtree(git_dir)


def init_push_repo(temp_dir: Path, repo: str, branch: str, force: bool) -> None:
    code, out = run_command(["git", "init"], cwd=temp_dir)
    if code != 0:
        raise RuntimeError(f"git init falló: {out}")

    code, out = run_command(["git", "checkout", "-b", branch], cwd=temp_dir)
    if code != 0:
        raise RuntimeError(f"git checkout {branch} falló: {out}")

    code, out = run_command(["git", "add", "--all"], cwd=temp_dir)
    if code != 0:
        raise RuntimeError(f"git add falló: {out}")

    code, out = run_command(["git", "commit", "-m", "Initial edu-standalone export"], cwd=temp_dir)
    if code != 0:
        raise RuntimeError(f"git commit falló: {out}")

    code, out = run_command(["git", "remote", "add", "origin", f"https://github.com/{repo}.git"], cwd=temp_dir)
    if code != 0:
        raise RuntimeError(f"git remote add origin falló: {out}")

    push_cmd = ["git", "push", "-u", "origin", branch]
    if force:
        push_cmd.append("--force")
    code, out = run_command(push_cmd, cwd=temp_dir)
    if code != 0:
        raise RuntimeError(f"git push falló: {out}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Exporta edu-standalone a un nuevo repositorio GitHub.")
    parser.add_argument("--repo", required=True, help="Nombre del repo en GitHub (ej: judiciales2026ush)")
    parser.add_argument("--visibility", choices=["public", "private"], default="public")
    parser.add_argument("--description", default="Edu standalone course repo ready for a new course.")
    parser.add_argument("--force", action="store_true", help="Usar repo existente si ya existe en GitHub")
    parser.add_argument("--branch", default="main", help="Nombre de la rama principal a usar")
    args = parser.parse_args()

    gh_ok, gh_out = check_gh()
    if not gh_ok:
        print("❌ GitHub CLI no está autenticado o no está disponible.", file=sys.stderr)
        print(gh_out, file=sys.stderr)
        sys.exit(1)

    owner = get_current_user()
    full_repo = f"{owner}/{args.repo}"

    if repo_exists(full_repo):
        if not args.force:
            print(f"❌ El repo {full_repo} ya existe. Usa --force para reutilizarlo.", file=sys.stderr)
            sys.exit(1)
        print(f"⚠️  El repo {full_repo} ya existe. Se sobrescribirá el contenido localmente en una nueva rama main.")
    else:
        print(f"🔧 Creando repo {full_repo} en GitHub...")
        create_github_repo(full_repo, args.visibility, args.description, args.visibility == "private", confirm=True)
        print(f"✅ Repo creado: https://github.com/{full_repo}")

    with tempfile.TemporaryDirectory(prefix="edu_export_") as tmp:
        temp_dir = Path(tmp)
        print(f"📁 Copiando edu-standalone a {temp_dir}...")
        copy_edu_root(temp_dir)
        print("🧾 Inicializando repo local y empujando a GitHub...")
        init_push_repo(temp_dir, full_repo, args.branch, args.force)
        print(f"✅ Exportado correctamente a https://github.com/{full_repo}")

if __name__ == "__main__":
    main()
