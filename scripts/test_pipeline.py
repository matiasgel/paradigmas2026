#!/usr/bin/env python3
"""
EDU Slides Pipeline — Test Runner de Integración
=================================================
Ejecuta el pipeline completo de creación de filminas como test de integración,
usando informe/filminas.md como fuente de referencia y generando un reporte
completo con capturas de cada filmina.

Estructura del reporte generado:
  {project-root}/reporte/test{YYYYMMDD_HHMMSS}/
    filminas.md           — copia del filminas.md usado como entrada
    slides-config.yaml    — copia del slides-config.yaml utilizado
    test-meta.yaml        — metadatos del run (timings, resultados, errores)
    tema-test/            — carpeta de trabajo del pipeline
      slides/             — artefactos generados
        plan-filminas-tema-test.yaml
        assets/           — imágenes IA + tablas PNG generadas
          F-00-bg.png
          F-01-bg.png
          ...
    filminas/             — capturas de pantalla de Google Slides
      filmina_00.png
      filmina_01.png
      ...
    report.html           — informe visual con thumbnails y estado de cada fase

Fases del test:
  1. Setup        — copia artefactos de referencia, crea estructura
  2. Plan         — ejecuta Fase 1 del pipeline (parse filminas.md → plan YAML)
  3. Assets       — ejecuta Fase 2 del pipeline (Imagen 4.0 + tablas matplotlib)
  4. Publish      — ejecuta Fase 3 del pipeline (crea presentación en Google Slides)
  5. Screenshots  — descarga capturas de slides via Google Slides API
  6. Report       — genera report.html + test-meta.yaml

Uso:
  python test_pipeline.py                          # test completo
  python test_pipeline.py --plan-only              # solo Fase 1 (sin Google APIs)
  python test_pipeline.py --no-images              # sin generación de imágenes IA
  python test_pipeline.py --from RUTA/filminas.md  # usar filminas.md alternativo
  python test_pipeline.py --reuse-plan RUTA        # reutilizar plan existente

Requiere:
  - _edu/secrets.local.yaml (credentials Google + gemini_api_key)
  - _edu/slides-config.yaml (sistema de diseño)
  - pip install -r requirements.txt
"""

from __future__ import annotations

import argparse
import base64
import shutil
import subprocess
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

# ══════════════════════════════════════════════════════════════════════
# Constantes
# ══════════════════════════════════════════════════════════════════════

SCOPES = [
    "https://www.googleapis.com/auth/presentations",
    "https://www.googleapis.com/auth/drive",
]

TOPIC_NAME = "tema-test"

# Colores de terminal
def _ok(msg: str)   -> None: print(f"\033[0;32m✅ {msg}\033[0m")
def _warn(msg: str) -> None: print(f"\033[1;33m⚠️  {msg}\033[0m")
def _err(msg: str)  -> None: print(f"\033[0;31m❌ {msg}\033[0m")
def _info(msg: str) -> None: print(f"   ℹ  {msg}")
def _step(n: int, msg: str) -> None: print(f"\n\033[1;34m[{n}/6] {msg}\033[0m")

# ══════════════════════════════════════════════════════════════════════
# Utilidades
# ══════════════════════════════════════════════════════════════════════

def find_project_root(start: Path) -> Path:
    cur = start.resolve()
    standalone_candidate: Path | None = None
    for _ in range(10):
        if (cur / ".git").exists() or (cur / "module.yaml").exists():
            return cur
        # Recordar como candidato standalone pero seguir buscando .git
        if standalone_candidate is None and (cur / "_edu").exists() and (cur / "scripts").exists():
            standalone_candidate = cur
        if cur == cur.parent:
            break
        cur = cur.parent
    if standalone_candidate:
        return standalone_candidate
    raise FileNotFoundError(f"Raíz del proyecto no encontrada desde {start}")


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def save_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)


def _get_creds(secrets_path: Path, token_path: Path) -> Credentials:
    secrets    = load_yaml(secrets_path)
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


# ══════════════════════════════════════════════════════════════════════
# FASE 1 — Setup del directorio de reporte
# ══════════════════════════════════════════════════════════════════════

