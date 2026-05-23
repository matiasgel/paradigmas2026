# Retrospectiva Epic E1 — Pipeline base v3

**Epic:** E1 — Pipeline base v3
**Sprint:** 1
**Fecha:** 2026-05-23
**Stories:** 1.1, 1.2, 1.3, 1.4, 1.5

---

## Resumen de ejecución

| Story | Título | Status | Issues resueltos |
|-------|--------|--------|-----------------|
| 1.1 | Crear workflow topic-cycle-v3 | ✅ | 0 blocker, 0 high |
| 1.2 | Crear agente topic-designer-v3 | ✅ | 0 blocker, 0 high |
| 1.3 | Persistencia de estado | ✅ | Integrado en 1.1+1.2 |
| 1.4 | Checkpoint 1 | ✅ | Integrado en 1.1+1.2 |
| 1.5 | Checkpoint 2 | ✅ | Integrado en 1.1+1.2 |

**Archivos creados:** 2 artefactos de producción + 5 story files
**Issues blocker:** 0
**Issues high auto-fixed:** 0

---

## Artefactos creados

- `salida/edu-standalone/_edu/workflows/topic-cycle-v3/workflow.md` — pipeline completo de 7 pasos con estado, CP1 y CP2
- `salida/edu-standalone/_edu/agents/topic-designer-v3.md` — agente Marcos v3 con lógica de Pasos 0–1c y checkpoints

---

## Decisiones de implementación

1. **Stories 1.3/1.4/1.5 integradas en 1.1/1.2:** La lógica de persistencia y checkpoints está intrínsecamente acoplada al workflow y al agente. Implementar como archivos separados hubiera creado fragmentación innecesaria.
2. **Constraint brownfield respetado al 100%:** Los archivos `topic-cycle/workflow.md` y `topic-designer.md` permanecen intactos.
3. **State machine completa:** El esquema `.pipeline-v3-state.yaml` implementa AD-01 de la arquitectura con campos: `pasos_completados`, `checkpoint_1_aprobado`, `checkpoint_2_aprobado`, timestamps.

---

## Próximo sprint

**Sprint 2 — E2: Bibliographic-first**
- 2.1: Crear esquema formal topic-extract-schema.yaml
- 2.2: Paso 1a — extracción ChromaDB con fail-fast
- 2.3: Paso 1b — enriquecimiento libros secundarios
- 2.4: Paso 1c — web research tendencias
- 2.5: Generación completa topic-extract.md con validaciones
