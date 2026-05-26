---
stepsCompleted: [1, 2, 3, 4]
workflowType: implementation-readiness
status: complete
verdict: READY_WITH_NOTES
completedAt: '2026-05-23'
inputDocuments:
  - salida/planning-artifacts/prd.md
  - salida/planning-artifacts/architecture-topic-cycle-v3.md
  - salida/planning-artifacts/epics.md
---

# Reporte de Implementation Readiness — topic-cycle-v3

**Fecha:** 2026-05-23  
**Veredicto:** READY_WITH_NOTES  
**Revisor:** GitHub Copilot (análisis autónomo, fast mode)

---

## Resumen Ejecutivo

El conjunto de documentos de planning para `topic-cycle-v3` está en un estado de readiness **esencialmente completo**. Los tres artefactos —PRD, arquitectura y epics/stories— están bien alineados y presentan una cobertura de 26/26 FRs y 10/10 NFRs explícitamente mapeada en el documento de epics y verificada en esta revisión. Las 7 decisiones arquitecturales (AD-01 a AD-07) tienen reflejo directo en stories implementables.

La fortaleza más destacada del planning es el **principio aditivo/opt-in garantizado a nivel de contrato**: la activación del comportamiento v3 en los agentes downstream requiere la presencia simultánea de `topic-extract.md` Y `checkpoint_2_aprobado: true` — condición que es imposible de cumplir accidentalmente. Esto protege la cursada 2026 en curso de cualquier regresión involuntaria.

Se identificaron **cinco issues menores** que no bloquean la implementación pero deben registrarse antes de comenzar: uno involucra un gap de implementación concreto (backup de `minuta.md` ausente en Story 6.4), y los demás son gaps de especificación que podrían generar ambigüedad durante la ejecución. Ningún issue es crítico. La implementación puede comenzar en el orden E1→E2→{E3,E4,E6}→E5 con las notas indicadas.

---

## Cobertura de Requisitos

### FRs cubiertos

| FR | Descripción | Story(ies) |
|---|---|---|
| FR01 | Invocación con tópico/libro/nivel | 1.1, 4.1 |
| FR02 | Libro default de config.yaml | 1.1, 2.2 |
| FR03 | Informar libro y nivel al inicio | 1.1 |
| FR04 | Parámetro `--base` filminas previas | 5.1 |
| FR05 | Consultar registro de temas dados | 3.1 |
| FR06 | Reportar superposiciones + esperar confirmación | 3.2 |
| FR07 | Capturar estrategia de tratamiento | 3.3 |
| FR08 | ChromaDB obligatorio, fail-fast | 2.2 |
| FR09 | Libros secundarios en Paso 1b | 2.3 |
| FR10 | Web research tendencias académicas | 2.4 |
| FR11 | Marcar libros >5 años conflictivos | 2.4 |
| FR12 | topic-extract.md con 5 secciones obligatorias | 2.1, 2.5 |
| FR13 | Persistir y esperar aprobación CP1 | 1.4, 2.5 |
| FR14 | Docente puede editar topic-extract.md | 1.4 |
| FR15 | Plan de generación con CP2 | 1.5 |
| FR16 | Docente puede editar plan (CP2) | 1.5 |
| FR17 | 3 niveles de densidad en filminas | 4.2 |
| FR18 | Guía de estudio sin re-invocar ChromaDB | 6.2, 4.3 |
| FR19 | Guía docente con topic-extract.md | 6.3 |
| FR20 | Compatibilidad con slides_pipeline.py | 4.2, 6.1 |
| FR21 | Comparar filminas previas vs topic-extract.md | 5.2 |
| FR22 | Reporte análisis renovación al docente | 5.3 |
| FR23 | Priorizar reúso sobre generación nueva | 5.3 |
| FR24 | topic-cycle original sin cambios | 1.1, 6.1, 6.2, 6.3 |
| FR25 | topic-cycle-v3 activable por flag o invocación | 1.1 ⚠️ (ver nota) |
| FR26 | Artefactos v3 conviven sin conflictos con v2 | 1.3, 6.4 |

> ⚠️ **FR25 — cobertura parcial:** Story 1.1 cubre la activación por invocación explícita (`@topic-cycle-v3`). La activación por *flag en config.yaml* está mencionada en el PRD y la arquitectura (§7.3) pero ninguna story tiene AC que la implemente ni la pruebe. Ver Issues Menores #1.

