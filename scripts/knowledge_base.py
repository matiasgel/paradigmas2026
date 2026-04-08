#!/usr/bin/env python3
"""
EDU Knowledge Base — ChromaDB ingestion & query system.

Ingesta documentos de _edu-knowledge/ (referencias académicas + docs de herramientas)
y material del curso de ingesta/ en ChromaDB. Si los PDFs de ingesta/ no tienen TXT
generados, los convierte automáticamente con pdfminer.

Uso:
    # Ingestar conocimiento base
    python scripts/knowledge_base.py ingest

    # Ingestar incluyendo material del curso (ingesta/)
    python scripts/knowledge_base.py ingest --include-material

    # Re-ingestar todo (borra y recrea)
    python scripts/knowledge_base.py ingest --force --include-material

    # Buscar
    python scripts/knowledge_base.py search "cognitive load theory slides"

    # Buscar filtrando por tipo
    python scripts/knowledge_base.py search "WCAG contrast" --type reference
    python scripts/knowledge_base.py search "FSRS algorithm" --type tool
    python scripts/knowledge_base.py search "paradigmas funcional" --type material

    # Listar documentos indexados
    python scripts/knowledge_base.py list

Chunk sizes:
    - reference/tool: max 1500 chars (markdown con headings)
    - material: max 800 chars (texto denso de libros → chunks pequeños para
      mejor retrieval semántico)
"""

import argparse
import hashlib
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Path resolution
# ---------------------------------------------------------------------------

def find_project_root() -> Path:
    """Walk up from this script to find the edu-standalone root."""
    p = Path(__file__).resolve().parent
    while p != p.parent:
        if (p / "_edu-knowledge").is_dir() or (p / "_edu").is_dir():
            return p
        p = p.parent
    return Path(__file__).resolve().parent.parent


ROOT = find_project_root()
KNOWLEDGE_DIR = ROOT / "_edu-knowledge"
CHROMA_DIR = KNOWLEDGE_DIR / "chroma_db"
TOOLS_DIR = KNOWLEDGE_DIR / "tools"
REFS_DIR = KNOWLEDGE_DIR / "references"

# ingesta/ lives at the top-level workspace root, which may differ from ROOT
# when this script lives inside salida/edu-standalone/
def _find_workspace_root() -> Path:
    """Find the top-level workspace root (contains .git or ingesta/)."""
    p = ROOT
    while p != p.parent:
        if (p / ".git").exists() or (p / "ingesta").is_dir():
            return p
        p = p.parent
    return ROOT

WORKSPACE_ROOT = _find_workspace_root()
INGESTA_DIR = WORKSPACE_ROOT / "ingesta"

COLLECTION_NAME = "edu_knowledge"
MATERIAL_CHUNK_SIZE = 800  # chars — chunks pequeños para texto denso de libros

# ---------------------------------------------------------------------------
# ChromaDB client
# ---------------------------------------------------------------------------

def get_client():
    """Persistent ChromaDB client."""
    import chromadb
    return chromadb.PersistentClient(path=str(CHROMA_DIR))


def get_or_create_collection(client):
    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

# ---------------------------------------------------------------------------
# PDF → TXT conversion (integrated)
# ---------------------------------------------------------------------------

def convert_pdfs_to_txt(folder: Path) -> int:
    """Convert all PDFs under folder to TXT if not already done. Returns count."""
    try:
        from pdfminer.high_level import extract_text
    except ImportError:
        print("  ⚠️  pdfminer.six no instalado — omitiendo conversión PDF→TXT")
        print("     Instalar con: pip install pdfminer.six")
        return 0

    converted = 0
    for pdf in sorted(folder.rglob("*.pdf")):
        txt_dir = pdf.parent / "txt"
        txt_path = txt_dir / f"{pdf.stem}.txt"
        if txt_path.exists():
            continue
        txt_dir.mkdir(parents=True, exist_ok=True)
        try:
            text = extract_text(str(pdf))
            if not text or not text.strip():
                text = f"[PDF sin texto extraíble: {pdf.name}]\n"
            from datetime import datetime
            timestamp = datetime.now().isoformat(timespec="seconds")
            output = (
                f"# Fuente\n"
                f"- archivo: {pdf.name}\n"
                f"- ruta: {pdf}\n"
                f"- extraido: {timestamp}\n\n"
                f"# Contenido\n\n"
                f"{text.strip()}\n"
            )
            txt_path.write_text(output, encoding="utf-8")
            converted += 1
            print(f"  📄 PDF→TXT: {pdf.name}")
        except Exception as exc:
            print(f"  ❌ Error convirtiendo {pdf.name}: {exc}")
    return converted

