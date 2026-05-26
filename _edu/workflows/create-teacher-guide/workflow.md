# Workflow: Create Teacher Guide

**Module:** edu
**Phase:** 3 — Producción de Temas
**Owner Agent:** class-writer (Roberto)

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
- **Agent:** class-writer (Roberto)
- **Output:** `{topic_folder}/guiaprofesor.md`
- **Estructura canónica (obligatoria):**
  1. Portada: título, fecha, docente, duración de clase
  2. Objetivos de aprendizaje y competencias (de `diseno.md`)
  3. Plan de clase por filmina (tabla: F-XX | título | tiempo | qué decir en síntesis | recurso)
  4. Extractos clave de los PDFs fuente (citas textuales o tablas relevantes, con referencia al archivo)
  5. Sugerencias de preguntas para clase, debates y evaluaciones
  6. Índice de artefactos: ruta local de `minuta.md`, `filminas.md`, `guia-estudio.md`, `tp.md` y PDFs
  7. Referencias y bibliografía (con rutas locales a los PDFs y textos extraídos)

### Step 3: Guardar y versionar
- Recomendar al docente que revise `guiaprofesor.md` y haga commit.
- Esta guía se considera un artefacto de producción del tema, distinto de la guía de estudio del alumno.

---

## Cómo ejecutar

```
/edu-create-teacher-guide
```

(Opción alternativa: ejecutar el workflow directo con `/edu-topic` y luego seleccionar la etapa correspondiente.)

---

## Comportamiento condicional v3

**ACTIVACIÓN v3 — verificar al inicio del workflow:**

```
SI {topic_folder}/topic-extract.md EXISTE
Y  {topic_folder}/.pipeline-v3-state.yaml EXISTE con checkpoint_2_aprobado: true
ENTONCES → comportamiento v3 (ver abajo)
SINO → comportamiento v2 (comportamiento original sin cambios)
```

### Comportamiento v3 (cuando topic-extract.md está presente y aprobado)

Agregar a la estructura canónica de `guiaprofesor.md` estas **secciones adicionales v3**:

1. **Sección 0.5 — Fundamentos bibliográficos (NUEVA en v3):**
   Derivada de `topic-extract.md ## fuentes`. Para cada fuente con `relevancia: alta`:
   - Libro, autor, sección, página, fragmento clave
   - Relevancia pedagógica para este tema

2. **Sección 2.5 — Variantes por nivel de densidad (NUEVA en v3):**
   Tabla con 3 columnas (Nivel 1 / Nivel 2 / Nivel 3) mostrando qué conceptos se incluyen en cada nivel, según `## conceptos-clave` del `topic-extract.md`. Permite al docente conocer cómo el mismo tema se enseña en distintos contextos.

3. **Sección 7.5 — Tendencias académicas (NUEVA en v3):**
   Derivada de `topic-extract.md ## tendencias`. Incluir solo tendencias con `relevancia: alta`. Si hay conflictos con bibliografía, señalar explícitamente qué sección del libro podría estar desactualizada.

**Backup antes de sobrescribir:** Si `guiaprofesor.md` ya existe → crear `guiaprofesor-v2-backup.md` antes de sobrescribir.

### Comportamiento v2 (cuando topic-extract.md NO existe o no tiene checkpoint_2_aprobado: true)

Comportamiento original completo sin ninguna modificación.

