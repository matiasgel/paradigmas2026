---
description: 'EDU Fase 3: Exportar guía de estudio a PDF — genera material de cátedra imprimible con portada, índice y formato académico usando pandoc'
agent: 'agent'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables:
   `{project_name}`, `{institution}`, `{user_name}`, `{communication_language}`.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}`.
   If not found → "Primero iniciá un tema con /edu-design-topic" → STOP.
3. Load `{project-root}/{topic_folder}/topic.yaml` → store all fields.
4. Verify that `{project-root}/{topic_folder}/guia-estudio.md` exists.
   If not → "No existe la guía de estudio. Ejecutá /edu-create-study-guide primero." → STOP.
   Pre-export checks (ejecutar ANTES de generar el PDF, en este orden):
   - Escanear `guia-estudio.md` en busca de marcadores `<!-- PENDIENTE:` → si se encuentran, advertir: "⚠️ La guía contiene marcadores de contenido pendiente. Revisalos antes de distribuir. ¿Continuar igual? [S/N]" → Si N → STOP.
   - Verificar si existe `{topic_folder}/writing-report.md` → si NO existe, advertir: "⚠️ Los loops de calidad no se ejecutaron. Recomendado: /edu-quality antes de exportar. ¿Continuar igual? [S/N]" → Si N → STOP.
5. Determine the current academic year dynamically (use system date) and store it as `{year}` session variable.
6. Generate the YAML front-matter header for pandoc and prepend it to a working copy of guia-estudio.md.
   The front-matter must include:
   ```yaml
   ---
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
   mainfont: "Latin Modern Roman"
   linestretch: 1.25
   header-includes:
     - \usepackage{fancyhdr}
     - \pagestyle{fancy}
     - \fancyhead[L]{{project_name}}
     - \fancyhead[R]{Tema {topic_number}: {topic_name}}
     - \fancyfoot[C]{\thepage}
   ---
   ```
7. Check if pandoc is available:
   - Run: `which pandoc` or `pandoc --version`
   - If available: proceed to step 8
   - If NOT available: show installation instructions and provide the command to run manually → STOP after showing instructions
8. Check LaTeX engine availability:
   - Run: `which pdflatex` or `which xelatex` or `which lualatex`
   - Prefer xelatex (better Unicode/Spanish support), fallback to pdflatex
   - If NO LaTeX engine found: show instructions to install TeX Live and provide pandoc command → STOP
9. Generate the pandoc command and execute it:
   - Output path: `{topic_folder}/guia-estudio.pdf`
   - Working file: `{topic_folder}/_guia-estudio-pandoc.md` (temp file with front-matter prepended)
   - Command template (xelatex):
     ```bash
     pandoc "{topic_folder}/_guia-estudio-pandoc.md" \
       --pdf-engine=xelatex \
       --from=markdown+smart \
       --highlight-style=tango \
       -o "{topic_folder}/guia-estudio.pdf"
     ```
   - Command template (pdflatex fallback):
     ```bash
     pandoc "{topic_folder}/_guia-estudio-pandoc.md" \
       --pdf-engine=pdflatex \
       --from=markdown+smart \
       --highlight-style=pygments \
       -o "{topic_folder}/guia-estudio.pdf"
     ```
10. Execute the pandoc command from `{project-root}`.
    - If SUCCESS: confirm "✅ PDF generado: {topic_folder}/guia-estudio.pdf" and clean up temp file.
    - If ERROR: show the pandoc error message, identify the cause (LaTeX missing packages, encoding issue, etc.) and suggest remediation.
11. If PDF was generated successfully:
    - Update `{topic_folder}/topic.yaml` → add or update field `pdf_exported: true` and `pdf_path: "{topic_folder}/guia-estudio.pdf"`.
    - Optional offer: "¿Querés que genere también una versión con portada dedicada y sin header institucional para distribución digital? [S/N]"
      - If yes: generate an alternative version without the fancyhdr headers, just clean layout

## Notes
- The temp file `_guia-estudio-pandoc.md` is always deleted after export (successful or failed)
- If `guia-estudio.md` contains HTML comments of the form `<!-- PENDIENTE: ... -->`, warn the professor before exporting: "La guía contiene marcadores de contenido pendiente — revisalos antes de distribuir el PDF."
- The PDF is optimized for print (A4, 2.5cm margins) AND digital reading (colored links)
- Running `/edu-export-pdf` multiple times overwrites the previous PDF without warning — mention this to the user at the end

