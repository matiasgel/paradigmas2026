---
description: 'EDU: Buscar en la knowledge base ChromaDB — referencias académicas y documentación de herramientas'
agent: 'agent'
tools: ['read', 'execute', 'search']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Ask the user:
   > "¿Qué querés buscar en la knowledge base? Podés escribir palabras clave o una pregunta."
   >
   > Opciones de filtro (opcionales):
   > - **Tipo:** `reference` (referencias académicas), `tool` (documentación de herramientas), o ambas (por defecto)
   >
   > **Referencias disponibles:** Multimedia Learning (Mayer/Fiorella), Cognitive Load (Sweller/Chen), WCAG 2.2/3.0, FSRS v4, Bloom/Haladyna, Learning Analytics, CS Education/GitHub, Slide Composition, Adaptive Learning/ITS, MCP Protocol, **MAIC — Multi-agent LLM Education (Yu et al. 2024, Tsinghua)**.
   >
   > **Herramientas disponibles:** FSRS (py-fsrs), MCP SDK, ChromaDB, GitHub CLI, GitHub Classroom, GitHub Actions, Google Slides API, JSON Schema, WCAG Quick Reference.
3. Construct the command:
   ```
   python scripts/knowledge_base.py search "{user_query}"
   ```
   Add `--type reference` or `--type tool` if the user specified a filter.
   Add `--n {number}` to control number of results (default 5).
4. Execute the command and show the results formatted:
   - For each result, show the **source document**, **relevance score**, and the **matching text chunk**.
   - Group results by document if results come from multiple sources.
5. If the user wants more results or a different query, repeat from step 3.
6. If the user wants to see all available documents, run:
   ```
   python scripts/knowledge_base.py list
   ```
