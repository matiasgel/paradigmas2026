# falta.md — Elementos ausentes del esquema para Tema 02

> Generado automáticamente por Dr. Roberto (class-writer) al ejecutar `/edu-create-class`
> Fecha: 2026-03-19
> Tema: 02 — Sintaxis y Semántica de Lenguajes

---

## Archivos de esquema no encontrados

Los siguientes archivos fueron buscados según el workflow `topic-cycle/workflow.md` y **no existen**:

| Archivo buscado | Ruta esperada | Impacto |
|----------------|---------------|---------|
| `class-template.md` | `_edu/templates/class-template.md` | Sin constraint estructural formal para `minuta.md` — se usó tema 01 como referencia |
| `filminas-template.md` | `_edu/templates/filminas-template.md` | Sin constraint estructural formal para `filminas.md` — se usó `informefinal/archivos/filminas.md` como baseline |
| `filminas-schema.yaml` | `_edu/templates/filminas-schema.yaml` | Sin esquema formal de validación de filminas |

**Fuente de verdad usada como reemplazo:**
- `informefinal/archivos/filminas.md` (baseline de 40 slides para tema 02, generado el 2026-03-18) → adaptado con B5 rediseñado
- `informefinal/archivos/slides-config.yaml` → paleta, tipografía y layouts disponibles
- `salida/cursadas/2026/temas/01-conceptos-introductorios/minuta.md` → formato de referencia para minuta.md

---

## Gap: @layout: no usado en filminas

El archivo `_edu/slides-config.yaml` define los layouts disponibles:

```
portada, concepto-abstracto, codigo, tabla-comparativa,
pregunta-socrática, timeline, cierre, demo-herramienta
```

Las filminas producidas **no incluyen directivas `@layout:`** porque ningún archivo de referencia existente las usa (ni `informefinal/archivos/filminas.md` ni las filminas de tema 01). El pipeline `slides_pipeline.py` parece inferir el layout desde la estructura de contenido de cada slide.

**Acción recomendada:** si el pipeline requiere `@layout:` explícito, agregar una directiva al inicio del cuerpo de cada slide según la tabla:

| Tipo de filmina | @layout sugerido |
|----------------|-----------------|
| Portada | `portada` |
| Slide de definición/concepto | `concepto-abstracto` |
| Slide con código TypeScript | `codigo` |
| Slide con tabla comparativa | `tabla-comparativa` |
| Pregunta al aula / actividad | `pregunta-socrática` |
| Línea del tiempo | `timeline` |
| Cierre / mapa final | `cierre` |
| Demo de herramienta | `demo-herramienta` |

---

## topic.yaml creado en esta sesión

No existía `topic.yaml` para tema 02. Creado en esta sesión con `estado: "clase-generada"`.

---

## Artefactos pendientes (no generados en esta sesión)

| Artefacto | Comando | Descripción |
|-----------|---------|-------------|
| `guia-estudio.md` | `/edu-create-study-guide` | Guía completa para estudio autónomo del alumno |
| `tp.md` | `/edu-create-tp` | Trabajo práctico del tema |
| `slides/plan-filminas-02-sintaxis-semantica.yaml` | script `slides_pipeline.py` Fase 1 | Plan de filminas para exportación a Google Slides |
| `slides/assets/` | script `slides_pipeline.py` Fase 2 | Assets de imagen para slides con `@imagen:` |
