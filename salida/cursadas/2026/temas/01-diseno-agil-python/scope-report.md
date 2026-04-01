# Reporte Guardrail — Scope + Density
## Tema 01: Módulo I — Diseño Ágil + Python
**Agente:** academic-guardrail 🛡️  
**Fecha:** 2026-04-01  
**`academic_guardrail_enabled`:** true  
**Prerrequisito:** Loops 1, 2, 3 completados ✅

---

## 1. Verificación de Scope (Alcance)

### Criterio: El contenido se ajusta al plan mínimo institucional

| Tópico plan-minimo.md (Módulo I) | Presente en documentos | Estado |
|----------------------------------|------------------------|--------|
| El Modelo Ágil para construcción de aplicaciones | T1-A, guia Part 1 | ✅ |
| Herramientas de desarrollo ágil (VS Code, Git, CI) | T1-A, guia Part 1.3 | ✅ |
| Entornos de desarrollo integrado (IDE) | T1-A, guia sección devcontainer | ✅ |
| Código autodocumentado + herramientas de extracción | T1-D + T2-C, guia Parts 7-8 | ✅ |
| Construcción de aplicaciones en entornos integrados | P1-A/P1-B/P2-A, guia Parts 4-6 | ✅ |
| Lenguajes dinámicos para desarrollo de aplicaciones | T1-B/T1-C, guia Parts 2-4 | ✅ |
| Introducción a Python (sintaxis, tipos, funciones, colecciones) | T1-B + T1-C + T2-A, guia Parts 2-6 | ✅ |

**Resultado:** ✅ Scope 100% alineado con plan mínimo institucional.

### Verificación de scope negativo (out-of-scope)

No se detectó contenido fuera del scope del Módulo I:
- No hay menciones a clases/OOP (Módulo III) ✅
- No hay profundización en pytest/TDD (Módulo II) ✅
- No hay async/await ni concurrencia (fuera de scope) ✅
- `@functools.wraps` y decoradores se introducen como *concepto*, no como habilidad evaluada ✅

---

## 2. Verificación de Formalidad de Lenguaje

### guia-estudio.md

| Aspecto | Evaluación |
|---------|-----------|
| Registro lingüístico | Apropiado: informal-académico ("podés", "tenés") — coherente con estilo universitario rioplatense |
| Ausencia de jerga coloquial inapropiada | ✅ Sin expresiones fuera de registro |
| Claridad del lenguaje para alumno de 1er/2do año | ✅ Accesible, sin presuponer conocimientos previos no declarados |
| Notas pedagógicas internas expuestas al alumno | ✅ Ninguna — corregidas en Loop 1 |

### minuta.md

| Aspecto | Evaluación |
|---------|-----------|
| Registro docente | ✅ Apropiado: directivo, con instrucciones claras para el docente |
| Lenguaje técnico correcto | ✅ Todos los términos técnicos usados correctamente |
| Secciones "Notas docentes" bien separadas | ✅ Claras y delimitadas |

---

## 3. Verificación de Densidad Cognitiva

Se aplica el perfil `student-guide` para guia-estudio.md (umbrales más permisivos que minuta).

### guia-estudio.md

| Métrica | Valor | Umbral student-guide | Estado |
|---------|-------|----------------------|--------|
| Partes temáticas | 10 | máx 12 | ✅ |
| Nuevos conceptos por sección | ~5 promedio | máx 8 | ✅ |
| Ejemplos de código por concepto | ≥1 por concepto | mín 1 | ✅ |
| Preguntas de autoevaluación | 13 (3 niveles) | mín 8 | ✅ |
| Glosario | 18 términos | mín 10 | ✅ |
| Referencias académicas | 4 papers + 6 URLs oficiales | mín 3 papers | ✅ |

**Densidad cognitiva:** APROPIADA para una guía de estudio de módulo intro a Python universitario.

### minuta.md

| Métrica | Valor | Umbral profesor-teorico | Estado |
|---------|-------|------------------------|--------|
| Sesiones planificadas | 4 (T1, P1, T2, P2) | = sesiones en topic.yaml | ✅ |
| Bloques por sesión | 4 cada sesión | = topic.yaml | ✅ |
| Minutos totales planificados | 140+160+140+160 = ~600 min + transiciones | ≤ 720 min constraint | ✅ |
| Código de referencia docente | Incluido en P1-A/P1-B | recomendado | ✅ |

---

## 4. Resultado Final Guardrail

| Check | Resultado |
|-------|-----------|
| Scope alineado con plan mínimo | ✅ PASS |
| Sin contenido out-of-scope | ✅ PASS |
| Formalidad de lenguaje apropiada | ✅ PASS |
| Densidad cognitiva dentro de umbrales | ✅ PASS |
| Notas internas de agentes eliminadas de guia alumno | ✅ PASS (corregido Loop 1) |

**GUARDRAIL STATUS: ✅ APROBADO — Sin bloqueos ni fixes automáticos requeridos.**

---

## 5. Post-Quality: Registro en Memoria Colectiva

Se registraron los siguientes hallazgos críticos en `_edu-memory/memory.db`:

```
[REGISTRADO] agent-error: "Escrita por" con nombre de agente en guia-estudio.md
  → course: leng-2026, topic: 01, agent: study-guide-writer
  → Patrón: header de documento expone identidad interna del agente
  → Fix: reemplazar por atribución institucional del docente

[REGISTRADO] quality-finding: Comentario de código inconsistente con código (sorted)
  → course: leng-2026, topic: 01, agent: study-guide-writer
  → Patrón: comentario describe resultado de reverse=True pero código usa sort ascendente

[REGISTRADO] quality-finding: Concordancia número/género en adjetivo ("importante→importantes")
  → course: leng-2026, topic: 01, agent: study-guide-writer
  
[REGISTRADO] quality-finding: Pipe literal en celda de tabla Markdown (X | None fragmenta tabla)
  → course: leng-2026, topic: 01, agent: class-writer
  → Fix: escapar con \| o usar backticks
```

---

_Loops de calidad 1–3 + Guardrail completados. Estado final: ✅ TODOS LOS DOCUMENTOS APROBADOS._
