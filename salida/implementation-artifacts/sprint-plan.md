---
generado: '2026-05-23'
proyecto: paradigmas2026
workflow: topic-cycle-v3
total_epics: 6
total_stories: 23
sprint_actual: 1
---

# Sprint Plan — topic-cycle-v3

**Generado:** 2026-05-23  
**Proyecto:** paradigmas2026  
**Total stories:** 23 en 6 epics  
**Sprint actual:** Sprint 1

---

## Resumen de Epics

| Epic | Nombre | Stories | Sprint | Status |
|---|---|---|---|---|
| E1 | Pipeline base v3 | 5 | 1 | ⬜ No iniciado |
| E2 | Bibliographic-first | 5 | 2 | ⬜ No iniciado |
| E6 | Agentes downstream | 4 | 3 | ⬜ No iniciado |
| E4 | Niveles de densidad | 3 | 4 | ⬜ No iniciado |
| E3 | Coherencia curricular | 3 | 5 | ⬜ No iniciado |
| E5 | Renovación de año anterior | 3 | 6 | ⬜ No iniciado |

---

## Orden de implementación y justificación

El orden elegido es **E1 → E2 → E6 → E4 → E3 → E5**, motivado por las siguientes dependencias:

- **E1 primero:** Es el andamiaje del pipeline. Sin el workflow `topic-cycle-v3`, el agente `topic-designer-v3`, el estado `.pipeline-v3-state.yaml` y los dos checkpoints, no existe un contexto en el que los demás epics puedan funcionar.

- **E2 segundo:** Implementa el corazón funcional del pipeline v3 — el grounding bibliográfico obligatorio vía ChromaDB y la generación del artefacto `topic-extract.md`. Todos los epics siguientes dependen del artefacto que E2 produce.

- **E6 tercero (antes de E4):** Los agentes downstream deben recibir la lógica condicional v3 antes de que E4 les agregue los modificadores de densidad. Si se invierte el orden, E4 estaría modificando archivos sin la estructura v3 preparada, generando conflictos de edición.

- **E4 cuarto:** Con los agentes ya preparados (E6), E4 agrega únicamente los modificadores de prompt de densidad — un cambio quirúrgico sobre archivos ya refactorizados.

- **E3 quinto:** La coherencia curricular (Paso 0) es funcionalmente independiente de E4. Se ubica aquí para no interrumpir el sprint de agentes downstream/densidad.

- **E5 último:** El análisis comparativo con filminas del año anterior depende de `topic-extract.md` funcional (E2), de CP1 implementado (E1) y de class-writer refactorizado (E6). Es el epic más desacoplado y puede entregarse sin bloquear la funcionalidad principal.

---

## Story Board

### Sprint 1 — E1: Pipeline base v3

> **Objetivo del sprint:** Crear el andamiaje completo del workflow v3: archivos, agente, estado y checkpoints. Al finalizar, el docente puede invocar `@topic-cycle-v3 [tópico]` y el pipeline persiste su estado entre sesiones.

#### Story 1.1: Crear workflow topic-cycle-v3 con estructura de 7 pasos
- **Status:** ⬜ No iniciado
- **FRs:** FR01, FR03, FR24, FR25
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 1.2: Crear agente topic-designer-v3
- **Status:** ⬜ No iniciado
- **FRs:** FR01, FR24
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 1.3: Implementar persistencia de estado del pipeline
- **Status:** ⬜ No iniciado
- **FRs:** FR26
- **NFRs:** NFR01, NFR03
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 1.4: Implementar Checkpoint 1 — aprobación de topic-extract.md
- **Status:** ⬜ No iniciado
- **FRs:** FR13, FR14
- **NFRs:** NFR03
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 1.5: Implementar Checkpoint 2 — aprobación del plan de generación
- **Status:** ⬜ No iniciado
- **FRs:** FR15, FR16
- **NFRs:** NFR03
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

---

### Sprint 2 — E2: Bibliographic-first

> **Objetivo del sprint:** Implementar los Pasos 1a, 1b y 1c del pipeline (ChromaDB, libros secundarios, web research), el esquema formal `topic-extract-schema.yaml` y la generación completa del artefacto `topic-extract.md` con validaciones.

#### Story 2.1: Crear esquema formal topic-extract-schema.yaml
- **Status:** ⬜ No iniciado
- **FRs:** FR12
- **NFRs:** NFR09
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 2.2: Implementar Paso 1a — extracción ChromaDB libro principal con fail-fast
- **Status:** ⬜ No iniciado
- **FRs:** FR02, FR08
- **NFRs:** NFR02, NFR07
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 2.3: Implementar Paso 1b — enriquecimiento con libros secundarios
- **Status:** ⬜ No iniciado
- **FRs:** FR09
- **NFRs:** NFR07
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 2.4: Implementar Paso 1c — web research de tendencias académicas
- **Status:** ⬜ No iniciado
- **FRs:** FR10, FR11
- **NFRs:** NFR07
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 2.5: Implementar generación completa de topic-extract.md con validaciones
- **Status:** ⬜ No iniciado
- **FRs:** FR12, FR13, FR14
- **NFRs:** NFR04, NFR05
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

