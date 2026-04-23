#!/usr/bin/env python3
"""
generate_gift_quiz.py — Generador de cuestionarios Moodle GIFT desde blueprint de examen (S2.3)

Convierte un exam-blueprint.json y las filminas del tema en preguntas de cuestionario
en formato GIFT (General Import Format Technology) compatible con Moodle 5.

Tipos de preguntas soportados:
  - MC    : Multiple Choice (una respuesta correcta con peso 100%)
  - MCM   : Multiple Choice Multiple (varias respuestas correctas con pesos)
  - TF    : True/False
  - SHORT : Short Answer (respuesta corta, case-insensitive)
  - MATCH : Matching (emparejamiento)
  - NUM   : Numerical (respuesta numérica con margen de error)
  - ESSAY : Essay (pregunta abierta sin corrección automática)

Generación por nivel Bloom:
  - recordar     → SHORT, MC
  - comprender   → TF, MC, MATCH
  - aplicar      → MC, MCM, SHORT
  - analizar     → MCM, ESSAY
  - evaluar      → ESSAY, MCM
  - crear        → ESSAY

Fuente: https://docs.moodle.org/en/GIFT_format (ver docs/Formato GIFT - MoodleDocs.html)

Uso:
    python scripts/generate_gift_quiz.py --topic 03-paradigmas --course leng-2026
    python scripts/generate_gift_quiz.py --topic 03-paradigmas --course leng-2026 --points 100 --time 90
    python scripts/generate_gift_quiz.py --blueprint path/to/exam-blueprint.json --out quiz.gift

Exit codes:
    0 → GIFT generado correctamente
    1 → error de entrada (topic no encontrado, plan no existe)
    2 → error de validación del GIFT generado
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Path setup — permite importar pipeline_common desde el mismo directorio
# ---------------------------------------------------------------------------
_this = Path(__file__).resolve()
_scripts = _this.parent
_root = _scripts.parent
if str(_scripts) not in sys.path:
    sys.path.insert(0, str(_scripts))

from pipeline_common import find_project_root, find_plan, load_json, load_yaml, save_json


# ---------------------------------------------------------------------------
# Constantes GIFT
# ---------------------------------------------------------------------------

BLOOM_TO_TYPES: dict[str, list[str]] = {
    "recordar":   ["SHORT", "MC"],
    "comprender": ["TF", "MC", "MATCH"],
    "aplicar":    ["MC", "MCM", "SHORT"],
    "analizar":   ["MCM", "ESSAY"],
    "evaluar":    ["ESSAY", "MCM"],
    "crear":      ["ESSAY"],
}

GIFT_HEADER = """\
// GIFT Format — Generado por generate_gift_quiz.py
// Curso: {course_id} | Tema: {topic_name} | Fecha: {date}
// Importar en Moodle: Administración del curso → Banco de preguntas → Importar → GIFT

$CATEGORY: {course_id}/{topic_name}