def setup_test_dir(
    project_root: Path,
    source_filminas: Path,
    source_config: Path,
) -> tuple[Path, Path, dict]:
    """
    Crea la estructura de directorios del reporte y copia los artefactos de
    referencia. Devuelve (test_dir, topic_folder, meta).
    """
    ts       = datetime.now().strftime("%Y%m%d_%H%M%S")
    test_dir = project_root / "reporte" / f"test{ts}"
    test_dir.mkdir(parents=True, exist_ok=True)

    # Copiar artefactos de referencia al directorio raíz del test
    dest_filminas = test_dir / "filminas.md"
    dest_config   = test_dir / "slides-config.yaml"
    shutil.copy2(source_filminas, dest_filminas)
    shutil.copy2(source_config,   dest_config)

    # Carpeta de trabajo del pipeline (simula una carpeta de tema)
    topic_folder = test_dir / TOPIC_NAME
    topic_folder.mkdir(parents=True, exist_ok=True)

    # Dentro del tema, el pipeline espera un filminas.md
    (topic_folder / "filminas.md").write_bytes(dest_filminas.read_bytes())

    # Crear subcarpetas esperadas
    (test_dir / "filminas").mkdir(exist_ok=True)

    meta: dict = {
        "test_run_id":     ts,
        "started_at":      datetime.now().isoformat(timespec="seconds"),
        "source_filminas": str(source_filminas.relative_to(project_root)),
        "source_config":   str(source_config.relative_to(project_root)),
        "test_dir":        str(test_dir.relative_to(project_root)),
        "phases": {
            "setup":       {"status": "ok",     "elapsed_s": 0},
            "plan":        {"status": "pending", "elapsed_s": 0, "slides": 0},
            "assets":      {"status": "pending", "elapsed_s": 0},
            "publish":     {"status": "pending", "elapsed_s": 0, "presentation_url": ""},
            "screenshots": {"status": "pending", "elapsed_s": 0, "count": 0},
            "report":      {"status": "pending", "elapsed_s": 0},
        },
        "errors": [],
    }

    _ok(f"Directorio de reporte creado: reporte/test{ts}/")
    return test_dir, topic_folder, meta


# ══════════════════════════════════════════════════════════════════════
# FASE 2 — Ejecutar pipeline (plan + assets + publish)
# ══════════════════════════════════════════════════════════════════════

def _run_pipeline_phase(
    pipeline_script: Path,
    topic_folder: Path,
    flag: str | None,
    python_bin: str,
) -> tuple[bool, str]:
    """Ejecuta una fase del pipeline como subproceso. Devuelve (ok, output)."""
    cmd = [python_bin, str(pipeline_script), str(topic_folder)]
    if flag:
        cmd.append(flag)
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode == 0, output


