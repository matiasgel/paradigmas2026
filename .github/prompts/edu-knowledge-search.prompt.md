---
description: 'EDU: Buscar en la knowledge base ChromaDB — referencias académicas, documentación de herramientas y material del curso'
agent: 'agent'
tools: ['read', 'execute', 'search']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Ask the user:
   > "¿Qué querés buscar en la knowledge base? Podés escribir palabras clave o una pregunta."
   >
   > Opciones de filtro (opcionales):
   > - **Tipo:** `reference` (referencias académicas), `tool` (documentación de herramientas), `material` (libros y apuntes del cursado), o todas (por defecto)
   > - **Cantidad:** número de resultados (por defecto 5)
   >
   > **Referencias disponibles (`--type reference`):** Multimedia Learning (Mayer/Fiorella), Cognitive Load (Sweller/Chen), WCAG 2.2/3.0, FSRS v4, Bloom/Haladyna, Learning Analytics, CS Education/GitHub, Slide Composition, Adaptive Learning/ITS, MCP Protocol, MAIC (Yu et al. 2024, Tsinghua), **OpenMAIC Platform (THU-MAIC 2026 — LangGraph orchestration, whiteboard, PBL, TTS)**.
   >
   > **Herramientas disponibles (`--type tool`):** FSRS (py-fsrs), MCP SDK, ChromaDB, GitHub CLI, GitHub Classroom, GitHub Actions, Google Slides API, JSON Schema, WCAG Quick Reference, OpenMAIC (6 archivos fuente: director-graph, director-prompt, pipeline-types, tool-schemas, scene-generator, outline-generator).
   >
   > **Material del cursado (`--type material`):** libros y apuntes de los docentes ingestados desde `ingesta/` (texto denso, chunks 800 chars).
3. Construct the command:
   ```
   python scripts/knowledge_base.py search "{user_query}"
   ```
   Add `--type reference`, `--type tool`, or `--type material` if the user specified a filter.
   Add `--n {number}` to control number of results (default 5).
4. Execute the command and show the results formatted:
   - For each result, show the **source document**, **relevance score**, and the **matching text chunk**.
   - Group results by document if results come from multiple sources.
5. If the user wants more results or a different query, repeat from step 3.
6. If the user wants to see all available documents, run:
   ```
   python scripts/knowledge_base.py list
   ```
   This shows counts by type (reference / tool / material) and document names.

> **MCP alternativo:** Los agentes pueden también invocar directamente `chroma_query_documents` con `collection_name: "edu_knowledge"` y filtrar con `where: {"type": "material"}` para búsquedas dentro de Copilot sin ejecutar comandos de terminal.
