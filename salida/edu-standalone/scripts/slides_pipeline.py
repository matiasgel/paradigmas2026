#!/usr/bin/env python3
"""
EDU Slides Pipeline — Módulo EDU
=================================
Consume artefactos YAML ya resueltos → assets (imágenes/tablas) → Google Slides.

Fases:
    1. validate — Valida plan-filminas-{tema}.yaml, assets-manifest.yaml y
                                publish-context.yaml generados por el agente.
    2. assets   — Genera imágenes con Gemini, renderiza tablas como PNG,
               sube todo a Google Drive.
    3. publish  — Lee el plan + assets y crea la presentación en Google Slides.

Uso:
  python slides_pipeline.py <ruta-tema>
  python slides_pipeline.py <ruta-tema> --plan-only
  python slides_pipeline.py <ruta-tema> --assets-only
  python slides_pipeline.py <ruta-tema> --publish-only

Ejemplos:
  python slides_pipeline.py salida/cursadas/2026/temas/01-conceptos-introductorios
  python slides_pipeline.py salida/cursadas/2026/temas/01-conceptos-introductorios --plan-only

Requiere:
  pip install -r requirements.txt

Archivos de configuración requeridos (en la raíz del proyecto):
  _edu/secrets.local.yaml  — google_credentials_path + gemini_api_key
  _edu/slides-config.yaml  — sistema de diseño generado por /edu-slides-designer

Artefactos requeridos en la carpeta del tema (generados por el agente):
    slides/plan-filminas-{tema}.yaml
    slides/assets-manifest.yaml
    slides/publish-context.yaml
"""

from __future__ import annotations

import argparse
import base64
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import requests
import yaml

# Google API
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# ═══════════════════════════════════════════════════════════════════════
# CONSTANTES
# ═══════════════════════════════════════════════════════════════════════

SCOPES = [
    "https://www.googleapis.com/auth/presentations",
    "https://www.googleapis.com/auth/drive",
]

DEFAULT_FILMINAS_SCHEMA = Path("_edu/templates/filminas-schema.yaml")

# Dimensiones estándar 16:9 en EMU (English Metric Units)
SLIDE_W = 9_144_000
SLIDE_H = 5_143_500
MARGIN = 457_200      # ~0.5 pulgada
TITLE_H = 760_000  # alto reservado para título, compacto para maximizar espacio útil de contenido
LOGO_CLEAR = 700_000  # y mínimo para no solapar el logo institucional del template
TITLE_SAFE_X = 1_520_000
BOTTOM_CLEAR = 760_000
TABLE_BOTTOM_CLEAR = 1_520_000
EMU_PER_PT = 12_700

# Estrategia de imagen por tipo de filmina
IMAGE_STRATEGY: dict[str, str] = {
    "portada":           "background",  # imagen de fondo full-slide
    "cierre":            "background",
    "socratica":         "background",
    "concepto-abstracto": "content",    # imagen en panel derecho
    "diagrama":          "content",
    "timeline":          "content",
    "codigo":            "none",
    "concepto-mixto":    "none",         # body izq + código der: no imagen
    "tabla-mixta":       "none",         # texto + código izq, tabla der
    "tabla":             "none",
    "tabla-comparativa": "none",
    "demo":              "none",
}

# Directrices de layout por tipo
LAYOUT_MAP: dict[str, dict] = {
    "portada":            {"title": "center-middle",  "body": "center-bottom", "image": "background", "code": "none",       "table": "none"},
    "concepto-abstracto": {"title": "full-title",     "body": "left-middle",   "image": "right-half", "code": "none",       "table": "none"},
    "concepto-mixto":     {"title": "full-title",     "body": "left-middle",   "image": "none",       "code": "right-half", "table": "none"},
    "tabla-mixta":        {"title": "full-title",     "body": "left-top-split", "image": "none",      "code": "left-bottom-split", "table": "right-half"},
    "codigo":             {"title": "full-title",     "body": "subtitle-only", "image": "none",       "code": "full-bottom", "table": "none"},
    "tabla":              {"title": "full-title",     "body": "table-intro",   "image": "none",       "code": "none",       "table": "table-main"},
    "tabla-comparativa":  {"title": "full-title",     "body": "table-intro",   "image": "none",       "code": "none",       "table": "table-main"},
    "diagrama":           {"title": "full-title",     "body": "left-middle",   "image": "right-half", "code": "none",       "table": "none"},
    "socratica":          {"title": "center-top",     "body": "center-middle", "image": "background", "code": "none",       "table": "none"},
    "demo":               {"title": "full-title",     "body": "left-middle",   "image": "none",       "code": "right-half", "table": "none"},
    "cierre":             {"title": "center-middle",  "body": "center-bottom", "image": "background", "code": "none",       "table": "none"},
    "timeline":           {"title": "full-title",     "body": "full-center",   "image": "none",       "code": "none",       "table": "none"},
}

