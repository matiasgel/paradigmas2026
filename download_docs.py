#!/usr/bin/env python3
"""
Descarga documentación oficial de Django y Bootstrap como archivos Markdown
para ingestión en ChromaDB.

Uso:
    python scripts/download_docs.py
    python scripts/download_docs.py --target django
    python scripts/download_docs.py --target bootstrap
"""

import argparse
import html2text
import httpx
import json
import re
import sys
import time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse


ROOT = Path(__file__).resolve().parent
KNOWLEDGE_DIR = ROOT / "_edu-knowledge" / "tools"

SOURCES = {
    "django": {
        "name": "Django official documentation 6.0",
        "start_url": "https://docs.djangoproject.com/en/6.0/",
        "prefix": "https://docs.djangoproject.com/en/6.0/",
        "output": KNOWLEDGE_DIR / "django-official-docs-6.0.md",
        "max_pages": 700,
        "delay": 0.3,
    },
    "bootstrap": {
        "name": "Bootstrap official documentation 5.3",
        "start_url": "https://getbootstrap.com/docs/5.3/getting-started/introduction/",
        "prefix": "https://getbootstrap.com/docs/5.3/",
        "output": KNOWLEDGE_DIR / "bootstrap-official-docs-5.3.md",
        "max_pages": 100,
        "delay": 0.5,
    },
}


def make_converter() -> html2text.HTML2Text:
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.ignore_tables = False
    h.body_width = 0
    h.skip_internal_links = True
    h.unicode_snob = True
    h.protect_links = False
    h.wrap_links = False
    return h


def extract_links(html: str, base_url: str, prefix: str) -> list[str]:
    """Extrae links del HTML que estén dentro del prefix."""
    pattern = re.compile(r'href=["\']([^"\'#?]+)["\']')
    links = []
    for m in pattern.finditer(html):
        href = m.group(1)
        abs_url = urljoin(base_url, href)
        # Normalizar: quitar trailing slash (excepto dominio raíz)
        parsed = urlparse(abs_url)
        if parsed.scheme not in ("http", "https"):
            continue
        abs_url = parsed._replace(fragment="", query="").geturl()
        if abs_url.startswith(prefix):
            links.append(abs_url)
    return links