def run_pipeline(
    project_root: Path,
    topic_folder: Path,
    meta: dict,
    plan_only: bool,
    no_images: bool,
    reuse_plan: Path | None,
    python_bin: str,
) -> tuple[bool, str | None]:
    """
    Ejecuta las 3 fases del pipeline completo.
    Devuelve (ok, presentation_id_or_None).
    """
    pipeline = project_root / "salida" / "edu-standalone" / "scripts" / "slides_pipeline.py"
    if not pipeline.exists():
        # Modo standalone: el script está en el mismo directorio
        pipeline = Path(__file__).parent / "slides_pipeline.py"
    if not pipeline.exists():
        meta["errors"].append("slides_pipeline.py no encontrado")
        return False, None

    # ── Fase Plan ─────────────────────────────────────────────────────
    if reuse_plan:
        plan_dest = topic_folder / "slides"
        plan_dest.mkdir(parents=True, exist_ok=True)
        shutil.copy2(reuse_plan, plan_dest / f"plan-filminas-{TOPIC_NAME}.yaml")
        meta["phases"]["plan"]["status"] = "skipped_reuse"
        _info(f"Plan reutilizado desde: {reuse_plan}")
    else:
        t0 = time.time()
        print(f"  Ejecutando plan...")
        ok, out = _run_pipeline_phase(pipeline, topic_folder, "--plan-only", python_bin)
        elapsed = round(time.time() - t0, 1)
        meta["phases"]["plan"]["elapsed_s"] = elapsed
        if not ok:
            meta["phases"]["plan"]["status"] = "error"
            meta["phases"]["plan"]["output"]  = out[-2000:]
            meta["errors"].append(f"Plan falló: {out[-500:]}")
            _err(f"Plan falló ({elapsed}s)")
            print(out[-1000:])
            return False, None
        # Contar slides del plan
        plan_path = topic_folder / "slides" / f"plan-filminas-{TOPIC_NAME}.yaml"
        if plan_path.exists():
            plan_data = load_yaml(plan_path)
            meta["phases"]["plan"]["slides"] = plan_data.get("meta", {}).get("total_slides", 0)
        meta["phases"]["plan"]["status"] = "ok"
        _ok(f"Plan generado ({elapsed}s, {meta['phases']['plan']['slides']} filminas)")

    if plan_only:
        return True, None

    # ── Fase Assets ───────────────────────────────────────────────────
    if not no_images:
        t0 = time.time()
        print(f"  Generando assets...")
        ok, out = _run_pipeline_phase(pipeline, topic_folder, "--assets-only", python_bin)
        elapsed = round(time.time() - t0, 1)
        meta["phases"]["assets"]["elapsed_s"] = elapsed
        if not ok:
            meta["phases"]["assets"]["status"] = "error"
            meta["phases"]["assets"]["output"]  = out[-2000:]
            meta["errors"].append(f"Assets fallaron: {out[-500:]}")
            _warn(f"Assets fallaron ({elapsed}s) — continuando con publish...")
        else:
            meta["phases"]["assets"]["status"] = "ok"
            _ok(f"Assets generados ({elapsed}s)")
    else:
        meta["phases"]["assets"]["status"] = "skipped_no_images"
        _info("Assets omitidos (--no-images)")

    # ── Fase Publish ──────────────────────────────────────────────────
    t0 = time.time()
    print(f"  Publicando en Google Slides...")
    ok, out = _run_pipeline_phase(pipeline, topic_folder, "--publish-only", python_bin)
    elapsed = round(time.time() - t0, 1)
    meta["phases"]["publish"]["elapsed_s"] = elapsed

    if not ok:
        meta["phases"]["publish"]["status"] = "error"
        meta["phases"]["publish"]["output"]  = out[-2000:]
        meta["errors"].append(f"Publish falló: {out[-500:]}")
        _err(f"Publish falló ({elapsed}s)")
        print(out[-1500:])
        return False, None

    # Extraer URL del output del pipeline
    pres_id: str | None = None
    url_file = topic_folder / "slides" / "slides-url.txt"
    if url_file.exists():
        url = url_file.read_text(encoding="utf-8").strip()
        meta["phases"]["publish"]["presentation_url"] = url
        # Extraer ID de la URL: .../presentation/d/{ID}/edit
        parts = url.split("/d/")
        if len(parts) > 1:
            pres_id = parts[1].split("/")[0]
    meta["phases"]["publish"]["status"] = "ok"
    _ok(f"Publicado en Google Slides ({elapsed}s)")
    if pres_id:
        _info(f"Presentation ID: {pres_id}")

    return True, pres_id


# ══════════════════════════════════════════════════════════════════════
# FASE 3 — Screenshots via Google Slides API
# ══════════════════════════════════════════════════════════════════════