# ---------------------------------------------------------------------------
# Document chunking
# ---------------------------------------------------------------------------

def chunk_markdown(text: str, source: str, doc_type: str, max_chars: int = 1500) -> list[dict]:
    """Split a markdown document into chunks by headings, respecting max_chars."""
    chunks = []
    # Split by ## headings
    sections = re.split(r'(?=^## )', text, flags=re.MULTILINE)

    for section in sections:
        section = section.strip()
        if not section:
            continue

        # Extract heading if present
        heading_match = re.match(r'^##\s+(.+)', section)
        heading = heading_match.group(1).strip() if heading_match else "intro"

        # If section is small enough, keep as one chunk
        if len(section) <= max_chars:
            chunks.append({
                "text": section,
                "source": source,
                "type": doc_type,
                "heading": heading,
            })
        else:
            # Split further by ### subheadings
            subsections = re.split(r'(?=^### )', section, flags=re.MULTILINE)
            for sub in subsections:
                sub = sub.strip()
                if not sub:
                    continue
                sub_heading_match = re.match(r'^###\s+(.+)', sub)
                sub_heading = sub_heading_match.group(1).strip() if sub_heading_match else heading

                # If still too large, split by paragraphs
                if len(sub) <= max_chars:
                    chunks.append({
                        "text": sub,
                        "source": source,
                        "type": doc_type,
                        "heading": f"{heading} > {sub_heading}",
                    })
                else:
                    paragraphs = sub.split("\n\n")
                    buffer = ""
                    for para in paragraphs:
                        if len(buffer) + len(para) + 2 > max_chars and buffer:
                            chunks.append({
                                "text": buffer.strip(),
                                "source": source,
                                "type": doc_type,
                                "heading": f"{heading} > {sub_heading}",
                            })
                            buffer = para
                        else:
                            buffer = buffer + "\n\n" + para if buffer else para
                    if buffer.strip():
                        chunks.append({
                            "text": buffer.strip(),
                            "source": source,
                            "type": doc_type,
                            "heading": f"{heading} > {sub_heading}",
                        })

    return chunks


def chunk_code(text: str, source: str, max_chars: int = 2000) -> list[dict]:
    """Chunk a code/config file."""
    chunks = []
    # For code files, split by class/function definitions or large blocks
    lines = text.split("\n")
    buffer = []
    current_chars = 0

    for line in lines:
        if current_chars + len(line) + 1 > max_chars and buffer:
            chunks.append({
                "text": "\n".join(buffer),
                "source": source,
                "type": "tool",
                "heading": f"code:{source}",
            })
            buffer = [line]
            current_chars = len(line)
        else:
            buffer.append(line)
            current_chars += len(line) + 1

    if buffer:
        chunks.append({
            "text": "\n".join(buffer),
            "source": source,
            "type": "tool",
            "heading": f"code:{source}",
        })

    return chunks

# ---------------------------------------------------------------------------
# Ingestion — material del curso
# ---------------------------------------------------------------------------

def book_label(txt_path: Path) -> str:
    """Derive a short book label from the TXT file path inside ingesta/."""
    parts = txt_path.relative_to(INGESTA_DIR).parts
    if len(parts) >= 3:  # <book-dir>/txt/<file>
        return parts[0]
    return "misc"


def chunk_ingesta_txt(text: str, source: str, book: str, max_chars: int = MATERIAL_CHUNK_SIZE) -> list[dict]:
    """Chunk a TXT extracted from PDF (format: # Fuente / # Contenido).

    Uses small chunks (800 chars default) because many academic books lack
    double‑newline paragraph separators.
    """
    content_match = re.search(r'# Contenido\s*\n(.*)', text, re.DOTALL)
    content = content_match.group(1).strip() if content_match else text.strip()

    # Normalize page-breaks (\x0c) to paragraph separators
    content = content.replace('\x0c', '\n\n')

    chunks = []

    def emit(blob: str) -> None:
        """Split a potentially large blob by line boundaries into max_chars pieces."""
        if len(blob) <= max_chars:
            if blob.strip():
                chunks.append({"text": blob.strip(), "source": source,
                               "type": "material", "heading": book})
            return
        lines = blob.split('\n')
        buf = ""
        for line in lines:
            if len(buf) + len(line) + 1 > max_chars and buf:
                if buf.strip():
                    chunks.append({"text": buf.strip(), "source": source,
                                   "type": "material", "heading": book})
                buf = line
            else:
                buf = buf + '\n' + line if buf else line
        if buf.strip():
            chunks.append({"text": buf.strip(), "source": source,
                           "type": "material", "heading": book})

    paragraphs = re.split(r'\n{2,}', content)
    buffer = ""
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if len(buffer) + len(para) + 2 > max_chars and buffer:
            emit(buffer)
            buffer = para
        else:
            buffer = buffer + "\n\n" + para if buffer else para
    if buffer.strip():
        emit(buffer)
    return chunks


