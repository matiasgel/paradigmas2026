#!/usr/bin/env python3
"""
EDU Slides Pipeline — Módulo EDU
=================================
Convierte filminas.md → plan YAML → assets (imágenes/tablas) → Google Slides.

Fases:
  1. plan    — Lee filminas.md y genera plan-filminas-{tema}.yaml con contenido
               completo y directrices de layout + prompts de imagen.
  2. assets  — Genera imágenes con Gemini, renderiza tablas como PNG,
               sube todo a Google Drive.
  3. publish — Lee el plan + assets y crea la presentación en Google Slides.

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

# Dimensiones estándar 16:9 en EMU (English Metric Units)
SLIDE_W = 9_144_000
SLIDE_H = 5_143_500
MARGIN = 457_200    # ~0.5 pulgada
TITLE_H = 1_400_000  # alto reservado para título (2 líneas de 46pt)

# Estrategia de imagen por tipo de filmina
IMAGE_STRATEGY: dict[str, str] = {
    "portada":           "background",  # imagen de fondo full-slide
    "cierre":            "background",
    "socratica":         "background",
    "concepto-abstracto": "content",    # imagen en panel derecho
    "diagrama":          "content",
    "timeline":          "content",
    "codigo":            "none",
    "tabla":             "none",
    "tabla-comparativa": "none",
    "demo":              "none",
}

# Directrices de layout por tipo
LAYOUT_MAP: dict[str, dict] = {
    "portada":            {"title": "center-middle",  "body": "center-bottom", "image": "background", "code": "none", "table": "none"},
    "concepto-abstracto": {"title": "full-title",     "body": "left-middle",   "image": "right-half", "code": "none", "table": "none"},
    "codigo":             {"title": "full-title",     "body": "subtitle-only", "image": "none",       "code": "full-bottom", "table": "none"},
    "tabla":              {"title": "full-title",     "body": "none",          "image": "none",       "code": "none", "table": "full-bottom"},
    "tabla-comparativa":  {"title": "full-title",     "body": "none",          "image": "none",       "code": "none", "table": "full-bottom"},
    "diagrama":           {"title": "full-title",     "body": "left-middle",   "image": "right-half", "code": "none", "table": "none"},
    "socratica":          {"title": "center-top",     "body": "center-middle", "image": "background", "code": "none", "table": "none"},
    "demo":               {"title": "full-title",     "body": "left-middle",   "image": "none",       "code": "right-half", "table": "none"},
    "cierre":             {"title": "center-middle",  "body": "center-bottom", "image": "background", "code": "none", "table": "none"},
    "timeline":           {"title": "full-title",     "body": "full-center",   "image": "none",       "code": "none", "table": "none"},
}

# Geometría de zonas en EMU: (x, y, width, height)
def _zones(w: int = SLIDE_W, h: int = SLIDE_H, m: int = MARGIN, th: int = TITLE_H) -> dict[str, tuple]:
    half_w = w // 2
    body_y = m + th + 80_000
    body_h = h - body_y - m
    return {
        "full-title":    (m,            m,            w - 2 * m,       th),        # ancho completo
        "left-top":      (m,            m,            half_w - m,      th),        # media anchura
        "center-top":    (m,            m,            w - 2 * m,       th),
        "center-middle": (m,            h // 3,       w - 2 * m,       h // 3),
        "center-bottom": (m,            h * 2 // 3,   w - 2 * m,       h // 3 - m),
        "left-middle":   (m,            body_y,       half_w - m,      body_h),
        "left-half":     (m,            body_y,       half_w - m,      body_h),
        "right-half":    (half_w + m,   body_y,       half_w - 2 * m,  body_h),
        "full-bottom":   (m,            body_y,       w - 2 * m,       body_h),
        "full-center":   (m,            m,            w - 2 * m,       h - 2 * m),
        "subtitle-only": (m,            body_y,       w - 2 * m,       th // 2),
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


# ═══════════════════════════════════════════════════════════════════════
# FASE 1 — PARSEO DE FILMINAS.MD
# ═══════════════════════════════════════════════════════════════════════

def parse_filminas(filminas_path: Path) -> list[dict]:
    """Lee filminas.md y extrae cada slide como estructura semántica completa."""
    text = filminas_path.read_text(encoding="utf-8")
    slides: list[dict] = []
    current: dict | None = None

    for line in text.splitlines():
        m = re.match(r"^###\s+\[F-(\d+)\]\s*(.*)$", line)
        if m:
            if current:
                slides.append(_finalize_slide(current))
            current = {
                "id":          f"F-{m.group(1).zfill(2)}",
                "raw_title":   m.group(2).strip(),
                "raw_lines":   [],
            }
        elif current is not None:
            current["raw_lines"].append(line)

    if current:
        slides.append(_finalize_slide(current))

    return slides


def _finalize_slide(raw: dict) -> dict:
    """Parsea raw_lines en bloques semánticos: subtitle, body_blocks, code_blocks, tables."""
    lines       = raw["raw_lines"]
    subtitle    = ""
    body_blocks: list[dict] = []
    code_blocks: list[dict] = []
    tables:      list[str]  = []

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

        # ── Tabla Markdown ──────────────────────────────────────────────
        if line.strip().startswith("|"):
            tbl_lines = [line]
            i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl_lines.append(lines[i])
                i += 1
            tables.append("\n".join(tbl_lines))
            continue

        # ── Saltar secciones del documento (## BLOQUE …, ### etc.) ────────
        if re.match(r'^#{2,}', line):
            i += 1
            continue

        # ── Subtitle (# heading) ────────────────────────────────────────
        m_h = re.match(r"^#\s+(.+)$", line)
        if m_h and not subtitle:
            subtitle = m_h.group(1).strip()
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
        if re.match(r"^[-*•]|\d+\.", first):
            items = []
            for bl in block_lines:
                # Strip bullet prefix correctamente: "- text", "* text", "• text", "1. text"
                stripped = re.sub(r'^\s*[-*•]\s+', '', bl)
                stripped = re.sub(r'^\s*\d+[.)]\s+', '', stripped).strip()
                if stripped:
                    items.append(stripped)
            if items:
                body_blocks.append({"type": "list", "items": items})
        else:
            combined = "\n".join(block_lines)
            body_blocks.append({"type": "text", "content": combined})

    return {
        "id":          raw["id"],
        "type":        _detect_type(raw["id"], raw["raw_title"], body_blocks, code_blocks, tables),
        "title":       raw["raw_title"],
        "subtitle":    subtitle,
        "body_blocks": body_blocks,
        "code_blocks": code_blocks,
        "tables":      tables,
    }


def _detect_type(slide_id: str, title: str, body_blocks, code_blocks, tables) -> str:
    num = int(slide_id.split("-")[1])
    if num == 0:
        return "portada"
    if code_blocks:
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

def _image_prompt(slide: dict, config: dict) -> str:
    """Genera un prompt Gemini para imagen de fondo o contenido."""
    title     = slide.get("title", "")
    stype     = slide.get("type", "concepto-abstracto")
    palette   = config.get("palette", {})
    primary   = palette.get("primary", "#8B0000")

    # Resumen del cuerpo (primeras 150 chars)
    body_text = ""
    for b in slide.get("body_blocks", []):
        if b["type"] == "text":
            body_text += " " + b["content"]
        elif b["type"] == "list":
            body_text += " " + " — ".join(b["items"][:3])
    body_text = body_text.strip()[:150]

    style = (
        "flat design académico, sin texto, sin palabras, sin letras, sin números, "
        "sin código, sin captions, sin watermarks, sin labels, "
        "no text, no words, no letters, no numbers, no captions, no watermarks, no labels, "
        "paleta rojo granate institucional y gris oscuro sobre fondo blanco, alta resolución"
    )

    if stype == "portada":
        return (
            f"Composición visual abstracta: paradigmas de programación, código, "
            f"lenguajes de software, fondo institucional elegante. {style}"
        )
    if stype == "cierre":
        return f"Imagen motivacional académica de finalización y aprendizaje. {style}"
    if stype == "socratica":
        return (
            f"Imagen minimalista evocadora para reflexión sobre: «{title}». "
            f"Mucho espacio negativo, composición centralizada. {style}"
        )
    if stype == "diagrama":
        return (
            f"Diagrama abstracto conceptual representando: «{title}». "
            f"Flechas, nodos, conexiones. {style}"
        )
    if stype == "timeline":
        return (
            f"Fondo abstracto representando evolución temporal en computación. "
            f"Décadas, hitos, tecnología. {style}"
        )
    # concepto-abstracto, default
    context = body_text[:80] if body_text else title
    return (
        f"Ilustración académica que representa conceptualmente: «{title}». "
        f"Contexto: {context}. {style}"
    )


def generate_plan(filminas_path: Path, config: dict, template_id: str) -> dict:
    """Fase 1: filminas.md → plan-filminas-{tema}.yaml."""
    print("📋 Fase 1 — Generando plan desde filminas.md …")

    slides      = parse_filminas(filminas_path)
    topic_id    = filminas_path.parent.name
    topic_title = slides[0]["title"] if slides else topic_id.replace("-", " ").title()

    # Budget de imágenes: máximo 8 por presentación
    max_images  = int(config.get("gemini_image_strategy", {}).get("max_per_presentation", 8) or 8)
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
        layout   = LAYOUT_MAP.get(slide["type"], LAYOUT_MAP["concepto-abstracto"])
        strategy = assigned[slide["id"]]

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
            "generated_at":  datetime.now().isoformat(timespec="seconds"),
            "template_id":   template_id,
            "total_slides":  len(slides),
            "images_planned": img_count,
        },
        "slides": plan_slides,
    }

    print(f"  ✅ {len(slides)} filminas procesadas, {img_count} imágenes planificadas.")
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
        if not geo or not text.strip():
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
        reqs.append({
            "updateShapeProperties": {
                "objectId": tb_id,
                "shapeProperties": {
                    "autoFit": {"autoFitType": "SHAPE_AUTO_FIT"}
                },
                "fields": "autoFit",
            }
        })

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
                                "fontSize":        _pt(13),
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
                                "fontSize":        _pt(12),
                            },
                            "textRange": {"type": "ALL"},
                            "fields":    "foregroundColor,fontSize",
                        }
                    })

    # ── 3. Imagen de fondo ──────────────────────────────────────────────
    bg = slide.get("background_image") or {}
    if bg.get("drive_id"):
        add_image(_drive_url(bg["drive_id"]), "background")

    # ── 4. Imagen de contenido ──────────────────────────────────────────
    ci = slide.get("content_image") or {}
    if ci.get("drive_id"):
        img_zone = layout.get("image", "right-half")
        if img_zone != "none":
            add_image(_drive_url(ci["drive_id"]), img_zone)

    # ── 5. Tablas (imagen desde Drive o native) ─────────────────────────
    table_zone = layout.get("table", "full-bottom")
    ta_list    = slide.get("table_assets") or []
    tables     = slide.get("tables") or []

    if table_zone and table_zone != "none":
        used_image = False
        for ta in ta_list:
            if ta.get("drive_id"):
                add_image(_drive_url(ta["drive_id"]), table_zone)
                used_image = True
                break    # una sola tabla por zona
        if not used_image and tables:
            add_native_table(tables[0], table_zone)

    # ── 6. Título ───────────────────────────────────────────────────────
    title      = slide.get("title", "")
    title_zone = layout.get("title", "left-top")
    t_size     = typo.get("title", {}).get("size", 36)
    if stype == "portada":
        t_size = 48
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
    if body_zone not in ("none", "subtitle-only"):
        body_txt = _blocks_to_text(slide.get("body_blocks") or [])
        b_size   = typo.get("body", {}).get("size", 18)
        add_textbox(body_txt, body_zone, b_size, color=text_col)
    elif body_zone == "subtitle-only" and subtitle:
        b_size = typo.get("body", {}).get("size", 18)
        add_textbox(subtitle, "subtitle-only", b_size, color=text_col)

    # ── 9. Código ───────────────────────────────────────────────────────
    code_zone  = layout.get("code", "none")
    code_blocks = slide.get("code_blocks") or []
    if code_zone != "none" and code_blocks:
        code_geo = ZONES.get(code_zone)
        if code_geo:
            # Fondo gris para el bloque de código
            bx, by, bw, bh = code_geo
            bg_id = nid("codebg")
            reqs.append({
                "createShape": {
                    "objectId":  bg_id,
                    "shapeType": "RECTANGLE",
                    "elementProperties": {
                        "pageObjectId": page_id,
                        "size":         _emu_size(bw, bh),
                        "transform":    _transform(bx, by),
                    },
                }
            })
            reqs.append({
                "updateShapeProperties": {
                    "objectId": bg_id,
                    "shapeProperties": {
                        "shapeBackgroundFill": {
                            "solidFill": {"color": _rgb_color("#F4F4F4")}
                        }
                    },
                    "fields": "shapeBackgroundFill",
                }
            })
        # Solo el contenido del código, sin marcadores de lenguaje
        code_text = "\n\n".join(cb['content'] for cb in code_blocks)
        c_size = typo.get("code", {}).get("size", 14)
        add_textbox(code_text, code_zone, c_size, font="Roboto Mono", color="#222222")

    return reqs


def _blocks_to_text(blocks: list[dict]) -> str:
    lines = []
    for b in blocks:
        if b.get("type") == "text":
            lines.append(_strip_markdown(b["content"]))
        elif b.get("type") == "list":
            lines.extend(f"• {_strip_markdown(item)}" for item in b.get("items", []))
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
        print(f"  ⚠️  {len(failed_batches)} lote(s) fallaron — la presentación puede estar incompleta:")
        for msg in failed_batches:
            print(f"     • {msg}")

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
        description="EDU Slides Pipeline — filminas.md → Google Slides",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "topic_folder",
        help="Ruta a la carpeta del tema (ej: salida/cursadas/2026/temas/01-conceptos-introductorios)",
    )
    parser.add_argument("--plan-only",    action="store_true", help="Solo genera el plan YAML")
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
    filminas_path = topic_folder / "filminas.md"
    plan_name     = f"plan-filminas-{topic_folder.name}.yaml"
    plan_path     = topic_folder / "slides" / plan_name

    # Verificar prerequisitos
    for p, label in [(secrets_path, "_edu/secrets.local.yaml"), (config_path, "_edu/slides-config.yaml")]:
        if not p.exists():
            print(f"❌ Falta {label} en {p}")
            print("   Ejecutar /edu-setup-apis y /edu-slides-designer primero.")
            sys.exit(1)

    config  = load_yaml(config_path)
    secrets = load_yaml(secrets_path)
    gemini_key   = secrets.get("gemini_api_key", "")
    template_id  = config.get("template_id", "")

    # ── Fase 1: Generar plan ─────────────────────────────────────────────
    if not args.assets_only and not args.publish_only:
        if not filminas_path.exists():
            print(f"❌ No se encontró filminas.md en: {filminas_path}")
            sys.exit(1)
        plan = generate_plan(filminas_path, config, template_id)
        save_yaml(plan_path, plan)
        print(f"  📄 Plan guardado en: {plan_path.relative_to(project_root)}")
        if args.plan_only:
            print("\n✅ Plan generado. Podés revisarlo y luego ejecutar sin --plan-only para publicar.")
            return
    else:
        if not plan_path.exists():
            print(f"❌ No se encontró el plan en: {plan_path}")
            print(f"   Ejecutar primero sin --assets-only / --publish-only.")
            sys.exit(1)
        plan = load_yaml(plan_path)

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
