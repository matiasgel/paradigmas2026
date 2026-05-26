# Task: Generación de topic-extract.md
# Usada por: topic-designer-v3 (Pasos 1a, 1b, 1c y generación)
# Schema: _edu/schemas/topic-extract-schema.yaml

---

## Contexto de ejecución

Este task es ejecutado por `topic-designer-v3` como parte del pipeline v3.
Prerequisitos al iniciar:
- `{topico}`: nombre del tópico (desde invocación)
- `{libro_principal}`: libro activo (desde config.yaml o `--libro`)
- `{nivel}`: 1, 2 o 3 (desde `--nivel` o default 2)
- `{topic_folder}`: carpeta del tema activo
- `{bibliog_libro_principal}`: resultados ChromaDB del Paso 1a (en sesión)
- `{bibliog_secundaria}`: resultados ChromaDB del Paso 1b (en sesión, puede ser vacío)
- `{tendencias}`: lista de tendencias del Paso 1c (en sesión, puede ser vacío)
- `{superposiciones}`: temas previos solapados del Paso 0 (en sesión, puede ser vacío)

---

## Paso 1a — Extracción ChromaDB libro principal (FAIL-FAST)

### Verificación previa de chroma-mcp

Antes de cualquier query, verificar que chroma-mcp está disponible:
```
chroma_query_documents(
  collection_name: "edu_knowledge",
  query_texts: ["test de disponibilidad"],
  n_results: 1
)
```

Si falla o no responde → **STOP INMEDIATO**:
```
❌ ERROR [paso-1a]: chroma-mcp no disponible.

Diagnóstico:
  1. Verificar que el MCP server está activo en .vscode/mcp.json
  2. La colección "edu_knowledge" debe estar inicializada
  3. Ruta ChromaDB: variable EDU_CHROMA_PATH en .env (default: ~/.edu/chroma_db)

El pipeline NO continúa sin grounding bibliográfico verificado.
Reintentá con @topic-cycle-v3 cuando el servidor esté activo.
```

### Query principal — libro principal

```
chroma_query_documents(
  collection_name: "edu_knowledge",
  query_texts: [
    "{topico}",
    "{topico} conceptos fundamentales",
    "{topico} definición principios"
  ],
  where: {
    "$and": [
      {"type": {"$eq": "material"}},
      {"libro": {"$eq": "{libro_principal}"}}
    ]
  },
  n_results: 10
)
```

Si 0 resultados con filtro libro → reintentar sin filtro `libro`:
```
chroma_query_documents(
  collection_name: "edu_knowledge",
  query_texts: ["{topico}", "{topico} conceptos fundamentales"],
  where: {"type": {"$eq": "material"}},
  n_results: 10
)
```

Si sigue en 0 → STOP:
```
❌ ERROR [paso-1a]: No se encontró material bibliográfico en ChromaDB para "{topico}".

Diagnóstico:
  - La colección "edu_knowledge" no contiene material sobre este tópico
  - Verificar que el libro está ingresado: python salida/edu-standalone/scripts/knowledge_base.py search "{topico}"
  - Considerar ejecutar ingesta: python salida/edu-standalone/scripts/knowledge_base.py ingest --include-material

El pipeline NO continúa sin grounding bibliográfico.
```

### Procesamiento de resultados

Para cada fragmento recuperado:
1. Extraer: `libro`, `autor`, `seccion`, `pagina` (del metadata del chunk)
2. Si `pagina` es null o vacío → marcar como `"⚠️ referencia incompleta"`
3. Crear objeto de fuente:
   ```yaml
   - libro: "[título del libro]"
     autor: "[autor(es)]"
     seccion: "[capítulo/sección]"
     pagina: "[N]"    # o "⚠️ referencia incompleta"
     relevancia: "[alta si similarity_score > 0.8, media si > 0.6]"
     fragmento: "[texto del chunk, máx 200 caracteres]"
   ```
4. Guardar lista consolidada como `{bibliog_libro_principal}` en sesión

---

## Paso 1b — Enriquecimiento con libros secundarios

### Identificar gaps de cobertura

Analizar `{bibliog_libro_principal}` e identificar sub-temas del tópico con cobertura insuficiente (< 2 fragmentos relevantes).

Lista de sub-temas con gap: `{subtemas_sin_cobertura}`

### Query por sub-tema (sin filtro libro)

Para cada sub-tema en `{subtemas_sin_cobertura}`:
```
chroma_query_documents(
  collection_name: "edu_knowledge",
  query_texts: ["{sub-tema}", "{sub-tema} en {topico}"],
  where: {"type": {"$eq": "material"}},
  n_results: 5
)
```

### Deduplicación y consolidación

