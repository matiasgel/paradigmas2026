# Workflow Specification: quality-loops

**Module:** edu
**Categoría:** Core — camino feliz crítico
**Prioridad de implementación:** 3
**Status:** Placeholder — Pendiente de implementación
**Created:** 2026-03-06

---

## Workflow Overview

**Goal:** Ejecutar los 3 loops de calidad + guardrail sobre los documentos de un tema, en secuencia obligatoria pero invocables independientemente.

**Description:** Protocolo de calidad secuencial con 4 capas: Loop 1 (escritura), Loop 2 (coherencia), Loop 3 (referencias), Guardrail (formalidad + scope + densidad). Cada loop es invocable independientemente. El orden de precedencia es obligatorio — no se puede correr Loop 3 sin haber pasado Loop 1 y 2. El tema no puede cerrarse hasta que todos los loops estén resueltos.

**Workflow Type:** Create-only — produce documentos de revisión y aplica correcciones

---

## Workflow Structure

### Entry Point

```yaml
---
name: quality-loops
description: "Loops de calidad secuenciales: escritura → coherencia → referencias → guardrail"
web_bundle: true
installed_path: '{project-root}/_edu/workflows/quality-loops'
entryCommands:
  - /edu-validate-writing
  - /edu-validate-coherence
  - /edu-validate-references
  - /edu-validate-scope
  - /edu-validate-density
---
```

### Mode

- [x] Create-only (steps-c/)

---

## Planned Steps

| Step | Nombre | Goal | Agente |
|------|--------|------|--------|
| step-01a | writing-validate | Detectar errores de escritura | `writing-validator` |
| step-01b | writing-fix | Aplicar correcciones de escritura | `writing-fixer` |
| step-02 | coherence-fix | Detectar y reparar rupturas de coherencia | `coherence-fixer` |
| step-03 | reference-validate | Verificar estado de todas las referencias | `reference-validator` |
| step-04 | guardrail | Formalidad + scope + densidad cognitiva | `academic-guardrail` |

---

## Protocolo de precedencia

```
Loop 1: writing-validator → writing-fixer
         ↓ (bloqueante)
Loop 2: coherence-fixer
         ↓ (bloqueante)
Loop 3: reference-validator
         ↓ (bloqueante)
Guardrail: academic-guardrail (validate-scope + validate-density)
```

Cada loop puede reabrirse independientemente si el docente cambia el scope del tema.

---

## Workflow Inputs

### Required Inputs

- `{N}` — número de tema

### Optional Inputs

- `{loop}` — loop específico a ejecutar (1, 2, 3, guardrail). Si omitido, sugerencia de próximo loop pendiente.

---

## Workflow Outputs

### Output Format

- [x] Document-producing

### Output Files

```
temas/NN-nombre/
  revisión-escritura.md
  revisión-coherencia.md
  referencias-estado.md
  revisión-guardrail.md
```

Cada corrección automática aplicada genera un commit Git con mensaje estandarizado.

---

## Agent Integration

### Primary Agent

`writing-validator` + `writing-fixer` (Loop 1) → `coherence-fixer` (Loop 2) → `reference-validator` (Loop 3) → `academic-guardrail` (Guardrail)

### Other Agents

`academic-researcher` (Carlos) — invocado por `reference-validator` para buscar fuentes alternativas
`course-planner` (Elena) — recibe estado de cada loop y bloquea cierre si hay pendientes

### MCP Tools Required

- git — commit automático por cada corrección aplicada
- herramienta de búsqueda web — lista blanca académica para Loop 3

---

## Notas de implementación

- El cierre de tema (`/edu-close-topic`) verifica que todos los loops estén en estado `resuelto`
- `/edu-fix-writing-auto` crea commit automáticamente — el docente puede hacer `git revert`
- Las mejoras `[MEJORA]` en Loop 1 requieren confirmación del docente antes de aplicarse

---

_Spec creada: 2026-03-06_