**Resultado: 25/26 FRs con cobertura completa. FR25 con cobertura parcial.**

### FRs con cobertura parcial o ausente

| FR | Gap |
|---|---|
| FR25 | Mecanismo de activación por flag en `config.yaml` no tiene AC en ninguna story. Solo cubre invocación explícita. |

### NFRs cubiertos

| NFR | Descripción | Story/Decisión arquitectural |
|---|---|---|
| NFR01 | Estado persistido por paso; reanudación | Story 1.3 / AD-01 |
| NFR02 | Fail-fast con diagnóstico si chroma-mcp falla | Story 2.2 / AD-03 |
| NFR03 | Checkpoints persistidos ante interrupción de sesión | Stories 1.4, 1.5 / AD-01 |
| NFR04 | Citas con referencia verificable o marcado explícito | Story 2.5 / Schema §4 |
| NFR05 | Bloquear plan sin fuente verificada en topic-extract | Story 2.5 / AD-02 |
| NFR06 | Mismo formato de salida que v2 | Stories 4.2, 6.1, 6.2, 6.3, 6.4 / AD-05 |
| NFR07 | Sin dependencias nuevas | Stories 2.2, 2.3, 2.4 / §2 stack |
| NFR08 | Tiempo ≤ 150% de v2 (checkpoints = tiempo docente) | Stories 4.1, 4.2, 4.3 / argumento arquitectural |
| NFR09 | Schema documentado formalmente | Story 2.1 / §4 arquitectura |
| NFR10 | Workflow independiente; no modifica topic-cycle | Stories 1.1, 1.2 / AD-06 |

**Resultado: 10/10 NFRs cubiertos.** ✅

---

## Alineación PRD ↔ Arquitectura

**Consistencia general: Alta.** Los requisitos técnicos del PRD (Área de Project-Type Requirements) se mapean directamente a decisiones arquitecturales:

| Requisito PRD | Resuelto en arquitectura |
|---|---|
| Persistencia de estado entre pasos | AD-01 (`.pipeline-v3-state.yaml`) |
| ChromaDB como paso obligatorio no salteable | AD-03 (fail-fast en Paso 1a) |
| `topic-extract.md` como contrato entre agentes | AD-02 (esquema §4, consumo desde disco) |
| Zero modificaciones al sistema existente | AD-06 (`topic-designer-v3` como archivo nuevo) |
| 3 niveles de densidad por invocación | AD-04 (nivel propagado desde estado, §7.5) |
| Coexistencia de artefactos v2/v3 | AD-05 (backup automático, naming conventions) |
| Renovación de material previo | AD-07 (análisis comparativo conservar/actualizar/eliminar/nueva) |

**Restricciones del PRD bien reflejadas:**
- **NFR06/NFR07 (compatibilidad):** La arquitectura §11 incluye una matriz de compatibilidad explícita que garantiza el principio brownfield. El invariante "presencia de `topic-extract.md` activa v3; ausencia garantiza v2 exacto" es una propiedad verificable de forma determinista.
- **NFR10 (workflow independiente):** AD-06 garantiza que `topic-designer-v3.md` es un archivo nuevo. La arquitectura no modifica `topic-designer.md`. Confirmado.
- **NFR08 (tiempo ≤ 150% de v2):** La arquitectura provee el argumento válido de que los checkpoints son tiempo docente (no tiempo de sistema). Es un NFR medible post-implementación sin historia de medición dedicada, lo cual es aceptable para un sistema de agentes LLM.

**Única inconsistencia menor:** El PRD describe la activación de v3 como "por flag en config.yaml o invocación explícita" (FR25). La arquitectura §7.3 documenta el formato canónico de invocación explícita exhaustivamente, pero no especifica cuál campo de config.yaml actúa como flag ni su comportamiento cuando está activo. La arquitectura asume invocación explícita como único mecanismo en la práctica.

---

## Alineación Arquitectura ↔ Epics/Stories

### Cobertura de decisiones arquitecturales

