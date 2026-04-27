---
mode: agent
description: Ingestar documentos en la knowledge base ChromaDB (incremental por defecto)
---

# /edu-ingest — Ingestión de Knowledge Base

Ingestá documentos en ChromaDB. El modo por defecto es **incremental**: agrega y actualiza documentos sin borrar los existentes.

## Pasos

1. Verificar que el entorno virtual esté activo y ChromaDB configurado:
   ```
   source .venv/bin/activate  # o .venv\Scripts\activate en Windows
   ```

2. Determinar qué modo de ingesta aplicar según la solicitud del usuario:

   | Solicitud | Comando |
   |---|---|
   | Ingestar solo referencias y herramientas | `python salida/edu-standalone/scripts/knowledge_base.py ingest` |
   | Ingestar todo (incluyendo libros/PDFs de `ingesta/`) | `python salida/edu-standalone/scripts/knowledge_base.py ingest --include-material` |
   | Borrar todo y reingestar desde cero | `python salida/edu-standalone/scripts/knowledge_base.py ingest --force --include-material` |

3. **Por defecto** (si el usuario solo dice "ingestar" o "actualizar la base"), ejecutar el modo incremental con material:
   ```
   python salida/edu-standalone/scripts/knowledge_base.py ingest --include-material
   ```
   Esto procesará todos los documentos en `_edu-knowledge/` y los PDFs/TXTs de `ingesta/`.

4. Verificar el resultado con:
   ```
   python salida/edu-standalone/scripts/knowledge_base.py list
   ```

## Notas importantes

- La base de datos se guarda en `EDU_CHROMA_PATH` (configurado en `.env`) o en `~/.edu/chroma_db` por defecto. **Nunca dentro del repo.**
- El flag `--force` **borra toda la collection** antes de reingestar. Usar solo cuando se necesite limpiar datos corruptos o cambiar el esquema de chunks.
- Los PDFs en `ingesta/` se convierten automáticamente a TXT si no tienen conversión previa.
- Para agregar nuevo material: colocarlo en `ingesta/` y ejecutar el comando incremental.
