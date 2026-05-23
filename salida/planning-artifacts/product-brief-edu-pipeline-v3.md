---
title: "Product Brief: EDU Production Pipeline v3 — Bibliographic-First, Density Levels & BMAD Step-by-Step"
status: "complete"
created: "2026-05-23"
updated: "2026-05-23"
inputs:
  - salida/planning-artifacts/sprints-mejoras-edu-v2.md
  - salida/planning-artifacts/arquitectura-pipeline-filminas-v4.md
  - salida/edu-standalone/_edu/config.yaml
  - salida/edu-standalone/_edu/agents/ (24 agentes mapeados)
  - salida/edu-standalone/_edu/workflows/ (16+ workflows mapeados)
---

# Product Brief: EDU Production Pipeline v3
## Bibliographic-First, Density Levels & BMAD Step-by-Step

**Proyecto:** Paradigmas y Lenguajes de Programación 2026  
**Stakeholder:** Matiasgel (docente responsable)  
**Fecha:** 23 de mayo de 2026

---

## Resumen Ejecutivo

El módulo EDU cuenta hoy con un sistema maduro de 24 agentes y 16+ workflows que produce material docente completo. Sin embargo, el pipeline de producción de temas tiene una limitación estructural: los agentes razonan y generan en bloques largos sin anclaje bibliográfico explícito, sin controlar el nivel de profundidad del material, y sin verificar coherencia con lo ya enseñado. El resultado son sesiones de generación largas propensas a interrupciones, material que asume conocimiento previo que no fue cubierto (o repite lo que ya se dio), y filminas de densidad uniforme que no sirven por igual para una clase introductoria y para un repaso exhaustivo.

Esta mejora refactoriza el corazón del pipeline — los cuatro agentes de producción (`topic-designer`, `class-writer`, `study-guide-writer`, `create-teacher-guide`) — para que operen según tres principios nuevos: **BMAD step-by-step** (plan explícito → pasos atómicos), **bibliographic-first** (los libros y tendencias académicas informan todo el contenido), y **density-aware** (el profesor elige el nivel de profundidad). El impacto esperado: menos interrupciones, material más coherente con la cursada y los libros, y control granular sobre la complejidad del contenido generado.

---

## El Problema

### 1. Agentes que razonan demasiado tiempo sin checkpoint

El flujo `topic-cycle` produce `diseno.md → minuta.md → filminas.md → guia-estudio.md` en operaciones largas sin estado intermedio persistido. Cuando una generación es interrumpida — por timeout, por corrección del profesor, o por un cambio de criterio a mitad de proceso — hay que reiniciar desde cero. No hay un "plan de generación" explícito que el profesor pueda revisar y aprobar antes de que el agente ejecute.

Esto viola las nuevas convenciones BMAD, que exigen que los agentes primero produzcan un plan y luego ejecuten paso a paso, con el profesor pudiendo intervenir entre pasos.

### 2. Generación sin anclaje bibliográfico

Los agentes actuales generan filminas y material sin consultar primero los libros de la materia en ChromaDB. El contenido se produce desde el conocimiento del modelo, no desde la bibliografía acordada con los alumnos. Esto produce inconsistencias terminológicas, énfasis que no coinciden con los libros, y material que es difícil de correlacionar con las lecturas obligatorias.

Hay un `academic-researcher` (Carlos) que hace búsquedas académicas, pero no está integrado como paso obligatorio previo en el pipeline de producción de temas.

### 3. Sin niveles de densidad

Todas las filminas y material se generan con la misma profundidad. Un docente que necesita una clase introductoria (primera exposición al tema) y uno que necesita material de repaso exhaustivo para un parcial usan el mismo agente con el mismo output. No hay forma de indicar "quiero filminas simples y directas" vs "quiero filminas completamente explicadas, sin asumir nada".

### 4. Sin coherencia curricular activa

Los agentes no verifican qué temas ya fueron dados en la cursada antes de generar. Un tópico puede cubrir conceptos que el alumno ya vio dos clases atrás, o puede asumir conceptos que aún no se dieron. El `curriculum-reviewer` existe pero no es invocado automáticamente en el pipeline de producción.

### 5. Sin reutilización de material del año anterior

Cuando hay filminas del año anterior que el profesor considera válidas como base, los agentes las ignoran completamente y generan desde cero. Se pierde el trabajo previo y se fragmenta la evolución histórica del material.

