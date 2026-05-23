# Workflow: topic-cycle-v3

**Module:** edu
**Version:** 3.0
**Phase:** 3 — Producción de Temas (v3 — Bibliographic-First + Niveles de Densidad)
**Owner Agent:** topic-designer-v3
**Constraint brownfield:** Este workflow es NUEVO. `_edu/workflows/topic-cycle/workflow.md` (v2) permanece invariante.

---

## Overview

Pipeline completo de producción de un tema con grounding bibliográfico obligatorio vía ChromaDB, niveles de densidad parametrizables, dos checkpoints de aprobación docente, y estado persistido por sesión.

**Invocación canónica:**
```
@topic-cycle-v3 [tópico] [--libro LIBRO] [--nivel 1|2|3] [--base RUTA_FILMINAS_PREVIAS]
```

**Ejemplos:**
```
@topic-cycle-v3 Programación Funcional
@topic-cycle-v3 Programación Funcional --libro SICP --nivel 2
@topic-cycle-v3 Programación Funcional --nivel 3
@topic-cycle-v3 Paradigma OO --nivel 2 --base temas/04-oo/filminas.md
```

---

## Mensaje de bienvenida (obligatorio al inicio)

Al activarse, mostrar siempre:

```
🚀 topic-cycle-v3 iniciado

Tópico:         {topico}
Libro activo:   {libro_principal}  [desde config.yaml | --libro]
Nivel:          {nivel} — {nombre_nivel}  [por defecto: 2 | --nivel]
Base previa:    {base_filminas | "ninguna"}

Estado:         {nuevo pipeline | reanudando desde Paso {N}}
```

Si no se especificó `--nivel` → agregar: "ℹ️ Nivel no especificado — usando nivel 2 (Estándar) por defecto."
Si no se especificó `--libro` → agregar: "ℹ️ Libro resuelto desde config.yaml: {libro_principal}"

---

## Niveles de densidad

| Nivel | Nombre | Taxonomía Bloom | Descripción operacional |
|-------|--------|-----------------|------------------------|
| 1 | Introductorio | Recordar / Comprender | Conceptos clave y 1 ejemplo directo; sin variantes ni detalles de implementación |
| 2 | Estándar | Aplicar / Analizar | Contexto completo, 2–3 ejemplos, comparación contextual |
| 3 | Exhaustivo | Analizar / Evaluar | Todos los conceptos, múltiples ejemplos, contra-ejemplos, sin asumir conocimiento previo |

---

## Estado del Pipeline (.pipeline-v3-state.yaml)

El agente crea y actualiza este archivo en `{topic_folder}/.pipeline-v3-state.yaml` al completar cada paso.

**Esquema:**
```yaml
topic: "Programación Funcional"
libro_principal: "SICP"
nivel: 2
base_filminas_previas: null          # o path relativo al topic_folder
pasos_completados: []                # ["paso-0", "paso-1a", "paso-1b", "paso-1c"]
checkpoint_1_aprobado: false
checkpoint_2_aprobado: false
iniciado_en: "2026-05-23T14:30:00"  # ISO 8601
ultimo_paso_en: "2026-05-23T14:45:00"
status: "in-progress"               # "in-progress" | "completed" | "failed"
```

**Regla de reanudación:** Al inicio de cada sesión, si `.pipeline-v3-state.yaml` existe en `{topic_folder}/`, leerlo y reanudar desde el primer paso no completado. Informar al docente qué paso se retoma.

---

## Steps

### Paso 0: Inicialización y resolución de parámetros

**Precondición:** Invocación del workflow con tópico mínimo.

**Acciones:**
1. Leer `{project-root}/salida/edu-standalone/_edu/config.yaml` → obtener `libro_principal`, `topics_folder`, `course_id`, `communication_language`
2. Leer `{project-root}/salida/edu-standalone/_edu/active-topic.yaml` → obtener `topic_folder`, `topic_number`, `topic_name` (si existe)
3. Resolver parámetros:
   - `--libro` presente → usar ese libro; sino usar `config.yaml → libro_principal`
   - `--nivel` presente → usar ese nivel; sino usar nivel 2 por defecto
   - `--base` presente → guardar path de filminas previas
