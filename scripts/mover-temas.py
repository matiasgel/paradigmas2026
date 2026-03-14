#!/usr/bin/env python3
"""mover-temas.py — Migra carpetas de temas desde la ubicación incorrecta
                    (raíz del proyecto) al año de cursada correcto.

Ruta correcta: salida/cursadas/{course_year}/temas/

Lee course_year desde _edu/config.yaml. Si no está configurado, usa el año actual.

Uso:
    python scripts/mover-temas.py [opciones]

Opciones:
    --dry-run        Solo muestra qué haría, sin mover nada
    --source RUTA    Carpeta origen (default: temas/)
    --year AÑO       Año de cursada (default: lee de _edu/config.yaml)
    --force          No pide confirmación ante conflictos

Ejemplos:
    python scripts/mover-temas.py --dry-run
    python scripts/mover-temas.py
    python scripts/mover-temas.py --source temas/ --year 2026
"""

import argparse
import os
import re
import shutil
import sys
from datetime import date
from pathlib import Path


def find_project_root(start: Path) -> tuple[Path, Path]:
    """Retorna (project_root, config_dir).

    - project_root: raíz donde viven temas/ y salida/
    - config_dir:   directorio que contiene _edu/config.yaml

    Busca subiendo la jerarquía. Como fallback, detecta el patrón del
    proyecto paradigmas2026 donde la config vive en salida/edu-standalone/.
    """
    for candidate in [start, *start.parents]:
        if (candidate / "_edu" / "config.yaml").exists():
            return candidate, candidate

    # Fallback: config dentro de salida/edu-standalone (proyecto principal BMAD)
    for candidate in [start, *start.parents]:
        edu_path = candidate / "salida" / "edu-standalone"
        if (edu_path / "_edu" / "config.yaml").exists():
            # project_root es el proyecto principal, config está en edu-standalone
            return candidate, edu_path

    return start, start


def read_config_value(config_path: Path, key: str) -> str:
    """Lee un valor simple de config.yaml sin dependencia en PyYAML."""
    try:
        text = config_path.read_text(encoding="utf-8")
        # Busca líneas como:  key: "value"  o  key: value
        pattern = rf'^{re.escape(key)}\s*:\s*["\']?([^"\'#\n]+)["\']?'
        match = re.search(pattern, text, re.MULTILINE)
        if match:
            return match.group(1).strip()
    except OSError:
        pass
    return ""


def resolve_topics_folder(project_root: Path, year: str) -> Path:
    """
    Construye la ruta destino: salida/cursadas/{year}/temas/
    Respeta la variable chain definida en config.yaml.
    """
    return project_root / "salida" / "cursadas" / year / "temas"


def get_course_year(config_dir: Path, override: str | None) -> str:
    if override:
        return override
    config_path = config_dir / "_edu" / "config.yaml"
    year = read_config_value(config_path, "course_year")
    if year:
        return year
    fallback = str(date.today().year)
    print(f"ℹ️  course_year no encontrado en _edu/config.yaml, usando año actual: {fallback}")
    return fallback


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Migra temas/ a salida/cursadas/{año}/temas/"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Solo muestra qué haría, sin mover nada"
    )
    parser.add_argument(
        "--source", default="temas",
        help="Carpeta origen relativa al proyecto (default: temas)"
    )
    parser.add_argument(
        "--year", default=None,
        help="Año de cursada (default: lee de _edu/config.yaml)"
    )
    parser.add_argument(
        "--force", action="store_true",
        help="No pide confirmación ante conflictos — saltea carpetas que ya existen"
    )
    args = parser.parse_args()

    project_root, config_dir = find_project_root(Path.cwd())
    source_dir = (project_root / args.source).resolve()
    year = get_course_year(config_dir, args.year)
    dest_dir = resolve_topics_folder(project_root, year)

    print()
    print(f"{'[DRY RUN] ' if args.dry_run else ''}Migración de temas")
    print(f"  Proyecto:  {project_root}")
    print(f"  Origen:    {source_dir}")
    print(f"  Destino:   {dest_dir}")
    print()

    if not source_dir.exists():
        print(f"✅ Carpeta origen no encontrada: {source_dir.relative_to(project_root)}")
        print("   No hay nada para migrar.")
        return 0

    topic_dirs = sorted(d for d in source_dir.iterdir() if d.is_dir())
    topic_files = [f for f in source_dir.iterdir() if f.is_file()]

    if not topic_dirs and not topic_files:
        print(f"ℹ️  La carpeta {args.source}/ está vacía — nada para migrar.")
        return 0

    # Mostrar plan
    conflicts = []
    to_move = []
    for t in topic_dirs:
        dest = dest_dir / t.name
        if dest.exists():
            conflicts.append(t)
            print(f"  ⚠️  CONFLICTO   {t.name}  →  ya existe en destino")
        else:
            to_move.append(t)
            print(f"  📦 mover       {t.name}  →  {dest.relative_to(project_root)}")

    if topic_files:
        print()
        print(f"  ℹ️  {len(topic_files)} archivo(s) suelto(s) en {args.source}/ (no se mueven — solo carpetas de temas)")

    print()

    if not to_move and not conflicts:
        print("ℹ️  Sin carpetas de temas que procesar.")
        return 0

    if args.dry_run:
        print("(modo --dry-run: nada fue movido)")
        return 0

    # Pedir confirmación si hay conflictos y no es --force
    if conflicts and not args.force:
        print(f"⚠️  {len(conflicts)} carpeta(s) ya existe(n) en el destino y serán salteadas.")
        resp = input("  ¿Continuar moviendo las carpetas sin conflicto? [s/N]: ").strip().lower()
        if resp != "s":
            print("Operación cancelada.")
            return 1

    # Crear directorio destino
    if to_move:
        dest_dir.mkdir(parents=True, exist_ok=True)

    moved = 0
    skipped = 0
    for topic in topic_dirs:
        dest = dest_dir / topic.name
        if dest.exists():
            print(f"  ⏭️  Salteado (ya existe en destino): {topic.name}")
            skipped += 1
            continue
        shutil.move(str(topic), str(dest))
        print(f"  ✅ Movido: {topic.name}")
        moved += 1

    # Limpiar carpeta origen si quedó vacía
    remaining = list(source_dir.iterdir())
    if not remaining:
        source_dir.rmdir()
        print(f"\n  🗑️  Carpeta origen eliminada (vacía): {source_dir.relative_to(project_root)}/")
    elif moved > 0:
        print(f"\n  ℹ️  Carpeta origen conservada (tiene contenido restante): {source_dir.relative_to(project_root)}/")

    print(f"\n✅ Listo: {moved} carpeta(s) movida(s) a {dest_dir.relative_to(project_root)}/")
    if skipped:
        print(f"   {skipped} carpeta(s) salteada(s) por conflicto")
    return 0


if __name__ == "__main__":
    sys.exit(main())