---

## La Solución

Refactorizar los cuatro agentes de producción para que sigan un **pipeline atómico de siete pasos**, con artefactos intermedios persistidos y control del profesor en los puntos de inflexión.

### Pipeline Nuevo (por tema)

```
┌─────────────────────────────────────────────────────────────┐
│ PASO 0 — Coherencia curricular                               │
│   Consulta temas ya dados → detecta superposiciones          │
│   → ajusta estructura del tópico antes de empezar           │
├─────────────────────────────────────────────────────────────┤
│ PASO 1a — Extracción libro principal (ChromaDB)              │
│   El libro principal es: config de la materia OR indicado   │
│   por el profesor en el prompt de activación                 │
├─────────────────────────────────────────────────────────────┤
│ PASO 1b — Enriquecimiento bibliográfico complementario       │
│   Libros secundarios del corpus → completan y enriquecen    │
│   (solo contenido vigente, descarta material desactualizado) │
├─────────────────────────────────────────────────────────────┤
│ PASO 1c — Investigación de tendencias académicas             │
│   Web research: últimas tendencias, papers relevantes,       │
│   evolución reciente del tema                                │
├─────────────────────────────────────────────────────────────┤
│ ARTEFACTO INTERMEDIO: topic-extract.md                       │
│   Núcleo del tópico con referencias, enriquecimiento y       │
│   tendencias. Usado por TODOS los agentes downstream.        │
│   ✅ CHECKPOINT — Profesor puede revisar y ajustar           │
├─────────────────────────────────────────────────────────────┤
│ PASO 2 — Plan de generación                                  │
│   Lista ordenada de filminas/secciones a generar             │
│   Con nivel de densidad (1/2/3) por sección o global        │
│   ✅ CHECKPOINT — Profesor puede reordenar filminas          │
├─────────────────────────────────────────────────────────────┤
│ PASO 3 — Generación paso a paso (por nivel de densidad)      │
│   Nivel 1: Filminas simples, conceptos clave, ejemplos       │
│            directos. Material del alumno introductorio.      │
│   Nivel 2: Filminas estándar con desarrollo y contexto.      │
│            Material del alumno completo.                     │
│   Nivel 3: Filminas completamente explicadas, sin asumir     │
│            nada. Material exhaustivo de estudio profundo.    │
├─────────────────────────────────────────────────────────────┤
│ PASO 4 — Material del alumno (de topic-extract + filminas)   │
│ PASO 5 — Material docente (guía del profesor)                │
└─────────────────────────────────────────────────────────────┘
```

### Reutilización de filminas del año anterior

Si el profesor indica filminas del año anterior al activar el agente, el pipeline las toma como **base de renovación** en lugar de generar desde cero. El agente las compara con el `topic-extract.md` nuevo, identifica qué actualizar, qué conservar y qué eliminar. Esto preserva la evolución histórica del material y reduce el trabajo de generación.

---

## Principios de Implementación

| Principio | Descripción |
|-----------|-------------|
| **BMAD Step-by-Step** | Cada agente produce primero un plan explícito. El docente puede aprobarlo o modificarlo antes de ejecutar. Cada paso es una llamada atómica. |
| **Bibliographic-First** | ChromaDB se consulta siempre antes de generar contenido. El modelo complementa la bibliografía, no la reemplaza. |
| **Intermediate Artifacts** | `topic-extract.md` es el artefacto pivote. Todos los agentes downstream lo consumen del disco, no re-consultan ChromaDB. |
| **Aditivo / Opt-in** | Consistent con `sprints-mejoras-edu-v2.md`: sin modificaciones destructivas, todo activable por flags en config. Los workflows actuales siguen funcionando. |
| **ChromaDB via MCP** | La extracción usa `chroma-mcp` (ya configurado en `.vscode/mcp.json`). Config de la base en `.env` (`EDU_CHROMA_PATH`). Si el plugin no está instalado, se auto-instala en la primera llamada. |

---

## Quién se Beneficia

**Docente (Matiasgel)** — Produce temas en menos pasos, con material anclado en los libros de la materia, controlando el nivel de profundidad. Puede intervenir entre pasos sin perder el trabajo hecho. No repite contenido ya enseñado.

**Alumnos (indirectamente)** — Reciben material de coherencia curricular garantizada, con profundidad adecuada al momento de la cursada, y terminología consistente con los libros que leen.