4. Verificar si existe `{topic_folder}/.pipeline-v3-state.yaml`:
   - Si existe → leer y reanudar (saltar al primer paso no completado)
   - Si no existe → crear con valores iniciales (ver esquema arriba)
5. Mostrar mensaje de bienvenida con tópico, libro, nivel y estado

**Output:** `.pipeline-v3-state.yaml` creado o leído. Variables de sesión: `{topic}`, `{libro}`, `{nivel}`, `{topic_folder}`
**Al completar:** Agregar `"paso-0"` a `pasos_completados` y actualizar `ultimo_paso_en`

---

### Paso 1a: Extracción ChromaDB — libro principal (FAIL-FAST)

**Precondición:** `paso-0` en `pasos_completados`

**Acciones:**
1. Verificar disponibilidad de `chroma-mcp` (intentar query de prueba)
2. Si `chroma-mcp` NO responde → **STOP inmediato** con mensaje:
   ```
   ❌ ERROR [paso-1a]: chroma-mcp no disponible.
   Diagnóstico: verificar que el MCP server está activo en .vscode/mcp.json
   El pipeline NO continúa sin grounding bibliográfico verificado.
   Reintentá con /topic-cycle-v3 cuando el server esté activo.
   ```
3. Ejecutar query ChromaDB:
   ```
   chroma_query_documents(
     collection_name: "edu_knowledge",
     query_texts: ["{topico}", "{topico} conceptos fundamentales", "{topico} definición"],
     where: {"type": "material", "libro": "{libro_principal}"},
     n_results: 10
   )
   ```
4. Si 0 resultados → intentar sin filtro de libro; si sigue en 0 → STOP con diagnóstico
5. Consolidar fragmentos relevantes; marcar con `⚠️ referencia incompleta` los que tengan `pagina: null`
6. Guardar resultados como contexto de sesión `{bibliog_libro_principal}`

**Output:** Contexto bibliográfico del libro principal.
**Al completar:** Agregar `"paso-1a"` a `pasos_completados`

---

### Paso 1b: Enriquecimiento ChromaDB — libros secundarios

**Precondición:** `paso-1a` en `pasos_completados`

**Acciones:**
1. Identificar sub-temas del tópico no suficientemente cubiertos en Paso 1a
2. Para cada sub-tema sin cobertura:
   ```
   chroma_query_documents(
     collection_name: "edu_knowledge",
     query_texts: ["{sub-tema}"],
     where: {"type": "material"},
     n_results: 5
   )
   ```
3. Filtrar resultados del libro principal (ya capturados en 1a) para evitar duplicados
4. Agregar resultados a `{bibliog_secundaria}`
5. Si falla (chroma-mcp error) → **ADVERTENCIA** (no bloqueante) + continuar:
   ```
   ⚠️ ADVERTENCIA [paso-1b]: No se pudo enriquecer con libros secundarios. Continuando con libro principal únicamente.
   ```

**Output:** Contexto bibliográfico enriquecido `{bibliog_completa}` = `{bibliog_libro_principal}` + `{bibliog_secundaria}`
**Al completar:** Agregar `"paso-1b"` a `pasos_completados`

---

### Paso 1c: Web research — tendencias académicas

**Precondición:** `paso-1b` en `pasos_completados`

**Acciones:**
1. Buscar tendencias académicas recientes del tópico (últimos 5 años)
2. Identificar conflictos con bibliografía de más de 5 años
3. Formato de cada tendencia:
   ```yaml
   - tendencia: "Descripción"
     relevancia: "alta|media|baja"
     conflicto_con_bibliografía: "sí|no"
     nota: "Si conflicto=sí: qué sección del libro podría estar desactualizada"
     fuente_url: "URL si disponible"
   ```
4. Si falla → **ADVERTENCIA** (no bloqueante) + continuar con `tendencias: []`

