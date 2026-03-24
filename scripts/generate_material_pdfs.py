#!/usr/bin/env python3
"""
Genera PDFs desde archivos TXT de referencia web.
Guarda los PDFs en material/tema 01/ con nombres descriptivos.

Uso: python scripts/generate_material_pdfs.py
"""

import os
import sys
from fpdf import FPDF

# Base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TXT_DIR = os.path.join(BASE_DIR, "material", "tema 01", "txt")
PDF_DIR = os.path.join(BASE_DIR, "material", "tema 01")

# Mapeo: nombre_txt -> nombre_pdf_salida
ARCHIVOS = [
    ("bootstrap5-grid.txt",       "bootstrap5-grid.pdf"),
    ("bootstrap5-navbar.txt",     "bootstrap5-navbar.pdf"),
    ("bootstrap5-card.txt",       "bootstrap5-card.pdf"),
    ("w3schools-css-flexbox.txt", "w3schools-css-flexbox.pdf"),
    ("html-css.txt",              "html-css-filminas.pdf"),
    ("tp1.txt",                   "tp1-consigna.pdf"),
    ("tp2.txt",                   "tp2-consigna.pdf"),
]


def crear_pdf(txt_path: str, pdf_path: str, titulo: str) -> bool:
    """Convierte un archivo TXT a PDF usando fpdf2."""
    try:
        with open(txt_path, "r", encoding="utf-8") as f:
            contenido = f.read()
    except FileNotFoundError:
        print(f"  [SKIP] No encontrado: {txt_path}")
        return False

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Título
    pdf.set_font("Helvetica", style="B", size=14)
    pdf.cell(0, 10, titulo, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    # Contenido
    pdf.set_font("Courier", size=9)

    page_width = pdf.w - pdf.l_margin - pdf.r_margin

    for linea in contenido.split("\n"):
        # Evitar caracteres no soportados por la fuente básica
        linea_safe = linea.encode("latin-1", errors="replace").decode("latin-1")

        # Detectar encabezados
        if linea_safe.startswith("==") or linea_safe.startswith("--"):
            continue  # separador visual, saltar
        elif linea_safe.isupper() and len(linea_safe.strip()) > 2 and not linea_safe.startswith(" "):
            # Línea de encabezado en mayúsculas
            pdf.set_font("Helvetica", style="B", size=10)
            pdf.cell(0, 6, linea_safe[:90], new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("Courier", size=9)
        elif linea_safe.strip().startswith("#"):
            # Línea de comentario/título markdown
            pdf.set_font("Helvetica", style="B", size=10)
            pdf.cell(0, 6, linea_safe.strip()[:90], new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("Courier", size=9)
        else:
            # Truncar línea si es demasiado larga para evitar overflow
            pdf.set_font("Courier", size=9)
            # Calcular caracteres máximos por línea (~90 chars en Courier 9)
            MAX_LINE = 110
            if len(linea_safe) > MAX_LINE:
                # Dividir en chunks
                for i in range(0, len(linea_safe), MAX_LINE):
                    chunk = linea_safe[i:i+MAX_LINE]
                    pdf.cell(0, 5, chunk, new_x="LMARGIN", new_y="NEXT")
            else:
                pdf.cell(0, 5, linea_safe, new_x="LMARGIN", new_y="NEXT")

    pdf.output(pdf_path)
    return True


def main():
    os.makedirs(PDF_DIR, exist_ok=True)

    print(f"Generando PDFs en: {PDF_DIR}")
    print("-" * 50)

    exitosos = 0
    fallidos = 0

    for nombre_txt, nombre_pdf in ARCHIVOS:
        txt_path = os.path.join(TXT_DIR, nombre_txt)
        pdf_path = os.path.join(PDF_DIR, nombre_pdf)
        titulo = nombre_pdf.replace(".pdf", "").replace("-", " ").replace("_", " ").title()

        print(f"  {nombre_txt} -> {nombre_pdf} ... ", end="", flush=True)
        ok = crear_pdf(txt_path, pdf_path, titulo)
        if ok:
            size_kb = os.path.getsize(pdf_path) // 1024
            print(f"OK ({size_kb} KB)")
            exitosos += 1
        else:
            fallidos += 1

    print("-" * 50)
    print(f"Resultado: {exitosos} PDFs generados, {fallidos} omitidos.")

    if exitosos > 0:
        print(f"\nPDFs disponibles en: material/tema 01/")


if __name__ == "__main__":
    main()
