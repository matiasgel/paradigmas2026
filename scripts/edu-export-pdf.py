#!/usr/bin/env python
"""
edu-export-pdf.py — Exporta guia-estudio.md a PDF usando pandoc + tectonic.
Uso: python scripts/edu-export-pdf.py [topic_folder]
     Si no se pasa topic_folder, usa el activo en _edu/active-topic.yaml
"""
import os
import sys
import subprocess
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    # 1. Cargar config
    config = load_yaml(ROOT / "_edu" / "config.yaml")
    project_name = config["project_name"]
    institution = config["institution"]
    user_name = config["user_name"]

    # 2. Cargar active-topic
    active = load_yaml(ROOT / "_edu" / "active-topic.yaml")
    topic_folder = ROOT / active["topic_folder"]
    topic_number = active["topic_number"]
    topic_name = active["topic_name"]

    print(f"📄 Exportando: Tema {topic_number} — {topic_name}")

    # 3. Verificar guia-estudio.md
    guia = topic_folder / "guia-estudio.md"
    if not guia.exists():
        print("❌ No existe guia-estudio.md. Ejecutá /edu-create-study-guide primero.")
        sys.exit(1)

    # 4. Pre-export checks
    content = guia.read_text(encoding="utf-8")
    if "<!-- PENDIENTE:" in content:
        print("⚠️  La guía contiene marcadores <!-- PENDIENTE: -->. Revisalos antes de distribuir.")

    if not (topic_folder / "writing-report.md").exists():
        print("⚠️  Los loops de calidad no se ejecutaron. Recomendado: /edu-quality antes de exportar.")

    # 5. Pandoc path (desde pypandoc_binary)
    try:
        import pypandoc
        pandoc_path = pypandoc.get_pandoc_path()
    except Exception:
        pandoc_path = "pandoc"  # fallback a PATH del sistema

    # 6. Tectonic path (en .venv/Scripts/)
    tectonic_path = ROOT / ".venv" / "Scripts" / "tectonic.exe"
    if not tectonic_path.exists():
        tectonic_path = "tectonic"  # fallback a PATH del sistema

    # 7. Generar front-matter y archivo temporal
    year = "2026"
    # Nota: header-includes con LaTeX se inyectan directamente en el .tex
    # para evitar problemas de parseo YAML con llaves { }
    frontmatter = f"""---
title: "{topic_name}"
subtitle: "Guía de Estudio — Tema {topic_number}"
author: "{user_name}"
institute: "{institution}"
date: "Ciclo lectivo {year}"
subject: "{project_name}"
lang: "es"
toc: true
toc-depth: 3
toc-title: "Índice de Contenidos"
numbersections: true
colorlinks: true
linkcolor: "blue"
urlcolor: "blue"
geometry: "margin=2.5cm"
fontsize: "11pt"
linestretch: 1.25
---

"""
    temp_file = topic_folder / "_guia-estudio-pandoc.md"
    temp_file.write_text(frontmatter + content, encoding="utf-8")

    # 8. Ejecutar pandoc (dos pasos: md → tex, luego tectonic tex → pdf)
    output_pdf = topic_folder / "guia-estudio.pdf"
    temp_tex = topic_folder / "_guia-estudio-pandoc.tex"

    # Paso A: pandoc genera .tex a partir del .md
    cmd_tex = [
        str(pandoc_path),
        str(temp_file),
        "--from=markdown+smart",
        "--to=latex",
        "--highlight-style=tango",
        "--standalone",
        "-o", str(temp_tex),
    ]

    # Paso B: tectonic compila el .tex a .pdf
    cmd_pdf = [
        str(tectonic_path),
        "--outdir", str(topic_folder),
        "--keep-logs",
        str(temp_tex),
    ]

    print(f"⚙️  Paso 1/2 — pandoc genera LaTeX...")

    tex_result = None
    tec_result = None
    try:
        tex_result = subprocess.run(cmd_tex, capture_output=True, text=True, cwd=str(ROOT))
        if tex_result.returncode != 0:
            print(f"❌ Error pandoc→tex (código {tex_result.returncode}):")
            print(tex_result.stderr)
            return

        # Inyectar fancyhdr en el .tex ANTES de \begin{document}
        tex_content = temp_tex.read_text(encoding="utf-8")
        fancyhdr_block = (
            "\n\\usepackage{fancyhdr}\n"
            "\\pagestyle{fancy}\n"
            f"\\fancyhead[L]{{{project_name}}}\n"
            f"\\fancyhead[R]{{Tema {topic_number}: {topic_name}}}\n"
            "\\fancyfoot[C]{\\thepage}\n"
        )
        tex_content = tex_content.replace("\\begin{document}", fancyhdr_block + "\\begin{document}", 1)
        temp_tex.write_text(tex_content, encoding="utf-8")

        print(f"⚙️  Paso 2/2 — tectonic compila PDF (primera vez descarga paquetes LaTeX ~30s)...")
        tec_result = subprocess.run(cmd_pdf, capture_output=True, text=True, cwd=str(ROOT))

        # El PDF generado por tectonic tiene el nombre del .tex
        generated_pdf = topic_folder / "_guia-estudio-pandoc.pdf"
        if tec_result.returncode == 0 and generated_pdf.exists():
            generated_pdf.rename(output_pdf)
            print(f"✅ PDF generado: {active['topic_folder']}/guia-estudio.pdf")
            # Actualizar topic.yaml
            topic_yaml_path = topic_folder / "topic.yaml"
            if topic_yaml_path.exists():
                topic_data = load_yaml(topic_yaml_path)
                topic_data["pdf_exported"] = True
                topic_data["pdf_path"] = f"{active['topic_folder']}/guia-estudio.pdf"
                with open(topic_yaml_path, "w", encoding="utf-8") as f:
                    yaml.dump(topic_data, f, allow_unicode=True, default_flow_style=False)
                print("   topic.yaml actualizado con pdf_exported: true")
        else:
            print(f"❌ Error tectonic (código {tec_result.returncode}):")
            print(tec_result.stderr[-3000:] if tec_result.stderr else "(sin salida)")
    finally:
        for f in [temp_file, temp_tex]:
            if f.exists():
                f.unlink()
        print("   Archivos temporales eliminados.")


if __name__ == "__main__":
    main()