def get_page_title(html: str, url: str) -> str:
    m = re.search(r'<title[^>]*>([^<]+)</title>', html, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return url


def crawl(source: dict) -> None:
    name = source["name"]
    start_url = source["start_url"]
    prefix = source["prefix"]
    output_path = source["output"]
    max_pages = source["max_pages"]
    delay = source["delay"]

    print(f"\n🕷️  Crawling: {name}")
    print(f"   Inicio: {start_url}")
    print(f"   Prefijo: {prefix}")
    print(f"   Máximo páginas: {max_pages}")

    h = make_converter()
    client = httpx.Client(
        follow_redirects=True,
        timeout=30.0,
        headers={"User-Agent": "EDU-KnowledgeBase-Crawler/1.0 (educational use)"},
    )

    visited: set[str] = set()
    queue: deque[str] = deque([start_url])
    pages_saved = 0
    pages_seen = 0
    failures = []
    sections: list[str] = []

    # Header del archivo
    started_at = datetime.now(timezone.utc).isoformat()

    while queue and pages_saved < max_pages:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)
        pages_seen += 1

        try:
            resp = client.get(url)
            if resp.status_code != 200:
                failures.append({"url": url, "status": resp.status_code})
                continue

            content_type = resp.headers.get("content-type", "")
            if "html" not in content_type:
                continue

            html = resp.text
            title = get_page_title(html, url)
            fetched_at = datetime.now(timezone.utc).isoformat()

            # Extraer main content: intentar quitar nav/footer
            # Buscar <main>, <article>, <div role="main">, o <div class="..." id="content">
            main_match = (
                re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL | re.IGNORECASE)
                or re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL | re.IGNORECASE)
                or re.search(r'<div[^>]+role=["\']main["\'][^>]*>(.*?)</div>', html, re.DOTALL | re.IGNORECASE)
                or re.search(r'<div[^>]+id=["\'](?:content|main|docs-content|bd-content)["\'][^>]*>(.*?)</div>', html, re.DOTALL | re.IGNORECASE)
            )
            content_html = main_match.group(1) if main_match else html

            md = h.handle(content_html).strip()
            if not md or len(md) < 100:
                continue

            # Limpiar líneas vacías excesivas
            md = re.sub(r'\n{4,}', '\n\n\n', md)

            section = f"## {title}\n- source: {url}\n- fetched_at: {fetched_at}\n\n{md}"
            sections.append(section)
            pages_saved += 1

            if pages_saved % 50 == 0:
                print(f"   ... {pages_saved} páginas descargadas")

            # Encolar nuevos links
            new_links = extract_links(html, url, prefix)
            for link in new_links:
                if link not in visited:
                    queue.append(link)

            time.sleep(delay)

        except Exception as e:
            failures.append({"url": url, "error": str(e)})
            continue

    client.close()

    # Construir archivo final
    downloaded_at = datetime.now(timezone.utc).isoformat()
    header = (
        f"# {name}\n\n"
        f"- start_url: {start_url}\n"
        f"- prefix: {prefix}\n"
        f"- downloaded_at: {downloaded_at}\n"
        f"- pages_saved: {pages_saved}\n"
        f"- pages_seen: {pages_seen}\n"
        f"- failures: {len(failures)}\n\n"
    )

    full_content = header + "\n\n---\n\n".join(sections)

    output_path.write_text(full_content, encoding="utf-8")
    print(f"   ✅ Guardado: {output_path.relative_to(ROOT)}")
    print(f"   📊 Páginas: {pages_saved} guardadas / {pages_seen} vistas / {len(failures)} fallos")

    if failures:
        print(f"   ⚠️  Primeros fallos: {failures[:3]}")

    return {
        "name": name,
        "start_url": start_url,
        "prefix": prefix,
        "output": str(output_path.relative_to(ROOT)),
        "pages_saved": pages_saved,
        "pages_seen": pages_seen,
        "failures": failures,
    }


def main():
    parser = argparse.ArgumentParser(description="Descarga docs oficiales para ChromaDB")
    parser.add_argument(
        "--target",
        choices=["django", "bootstrap", "all"],
        default="all",
        help="Qué documentación descargar (default: all)",
    )
    args = parser.parse_args()

    targets = ["django", "bootstrap"] if args.target == "all" else [args.target]
    results = []

    for target in targets:
        result = crawl(SOURCES[target])
        results.append(result)

    # Actualizar manifest
    manifest_path = ROOT / "_edu-knowledge" / "official-docs-manifest.json"
    if manifest_path.exists():
        with open(manifest_path, encoding="utf-8") as f:
            manifest = json.load(f)
    else:
        manifest = {"sources": []}

    # Actualizar entradas del manifest para los targets procesados
    for result in results:
        existing = next((s for s in manifest["sources"] if s.get("name") == result["name"]), None)
        if existing:
            existing.update({
                "output": result["output"],
                "pages_saved": result["pages_saved"],
                "pages_seen": result["pages_seen"],
                "failures": [f["url"] if isinstance(f, dict) else f for f in result["failures"][:5]],
            })
        else:
            manifest["sources"].append({
                "name": result["name"],
                "start_url": result["start_url"],
                "prefix": result["prefix"],
                "output": result["output"],
                "pages_saved": result["pages_saved"],
                "pages_seen": result["pages_seen"],
                "failures": [],
            })

    manifest["generated_at"] = datetime.now(timezone.utc).isoformat()
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\n📋 Manifest actualizado: {manifest_path.relative_to(ROOT)}")
    print("\n✅ Descarga completa. Ejecutando ingesta incremental...")


if __name__ == "__main__":
    main()