---

### Sprint 3 — E6: Agentes downstream

> **Objetivo del sprint:** Agregar lógica condicional v3 a los tres agentes downstream y el mecanismo de backup. Al finalizar, los agentes detectan automáticamente si deben operar en modo v2 o v3 sin intervención manual, con cero regresión en flujos v2.

#### Story 6.1: Agregar lógica condicional v3 a class-writer.md
- **Status:** ⬜ No iniciado
- **FRs:** FR20, FR24, FR26
- **NFRs:** NFR06
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 6.2: Agregar lógica condicional v3 a study-guide-writer.md
- **Status:** ⬜ No iniciado
- **FRs:** FR18
- **NFRs:** NFR06, NFR07
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 6.3: Agregar lógica condicional v3 a create-teacher-guide.md
- **Status:** ⬜ No iniciado
- **FRs:** FR19
- **NFRs:** NFR06
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 6.4: Implementar mecanismo de backup de artefactos v2 en todos los agentes downstream
- **Status:** ⬜ No iniciado
- **FRs:** FR26
- **NFRs:** NFR06
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

---

### Sprint 4 — E4: Niveles de densidad

> **Objetivo del sprint:** Implementar el parámetro `--nivel` como parámetro de primera clase y los modificadores de prompt diferenciados (N1/N2/N3) en class-writer y study-guide-writer. Prerequisito: agentes ya con lógica v3 (Sprint 3).

#### Story 4.1: Implementar parámetro --nivel y propagación al estado del pipeline
- **Status:** ⬜ No iniciado
- **FRs:** FR01 (parcial), FR17
- **NFRs:** NFR08
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 4.2: Implementar modificadores de densidad en class-writer (niveles 1, 2 y 3)
- **Status:** ⬜ No iniciado
- **FRs:** FR17, FR20
- **NFRs:** NFR06, NFR08
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 4.3: Implementar propagación de nivel en study-guide-writer
- **Status:** ⬜ No iniciado
- **FRs:** FR18 (parcial)
- **NFRs:** NFR06, NFR08
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

---

### Sprint 5 — E3: Coherencia curricular

> **Objetivo del sprint:** Implementar el Paso 0 del pipeline — escaneo de temas previos, reporte de superposiciones y captura de estrategia de tratamiento. Al finalizar, el docente recibe aviso explícito antes de generar material con conceptos ya cubiertos en la cursada.

#### Story 3.1: Implementar Paso 0 — escaneo del registro de temas dados
- **Status:** ⬜ No iniciado
- **FRs:** FR05
- **NFRs:** NFR01 (parcial)
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 3.2: Implementar reporte de coherencia curricular con formato estándar
- **Status:** ⬜ No iniciado
- **FRs:** FR06
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 3.3: Capturar estrategia de superposición y propagarla al topic-extract.md
- **Status:** ⬜ No iniciado
- **FRs:** FR07
- **NFRs:** NFR01 (parcial)
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

---

### Sprint 6 — E5: Renovación de año anterior

> **Objetivo del sprint:** Implementar el flujo completo de `--base` — lectura de filminas previas, análisis comparativo contra topic-extract.md (conservar/actualizar/eliminar/nueva), reporte de renovación en CP2 y priorización de reúso en la generación.

#### Story 5.1: Implementar procesamiento del parámetro --base
- **Status:** ⬜ No iniciado
- **FRs:** FR04
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 5.2: Implementar análisis comparativo filminas previas vs topic-extract.md
- **Status:** ⬜ No iniciado
- **FRs:** FR21
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

#### Story 5.3: Implementar reporte de renovación y priorización en generación
- **Status:** ⬜ No iniciado
- **FRs:** FR22, FR23
- **Para implementar:** ejecutar `bmad-create-story` → `bmad-dev-story`

---

## Estado general

| Métrica | Valor |
|---|---|
| Total de epics | 6 |
| Total de stories | 23 |
| Stories completadas | 0 |
| Stories en progreso | 0 |
| Stories no iniciadas | 23 |
| Sprint actual | 1 |
| Sprints estimados | 6 |
| **Próxima story** | **1.1 — Crear workflow topic-cycle-v3 con estructura de 7 pasos** |

---

## Próximo paso

Para comenzar la implementación:

1. Ejecutar `bmad-create-story` para preparar la Story 1.1 con todo el contexto del epics.md
2. Ejecutar `bmad-dev-story` para implementar Story 1.1
3. Ejecutar `bmad-code-review` para validar Story 1.1
4. Actualizar `sprint-status.yaml`: cambiar status de `1.1` a `completed`
5. Pasar a Story 1.2 y repetir

> **Regla de actualización:** Tras completar cada story, actualizar `sprint-status.yaml` con el nuevo status. Cuando todas las stories de un epic tengan `completed`, actualizar el status del epic.