**Output:** Lista `{tendencias}` para incluir en `topic-extract.md`
**Al completar:** Agregar `"paso-1c"` a `pasos_completados`

---

### CHECKPOINT 1 — Aprobación de topic-extract.md

**Precondición:** `paso-1c` en `pasos_completados`; `topic-extract.md` generado

**Acciones:**
1. Generar `{topic_folder}/topic-extract.md` con el esquema completo (ver §Esquema topic-extract.md abajo)
2. Validar: `fuentes` tiene al menos 1 ítem con `pagina` no nulo
3. Mostrar bloque de checkpoint:
   ```
   ╔═══════════════════════════════════════════════════════════╗
   ║  CHECKPOINT 1 — Aprobación de topic-extract.md            ║
   ║  Revisá: [{topic_folder}/topic-extract.md]                ║
   ║  Verificá: fuentes, conceptos-clave, ejemplos.            ║
   ║  Podés editar el archivo directamente antes de responder. ║
   ║  Respondé "ok" para continuar, o indicá correcciones.    ║
   ╚═══════════════════════════════════════════════════════════╝
   ```
4. Si docente indica correcciones → aplicar y volver a mostrar CP1 (sin continuar)
5. Si docente responde "ok" → persistir `checkpoint_1_aprobado: true` en state file y continuar

**Output:** `topic-extract.md` aprobado; `checkpoint_1_aprobado: true` en state file

---

### Paso 2: Plan de generación

**Precondición:** `checkpoint_1_aprobado: true` en state file

**Acciones:**
1. Leer `topic-extract.md` → extraer lista de conceptos a cubrir
2. Si `--base` fue especificado → ejecutar análisis comparativo filminas previas vs topic-extract.md:
   - Categorizar filminas previas: `conservar` | `actualizar` | `eliminar` | `nueva`
   - Incluir análisis en el plan
3. Generar lista numerada de filminas con:
   - Número, título descriptivo
   - Conceptos cubiertos (del topic-extract.md)
   - Nivel de densidad aplicado
   - Acción si viene de `--base`: conservar/actualizar/nueva
4. Presentar plan con CHECKPOINT 2

---

### CHECKPOINT 2 — Aprobación del plan de generación

**Precondición:** Plan generado en Paso 2

**Acciones:**
1. Mostrar plan completo de filminas
2. Mostrar bloque de checkpoint:
   ```
   ╔═══════════════════════════════════════════════════════════╗
   ║  CHECKPOINT 2 — Aprobación del plan de generación         ║
   ║  Revisá el plan de filminas arriba.                       ║
   ║  Podés reordenar, agregar o eliminar filminas.            ║
   ║  Respondé "ok" para generar, o indicá modificaciones.    ║
   ╚═══════════════════════════════════════════════════════════╝
   ```
3. Si docente indica modificaciones → aplicar (reordenar/agregar/eliminar) y volver a presentar CP2
4. Si docente responde "ok" → persistir `checkpoint_2_aprobado: true` y continuar

**Output:** Plan aprobado; `checkpoint_2_aprobado: true` en state file

---

### Paso 3: Generación de filminas

**Precondición:** `checkpoint_2_aprobado: true` en state file

**Acciones:**
1. Leer nivel del state file: `nivel` (1, 2 o 3)
2. Si existe `{topic_folder}/filminas.md` → hacer backup: `{topic_folder}/filminas-v2-backup.md`
3. Invocar agente `class-writer` con:
   - `topic-extract.md` como fuente primaria
   - Nivel de densidad según state file
   - Plan aprobado en CP2
4. Output: `{topic_folder}/filminas.md`, `{topic_folder}/minuta.md`

**Al completar:** Agregar `"paso-3"` a `pasos_completados`

---

### Paso 4: Guía de estudio

**Precondición:** `paso-3` en `pasos_completados`

**Acciones:**
1. Invocar agente `study-guide-writer` con:
   - `topic-extract.md` como fuente bibliográfica primaria
   - `filminas.md` y `minuta.md` como contexto de clase
   - Nivel de densidad desde state file
