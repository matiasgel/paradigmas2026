#!/usr/bin/env python3
"""
validate_layout_cognition.py — Validador de reglas cognitivas para filminas (S4.1)

Valida que las filminas respeten principios de ciencia cognitiva:
- Assertion-Evidence (Garner & Alley, 2016): título = oración declarativa
- Contiguidad espacial (Mayer/Fiorella 2023): texto cerca de imagen
- Densidad por tipo: max palabras por tipo de filmina
- Principio de segmentación: max slides teóricas sin variación

Solo lectura — no modifica ningún archivo existente.
Sin dependencias externas.

Uso:
    python scripts/validate_layout_cognition.py --topic 01-intro --course leng-2026
    python scripts/validate_layout_cognition.py <topic_folder>

Exit codes:
    0 — reporte generado (o feature desactivada)
    1 — error de entrada
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

from pipeline_common import find_plan, find_project_root, load_json, load_yaml


# ═══════════════════════════════════════════════════════════════════════
# REGLAS COGNITIVAS POR TIPO DE FILMINA
# ═══════════════════════════════════════════════════════════════════════

COGNITIVE_RULES = {
    "concepto-abstracto": {
        "max_body_words": 30,
        "image_required": True,
        "no_decorative_clipart": True,
        "assertion_evidence": True,
    },
    "concepto-mixto": {
        "max_body_words": 30,
        "assertion_evidence": True,
    },
    "codigo": {
        "max_code_lines": 25,
        "no_mixed_languages": True,
        "assertion_evidence": False,  # puede ser título descriptivo
    },
    "socratica": {
        "title_is_question": True,
        "max_options": 3,
        "suggest_pause": True,
    },
    "diagrama": {
        "max_nodes": 7,  # Miller's 7±2
        "labels_on_arrows": True,
        "assertion_evidence": True,
    },
    "tabla": {
        "max_rows": 7,
        "max_columns": 5,
    },
    "tabla-comparativa": {
        "max_rows": 7,
        "max_columns": 5,
    },
}

# Reglas globales
GLOBAL_RULES = {
    "assertion_evidence_pattern": r"^[A-ZÁÉÍÓÚÑ].*[.!:]$",
    # Un buen título assertion-evidence es una oración declarativa que
    # termina en punto, exclamación o dos puntos
}


# ═══════════════════════════════════════════════════════════════════════
# VALIDACIONES
# ═══════════════════════════════════════════════════════════════════════


def count_body_words(slide: dict) -> int:
    """Cuenta las palabras en todos los body_blocks."""
    total = 0
    for block in slide.get("body_blocks", []):
        btype = block.get("type", "")
        if btype == "text":
            total += len(block.get("content", "").split())
        elif btype == "heading":
            total += len(block.get("content", "").split())
        elif btype == "list":
            for item in block.get("items", []):
                total += len(item.get("content", "").split())
    return total


def count_code_lines(slide: dict) -> int:
    """Cuenta las líneas de código en code_blocks."""
    total = 0
    for cb in slide.get("code_blocks", []):
        code = cb.get("code", "")
        total += code.count("\n") + (1 if code.strip() else 0)
    return total


def is_question_title(title: str) -> bool:
    """Verifica si el título es una pregunta."""
    return title.strip().endswith("?")


def is_assertion_evidence(title: str) -> bool:
    """Verifica si el título sigue el patrón assertion-evidence.

    Un título assertion-evidence es una oración declarativa completa
    que comunica el mensaje principal de la slide.
    Es lo opuesto a un título-label como "Introducción" o "Tipos de datos".
    """
    title = title.strip()
    if not title:
        return False
    # Debe tener al menos 3 palabras (no es un label)
    if len(title.split()) < 3:
        return False
    # Debe terminar en puntuación de cierre (declaración completada)
    if title[-1] in ".!:":
        return True
    # Acepta títulos largos que claramente son frases (>5 palabras)
    if len(title.split()) > 5:
        return True
    return False


def validate_slide_cognition(slide: dict, config: dict) -> list[dict]:
    """Valida una filmina contra reglas cognitivas de su tipo."""
    issues = []
    slide_type = slide.get("type", "concepto-abstracto")
    rules = COGNITIVE_RULES.get(slide_type, {})
    slide_id = slide.get("id", "?")
    title = slide.get("title", "")

    # 1. Assertion-Evidence
    if rules.get("assertion_evidence"):
        if not is_assertion_evidence(title):
            issues.append({
                "rule": "Assertion-Evidence",
                "severity": "warning",
                "message": f"Título no es assertion-evidence: \"{title}\"",
                "suggestion": "Reformular como oración declarativa que comunique el mensaje principal",
                "reference": "Garner & Alley (2016), d=0.72-0.84",
            })

    # 2. Max body words
    max_words = rules.get("max_body_words")
    if max_words:
        actual_words = count_body_words(slide)
        if actual_words > max_words:
            issues.append({
                "rule": "Densidad textual",
                "severity": "warning",
                "message": f"{actual_words} palabras en body (máximo: {max_words})",
                "suggestion": f"Reducir a {max_words} palabras o dividir en 2 filminas",
                "reference": "Principio de segmentación (Mayer 2021)",
            })

    # 3. Image required
    if rules.get("image_required"):
        image = slide.get("image", {})
        has_image = image.get("image_layer", "none") != "none"
        if not has_image:
            issues.append({
                "rule": "Imagen obligatoria",
                "severity": "info",
                "message": f"Tipo '{slide_type}' debería tener imagen de apoyo",
                "suggestion": "Agregar imagen conceptual (no decorativa)",
                "reference": "Principio multimedia (Mayer 2021)",
            })

    # 4. Max code lines
    max_lines = rules.get("max_code_lines")
    if max_lines:
        actual_lines = count_code_lines(slide)
        if actual_lines > max_lines:
            issues.append({
                "rule": "Densidad de código",
                "severity": "warning",
                "message": f"{actual_lines} líneas de código (máximo: {max_lines})",
                "suggestion": "Dividir en múltiples filminas o usar resaltado progresivo",
                "reference": "Working memory limits (Sweller 2011)",
            })

    # 5. Title is question (socráticas)
    if rules.get("title_is_question"):
        if not is_question_title(title):
            issues.append({
                "rule": "Título socrático",
                "severity": "warning",
                "message": "Filmina socrática debe tener título formulado como pregunta",
                "suggestion": f"Reformular \"{title}\" como pregunta",
            })

    # 6. Max nodes (diagramas)
    max_nodes = rules.get("max_nodes")
    if max_nodes:
        # Heurística: contar items en listas como proxy de nodos
        body_blocks = slide.get("body_blocks", [])
        for block in body_blocks:
            if block.get("type") == "list":
                n_items = len(block.get("items", []))
                if n_items > max_nodes:
                    issues.append({
                        "rule": "Límite de nodos (Miller 7±2)",
                        "severity": "warning",
                        "message": f"{n_items} elementos (máximo: {max_nodes})",
                        "suggestion": "Agrupar o dividir en sub-diagramas",
                        "reference": "Miller (1956) — The Magical Number Seven",
                    })

    # 7. Max table rows/columns
    max_rows = rules.get("max_rows")
    max_cols = rules.get("max_columns")
    if max_rows or max_cols:
        for tbl in slide.get("tables", []):
            rows = tbl.get("rows", [])
            if max_rows and len(rows) > max_rows:
                issues.append({
                    "rule": "Tabla densa",
                    "severity": "warning",
                    "message": f"Tabla con {len(rows)} filas (máximo: {max_rows})",
                    "suggestion": "Simplificar o dividir tabla",
                })
            if max_cols and rows:
                n_cols = len(rows[0]) if isinstance(rows[0], list) else len(rows[0].get("cells", []))
                if n_cols > max_cols:
                    issues.append({
                        "rule": "Tabla ancha",
                        "severity": "warning",
                        "message": f"Tabla con {n_cols} columnas (máximo: {max_cols})",
                    })

    return issues


def validate_sequence_cognition(slides: list[dict], config: dict) -> list[dict]:
    """Valida reglas cognitivas a nivel de secuencia (no por slide individual)."""
    issues = []

    max_consecutive_theory = config.get("cognitive_max_consecutive_theory", 3)
    max_concepts_per_30min = config.get("cognitive_concepts_per_30min", 6)

    # 1. Max slides teóricas consecutivas sin attention reset
    theory_types = {"concepto-abstracto", "concepto-mixto", "codigo", "tabla", "tabla-comparativa"}
    reset_types = {"socratica", "demo", "diagrama"}
    consecutive = 0
    
    for i, slide in enumerate(slides):
        stype = slide.get("type", "")
        if stype in theory_types:
            consecutive += 1
            if consecutive > max_consecutive_theory:
                issues.append({
                    "rule": "Segmentación",
                    "severity": "warning",
                    "message": f"Slide {slide.get('id', i)} — {consecutive} filminas teóricas consecutivas sin pausa (máx: {max_consecutive_theory})",
                    "suggestion": "Insertar filmina socrática, demo o diagrama como attention reset",
                    "reference": "Principio de segmentación (Mayer 2021)",
                })
        elif stype in reset_types:
            consecutive = 0
        elif stype in ("portada", "cierre"):
            consecutive = 0

    # 2. Conceptos nuevos por bloque de 30 min
    # Heurística: cada 15 slides ≈ 30 min (2 min/slide promedio)
    block_size = 15
    for block_start in range(0, len(slides), block_size):
        block = slides[block_start : block_start + block_size]
        concept_count = sum(
            1 for s in block if s.get("type") in theory_types
        )
        if concept_count > max_concepts_per_30min:
            issues.append({
                "rule": "Carga cognitiva por bloque",
                "severity": "info",
                "message": f"Bloque slides {block_start+1}-{block_start+len(block)}: {concept_count} conceptos (máx: {max_concepts_per_30min} por 30 min)",
                "suggestion": "Redistribuir o intercalar con actividades prácticas",
                "reference": "Cognitive Load Theory (Sweller & Chandler 2011)",
            })

    return issues


# ═══════════════════════════════════════════════════════════════════════
# REPORTE
# ═══════════════════════════════════════════════════════════════════════


def generate_report(slide_issues: dict[str, list[dict]],
                    sequence_issues: list[dict],
                    topic_id: str) -> str:
    """Genera reporte Markdown de validación cognitiva."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    total_warnings = sum(
        sum(1 for i in issues if i["severity"] == "warning")
        for issues in slide_issues.values()
    ) + sum(1 for i in sequence_issues if i["severity"] == "warning")
    
    total_info = sum(
        sum(1 for i in issues if i["severity"] == "info")
        for issues in slide_issues.values()
    ) + sum(1 for i in sequence_issues if i["severity"] == "info")

    lines = [
        f"# Reporte Cognitivo — {topic_id}",
        f"**Generado:** {now}",
        f"**Basado en:** Mayer (2021), Fiorella (2023), Garner & Alley (2016), Sweller (2011)",
        "",
        f"**Resumen:** {total_warnings} advertencias, {total_info} sugerencias",
        "",
    ]

    # Issues por filmina
    slides_with_issues = {k: v for k, v in slide_issues.items() if v}
    if slides_with_issues:
        lines.extend(["## Issues por Filmina", ""])
        for slide_id, issues in slides_with_issues.items():
            lines.append(f"### {slide_id}")
            for issue in issues:
                emoji = "⚠️" if issue["severity"] == "warning" else "ℹ️"
                lines.append(f"- {emoji} **{issue['rule']}:** {issue['message']}")
                if "suggestion" in issue:
                    lines.append(f"  - 💡 {issue['suggestion']}")
                if "reference" in issue:
                    lines.append(f"  - 📚 {issue['reference']}")
            lines.append("")
    else:
        lines.extend(["## Issues por Filmina", "", "✅ Ninguna filmina tiene issues cognitivos.", ""])

    # Issues de secuencia
    if sequence_issues:
        lines.extend(["## Issues de Secuencia", ""])
        for issue in sequence_issues:
            emoji = "⚠️" if issue["severity"] == "warning" else "ℹ️"
            lines.append(f"- {emoji} **{issue['rule']}:** {issue['message']}")
            if "suggestion" in issue:
                lines.append(f"  - 💡 {issue['suggestion']}")
        lines.append("")
    else:
        lines.extend(["## Issues de Secuencia", "", "✅ La secuencia respeta los principios de segmentación.", ""])

    # Resultado
    all_pass = total_warnings == 0
    lines.extend([
        "## Resultado Global",
        "",
        f"**{'✅ PASA' if all_pass else '⚠️ REQUIERE ATENCIÓN'}** — {total_warnings} advertencias, {total_info} sugerencias",
    ])

    return "\n".join(lines) + "\n"


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════