**El sistema EDU** — Los agentes downstream (`class-writer`, `study-guide-writer`, `create-teacher-guide`) trabajan desde un artefacto validado (`topic-extract.md`) en lugar de regenerar el contexto cada vez.

---

## Criterios de Éxito

| Criterio | Indicador |
|----------|-----------|
| Generación sin interrupciones | Un tema completo se genera sin timeout ni reinicio manual |
| Anclaje bibliográfico | El `topic-extract.md` cita explícitamente secciones del libro principal |
| Coherencia curricular | El agente detecta y reporta superposiciones con temas previos |
| Niveles funcionales | El mismo tópico se puede generar en nivel 1, 2 y 3 con diferencia visible de densidad |
| Reúso de año anterior | Si se proveen filminas del año anterior, al menos el 40% se reutiliza/adapta |
| Checkpoints respetados | El profesor puede aprobar/modificar el plan antes de ejecutar cada paso |

---

## Decisiones de Diseño Clave

| # | Decisión | Elección para v1 | Rationale |
|---|----------|------------------|-----------|
| A | Formato `topic-extract.md` | Estructura fija con secciones: `fuentes`, `conceptos-clave`, `ejemplos-bibliograficos`, `tendencias`, `superposiciones-detectadas` | Permite que los agentes downstream lo consuman de forma predecible |
| B | Granularidad del nivel de densidad | **Global por invocación** (1 nivel para todo el tema) | Más simple para v1; por sección queda para v2 |
| C | Punto de entrada del profesor | **Nuevo workflow `topic-cycle-v3`** que extiende el existente; el `topic-cycle` original sigue funcionando sin cambios | Principio aditivo/opt-in del sprint plan |
| D | Retrocompatibilidad con temas ya generados | **Solo temas nuevos en v1**. Los temas existentes pueden generar su `topic-extract.md` invocando manualmente el PASO 1, pero no es obligatorio | Evita complejidad de migración en cursada ya comenzada |
| E | Vigencia bibliográfica (PASO 1b) | El agente marca el contenido como "a verificar" si el libro tiene más de 5 años en el tema tratado y hay tendencias académicas contradictorias del PASO 1c | Criterio operacional concreto |
| F | Conflicto libro config vs libro en prompt | **El prompt tiene precedencia**; el agente informa explícitamente qué libro usó como principal | Flexibilidad máxima al docente |

---

## Alcance — Primera Versión

**Incluido:**
- Nuevo workflow `topic-cycle-v3` (no reemplaza `topic-cycle`, lo extiende)
- Refactorización de los 4 agentes de producción: `topic-designer`, `class-writer`, `study-guide-writer`, `create-teacher-guide`
- Nuevo artefacto intermedio `topic-extract.md` con esquema definido (sección Decisiones A)
- Integración de `chroma-mcp` como paso explícito y obligatorio (PASOS 1a/1b)
- Investigación de tendencias académicas vía web research (PASO 1c)
- Paso de coherencia curricular (PASO 0) consultando temas previos del año
- Tres niveles de densidad globales configurables por invocación del workflow
- Soporte para filminas del año anterior como base opcional de renovación
- Actualización del workflow `create-teacher-guide` para consumir `topic-extract.md`

**Excluido — primera versión:**
- Cambios al schema registry v3 (inmutable por principio de arquitectura)
- Cambios al pipeline de publicación a Google Slides (`slides_pipeline.py`)
- Cambios a los agentes de calidad y testing (`writing-validator`, `student-simulator`, etc.)
- Niveles de densidad por sección individual (queda para v2)
- Retrocompatibilidad automática con temas ya generados en 2026
- Nuevas funcionalidades de los sprints S7-S13 (`sprints-mejoras-edu-v2.md`)

---

## Visión

Si este pipeline se consolida, el módulo EDU evoluciona hacia un sistema donde el docente define **qué tema**, **qué libros**, y **qué nivel de profundidad** — y el sistema produce material coherente, bibliográficamente anclado y pedagógicamente calibrado, con la historia del material anterior como contexto vivo. En el mediano plazo, el `topic-extract.md` se convierte en el nodo central del grafo de conocimiento de la materia, alimentando también el tutor adaptativo, el generador de TPs y el simulador de estudiantes.

---

---

*Brief completo. Generado con el skill `bmad-product-brief` (Stage 5). Próximo paso: crear el PRD usando este brief y el detail pack como inputs.*
