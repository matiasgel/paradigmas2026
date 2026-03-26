#!/usr/bin/env python3
"""
validate_plan.py — Validador de plan-filminas YAML

Valida que el plan YAML de un tema cumpla el contrato canónico antes
de ejecutar el pipeline de generación y publicación de filminas.

Uso:
    python scripts/validate_plan.py salida/cursadas/2026/temas/02-sintaxis-semantica

Exit codes:
    0 — plan válido
    1 — errores encontrados (muestra lista detallada)
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from slides_pipeline import load_pipeline_runtime

# Estrategias de imagen permitidas
ALLOWED_IMAGE_STRATEGIES = {"background", "content", "gemini", "none"}


def find_project_root(start: Path) -> Path:
    cur = start.resolve()
    while True:
        if (cur / ".git").exists() or (cur / "_edu").exists():
            return cur
        if cur == cur.parent:
            break
        cur = cur.parent
    raise FileNotFoundError("No se encontró la raíz del proyecto.")


def load_config(project_root: Path) -> dict:
    config_path = project_root / "_edu" / "slides-config.yaml"
    if config_path.exists():
        with config_path.open(encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}


def pipeline_contract(project_root: Path, topic_folder: Path, config: dict) -> tuple[set[str], dict[str, set[str]]]:
    runtime = load_pipeline_runtime(project_root, config, topic_folder)
    slide_types = runtime.get("slide_types", {}) or {}
    allowed_types = set(slide_types.keys())
    allowed_layout_zones = {
        "title": set(),
        "body": set(),
        "image": set(),
        "code": set(),
        "table": set(),
    }
    for spec in slide_types.values():
        layout = spec.get("layout", {}) or {}
        for zone, allowed in allowed_layout_zones.items():
            value = layout.get(zone)
            if value is not None:
                allowed.add(str(value))
    for allowed in allowed_layout_zones.values():
        allowed.add("none")
    return allowed_types, allowed_layout_zones


def validate_plan(topic_folder: Path) -> list[str]:
    """Valida el plan YAML y retorna lista de errores (vacía = válido)."""
    project_root = find_project_root(topic_folder)
    config = load_config(project_root)
    allowed_types, allowed_layout_zones = pipeline_contract(project_root, topic_folder, config)

    # Encontrar el plan YAML
    slides_dir = topic_folder / "slides"
    topic_id = topic_folder.name
    plan_path = slides_dir / f"plan-filminas-{topic_id}.yaml"

    if not plan_path.exists():
        # Buscar cualquier plan-filminas-*.yaml
        candidates = list(slides_dir.glob("plan-filminas-*.yaml"))
        if not candidates:
            return [f"ERROR: No se encontró plan-filminas-*.yaml en {slides_dir}"]
        plan_path = candidates[0]

    with plan_path.open(encoding="utf-8") as f:
        plan = yaml.safe_load(f) or {}

    errors: list[str] = []
    meta = plan.get("meta", {})
    slides = plan.get("slides", [])

    # Validar meta
    for field in ("topic_id", "title", "source", "generated_at", "template_id"):
        if not meta.get(field):
            errors.append(f"META: campo '{field}' faltante o vacío")

    if not slides:
        errors.append("PLAN: no contiene slides")
        return errors

    # Leer max_per_presentation del config
    gem_strategy = config.get("gemini_image_strategy", {})
    max_images = int(
        gem_strategy.get("max_per_presentation",
        gem_strategy.get("max_images_per_presentation", 12))
    )

    images_planned = 0

    for slide in slides:
        sid = slide.get("id", "?")
        prefix = f"Slide {sid}"

        # 1. type explícito y en el enum
        slide_type = slide.get("type", "")
        if not slide_type:
            errors.append(f"{prefix}: campo 'type' faltante — DEBE ser explícito, nunca inferido")
        elif slide_type not in allowed_types:
            errors.append(f"{prefix}: type='{slide_type}' no está en el enum permitido: {sorted(allowed_types)}")

        # 2. title no vacío
        if not slide.get("title", "").strip():
            errors.append(f"{prefix}: 'title' está vacío")

        # 3. layout — todas las zonas presentes
        layout = slide.get("layout", {})
        if not layout:
            errors.append(f"{prefix}: 'layout' faltante")
        else:
            for zone, allowed in allowed_layout_zones.items():
                val = layout.get(zone)
                if val is None:
                    errors.append(f"{prefix}: layout.{zone} faltante")
                elif val not in allowed:
                    errors.append(f"{prefix}: layout.{zone}='{val}' inválido — permitidos: {sorted(allowed)}")

        # 4. image — strategy/layer y prompt
        bg_image = slide.get("background_image", {})
        content_image = slide.get("content_image", {})

        for img_field, img_data in [("background_image", bg_image), ("content_image", content_image)]:
            if not img_data:
                continue
            strategy = img_data.get("strategy", "none")
            if strategy not in ALLOWED_IMAGE_STRATEGIES:
                errors.append(f"{prefix}: {img_field}.strategy='{strategy}' inválido")
            if strategy in ("gemini", "background", "content"):
                prompt = (img_data.get("prompt") or "").strip()
                if not prompt:
                    errors.append(
                        f"{prefix}: {img_field}.strategy='{strategy}' pero prompt está vacío — "
                        "el agente DEBE especificar un prompt de imagen visual puro"
                    )
                else:
                    images_planned += 1

    # 5. Verificar budget de imágenes
    if images_planned > max_images:
        errors.append(
            f"BUDGET: {images_planned} imágenes planificadas pero max_per_presentation={max_images} en config. "
            "Reducir imágenes o actualizar slides-config.yaml."
        )

    return errors


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python scripts/validate_plan.py <ruta-tema>")
        print("Ejemplo: python scripts/validate_plan.py salida/cursadas/2026/temas/02-sintaxis-semantica")
        sys.exit(1)

    topic_folder = Path(sys.argv[1])
    if not topic_folder.is_absolute():
        topic_folder = (Path.cwd() / topic_folder).resolve()

    if not topic_folder.exists():
        print(f"ERROR: La carpeta del tema no existe: {topic_folder}")
        sys.exit(1)

    print(f"Validando plan de: {topic_folder.name}")
    errors = validate_plan(topic_folder)

    if errors:
        print(f"\n❌ {len(errors)} error(es) encontrado(s):\n")
        for err in errors:
            print(f"  • {err}")
        print("\n→ El agente debe corregir el plan antes de ejecutar el pipeline.")
        sys.exit(1)
    else:
        print("✅ Plan válido — todos los campos obligatorios presentes y coherentes.")
        print("   Podés ejecutar: python scripts/slides_pipeline.py <tema> --assets-only")
        sys.exit(0)


if __name__ == "__main__":
    main()
