import sys
from pathlib import Path
from markdown_it import MarkdownIt
from xhtml2pdf import pisa

def md_to_pdf(md_path, pdf_path):
    md = Path(md_path).read_text(encoding="utf-8")
    mdi = MarkdownIt()
    html_body = mdi.render(md)
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {{ font-family: Arial, sans-serif; font-size: 11pt; margin: 2cm; }}
h1,h2,h3,h4 {{ color: #333; }}
code, pre {{ background: #f4f4f4; padding: 4px; font-family: monospace; font-size: 10pt; }}
pre {{ padding: 10px; border-left: 3px solid #ccc; }}
</style>
</head>
<body>{html_body}</body>
</html>"""
    with open(pdf_path, "wb") as f:
        result = pisa.CreatePDF(html, dest=f, encoding="utf-8")
    if result.err:
        print(f"ERROR: {result.err}")
        return False
    print(f"OK: {pdf_path}")
    return True

base = Path("salida/cursadas/2026/temas/05-monadas-ts")
for name in ["guia-estudio", "guiaprofesor"]:
    md = base / f"{name}.md"
    pdf = base / f"{name}.pdf"
    if md.exists():
        md_to_pdf(str(md), str(pdf))
    else:
        print(f"NOT FOUND: {md}")
