#!/usr/bin/env python3
"""
Captura thumbnails de una presentación Google Slides publicada.
Uso:
    python scripts/capture_thumbnails.py <presentation_id> <output_dir>
    python scripts/capture_thumbnails.py --topic 08-paradigma-oo-ts --course 2026

Requiere credenciales OAuth2 en _edu/token_slides.json (ya autenticado).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import requests
import yaml

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from pipeline_common import ensure_git_ignored_dir, ensure_git_ignored_path, find_project_root


SCOPES = [
    "https://www.googleapis.com/auth/presentations.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]


def get_credentials(project_root: Path) -> Credentials:
    secrets_path = project_root / "_edu" / "secrets.local.yaml"
    token_path = project_root / "_edu" / "token_slides.json"
    with secrets_path.open() as f:
        secrets = yaml.safe_load(f)
    creds_path = project_root / secrets["google_credentials_path"]

    creds = None
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            from google_auth_oauthlib.flow import InstalledAppFlow
            flow = InstalledAppFlow.from_client_secrets_file(str(creds_path), SCOPES)
            creds = flow.run_local_server(port=0)
        with token_path.open("w") as f:
            f.write(creds.to_json())
    return creds


def _extract_presentation_id(slides_url: str) -> str:
    match = re.search(r"/d/([^/]+)", slides_url)
    if not match:
        raise ValueError(f"No se pudo extraer presentation_id desde {slides_url}")
    return match.group(1)


def _resolve_topic_output(project_root: Path, topic: str, course: str) -> tuple[str, Path]:
    topic_folder = project_root / "salida" / "cursadas" / course / "temas" / topic
    url_path = ensure_git_ignored_path(topic_folder, Path("slides") / "slides-url.txt")
    if not url_path.exists():
        raise FileNotFoundError(f"No se encontró slides-url.txt para {topic_folder}")

    presentation_id = _extract_presentation_id(url_path.read_text(encoding="utf-8").strip())
    output_dir = ensure_git_ignored_dir(topic_folder, Path("slides") / "thumbnails")
    return presentation_id, output_dir


def _remap_output_dir(project_root: Path, output_dir: Path) -> Path:
    resolved = output_dir if output_dir.is_absolute() else (project_root / output_dir)
    resolved = resolved.resolve()

    try:
        relative = resolved.relative_to(project_root)
    except ValueError:
        return resolved

    parts = relative.parts
    if len(parts) < 6:
        return resolved
    if parts[0] != "salida" or parts[1] != "cursadas" or parts[3] != "temas":
        return resolved

    topic_folder = project_root.joinpath(*parts[:5])
    logical_dir = Path(*parts[5:])
    return ensure_git_ignored_dir(topic_folder, logical_dir)


def capture_thumbnails(presentation_id: str, output_dir: Path) -> None:
    project_root = find_project_root(Path(__file__))
    creds = get_credentials(project_root)

    slides_svc = build("slides", "v1", credentials=creds)

    print(f"  Descargando lista de slides de presentación {presentation_id}...")
    presentation = slides_svc.presentations().get(
        presentationId=presentation_id
    ).execute()

    slides = presentation.get("slides", [])
    print(f"  Total de slides: {len(slides)}")

    output_dir.mkdir(parents=True, exist_ok=True)

    authed_session = requests.Session()
    authed_session.headers["Authorization"] = f"Bearer {creds.token}"

    ok = 0
    failed = []
    for i, slide in enumerate(slides):
        page_id = slide["objectId"]
        url = (
            f"https://slides.googleapis.com/v1/presentations/{presentation_id}"
            f"/pages/{page_id}/thumbnail?thumbnailProperties.thumbnailSize=LARGE"
        )
        resp = authed_session.get(url, timeout=30)
        if resp.status_code != 200:
            print(f"  [{i+1:02d}/{len(slides)}] ❌ Error thumbnail API: {resp.status_code} — {resp.text[:100]}")
            failed.append(i + 1)
            continue

        thumb_url = resp.json().get("contentUrl", "")
        img_resp = None
        for attempt in range(3):
            try:
                img_resp = requests.get(thumb_url, timeout=60)
                if img_resp.status_code == 200:
                    break
            except Exception as e:
                print(f"  [{i+1:02d}/{len(slides)}] ⚠️  Intento {attempt+1}/3 timeout: {e}")
                import time; time.sleep(2)
                img_resp = None

        if img_resp and img_resp.status_code == 200:
            out_path = output_dir / f"slide-{i+1:02d}-{page_id}.jpg"
            out_path.write_bytes(img_resp.content)
            ok += 1
            print(f"  [{i+1:02d}/{len(slides)}] ✅ {out_path.name}")
        else:
            code = img_resp.status_code if img_resp else "timeout"
            print(f"  [{i+1:02d}/{len(slides)}] ❌ Error descargando imagen: {code}")
            failed.append(i + 1)

    print(f"\nResumen: {ok}/{len(slides)} thumbnails capturados.")
    if failed:
        print(f"Fallidos: {failed}")
    print(f"Carpeta: {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Captura thumbnails de Google Slides")
    parser.add_argument("presentation_id", nargs="?", help="ID de la presentación")
    parser.add_argument("output_dir", nargs="?", help="Directorio de salida")
    parser.add_argument("--topic", help="ID del tema")
    parser.add_argument("--course", help="ID del curso")
    args = parser.parse_args()

    root = find_project_root(Path(__file__))

    if args.topic and args.course:
        pres_id, output_dir = _resolve_topic_output(root, args.topic, args.course)
        capture_thumbnails(pres_id, output_dir)
        sys.exit(0)

    if not args.presentation_id or not args.output_dir:
        parser.error("usar <presentation_id> <output_dir> o bien --topic <tema> --course <curso>")

    capture_thumbnails(args.presentation_id, _remap_output_dir(root, Path(args.output_dir)))