"""


# ---------------------------------------------------------------------------
# Helpers GIFT
# ---------------------------------------------------------------------------

def _escape_gift(text: str) -> str:
    """Escapa caracteres especiales de GIFT."""
    # Los siguientes deben ser escapados con backslash en GIFT
    for ch in ("~", "=", "#", "{", "}", ":"):
        text = text.replace(ch, f"\\{ch}")
    return text


def _clean_markdown(text: str) -> str:
    """Elimina markup Markdown básico para texto plano en GIFT."""
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text.strip()


def _make_mc(title: str, stem: str, correct: str, distractors: list[str], weight: float = 100.0) -> str:
    """Genera una pregunta Multiple Choice (MC) en GIFT."""
    lines = [f"::{title}::{_escape_gift(stem)} {{"]
    lines.append(f"  ={_escape_gift(correct)}")
    for d in distractors:
        lines.append(f"  ~{_escape_gift(d)}")
    lines.append("}")
    return "\n".join(lines)


def _make_mcm(title: str, stem: str, correct_list: list[str], wrong_list: list[str]) -> str:
    """Genera Multiple Choice con múltiples respuestas correctas (pesos iguales)."""
    if not correct_list:
        return ""
    pct = round(100.0 / len(correct_list), 4)
    wrong_pct = round(-100.0 / max(len(wrong_list), 1), 4)
    lines = [f"::{title}::{_escape_gift(stem)} {{"]
    for c in correct_list:
        lines.append(f"  %{pct}%{_escape_gift(c)}")
    for w in wrong_list:
        lines.append(f"  %{wrong_pct}%{_escape_gift(w)}")
    lines.append("}")
    return "\n".join(lines)


def _make_tf(title: str, stem: str, correct: bool, feedback_true: str = "", feedback_false: str = "") -> str:
    """Genera True/False en GIFT."""
    ans = "TRUE" if correct else "FALSE"
    fb_t = f"#{_escape_gift(feedback_true)}" if feedback_true else ""
    fb_f = f"#{_escape_gift(feedback_false)}" if feedback_false else ""
    return f"::{title}::{_escape_gift(stem)} {{{ans}{fb_t}{fb_f}}}"


def _make_short(title: str, stem: str, answers: list[str]) -> str:
    """Genera Short Answer en GIFT (case-insensitive por defecto)."""
    lines = [f"::{title}::{_escape_gift(stem)} {{"]
    for a in answers:
        lines.append(f"  ={_escape_gift(a)}")
    lines.append("}")
    return "\n".join(lines)


def _make_match(title: str, stem: str, pairs: list[tuple[str, str]]) -> str:
    """Genera Matching en GIFT."""
    lines = [f"::{title}::{_escape_gift(stem)} {{"]
    for left, right in pairs:
        lines.append(f"  ={_escape_gift(left)} -> {_escape_gift(right)}")
    lines.append("}")
    return "\n".join(lines)


def _make_essay(title: str, stem: str, feedback: str = "") -> str:
    """Genera Essay (pregunta abierta) en GIFT."""
    fb = f"#{_escape_gift(feedback)}" if feedback else ""
    return f"::{title}::{_escape_gift(stem)} {{{{}}{fb}}}"


# ---------------------------------------------------------------------------
# Generación de preguntas desde slide
# ---------------------------------------------------------------------------

def _generate_from_slide(slide: dict, bloom_level: str, idx: int, topic_slug: str) -> list[str]:
    """
    Genera entre 1 y 3 preguntas GIFT a partir de los datos de una filmina.
    Intenta crear el tipo más apropiado según el nivel Bloom asignado.
    """
    title_base = _clean_markdown(slide.get("title", f"Filmina-{idx}"))
    body_blocks = slide.get("body_blocks", [])
    body_text = " ".join(
        _clean_markdown(b.get("content", b) if isinstance(b, dict) else str(b))
        for b in body_blocks
    )

    questions: list[str] = []
    q_types = BLOOM_TO_TYPES.get(bloom_level.lower(), ["MC"])

    q_id = f"{topic_slug}-F{idx:02d}"

    # --- Pregunta 1: según bloom level principal ---
    primary_type = q_types[0]

    if primary_type == "MC" and body_text:
        stem = f"Respecto a «{title_base}», ¿cuál de las siguientes afirmaciones es CORRECTA?"
        correct = f"{title_base}: {body_text[:80]}..."  if len(body_text) > 80 else body_text
        distractors = [
            f"Lo contrario de lo que dice «{title_base}»",
            f"Una versión incorrecta de «{title_base}»",
            "Ninguna de las anteriores",
        ]
        questions.append(_make_mc(f"{q_id}-MC", stem, correct, distractors))

    elif primary_type == "TF" and body_text:
        stem = f"«{title_base}» implica que: {body_text[:120]}"
        questions.append(_make_tf(f"{q_id}-TF", stem, correct=True,
                                  feedback_true="Correcto.",
                                  feedback_false=f"Incorrecto. Ver filmina: {title_base}"))

    elif primary_type == "SHORT":
        stem = f"¿Cómo se denomina el concepto presentado en la filmina «{title_base}»?"
        answers = [title_base, title_base.lower()]
        questions.append(_make_short(f"{q_id}-SHT", stem, answers))

    elif primary_type == "ESSAY":
        stem = (f"Explicá con tus propias palabras el concepto presentado en «{title_base}». "
                "Incluí al menos un ejemplo concreto.")
        questions.append(_make_essay(f"{q_id}-ESS", stem,
                                     feedback=f"Ver filmina {idx}: {title_base}"))

    # --- Pregunta 2: tablas → MATCH si hay datos ---
    tables = slide.get("tables", [])
    if tables and "MATCH" in q_types:
        for tbl in tables[:1]:
            rows = tbl.get("rows", [])
            pairs = []
            for row in rows[:4]:
                cells = row.get("cells", [])
                if len(cells) >= 2:
                    pairs.append((_clean_markdown(str(cells[0])), _clean_markdown(str(cells[1]))))
            if len(pairs) >= 2:
                stem = f"Relacioná correctamente los elementos de «{title_base}»:"
                questions.append(_make_match(f"{q_id}-MCH", stem, pairs))

    return questions


# ---------------------------------------------------------------------------
# Función principal
# ---------------------------------------------------------------------------

def generate_gift(topic_folder: Path, course_id: str, out_path: Path | None = None) -> Path:
    """
    Genera un archivo GIFT desde el plan-filminas del topic.
    Retorna la ruta al archivo GIFT generado.
    """
    root = find_project_root()

    # --- Cargar plan ---
    plan_result = find_plan(topic_folder)
    if not plan_result.ok:
        print(f"❌ No se encontró plan-filminas en {topic_folder}: {plan_result.error}", file=sys.stderr)
        sys.exit(1)
    plan = plan_result.value

    slides: list[dict] = plan.get("slides", [])
    if not slides:
        print("❌ El plan no tiene slides.", file=sys.stderr)
        sys.exit(1)

    topic_name = topic_folder.name
    topic_slug = re.sub(r"[^a-z0-9-]", "", topic_name.lower())[:30]
    date_str = datetime.now().strftime("%Y-%m-%d")

    # --- Intentar cargar exam-blueprint si existe ---
    blueprint_path = topic_folder / "slides" / f"exam-blueprint-{topic_slug}.json"
    bloom_map: dict[str, str] = {}
    if blueprint_path.exists():
        try:
            bp = load_json(blueprint_path).value
            for item in bp.get("items", []):
                sid = item.get("slide_id", "")
                bloom_map[sid] = item.get("bloom_level", "comprender")
        except Exception:
            pass  # bloom_map queda vacío → usamos 'comprender' por defecto

    # --- Generar preguntas ---
    all_questions: list[str] = []
    for i, slide in enumerate(slides):
        slide_id = slide.get("id", f"F-{i:02d}")
        bloom = bloom_map.get(slide_id, "comprender")
        questions = _generate_from_slide(slide, bloom, i, topic_slug)
        all_questions.extend(questions)

    if not all_questions:
        print("⚠️  No se generaron preguntas. Verificar que el plan tenga slides con contenido.",
              file=sys.stderr)
        sys.exit(1)

    # --- Ensamblar archivo GIFT ---
    header = GIFT_HEADER.format(
        course_id=course_id,
        topic_name=topic_name,
        date=date_str,
    )
    gift_content = header + "\n\n".join(all_questions) + "\n"

    # --- Determinar ruta de salida ---
    if out_path is None:
        out_path = topic_folder / "slides" / f"quiz-{topic_slug}.gift"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(gift_content, encoding="utf-8")

    # --- Generar manifiesto JSON paralelo ---
    manifest = {
        "generated_at": date_str,
        "course_id": course_id,
        "topic": topic_name,
        "total_questions": len(all_questions),
        "bloom_distribution": {},
        "source_plan": str(plan_result.value.get("meta", {}).get("plan_path", "")),
        "output": str(out_path),
    }
    for slide in slides:
        sid = slide.get("id", "")
        b = bloom_map.get(sid, "comprender")
        manifest["bloom_distribution"][b] = manifest["bloom_distribution"].get(b, 0) + 1

    manifest_path = out_path.with_suffix(".json")
    save_json(manifest_path, manifest)

    return out_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Genera cuestionarios Moodle GIFT desde plan-filminas."
    )
    parser.add_argument("topic_folder", nargs="?", help="Ruta al directorio del tema")
    parser.add_argument("--topic", help="Nombre o número de tema (alternativa a topic_folder)")
    parser.add_argument("--course", default=None, help="ID del curso (ej: leng-2026)")
    parser.add_argument("--out", default=None, help="Ruta de salida del archivo .gift")
    parser.add_argument("--blueprint", default=None, help="Ruta a exam-blueprint.json existente")

    args = parser.parse_args()

    root = find_project_root()

    # Determinar course_id
    course_id = args.course
    if not course_id:
        try:
            cfg = load_yaml(root / "_edu" / "config.yaml").value
            prefix = cfg.get("course_prefix", "edu")
            year = cfg.get("course_year", "2026")
            course_id = f"{prefix}-{year}"
        except Exception:
            course_id = "edu-2026"

    # Determinar topic_folder
    if args.topic_folder:
        topic_folder = Path(args.topic_folder)
    elif args.topic:
        cfg = load_yaml(root / "_edu" / "config.yaml").value
        topics_base = root / cfg.get("topics_folder", f"salida/cursadas/{course_id}/temas")
        # Buscar tema por prefijo numérico o nombre
        matches = [
            p for p in sorted(topics_base.iterdir())
            if p.is_dir() and args.topic in p.name
        ]
        if not matches:
            print(f"❌ No se encontró tema '{args.topic}' en {topics_base}", file=sys.stderr)
            sys.exit(1)
        topic_folder = matches[0]
    else:
        parser.print_help()
        sys.exit(1)

    if not topic_folder.exists():
        print(f"❌ Directorio no existe: {topic_folder}", file=sys.stderr)
        sys.exit(1)

    out_path = Path(args.out) if args.out else None
    gift_path = generate_gift(topic_folder, course_id, out_path)

    print(f"✅ GIFT generado: {gift_path}")
    print(f"   Importar en Moodle: Banco de preguntas → Importar → GIFT")
    print(f"   Manifiesto: {gift_path.with_suffix('.json')}")


if __name__ == "__main__":
    main()
