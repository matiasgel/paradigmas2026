"""
guias_to_pdf.py — Convierte todas las guías de iapjn-2026 a PDF
Usa: Markdown → HTML (con CSS) → Edge headless → PDF

Uso:
    python scripts/guias_to_pdf.py
    python scripts/guias_to_pdf.py --course iapjn-2026
    python scripts/guias_to_pdf.py --topic 01-que-es-la-ia
"""

import argparse
import glob
import os
import subprocess
import sys
import tempfile
import markdown

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

TEMAS_BASE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "salida", "cursadas", "iapjn-2026", "temas"
)

CSS = """
@page {
    size: A4;
    margin: 2.5cm 3cm;
    @bottom-right { content: counter(page) " / " counter(pages); font-size: 9pt; color: #888; }
}
* { box-sizing: border-box; }
body {
    font-family: Lato, Calibri, 'Segoe UI', Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #1a1a1a;
    max-width: 100%;
}
h1 {
    font-size: 20pt;
    color: #1b3a5c;
    border-bottom: 2px solid #1b3a5c;
    padding-bottom: 6px;
    margin-top: 0;
    margin-bottom: 16px;
}
h2 {
    font-size: 15pt;
    color: #1b3a5c;
    border-bottom: 1px solid #b0c4d8;
    padding-bottom: 4px;
    margin-top: 24px;
    margin-bottom: 10px;
}
h3 {
    font-size: 12pt;
    color: #2c5f8a;
    margin-top: 18px;
    margin-bottom: 8px;
}
h4, h5, h6 {
    font-size: 11pt;
    color: #2c5f8a;
    margin-top: 14px;
    margin-bottom: 6px;
}
p { margin: 0 0 10px; }
ul, ol {
    margin: 0 0 10px 0;
    padding-left: 24px;
}
li { margin-bottom: 4px; }
table {
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
    font-size: 10pt;
}
th {
    background-color: #1b3a5c;
    color: white;
    padding: 6px 10px;
    text-align: left;
}
td {
    border: 1px solid #b0c4d8;
    padding: 5px 10px;
    vertical-align: top;
}
tr:nth-child(even) td { background-color: #f0f4f8; }
blockquote {
    border-left: 4px solid #c8932a;
    margin: 10px 0;
    padding: 6px 14px;
    background: #f7f3ea;
    color: #2a2a2a;
    font-style: italic;
}
blockquote p { margin: 0; }
code {
    font-family: 'Roboto Mono', Consolas, monospace;
    font-size: 9.5pt;
    background: #f0f4f8;
    color: #1b3a5c;
    padding: 1px 4px;
    border-radius: 3px;
}
pre {
    background: #f0f4f8;
    border: 1px solid #b0c4d8;
    padding: 10px 14px;
    border-radius: 4px;
    overflow-x: auto;
    font-size: 9pt;
    margin: 10px 0;
}
pre code { background: none; padding: 0; color: inherit; }
hr {
    border: none;
    border-top: 1px solid #b0c4d8;
    margin: 18px 0;
}
strong { color: #1a1a1a; }
a { color: #1b3a5c; text-decoration: underline; }
.header-meta {
    font-size: 9pt;
    color: #888;
    border-bottom: 1px solid #eee;
    margin-bottom: 20px;
    padding-bottom: 6px;
}
"""

GUIDE_LABELS = {
    "guia-estudio": "Guía de Estudio",
    "guia-profesor": "Guía del Docente",
    "guia-practica": "Guía Práctica",
    "minuta": "Minuta de Clase",
}


def md_to_html(md_path: str) -> str:
    """Convert a Markdown file to a full HTML document with CSS."""
    with open(md_path, encoding="utf-8") as f:
        md_text = f.read()

    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "toc", "nl2br", "attr_list"],
    )

    stem = os.path.splitext(os.path.basename(md_path))[0]
    guide_label = GUIDE_LABELS.get(stem, stem)
    topic_folder = os.path.basename(os.path.dirname(md_path))

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>{guide_label} — {topic_folder}</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="header-meta">iapjn-2026 | {topic_folder} | {guide_label}</div>
{html_body}
</body>
</html>"""
    return html


def convert_to_pdf(md_path: str, out_dir: str | None = None) -> str:
    """Convert a .md guide to PDF using Edge headless. Returns output PDF path."""
    if out_dir is None:
        out_dir = os.path.dirname(md_path)

    stem = os.path.splitext(os.path.basename(md_path))[0]
    pdf_path = os.path.join(out_dir, f"{stem}.pdf")

    html_content = md_to_html(md_path)

    # Write HTML to a temporary file
    with tempfile.NamedTemporaryFile(
        suffix=".html", delete=False, mode="w", encoding="utf-8"
    ) as tmp:
        tmp.write(html_content)
        tmp_html = tmp.name

    try:
        result = subprocess.run(
            [
                EDGE_PATH,
                "--headless=new",
                "--disable-gpu",
                "--no-sandbox",
                "--run-all-compositor-stages-before-draw",
                f"--print-to-pdf={pdf_path}",
                "--print-to-pdf-no-header",
                f"file:///{tmp_html.replace(os.sep, '/')}",
            ],
            capture_output=True,
            timeout=30,
        )
        if result.returncode != 0 and not os.path.exists(pdf_path):
            raise RuntimeError(
                f"Edge returned {result.returncode}: {result.stderr.decode(errors='replace')}"
            )
    finally:
        os.unlink(tmp_html)

    return pdf_path


def find_guides(base_dir: str, topic: str | None = None) -> list[str]:
    """Find all guia-*.md and minuta.md files under base_dir, optionally filtered by topic."""
    if topic:
        patterns = [
            os.path.join(base_dir, topic, "guia-*.md"),
            os.path.join(base_dir, topic, "minuta.md"),
        ]
    else:
        patterns = [
            os.path.join(base_dir, "**", "guia-*.md"),
            os.path.join(base_dir, "**", "minuta.md"),
        ]
    files = []
    for pattern in patterns:
        files.extend(glob.glob(pattern, recursive=True))
    return sorted(files)


def main():
    parser = argparse.ArgumentParser(description="Convert guías MD to PDF")
    parser.add_argument("--course", default="iapjn-2026", help="Course ID")
    parser.add_argument("--topic", default=None, help="Specific topic folder name")
    parser.add_argument(
        "--out-dir",
        default=None,
        help="Output directory (default: same folder as each .md file)",
    )
    args = parser.parse_args()

    # Adjust base path if different course
    base_dir = TEMAS_BASE.replace("iapjn-2026", args.course)

    guides = find_guides(base_dir, args.topic)
    if not guides:
        print(f"No guia-*.md files found under {base_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(guides)} guide(s) to convert.\n")
    errors = []

    for md_path in guides:
        rel = os.path.relpath(md_path, base_dir)
        print(f"  Converting {rel} ...", end=" ", flush=True)
        try:
            pdf_path = convert_to_pdf(md_path, out_dir=args.out_dir)
            size_kb = os.path.getsize(pdf_path) // 1024
            print(f"OK ({size_kb} KB) → {os.path.basename(pdf_path)}")
        except Exception as exc:
            print(f"ERROR: {exc}")
            errors.append((rel, str(exc)))

    print()
    total = len(guides)
    ok = total - len(errors)
    print(f"Done: {ok}/{total} converted successfully.")
    if errors:
        print("\nErrors:")
        for path, msg in errors:
            print(f"  {path}: {msg}")
        sys.exit(1)


if __name__ == "__main__":
    main()