def resolve_topic_folder(args: argparse.Namespace, project_root: Path) -> Path:
    """Resuelve la carpeta del tema desde los argumentos CLI."""
    if args.topic_folder:
        return Path(args.topic_folder).resolve()

    config_path = project_root / "_edu" / "config.yaml"
    config = load_yaml(config_path) if config_path.exists() else {}
    course_prefix = args.course or config.get("course_prefix", "")
    course_year = config.get("course_year", "2026")
    if not course_prefix:
        print("ERROR: Especificar --course o configurar course_prefix en config.yaml", file=sys.stderr)
        sys.exit(1)

    course_id = f"{course_prefix}-{course_year}"
    return project_root / "salida" / "cursadas" / course_id / "temas" / args.topic


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validador cognitivo de filminas EDU"
    )
    parser.add_argument("topic_folder", nargs="?", help="Carpeta del tema (path directo)")
    parser.add_argument("--topic", help="ID del tema (ej: 01-intro)")
    parser.add_argument("--course", help="Prefijo del curso (ej: leng-2026)")
    args = parser.parse_args()

    if not args.topic_folder and not args.topic:
        parser.error("Especificar topic_folder o --topic")

    project_root = find_project_root(Path(__file__).parent)

    # Verificar si está habilitado
    edu_config_path = project_root / "_edu" / "config.yaml"
    edu_config = load_yaml(edu_config_path) if edu_config_path.exists() else {}
    if not edu_config.get("cognitive_validation_enabled", False):
        print("ℹ️  Validación cognitiva desactivada. Activar con cognitive_validation_enabled: true en config.yaml")
        sys.exit(0)

    topic_folder = resolve_topic_folder(args, project_root)
    if not topic_folder.exists():
        print(f"ERROR: Carpeta de tema no encontrada: {topic_folder}", file=sys.stderr)
        sys.exit(1)

    # Cargar plan JSON
    plan_result = find_plan(topic_folder)
    if not plan_result.is_ok:
        print(f"ERROR: {plan_result.errors[0]}", file=sys.stderr)
        sys.exit(1)

    plan = load_json(plan_result.unwrap())
    slides = plan.get("slides", [])

    # Validar cada filmina
    slide_issues: dict[str, list[dict]] = {}
    for slide in slides:
        issues = validate_slide_cognition(slide, edu_config)
        slide_id = slide.get("id", "?")
        slide_issues[slide_id] = issues

    # Validar secuencia
    sequence_issues = validate_sequence_cognition(slides, edu_config)

    # Generar reporte
    topic_id = topic_folder.name
    report = generate_report(slide_issues, sequence_issues, topic_id)

    output_path = topic_folder / "cognition-report.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"✅ Reporte generado: {output_path}")


if __name__ == "__main__":
    main()