def screenshot_slides(
    pres_id: str,
    creds: Credentials,
    output_dir: Path,
    meta: dict,
) -> int:
    """
    Descarga capturas PNG de cada filmina usando la API de Google Slides.
    Devuelve la cantidad de capturas obtenidas.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    slides_svc = build("slides", "v1", credentials=creds)

    try:
        pres    = slides_svc.presentations().get(presentationId=pres_id).execute()
        slides  = pres.get("slides", [])
    except Exception as exc:
        meta["errors"].append(f"Error obteniendo presentación: {exc}")
        _err(f"No se pudo obtener la presentación: {exc}")
        return 0

    count  = 0
    errors = 0
    total  = len(slides)
    _info(f"Descargando {total} capturas...")

    for idx, slide in enumerate(slides, start=1):
        page_id = slide["objectId"]
        fname   = output_dir / f"filmina_{idx:02d}.png"

        if fname.exists():
            _info(f"  Captura {idx:02d} ya existe, omitiendo.")
            count += 1
            continue

        try:
            thumb = slides_svc.presentations().pages().getThumbnail(
                presentationId=pres_id,
                pageObjectId=page_id,
                thumbnailProperties_thumbnailSize="LARGE",
                thumbnailProperties_mimeType="PNG",
            ).execute()

            content_url = thumb.get("contentUrl", "")
            if not content_url:
                raise ValueError("contentUrl vacío en respuesta de thumbnail")

            # Descargar la imagen (URL autenticada por token)
            resp = requests.get(
                content_url,
                headers={"Authorization": f"Bearer {creds.token}"},
                timeout=30,
            )
            resp.raise_for_status()
            fname.write_bytes(resp.content)
            count += 1
            print(f"  📸 Captura {idx:02d}/{total} ✓", end="\r")
            time.sleep(0.2)   # respetar rate limits

        except Exception as exc:
            _warn(f"Error captura filmina {idx:02d}: {exc}")
            errors += 1
            meta["errors"].append(f"Screenshot filmina {idx:02d}: {exc}")

    print()  # nueva línea tras el \r
    meta["phases"]["screenshots"]["count"]  = count
    meta["phases"]["screenshots"]["errors"] = errors
    meta["phases"]["screenshots"]["status"] = "ok" if count > 0 else "error"
    _ok(f"Capturas: {count}/{total} OK, {errors} errores")
    return count


# ══════════════════════════════════════════════════════════════════════
# FASE 4 — Generar informe HTML
# ══════════════════════════════════════════════════════════════════════

def _thumb_tag(img_path: Path, label: str, test_dir: Path) -> str:
    """Genera un tag <img> con base64 o ruta relativa."""
    if img_path.exists():
        rel = img_path.relative_to(test_dir)
        return (
            f'<figure>'
            f'<img src="{rel}" alt="{label}" />'
            f'<figcaption>{label}</figcaption>'
            f'</figure>'
        )
    return f'<figure class="missing"><span>{label} (no generada)</span></figure>'


def generate_report(
    test_dir:    Path,
    topic_folder: Path,
    meta:         dict,
    plan_only:    bool,
) -> Path:
    """Genera report.html y test-meta.yaml en el directorio de reporte."""
    ts         = meta["test_run_id"]
    total_s    = sum(v.get("elapsed_s", 0) for v in meta["phases"].values())
    ok_count   = sum(1 for v in meta["phases"].values() if v.get("status") == "ok")
    err_count  = len(meta["errors"])
    pres_url   = meta["phases"].get("publish", {}).get("presentation_url", "")
    n_slides   = meta["phases"]["plan"].get("slides", 0)
    n_shots    = meta["phases"]["screenshots"].get("count", 0)

    status_html = "✅ PASS" if err_count == 0 else f"⚠️ {err_count} errores"

    # ── Galería de capturas ────────────────────────────────────────────
    shots_dir = test_dir / "filminas"
    gallery_items = sorted(shots_dir.glob("filmina_*.png"))
    gallery_html = ""
    if gallery_items:
        gallery_html = "\n".join(
            _thumb_tag(p, p.stem.replace("_", " ").title(), test_dir)
            for p in gallery_items
        )
    elif plan_only:
        gallery_html = "<p class='info'>Plan-only: no se generaron capturas.</p>"
    else:
        gallery_html = "<p class='warn'>No se generaron capturas de pantalla.</p>"

    # ── Assets generados ──────────────────────────────────────────────
    assets_dir = topic_folder / "slides" / "assets"
    asset_items = sorted(assets_dir.glob("*.png")) if assets_dir.exists() else []
    assets_html = "\n".join(
        _thumb_tag(p, p.name, test_dir) for p in asset_items
    ) or "<p class='info'>No hay assets generados.</p>"

    # ── Tabla de fases ─────────────────────────────────────────────────
    def phase_row(name: str, label: str) -> str:
        ph = meta["phases"].get(name, {})
        st = ph.get("status", "pending")
        el = ph.get("elapsed_s", 0)
        icon = {"ok": "✅", "error": "❌", "pending": "⏳",
                "skipped_reuse": "⏭️", "skipped_no_images": "⏭️"}.get(st, "❓")
        extra = ""
        if name == "plan":
            extra = f" — {ph.get('slides', '?')} filminas"
        if name == "publish" and ph.get("presentation_url"):
            extra = f' — <a href="{ph["presentation_url"]}" target="_blank">abrir ↗</a>'
        if name == "screenshots":
            extra = f" — {ph.get('count', 0)} capturas"
        return f"<tr><td>{icon} {label}</td><td>{el}s{extra}</td></tr>"

    phases_html = (
        phase_row("plan",        "Fase 1 — Plan YAML") +
        phase_row("assets",      "Fase 2 — Assets (IA + tablas)") +
        phase_row("publish",     "Fase 3 — Publicar Google Slides") +
        phase_row("screenshots", "Fase 4 — Screenshots")
    )

    # ── Errores ────────────────────────────────────────────────────────
    errs_html = ""
    if meta["errors"]:
        items = "".join(f"<li>{e}</li>" for e in meta["errors"])
        errs_html = f"<h2 class='err-h'>Errores ({len(meta['errors'])})</h2><ul class='errs'>{items}</ul>"

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Test Pipeline — {ts}</title>
  <style>
    :root {{
      --primary: #A9191B; --bg: #fff; --surface: #F4F4F4;
      --text: #222; --muted: #666; --border: #ddd;
    }}
    body {{ font-family: Roboto, Arial, sans-serif; margin: 0; color: var(--text); background: var(--bg); }}
    header {{ background: var(--primary); color: #fff; padding: 1.5rem 2rem; }}
    header h1 {{ margin: 0; font-size: 1.6rem; }}
    header p  {{ margin: .3rem 0 0; opacity: .85; font-size: .9rem; }}
    main {{ max-width: 1400px; margin: 0 auto; padding: 2rem; }}
    .summary {{ display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 2rem; }}
    .card {{ background: var(--surface); border-radius: 8px; padding: 1rem 1.5rem; flex: 1; min-width: 140px; }}
    .card .num {{ font-size: 2rem; font-weight: 700; color: var(--primary); }}
    .card .lbl {{ font-size: .8rem; color: var(--muted); margin-top: .2rem; }}
    table {{ border-collapse: collapse; width: 100%; margin-bottom: 2rem; }}
    th, td {{ text-align: left; padding: .7rem 1rem; border-bottom: 1px solid var(--border); }}
    th {{ background: var(--surface); font-weight: 600; }}
    h2 {{ font-size: 1.2rem; margin: 2rem 0 .8rem; border-bottom: 2px solid var(--primary); padding-bottom: .3rem; }}
    .gallery {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.2rem; margin-bottom: 2rem; }}
    .gallery figure {{ margin: 0; background: var(--surface); border-radius: 8px; overflow: hidden; border: 1px solid var(--border); }}
    .gallery figure img {{ width: 100%; display: block; }}
    .gallery figcaption {{ padding: .4rem .6rem; font-size: .8rem; color: var(--muted); text-align: center; }}
    .gallery .missing {{ padding: 3rem; display: flex; align-items: center; justify-content: center; color: var(--muted); font-size: .85rem; }}
    .errs {{ background: #fff3f3; border-left: 4px solid #c00; padding: 1rem 1rem 1rem 2rem; border-radius: 4px; }}
    .err-h {{ color: #c00; }}
    .info {{ color: var(--muted); font-style: italic; }}
    .warn {{ color: #b66000; }}
    a {{ color: var(--primary); }}
  </style>
</head>
<body>
<header>
  <h1>🧪 Test Pipeline — Filminas</h1>
  <p>{ts} · {status_html} · {ok_count} fases OK · {total_s:.1f}s total</p>
</header>
<main>

  <div class="summary">
    <div class="card"><div class="num">{n_slides}</div><div class="lbl">Filminas parseadas</div></div>
    <div class="card"><div class="num">{n_shots}</div><div class="lbl">Capturas generadas</div></div>
    <div class="card"><div class="num">{len(asset_items)}</div><div class="lbl">Assets generados</div></div>
    <div class="card"><div class="num">{err_count}</div><div class="lbl">Errores detectados</div></div>
  </div>

  <h2>Fases de ejecución</h2>
  <table>
    <thead><tr><th>Fase</th><th>Resultado</th></tr></thead>
    <tbody>{phases_html}</tbody>
  </table>

  {"<p><a href='" + pres_url + "' target='_blank'>🔗 Abrir presentación en Google Slides ↗</a></p>" if pres_url else ""}

  {errs_html}

  <h2>📸 Capturas de filminas ({n_shots})</h2>
  <div class="gallery">{gallery_html}</div>

  <h2>🖼️ Assets generados ({len(asset_items)})</h2>
  <div class="gallery">{assets_html}</div>

  <h2>📋 Datos del test</h2>
  <table>
    <tr><th>Parámetro</th><th>Valor</th></tr>
    <tr><td>ID test</td><td>{ts}</td></tr>
    <tr><td>Iniciado</td><td>{meta['started_at']}</td></tr>
    <tr><td>Finalizado</td><td>{meta.get('finished_at', '—')}</td></tr>
    <tr><td>filminas.md fuente</td><td>{meta['source_filminas']}</td></tr>
    <tr><td>slides-config.yaml fuente</td><td>{meta['source_config']}</td></tr>
    <tr><td>Directorio</td><td>{meta['test_dir']}</td></tr>
  </table>

</main>
</body>
</html>
"""

    report_path = test_dir / "report.html"
    report_path.write_text(html, encoding="utf-8")

    meta["finished_at"] = datetime.now().isoformat(timespec="seconds")
    meta["phases"]["report"]["status"]    = "ok"
    meta["phases"]["report"]["elapsed_s"] = 0

    save_yaml(test_dir / "test-meta.yaml", meta)

    _ok(f"Informe HTML generado: {report_path.relative_to(report_path.parent.parent.parent)}")
    return report_path


