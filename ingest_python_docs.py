"""
Ingest Python 3.14 documentation (HTML) into ChromaDB.
Uses the new PersistentClient API (ChromaDB >= 0.4.x).
Preserves existing collections — only adds to 'python-3.14-docs'.
"""
import os
import re
import sys
import hashlib
from pathlib import Path
from bs4 import BeautifulSoup
import chromadb

# ── Config ──────────────────────────────────────────────────────────────────
HTML_DIR      = Path("python-3.14-docs-html")
CHROMA_DIR    = Path("_edu-knowledge/chroma_db")
COLLECTION    = "python-3.14-docs"
CHUNK_WORDS   = 400       # words per chunk (safe margin under token limits)
BATCH_SIZE    = 50        # docs to add per batch call
SKIP_PATTERNS = [         # glob-like path fragments to skip (nav/index noise)
    "_static", "_images", "genindex", "py-modindex",
]

# ── Helpers ──────────────────────────────────────────────────────────────────

def extract_text(html_path: Path) -> tuple[str, str]:
    """Return (title, clean_text) from an HTML file."""
    content = html_path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(content, "lxml")

    # Remove nav, sidebars, scripts, styles
    for tag in soup.find_all(["nav", "script", "style", "footer",
                               "header", "aside"]):
        tag.decompose()
    for tag in soup.find_all(class_=re.compile(r"(sidebar|toctree|navigation|related|footer)")):
        tag.decompose()

    title_tag = soup.find("h1") or soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else html_path.stem

    body = soup.find("div", class_=re.compile(r"body|document|content")) or soup.body or soup
    text = body.get_text(separator=" ", strip=True)
    text = re.sub(r"\s{2,}", " ", text)
    return title, text


def chunk_text(text: str, max_words: int) -> list[str]:
    """Split text into chunks of max_words words."""
    words = text.split()
    return [" ".join(words[i:i + max_words])
            for i in range(0, len(words), max_words)
            if words[i:i + max_words]]


def make_id(path_str: str, idx: int) -> str:
    """Deterministic ID so re-runs don't duplicate."""
    raw = f"{path_str}__chunk_{idx}"
    return hashlib.md5(raw.encode()).hexdigest()


def should_skip(path: Path) -> bool:
    p_str = str(path)
    return any(pat in p_str for pat in SKIP_PATTERNS)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    if not HTML_DIR.exists():
        print(f"ERROR: '{HTML_DIR}' not found. Run the download first.", file=sys.stderr)
        sys.exit(1)

    print(f"Connecting to ChromaDB at '{CHROMA_DIR}'...")
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    print(f"Getting or creating collection '{COLLECTION}'...")
    collection = client.get_or_create_collection(
        name=COLLECTION,
        metadata={"hnsw:space": "cosine", "source": "python-3.14-official-docs"}
    )
    existing_count = collection.count()
    print(f"  Existing documents in collection: {existing_count}")

    html_files = sorted(HTML_DIR.rglob("*.html"))
    print(f"Found {len(html_files)} HTML files to process...")

    total_chunks = 0
    batch_ids, batch_docs, batch_metas = [], [], []

    for i, html_file in enumerate(html_files, 1):
        if should_skip(html_file):
            continue

        try:
            title, text = extract_text(html_file)
        except Exception as e:
            print(f"  WARN: skipping {html_file.name} ({e})")
            continue

        if len(text.split()) < 20:
            continue  # Skip trivially short pages

        chunks = chunk_text(text, CHUNK_WORDS)
        rel_path = str(html_file.relative_to(HTML_DIR))

        for cidx, chunk in enumerate(chunks):
            doc_id = make_id(rel_path, cidx)
            batch_ids.append(doc_id)
            batch_docs.append(chunk)
            batch_metas.append({
                "source": "python-3.14-docs",
                "type": "tool",
                "file": rel_path,
                "title": title[:200],
                "chunk_index": cidx,
            })

        # Flush batch
        if len(batch_ids) >= BATCH_SIZE:
            collection.upsert(ids=batch_ids, documents=batch_docs, metadatas=batch_metas)
            total_chunks += len(batch_ids)
            batch_ids, batch_docs, batch_metas = [], [], []

        if i % 50 == 0:
            print(f"  Processed {i}/{len(html_files)} files, {total_chunks} chunks ingested so far...")

    # Final flush
    if batch_ids:
        collection.upsert(ids=batch_ids, documents=batch_docs, metadatas=batch_metas)
        total_chunks += len(batch_ids)

    print(f"\nDone! Ingested {total_chunks} new/updated chunks into '{COLLECTION}'.")
    print(f"Total documents in collection now: {collection.count()}")


if __name__ == "__main__":
    main()
