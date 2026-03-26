# Template de clase EDU

Este archivo define el marco estructural general de `minuta.md` y `filminas.md`.

## minuta.md

La minuta es el **guion de clase del docente**: autocontenida, usable slide a slide sin abrir otros archivos.

- Debe seguir la estructura aprobada en `diseno.md`.
- Debe ser proporcional a la duración de clase.
- Debe mantener coherencia total con `filminas.md`.
- **Es per-filmina:** cada `[F-XX]` de `filminas.md` tiene una sección correspondiente en la minuta.

### Estructura canónica de minuta.md

```
# Clase: [Nombre del Tema]
**Materia:** {project_name} | **Fecha:** | **Duración:** X min

## Objetivos
[objetivos de diseno.md]

---

### [F-01] Título de la filmina
**Tiempo:** X min
**Qué decir:** [guion del docente — 3-5 bullets con qué explica, cómo introduce y qué ejemplo usa]
**Conceptos clave:** [1-3 conceptos que el alumno DEBE retener de esta slide]
**Preguntas anticipadas:** [qué preguntas suelen surgir en este punto]
**Transición:** [cómo se conecta con F-02]

### [F-02] ...
...

---

## Cierre (2-3 min)
**Resumen:** [2-3 puntos clave de toda la clase]
**Anuncio del TP:** [tipo y fecha]
**Próxima clase:** [tema siguiente del plan-borrador.md]
```

El orden de secciones en `minuta.md` espeja exactamente el orden de filminas en `filminas.md`.

## filminas.md

El contrato canónico de filminas se define en dos niveles:

**Autoría** (estructura del Markdown fuente):
- `_edu/templates/filminas-template.md` — formato y directivas para `filminas.md`
- `_edu/templates/filminas-schema.yaml` — marcadores, directivas y enum de tipos

**Validación y pipeline** (plan JSON + schemas):
- `_edu/schemas/schema-registry.json` — fuente de verdad para tipos, layouts e imágenes
- `_edu/schemas/plan-filminas.schema.json` — contrato del plan JSON generado
- `_edu/schemas/filmina-slide.schema.json` — contrato por filmina individual

Objetivo:

- que el escritor de clase, el generador de plan y el publicador lean la misma estructura,
- que no haya ambigüedad entre título, subtítulo, bullets, tablas, código y hints visuales,
- que el pipeline valide contra JSON Schema antes de publicar.