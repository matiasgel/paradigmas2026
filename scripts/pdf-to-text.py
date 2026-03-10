#!/usr/bin/env python3
"""
pdf-to-text.py — Convierte PDFs de material/ a texto plano (UTF-8).

Uso:
    python scripts/pdf-to-text.py                   # procesa toda la carpeta material/
    python scripts/pdf-to-text.py material/          # ídem, explícito
    python scripts/pdf-to-text.py material/lab.pdf   # convierte un PDF específico

Salida:
    Los archivos .txt se guardan en material/txt/<nombre>.txt
    Si el .txt ya existe, el archivo se omite (operación idempotente).

Dependencias:
    pip install pdfminer.six

Compatibilidad: Python 3.8+
"""

import sys
import os
from pathlib import Path


def _ensure_pdfminer():
    """Verifica que pdfminer.six esté instalado."""
    try:
        from pdfminer.high_level import extract_text  # noqa: F401
    except ImportError:
        print(
            "ERROR: Dependencia faltante.\n"
            "  Instalá con:  pip install pdfminer.six\n"
            "  O con uv:     uv pip install pdfminer.six"
        )
        sys.exit(1)


def convert_pdf(pdf_path: Path, output_dir: Path) -> tuple[Path, str]:
    """
    Convierte un PDF a .txt.
    Retorna (output_path, status) donde status es 'converted' o 'skipped'.
    """
    from pdfminer.high_level import extract_text

    output_path = output_dir / (pdf_path.stem + ".txt")

    if output_path.exists():
        return output_path, "skipped"

    text = extract_text(str(pdf_path))
    if not text or not text.strip():
        # PDF sin texto extraíble (imagen escaneada). Generamos aviso.
        text = (
            f"[ADVERTENCIA: El PDF '{pdf_path.name}' no contiene texto extraíble.]\n"
            "[Puede ser una imagen escaneada. Revisá manualmente o usá OCR.]\n"
        )

    output_path.write_text(text, encoding="utf-8")
    return output_path, "converted"


def resolve_targets(arg: str) -> tuple[list[Path], Path]:
    """
    Dado un argumento de línea de comandos (carpeta o archivo .pdf),
    devuelve (lista_de_pdfs, directorio_de_salida).
    """
    target = Path(arg)

    if not target.exists():
        print(f"ERROR: La ruta no existe: {target}")
        sys.exit(1)

    if target.is_file():
        if target.suffix.lower() != ".pdf":
            print(f"ERROR: El archivo no es un PDF: {target}")
            sys.exit(1)
        return [target], target.parent / "txt"

    if target.is_dir():
        pdfs = sorted(target.glob("*.pdf"))
        return pdfs, target / "txt"

    print(f"ERROR: La ruta debe ser un PDF o una carpeta: {target}")
    sys.exit(1)


def main():
    _ensure_pdfminer()

    arg = sys.argv[1] if len(sys.argv) > 1 else "material"
    pdfs, output_dir = resolve_targets(arg)

    if not pdfs:
        print("No se encontraron archivos .pdf en la ruta indicada.")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"PDFs encontrados : {len(pdfs)}")
    print(f"Directorio salida: {output_dir}/\n")

    converted_count = 0
    skipped_count = 0

    for pdf in pdfs:
        out_path, status = convert_pdf(pdf, output_dir)
        if status == "converted":
            print(f"  ✓ Convertido : {pdf.name}  →  {out_path.name}")
            converted_count += 1
        else:
            print(f"  - Omitido    : {pdf.name}  (ya existe {out_path.name})")
            skipped_count += 1

    print(f"\nResumen: {converted_count} convertido(s), {skipped_count} omitido(s).")
    print(f"Textos disponibles en: {output_dir}/")


if __name__ == "__main__":
    main()
