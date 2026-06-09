

<!-- EDU:START -->
## EDU Module — Output Rules

The EDU module lives **exclusively** in `salida/edu-standalone/`. There is no root `_edu/` folder.

### ChromaDB Knowledge Base — chroma-mcp (OBLIGATORIO)

**Todos los agentes EDU** tienen acceso al MCP server `chroma` configurado en `.vscode/mcp.json` (usa [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp) con `--client-type persistent`).

- **Collection activa:** `edu_knowledge` con cosine similarity
- **Tipos de metadata (`type`):** `reference` (12 refs académicas), `tool` (16 docs de herramientas), `material` (libros del curso)
- **Chunk sizes:** reference/tool = 1500 chars, material = 800 chars (chunks pequeños para texto denso de libros sin separación de párrafos)
- **Búsqueda via MCP:** usar `chroma_query_documents` con `collection_name: "edu_knowledge"` y filtrar con `where: {"type": "material"}` si se necesita solo material del curso
- **Ruta ChromaDB:** se guarda en **disco local fuera del repo** (`EDU_CHROMA_PATH` en `.env`, default: `~/.edu/chroma_db`). NUNCA en git. Cada rama usa su propio directorio para evitar solapamientos. Rama `production`: `C:\Users\matia\Documents\chroma_db` (datos ya cargados). Los scripts cargan `.env` automáticamente desde la raíz del repo. Comando: `/edu-ingest`
- **Ingesta incremental (por defecto):** `python salida/edu-standalone/scripts/knowledge_base.py ingest --include-material` (agrega/actualiza sin borrar datos existentes; auto-convierte PDFs de `ingesta/` a TXT con pdfminer)
- **Re-ingesta destructiva (solo si es necesario):** `python salida/edu-standalone/scripts/knowledge_base.py ingest --force --include-material` (borra toda la collection primero)
- **Backup a Drive:** `python salida/edu-standalone/scripts/backup_knowledge_base.py` — comando `/edu-backup`
- **CLI alternativo:** `python salida/edu-standalone/scripts/knowledge_base.py search "query" --type material`

### REGLA CRÍTICA DE RUTAS — Sin excepciones

Cuando cualquier agente (BMAD o EDU) crea o modifica artefactos del módulo EDU, las rutas de destino son:

| Tipo de artefacto | Ruta de destino |
|---|---|
| Agentes EDU | `salida/edu-standalone/_edu/agents/` |
| Workflows EDU | `salida/edu-standalone/_edu/workflows/` |
| Tasks EDU | `salida/edu-standalone/_edu/tasks/` |
| Prompts EDU (`/edu-*`) | `salida/edu-standalone/.github/prompts/` |
| Agent files EDU | `salida/edu-standalone/.github/agents/` |
| Config EDU | `salida/edu-standalone/_edu/config.yaml` |
| Module help EDU | `salida/edu-standalone/_edu/module-help.csv` |

### Qué va a `salida/planning-artifacts/` o `salida/implementation-artifacts/`

Solo artefactos del framework BMAD (PRDs, epics, stories, arquitectura, etc.) que NO sean parte del módulo EDU.

### Deploy

`/goproduction` despliega `salida/edu-standalone/` → rama `production`. GitHub Actions lo ejecuta automáticamente al hacer push a `main` si se modificó algún path dentro de `salida/edu-standalone/`.
<!-- EDU:END -->
