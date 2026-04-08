# Workflow: Build Course from Materials

**Module:** edu
**Phase:** 2 — Planificación del Cursado
**Owner Agent:** course-planner, material-ingester (internal)

---

## Overview

Construye el plan del cursado procesando material docente existente (PDFs, PPTX, DOCX).

## Steps

### Step 1: Ingest Materials
- **Agent:** material-ingester (internal)
- **Input:** Folder with existing course materials
- **Action:** Convert all files to structured Markdown
- **Output:** Ingested materials in `{course_output_folder}/_ingestado/`

### Step 2: Analyze & Propose Plan
- **Agent:** course-planner (Elena)
- **Input:** Ingested materials + `plan-minimo.md`
- **Action:** Map existing content to mandatory topics, identify gaps
- **Output:** `plan-borrador.md` with proposed topic sequence and durations

### Step 3: Professor Review
- **Agent:** course-planner (Elena)
- **Gate:** Professor reviews and adjusts the draft plan
- **Output:** Approved `plan-borrador.md`

