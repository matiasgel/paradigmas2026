# Workflow: Create Teacher Guide

**Module:** edu
**Phase:** 3 — Producción de Temas
**Owner Agent:** course-planner (orchestrator), class-writer, study-guide-writer

---

## Overview

Genera `guiaprofesor.md` como **documento maestro** para el docente, que contiene:

- Resumen y objetivos del tema
- Plan de clase detallado (tiempos, actividades, hitos)
- Extractos clave de los materiales fuente (PDFs, artículos, libros)
- Resumen de los contenidos generados (minuta, filminas, guía de estudio)
- Sugerencias de cómo usar cada recurso en clase y en autoestudio
- Referencias y enlaces directos a los archivos usados

El objetivo es ofrecer un único punto de repaso para el docente, con todo lo necesario para enseñar el tema y comprender de dónde provino cada decisión pedagógica.

---

## Steps

### Step 1: Validar contexto
- **Precondition:** `{project-root}/_edu/active-topic.yaml` debe existir (generado por `/edu-design-topic` o `/edu-topic`).
- **Input:** `{project-root}/{topic_folder}/diseno.md`, `{topic_folder}/minuta.md`, `{topic_folder}/filminas.md`, `{topic_folder}/guia-estudio.md`.
- **Input adicional (recomendado):** todo el material fuente en `{project-root}/material/{topic_number}-{topic_name}/` (PDFs + txt extraídos) y cualquier archivo en el folder del tema.

### Step 2: Generar `guiaprofesor.md`
- **Agent:** class-writer (Roberto) o study-guide-writer (Sofía)
- **Output:** `{topic_folder}/guiaprofesor.md`
- **Estructura sugerida:**
  1. Portada (título, fecha, docente)
  2. Objetivos de aprendizaje y competencias
  3. Plan de clase por bloques (tiempos, actividades, recursos)
  4. Resumen rápido de cada sección de `minuta.md` + link a `filminas.md`
  5. Fragmentos clave de los PDFs fuente (extraídos de `material/.../txt/`)
  6. Sugerencias para preguntas en clase, debates y trabajos prácticos
  7. Consulta rápida (dónde buscar cada cosa en el repositorio)
  8. Referencias y bibliografía (con enlaces locales a los PDFs y textos)

### Step 3: Guardar y versionar
- Recomendar al docente que revise `guiaprofesor.md` y haga commit.
- Esta guía se considera un artefacto de producción del tema, distinto de la guía de estudio del alumno.

---

## Cómo ejecutar

```
/edu-create-teacher-guide
```

(Opción alternativa: ejecutar el workflow directo con `/edu-topic` y luego seleccionar la etapa correspondiente.)
