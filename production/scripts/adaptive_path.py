#!/usr/bin/env python3
"""
adaptive_path.py ÔÇö Motor de recomendaci├│n de rutas de estudio (S5.2)

Genera rutas de estudio personalizadas basadas en scores del alumno.
Graceful degradation: sin datos genera solo ruta-estandar.md.

Uso:
    python scripts/adaptive_path.py --course leng-2026 --topic 03-memoria --student "Garc├¡a, M."
    python scripts/adaptive_path.py --course leng-2026 --topic 03-memoria

Exit codes:
    0 ÔÇö rutas generadas
    1 ÔÇö error de entrada
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

from pipeline_common import find_project_root, load_yaml


# Umbrales de clasificaci├│n por percentil
THRESHOLD_ADVANCED = 80  # ÔëÑ80% ÔåÆ ruta avanzada
THRESHOLD_STANDARD = 50  # ÔëÑ50% ÔåÆ ruta est├índar
# <50% ÔåÆ ruta de refuerzo


def get_student_score(db_path: Path, course_id: str, student_id: str) -> float | None:
    """Obtiene el promedio del alumno en el curso."""
    if not db_path.exists():
        return None
    conn = sqlite3.connect(str(db_path))
    try:
        row = conn.execute(
            "SELECT AVG(score * 100.0 / max_score) FROM grades WHERE course_id = ? AND student_id = ?",
            (course_id, student_id),
        ).fetchone()
        return row[0] if row and row[0] is not None else None
    except sqlite3.OperationalError:
        return None
    finally:
        conn.close()


def classify_level(score: float | None) -> str:
    """Clasifica el nivel del alumno."""
    if score is None:
        return "estandar"
    if score >= THRESHOLD_ADVANCED:
        return "avanzada"
    if score >= THRESHOLD_STANDARD:
        return "estandar"
    return "refuerzo"


def generate_route(
    level: str,
    topic_id: str,
    course_id: str,
    student_name: str | None,
    topic_folder: Path,
) -> Path:
    """Genera la ruta de estudio Markdown para el nivel dado."""
    now = datetime.now().strftime("%Y-%m-%d")
    header = f"# Ruta de estudio ÔÇö {topic_id}"
    if student_name:
        header += f" ÔÇö {student_name}"

    content_map = {
        "avanzada": {
            "emoji": "­ƒÜÇ",
            "desc": "Ruta para alumnos con dominio s├│lido de las bases",
            "sections": [
                "## Actividades\n",
                "1. **Proyecto aplicado** ÔÇö Resolver un problema real usando los conceptos del tema",
                "2. **Lectura avanzada** ÔÇö Papers de referencia y extensiones del tema",
                "3. **Mentoring** ÔÇö Ayudar a compa├▒eros con la ruta est├índar (aprendizaje por ense├▒anza)",
                "4. **Exploraci├│n** ÔÇö Investigar conexiones con otros temas del curso",
            ],
        },
        "estandar": {
            "emoji": "­ƒôÜ",
            "desc": "Ruta principal del curso",
            "sections": [
                "## Actividades\n",
                "1. **Lectura gu├¡a de estudio** ÔÇö Revisar `guia-estudio.md` completa",
                "2. **Pr├íctica** ÔÇö Completar el TP asociado al tema",
                "3. **Autoevaluaci├│n** ÔÇö Responder las preguntas del final de la gu├¡a",
                "4. **Repaso** ÔÇö Revisar filminas antes de la siguiente clase",
            ],
        },
        "refuerzo": {
            "emoji": "­ƒöº",
            "desc": "Ruta de refuerzo con soporte adicional",
            "sections": [
                "## Actividades\n",
                "1. **Prerequisitos** ÔÇö Verificar comprensi├│n de temas anteriores",
                "2. **Lectura guiada** ÔÇö Leer `guia-estudio.md` secci├│n por secci├│n con pausa",
                "3. **Ejercicios b├ísicos** ÔÇö Resolver ejercicios de baja complejidad primero",
                "4. **Tutor├¡a** ÔÇö Agendar consulta con el docente o ayudante",
                "5. **Repaso espaciado** ÔÇö Programar 2 sesiones de repaso adicionales",
            ],
        },
    }

    info = content_map[level]
    lines = [
        header,
        f"\n> {info['emoji']} {info['desc']}",
        f"> Nivel: **{level}** | Generado: {now}\n",
        *info["sections"],
        "",
        "## Recursos\n",
        f"- Gu├¡a de estudio: `salida/cursadas/{course_id}/temas/{topic_id}/guia-estudio.md`",
        f"- Filminas: `salida/cursadas/{course_id}/temas/{topic_id}/filminas.md`",
        f"- TP: `salida/cursadas/{course_id}/temas/{topic_id}/tp.md`",
    ]

    output_dir = topic_folder / "adaptive"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"ruta-{level}.md"
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Adaptive Learning Path Generator")
    parser.add_argument("--course", required=True, help="ID del curso")
    parser.add_argument("--topic", required=True, help="ID del tema")
    parser.add_argument("--student", default=None, help="ID o nombre del alumno")
    args = parser.parse_args()

    root = find_project_root(Path(__file__).parent)
    topic_folder = root / "salida" / "cursadas" / args.course / "temas" / args.topic

    if not topic_folder.is_dir():
        topic_folder.mkdir(parents=True, exist_ok=True)

    db_path = root / "_edu-memory" / "memory.db"

    if args.student:
        score = get_student_score(db_path, args.course, args.student)
        level = classify_level(score)
        path = generate_route(level, args.topic, args.course, args.student, topic_folder)
        score_str = f"{score:.0f}%" if score is not None else "sin datos"
        print(f"Ô£à Ruta {level} generada ({score_str}): {path}")
    else:
        # Sin alumno espec├¡fico, generar las 3 rutas
        for level in ("avanzada", "estandar", "refuerzo"):
            path = generate_route(level, args.topic, args.course, None, topic_folder)
            print(f"Ô£à Ruta {level}: {path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())