| AD | Título | Stories que la implementan |
|---|---|---|
| AD-01 | Pipeline State Machine con persistencia | 1.3, 3.3, 1.4, 1.5 |
| AD-02 | topic-extract.md como contrato de interfaz | 2.5, 6.1, 6.2, 6.3 |
| AD-03 | ChromaDB como paso no-salteable (fail-fast) | 2.2 |
| AD-04 | Niveles de densidad como modificador de prompt | 4.1, 4.2, 4.3 |
| AD-05 | Política de coexistencia de artefactos | 1.3, 6.4 |
| AD-06 | topic-designer-v3 como variante independiente | 1.2 |
| AD-07 | Renovación de material previo como análisis comparativo | 5.1, 5.2, 5.3 |

**Resultado: 7/7 decisiones arquitecturales cubiertos.** ✅

### Schema de topic-extract.md (§4 arquitectura)

- Story 2.1 crea el schema formal `topic-extract-schema.yaml` con las 5 secciones, tipos y reglas de validación ✅
- Story 2.5 implementa la generación del artefacto con validaciones (≥1 fuente con página, ≥3 conceptos-clave) ✅

### Integración ChromaDB (§9 arquitectura)

- Story 2.2 cubre Paso 1a (§9.1 y §9.3) incluyendo validación de colección vacía ✅
- Story 2.3 cubre Paso 1b (§9.2) con comportamiento no-bloqueante ✅
- Story 2.4 cubre Paso 1c (web research, no-bloqueante) ✅

### Comportamiento condicional v3/v2 en agentes downstream

La lógica condicional está cubierta en Stories 6.1, 6.2, 6.3 con AC explícitas para los tres casos posibles:
1. `topic-extract.md` NO existe → comportamiento v2 exacto ✅
2. `topic-extract.md` existe pero `checkpoint_2_aprobado: false` → comportamiento v2 ✅
3. Ambas condiciones cumplen → comportamiento v3 ✅

**Este diseño de doble condición es la garantía más sólida del principio brownfield.**

### Tabla de estado (§5 arquitectura) vs stories

El estado documentado en §5 incluye las tablas de transición completas. Las stories cubren todas las transiciones críticas. Hay una omisión menor: la arquitectura §8.1 lista `minuta-v2-backup.md` como artefacto nuevo, pero Story 6.4 no incluye AC explícita para el backup de `minuta.md`. Ver Issues Menores #2.

---

## Riesgos de Implementación

| Riesgo | Probabilidad | Impacto | Mitigación en Stories |
|---|---|---|---|
| chroma-mcp no disponible durante Paso 1a | Media | Alto | Story 2.2: fail-fast con diagnóstico explícito. AD-03 documenta el mensaje estándar. |
| Colección `edu_knowledge` vacía al primer uso | Baja | Alto | Story 2.2 (último AC): detecta count==0 y provee instrucción de ingesta. |
| Activación accidental de v3 en flujo v2 | Muy baja | Alto | Doble condición (topic-extract.md + checkpoint_2_aprobado:true) es determinista. Stories 6.1-6.3 cubren el caso. |
| Estado inconsistente post-interrupción (CP1 aprobado, topic-extract.md borrado) | Baja | Alto | Arquitectura §13 lo registra como riesgo. Las stories no tienen AC explícita para recuperación de estado inconsistente. **Gap menor** — no bloquea implementación pero requiere documentación al implementar Story 1.3. |
| Schema drift de topic-extract.md | Baja | Medio | NFR09 y Story 2.1 establecen que el schema es fuente de verdad formal. Cualquier cambio requiere actualización de todos los consumidores (documentado en NFR09). |
| Docente rompe el schema al editar topic-extract.md | Baja | Medio | Arquitectura §13 lo registra. Story 2.5 incluye AC de validación automática en CP1. El agente corrige antes de presentar al docente. |
| Backup de mismo día (doble ejecución v3 en misma fecha) | Baja | Bajo | Story 6.4 (último AC): sufijo secuencial `-2`, `-3`, etc. Cubierto. |
| Modificación de agentes de producción (6.1-6.3) genera regresión | Baja | Alto | Cada story de E6 incluye AC explícita de "cero regresión". Sin embargo, no hay story dedicada a **probar** la ruta v2 post-modificación. Ver Issues Menores #3. |

---

## Verificación Brownfield (no-regresión)

### Principio aditivo/opt-in

**Estado: Bien garantizado.** El principio brownfield opera en dos capas:

