#!/usr/bin/env python3
"""
EDU Knowledge Base — Backup a Google Drive.

Comprime el directorio ChromaDB (EDU_CHROMA_PATH o ~/.edu/chroma_db) en un
archivo ZIP con timestamp y lo sube a la carpeta "edu-chroma-backups" en Drive.

Uso:
    # Crear backup y subir a Drive
    python scripts/backup_knowledge_base.py

    # Solo crear el ZIP local, sin subir
    python scripts/backup_knowledge_base.py --local-only

    # Listar backups existentes en Drive
    python scripts/backup_knowledge_base.py --list

    # Restaurar un backup desde Drive (por nombre de archivo)
    python scripts/backup_knowledge_base.py --restore edu-chroma-backup-2026-04-27T12-00-00.zip

Requisitos:
    pip install google-api-python-client google-auth-oauthlib google-auth-httplib2

Credenciales:
    Usa las mismas credenciales OAuth que slides_pipeline.py.
    Configurar EDU_SECRETS_PATH y EDU_TOKEN_PATH en .env.
"""

import argparse
import os
import sys
import zipfile
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Path resolution
# ---------------------------------------------------------------------------

def _find_project_root() -> Path:
    p = Path(__file__).resolve().parent
    while p != p.parent:
        if (p / "_edu").is_dir() or (p / "_edu-knowledge").is_dir():
            return p
        p = p.parent
    return Path(__file__).resolve().parent.parent


ROOT = _find_project_root()
DRIVE_FOLDER_NAME = "edu-chroma-backups"


def _load_dotenv() -> None:
    """Carga variables de entorno desde .env si existe."""
    env_path = ROOT / ".env"
    if not env_path.exists():
        # Buscar también en workspace root
        ws = ROOT.parent
        while ws != ws.parent:
            candidate = ws / ".env"
            if candidate.exists():
                env_path = candidate
                break
            if (ws / ".git").exists():
                break
            ws = ws.parent

    if env_path.exists():
        with open(env_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key and key not in os.environ:
                    os.environ[key] = value


def _resolve_chroma_dir() -> Path:
    env_path = os.environ.get("EDU_CHROMA_PATH", "").strip()
    if env_path:
        return Path(env_path).expanduser().resolve()
    return Path.home() / ".edu" / "chroma_db"


def _resolve_secrets() -> tuple[Path, Path]:
    """Devuelve (secrets_path, token_path) desde env o defaults."""
    secrets = ROOT / os.environ.get("EDU_SECRETS_PATH", "_edu/secrets.local.yaml")
    token = ROOT / os.environ.get("EDU_TOKEN_PATH", "_edu/token_slides.json")
    return secrets.resolve(), token.resolve()


# ---------------------------------------------------------------------------
# ZIP creation
# ---------------------------------------------------------------------------

def create_backup_zip(chroma_dir: Path, output_dir: Path) -> Path:
    """Comprime chroma_dir en un ZIP con timestamp. Devuelve la ruta del ZIP."""
    ts = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    zip_name = f"edu-chroma-backup-{ts}.zip"
    zip_path = output_dir / zip_name

    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"📦 Comprimiendo {chroma_dir} …")
    total_files = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for file in sorted(chroma_dir.rglob("*")):
            if file.is_file():
                arcname = file.relative_to(chroma_dir.parent)
                zf.write(file, arcname)
                total_files += 1

    size_mb = zip_path.stat().st_size / (1024 * 1024)
    print(f"  ✅ {total_files} archivos comprimidos → {zip_name} ({size_mb:.1f} MB)")
    return zip_path


# ---------------------------------------------------------------------------
# Google Drive operations
# ---------------------------------------------------------------------------

SCOPES = [
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/slides",
]


def _get_creds(secrets_path: Path, token_path: Path):
    """Obtiene credenciales OAuth reutilizando la lógica de slides_pipeline."""
    import yaml
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from google_auth_oauthlib.flow import InstalledAppFlow

    if not secrets_path.exists():
        print(f"❌ No se encontró {secrets_path}")
        print("   Configurar EDU_SECRETS_PATH en .env o ejecutar /edu-setup-apis primero.")
        sys.exit(1)

    with open(secrets_path, encoding="utf-8") as f:
        secrets = yaml.safe_load(f) or {}

    creds_file = Path(secrets.get("google_credentials_path", "")).expanduser().resolve()
    if not creds_file.exists():
        # Intentar relativo a ROOT
        creds_file = ROOT / secrets.get("google_credentials_path", "_edu/credentials.json")

    creds = None
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not creds_file.exists():
                print(f"❌ No se encontró credentials.json en {creds_file}")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(str(creds_file), SCOPES)
            creds = flow.run_local_server(port=0)
        token_path.parent.mkdir(parents=True, exist_ok=True)
        token_path.write_text(creds.to_json(), encoding="utf-8")

    return creds


def _get_drive_service(secrets_path: Path, token_path: Path):
    from googleapiclient.discovery import build
    creds = _get_creds(secrets_path, token_path)
    return build("drive", "v3", credentials=creds)


def _ensure_drive_folder(drive_svc, name: str) -> str:
    """Obtiene o crea carpeta en Drive. Devuelve folder_id."""
    q = (
        f"name='{name}' and mimeType='application/vnd.google-apps.folder' "
        f"and trashed=false"
    )
    res = drive_svc.files().list(q=q, fields="files(id, name)").execute()
    files = res.get("files", [])
    if files:
        return files[0]["id"]
    meta = {"name": name, "mimeType": "application/vnd.google-apps.folder"}
    f = drive_svc.files().create(body=meta, fields="id").execute()
    return f["id"]