2. Output: `{topic_folder}/guia-estudio.md`

**Al completar:** Agregar `"paso-4"` a `pasos_completados`

---

### Paso 5: Guía docente

**Precondición:** `paso-4` en `pasos_completados`

**Acciones:**
1. Invocar agente `create-teacher-guide` con:
   - `topic-extract.md` (sección fuentes + tendencias)
   - `filminas.md`, `minuta.md`, `guia-estudio.md`
   - Nivel de densidad desde state file
2. Output: `{topic_folder}/guiaprofesor.md`
3. Actualizar state file: `status: "completed"`, agregar `"paso-5"` a `pasos_completados`
4. Mostrar resumen final:
   ```
   ✅ topic-cycle-v3 completado

   Tópico:   {topico}
   Nivel:    {nivel} — {nombre_nivel}
   Libro:    {libro_principal}

   Artefactos generados:
   - {topic_folder}/topic-extract.md   ← grounding bibliográfico
   - {topic_folder}/filminas.md
   - {topic_folder}/minuta.md
   - {topic_folder}/guia-estudio.md
   - {topic_folder}/guiaprofesor.md
   ```

---

## Esquema topic-extract.md

```markdown
---
tema: "{topico}"
libro_principal: "{libro_principal}"
nivel: {nivel}
generado_en: "{ISO timestamp}"
aprobado_en: null    # se actualiza en CP1
version: "1"
---

# topic-extract — {topico}

## fuentes
- libro: "[Título]"
  autor: "[Autor(es)]"
  seccion: "[Capítulo/Sección]"
  pagina: "[N o rango N-M]"    # null → marcar "⚠️ referencia incompleta"
  relevancia: "alta|media"
  fragmento: "[Cita textual breve o paráfrasis]"

## conceptos-clave
- concepto: "[Nombre]"
  definicion: "[1-2 oraciones]"
  fuente_seccion: "[libro §sección]"
  nivel_bloom: "recordar|comprender|aplicar|analizar|evaluar"

## ejemplos-bibliograficos
- titulo: "[Nombre descriptivo]"
  descripcion: "[Qué ilustra]"
  codigo_o_texto: |
    [Contenido del ejemplo]
  fuente_libro: "[libro]"
  fuente_pagina: "[página]"

## tendencias
- tendencia: "[Descripción]"
  relevancia: "alta|media|baja"
  conflicto_con_bibliografía: "sí|no"
  nota: "[Si conflicto=sí: qué sección podría estar desactualizada]"
  fuente_url: "[URL si disponible]"

## superposiciones-detectadas
- tema_previo: "[NN-nombre-tema]"
  conceptos_solapados: "[Lista de conceptos]"
  nivel_solapamiento: "alto|medio|bajo"
  estrategia: "asumir-conocido|resumir|referenciar"
```

**Validaciones:**
- `fuentes`: mínimo 1 ítem con `pagina` no nulo
- `conceptos-clave`: mínimo 3 ítems
- `superposiciones-detectadas`: puede estar vacío

---

## Política de coexistencia de artefactos

Antes de sobrescribir artefactos v2, hacer backup:

| Artefacto | Acción v3 |
|-----------|-----------|
| `filminas.md` | Backup → `filminas-v2-backup.md` antes de sobrescribir |
| `minuta.md` | Backup → `minuta-v2-backup.md` antes de sobrescribir |
| `guia-estudio.md` | Backup → `guia-estudio-v2-backup.md` antes de sobrescribir |
| `guiaprofesor.md` | Backup → `guiaprofesor-v2-backup.md` antes de sobrescribir |
| `topic-extract.md` | Nuevo — sin colisión |
| `.pipeline-v3-state.yaml` | Nuevo — sin colisión |

---

## Constraint brownfield

`_edu/workflows/topic-cycle/workflow.md` permanece **invariante**. Este workflow (v3) opera en paralelo. No hereda ni modifica el workflow v2.
