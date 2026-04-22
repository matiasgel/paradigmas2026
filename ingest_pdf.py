"""
Ingesta un PDF en ChromaDB sin borrar colecciones existentes.
Uso: python ingest_pdf.py <ruta_al_pdf> [nombre_coleccion]
"""
import sys
import re
import hashlib
from pathlib import Path
import pymupdf  # PyMuPDF
import chromadb

# ── Config ──────────────────────────────────────────────────────────────────
CHROMA_DIR  = Path("_edu-knowledge/chroma_db")
CHUNK_WORDS = 400
BATCH_SIZE  = 50

# ── Helpers ──────────────────────────────────────────────────────────────────

def extract_pdf_text(pdf_path: Path) -> list[tuple[int, str]]:
    """Retorna lista de (page_num, text) por página."""
    doc = pymupdf.open(str(pdf_path))
    pages = []
    for i, page in enumerate(doc, 1):
        text = page.get_text("text")
        text = re.sub(r"\s{2,}", " ", text).strip()
        if text:
            pages.append((i, text))
    doc.close()
    return pages


def chunk_text(text: str, max_words: int) -> list[str]:
    words = text.split()
    return [" ".join(words[i:i + max_words])
            for i in range(0, len(words), max_words)
            if words[i:i + max_words]]


def make_id(source: str, page: int, idx: int) -> str:
    raw = f"{source}__p{page}__chunk_{idx}"
    return hashlib.md5(raw.encode()).hexdigest()


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Uso: python ingest_pdf.py <ruta_pdf> [nombre_coleccion]")
        sys.exit(1)

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        print(f"ERROR: No se encontró '{pdf_path}'")
        sys.exit(1)

    # Nombre de colección: arg opcional, o derivado del nombre del PDF
    if len(sys.argv) >= 3:
        collection_name = sys.argv[2]
    else:
        collection_name = re.sub(r"[^a-zA-Z0-9_-]", "-", pdf_path.stem.lower())
        # ChromaDB requiere nombre entre 3 y 63 chars
        if len(collection_name) < 3:
            collection_name = "pdf-" + collection_name

    print(f"PDF:        {pdf_path}")
    print(f"Colección:  {collection_name}")
    print(f"ChromaDB:   {CHROMA_DIR}")

    # Conectar
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    print("\nColecciones existentes (se preservan):")
    for col in client.list_collections():
        print(f"  - {col.name}: {client.get_collection(col.name).count()} docs")

    collection = client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine", "source": str(pdf_path), "type": "tool"}
    )
    print(f"\nDocs existentes en '{collection_name}': {collection.count()}")

    # Extraer texto
    print(f"\nExtrayendo texto de '{pdf_path.name}'...")
    pages = extract_pdf_text(pdf_path)
    print(f"  Páginas con texto: {len(pages)}")

    # Chunking e ingestión
    total_chunks = 0
    batch_ids, batch_docs, batch_metas = [], [], []

    for page_num, page_text in pages:
        chunks = chunk_text(page_text, CHUNK_WORDS)
        for cidx, chunk in enumerate(chunks):
            batch_ids.append(make_id(pdf_path.name, page_num, cidx))
            batch_docs.append(chunk)
            batch_metas.append({
                "source": pdf_path.name,
                "type": "tool",
                "page": page_num,
                "chunk_index": cidx,
            })

        if len(batch_ids) >= BATCH_SIZE:
            collection.upsert(ids=batch_ids, documents=batch_docs, metadatas=batch_metas)
            total_chunks += len(batch_ids)
            batch_ids, batch_docs, batch_metas = [], [], []

    if batch_ids:
        collection.upsert(ids=batch_ids, documents=batch_docs, metadatas=batch_metas)
        total_chunks += len(batch_ids)

    print(f"\nListo! {total_chunks} chunks ingresados en '{collection_name}'.")
    print(f"Total en la colección: {collection.count()}")

    print("\nEstado final de ChromaDB:")
    for col in client.list_collections():
        print(f"  - {col.name}: {client.get_collection(col.name).count()} docs")


if __name__ == "__main__":
    main()