def upload_backup(zip_path: Path, drive_svc) -> str:
    """Sube el ZIP a Drive en la carpeta de backups. Devuelve el file_id."""
    from googleapiclient.http import MediaFileUpload

    folder_id = _ensure_drive_folder(drive_svc, DRIVE_FOLDER_NAME)
    print(f"☁️  Subiendo a Drive (carpeta: {DRIVE_FOLDER_NAME}) …")

    meta = {"name": zip_path.name, "parents": [folder_id]}
    media = MediaFileUpload(str(zip_path), mimetype="application/zip", resumable=True)
    f = drive_svc.files().create(body=meta, media_body=media, fields="id, name").execute()
    file_id = f["id"]

    print(f"  ✅ Backup subido: {zip_path.name} (Drive ID: {file_id})")
    return file_id


def list_backups(drive_svc) -> list[dict]:
    """Lista los backups existentes en Drive."""
    folder_id = None
    q = (
        f"name='{DRIVE_FOLDER_NAME}' and mimeType='application/vnd.google-apps.folder' "
        f"and trashed=false"
    )
    res = drive_svc.files().list(q=q, fields="files(id)").execute()
    files = res.get("files", [])
    if not files:
        print(f"ℹ️  No existe la carpeta '{DRIVE_FOLDER_NAME}' en Drive.")
        return []
    folder_id = files[0]["id"]

    q2 = f"'{folder_id}' in parents and trashed=false and name contains 'edu-chroma-backup'"
    res2 = drive_svc.files().list(
        q=q2,
        fields="files(id, name, size, createdTime)",
        orderBy="createdTime desc",
    ).execute()
    backups = res2.get("files", [])

    if not backups:
        print("ℹ️  No hay backups en Drive.")
    else:
        print(f"\n☁️  Backups en Drive (carpeta: {DRIVE_FOLDER_NAME}):\n")
        print(f"  {'Nombre':<55} {'Tamaño':>10}  {'Fecha'}")
        print(f"  {'─'*55} {'─'*10}  {'─'*20}")
        for b in backups:
            size = int(b.get("size", 0))
            size_str = f"{size / (1024*1024):.1f} MB" if size else "?"
            created = b.get("createdTime", "")[:19].replace("T", " ")
            print(f"  {b['name']:<55} {size_str:>10}  {created}")

    return backups


def restore_backup(backup_name: str, drive_svc, chroma_dir: Path) -> None:
    """Descarga un backup de Drive y lo restaura en chroma_dir."""
    import io
    from googleapiclient.http import MediaIoBaseDownload

    # Buscar el archivo por nombre
    q = f"name='{backup_name}' and trashed=false"
    res = drive_svc.files().list(q=q, fields="files(id, name, size)").execute()
    files = res.get("files", [])
    if not files:
        print(f"❌ No se encontró '{backup_name}' en Drive.")
        sys.exit(1)

    file_id = files[0]["id"]
    print(f"📥 Descargando {backup_name} …")

    # Descargar a temp
    tmp_zip = Path("/tmp") / backup_name
    request = drive_svc.files().get_media(fileId=file_id)
    with open(tmp_zip, "wb") as fh:
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()

    print(f"  ✅ Descargado: {tmp_zip}")

    # Restaurar: vaciar chroma_dir y extraer ZIP
    import shutil
    if chroma_dir.exists():
        print(f"⚠️  Reemplazando {chroma_dir} con el backup …")
        shutil.rmtree(chroma_dir)

    chroma_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(tmp_zip, "r") as zf:
        # Los archivos están archivados como chroma_db/<file>, extraer dentro del parent
        zf.extractall(chroma_dir.parent)

    tmp_zip.unlink(missing_ok=True)
    print(f"  ✅ Backup restaurado en: {chroma_dir}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    _load_dotenv()

    parser = argparse.ArgumentParser(
        description="EDU Knowledge Base — Backup/Restore ChromaDB en Google Drive",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--local-only", action="store_true",
        help="Solo crear ZIP local, sin subir a Drive",
    )
    parser.add_argument(
        "--list", action="store_true",
        help="Listar backups existentes en Drive",
    )
    parser.add_argument(
        "--restore", metavar="BACKUP_NAME",
        help="Restaurar backup desde Drive (nombre del archivo ZIP)",
    )
    parser.add_argument(
        "--output-dir", metavar="DIR",
        help="Directorio donde guardar el ZIP local (default: /tmp)",
    )

    args = parser.parse_args()

    chroma_dir = _resolve_chroma_dir()
    secrets_path, token_path = _resolve_secrets()

    if args.list:
        drive_svc = _get_drive_service(secrets_path, token_path)
        list_backups(drive_svc)
        return

    if args.restore:
        drive_svc = _get_drive_service(secrets_path, token_path)
        restore_backup(args.restore, drive_svc, chroma_dir)
        return

    # Backup
    if not chroma_dir.exists() or not any(chroma_dir.iterdir()):
        print(f"⚠️  ChromaDB vacía o inexistente en: {chroma_dir}")
        print("   Ejecutar /edu-ingest primero para poblar la base de datos.")
        sys.exit(1)

    output_dir = Path(args.output_dir) if args.output_dir else Path("/tmp")
    zip_path = create_backup_zip(chroma_dir, output_dir)

    if args.local_only:
        print(f"\n📦 Backup local listo: {zip_path}")
        return

    drive_svc = _get_drive_service(secrets_path, token_path)
    upload_backup(zip_path, drive_svc)

    # Limpiar ZIP temporal
    zip_path.unlink(missing_ok=True)
    print(f"\n✅ Backup completado.")
    print(f"   Para listar backups: python scripts/backup_knowledge_base.py --list")
    print(f"   Para restaurar:      python scripts/backup_knowledge_base.py --restore <nombre.zip>")


if __name__ == "__main__":
    main()
