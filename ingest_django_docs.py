"""
Descarga e ingesta la documentación oficial Django 6.0 en ChromaDB.
Usa PersistentClient API (ChromaDB >= 0.4.x).
Preserva todas las colecciones existentes — solo agrega a 'django-6.0-docs'.
"""
import os
import re
import sys
import hashlib
import zipfile
import urllib.request
from pathlib import Path
from bs4 import BeautifulSoup
import chromadb

# ── Config ──────────────────────────────────────────────────────────────────
ZIP_URL       = "https://media.djangoproject.com/docs/django-docs-6.0-en.zip"
ZIP_FILE      = Path("django-6.0-docs.zip")
EXTRACT_DIR   = Path("django-6.0-docs-html")
CHROMA_DIR    = Path("_edu-knowledge/chroma_db")
COLLECTION    = "django-6.0-docs"
CHUNK_WORDS   = 400
BATCH_SIZE    = 50
SKIP_PATTERNS = ["_static", "_images", "genindex", "py-modindex", "search"]

# ── Helpers ──────────────────────────────────────────────────────────────────

def download_zip():
    if ZIP_FILE.exists():
        print(f"  ZIP ya existe: {ZIP_FILE} — saltando descarga.")
        return
    print(f"Descargando {ZIP_URL}...")
    urllib.request.urlretrieve(ZIP_URL, ZIP_FILE)
    print(f"  Descargado: {ZIP_FILE} ({ZIP_FILE.stat().st_size / 1024 / 1024:.1f} MB)")


def extract_zip():
    if EXTRACT_DIR.exists() and any(EXTRACT_DIR.rglob("*.html")):
        print(f"  Directorio '{EXTRACT_DIR}' ya existe con HTML — saltando extracción.")
        return
    print(f"Extrayendo {ZIP_FILE}...")
    with zipfile.ZipFile(ZIP_FILE, "r") as zf:
        zf.extractall(".")
    # Django zip puede extraer en un subdirectorio: buscar la carpeta raíz
    candidates = [p for p in Path(".").iterdir()
                  if p.is_dir() and "django" in p.name.lower() and p != EXTRACT_DIR]
    if candidates and not EXTRACT_DIR.exists():
        candidates[0].rename(EXTRACT_DIR)
    print(f"  Extraído en '{EXTRACT_DIR}'")


def extract_text(html_path: Path) -> tuple[str, str]:
    content = html_path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(content, "lxml")
    for tag in soup.find_all(["nav", "script", "style", "footer", "header", "aside"]):
        tag.decompose()
    for tag in soup.find_all(class_=re.compile(
            r"(sidebar|toctree|navigation|related|footer|breadcrumbs|sphinxsidebar)")):
        tag.decompose()
    title_tag = soup.find("h1") or soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else html_path.stem
    body = (soup.find("div", class_=re.compile(r"body|document|content"))
            or soup.body or soup)
    text = body.get_text(separator=" ", strip=True)
    text = re.sub(r"\s{2,}", " ", text)
    return title[:200], text


def chunk_text(text: str, max_words: int) -> list[str]:
    words = text.split()
    return [" ".join(words[i:i + max_words])
            for i in range(0, len(words), max_words)
            if words[i:i + max_words]]


def make_id(path_str: str, idx: int) -> str:
    return hashlib.md5(f"{path_str}__chunk_{idx}".encode()).hexdigest()


def should_skip(path: Path) -> bool:
    return any(pat in str(path) for pat in SKIP_PATTERNS)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    download_zip()
    extract_zip()

    # Buscar HTML en el directorio extraído (puede tener subdirectorio)
    html_dir = EXTRACT_DIR
    if not html_dir.exists():
        # Buscar el primer directorio que tenga index.html
        for p in Path(".").iterdir():
            if p.is_dir() and (p / "index.html").exists():
                html_dir = p
                break
    if not html_dir.exists():
        print(f"ERROR: No se encontró directorio con docs HTML.", file=sys.stderr)
        sys.exit(1)

    print(f"Conectando a ChromaDB en '{CHROMA_DIR}'...")
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    # Mostrar colecciones existentes
    print("Colecciones existentes (se preservan):")
    for col in client.list_collections():
        print(f"  - {col.name}: {client.get_collection(col.name).count()} docs")

    print(f"\nCreando/obteniendo colección '{COLLECTION}'...")
    collection = client.get_or_create_collection(
        name=COLLECTION,
        metadata={"hnsw:space": "cosine", "source": "django-6.0-official-docs"}
    )
    print(f"  Documentos existentes: {collection.count()}")

    html_files = sorted(html_dir.rglob("*.html"))
    print(f"Archivos HTML encontrados: {len(html_files)}")

    total_chunks = 0
    batch_ids, batch_docs, batch_metas = [], [], []

    for i, html_file in enumerate(html_files, 1):
        if should_skip(html_file):
            continue
        try:
            title, text = extract_text(html_file)
        except Exception as e:
            print(f"  WARN: saltando {html_file.name} ({e})")
            continue
        if len(text.split()) < 20:
            continue

        chunks = chunk_text(text, CHUNK_WORDS)
        rel_path = str(html_file.relative_to(html_dir))

        for cidx, chunk in enumerate(chunks):
            batch_ids.append(make_id(rel_path, cidx))
            batch_docs.append(chunk)
            batch_metas.append({
                "source": "django-6.0-docs",
                "type": "tool",
                "file": rel_path,
                "title": title,
                "chunk_index": cidx,
            })

        if len(batch_ids) >= BATCH_SIZE:
            collection.upsert(ids=batch_ids, documents=batch_docs, metadatas=batch_metas)
            total_chunks += len(batch_ids)
            batch_ids, batch_docs, batch_metas = [], [], []

        if i % 100 == 0:
            print(f"  Procesados {i}/{len(html_files)} archivos, {total_chunks} chunks...")

    if batch_ids:
        collection.upsert(ids=batch_ids, documents=batch_docs, metadatas=batch_metas)
        total_chunks += len(batch_ids)

    print(f"\nListo! {total_chunks} chunks ingresados en '{COLLECTION}'.")
    print(f"Total en la colección: {collection.count()}")

    print("\nEstado final de ChromaDB:")
    for col in client.list_collections():
        print(f"  - {col.name}: {client.get_collection(col.name).count()} docs")


if __name__ == "__main__":
    main()