# ══════════════════════════════════════════════════════════════════════
# FASE 5 — Copiar assets finales al directorio del reporte
# ══════════════════════════════════════════════════════════════════════

def copy_assets_to_report(test_dir: Path, topic_folder: Path, meta: dict) -> None:
    """Copia los assets generados (PNG) al directorio raíz del reporte para fácil acceso."""
    assets_src = topic_folder / "slides" / "assets"
    if not assets_src.exists():
        return
    assets_dst = test_dir / "assets"
    if assets_dst.exists():
        shutil.rmtree(assets_dst)
    shutil.copytree(assets_src, assets_dst)

    # Copiar también el plan YAML
    plan_src = topic_folder / "slides" / f"plan-filminas-{TOPIC_NAME}.yaml"
    if plan_src.exists():
        shutil.copy2(plan_src, test_dir / "plan.yaml")

    _ok("Assets y plan copiados al directorio del reporte")


# ══════════════════════════════════════════════════════════════════════
# Punto de entrada
# ══════════════════════════════════════════════════════════════════════

def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="EDU Slides Pipeline — Test de integración completo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--from",
        dest="source_filminas",
        default=None,
        help="Ruta a filminas.md alternativo (por defecto: informe/filminas.md)",
    )
    parser.add_argument(
        "--config",
        dest="source_config",
        default=None,
        help="Ruta a slides-config.yaml alternativo (por defecto: _edu/slides-config.yaml)",
    )
    parser.add_argument(
        "--plan-only",
        action="store_true",
        help="Solo ejecutar Fase 1 (parse + plan YAML), sin Google APIs",
    )
    parser.add_argument(
        "--no-images",
        action="store_true",
        help="Omitir generación de imágenes IA (Imagen 4.0) en Fase 2",
    )
    parser.add_argument(
        "--reuse-plan",
        metavar="PATH",
        default=None,
        help="Reutilizar plan.yaml existente, omitir Fase 1",
    )
    parser.add_argument(
        "--python",
        default=sys.executable,
        help=f"Intérprete Python a usar (por defecto: {sys.executable})",
    )
    args = parser.parse_args(argv)

    project_root = find_project_root(Path(__file__).parent)

    # ── Resolver rutas de entrada ──────────────────────────────────────
    source_filminas = Path(args.source_filminas) if args.source_filminas else (
        project_root / "informe" / "filminas.md"
    )
    source_config = Path(args.source_config) if args.source_config else (
        project_root / "_edu" / "slides-config.yaml"
    )

    for p, label in [
        (source_filminas, "filminas.md"),
        (source_config,   "slides-config.yaml"),
    ]:
        if not p.exists():
            _err(f"No se encontró {label}: {p}")
            sys.exit(1)

    secrets_path = project_root / "_edu" / "secrets.local.yaml"
    token_path   = project_root / "_edu" / "token_slides.json"

    if not args.plan_only and not secrets_path.exists():
        _err(f"Falta _edu/secrets.local.yaml — ejecutar /edu-setup-apis primero")
        sys.exit(1)

    print("""
╔═══════════════════════════════════════════════════════════╗
║   🧪 EDU Slides Pipeline — Test de Integración             ║
╚═══════════════════════════════════════════════════════════╝""")
    _info(f"filminas.md:       {source_filminas.relative_to(project_root)}")
    _info(f"slides-config:     {source_config.relative_to(project_root)}")
    _info(f"plan-only:         {args.plan_only}")
    _info(f"no-images:         {args.no_images}")

    t_total = time.time()

    # ── Paso 1: Setup ──────────────────────────────────────────────────
    _step(1, "Setup del directorio de reporte")
    t0 = time.time()
    test_dir, topic_folder, meta = setup_test_dir(
        project_root, source_filminas, source_config
    )
    meta["phases"]["setup"]["elapsed_s"] = round(time.time() - t0, 1)

    # Sobreescribir el slides-config del pipeline con el de referencia del test
    config_override = project_root / "_edu" / "slides-config.yaml"
    if source_config != config_override:
        _info(f"Usando slides-config de referencia para el test: {source_config}")

    # ── Paso 2: Pipeline ───────────────────────────────────────────────
    _step(2, "Ejecutando pipeline (Plan → Assets → Publish)")
    reuse_plan = Path(args.reuse_plan) if args.reuse_plan else None

    pipeline_ok, pres_id = run_pipeline(
        project_root  = project_root,
        topic_folder  = topic_folder,
        meta          = meta,
        plan_only     = args.plan_only,
        no_images     = args.no_images,
        reuse_plan    = reuse_plan,
        python_bin    = args.python,
    )

    # ── Paso 3: Screenshots ────────────────────────────────────────────
    if pres_id and not args.plan_only:
        _step(3, f"Descargando capturas de Google Slides (pres_id: {pres_id})")
        t0 = time.time()
        try:
            creds = _get_creds(secrets_path, token_path)
            n_shots = screenshot_slides(
                pres_id    = pres_id,
                creds      = creds,
                output_dir = test_dir / "filminas",
                meta       = meta,
            )
        except Exception as exc:
            _warn(f"Screenshots fallaron: {exc}")
            meta["errors"].append(f"Screenshots: {exc}")
            meta["phases"]["screenshots"]["status"] = "error"
        meta["phases"]["screenshots"]["elapsed_s"] = round(time.time() - t0, 1)
    elif args.plan_only:
        meta["phases"]["screenshots"]["status"] = "skipped_plan_only"
        _step(3, "Screenshots — omitido (plan-only)")
    else:
        meta["phases"]["screenshots"]["status"] = "skipped_no_pres"
        _step(3, "Screenshots — omitido (sin presentación disponible)")

    # ── Paso 4: Copiar assets ──────────────────────────────────────────
    _step(4, "Copiando assets al directorio de reporte")
    copy_assets_to_report(test_dir, topic_folder, meta)

    # ── Paso 5: Generar reporte ────────────────────────────────────────
    _step(5, "Generando informe HTML")
    report_path = generate_report(test_dir, topic_folder, meta, args.plan_only)

    # ── Resumen final ──────────────────────────────────────────────────
    total_elapsed = round(time.time() - t_total, 1)
    err_count = len(meta["errors"])

    print(f"""
╔═══════════════════════════════════════════════════════════╗
║   Test completado en {total_elapsed:.1f}s{"" if err_count == 0 else f" — ⚠️ {err_count} errores"}
╚═══════════════════════════════════════════════════════════╝
   Directorio:  {test_dir.relative_to(project_root)}
   Filminas:    {meta['phases']['plan'].get('slides', '?')}
   Capturas:    {meta['phases']['screenshots'].get('count', 0)}
   Assets:      {len(list((test_dir / 'assets').glob('*.png'))) if (test_dir / 'assets').exists() else 0}
   Informe:     {report_path.relative_to(project_root)}
""")
    if meta.get("phases", {}).get("publish", {}).get("presentation_url"):
        _ok(f"Presentación: {meta['phases']['publish']['presentation_url']}")

    if err_count > 0:
        print("\n   Errores detectados:")
        for e in meta["errors"]:
            print(f"   • {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
