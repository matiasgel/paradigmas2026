---
description: 'EDU Fase 3: Crear guía de estudio — genera guia-estudio.md completo para estudio autónomo del alumno, integrando clase y PDFs fuente'
agent: 'edu-agent-study-guide-writer'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables.
   If not found → "Primero iniciá un tema con /edu-design-topic" → STOP.
3. Load `{project-root}/{topic_folder}/topic.yaml` and store all fields as session variables.
4. Verify prerequisites:
   - `{project-root}/{topic_folder}/diseno.md` must exist and contain "APROBADO" → If not: "El diseño del tema no está aprobado. Ejecutá /edu-approve-design primero." → STOP.
   - `{project-root}/{topic_folder}/minuta.md` must exist → If not: "No existe la minuta. Ejecutá /edu-create-class primero." → STOP.
   - `{project-root}/{topic_folder}/filminas.md` must exist → If not: "No existen las filminas. Ejecutá /edu-create-class primero." → STOP.
5. Check if `{project-root}/_edu/templates/study-guide-template.md` exists.
   If yes → load it and pass it to Sofía como constraint estructural para guia-estudio.md.
6. Scan for source PDFs:
   - Check `{project-root}/material/` for PDF files
   - Check `{topic_folder}/` for any PDF files or additional reference material
   - Inform Sofía of all found files so she can integrate them
7. Load and follow the workflow at `{project-root}/_edu/workflows/topic-cycle/workflow.md`.
   Punto de entrada: Step 4.5 (Create Study Guide). El contexto de los pasos 1-6 ya está cargado — no re-inicializar.
8. Purpose: Generate `{topic_folder}/guia-estudio.md` — documento completo de estudio para el alumno.
   - Sigue la estructura de minuta.md y filminas.md como base
   - Integra contenido de los PDFs fuente de material/
   - Incluye desarrollo teórico expandido, ejemplos trabajados, autoevaluación y glosario
   - Es proporcional al scope definido en diseno.md — sin scope creep
   - Va a pasar por los loops de calidad en /edu-quality