- Filtrar resultados del `{libro_principal}` (ya en `{bibliog_libro_principal}`)
- Agregar resultados únicos de otros libros a `{bibliog_secundaria}`
- Si todo falla → `{bibliog_secundaria} = []` + ADVERTENCIA:
  ```
  ⚠️ ADVERTENCIA [paso-1b]: No se pudo enriquecer con libros secundarios.
  Continuando con libro principal únicamente.
  ```

---

## Paso 1c — Web research de tendencias académicas

### Búsqueda de tendencias

Buscar (usando herramientas de web disponibles):
- `{topico} tendencias académicas 2023 2024 2025`
- `{topico} computer science research recent developments`
- `{topico} programming paradigm evolution`

### Análisis de conflictos bibliográficos

Para cada tendencia encontrada:
1. Verificar si los libros en `{bibliog_libro_principal}` tienen fecha de publicación > 5 años
2. Si hay conflicto potencial → documentar en `nota`
3. Crear objeto de tendencia:
   ```yaml
   - tendencia: "[descripción de la tendencia]"
     relevancia: "[alta|media|baja según relevancia pedagógica]"
     conflicto_con_bibliografía: "[sí|no]"
     nota: "[Si sí: qué sección del libro podría estar desactualizada]"
     fuente_url: "[URL del artículo/paper si disponible]"
   ```

Si falla → `{tendencias} = []` + ADVERTENCIA:
```
⚠️ ADVERTENCIA [paso-1c]: No se pudo obtener tendencias académicas.
Continuando sin datos de tendencias. Sección 'tendencias' estará vacía en topic-extract.md.
```

---

## Generación de topic-extract.md

### Consolidación bibliográfica

Combinar `{bibliog_libro_principal}` + `{bibliog_secundaria}` en la lista `{fuentes}`.

Para el campo `conceptos-clave`: extraer de los fragmentos los conceptos centrales del tópico:
- Nivel 1: extraer 3–5 conceptos fundamentales (nivel_bloom: recordar/comprender)
- Nivel 2: extraer 5–8 conceptos con aplicación (nivel_bloom: aplicar/analizar)
- Nivel 3: extraer todos los conceptos relevantes (nivel_bloom: analizar/evaluar)

Para el campo `ejemplos-bibliograficos`: extraer de los fragmentos los ejemplos concretos (código, pseudocódigo, casos de estudio).

### Generación del archivo

Generar `{topic_folder}/topic-extract.md` con esta estructura exacta:

```markdown
---
tema: "{topico}"
libro_principal: "{libro_principal}"
nivel: {nivel}
generado_en: "{timestamp ISO 8601}"
aprobado_en: null
version: "1"
---

# topic-extract — {topico}

## fuentes

{lista de fuentes en formato YAML-markdown}

## conceptos-clave

{lista de conceptos en formato YAML-markdown}

## ejemplos-bibliograficos

{lista de ejemplos en formato YAML-markdown}

## tendencias

{lista de tendencias en formato YAML-markdown, o vacío}

## superposiciones-detectadas

{lista de superposiciones del Paso 0, o vacío}
```

### Validaciones post-generación

Ejecutar validaciones antes de presentar CP1:

**V01 — Fuente con página verificada:**
```
¿{fuentes} tiene al menos 1 ítem con pagina != null?
  → No → ERROR: "topic-extract.md no tiene ninguna fuente con página verificada.
     Necesitás al menos una cita con número de página para el CP1."
     No presentar CP1 hasta resolver.
```

**V02 — Mínimo de conceptos:**
```
¿{conceptos-clave} tiene al menos 3 ítems?
  → No → ERROR: "topic-extract.md tiene solo {N} concepto(s). Necesitás al menos 3."
     Agregar conceptos antes de presentar CP1.
```

**V03 — Marcado de incompletas:**
```
Para cada fuente con pagina null:
  → Agregar sufijo " ⚠️ referencia incompleta" al campo fragmento
```

### Formato de referencias (AD §7.2)

En todos los artefactos generados por v3, usar:
```
[Autor, Libro §Sección, p. N]
```
Ejemplo: `[Abelson & Sussman, SICP §1.3, p. 58]`
Sin página: `[Abelson & Sussman, SICP §1.3, p. ⚠️ referencia incompleta]`

---

## Post-generación: presentar Checkpoint 1

Tras validaciones exitosas, mostrar:
```
╔═══════════════════════════════════════════════════════════╗
║  CHECKPOINT 1 — Aprobación de topic-extract.md            ║
║  Revisá: [{topic_folder}/topic-extract.md]                ║
║  Verificá: fuentes, conceptos-clave, ejemplos.            ║
║  Podés editar el archivo directamente antes de responder. ║
║  Respondé "ok" para continuar, o indicá correcciones.    ║
╚═══════════════════════════════════════════════════════════╝
```

Si el docente indica correcciones → aplicar y volver a CP1.
Si responde "ok" → actualizar `aprobado_en` en el frontmatter del topic-extract.md + persistir `checkpoint_1_aprobado: true` en `.pipeline-v3-state.yaml`.
