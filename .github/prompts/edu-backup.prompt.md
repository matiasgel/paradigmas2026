---
mode: agent
description: Backup y restore de ChromaDB en Google Drive
---

# /edu-backup — Backup de Knowledge Base en Drive

Hace backup del directorio ChromaDB comprimiéndolo en un ZIP y subiéndolo a la carpeta `edu-chroma-backups` en Google Drive. También permite listar y restaurar backups existentes.

## Pasos según la acción solicitada

### Hacer un backup (por defecto)

```bash
python salida/edu-standalone/scripts/backup_knowledge_base.py
```

Esto:
1. Comprime `EDU_CHROMA_PATH` (o `~/.edu/chroma_db`) en un ZIP con timestamp
2. Sube el ZIP a Drive en la carpeta `edu-chroma-backups`
3. Elimina el ZIP temporal

### Solo backup local (sin subir a Drive)

```bash
python salida/edu-standalone/scripts/backup_knowledge_base.py --local-only
```

Guarda el ZIP en `/tmp/` (o usar `--output-dir /ruta/destino`).

### Listar backups en Drive

```bash
python salida/edu-standalone/scripts/backup_knowledge_base.py --list
```

### Restaurar un backup

```bash
python salida/edu-standalone/scripts/backup_knowledge_base.py --restore edu-chroma-backup-2026-04-27T12-00-00.zip
```

⚠️ **La restauración reemplaza completamente** el directorio ChromaDB local.

## Configuración necesaria

- `EDU_SECRETS_PATH` y `EDU_TOKEN_PATH` en `.env` (mismas credenciales que usa el pipeline de slides)
- Si es la primera vez, se abrirá el navegador para autenticación OAuth

## Notas

- Los backups se acumulan en Drive — no se borran automáticamente
- Se recomienda hacer backup antes de usar `--force` en `/edu-ingest`
- La carpeta en Drive se llama `edu-chroma-backups` y es creada automáticamente si no existe
