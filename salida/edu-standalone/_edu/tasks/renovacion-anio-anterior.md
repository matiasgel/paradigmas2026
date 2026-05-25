# Task: Renovación de año anterior — análisis comparativo
# Ejecutado por: topic-designer-v3 (topic-cycle-v3/workflow.md Paso 2)
# Activación: SOLO cuando `--base RUTA_FILMINAS_PREVIAS` fue especificado en la invocación

---

## Propósito

Cuando el docente quiere actualizar filminas del año anterior en lugar de crear desde cero, este task implementa el análisis comparativo entre las filminas existentes (`--base`) y el nuevo `topic-extract.md` aprobado.

---

## Paso 1: Lectura de filminas previas

```
ruta_base = state.base_filminas_previas  # del .pipeline-v3-state.yaml
SI ruta_base es relativa → resolver relativa a {topic_folder}
SI el archivo NO existe → error inmediato:
  "❌ ERROR: --base especificado pero el archivo no existe: {ruta_base}"
  "Verificá la ruta y reinvocá el pipeline."

leer filminas_previas.md → extraer:
  - Lista de filminas (por número/título)
  - Conceptos mencionados en cada filmina (análisis de contenido)
  - Bibliografía citada (si la hay)
```

---

## Paso 2: Análisis comparativo

Para cada filmina previa, comparar contra `topic-extract.md ## conceptos-clave`:

**Categorías de acción:**

| Categoría | Criterio | Acción para class-writer |
|-----------|----------|--------------------------|
| `conservar` | Los conceptos de la filmina coinciden con el topic-extract.md y la bibliografía sigue vigente | Usar la filmina actual sin cambios |
| `actualizar` | Los conceptos son relevantes pero la bibliografía cambió o el topic-extract.md agrega profundidad | Conservar estructura, actualizar contenido |
| `eliminar` | La filmina cubre un concepto que ya no está en topic-extract.md o su solapamiento la hace redundante | No incluir en el nuevo conjunto |
| `nueva` | topic-extract.md identificó conceptos no cubiertos por ninguna filmina previa | Crear filmina nueva |

**Reglas de clasificación:**
- Un concepto de filmina previa que aparece en `## superposiciones-detectadas` con estrategia `asumir-conocido` → filmina clasificada como `eliminar` (ya no es necesaria)
- Un concepto con fuente bibliográfica desactualizada (libro > 5 años) y tendencia conflictiva en `## tendencias` → filmina clasificada como `actualizar`
- Filminas sin conceptos en topic-extract.md → `eliminar`

---

## Paso 3: Reporte de renovación

Presentar al docente el análisis antes de CP2:

```
🔄 Reporte de Renovación — Análisis vs. Año Anterior
======================================================

Base: {ruta_base}
Filminas previas analizadas: {N}

📊 Resumen:
  ✅ Conservar sin cambios:  {n} filminas
  🔄 Actualizar contenido:   {n} filminas
  ❌ Eliminar:               {n} filminas
  ✨ Nuevas (de topic-extract): {n} filminas

Detalle:

| # | Título filmina previa | Acción | Motivo |
|---|----------------------|--------|--------|
| 1 | Introducción a lambdas | conservar | Conceptos vigentes en SICP |
| 2 | Listas en Haskell | actualizar | topic-extract.md agrega §3.4 de SICP |
| 3 | Imperativo vs funcional | eliminar | Cubierto en Tema 02 (superposición alta) |
| — | Mónadas (nueva) | nueva | Identificada en topic-extract.md, N3 |

¿Confirmás estas acciones o querés ajustar? (Enter para confirmar, o indicá cambios)
```

---

## Paso 4: Integración con Paso 2 del workflow

El análisis de renovación se incluye en el plan de generación del Paso 2:

```markdown
## Plan de Filminas (con renovación)

| # | Título | Conceptos | Nivel | Acción |
|---|--------|-----------|-------|--------|
| 1 | {titulo} | {conceptos} | N{nivel} | conservar |
| 2 | {titulo} | {conceptos} | N{nivel} | actualizar |
| 3 | {titulo} | {conceptos} | N{nivel} | nueva |
```

El CP2 incluye la columna `Acción` para que el docente vea y modifique.

---

## Integración con class-writer (v3)

Cuando `filminas-base-acciones.yaml` está presente (generado en Paso 2), class-writer en modo v3:
- `conservar` → copiar filmina previa sin modificación
- `actualizar` → usar filmina previa como base, aplicar cambios según topic-extract.md
- `nueva` → generar desde cero con topic-extract.md

**Archivo generado por el workflow:** `{topic_folder}/filminas-base-acciones.yaml`

```yaml
# Generado en Paso 2 cuando --base fue especificado
base_filminas_previas: "temas/04-oo/filminas.md"
acciones:
  - numero: 1
    titulo: "Introducción a lambdas"
    accion: "conservar"
    filmina_previa_ref: "filmina-1"
  - numero: 2
    titulo: "Composición de funciones"
    accion: "actualizar"
    filmina_previa_ref: "filmina-3"
    motivo: "Agregar ejemplos de SICP §1.3 (p. 58-62)"
  - numero: 3
    titulo: "Mónadas"
    accion: "nueva"
    filmina_previa_ref: null
```

---

## Caso especial: Solo generación parcial

Si el docente quiere generar solo las filminas `actualizar` + `nueva` (sin tocar las `conservar`):
- Informar: "Solo se generarán {n} filminas (actualizar + nueva). Las filminas 'conservar' se copian tal cual."
- class-writer aplica la misma lógica.