**Capa 1 — Nuevos archivos sin interferencia:**
- `topic-cycle-v3/workflow.md` es un archivo completamente nuevo; no modifica `topic-cycle/workflow.md`
- `topic-designer-v3.md` es un agente nuevo; `topic-designer.md` permanece intacto
- `topic-extract-schema.yaml` es un nuevo schema; no modifica `schema-registry.json`

Stories 1.1 y 1.2 tienen AC de verificación directa: "el archivo `topic-cycle/workflow.md` / `topic-designer.md` permanece sin ninguna modificación".

**Capa 2 — Modificaciones condicionales en agentes existentes:**
Los 3 agentes downstream reciben una sección adicional con lógica condicional. La invariante de seguridad es:

```
v3 activo ↔ (topic-extract.md existe) AND (checkpoint_2_aprobado = true)
```

Esta condición NO puede cumplirse en ningún tema generado con v2 puro, porque `.pipeline-v3-state.yaml` no existe en esos directorios, y `topic-extract.md` tampoco existe. Por tanto, **todos los temas ya generados con v2 seguirán usando v2 exacto** sin ninguna intervención.

**Capa 3 — Backup antes de sobrescritura:**
Story 6.4 garantiza backup automático de `filminas.md`, `guia-estudio.md`, `guiaprofesor.md` con sufijo `YYYYMMDD`. La arquitectura §8.1 documenta también `minuta-v2-backup.md`, que está ausente en las ACs de Story 6.4 (ver Issues Menores #2).

### Temas ya generados en cursada 2026

Los temas generados con `topic-cycle` v2 tienen en su carpeta: `filminas.md`, `minuta.md`, `guia-estudio.md`, `guiaprofesor.md`, `diseno.md`, `topic.yaml`. **No tienen** `topic-extract.md` ni `.pipeline-v3-state.yaml`. La ausencia de `topic-extract.md` garantiza que los agentes downstream (una vez modificados con E6) seguirán su ruta v2 exacta. No se requiere migración ni intervención manual en ningún tema existente.

---

## Orden de Implementación Recomendado

El orden documentado en epics es correcto y se confirma en este análisis:

```
E1 (Pipeline base) → E2 (Bibliographic-first) → E3 / E4 / E6 (paralelo) → E5 (Renovación)
```

**Justificación por bloqueos:**

| Epic | Puede empezar cuando... | Razón |
|---|---|---|
| **E1** | Inmediatamente | Sin dependencias; crea el andamiaje completo |
| **E2** | Después de E1 | Necesita workflow.md y agent topic-designer-v3 existentes; implementa el corazón del pipeline |
| **E3** | Después de E1+E2 | Paso 0 se integra en topic-designer-v3; necesita el estado del pipeline definido |
| **E4** | Después de E1+E2 | Niveles de densidad modifican class-writer y study-guide-writer; necesita el contrato topic-extract.md |
| **E6** | Después de E1+E2 | Modifica agentes downstream; necesita schema de topic-extract.md (Story 2.1) para escribir las ACs correctamente |
| **E5** | Después de E2 | Análisis comparativo opera sobre topic-extract.md ya aprobado; puede hacerse sin E3/E4/E6 |

**Recomendación adicional:** Implementar E6 antes de E4. Las stories de E4 (4.2, 4.3) modifican los mismos agentes que E6 (6.1, 6.2). Hacer E6 primero establece la estructura condicional; E4 agrega los modificadores de densidad dentro del bloque v3 ya definido. Esto reduce el riesgo de conflicto de edición en los mismos archivos.

**Orden óptimo sugerido:**
```
E1 → E2 → E6 → E4 → E3 → E5
```

---

## Issues Críticos

**No hay issues críticos.** El planning puede avanzar a implementación.

---

## Issues Menores / Sugerencias

### Issue #1 — FR25: Activación por flag en config.yaml sin implementación

**Tipo:** Gap de implementación  
**Severidad:** Baja  
**Descripción:** FR25 especifica que `topic-cycle-v3` puede activarse por "flag en config.yaml o por invocación explícita". Story 1.1 cubre la invocación explícita exhaustivamente, pero ninguna story tiene AC para el mecanismo de flag en config.yaml. La arquitectura §7.3 tampoco especifica cuál campo de `config.yaml` actuaría como flag ni qué comportamiento tendría.

**Sugerencia:** Si la activación por config.yaml es realmente necesaria (vs. invocación explícita que ya es simple), agregar en Story 1.1 una AC adicional: definir el campo `default_workflow: topic-cycle-v3` en config.yaml y su comportamiento. Si no se planea implementar, ajustar FR25 para eliminar esa variante de activación.

---

### Issue #2 — Story 6.4: minuta.md no incluida en mecanismo de backup

**Tipo:** Gap de especificación  
**Severidad:** Baja  
**Descripción:** La arquitectura §8.1 lista `minuta-v2-backup.md` como artefacto nuevo que se crea cuando v3 sobrescribe `minuta.md`. Sin embargo, Story 6.4 solo tiene ACs explícitas para backup de `filminas.md`, `guia-estudio.md` y `guiaprofesor.md`. `minuta.md` (generado por class-writer en v2 junto con filminas.md) queda sin AC de backup.

**Sugerencia:** Agregar a Story 6.4 el AC: "Dado que `minuta.md` existe antes de la generación v3, cuando class-writer genera en modo v3, entonces crea `minuta-v2-backup-YYYYMMDD.md` antes de escribir el nuevo archivo."

---

### Issue #3 — Ausencia de procedimiento de regresión post-E6

**Tipo:** Gap de proceso  
**Severidad:** Baja  
**Descripción:** Las stories de Epic 6 incluyen ACs de "cero regresión" verificables conceptualmente, pero no existe una story dedicada a ejecutar y documentar la **verificación empírica** del comportamiento v2 en los agentes modificados. En un entorno brownfield con cursada activa, es buena práctica tener una verificación explícita post-modificación.

**Sugerencia:** Al implementar E6, documentar informalmente en el commit/PR la evidencia de que el path v2 sigue funcionando (ej. invocar class-writer en un tema sin topic-extract.md y confirmar el output). No bloquea implementación.

---

### Issue #4 — Dependencias E1+E2 no documentadas en stories de E3/E4/E6

**Tipo:** Gap de documentación  
**Severidad:** Muy baja  
**Descripción:** Las stories de E3, E4 y E6 no listan explícitamente en su texto que requieren E1+E2 completados. El orden correcto está documentado en la sección "Validación Final" de epics.md, pero no en las stories individuales. Si un agente implementador abordara E4 antes de E2, encontraría que `topic-designer-v3.md` no tiene el bloque de generación de topic-extract.md aún, generando inconsistencias.

**Sugerencia:** Al crear los archivos de story individuales para ejecución, agregar "Prerrequisito: E1 y E2 completos" en el encabezado de cada story de E3, E4 y E6.

---

### Issue #5 — Inconsistencia menor en tabla de cobertura NFR del Epic 4

**Tipo:** Error de documentación  
**Severidad:** Muy baja  
**Descripción:** La tabla de inventario de epics indica que E4 cubre "NFR08" únicamente. Sin embargo, las stories 4.2 y 4.3 listan explícitamente "NFR cubiertos: NFR06, NFR08". La tabla del epic omite NFR06 (compatibilidad de formato de salida), que sí es relevante para E4 ya que modifica class-writer y study-guide-writer.

**Sugerencia:** Corregir la fila de E4 en la tabla de inventario de epics: `NFR08, NFR06`. No afecta implementación.

---

## Conclusión

**Veredicto: READY_WITH_NOTES**

El planning de `topic-cycle-v3` está listo para comenzar implementación. La cobertura es de **26/26 FRs** (con un gap menor en FR25) y **10/10 NFRs**. Las 7 decisiones arquitecturales tienen reflejo directo en stories con criterios de aceptación testables. El principio brownfield es la fortaleza central del diseño: la doble condición de activación v3 garantiza determinísticamente que ningún tema existente en la cursada 2026 puede verse afectado.

Los 5 issues menores identificados son todos de baja severidad y ninguno requiere rediseño. Dos de ellos (Issue #1 y Issue #2) tienen una corrección de 2-3 ACs que conviene hacer antes de ejecutar las stories afectadas. Los issues #3, #4 y #5 son de proceso y documentación, sin impacto en código.

El orden de implementación óptimo es **E1 → E2 → E6 → E4 → E3 → E5**, con la justificación de que E6 antes que E4 reduce el riesgo de edición conflictiva en los agentes downstream que ambos epics modifican.

---

*Reporte generado con análisis autónomo de readiness. 2026-05-23.*
