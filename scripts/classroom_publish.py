#!/usr/bin/env python3
"""
classroom_publish.py — Publicación de TPs a GitHub Classroom (S3.1)

Wrapper de `gh classroom` CLI para publicar assignments directamente.
Solo lectura de archivos EDU — no modifica artefactos existentes.

Uso:
    python scripts/classroom_publish.py --course leng-2026 --topic 01-intro
    python scripts/classroom_publish.py --course leng-2026 --topic 01-intro --grades

Exit codes:
    0 — publicado correctamente (o feature desactivada)
    1 — error (gh CLI no instalado, topic no encontrado, etc.)
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

from pipeline_common import find_project_root, load_yaml


def check_gh_cli() -> bool:
    """Verifica que `gh` CLI esté instalado y autenticado."""
    return shutil.which("gh") is not None


def check_gh_auth() -> bool:
    """Verifica autenticación de gh CLI."""
    try:
        result = subprocess.run(
            ["gh", "auth", "status"],
            capture_output=True, text=True, timeout=10,
        )
        return result.returncode == 0
    except (subprocess.SubprocessError, FileNotFoundError):
        return False


def find_autograde_repo(topic_folder: Path) -> Path | None:
    """Busca el directorio autograde-repo/ en la carpeta del tema."""
    repo_dir = topic_folder / "autograde-repo"
    return repo_dir if repo_dir.is_dir() else None


def publish_assignment(
    topic_folder: Path,
    config: dict,
    course_id: str,
    topic_id: str,
) -> dict:
    """Publica un assignment en GitHub Classroom."""
    org = config.get("classroom_org", "")
    classroom_id = config.get("classroom_id", "")
    deadline_days = config.get("classroom_default_deadline_days", 14)

    if not org:
        return {"ok": False, "error": "classroom_org no configurado en config.yaml"}

    autograde = find_autograde_repo(topic_folder)
    if not autograde:
        return {"ok": False, "error": f"No existe autograde-repo/ en {topic_folder}"}

    deadline = (datetime.now() + timedelta(days=deadline_days)).strftime("%Y-%m-%dT23:59:00Z")
    title = f"{course_id} — {topic_id}"

    cmd = [
        "gh", "classroom", "assignment", "create",
        "--title", title,
        "--repo", f"{org}/{course_id}-{topic_id}",
        "--deadline", deadline,
        "--type", "individual",
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            return {"ok": True, "title": title, "deadline": deadline, "output": result.stdout.strip()}
        return {"ok": False, "error": result.stderr.strip()}
    except subprocess.SubprocessError as e:
        return {"ok": False, "error": str(e)}


def fetch_grades(config: dict, course_id: str) -> dict:
    """Obtiene notas de GitHub Classroom."""
    org = config.get("classroom_org", "")
    classroom_id = config.get("classroom_id", "")

    if not classroom_id:
        return {"ok": False, "error": "classroom_id no configurado en config.yaml"}

    cmd = ["gh", "classroom", "grades", "--classroom-id", classroom_id]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            return {"ok": True, "grades": result.stdout.strip()}
        return {"ok": False, "error": result.stderr.strip()}
    except subprocess.SubprocessError as e:
        return {"ok": False, "error": str(e)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Publicar TP en GitHub Classroom")
    parser.add_argument("--course", required=True, help="ID del curso (ej: leng-2026)")
    parser.add_argument("--topic", required=True, help="ID del tema (ej: 01-intro)")
    parser.add_argument("--grades", action="store_true", help="Obtener notas en vez de publicar")
    args = parser.parse_args()

    root = find_project_root(Path(__file__).parent)
    edu_config = load_yaml(root / "_edu" / "config.yaml")

    if not edu_config.get("classroom_enabled", False):
        print("ℹ️  GitHub Classroom desactivado (classroom_enabled: false en config.yaml)")
        return 0

    if not check_gh_cli():
        print("❌ GitHub CLI (gh) no está instalado.")
        print("   Instalación: https://cli.github.com/")
        print("   brew install gh  |  sudo apt install gh  |  winget install GitHub.cli")
        return 1

    if not check_gh_auth():
        print("❌ GitHub CLI no autenticado. Ejecutar: gh auth login")
        return 1

    if args.grades:
        result = fetch_grades(edu_config, args.course)
        if result["ok"]:
            print(result["grades"])
            return 0
        print(f"❌ {result['error']}")
        return 1

    topic_folder = root / "salida" / "cursadas" / args.course / "temas" / args.topic
    if not topic_folder.is_dir():
        print(f"❌ Carpeta de tema no encontrada: {topic_folder}")
        return 1

    result = publish_assignment(topic_folder, edu_config, args.course, args.topic)
    if result["ok"]:
        print(f"✅ Assignment publicado: {result['title']}")
        print(f"   Deadline: {result['deadline']}")
        if result.get("output"):
            print(f"   {result['output']}")
        return 0

    print(f"❌ {result['error']}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
