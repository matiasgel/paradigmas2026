#!/usr/bin/env python3
"""
EDU Knowledge Watcher — Monitorea ingesta/ y auto-ingesta PDFs en ChromaDB.

Cuando se detecta un nuevo PDF en ingesta/:
  1. Convierte a TXT (pdfminer)
  2. Chunkea con tamaño 800 chars
  3. Inserta en ChromaDB (collection edu_knowledge, type=material)

Uso:
    python salida/edu-standalone/scripts/knowledge_watcher.py

    # O en background:
    python salida/edu-standalone/scripts/knowledge_watcher.py &

Dependencias: watchdog, pdfminer.six, chromadb
"""

from __future__ import annotations

import hashlib
import time
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileCreatedEvent, FileMovedEvent

# Import from knowledge_base (same directory)
from knowledge_base import (
    INGESTA_DIR,
    WORKSPACE_ROOT,
    MATERIAL_CHUNK_SIZE,
    book_label,
    chunk_ingesta_txt,
    convert_pdfs_to_txt,
    get_client,
    get_or_create_collection,
    COLLECTION_NAME,
)


WATCH_DIR = INGESTA_DIR


def ingest_single_txt(txt_path: Path) -> int:
    """Ingest a single TXT file into ChromaDB. Returns chunk count."""
    if not txt_path.exists() or txt_path.suffix != ".txt":
        return 0

    text = txt_path.read_text(encoding="utf-8", errors="replace")
    book = book_label(txt_path)
    source = str(txt_path.relative_to(INGESTA_DIR))
    chunks = chunk_ingesta_txt(text, source, book)

    if not chunks:
        return 0

    client = get_client()
    collection = get_or_create_collection(client)

    ids = []
    documents = []
    metadatas = []
    for i, chunk in enumerate(chunks):
        doc_id = hashlib.md5(
            f"{chunk['source']}:{chunk['heading']}:{i}".encode()
        ).hexdigest()[:16]
        ids.append(doc_id)
        documents.append(chunk["text"])
        metadatas.append({
            "source": chunk["source"],
            "type": chunk["type"],
            "heading": chunk["heading"],
        })

    collection.add(ids=ids, documents=documents, metadatas=metadatas)
    return len(chunks)


def process_pdf(pdf_path: Path) -> None:
    """Convert a single PDF to TXT and ingest it."""
    txt_dir = pdf_path.parent / "txt"
    txt_path = txt_dir / f"{pdf_path.stem}.txt"

    if txt_path.exists():
        print(f"  ⏭️  TXT ya existe: {txt_path.name}")
        return

    # Convert PDF → TXT
    n = convert_pdfs_to_txt(pdf_path.parent)
    if n == 0:
        print(f"  ⚠️  No se pudo convertir: {pdf_path.name}")
        return

    # Ingest the new TXT
    if txt_path.exists():
        count = ingest_single_txt(txt_path)
        print(f"  ✅ Ingestado: {txt_path.name} → {count} chunks")


class IngestaHandler(FileSystemEventHandler):
    """Handles new PDF files in the ingesta/ directory."""

    def on_created(self, event: FileCreatedEvent) -> None:
        if event.is_directory:
            return
        path = Path(event.src_path)
        if path.suffix.lower() == ".pdf":
            print(f"\n📥 Nuevo PDF detectado: {path.name}")
            # Small delay to ensure file is fully written
            time.sleep(1)
            process_pdf(path)

    def on_moved(self, event: FileMovedEvent) -> None:
        if event.is_directory:
            return
        path = Path(event.dest_path)
        if path.suffix.lower() == ".pdf":
            print(f"\n📥 PDF movido/renombrado: {path.name}")
            time.sleep(1)
            process_pdf(path)


def main() -> None:
    watch_path = WATCH_DIR

    if not watch_path.exists():
        watch_path.mkdir(parents=True, exist_ok=True)
        print(f"📁 Creada carpeta: {watch_path}")

    print(f"👀 Monitoreando: {watch_path}")
    print(f"   ChromaDB collection: {COLLECTION_NAME}")
    print(f"   Chunk size (material): {MATERIAL_CHUNK_SIZE} chars")
    print(f"   Ctrl+C para detener\n")

    observer = Observer()
    observer.schedule(IngestaHandler(), str(watch_path), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Watcher detenido.")

    observer.join()


if __name__ == "__main__":
    main()
