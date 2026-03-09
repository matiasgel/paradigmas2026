# Workflow: Quality Loops

**Module:** edu
**Phase:** 3 — Producción de Temas
**Agents:** writing-validator, writing-fixer, coherence-fixer, reference-validator, academic-guardrail

---

## Overview

Cadena secuencial de 4 loops de calidad que se ejecutan DESPUÉS de crear la clase y el TP.

## Loop Sequence

### Loop 1a: Validate Writing
- **Agent:** writing-validator
- **Input:** All topic documents (diseno.md, minuta.md, filminas.md, tp.md)
- **Output:** `writing-report.md` with classified issues [CRITICAL], [ERROR], [IMPROVEMENT]

### Loop 1b: Fix Writing
- **Agent:** writing-fixer
- **Auto-fix:** [CRITICAL] and [ERROR]
- **Confirm:** [IMPROVEMENT] requires professor approval
- **Output:** Git commits: `[writing-fixer] {ID}: {description}`

### Loop 2a: Validate Coherence
- **Agent:** coherence-fixer (detect mode)
- **Prerequisite:** Loop 1 completed
- **Input:** All topic documents
- **Output:** `coherence-report.md`

### Loop 2b: Fix Coherence
- **Agent:** coherence-fixer (fix mode)
- **Output:** Git commits: `[coherence-fixer] {ID}: {description}`

### Loop 3: Validate References
- **Agent:** reference-validator
- **Sources:** CrossRef, Semantic Scholar, arXiv, OpenLibrary
- **Output:** `references-report.md`
- **Manual:** Professor decides on flagged references

### Guardrail: Scope & Density
- **Agent:** academic-guardrail
- **Prerequisite:** Loops 1-3 completed
- **Checks:** Informal language, scope deviation, cognitive density
- **Output:** `scope-report.md`, `density-report.md`
- **Auto-fix:** Only if `academic_guardrail_enabled: true`

