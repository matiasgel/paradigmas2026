# FIX.md - Plan de Reparacion EDU Standalone

## Contexto
Este documento define las correcciones necesarias para alinear el modulo EDU (`salida/edu-standalone`) en consistencia operacional, trazabilidad y ejecutabilidad por agentes BMAD.

Fecha: 2026-03-09
Origen: auditoria estructural de agentes, prompts, workflows y catalogo (`_edu/module-help.csv`).

## Objetivo
Corregir inconsistencias que hoy pueden romper ejecucion de comandos, enrutamiento de menu, parseo de prompts y flujos Git.

## Alcance
- Incluir SOLO cambios dentro de `salida/edu-standalone`.
- NO modificar `_bmad` global ni otras salidas de modulos.
- Preservar comportamiento funcional previsto del pipeline EDU.

## Hallazgos A Reparar (prioridad)

### P0 - Criticos
1. Menu handlers en agentes con soporte parcial de comandos:
- Varios agentes solo definen handler `exec`, pero tienen items sin `exec` (`MH`, `CH`, `DA`, `ST`) sin accion declarada.
- Riesgo: comandos no ejecutables o comportamiento indefinido.

2. Uso de `git pushall` en workflows:
- `git pushall` no es comando Git estandar.
- Riesgo: fallo en cierre de tema/cursada si no existe alias local.

### P1 - Importantes
3. Desalineacion entre catalogo y prompts:
- `module-help.csv` tiene 35 comandos.
- `.github/prompts` tiene 36 prompts.
- `edu-debate-topic` existe como prompt+workflow pero no esta en `module-help.csv`.
- Riesgo: comando fuera de ayuda/ruteo basado en catalogo.

4. Inconsistencia de formato en prompt files:
- Mezcla de archivos con frontmatter directo y otros envueltos en bloque ```prompt.
- Riesgo: parseo inconsistente segun runtime.

5. Variables no definidas en task de ayuda:
- `help.md` usa `{edu_output}` y `{edu_memory}`, pero en `config.yaml` existen `output_folder`, `course_output_folder`, `memory_folder`.
- Riesgo: resolucion ambigua de rutas.

### P2 - Mejora de coherencia
6. Ruta de output de ingestion:
- Workflow de materiales usa `salida/ingestado/`, mientras el modulo converge en `salida/cursadas` + `_edu-memory`.
- No bloquea, pero rompe convencion de estructura.

## Archivos Objetivo
- `salida/edu-standalone/_edu/agents/course-planner.md`
- `salida/edu-standalone/_edu/agents/topic-designer.md`
- `salida/edu-standalone/_edu/agents/student-simulator.md`
- `salida/edu-standalone/_edu/agents/class-writer.md`
- `salida/edu-standalone/_edu/agents/tp-designer.md`
- `salida/edu-standalone/_edu/agents/curriculum-reviewer.md`
- `salida/edu-standalone/_edu/agents/academic-researcher.md`
- `salida/edu-standalone/_edu/workflows/topic-cycle/workflow.md`
- `salida/edu-standalone/_edu/workflows/close-course/workflow.md`
- `salida/edu-standalone/_edu/module-help.csv`
- `salida/edu-standalone/_edu/tasks/help.md`
- `salida/edu-standalone/_edu/workflows/build-course-from-materials/workflow.md`
- `salida/edu-standalone/.github/prompts/*.prompt.md`
- `salida/edu-standalone/README.md`

## Requisitos de Implementacion

### R1. Normalizar manejo de menu en agentes
Para cada agente con menu:
- Mantener `exec` para items que cargan workflows.
- Agregar manejo explicito para items sin `exec`:
  - `MH`: re-mostrar menu.
  - `CH`: modo chat contextual.
  - `DA`: salir del agente.
  - `ST` (si aplica): resolver via accion/task definida o remover del menu si no se implementa.
- Alternativa valida: usar `handler type="action"` y declarar `action="..."` en items sin `exec`.

### R2. Reemplazar `git pushall`
En workflows:
- Reemplazar `git pushall` por secuencia portable:
  - `git push origin main`
  - `git push origin production`
- Si `production` puede no existir, documentar condicion o fallback.

### R3. Unificar catalogo de comandos
- Agregar entrada de `edu-debate-topic` a `module-help.csv` con fase, secuencia, agente y workflow correctos.
- Verificar que cantidad de comandos catalogados == cantidad de prompts activos (o documentar excepciones explicitas).

### R4. Estandarizar formato de prompts
Elegir una convencion y aplicarla en todos los prompt files:
- Opcion A (recomendada): frontmatter YAML directo (sin fences).
- Opcion B: bloque fenced uniforme para todos.

### R5. Corregir variables en task de ayuda
En `help.md`:
- Reemplazar referencias a `{edu_output}` / `{edu_memory}` por variables reales del config o definir mapeo explicito:
  - `{edu_output} := {course_output_folder}`
  - `{edu_memory} := {memory_folder}`
- Mantener reglas de deteccion de fase coherentes con rutas reales.

### R6. Alinear output de ingestion
En `build-course-from-materials/workflow.md`:
- Ajustar salida de ingestion para no romper convencion del modulo.
- Ejemplo aceptable: `salida/cursadas/_ingestado/` o ruta definida por variable de config.

## Criterios de Aceptacion
1. Ningun comando de menu queda sin ruta de ejecucion definida.
2. No quedan referencias a `git pushall` en `_edu/workflows`.
3. `edu-debate-topic` aparece en `module-help.csv` o se elimina formalmente de prompts/README.
4. Todos los prompts usan el mismo formato.
5. `help.md` no usa variables indefinidas.
6. README y `module-help.csv` quedan sincronizados en conteo y lista de comandos.

## Validacion Minima (post-fix)
1. Buscar pendientes:
- Sin `git pushall`.
- Sin `{edu_output}` y `{edu_memory}` sin mapping.
2. Verificar conteo:
- prompts `.prompt.md` vs filas de `module-help.csv`.
3. Smoke check documental:
- Cada comando `/edu-*` en README existe en prompts y viceversa.
4. Revisar que no se introduzcan cambios fuera de `salida/edu-standalone`.

## Entregables
- Archivos corregidos en `salida/edu-standalone`.
- Resumen de cambios por archivo.
- Lista de checks de validacion ejecutados y resultado.
