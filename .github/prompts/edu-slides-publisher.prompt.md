---
description: 'EDU: Publicar filminas → usar /edu-publish-slides (pipeline v3 schema-driven)'
agent: 'agent'
tools: ['read']
---

> **⚠️ Este prompt fue unificado en `/edu-publish-slides`.**
>
> Usa `/edu-publish-slides` para ejecutar el pipeline completo automático v3:
> - Lee `_edu/schemas/schema-registry.json` (OBLIGATORIO)
> - Genera `plan-filminas-{tema}.json` determinista desde `filminas.md`
> - Valida contra JSON Schema
> - Genera imágenes con Gemini
> - Publica en Google Slides
>
> Todo sin preguntas al usuario. Schema-driven.

Redirigir al usuario a `/edu-publish-slides`.

