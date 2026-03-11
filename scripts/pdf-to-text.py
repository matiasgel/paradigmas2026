#!/usr/bin/env python3
"""
pdf-to-text.py — Convierte PDFs de material/ a texto plano (UTF-8).

Estructura esperada:
    material/
        01-intro/
            ref1.pdf
            ref2.pdf
            txt/          ← generado automáticamente
                ref1.txt
                ref2.txt
        02-poo/
            ...

Uso:
    python scripts/pdf-to-text.py                        # procesa todas las subcarpetas de material/
    python scripts/pdf-to-text.py material/              # ídem, explícito
    python scripts/pdf-to-text.py material/01-intro/     # solo la subcarpeta de ese tema
    python scripts/pdf-to-text.py material/01-intro/ref1.pdf  # convierte un PDF específico

Salida:
    Los archivos .txt se guardan en <subcarpeta-tema>/txt/<nombre>.txt
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


def resolve_targets(arg: str) -> list[tuple[Path, Path]]:
    """
    Dado un argumento de línea de comandos (carpeta o archivo .pdf),
    devuelve una lista de pares (pdf_path, output_dir).

    Lógica:
    - Archivo .pdf    → [(pdf, carpeta-padre/txt)]
    - Carpeta hoja    → PDFs directamente dentro → [(pdf, carpeta/txt) ...]
    - Carpeta raíz    → subcarpetas con PDFs    → [(pdf, subdir/txt) ...] por cada subdir
    """
    target = Path(arg)

    if not target.exists():
        print(f"ERROR: La ruta no existe: {target}")
        sys.exit(1)

    if target.is_file():
        if target.suffix.lower() != ".pdf":
            print(f"ERROR: El archivo no es un PDF: {target}")
            sys.exit(1)
        return [(target, target.parent / "txt")]

    if target.is_dir():
        pairs: list[tuple[Path, Path]] = []

        # PDFs directamente en esta carpeta → van a target/txt/
        for pdf in sorted(target.glob("*.pdf")):
            pairs.append((pdf, target / "txt"))

        # PDFs en subcarpetas de tema → cada una tiene su propio subdir/txt/
        subdirs = sorted(d for d in target.iterdir() if d.is_dir() and d.name != "txt")
        for subdir in subdirs:
            for pdf in sorted(subdir.glob("*.pdf")):
                pairs.append((pdf, subdir / "txt"))

        return pairs

    print(f"ERROR: La ruta debe ser un PDF o una carpeta: {target}")
    sys.exit(1)


def main():
    _ensure_pdfminer()

    arg = sys.argv[1] if len(sys.argv) > 1 else "material"
    pairs = resolve_targets(arg)

    if not pairs:
        print("No se encontraron archivos .pdf en la ruta indicada.")
        return

    print(f"PDFs encontrados : {len(pairs)}\n")

    converted_count = 0
    skipped_count = 0
    current_dir: Path | None = None

    for pdf, output_dir in pairs:
        # Imprimir encabezado de carpeta cuando cambia
        if output_dir != current_dir:
            current_dir = output_dir
            output_dir.mkdir(parents=True, exist_ok=True)
            print(f"  [{output_dir.parent.name}/]")

        out_path, status = convert_pdf(pdf, output_dir)
        if status == "converted":
            print(f"    ✓ Convertido : {pdf.name}  →  txt/{out_path.name}")
            converted_count += 1
        else:
            print(f"    - Omitido    : {pdf.name}  (ya existe txt/{out_path.name})")
            skipped_count += 1

    print(f"\nResumen: {converted_count} convertido(s), {skipped_count} omitido(s).")


if __name__ == "__main__":
    main()
