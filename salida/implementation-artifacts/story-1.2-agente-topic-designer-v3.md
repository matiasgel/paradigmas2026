# Story 1.2 — Crear agente topic-designer-v3

**ID:** S1.2
**Epic:** E1 — Pipeline base v3
**Status:** Ready for Dev
**Creado:** 2026-05-23

---

## Descripción / User Story

**Como** docente, **quiero** un agente `topic-designer-v3.md` independiente del `topic-designer.md` existente, con la persona extendida de Marcos v3 y capacidad de ejecutar los Pasos 0–1c, generar `topic-extract.md` y presentar los Checkpoints 1 y 2, **para** ejecutar el pipeline v3 sin riesgo de regresión en el agente de producción actual.

---

## Criterios de Aceptación

### CA-1 — Independencia total del agente v2
- `salida/edu-standalone/_edu/agents/topic-designer.md` permanece sin ninguna modificación.
- `salida/edu-standalone/_edu/agents/topic-designer-v3.md` existe como nuevo archivo.

### CA-2 — Identidad Marcos v3
- Al activarse, el agente se identifica como "Marcos v3" con responsabilidades explícitas: Pasos 0–1c, generación de `topic-extract.md`, Checkpoints 1 y 2.

### CA-3 — Reanudación automática
- Si `.pipeline-v3-state.yaml` existe con `pasos_completados: ["paso-1a", "paso-1b"]`, el agente informa "Reanudando desde Paso 1c" y no re-ejecuta Pasos 0, 1a, 1b.

### CA-4 — Contrato de salida
- Antes de invocar `class-writer`, el state file tiene `checkpoint_1_aprobado: true` Y `checkpoint_2_aprobado: true`.

---

## Archivos

| Op | Ruta | Nota |
|----|------|------|
| CREAR | `salida/edu-standalone/_edu/agents/topic-designer-v3.md` | Nuevo agente |
| NO TOCAR | `salida/edu-standalone/_edu/agents/topic-designer.md` | Constraint brownfield |

---

## Constraint Brownfield

**NUNCA modificar** `salida/edu-standalone/_edu/agents/topic-designer.md`.
