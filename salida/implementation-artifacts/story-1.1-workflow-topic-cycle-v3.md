# Story 1.1 — Crear workflow topic-cycle-v3 con estructura de 7 pasos

**ID:** S1.1
**Epic:** E1 — Pipeline base v3
**Status:** Ready for Dev
**Creado:** 2026-05-23

---

## Descripción / User Story

**Como** docente universitario de Paradigmas de Programación,
**quiero** invocar `@topic-cycle-v3 [tópico] --libro [libro] --nivel [1|2|3]`
**para** que el agente orqueste un pipeline de 7 pasos con estado persistido, grounding bibliográfico obligatorio y niveles de densidad, sin interferir con el workflow v2 existente.

---

## Criterios de Aceptación

### CA-1 — Archivos en rutas correctas
- `salida/edu-standalone/_edu/workflows/topic-cycle-v3/workflow.md` existe y es operativo.
- `salida/edu-standalone/_edu/workflows/topic-cycle/workflow.md` (v2) permanece sin modificaciones.

### CA-2 — Invocación con parámetros explícitos
- `@topic-cycle-v3 Prog. Funcional --libro SICP --nivel 2` → output visible: tópico + "Libro: SICP" + "Nivel: 2 — Estándar".

### CA-3 — Fallback a libro_principal
- Sin `--libro` → lee `libro_principal` de `_edu/config.yaml` e informa qué libro fue seleccionado.

### CA-4 — Fallback a nivel 2 por defecto
- Sin `--nivel` → adopta nivel 2 e informa: "Nivel no especificado — usando nivel 2 (Estándar) por defecto."

### CA-5 — Secuencia de pasos preservada
El workflow sigue la secuencia: Paso 0 → Paso 1a → Paso 1b → Paso 1c → CP1 → Paso 2 → CP2 → Paso 3 → Paso 4 → Paso 5

---

## Tasks de Implementación

- [x] T1: Crear `salida/edu-standalone/_edu/workflows/topic-cycle-v3/workflow.md`
- [x] T2: Implementar resolución de parámetros `--libro` y `--nivel` en Paso 0
- [x] T3: Documentar estructura completa de 7 pasos con contratos de entrada/salida
- [x] T4: Definir formato de `.pipeline-v3-state.yaml`
- [x] T5: Definir mensajes de bienvenida y progreso

---

## Archivos

| Op | Ruta | Nota |
|----|------|------|
| CREAR | `salida/edu-standalone/_edu/workflows/topic-cycle-v3/workflow.md` | Nuevo v3 |
| NO TOCAR | `salida/edu-standalone/_edu/workflows/topic-cycle/workflow.md` | Constraint brownfield |

---

## Constraint Brownfield

**NUNCA modificar** `salida/edu-standalone/_edu/workflows/topic-cycle/workflow.md`.