# Geometría de zonas en EMU: (x, y, width, height)
def _zones(w: int = SLIDE_W, h: int = SLIDE_H, m: int = MARGIN, th: int = TITLE_H) -> dict[str, tuple]:
    half_w = w // 2
    body_y = LOGO_CLEAR + th + 80_000
    body_h = h - body_y - max(m, BOTTOM_CLEAR)
    table_intro_h = 620_000
    table_gap = 220_000
    table_main_y = body_y + table_intro_h + table_gap
    table_main_h = h - table_main_y - max(m, TABLE_BOTTOM_CLEAR)
    split_intro_h = 600_000
    split_gap = 180_000
    split_left_w = half_w - int(m * 1.35)
    split_bottom_y = body_y + split_intro_h + split_gap
    split_bottom_h = max(600_000, body_h - split_intro_h - split_gap)
    return {
        "full-title":    (TITLE_SAFE_X, LOGO_CLEAR,   w - TITLE_SAFE_X - m, th),   # reserva lateral para logo
        "left-top":      (m,            LOGO_CLEAR,   half_w - m,      th),        # media anchura
        "center-top":    (m,            LOGO_CLEAR,   w - 2 * m,       th),
        "center-middle": (m,            h // 3,       w - 2 * m,       h // 3),
        "center-bottom": (m,            h * 2 // 3,   w - 2 * m,       h // 3 - m),
        "left-middle":   (m,            body_y,       half_w - m,      body_h),
        "left-half":     (m,            body_y,       half_w - m,      body_h),
        "left-top-split": (m,           body_y,       split_left_w,    split_intro_h),
        "left-bottom-split": (m,        split_bottom_y, split_left_w,  split_bottom_h),
        "right-half":    (half_w + m,   body_y,       half_w - 2 * m,  body_h),
        "full-bottom":   (m,            body_y,       w - 2 * m,       body_h),
        "full-center":   (m,            m,            w - 2 * m,       h - 2 * m),
        "subtitle-only": (m,            body_y,       w - 2 * m,       th // 2),
        "table-intro":   (m,            body_y,       w - 2 * m,       table_intro_h),
        "table-main":    (m,            table_main_y, w - 2 * m,       table_main_h),
        "background":    (0,            0,            w,               h),
        "none":          None,
    }

ZONES = _zones()

# ═══════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════

def find_project_root(start: Path) -> Path:
    cur = start.resolve()
    while True:
        if (cur / ".git").exists() or (cur / "module.yaml").exists():
            return cur
        # Modo standalone: edu-standalone/ tiene su propio _edu/
        if (cur / "_edu").exists() and (cur / "scripts").exists():
            return cur
        if cur == cur.parent:
            break
        cur = cur.parent
    raise FileNotFoundError(f"No se encontró la raíz del proyecto desde {start}.")


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def save_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)


def _deep_merge_dict(base: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in incoming.items():
        current = merged.get(key)
        if isinstance(current, dict) and isinstance(value, dict):
            merged[key] = _deep_merge_dict(current, value)
        else:
            merged[key] = value
    return merged


def _default_filminas_schema() -> dict[str, Any]:
    return {
        "version": "filminas/v1",
        "template_path": "_edu/templates/filminas-template.md",
        "markers": {
            "slide_heading_pattern": r"^###\s+\[F-(\d+)\]\s*(.*)$",
            "ignored_section_patterns": [
                r"^##\s+PORTADA\b",
                r"^##\s+BLOQUE\b",
            ],
            "separator": "---",
        },
        "headings": {
            "subtitle_levels": [1],
            "body_heading_levels": [2, 3, 4, 5, 6],
        },
        "directives": {
            "type": "@tipo:",
            "layout": "@layout:",
            "image": "@imagen:",
            "image_prompt": "@prompt-imagen:",
            "asset": "@asset:",
        },
        "allowed": {
            "slide_types": sorted(LAYOUT_MAP.keys()),
            "layout_presets": sorted(LAYOUT_MAP.keys()),
            "image_strategies": ["background", "content", "none"],
        },
    }


def load_filminas_schema(project_root: Path) -> dict[str, Any]:
    schema = _default_filminas_schema()
    schema_path = project_root / DEFAULT_FILMINAS_SCHEMA
    if schema_path.exists():
        schema = _deep_merge_dict(schema, load_yaml(schema_path))
    schema["_path"] = str(
        schema_path.relative_to(project_root) if schema_path.exists() else DEFAULT_FILMINAS_SCHEMA
    )
    return schema


def _pt(v: float) -> dict:
    return {"magnitude": v, "unit": "PT"}


def _emu_size(w: int, h: int) -> dict:
    return {"width": {"magnitude": w, "unit": "EMU"}, "height": {"magnitude": h, "unit": "EMU"}}


def _transform(tx: int, ty: int) -> dict:
    return {"scaleX": 1, "scaleY": 1, "translateX": tx, "translateY": ty, "unit": "EMU"}


def _hex_rgb(color: str) -> dict:
    h = color.lstrip("#")
    return {"red": int(h[0:2], 16) / 255.0, "green": int(h[2:4], 16) / 255.0, "blue": int(h[4:6], 16) / 255.0}


def _color(hex_color: str) -> dict:
    # Para estilos de texto (foregroundColor) Google Slides usa OpaqueColor.
    return {"opaqueColor": {"rgbColor": _hex_rgb(hex_color)}}


def _rgb_color(hex_color: str) -> dict:
    # Para fondos y rellenos (pageBackgroundFill, solidFill) usa rgbColor directo.
    return {"rgbColor": _hex_rgb(hex_color)}


def _normalize_alignment(align: str) -> str:
    """Map human-friendly alignment values to Google Slides API enums."""
    a = (align or "").strip().upper()
    if a in ("LEFT", "START"):
        return "START"
    if a in ("RIGHT", "END"):
        return "END"
    if a in ("CENTER", "MIDDLE"):
        return "CENTER"
    return "START"


def _strip_markdown(text: str) -> str:
    """Elimina marcado Markdown del texto para display limpio en Google Slides."""
    # Eliminar **bold** y __bold__
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text, flags=re.DOTALL)
    text = re.sub(r'__(.+?)__', r'\1', text, flags=re.DOTALL)
    # Eliminar *italic* y _italic_
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'_(.+?)_', r'\1', text)
    # Eliminar `inline code`
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Eliminar links [texto](url) → solo texto
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # Eliminar > blockquotes
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
    # Eliminar ## headings al inicio de línea
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    return text.strip()


def _sanitize_markdown_paragraph(text: str) -> str:
    """Limpia marcadores de bloque que no deben quedar visibles en Slides."""
    clean = re.sub(r'^\s*>+\s?', '', text.strip())
    return clean.strip()


def _parse_directive_pairs(text: str) -> dict[str, str]:
    pairs = {}
    for key, raw_value in re.findall(r'([A-Za-z_][\w-]*)=("[^"]*"|\S+)', text):
        pairs[key] = raw_value.strip('"')
    return pairs


def _parse_schema_directive(line: str, schema: dict[str, Any]) -> dict[str, Any] | None:
    stripped = line.strip()
    directives = schema.get("directives", {})
    for name, prefix in directives.items():
        if stripped.lower().startswith(str(prefix).lower()):
            value = stripped[len(prefix):].strip()
            parsed: dict[str, Any] = {"name": name, "raw": value}
            if name == "asset":
                parsed["value"] = _parse_directive_pairs(value) or {"raw": value}
            else:
                parsed["value"] = value
            return parsed
    return None


def _compose_body_text(subtitle: str, blocks: list[dict]) -> str:
    parts: list[str] = []
    clean_subtitle = _strip_markdown(subtitle or "")
    if clean_subtitle:
        parts.append(clean_subtitle)

    body_text = _blocks_to_text(blocks)
    if body_text:
        parts.append(body_text)

    return "\n\n".join(part for part in parts if part)


def _list_item_parts(item: Any) -> tuple[str, int]:
    if isinstance(item, dict):
        return _strip_markdown(str(item.get("content", ""))), int(item.get("level", 0) or 0)
    return _strip_markdown(str(item)), 0


def _parse_inline_markdown(text: str) -> tuple[str, list[dict[str, Any]]]:
    plain_parts: list[str] = []
    spans: list[dict[str, Any]] = []
    i = 0

    def current_len() -> int:
        return sum(len(part) for part in plain_parts)

    while i < len(text):
        if text.startswith("**", i) or text.startswith("__", i):
            marker = text[i:i + 2]
            end = text.find(marker, i + 2)
            if end != -1:
                inner_plain, inner_spans = _parse_inline_markdown(text[i + 2:end])
                start = current_len()
                plain_parts.append(inner_plain)
                spans.extend(
                    {**span, "start": span["start"] + start, "end": span["end"] + start}
                    for span in inner_spans
                )
                if inner_plain:
                    spans.append({"start": start, "end": start + len(inner_plain), "bold": True})
                i = end + 2
                continue

        if text[i] in "*_":
            marker = text[i]
            end = text.find(marker, i + 1)
            if end != -1:
                inner_plain, inner_spans = _parse_inline_markdown(text[i + 1:end])
                start = current_len()
                plain_parts.append(inner_plain)
                spans.extend(
                    {**span, "start": span["start"] + start, "end": span["end"] + start}
                    for span in inner_spans
                )
                if inner_plain:
                    spans.append({"start": start, "end": start + len(inner_plain), "italic": True})
                i = end + 1
                continue

        if text[i] == "`":
            end = text.find("`", i + 1)
            if end != -1:
                literal = text[i + 1:end]
                start = current_len()
                plain_parts.append(literal)
                if literal:
                    spans.append({"start": start, "end": start + len(literal), "code": True})
                i = end + 1
                continue

        if text[i] == "[":
            close_label = text.find("]", i + 1)
            if close_label != -1 and close_label + 1 < len(text) and text[close_label + 1] == "(":
                close_url = text.find(")", close_label + 2)
                if close_url != -1:
                    label = text[i + 1:close_label]
                    url = text[close_label + 2:close_url].strip()
                    inner_plain, inner_spans = _parse_inline_markdown(label)
                    start = current_len()
                    plain_parts.append(inner_plain)
                    spans.extend(
                        {**span, "start": span["start"] + start, "end": span["end"] + start}
                        for span in inner_spans
                    )
                    if inner_plain and url:
                        spans.append({"start": start, "end": start + len(inner_plain), "link": url})
                    i = close_url + 1
                    continue

        plain_parts.append(text[i])
        i += 1

    return "".join(plain_parts), spans


def _compose_rich_text(subtitle: str, blocks: list[dict]) -> dict[str, Any]:
    groups: list[dict[str, Any]] = []

    lead = _sanitize_markdown_paragraph(subtitle or "")
    if lead:
        groups.append({"kind": "lead", "paragraphs": [lead]})

    for block in blocks:
        kind = block.get("type")
        if kind == "heading":
            content = _sanitize_markdown_paragraph(str(block.get("content", "")))
            if content:
                groups.append({
                    "kind": "heading",
                    "level": int(block.get("level", 2) or 2),
                    "paragraphs": [content],
                })
            continue

        if kind == "text":
            paragraphs = [
                _sanitize_markdown_paragraph(line)
                for line in str(block.get("content", "")).splitlines()
                if line.strip()
            ]
            paragraphs = [paragraph for paragraph in paragraphs if paragraph]
            if paragraphs:
                groups.append({"kind": "text", "paragraphs": paragraphs})
            continue

        if kind == "list":
            paragraphs = []
            for item in block.get("items", []):
                item_text, _level = _list_item_parts(item)
                if item_text:
                    paragraphs.append(item_text)
            if paragraphs:
                groups.append({
                    "kind": "list",
                    "ordered": bool(block.get("ordered", False)),
                    "paragraphs": paragraphs,
                })

    text_parts: list[str] = []
    spans: list[dict[str, Any]] = []
    bullet_ranges: list[dict[str, Any]] = []
    emphasis_ranges: list[dict[str, Any]] = []
    cursor = 0

    for group_idx, group in enumerate(groups):
        if group_idx > 0:
            text_parts.append("\n\n")
            cursor += 2

        group_start = cursor
        for paragraph_idx, paragraph in enumerate(group.get("paragraphs", [])):
            if paragraph_idx > 0:
                text_parts.append("\n")
                cursor += 1

            plain, local_spans = _parse_inline_markdown(paragraph)
            if not plain:
                continue
            start = cursor
            text_parts.append(plain)
            cursor += len(plain)
            end = cursor

            spans.extend(
                {**span, "start": span["start"] + start, "end": span["end"] + start}
                for span in local_spans
            )

            if group["kind"] == "lead":
                emphasis_ranges.append({"start": start, "end": end, "role": "lead", "level": 1})
            elif group["kind"] == "heading":
                emphasis_ranges.append({
                    "start": start,
                    "end": end,
                    "role": "heading",
                    "level": int(group.get("level", 2) or 2),
                })

        if group["kind"] == "list" and cursor > group_start:
            bullet_ranges.append({
                "start": group_start,
                "end": cursor,
                "ordered": bool(group.get("ordered", False)),
            })

    return {
        "text": "".join(text_parts).strip(),
        "spans": spans,
        "bullet_ranges": bullet_ranges,
        "emphasis_ranges": emphasis_ranges,
    }


def _inset_geometry(geo: tuple[int, int, int, int], pad_x: int, pad_y: int | None = None) -> tuple[int, int, int, int]:
    if pad_y is None:
        pad_y = pad_x
    x, y, w, h = geo
    inner_w = max(300_000, w - 2 * pad_x)
    inner_h = max(220_000, h - 2 * pad_y)
    return (x + pad_x, y + pad_y, inner_w, inner_h)


def _fit_code_font_size(
    code_text: str,
    geo: tuple[int, int, int, int],
    preferred_size: float,
    min_size: float = 5,
) -> tuple[float, bool]:
    lines = [line.expandtabs(4).rstrip() for line in code_text.splitlines()] or [""]
    longest_line = max((len(line) for line in lines), default=1)
    line_count = len(lines)
    _, _, width_emu, height_emu = geo
    width_pt = width_emu / EMU_PER_PT
    height_pt = height_emu / EMU_PER_PT

    probe = int(preferred_size)
    floor = int(min_size)
    for size in range(probe, floor - 1, -1):
        approx_chars = width_pt / max(size * 0.66, 1)
        approx_lines = height_pt / max(size * 1.55, 1)
        if longest_line <= approx_chars and line_count <= approx_lines:
            return float(size), size < probe

    return float(min_size), True


def _fit_text_font_size(
    text: str,
    geo: tuple[int, int, int, int],
    preferred_size: float,
    min_size: float = 10,
) -> float:
    lines = [line.strip() for line in text.splitlines() if line.strip()] or [""]
    _, _, width_emu, height_emu = geo
    width_pt = width_emu / EMU_PER_PT
    height_pt = height_emu / EMU_PER_PT

    probe = int(preferred_size)
    floor = int(min_size)
    for size in range(probe, floor - 1, -1):
        chars_per_line = max(width_pt / max(size * 0.52, 1), 8)
        visual_lines = 0
        for line in lines:
            visual_lines += max(1, int((len(line) + chars_per_line - 1) // chars_per_line))
        max_lines = height_pt / max(size * 1.32, 1)
        if visual_lines <= max_lines:
            return float(size)

    return float(min_size)


def _table_dimensions(table_md: str) -> tuple[int, int]:
    rows = []
    for line in table_md.strip().splitlines():
        clean = line.replace("|", "").strip()
        if re.match(r"^[\-:\s]+$", clean):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return (0, 0)
    return len(rows), max(len(row) for row in rows)


def _should_use_native_table(table_md: str) -> bool:
    rows, cols = _table_dimensions(table_md)
    return rows > 0 and rows <= 8 and cols <= 5


def _looks_like_ascii_diagram(code_text: str) -> bool:
    lines = [line.rstrip() for line in code_text.splitlines() if line.strip()]
    if not lines or len(lines) > 6:
        return False
    joined = "\n".join(lines)
    has_ascii_connectors = any(token in joined for token in ("→", "←", "↑", "↓", "──", "|", "/", "\\"))
    looks_like_program = any(token in joined for token in ("{", "}", ";", "=>", "function", "const ", "let ", "class "))
    return has_ascii_connectors and not looks_like_program


def _centered_box(geo: tuple[int, int, int, int], width_ratio: float, height_ratio: float) -> tuple[int, int, int, int]:
    x, y, w, h = geo
    inner_w = int(w * width_ratio)
    inner_h = int(h * height_ratio)
    inner_x = x + (w - inner_w) // 2
    inner_y = y + (h - inner_h) // 2
    return (inner_x, inner_y, inner_w, inner_h)


# ═══════════════════════════════════════════════════════════════════════
# FASE 1 — PARSEO DE FILMINAS.MD
# ═══════════════════════════════════════════════════════════════════════

def parse_filminas(filminas_path: Path, schema: dict[str, Any] | None = None) -> list[dict]:
    """Lee filminas.md y extrae cada slide como estructura semántica completa."""
    if schema is None:
        schema = load_filminas_schema(find_project_root(filminas_path.parent))

    text = filminas_path.read_text(encoding="utf-8")
    slides: list[dict] = []
    current: dict | None = None
    slide_pattern = re.compile(schema["markers"]["slide_heading_pattern"])

    for line in text.splitlines():
        m = slide_pattern.match(line)
        if m:
            if current:
                slides.append(_finalize_slide(current, schema))
            current = {
                "id":          f"F-{m.group(1).zfill(2)}",
                "raw_title":   m.group(2).strip(),
                "raw_lines":   [],
            }
        elif current is not None:
            current["raw_lines"].append(line)

    if current:
        slides.append(_finalize_slide(current, schema))

    validate_filminas_contract(slides, schema, filminas_path)

    return slides


def _finalize_slide(raw: dict, schema: dict[str, Any]) -> dict:
    """Parsea raw_lines en bloques semánticos: subtitle, body_blocks, code_blocks, tables."""
    lines       = raw["raw_lines"]
    title       = raw["raw_title"]
    subtitle    = ""
    body_blocks: list[dict] = []
    code_blocks: list[dict] = []
    tables:      list[str]  = []
    directives: dict[str, Any] = {}
    asset_hints: list[dict[str, Any]] = []
    ignored_section_patterns = [
        re.compile(pattern, flags=re.IGNORECASE)
        for pattern in schema.get("markers", {}).get("ignored_section_patterns", [])
    ]
    subtitle_levels = set(schema.get("headings", {}).get("subtitle_levels", [1]))

    in_code    = False
    code_lang  = ""
    code_lines: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # ── Bloque de código ────────────────────────────────────────────
        m_code = re.match(r"^```(\w*)\s*$", line)
        if m_code and not in_code:
            in_code   = True
            code_lang = m_code.group(1) or "text"
            code_lines = []
            i += 1
            continue
        if in_code:
            if line.strip() == "```":
                code_blocks.append({"lang": code_lang, "content": "\n".join(code_lines)})
                in_code = False
            else:
                code_lines.append(line)
            i += 1
            continue

        directive = _parse_schema_directive(line, schema)
        if directive:
            if directive["name"] == "asset":
                asset_hints.append(directive["value"])
            else:
                directives[directive["name"]] = directive["value"]
            i += 1
            continue

        # ── Tabla Markdown ──────────────────────────────────────────────
        if line.strip().startswith("|"):
            tbl_lines = [line]
            i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl_lines.append(lines[i])
                i += 1
            tables.append("\n".join(tbl_lines))
            continue

        # ── Saltar secciones del documento que no pertenecen a la slide ───
        if any(pattern.match(line) for pattern in ignored_section_patterns):
            i += 1
            continue

        # ── Headings Markdown → subtítulo o texto destacado ─────────────
        m_h = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m_h and not title:
            title = m_h.group(2).strip()
            i += 1
            continue
        if m_h and not subtitle and len(m_h.group(1)) in subtitle_levels:
            subtitle = m_h.group(2).strip()
            i += 1
            continue
        if m_h:
            body_blocks.append({
                "type": "heading",
                "level": len(m_h.group(1)),
                "content": m_h.group(2).strip(),
            })
            i += 1
            continue

        # ── Separadores / líneas vacías ─────────────────────────────────
        if not line.strip() or line.strip() == "---":
            i += 1
            continue

        # ── Texto / lista ───────────────────────────────────────────────
        block_lines = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            if (not nxt.strip()
                    or nxt.strip() == "---"
                    or nxt.startswith("#")
                    or nxt.startswith("```")
                    or nxt.startswith("|")):
                break
            block_lines.append(nxt)
            i += 1

        first = block_lines[0].strip()
        if re.match(r"^(?:[-*•]|\d+\.)", first):
            ordered = bool(re.match(r"^\s*\d+[.)]\s+", first))
            items = []
            for bl in block_lines:
                # Strip bullet prefix correctamente: "- text", "* text", "• text", "1. text"
                stripped = re.sub(r'^\s*[-*•]\s+', '', bl)
                stripped = re.sub(r'^\s*\d+[.)]\s+', '', stripped).strip()
                if stripped:
                    items.append({"content": stripped, "level": 0})
            if items:
                body_blocks.append({"type": "list", "ordered": ordered, "items": items})
        else:
            combined = "\n".join(block_lines)
            body_blocks.append({"type": "text", "content": combined})

    return {
        "id":          raw["id"],
        # v2 (Sprint 2): el tipo viene SIEMPRE del @tipo: explícito en filminas.md.
        # Sin @tipo: → "pending". _detect_type() ya no se llama aquí.
        "type":        directives.get("type") or "pending",
        "title":       title,
        "subtitle":    subtitle,
        "body_blocks": body_blocks,
        "code_blocks": code_blocks,
        "tables":      tables,
        "directives":  directives,
        "asset_hints": asset_hints,
    }


def validate_filminas_contract(slides: list[dict], schema: dict[str, Any], filminas_path: Path) -> None:
    errors: list[str] = []
    if not slides:
        errors.append("No se detectaron filminas con el patrón canónico ### [F-XX] Título")

    seen_ids: set[str] = set()
    allowed = schema.get("allowed", {})
    allowed_types = set(allowed.get("slide_types", []))
    allowed_layouts = set(allowed.get("layout_presets", []))
    allowed_images = set(allowed.get("image_strategies", []))
    validation_cfg = schema.get("validation", {}) or {}
    image_prompt_required = bool(validation_cfg.get("image_prompt_required_when_image_enabled", False))

    for slide in slides:
        slide_id = slide.get("id", "?")
        if slide_id in seen_ids:
            errors.append(f"{slide_id}: ID duplicado")
        seen_ids.add(slide_id)

        if not str(slide.get("title", "")).strip():
            errors.append(f"{slide_id}: título vacío")

        directives = slide.get("directives") or {}
        forced_type = directives.get("type")
        if forced_type and forced_type not in allowed_types:
            errors.append(f"{slide_id}: @tipo inválido ({forced_type})")

        layout_override = directives.get("layout")
        if layout_override and layout_override not in allowed_layouts:
            errors.append(f"{slide_id}: @layout inválido ({layout_override})")

        image_override = directives.get("image")
        if image_override and image_override not in allowed_images:
            errors.append(f"{slide_id}: @imagen inválido ({image_override})")

        if image_prompt_required and image_override in {"background", "content"}:
            image_prompt = str(directives.get("image_prompt", "")).strip()
            asset_hints = slide.get("asset_hints") or []
            asset_prompt = any(str(asset.get("prompt", "")).strip() for asset in asset_hints if isinstance(asset, dict))
            if not image_prompt and not asset_prompt:
                errors.append(f"{slide_id}: requiere @prompt-imagen o @asset con prompt cuando @imagen={image_override}")

    if errors:
        raise ValueError(
            "Contrato de filminas inválido en "
            f"{filminas_path}:\n- " + "\n- ".join(errors)
        )


# DEPRECATED (v2 — Sprint 2): _detect_type() ya no se llama desde _finalize_slide().
# La inferencia automática de tipo fue la causa del Bug 1 (tipo 'codigo' tapaba el cuerpo).
# Usar @tipo: en filminas.md. Se mantiene solo para generate_plan() (backwards compat).
# El nuevo flujo usa parse_filminas.py → agente asigna tipo explícito → validate_plan.py.
def _detect_type(slide_id: str, title: str, code_blocks, tables, directives: dict[str, Any] | None = None, body_blocks: list | None = None) -> str:
    forced_type = str((directives or {}).get("type", "")).strip()
    if forced_type in LAYOUT_MAP:
        return forced_type
    num = int(slide_id.split("-")[1])
    if num == 0:
        return "portada"
    if code_blocks and tables:
        return "tabla-mixta"
    if code_blocks:
        # Si hay cuerpo sustancial (listas o varios bloques de texto), usar diseño mixto
        if body_blocks:
            substantial = sum(
                len(b.get("items", []))
                if b.get("type") == "list"
                else (1 if b.get("type") in ("text", "heading") else 0)
                for b in body_blocks
            )
            if substantial >= 2:
                return "concepto-mixto"
        return "codigo"
    if tables:
        return "tabla"
    tl = title.lower()
    if any(k in tl for k in ["demo ", "en vivo", "práctica", "ejercicio"]):
        return "demo"
    if any(k in tl for k in ["cierre", "adelanto", "mapa de la materia", "fin de"]):
        return "cierre"
    if any(k in tl for k in ["timeline", "línea del tiempo", "historia"]):
        return "timeline"
    if any(k in tl for k in ["¿", "pregunta", "reflexión", "socrát"]):
        return "socratica"
    if any(k in tl for k in ["diagrama", "pipeline", "flujo", "arquitectura", "cuello de botella"]):
        return "diagrama"
    return "concepto-abstracto"


# ═══════════════════════════════════════════════════════════════════════
# FASE 1 — GENERADOR DE PLAN
# ═══════════════════════════════════════════════════════════════════════

def _preferred_image_prompt(slide: dict) -> str:
    directives = slide.get("directives") or {}
    explicit = str(directives.get("image_prompt", "")).strip()
    if explicit:
        return explicit

    for asset in slide.get("asset_hints") or []:
        if not isinstance(asset, dict):
            continue
        prompt = str(asset.get("prompt", "")).strip()
        if prompt:
            return prompt

    return ""


def _slide_visual_context(slide: dict) -> str:
    parts: list[str] = []
    title = _strip_markdown(str(slide.get("title", "")).strip())
    subtitle = _strip_markdown(str(slide.get("subtitle", "")).strip())

    if title:
        parts.append(title)
    if subtitle:
        parts.append(subtitle)

    return ". ".join(part for part in parts if part)


def _palette_prompt_fragment(config: dict) -> str:
    palette = config.get("palette", {}) or {}
    color_names = {
        "#8B0000": "bordo institucional",
        "#FFFFFF": "blanco",
        "#1A1A1A": "gris carbon",
        "#000000": "negro",
    }
    mapped = [
        color_names.get(str(color).strip().upper())
        for color in [palette.get("primary"), palette.get("secondary"), palette.get("text")]
        if color
    ]
    mapped = [color for color in mapped if color]
    if not mapped:
        return "paleta sobria universitaria"
    return "paleta " + ", ".join(dict.fromkeys(mapped))


def _image_safety_rules() -> str:
    return (
        "Sin texto, sin letras, sin código, sin etiquetas ni fórmulas. "
        "Solo elementos visuales: objetos, iconos, escenas o diagramas mudos. "
        "Estilo vectorial limpio, fondo claro, académico."
    )


# DEPRECATED (v2 — Sprint 2): _append_image_guardrails() y _image_prompt() ya no se
# llaman desde el flujo principal. La inferencia automática de prompts fue la causa del
# Bug 3 (etiquetas de texto en inglés en imágenes). El agente escribe los prompts con
# lenguaje visual puro (ver _edu/templates/prompt-imagen-guide.md). Se mantienen solo
# para generate_plan() (backwards compat).


def _append_image_guardrails(prompt: str, config: dict) -> str:
    base = re.sub(r"\s+", " ", prompt).strip().rstrip(".")
    style = f"Alta resolución, {_palette_prompt_fragment(config)}. {_image_safety_rules()}"
    return f"{base}. {style}"


def _max_images_per_presentation(config: dict) -> int:
    strategy = config.get("gemini_image_strategy", {}) or {}
    raw = strategy.get("max_per_presentation", strategy.get("max_images_per_presentation", 8))
    if raw is None or raw == "":
        return 8
    return int(raw)

def _image_prompt(slide: dict, config: dict) -> str:
    """Genera un prompt Gemini para imagen de fondo o contenido."""
    preferred = _preferred_image_prompt(slide)
    if preferred:
        return _append_image_guardrails(preferred, config)

    stype = slide.get("type", "concepto-abstracto")
    title = _strip_markdown(str(slide.get("title", "")).strip()) or "lenguajes de programación"

    if stype == "portada":
        prompt = (
            f"Portada académica universitaria: bloques geométricos y flechas representando etapas de un compilador, "
            f"aula y materiales de estudio. Tema: {title}"
        )
    elif stype == "cierre":
        prompt = (
            f"Composición visual de síntesis: árbol sintáctico, bloques de pipeline y símbolo de completitud. "
            f"Tema: {title}"
        )
    elif stype == "socratica":
        prompt = (
            f"Escena de debate académico: dos caminos visuales opuestos con íconos contrastantes. "
            f"Tema: {title}"
        )
    elif stype == "diagrama":
        prompt = (
            f"Infografía técnica con cajas y flechas representando un pipeline o flujo de procesamiento. "
            f"Tema: {title}"
        )
    elif stype == "timeline":
        prompt = (
            f"Línea de tiempo con hitos visuales concretos, íconos mudos, sin texto. "
            f"Tema: {title}"
        )
    else:
        prompt = (
            f"Ilustración técnica universitaria: objetos y escenas propios del dominio de compiladores, "
            f"sin elementos decorativos. Tema: {title}"
        )
    return _append_image_guardrails(prompt, config)


# DEPRECATED (v2 — Sprint 2): generate_plan() fue movido a scripts/parse_filminas.py.
# El nuevo flujo: parse_filminas.py → agente completa → validate_plan.py → slides_pipeline.py
# Esta función se mantiene SOLO para compatibilidad con --regen-plan legacy.
def generate_plan(filminas_path: Path, config: dict, template_id: str) -> dict:
    """Fase 1: filminas.md → plan-filminas-{tema}.yaml.

    DEPRECATED (v2): Usar scripts/parse_filminas.py en su lugar.
    """
    import warnings
    warnings.warn(
        "generate_plan() está deprecado (v2). Usar scripts/parse_filminas.py en su lugar.",
        DeprecationWarning,
        stacklevel=2,
    )
    print("⚠️  DEPRECADO: generate_plan() → usar scripts/parse_filminas.py (flujo v2)")
    print("📋 Generando plan (legacy — con inferencia de tipos) desde filminas.md …")

    project_root = find_project_root(filminas_path.parent)
    schema = load_filminas_schema(project_root)
    slides      = parse_filminas(filminas_path, schema)

    # Backwards compat: re-inferir tipos para slides con type: "pending" (sin @tipo:)
    for s in slides:
        if s.get("type") == "pending":
            s["type"] = _detect_type(
                s["id"], s["title"], s["code_blocks"], s["tables"],
                s.get("directives"), s.get("body_blocks")
            )

    topic_id    = filminas_path.parent.name
    topic_title = topic_id.replace("-", " ").title()
    if slides:
        first_title = (slides[0].get("title") or "").strip()
        first_subtitle = (slides[0].get("subtitle") or "").strip()
        topic_title = first_subtitle or first_title or topic_title
        if first_title.lower() == "portada" and first_subtitle:
            topic_title = first_subtitle

    # Budget de imágenes: máximo 12 por presentación
    max_images  = _max_images_per_presentation(config)
    if max_images < 12:
        max_images = 12
    img_count   = 0
    priority    = ["portada", "cierre", "concepto-abstracto", "diagrama", "socratica", "timeline"]

    assigned: dict[str, str] = {}
    for stype in priority:
        for s in slides:
            if s["id"] in assigned:
                continue
            if s["type"] == stype and IMAGE_STRATEGY.get(stype, "none") != "none":
                assigned[s["id"]] = IMAGE_STRATEGY[stype] if img_count < max_images else "none"
                if IMAGE_STRATEGY.get(stype, "none") != "none" and img_count < max_images:
                    img_count += 1
    for s in slides:
        assigned.setdefault(s["id"], "none")

    plan_slides = []
    for slide in slides:
        directives = slide.get("directives") or {}
        layout_key = directives.get("layout") or slide["type"]
        layout   = LAYOUT_MAP.get(layout_key, LAYOUT_MAP[slide["type"]])
        strategy = directives.get("image") or assigned[slide["id"]]

        bg_strategy = strategy if strategy == "background" else "none"
        ct_strategy = strategy if strategy == "content"    else "none"

        bg_prompt = _image_prompt(slide, config) if bg_strategy == "gemini" or bg_strategy == "background" else ""
        ct_prompt = _image_prompt(slide, config) if ct_strategy == "gemini" or ct_strategy == "content"    else ""

        # Si la estrategia es "background" o "content", el medio de generación es "gemini"
        bg_gen = "gemini" if bg_strategy == "background" else "none"
        ct_gen = "gemini" if ct_strategy == "content"    else "none"

        table_assets = [
            {
                "index":          idx,
                "table_markdown": tmd,
                "local_asset":    f"slides/assets/{slide['id']}-table-{idx + 1}.png",
                "drive_id":       None,
            }
            for idx, tmd in enumerate(slide["tables"])
        ]

        plan_slides.append({
            "id":       slide["id"],
            "type":     slide["type"],
            # Contenido completo de filminas.md
            "title":       slide["title"],
            "subtitle":    slide["subtitle"],
            "body_blocks": slide["body_blocks"],
            "code_blocks": slide["code_blocks"],
            "tables":      slide["tables"],
            "directives":  directives,
            "asset_hints": slide.get("asset_hints") or [],
            # Directrices de layout
            "layout": layout,
            # Imágenes
            "background_image": {
                "strategy":    bg_gen,
                "prompt":      bg_prompt,
                "local_asset": f"slides/assets/{slide['id']}-bg.png" if bg_gen == "gemini" else "",
                "drive_id":    None,
            },
            "content_image": {
                "strategy":    ct_gen,
                "prompt":      ct_prompt,
                "local_asset": f"slides/assets/{slide['id']}-content.png" if ct_gen == "gemini" else "",
                "drive_id":    None,
            },
            "table_assets": table_assets,
        })

    plan = {
        "meta": {
            "topic_id":      topic_id,
            "title":         topic_title,
            "source":        "filminas.md",
            "schema_version": schema.get("version", "filminas/v1"),
            "schema_path": schema.get("_path", str(DEFAULT_FILMINAS_SCHEMA)),
            "generated_at":  datetime.now().isoformat(timespec="seconds"),
            "template_id":   template_id,
            "total_slides":  len(slides),
            "images_planned": img_count,
        },
        "slides": plan_slides,
    }

    print(f"  ✅ {len(slides)} filminas procesadas, {img_count} imágenes planificadas.")
    return plan


def validate_publish_artifacts(
    topic_folder: Path,
    plan_path: Path,
    assets_manifest_path: Path,
    publish_context_path: Path,
) -> dict[str, Any]:
    missing = []
    for path, label in [
        (plan_path, "slides/plan-filminas-{tema}.yaml"),
        (assets_manifest_path, "slides/assets-manifest.yaml"),
        (publish_context_path, "slides/publish-context.yaml"),
    ]:
        if not path.exists():
            missing.append(f"- {label} ({path})")

    if missing:
        raise FileNotFoundError(
            "Faltan artefactos de publicación generados por el agente:\n" + "\n".join(missing)
        )

    plan = load_yaml(plan_path)
    if not plan.get("meta") or not plan.get("slides"):
        raise ValueError(f"Plan inválido: {plan_path} debe incluir 'meta' y 'slides'.")

    meta = plan.get("meta", {}) or {}
    required_meta = {"topic_id", "title", "source", "template_id"}
    missing_meta = required_meta - set(meta.keys())
    if missing_meta:
        raise ValueError(
            f"Plan inválido: faltan campos en meta: {', '.join(sorted(missing_meta))}"
        )

    for slide in plan.get("slides", []):
        slide_id = slide.get("id", "?")
        bg = slide.get("background_image") or {}
        ci = slide.get("content_image") or {}
        if bg.get("strategy") == "gemini" and not str(bg.get("prompt", "")).strip():
            raise ValueError(f"Plan inválido: {slide_id} requiere background_image.prompt no vacío.")
        if ci.get("strategy") == "gemini" and not str(ci.get("prompt", "")).strip():
            raise ValueError(f"Plan inválido: {slide_id} requiere content_image.prompt no vacío.")

    load_yaml(assets_manifest_path)
    load_yaml(publish_context_path)
    return plan


# ═══════════════════════════════════════════════════════════════════════
# FASE 2 — GENERACIÓN DE ASSETS
# ═══════════════════════════════════════════════════════════════════════

def _gemini_image(prompt: str, output_path: Path, api_key: str) -> bool:
    """Genera una imagen con Imagen 4.0 y la guarda en output_path."""
    model   = "imagen-4.0-generate-001"
    url     = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:predict?key={api_key}"
    )
    payload = {
        "instances": [{"prompt": prompt}],
        "parameters": {"sampleCount": 1},
    }
    try:
        resp = requests.post(url, json=payload, timeout=90)
        resp.raise_for_status()
        predictions = resp.json().get("predictions", [])
        if not predictions:
            raise ValueError("Sin predicciones en la respuesta")
        img_b64 = predictions[0].get("bytesBase64Encoded")
        if not img_b64:
            raise ValueError("No se encontró imagen en la respuesta")
        img_bytes = base64.b64decode(img_b64)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(img_bytes)
        return True
    except Exception as exc:
        print(f"    ⚠️  Imagen 4.0 falló para {output_path.name}: {exc}")
        return False


def _render_table_png(table_md: str, output_path: Path, config: dict) -> bool:
    """Renderiza tabla Markdown como PNG académico usando matplotlib."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import matplotlib.patches as patches

        palette    = config.get("palette", {})
        primary    = palette.get("primary", "#8B0000")
        bg_color   = palette.get("background", "#FFFFFF")
        text_color = palette.get("text", "#1A1A1A")

        rows = []
        for line in table_md.strip().splitlines():
            # Omitir línea separadora (|---|---|)
            clean = line.replace("|", "").strip()
            if re.match(r"^[\-:\s]+$", clean):
                continue
            cells = [_strip_markdown(c.strip()) for c in line.strip().strip("|").split("|")]
            rows.append(cells)

        if not rows:
            return False

        n_cols = max(len(r) for r in rows)
        rows   = [r + [""] * (n_cols - len(r)) for r in rows]
        n_rows = len(rows)

        fig_w = max(8.0, n_cols * 2.8)
        fig_h = max(2.0, n_rows * 0.65 + 0.4)

        fig, ax = plt.subplots(figsize=(fig_w, fig_h))
        ax.set_xlim(0, n_cols)
        ax.set_ylim(0, n_rows)
        ax.axis("off")
        fig.patch.set_facecolor(bg_color)

        for r_idx, row in enumerate(rows):
            y = n_rows - r_idx - 1
            for c_idx, cell in enumerate(row):
                if r_idx == 0:
                    face, fc, fw = primary, "#FFFFFF", "bold"
                else:
                    face = "#F2F2F2" if r_idx % 2 == 0 else bg_color
                    fc, fw = text_color, "normal"
                rect = patches.Rectangle(
                    (c_idx, y), 1, 1,
                    linewidth=0.6, edgecolor="#CCCCCC", facecolor=face
                )
                ax.add_patch(rect)
                ax.text(
                    c_idx + 0.5, y + 0.5, cell,
                    ha="center", va="center",
                    fontsize=10, color=fc, fontweight=fw,
                )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.tight_layout(pad=0.1)
        plt.savefig(str(output_path), dpi=150, bbox_inches="tight", facecolor=bg_color)
        plt.close(fig)
        return True
    except ImportError:
        print("    ⚠️  matplotlib no instalado — omitiendo imagen de tabla")
        return False
    except Exception as exc:
        print(f"    ⚠️  Error renderizando tabla: {exc}")
        return False


def _upload_drive(drive_svc, file_path: Path, folder_id: str | None) -> str | None:
    """Sube un archivo a Drive, lo hace público y devuelve el file_id."""
    try:
        meta  = {"name": file_path.name}
        if folder_id:
            meta["parents"] = [folder_id]
        media = MediaFileUpload(str(file_path), resumable=False)
        f     = drive_svc.files().create(body=meta, media_body=media, fields="id").execute()
        fid   = f["id"]
        drive_svc.permissions().create(
            fileId=fid,
            body={"role": "reader", "type": "anyone"},
        ).execute()
        time.sleep(0.3)   # margen para propagación de permisos
        return fid
    except Exception as exc:
        print(f"    ⚠️  Error subiendo {file_path.name} a Drive: {exc}")
        return None


def _ensure_drive_folder(drive_svc, name: str) -> str:
    """Obtiene o crea una carpeta de Drive. Devuelve el folder_id."""
    q = (
        f"name='{name}' and mimeType='application/vnd.google-apps.folder' "
        f"and trashed=false"
    )
    res = drive_svc.files().list(q=q, fields="files(id)").execute()
    files = res.get("files", [])
    if files:
        return files[0]["id"]
    meta = {"name": name, "mimeType": "application/vnd.google-apps.folder"}
    f    = drive_svc.files().create(body=meta, fields="id").execute()
    return f["id"]


def generate_assets(
    plan: dict,
    config: dict,
    creds: Credentials,
    gemini_api_key: str,
    topic_folder: Path,
) -> dict:
    """Fase 2: Genera imágenes Gemini, renderiza tablas y sube todo a Drive."""
    print("\n🎨 Fase 2 — Generando assets …")

    drive_svc = build("drive", "v3", credentials=creds)
    folder_id = _ensure_drive_folder(drive_svc, f"edu-slides-{plan['meta']['topic_id']}")

    updated = []
    for slide in plan["slides"]:
        s = dict(slide)

        # ── Imagen de fondo ─────────────────────────────────────────────
        bg = dict(slide.get("background_image") or {})
        if bg.get("strategy") == "gemini" and bg.get("prompt") and bg.get("local_asset"):
            lp = topic_folder / bg["local_asset"]
            if not lp.exists():
                print(f"  🖼️  Generando fondo para {slide['id']} …")
                _gemini_image(bg["prompt"], lp, gemini_api_key)
            if lp.exists() and not bg.get("drive_id"):
                bg["drive_id"] = _upload_drive(drive_svc, lp, folder_id)
            s["background_image"] = bg

        # ── Imagen de contenido ─────────────────────────────────────────
        ci = dict(slide.get("content_image") or {})
        if ci.get("strategy") == "gemini" and ci.get("prompt") and ci.get("local_asset"):
            lp = topic_folder / ci["local_asset"]
            if not lp.exists():
                print(f"  🖼️  Generando imagen de contenido para {slide['id']} …")
                _gemini_image(ci["prompt"], lp, gemini_api_key)
            if lp.exists() and not ci.get("drive_id"):
                ci["drive_id"] = _upload_drive(drive_svc, lp, folder_id)
            s["content_image"] = ci

        # ── Tablas como PNG ─────────────────────────────────────────────
        updated_ta = []
        for ta in slide.get("table_assets") or []:
            ta = dict(ta)
            lp = topic_folder / ta["local_asset"]
            if not lp.exists() and ta.get("table_markdown"):
                print(f"  📊 Renderizando tabla {slide['id']}-table-{ta['index'] + 1} …")
                _render_table_png(ta["table_markdown"], lp, config)
            if lp.exists() and not ta.get("drive_id"):
                ta["drive_id"] = _upload_drive(drive_svc, lp, folder_id)
            updated_ta.append(ta)
        s["table_assets"] = updated_ta

        updated.append(s)

    plan = dict(plan)
    plan["slides"] = updated
    print("  ✅ Assets completados.")
    return plan


# ═══════════════════════════════════════════════════════════════════════
# FASE 3 — PUBLICACIÓN EN GOOGLE SLIDES
# ═══════════════════════════════════════════════════════════════════════

def _get_creds(secrets_path: Path, token_path: Path) -> Credentials:
    secrets   = load_yaml(secrets_path)
    creds_file = Path(secrets["google_credentials_path"])
    creds: Credentials | None = None

    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow  = InstalledAppFlow.from_client_secrets_file(str(creds_file), SCOPES)
            creds = flow.run_local_server(port=0)
        token_path.write_text(creds.to_json(), encoding="utf-8")
    return creds


def _copy_template(drive_svc, template_id: str, title: str) -> str:
    result = drive_svc.files().copy(fileId=template_id, body={"name": title}).execute()
    return result["id"]


def _clear_slides(slides_svc, pres_id: str) -> None:
    pres = slides_svc.presentations().get(presentationId=pres_id).execute()
    existing = pres.get("slides", [])
    if not existing:
        return
    reqs = [{"deleteObject": {"objectId": s["objectId"]}} for s in existing]
    slides_svc.presentations().batchUpdate(presentationId=pres_id, body={"requests": reqs}).execute()


def _drive_url(drive_id: str) -> str:
    return f"https://drive.google.com/uc?export=view&id={drive_id}"


def _build_slide_requests(slide: dict, config: dict, page_id: str, insert_idx: int) -> list:
    """Construye todos los requests de la API para una filmina."""
    reqs:    list[dict] = []
    palette  = config.get("palette", {})
    typo     = config.get("typography", {})
    primary  = palette.get("primary", "#8B0000")
    text_col = palette.get("text",    "#1A1A1A")
    bg_color = palette.get("background", "#FFFFFF")
    stype    = slide.get("type", "concepto-abstracto")
    layout   = slide.get("layout") or LAYOUT_MAP.get(stype, LAYOUT_MAP["concepto-abstracto"])

    counter  = [0]

    def nid(suffix: str = "") -> str:
        counter[0] += 1
        return f"{page_id}_e{counter[0]}_{suffix}"[:50]

    def add_box(geo: tuple[int, int, int, int], fill: str, outline: str | None = None, alpha: float | None = None) -> str:
        box_id = nid("box")
        x, y, w, h = geo
        solid_fill: dict[str, Any] = {"color": _rgb_color(fill)}
        if alpha is not None:
            solid_fill["alpha"] = alpha
        shape_props: dict[str, Any] = {
            "shapeBackgroundFill": {"solidFill": solid_fill},
        }
        # Google Slides no acepta solidFill directo en outline; el efecto de marco
        # se logra anidando cajas con distintos fondos.
        _ = outline
        shape_props["outline"] = {"propertyState": "NOT_RENDERED"}
        reqs.append({
            "createShape": {
                "objectId":  box_id,
                "shapeType": "RECTANGLE",
                "elementProperties": {
                    "pageObjectId": page_id,
                    "size":         _emu_size(w, h),
                    "transform":    _transform(x, y),
                },
            }
        })
        reqs.append({
            "updateShapeProperties": {
                "objectId": box_id,
                "shapeProperties": shape_props,
                "fields": "shapeBackgroundFill,outline",
            }
        })
        return box_id

    def add_textbox_geo(
        text: str,
        geo: tuple[int, int, int, int],
        size: float,
        bold: bool = False,
        italic: bool = False,
        color: str = "#1A1A1A",
        font: str = "Roboto",
        align: str = "LEFT",
    ) -> None:
        if not text.strip():
            return
        x, y, w, h = geo
        tb_id = nid("txt")
        reqs.append({
            "createShape": {
                "objectId":  tb_id,
                "shapeType": "TEXT_BOX",
                "elementProperties": {
                    "pageObjectId": page_id,
                    "size":         _emu_size(w, h),
                    "transform":    _transform(x, y),
                },
            }
        })
        reqs.append({"insertText": {"objectId": tb_id, "insertionIndex": 0, "text": text}})
        reqs.append({
            "updateTextStyle": {
                "objectId": tb_id,
                "style": {
                    "bold":            bold,
                    "italic":          italic,
                    "fontSize":        _pt(size),
                    "fontFamily":      font,
                    "foregroundColor": _color(color),
                },
                "textRange": {"type": "ALL"},
                "fields": "bold,italic,fontSize,fontFamily,foregroundColor",
            }
        })
        reqs.append({
            "updateParagraphStyle": {
                "objectId": tb_id,
                "style":    {"alignment": _normalize_alignment(align)},
                "textRange": {"type": "ALL"},
                "fields":   "alignment",
            }
        })

    def add_rich_textbox_geo(
        subtitle_text: str,
        blocks: list[dict],
        geo: tuple[int, int, int, int],
        size: float,
        color: str = "#1A1A1A",
        font: str = "Roboto",
        align: str = "LEFT",
    ) -> None:
        rich = _compose_rich_text(subtitle_text, blocks)
        rich_text = rich.get("text", "")
        if not rich_text.strip():
            return

        render_cfg = config.get("markdown_rendering", {}) or {}
        unordered_preset = render_cfg.get("unordered_bullet_preset", "BULLET_DISC_CIRCLE_SQUARE")
        ordered_preset = render_cfg.get("ordered_bullet_preset", "NUMBERED_DIGIT_ALPHA_ROMAN")
        code_font = render_cfg.get("inline_code_font", typo.get("code", {}).get("font", "Roboto Mono"))
        code_color = render_cfg.get("inline_code_color", primary)
        lead_scale = float(render_cfg.get("lead_scale", 1.08) or 1.08)
        heading_scale = float(render_cfg.get("heading_scale", 1.12) or 1.12)

        x, y, w, h = geo
        tb_id = nid("rich")
        reqs.append({
            "createShape": {
                "objectId":  tb_id,
                "shapeType": "TEXT_BOX",
                "elementProperties": {
                    "pageObjectId": page_id,
                    "size":         _emu_size(w, h),
                    "transform":    _transform(x, y),
                },
            }
        })
        reqs.append({"insertText": {"objectId": tb_id, "insertionIndex": 0, "text": rich_text}})
        reqs.append({
            "updateTextStyle": {
                "objectId": tb_id,
                "style": {
                    "fontSize":        _pt(size),
                    "fontFamily":      font,
                    "foregroundColor": _color(color),
                },
                "textRange": {"type": "ALL"},
                "fields": "fontSize,fontFamily,foregroundColor",
            }
        })
        reqs.append({
            "updateParagraphStyle": {
                "objectId": tb_id,
                "style":    {"alignment": _normalize_alignment(align)},
                "textRange": {"type": "ALL"},
                "fields":   "alignment",
            }
        })

        for bullet in rich.get("bullet_ranges", []):
            if bullet["end"] <= bullet["start"]:
                continue
            reqs.append({
                "createParagraphBullets": {
                    "objectId": tb_id,
                    "textRange": {
                        "type": "FIXED_RANGE",
                        "startIndex": bullet["start"],
                        "endIndex": bullet["end"],
                    },
                    "bulletPreset": ordered_preset if bullet.get("ordered") else unordered_preset,
                }
            })

        for emphasis in rich.get("emphasis_ranges", []):
            if emphasis["end"] <= emphasis["start"]:
                continue
            role = emphasis.get("role")
            scale = heading_scale if role == "heading" else lead_scale
            heading_size = round(size * scale, 1)
            reqs.append({
                "updateTextStyle": {
                    "objectId": tb_id,
                    "style": {
                        "bold": True,
                        "fontSize": _pt(heading_size),
                        "foregroundColor": _color(primary if role == "heading" else color),
                    },
                    "textRange": {
                        "type": "FIXED_RANGE",
                        "startIndex": emphasis["start"],
                        "endIndex": emphasis["end"],
                    },
                    "fields": "bold,fontSize,foregroundColor",
                }
            })

        for span in rich.get("spans", []):
            if span["end"] <= span["start"]:
                continue
            style: dict[str, Any] = {}
            fields: list[str] = []
            if span.get("bold"):
                style["bold"] = True
                fields.append("bold")
            if span.get("italic"):
                style["italic"] = True
                fields.append("italic")
            if span.get("code"):
                style["fontFamily"] = code_font
                style["foregroundColor"] = _color(code_color)
                fields.extend(["fontFamily", "foregroundColor"])
            if span.get("link"):
                style["link"] = {"url": span["link"]}
                fields.append("link")
            if not fields:
                continue
            reqs.append({
                "updateTextStyle": {
                    "objectId": tb_id,
                    "style": style,
                    "textRange": {
                        "type": "FIXED_RANGE",
                        "startIndex": span["start"],
                        "endIndex": span["end"],
                    },
                    "fields": ",".join(dict.fromkeys(fields)),
                }
            })

    # ── 1. Crear slide en blanco ────────────────────────────────────────
    reqs.append({
        "createSlide": {
            "objectId":         page_id,
            "insertionIndex":   insert_idx,
            "slideLayoutReference": {"predefinedLayout": "BLANK"},
        }
    })

    # ── 2. Fondo de slide ───────────────────────────────────────────────
    reqs.append({
        "updatePageProperties": {
            "objectId": page_id,
            "pageProperties": {
                "pageBackgroundFill": {"solidFill": {"color": _rgb_color(bg_color)}}
            },
            "fields": "pageBackgroundFill",
        }
    })

    def add_image(url: str, zone: str) -> None:
        geo = ZONES.get(zone)
        if not geo:
            return
        x, y, w, h = geo
        reqs.append({
            "createImage": {
                "objectId": nid("img"),
                "url":      url,
                "elementProperties": {
                    "pageObjectId": page_id,
                    "size":         _emu_size(w, h),
                    "transform":    _transform(x, y),
                },
            }
        })

    def add_bg_overlay(zone: str, opacity: float = 0.6) -> None:
        """Rectángulo blanco semitransparente encima de la imagen de fondo."""
        geo = ZONES.get(zone)
        if not geo:
            return
        x, y, w, h = geo
        ov_id = nid("overlay")
        reqs.append({
            "createShape": {
                "objectId":  ov_id,
                "shapeType": "RECTANGLE",
                "elementProperties": {
                    "pageObjectId": page_id,
                    "size":         _emu_size(w, h),
                    "transform":    _transform(x, y),
                },
            }
        })
        reqs.append({
            "updateShapeProperties": {
                "objectId": ov_id,
                "shapeProperties": {
                    "shapeBackgroundFill": {
                        "solidFill": {
                            "color": {"rgbColor": {"red": 1.0, "green": 1.0, "blue": 1.0}},
                            "alpha": opacity,
                        }
                    },
                    "outline": {"propertyState": "NOT_RENDERED"},
                },
                "fields": "shapeBackgroundFill,outline",
            }
        })

    def add_textbox(
        text:    str,
        zone:    str,
        size:    float,
        bold:    bool  = False,
        italic:  bool  = False,
        color:   str   = "#1A1A1A",
        font:    str   = "Roboto",
        align:   str   = "LEFT",
    ) -> None:
        geo = ZONES.get(zone)
        if not geo:
            return
        add_textbox_geo(text, geo, size, bold=bold, italic=italic, color=color, font=font, align=align)

    def add_native_table(table_md: str, zone: str) -> None:
        geo = ZONES.get(zone)
        if not geo:
            return
        rows = []
        for ln in table_md.strip().splitlines():
            clean = ln.replace("|", "").strip()
            if re.match(r"^[\-:\s]+$", clean):
                continue
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            rows.append(cells)
        if not rows:
            return
        n_cols = max(len(r) for r in rows)
        rows   = [r + [""] * (n_cols - len(r)) for r in rows]
        n_rows = len(rows)
        x, y, w, h = geo
        if zone == "table-main":
            y += 110_000
            h = max(360_000, h - 620_000)
        header_font = 13
        body_font = 12
        if n_rows >= 7:
            header_font = 10
            body_font = 9
        tbl_id = nid("tbl")
        reqs.append({
            "createTable": {
                "objectId": tbl_id,
                "elementProperties": {
                    "pageObjectId": page_id,
                    "size":         _emu_size(w, h),
                    "transform":    _transform(x, y),
                },
                "rows":    n_rows,
                "columns": n_cols,
            }
        })
        for r_idx, row in enumerate(rows):
            for c_idx, cell in enumerate(row):
                if not cell:
                    continue
                # Limpiar markdown de las celdas de tabla
                clean_cell = _strip_markdown(cell)
                reqs.append({
                    "insertText": {
                        "objectId":       tbl_id,
                        "cellLocation":   {"rowIndex": r_idx, "columnIndex": c_idx},
                        "insertionIndex": 0,
                        "text":           clean_cell,
                    }
                })
                if r_idx == 0:
                    reqs.append({
                        "updateTextStyle": {
                            "objectId":     tbl_id,
                            "cellLocation": {"rowIndex": r_idx, "columnIndex": c_idx},
                            "style": {
                                "bold":            True,
                                "foregroundColor": _color("#FFFFFF"),
                                "fontSize":        _pt(header_font),
                            },
                            "textRange": {"type": "ALL"},
                            "fields":    "bold,foregroundColor,fontSize",
                        }
                    })
                    reqs.append({
                        "updateTableCellProperties": {
                            "objectId": tbl_id,
                            "tableRange": {
                                "location":  {"rowIndex": r_idx, "columnIndex": c_idx},
                                "rowSpan":   1,
                                "columnSpan": 1,
                            },
                            "tableCellProperties": {
                                "tableCellBackgroundFill": {
                                    "solidFill": {"color": _rgb_color(primary)}
                                }
                            },
                            "fields": "tableCellBackgroundFill",
                        }
                    })
                else:
                    reqs.append({
                        "updateTextStyle": {
                            "objectId":     tbl_id,
                            "cellLocation": {"rowIndex": r_idx, "columnIndex": c_idx},
                            "style": {
                                "foregroundColor": _color(text_col),
                                "fontSize":        _pt(body_font),
                            },
                            "textRange": {"type": "ALL"},
                            "fields":    "foregroundColor,fontSize",
                        }
                    })

    # ── 3. Imagen de fondo ──────────────────────────────────────────────
    bg = slide.get("background_image") or {}
    if bg.get("drive_id"):
        add_image(_drive_url(bg["drive_id"]), "background")
        add_bg_overlay("background", opacity=0.6)

    # ── 4. Imagen de contenido ──────────────────────────────────────────
    ci = slide.get("content_image") or {}
    if ci.get("drive_id"):
        img_zone = layout.get("image", "right-half")
        if img_zone != "none":
            add_image(_drive_url(ci["drive_id"]), img_zone)

    # ── 5. Tablas (preferir nativas cuando entren bien) ─────────────────
    table_zone = layout.get("table", "full-bottom")
    ta_list    = slide.get("table_assets") or []
    tables     = slide.get("tables") or []

    if table_zone and table_zone != "none":
        if tables and _should_use_native_table(tables[0]):
            add_native_table(tables[0], table_zone)
        else:
            used_image = False
            for ta in ta_list:
                if ta.get("drive_id"):
                    add_image(_drive_url(ta["drive_id"]), table_zone)
                    used_image = True
                    break
            if not used_image and tables:
                add_native_table(tables[0], table_zone)

    # ── 6. Título ───────────────────────────────────────────────────────
    title      = slide.get("title", "")
    title_zone = layout.get("title", "left-top")
    t_size     = typo.get("title", {}).get("size", 36)
    if stype == "portada":
        t_size = 36
    if len(title) > 42:
        t_size = min(t_size, 32)
    if len(title) > 60:
        t_size = min(t_size, 28)
    title_geo = ZONES.get(title_zone)
    if title_geo and title:
        min_title_size = 24 if stype == "portada" else 20
        t_size = _fit_text_font_size(title, title_geo, t_size, min_size=min_title_size)
    t_align    = "CENTER" if "center" in str(title_zone) else "LEFT"
    t_align    = _normalize_alignment(t_align)
    add_textbox(title, title_zone, t_size, bold=True, color=primary, align=t_align)

    # ── 7. Subtítulo (portada) ──────────────────────────────────────────
    subtitle = slide.get("subtitle", "")
    if subtitle and stype == "portada":
        s_size = typo.get("subtitle", {}).get("size", 24)
        add_textbox(subtitle, "center-middle", s_size, color=text_col, align="CENTER")

    # ── 8. Cuerpo (texto + listas) ──────────────────────────────────────
    body_zone = layout.get("body", "left-middle")
    body_subtitle = slide.get("subtitle", "") if stype != "portada" else ""
    if body_zone not in ("none", "subtitle-only"):
        body_blocks = slide.get("body_blocks") or []
        body_txt = _compose_body_text(body_subtitle, body_blocks)
        b_size   = typo.get("body", {}).get("size", 18)
        if body_zone == "table-intro":
            b_size = min(b_size, 13)
        if body_zone == "left-top-split":
            b_size = min(b_size, 15)
        body_geo = ZONES.get(body_zone)
        if body_geo and body_txt:
            b_size = _fit_text_font_size(body_txt, body_geo, b_size, min_size=10)
        if body_geo:
            add_rich_textbox_geo(body_subtitle, body_blocks, body_geo, b_size, color=text_col)
    elif body_zone == "subtitle-only" and subtitle:
        b_size = typo.get("body", {}).get("size", 18)
        add_textbox(subtitle, "subtitle-only", b_size, color=text_col)

    # ── 9. Código ───────────────────────────────────────────────────────
    code_zone  = layout.get("code", "none")
    code_blocks = slide.get("code_blocks") or []
    if code_zone != "none" and code_blocks:
        code_geo = ZONES.get(code_zone)
        code_text = "\n\n".join(cb['content'] for cb in code_blocks)
        c_size = typo.get("code", {}).get("size", 14)
        if code_geo and _looks_like_ascii_diagram(code_text):
            diagram_geo = _centered_box(code_geo, 0.78, 0.55)
            add_box(diagram_geo, "#F4F4F4", outline="#D8D8D8")
            inner_geo = _inset_geometry(diagram_geo, 140_000, 110_000)
            c_size = _fit_code_font_size(code_text, inner_geo, max(c_size + 6, 20), min_size=14)[0]
            add_textbox_geo(code_text, inner_geo, c_size, font="Roboto Mono", color="#222222")
        else:
            if code_geo:
                add_box(code_geo, "#F4F4F4", outline="#D8D8D8")
            inner_geo = _inset_geometry(code_geo, 170_000, 130_000) if code_geo else None
            if inner_geo:
                dense_code = len(code_text.splitlines()) > 12 or max((len(line) for line in code_text.splitlines()), default=0) > 52
                c_size, needs_inner_frame = _fit_code_font_size(code_text, inner_geo, c_size, min_size=5)
                if needs_inner_frame or dense_code:
                    inner_geo = _inset_geometry(code_geo, 280_000, 210_000)
                    add_box(inner_geo, "#FFFFFF", outline="#C8C8C8")
                    c_size, _ = _fit_code_font_size(code_text, inner_geo, min(c_size, typo.get("code", {}).get("size", 14)), min_size=5)
                add_textbox_geo(code_text, inner_geo, c_size, font="Roboto Mono", color="#222222")

    return reqs


def _blocks_to_text(blocks: list[dict]) -> str:
    lines = []
    for b in blocks:
        if b.get("type") == "text":
            lines.append(_strip_markdown(b["content"]))
        elif b.get("type") == "heading":
            lines.append(_strip_markdown(b["content"]))
        elif b.get("type") == "list":
            for item in b.get("items", []):
                text, _level = _list_item_parts(item)
                if text:
                    lines.append(text)
    return "\n".join(lines)


def publish_slides(plan: dict, config: dict, creds: Credentials, topic_folder: Path) -> str:
    """Fase 3: Crea presentación en Google Slides desde el plan. Devuelve la URL."""
    print("\n🚀 Fase 3 — Publicando en Google Slides …")

    drive_svc  = build("drive", "v3", credentials=creds)
    slides_svc = build("slides", "v1", credentials=creds)

    template_id = plan["meta"]["template_id"]
    title       = plan["meta"]["title"]

    print(f"  Copiando plantilla {template_id} …")
    pres_id = _copy_template(drive_svc, template_id, title)
    print(f"  Presentación creada: {pres_id}")

    _clear_slides(slides_svc, pres_id)

    all_reqs: list[dict] = []
    for idx, slide in enumerate(plan["slides"]):
        page_id  = f"slide_{slide['id'].replace('-', '_')}"
        reqs     = _build_slide_requests(slide, config, page_id, idx)
        all_reqs.extend(reqs)

    BATCH = 50
    total = len(all_reqs)
    failed_batches: list[str] = []
    print(f"  Enviando {total} requests en lotes de {BATCH} …")
    for i in range(0, total, BATCH):
        batch = all_reqs[i : i + BATCH]
        label = f"Lote {i // BATCH + 1}/{(total + BATCH - 1) // BATCH}"
        try:
            slides_svc.presentations().batchUpdate(
                presentationId=pres_id, body={"requests": batch}
            ).execute()
            print(f"  {label} ✓")
        except Exception as exc:
            print(f"  ⚠️  Error en {label}: {exc}")
            failed_batches.append(f"{label}: {exc}")

    if failed_batches:
        print(f"  ⚠️  {len(failed_batches)} lote(s) fallaron — la presentación quedó incompleta:")
        for msg in failed_batches:
            print(f"     • {msg}")
        raise RuntimeError("Publish incompleto: uno o más lotes de Google Slides fallaron")

    # ── Limpieza: elimina textos del template que quedaron en los slides ─
    _TEMPLATE_TEXTS = {
        "portada", "the uncomfortable question",
        "the uncomfistable question", "what is a paradigmm?",
        "the factors that shaped poradgms",
    }
    try:
        pres = slides_svc.presentations().get(presentationId=pres_id).execute()
        del_reqs: list[dict] = []
        for s in pres.get("slides", []):
            for el in s.get("pageElements", []):
                txt_data = (el.get("shape") or {}).get("text") or {}
                content = "".join(
                    e.get("textRun", {}).get("content", "")
                    for e in txt_data.get("textElements", [])
                    if "textRun" in e
                ).strip().lower()
                if content in _TEMPLATE_TEXTS:
                    del_reqs.append({"deleteObject": {"objectId": el["objectId"]}})
        if del_reqs:
            slides_svc.presentations().batchUpdate(
                presentationId=pres_id, body={"requests": del_reqs}
            ).execute()
            print(f"  🗑️  Eliminados {len(del_reqs)} textos residuales del template.")
    except Exception as exc:
        print(f"  ⚠️  No se pudo limpiar textos del template: {exc}")

    url      = f"https://docs.google.com/presentation/d/{pres_id}/edit"
    url_path = topic_folder / "slides" / "slides-url.txt"
    url_path.parent.mkdir(parents=True, exist_ok=True)
    url_path.write_text(url, encoding="utf-8")

    print(f"  ✅ URL: {url}")
    return url


# ═══════════════════════════════════════════════════════════════════════
# PUNTO DE ENTRADA
# ═══════════════════════════════════════════════════════════════════════

def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="EDU Slides Pipeline — YAML de publicación → Google Slides",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "topic_folder",
        help="Ruta a la carpeta del tema (ej: salida/cursadas/2026/temas/01-conceptos-introductorios)",
    )
    parser.add_argument("--plan-only",    action="store_true", help="Solo valida los YAML de publicación")
    parser.add_argument("--regen-plan",   action="store_true", help="Regenera plan-filminas YAML desde filminas.md")
    parser.add_argument("--assets-only",  action="store_true", help="Solo genera assets (requiere plan previo)")
    parser.add_argument("--publish-only", action="store_true", help="Solo publica (requiere plan + assets)")
    args = parser.parse_args(argv)

    topic_folder = Path(args.topic_folder).resolve()
    if not topic_folder.is_dir():
        print(f"❌ El directorio no existe: {topic_folder}")
        sys.exit(1)

    project_root = find_project_root(topic_folder)

    secrets_path  = project_root / "_edu" / "secrets.local.yaml"
    config_path   = project_root / "_edu" / "slides-config.yaml"
    token_path    = project_root / "_edu" / "token_slides.json"
    plan_name     = f"plan-filminas-{topic_folder.name}.yaml"
    plan_path     = topic_folder / "slides" / plan_name
    assets_manifest_path = topic_folder / "slides" / "assets-manifest.yaml"
    publish_context_path = topic_folder / "slides" / "publish-context.yaml"

    required_paths = [(config_path, "_edu/slides-config.yaml")]
    if not args.plan_only and not args.regen_plan:
        required_paths.insert(0, (secrets_path, "_edu/secrets.local.yaml"))

    # Verificar prerequisitos
    for p, label in required_paths:
        if not p.exists():
            print(f"❌ Falta {label} en {p}")
            if label == "_edu/secrets.local.yaml":
                print("   Ejecutar /edu-setup-apis y /edu-slides-designer primero.")
            else:
                print("   Ejecutar /edu-slides-designer primero.")
            sys.exit(1)

    config  = load_yaml(config_path)
    secrets = load_yaml(secrets_path) if secrets_path.exists() else {}
    gemini_key   = secrets.get("gemini_api_key", "")
    template_id  = config.get("template_id", "")

    # ── --regen-plan: DEPRECADO — redirige a parse_filminas.py (v2) ──────────
    if args.regen_plan:
        print("⚠️  DEPRECADO: --regen-plan")
        print("   El flujo v2 usa scripts/parse_filminas.py para generar el plan DRAFT.")
        print("   parse_filminas.py produce type: pending para slides sin @tipo: explícito.")
        print("   El agente completa los tipos y prompts. validate_plan.py verifica el contrato.\n")
        filminas_path = topic_folder / "filminas.md"
        if not filminas_path.exists():
            print(f"❌ No se encontró filminas.md en {topic_folder}")
            sys.exit(1)
        parse_script = Path(__file__).parent / "parse_filminas.py"
        if parse_script.exists():
            import subprocess as _sp
            result = _sp.run([sys.executable, str(parse_script), str(topic_folder)], check=False)
            sys.exit(result.returncode)
        # Fallback: comportamiento legacy (si parse_filminas.py no existe aún)
        print("   (parse_filminas.py no encontrado — usando generate_plan() legacy)")
        if not template_id:
            print("❌ template_id no configurado en slides-config.yaml")
            sys.exit(1)
        new_plan = generate_plan(filminas_path, config, template_id)
        plan_path.parent.mkdir(parents=True, exist_ok=True)
        save_yaml(plan_path, new_plan)
        print(f"  📄 Plan regenerado (legacy): {plan_path.relative_to(project_root)}")
        print(f"     {new_plan['meta']['total_slides']} filminas, {new_plan['meta']['images_planned']} imágenes.")
        print("\n✅ Plan listo (legacy). Verificar con validate_plan.py antes de ejecutar.")
        return

    # ── Fase 1: Validar artefactos generados por el agente ────────────────
    try:
        plan = validate_publish_artifacts(topic_folder, plan_path, assets_manifest_path, publish_context_path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"❌ {exc}")
        print("   Ejecutar primero el prompt/agente que genera los YAML de publicación.")
        sys.exit(1)

    print(f"  📄 Plan cargado desde: {plan_path.relative_to(project_root)}")
    if args.plan_only:
        print("\n✅ Artefactos validados. Podés ejecutar sin --plan-only para generar assets y publicar.")
        return

    # ── Autenticar con Google ─────────────────────────────────────────────
    creds = _get_creds(secrets_path, token_path)

    # ── Fase 2: Generar assets ─────────────────────────────────────────────
    if not args.publish_only:
        plan = generate_assets(plan, config, creds, gemini_key, topic_folder)
        save_yaml(plan_path, plan)
        print(f"  📄 Plan actualizado con drive_ids: {plan_path.relative_to(project_root)}")
        if args.assets_only:
            print("\n✅ Assets generados. Ejecutar con --publish-only para publicar.")
            return

    # ── Fase 3: Publicar ─────────────────────────────────────────────────
    url = publish_slides(plan, config, creds, topic_folder)

    print(f"""
🎉 Pipeline completado!
   Tema:    {plan['meta']['title']}
   Slides:  {plan['meta']['total_slides']}
   Plan:    {plan_path.relative_to(project_root)}
   URL:     {url}
""")


if __name__ == "__main__":
    main()
