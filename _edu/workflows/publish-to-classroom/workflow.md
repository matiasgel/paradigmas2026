# Workflow: Publicar a GitHub Classroom

## Objetivo
Publicar un TP como assignment de GitHub Classroom con autograding y deadline configurable.

## Prerequisitos
- `gh` CLI instalado con `gh classroom` extension
- `classroom_enabled: true` en `config.yaml`
- `classroom_org` y `classroom_id` configurados
- El directorio `autograde-repo/` existe en el tema

## Pasos

### Paso 1 — Verificar prerequisitos
1. Verificar que `classroom_enabled` está activo en `config.yaml`
2. Ejecutar `python scripts/classroom_publish.py check` para validar `gh` CLI y auth
3. Si falla, mostrar instrucciones de instalación

### Paso 2 — Preparar assignment
1. Leer `topic.yaml` del tema para obtener título y deadline
2. Verificar que `autograde-repo/` existe en el directorio del tema
3. Calcular fecha límite (fecha actual + `classroom_default_deadline_days`)

### Paso 3 — Publicar
1. Ejecutar: `python scripts/classroom_publish.py --topic {topic_id} --course {course_id}`
2. El script crea el assignment en GitHub Classroom y devuelve el invite link
3. Mostrar el link al docente

### Paso 4 — Post-publicación
1. Registrar en `memory.db` la publicación (categoría: `classroom-publish`)
2. Informar al docente que puede ver las entregas en GitHub Classroom

## Notas
- El script NO modifica el autograde-repo
- Si el assignment ya existe, informa sin duplicar
- El invite link se guarda en `{topic_folder}/classroom-invite.txt`
