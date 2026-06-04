---
applyTo: "**"
---

# 🔒 EDU Standalone — Reglas de Protección de Archivos Inmutables

## CRÍTICO: Archivos que NINGÚN agente puede modificar

Los siguientes paths son **de solo lectura** para todos los agentes del módulo EDU.
**NUNCA** crear, editar, renombrar ni borrar archivos en estas rutas:

### 1. Schemas del pipeline (`_edu/schemas/`)
- `_edu/schemas/schema-registry.json` — Manifiesto inmutable del pipeline
- `_edu/schemas/filmina-slide.schema.json` — Contrato por filmina
- `_edu/schemas/plan-filminas.schema.json` — Contrato de plan completo
- `_edu/schemas/design-system.schema.json` — Contrato del sistema de diseño
- `_edu/schemas/*.schema.json` — **Todos** los schemas

**Razón:** Los schemas son el contrato técnico del pipeline. Modificarlos sin bump de versión rompe reproducibilidad y corrompe planes existentes.

### 2. Scripts del pipeline (`scripts/`)
- `scripts/slides_pipeline.py` — Motor de publicación Google Slides
- `scripts/validate_plan.py` — Validador de contratos
- `scripts/repair_plan.py` — Orquestador de corrección
- `scripts/refresh_plan.py` — Actualizador de plan sin pérdida de assets
- `scripts/pipeline_common.py` — Módulo base compartido
- `scripts/parse_filminas.py` — Parser filminas.md → JSON DRAFT
- `scripts/*.py` — **Todos** los scripts
- `scripts/requirements.txt`

**Razón:** Los scripts son binarios de producción auditados. Los agentes los ejecutan, no los programan.

### 3. Templates del módulo (`_edu/templates/`)
- `_edu/templates/class-template.md`
- `_edu/templates/filminas-schema.yaml`
- `_edu/templates/filminas-template.md`
- `_edu/templates/prompt-imagen-guide.md`

**Razón:** Los templates son la especificación de formato para Roberto y Diego. Cambiarlos mid-cursada genera inconsistencias.

---

## Qué SÍ pueden hacer los agentes

| Acción | Rutas permitidas |
|--------|-----------------|
| Leer (siempre) | Todo el proyecto |
| Ejecutar (siempre) | `scripts/*.py` |
| Crear y editar | `{topics_folder}/**` (filminas.md, minuta.md, diseño.md, topic.yaml, .pipeline-state.json, plan-filminas-*.json, slides-url.txt, *.gift) |
| Crear y editar | `_edu/config.yaml`, `_edu/active-topic.yaml`, `_edu/slides-config.yaml` |
| Crear y editar | `_edu-memory/**` (memory.db, calibraciones) |
| Crear y editar | `_edu/knowledge/**` (ontología, documentos de referencia) |

---

## Si un script o schema necesita cambio

1. El agente detecta la necesidad → reporta al docente con descripción exacta del cambio
2. El docente lo escala al Arquitecto (BMAD)  
3. El Arquitecto hace el cambio con bump de versión (`schema-registry.json` v4.0.0)
4. El cambio se documenta y comunica a todos los agentes

---

## Protección técnica adic

- `.gitattributes` marca `_edu/schemas/*.json` y `scripts/*.py` como `linguist-generated merge=ours`
- `copilot-instructions.md` restricciones #12–#16 aplican a nivel workspace
- Esta instrucción aplica a todos los archivos del workspace (`applyTo: "**"`)
