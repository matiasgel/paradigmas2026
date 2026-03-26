# Template de clase EDU

Este archivo define el marco estructural general de `minuta.md` y `filminas.md`.

## minuta.md

- Debe seguir la estructura aprobada en `diseno.md`.
- Debe ser proporcional a la duración de clase.
- Debe mantener coherencia total con `filminas.md`.

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