def collect_material_documents() -> list[dict]:
    """Collect all TXT files from ingesta/**/txt/. Auto‑converts PDFs first."""
    all_chunks = []
    if not INGESTA_DIR.is_dir():
        print("  ⚠️  Carpeta ingesta/ no encontrada, omitiendo material del curso.")
        return all_chunks

    n_converted = convert_pdfs_to_txt(INGESTA_DIR)
    if n_converted:
        print(f"  ✅ Convertidos {n_converted} PDFs nuevos a TXT\n")

    txt_files = sorted(INGESTA_DIR.rglob("txt/*.txt"))
    for f in txt_files:
        book = book_label(f)
        source = str(f.relative_to(INGESTA_DIR))
        text = f.read_text(encoding="utf-8", errors="replace")
        chunks = chunk_ingesta_txt(text, source, book)
        if chunks:
            all_chunks.extend(chunks)
            print(f"  📖 {source}: {len(chunks)} chunks  [{book[:50]}]")
    return all_chunks

# ---------------------------------------------------------------------------
# Ingestion
# ---------------------------------------------------------------------------

def collect_documents(include_material: bool = False) -> list[dict]:
    """Collect all documents from _edu-knowledge/ (and optionally ingesta/)."""
    all_chunks = []

    # References (markdown)
    if REFS_DIR.is_dir():
        for f in sorted(REFS_DIR.glob("*.md")):
            text = f.read_text(encoding="utf-8", errors="replace")
            chunks = chunk_markdown(text, f.name, "reference")
            all_chunks.extend(chunks)
            print(f"  📚 {f.name}: {len(chunks)} chunks")

    # Tools (markdown + code)
    if TOOLS_DIR.is_dir():
        for f in sorted(TOOLS_DIR.iterdir()):
            if f.suffix in (".md", ".yml", ".yaml"):
                text = f.read_text(encoding="utf-8", errors="replace")
                chunks = chunk_markdown(text, f.name, "tool")
                all_chunks.extend(chunks)
                print(f"  🔧 {f.name}: {len(chunks)} chunks")
            elif f.suffix in (".py", ".js", ".json"):
                text = f.read_text(encoding="utf-8", errors="replace")
                if len(text) > 100:  # skip empty/tiny files
                    chunks = chunk_code(text, f.name)
                    all_chunks.extend(chunks)
                    print(f"  🔧 {f.name}: {len(chunks)} chunks")
            elif f.suffix == ".html":
                # Skip large HTML files (WCAG quickref etc.)
                print(f"  ⏭️  {f.name}: skipped (HTML, use markdown refs instead)")

    # Course material (ingesta/**/txt/*.txt)
    if include_material:
        print("\n📥 Recolectando material del curso (ingesta/)...")
        material_chunks = collect_material_documents()
        all_chunks.extend(material_chunks)

    return all_chunks


def ingest(force: bool = False, include_material: bool = False):
    """Ingest all documents into ChromaDB."""
    client = get_client()

    if force:
        try:
            client.delete_collection(COLLECTION_NAME)
            print("🗑️  Collection eliminada (--force)")
        except Exception:
            pass

    collection = get_or_create_collection(client)

    # Check if already populated
    existing = collection.count()
    if existing > 0 and not force:
        print(f"ℹ️  Collection ya tiene {existing} documentos. Usar --force para re-ingestar.")
        return

    print("📥 Recolectando documentos...")
    chunks = collect_documents(include_material=include_material)

    if not chunks:
        print("⚠️  No se encontraron documentos en _edu-knowledge/")
        return

    # Prepare for ChromaDB
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

    # Batch insert (ChromaDB limit: 5461 per batch)
    batch_size = 5000
    for start in range(0, len(ids), batch_size):
        end = min(start + batch_size, len(ids))
        collection.add(
            ids=ids[start:end],
            documents=documents[start:end],
            metadatas=metadatas[start:end],
        )

    print(f"\n✅ Ingestados {len(chunks)} chunks de {len(set(c['source'] for c in chunks))} documentos")
    print(f"   ChromaDB path: {CHROMA_DIR}")

# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------

def search(query: str, doc_type: str | None = None, n_results: int = 8):
    """Search the knowledge base."""
    client = get_client()

    try:
        collection = client.get_collection(COLLECTION_NAME)
    except Exception:
        print("⚠️  Knowledge base vacía. Ejecutar: python scripts/knowledge_base.py ingest")
        sys.exit(1)

    where = {"type": doc_type} if doc_type else None

    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        where=where,
        include=["documents", "metadatas", "distances"],
    )

    if not results["documents"] or not results["documents"][0]:
        print("❌ Sin resultados.")
        return []

    entries = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        relevance = 1 - dist  # cosine distance → similarity
        entries.append({
            "text": doc,
            "source": meta["source"],
            "type": meta["type"],
            "heading": meta["heading"],
            "relevance": round(relevance, 3),
        })

    return entries


def print_results(entries: list[dict]):
    """Print search results."""
    if not entries:
        return
    print(f"\n🔍 {len(entries)} resultados:\n")
    for i, e in enumerate(entries, 1):
        icon = "📚" if e["type"] == "reference" else "🔧"
        print(f"{'─'*60}")
        print(f"{icon} [{i}] {e['source']} — {e['heading']}")
        print(f"   Relevancia: {e['relevance']}")
        # Show first 300 chars
        preview = e["text"][:300].replace("\n", "\n   ")
        print(f"   {preview}...")
        print()

# ---------------------------------------------------------------------------
# List
# ---------------------------------------------------------------------------

def list_docs():
    """List all indexed documents."""
    client = get_client()
    try:
        collection = client.get_collection(COLLECTION_NAME)
    except Exception:
        print("⚠️  Knowledge base vacía.")
        return

    count = collection.count()
    print(f"📊 {count} chunks indexados\n")

    # Get unique sources
    results = collection.get(include=["metadatas"])
    sources = {}
    for meta in results["metadatas"]:
        src = meta["source"]
        typ = meta["type"]
        if src not in sources:
            sources[src] = {"type": typ, "chunks": 0}
        sources[src]["chunks"] += 1

    print(f"{'Documento':<55} {'Tipo':<12} {'Chunks':>6}")
    print(f"{'─'*55} {'─'*12} {'─'*6}")
    for src, info in sorted(sources.items()):
        icon = "📚" if info["type"] == "reference" else "🔧"
        print(f"{icon} {src:<53} {info['type']:<12} {info['chunks']:>6}")

# ---------------------------------------------------------------------------
# API for agents (importable)
# ---------------------------------------------------------------------------

def query_knowledge(query: str, doc_type: str | None = None, n_results: int = 5) -> str:
    """
    Query the knowledge base and return formatted text.
    Designed for agent consumption — returns a single string.
    """
    entries = search(query, doc_type, n_results)
    if not entries:
        return "Sin resultados en la knowledge base."

    parts = []
    for i, e in enumerate(entries, 1):
        parts.append(f"[{i}] {e['source']} — {e['heading']} (relevancia: {e['relevance']})")
        parts.append(e["text"][:800])
        parts.append("")

    return "\n".join(parts)

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="EDU Knowledge Base — ChromaDB",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command")

    # ingest
    p_ingest = sub.add_parser("ingest", help="Ingestar documentos en ChromaDB")
    p_ingest.add_argument("--force", action="store_true", help="Re-ingestar borrando datos previos")
    p_ingest.add_argument("--include-material", action="store_true",
                          help="Incluir material del curso (ingesta/**/txt/). Auto-convierte PDFs.")

    # search
    p_search = sub.add_parser("search", help="Buscar en la knowledge base")
    p_search.add_argument("query", help="Texto de búsqueda")
    p_search.add_argument("--type", choices=["reference", "tool", "material"], help="Filtrar por tipo")
    p_search.add_argument("-n", type=int, default=8, help="Cantidad de resultados")

    # list
    sub.add_parser("list", help="Listar documentos indexados")

    args = parser.parse_args()

    if args.command == "ingest":
        ingest(force=args.force, include_material=args.include_material)
    elif args.command == "search":
        entries = search(args.query, doc_type=args.type, n_results=args.n)
        print_results(entries)
    elif args.command == "list":
        list_docs()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
