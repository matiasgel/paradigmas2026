---
stepsCompleted: ['step-01-init', 'step-02-discovery', 'step-02b-vision', 'step-02c-executive-summary', 'step-03-success', 'step-04-journeys', 'step-05-domain', 'step-06-innovation', 'step-07-project-type', 'step-08-scoping', 'step-09-functional', 'step-10-nonfunctional', 'step-11-polish', 'step-12-complete']
inputDocuments:
  - salida/planning-artifacts/product-brief-edu-pipeline-v3.md
  - salida/planning-artifacts/product-brief-edu-pipeline-v3-distillate.md
  - salida/planning-artifacts/sprints-mejoras-edu-v2.md
  - salida/planning-artifacts/arquitectura-pipeline-filminas-v4.md
workflowType: 'prd'
briefCount: 2
researchCount: 0
brainstormingCount: 0
projectDocsCount: 2
classification:
  projectType: "AI-Augmented Content Authoring System / Knowledge Production System"
  domain: "Education Technology (EdTech)"
  complexity: "Alta — complejidad cognitiva/lógica alta (coordinación LLMs, grounding bibliográfico, densidad pedagógica, artefactos intermedios); complejidad operacional/infraestructura baja (usuario único, sin multitenancy)"
  projectContext: "brownfield"
  brownfieldRisk: "Alto — 24 agentes y 16+ workflows en producción activa con clases en curso; principio aditivo/opt-in obligatorio; cualquier regresión tiene costo académico inmediato"
  strategicArtifact: "topic-extract.md — contrato de acoplamiento entre topic-designer y agentes downstream; nodo pivote hacia grafo de conocimiento a largo plazo"
  stakeholders:
    primary: "Matiasgel (docente) — único usuario directo, poder de veto sobre calidad"
    indirect: "Estudiantes — consumidores finales del material generado"
    normative: "Currícula institucional — restricción normativa sobre temas y nivel taxonómico (Bloom)"
---

# Product Requirements Document - paradigmas2026

**Author:** Matiasgel
**Date:** 2026-05-23

## Executive Summary

El módulo EDU de paradigmas2026 cuenta con un sistema maduro de 24 agentes y 16+ workflows que genera material docente completo para la materia "Paradigmas y Lenguajes de Programación". Este PRD especifica la refactorización del pipeline de producción de temas — los cuatro agentes centrales (`topic-designer`, `class-writer`, `study-guide-writer`, `create-teacher-guide`) — para resolver cinco fallos estructurales observados en la cursada 2026: generación sin checkpoints intermedios (propensa a timeouts y reinicios costosos), contenido desanclado de la bibliografía asignada, profundidad uniforme independiente del contexto pedagógico, ausencia de verificación curricular activa, y no reutilización del material del año anterior.

El producto de esta refactorización es `topic-cycle-v3`: un nuevo workflow opt-in que opera con un pipeline atómico de siete pasos, artefactos intermedios persistidos y puntos de control explícitos para el docente. El workflow existente `topic-cycle` permanece sin modificaciones.

**Usuario primario:** Matiasgel (docente) — único usuario directo con poder de veto sobre calidad del output.
**Beneficiarios indirectos:** Estudiantes (consumidores del material), currícula institucional (restricción normativa sobre temas y nivel taxonómico Bloom).

### What Makes This Special

**Grounding antes que generación.** El breakthrough no es generar más inteligentemente — es hacer el proceso visible y controlable. El artefacto intermedio `topic-extract.md` actúa como contrato validado de conocimiento: el docente lo revisa y corrige antes de que cualquier material de enseñanza sea generado. Los agentes downstream lo consumen del disco; no re-consultan ChromaDB.

**Bibliographic-first como señal primaria.** ChromaDB con los libros asignados de la materia es el primer input, no el último recurso. El LLM complementa contenido bibliográfico verificado en lugar de fabricar desde datos de entrenamiento. Esto garantiza coherencia terminológica entre el material generado y las lecturas obligatorias de los alumnos.

**Densidad como parámetro explícito.** El mismo tópico produce material de Nivel 1 (introductorio, primera exposición), Nivel 2 (estándar, desarrollo completo) o Nivel 3 (exhaustivo, sin asumir nada) según el momento de la cursada. Un único parámetro de invocación controla la profundidad global.

**Aditivo por diseño.** Zero riesgo de regresión: `topic-cycle-v3` coexiste con `topic-cycle` sin modificarlo. Con la cursada 2026 en curso, no hay presión de migración para temas ya generados.

**Visión a largo plazo:** `topic-extract.md` evoluciona de artefacto intermedio a nodo central del grafo de conocimiento de la materia, alimentando el tutor adaptativo, el generador de TPs y el simulador de estudiantes.

## Project Classification

| Campo | Valor |
|---|---|
| **Tipo** | AI-Augmented Content Authoring System / Knowledge Production System |
| **Dominio** | Education Technology — producción de material docente universitario |
| **Complejidad** | Alta (cognitiva/lógica) · Baja (operacional/infraestructura) |
| **Contexto** | Brownfield — riesgo de regresión alto; semester activo; principio aditivo/opt-in obligatorio |
| **Artefacto estratégico** | `topic-extract.md` — contrato de acoplamiento y nodo pivote hacia grafo de conocimiento |

---

## Success Criteria

### User Success

- **Sin interrupciones:** Un tema completo — desde invocación del workflow hasta guía docente final — se genera sin timeout ni reinicio manual en la misma sesión.
- **Checkpoints respetados:** El docente puede revisar y modificar el `topic-extract.md` y el plan de generación antes de que cualquier material de clase sea producido. El sistema espera aprobación explícita en cada checkpoint.
- **Anclaje bibliográfico visible:** El `topic-extract.md` cita explícitamente secciones y páginas del libro principal. El docente puede rastrear cada concepto clave a su fuente bibliográfica.
- **Coherencia curricular activa:** El agente detecta y reporta superposiciones con temas ya dados en la cursada 2026 antes de generar contenido.
- **Densidad diferenciada:** El mismo tópico produce output visiblemente distinto en Nivel 1, 2 y 3 — en extensión, profundidad de explicación y cantidad de ejemplos.
- **Reúso de material previo:** Cuando se proveen filminas del año anterior, al menos el 40% del contenido se reutiliza o adapta.

### Business / Academic Success

- Material generado es directamente correlacionable con las lecturas obligatorias de los alumnos sin post-edición manual para alinear terminología.
- El docente produce un tema completo en menos sesiones que con `topic-cycle` v2, sin pérdida de contenido por reinicio.
- Ningún workflow existente se ve afectado: todos los temas ya generados con `topic-cycle` siguen siendo accesibles y reproducibles.

### Technical Success

- `topic-cycle-v3` se activa por flag de configuración o invocación explícita — `topic-cycle` original funciona sin cambios.
- `topic-extract.md` sigue un esquema fijo con secciones obligatorias: `fuentes`, `conceptos-clave`, `ejemplos-bibliograficos`, `tendencias`, `superposiciones-detectadas`. Los agentes downstream pueden parsearlo de forma predecible.
- ChromaDB vía `chroma-mcp` es invocado como Paso 1a/1b obligatorio — no es salteable.
- Los 4 agentes refactorizados mantienen retrocompatibilidad de interfaz: mismos parámetros de entrada, salida en los mismos formatos destino.
- Zero regresiones en los 24 agentes y 16+ workflows existentes.

### Measurable Outcomes

| Métrica | Target v1 |
|---|---|
| Temas completados sin reinicio | ≥ 90% de las sesiones |
| `topic-extract.md` con citas bibliográficas explícitas | 100% de los temas generados con v3 |
| Diferencia de densidad Nivel 1 vs Nivel 3 (ratio de palabras) | ≥ 2x |
| Reúso de filminas del año anterior (cuando se proveen) | ≥ 40% conservado/adaptado |
| Regresiones en workflows existentes | 0 |
| Tiempo del docente en checkpoint de `topic-extract.md` | < 5 minutos por tema |

## Product Scope

### MVP — Minimum Viable Product

- Nuevo workflow `topic-cycle-v3` con pipeline de 7 pasos (Paso 0 a Paso 5)
- Refactorización de 4 agentes: `topic-designer`, `class-writer`, `study-guide-writer`, `create-teacher-guide`
- Artefacto intermedio `topic-extract.md` con esquema fijo y 2 checkpoints (post-extracción, post-plan)
- Integración ChromaDB vía `chroma-mcp` como paso obligatorio (Pasos 1a/1b)
- Web research de tendencias académicas (Paso 1c)
- Coherencia curricular (Paso 0) consultando temas previos de la cursada
- 3 niveles de densidad globales por invocación
- Soporte de filminas del año anterior como base opcional de renovación

### Growth Features (Post-MVP)

- Niveles de densidad por sección individual (no solo global)
- Generación automática de `topic-extract.md` para temas ya existentes en 2026
- Dashboard del docente con historial de temas y versiones de `topic-extract.md`
- Métricas de reúso de material previo por tema

### Vision (Futuro)

- `topic-extract.md` como nodo central del grafo de conocimiento de la materia
- Alimentación automática del tutor adaptativo, generador de TPs y simulador de estudiantes desde el grafo de conocimiento

---

## User Journeys

### Journey 1 — Generación de un tema nuevo (flujo principal)

**Matiasgel quiere preparar el material para el Tema 08: Programación Funcional.**

Matias abre su entorno y escribe: `@topic-cycle-v3 Programación Funcional --libro SICP --nivel 2`. El sistema responde confirmando el libro principal y el nivel. Ejecuta el Paso 0: le reporta que Tema 05 ya cubrió recursión y funciones de orden superior — sugiere que el material asuma ese conocimiento. Matias lee el reporte, confirma.

El sistema ejecuta los Pasos 1a/1b consultando ChromaDB — extrae secciones de SICP sobre funciones de orden superior, closures y evaluación lazy. Agrega tendencias de investigación sobre FP en lenguajes modernos. Genera el `topic-extract.md` y lo presenta para revisión. Matias lee las secciones extraídas, ajusta una cita, aprueba.

El sistema genera el plan de generación: 12 filminas ordenadas por progresión conceptual. Matias reordena dos filminas, aprueba el plan. El sistema ejecuta la generación filmina a filmina (Nivel 2). Al terminar, produce guía de estudio y guía docente consumiendo `topic-extract.md` desde disco. Matias tiene el tema completo en una sola sesión.

**Momento de deleite:** Matias abre la guía de estudio y ve que cada concepto tiene una referencia directa a SICP con número de página. Puede decirles a los alumnos exactamente qué leer.

### Journey 2 — Renovación de material del año anterior

**Matias tiene las filminas de Paradigmas 2025 para el Tema 08 y quiere actualizarlas.**

Invoca: `@topic-cycle-v3 Programación Funcional --libro SICP --nivel 2 --base filminas-2025/tema08.md`. El sistema ejecuta el pipeline normalmente hasta después del `topic-extract.md`. Luego compara las filminas 2025 con el `topic-extract.md` 2026: reporta que 7 de 14 filminas son válidas sin cambios, 4 necesitan actualización de terminología, y 3 deben eliminarse porque cubren temas que ya se dieron antes en la cursada 2026. Matias revisa el análisis, confirma la estrategia. El sistema genera el nuevo set usando las filminas válidas como base y regenerando solo las necesarias.

**Momento de deleite:** El trabajo histórico no se descarta — el 50% del material 2025 sobrevive directamente a 2026.

### Journey 3 — Material de repaso intensivo antes de parcial

**Una semana antes del parcial, Matias quiere filminas exhaustivas para que los alumnos puedan estudiar solos.**

Invoca: `@topic-cycle-v3 Programación Funcional --libro SICP --nivel 3`. El pipeline corre igual, pero en la generación (Paso 3) produce filminas que no asumen nada: cada concepto es explicado desde cero, con múltiples ejemplos, contra-ejemplos y variantes. La guía de estudio resultante tiene el triple de contenido que la versión Nivel 1. Matias la distribuye en el campus como material de repaso autónomo.

---

## Domain Requirements

### Dominio: EdTech — Producción de material docente universitario

**Restricciones normativas:**
- El nivel taxonómico de Bloom implícito en el material debe ser apropiado al momento de la cursada. Contenido introductorio (Bloom: Recordar/Comprender), material estándar (Bloom: Aplicar/Analizar), material exhaustivo de repaso (Bloom: Analizar/Evaluar). El parámetro de densidad mapea a estos niveles.
- La coherencia curricular no es opcional: un tema no puede asumir conceptos no cubiertos en temas anteriores del año en curso.

**Restricciones de calidad bibliográfica:**
- Solo libros en el corpus ChromaDB de la materia son fuentes válidas para el grounding principal.
- Contenido de libros con > 5 años en el tema tratado debe marcarse como "a verificar" si hay tendencias académicas contradictorias (Paso 1c).
- Las citas bibliográficas deben incluir referencia verificable (autor, libro, sección/página).

**Restricciones de compatibilidad:**
- Todo material generado debe ser compatible con el pipeline de publicación a Google Slides (`slides_pipeline.py`) — el schema de salida de filminas no cambia.
- Los artefactos generados por `topic-cycle-v3` deben convivir en el mismo directorio de temas que los generados por `topic-cycle` sin conflictos.

**Riesgos de dominio:**
- *Errores silenciosos de grounding:* el sistema puede producir contenido que parece bien citado pero malinterpreta el contexto del libro. Mitigación: checkpoint de `topic-extract.md` con revisión docente.
- *Superposición curricular no detectada:* el Paso 0 consulta el registro de temas dados, pero si ese registro está desactualizado, la coherencia falla. Mitigación: el docente puede forzar re-escaneo del historial.

---

## Innovation Patterns

**Bibliographic grounding como señal primaria obligatoria.** La innovación central no es técnica — es de proceso. Hacer que ChromaDB sea el primer paso en el pipeline (no opcional, no post-hoc) invierte el flujo habitual: en lugar de generar y luego citar, se extrae primero y luego se genera. Esto produce material donde el LLM es un editor de contenido bibliográfico, no un generador libre.

**`topic-extract.md` como contrato de conocimiento persisitido.** El artefacto intermedio no es solo un cache — es un contrato verificable entre el docente y el sistema. Su existencia como archivo en disco habilita: (a) revisión y edición humana, (b) consumo downstream sin re-invocar ChromaDB, (c) versionado y comparación entre años. Es la innovación estructural más significativa.

**Densidad como parámetro de primera clase.** Los sistemas de generación de material educativo típicamente producen un único nivel de profundidad. Hacer que la densidad sea un parámetro explícito de invocación — no un post-proceso de resumen/expansión — permite que el mismo pipeline produzca material pedagógicamente diferenciado para distintos momentos del curso.

---

## Project-Type Requirements

### AI Agent Pipeline — Consideraciones técnicas específicas

**Coordinación de agentes:**
- Cada paso del pipeline (Paso 0 a Paso 5) es una invocación atómica de un agente específico.
- Los agentes downstream (`class-writer`, `study-guide-writer`, `create-teacher-guide`) reciben `topic-extract.md` como input primario — no tienen acceso directo a ChromaDB en el flujo normal.
- El estado del pipeline se persiste en disco entre pasos: si se interrumpe en cualquier punto, el docente puede reanudar desde el último checkpoint completado.

**Contratos entre agentes:**
- El esquema de `topic-extract.md` es la interfaz de contrato entre `topic-designer` y los agentes downstream. Cualquier cambio al esquema requiere actualización de todos los consumidores.
- Secciones obligatorias del esquema: `fuentes` (lista de referencias con libro/sección/página), `conceptos-clave` (lista con definición corta), `ejemplos-bibliograficos` (ejemplos extraídos de los libros), `tendencias` (investigación académica reciente), `superposiciones-detectadas` (temas previos relacionados de la cursada 2026).

**Integración ChromaDB:**
- La colección activa es `edu_knowledge` con cosine similarity.
- Los Pasos 1a/1b usan `chroma_query_documents` con `where: {"type": "material"}` para filtrar solo material del curso.
- Si `chroma-mcp` no está disponible, el pipeline reporta el error y detiene la ejecución (no degrada silenciosamente).

**Compatibilidad con sistema existente:**
- Los 4 agentes refactorizados mantienen las mismas interfaces de invocación y los mismos formatos de salida.
- `topic-cycle-v3` es un nuevo archivo de workflow — no modifica `topic-cycle`.
- Los nuevos comportamientos (bibliographic-first, density levels, checkpoints) se activan únicamente vía la nueva invocación de workflow.

---

## Functional Requirements

### Área 1 — Invocación y configuración del workflow

- **FR01:** El docente puede invocar `topic-cycle-v3` especificando tópico, libro principal (override opcional) y nivel de densidad (1, 2 o 3).
- **FR02:** El sistema usa el libro configurado en `salida/edu-standalone/_edu/config.yaml` como libro principal por defecto cuando no se especifica en el prompt.
- **FR03:** El sistema informa explícitamente al inicio de cada ejecución qué libro fue seleccionado como fuente principal y qué nivel de densidad está activo.
- **FR04:** El docente puede proveer filminas del año anterior como parámetro opcional de base de renovación en la invocación.

### Área 2 — Coherencia curricular (Paso 0)

- **FR05:** El sistema consulta el registro de temas ya dados en la cursada 2026 antes de iniciar la extracción bibliográfica.
- **FR06:** El sistema reporta al docente las superposiciones detectadas con temas previos (conceptos cubiertos, nivel de solapamiento) y espera confirmación antes de continuar.
- **FR07:** El docente puede ajustar la estrategia de tratamiento de superposiciones (asumir conocido, resumir, referenciar) antes de que el pipeline continúe.

### Área 3 — Extracción bibliográfica (Pasos 1a/1b/1c)

- **FR08:** El sistema extrae contenido relevante del libro principal desde ChromaDB vía `chroma-mcp` como paso obligatorio no salteable.
- **FR09:** El sistema enriquece la extracción con libros secundarios del corpus cuando el libro principal no cubre suficientemente algún subtema.
- **FR10:** El sistema ejecuta investigación de tendencias académicas recientes vía web research (Paso 1c) y las integra al `topic-extract.md`.
- **FR11:** El sistema marca secciones de libros con > 5 años como "a verificar" cuando hay tendencias académicas contradictorias del Paso 1c.

### Área 4 — Artefacto intermedio y checkpoints

- **FR12:** El sistema genera `topic-extract.md` con las secciones obligatorias: `fuentes`, `conceptos-clave`, `ejemplos-bibliograficos`, `tendencias`, `superposiciones-detectadas`.
- **FR13:** El sistema persiste `topic-extract.md` en disco y espera aprobación explícita del docente antes de continuar al Paso 2 (checkpoint 1).
- **FR14:** El docente puede editar `topic-extract.md` directamente antes de aprobar el checkpoint.
- **FR15:** El sistema genera un plan de generación (lista ordenada de filminas/secciones con nivel de densidad) y espera aprobación del docente (checkpoint 2).
- **FR16:** El docente puede reordenar, agregar o eliminar filminas del plan antes de aprobar el checkpoint 2.

### Área 5 — Generación de material (Pasos 3/4/5)

- **FR17:** El sistema genera filminas en el nivel de densidad especificado: Nivel 1 (conceptos clave y ejemplos directos), Nivel 2 (desarrollo completo con contexto), Nivel 3 (exhaustivo, sin asumir conocimiento previo).
- **FR18:** El sistema genera guía de estudio consumiendo `topic-extract.md` desde disco, sin re-invocar ChromaDB.
- **FR19:** El sistema genera guía docente consumiendo `topic-extract.md` y las filminas generadas.
- **FR20:** El output de filminas es compatible con el pipeline de publicación a Google Slides (`slides_pipeline.py`) — el schema de salida no cambia.

### Área 6 — Renovación de material del año anterior

- **FR21:** Cuando se proveen filminas del año anterior, el sistema las compara con el `topic-extract.md` nuevo e identifica: filminas a conservar sin cambios, filminas a actualizar, filminas a eliminar (por superposición curricular).
- **FR22:** El sistema reporta el análisis de renovación al docente antes de generar el nuevo material.
- **FR23:** El sistema prioriza el reúso/adaptación de filminas existentes sobre la generación desde cero.

### Área 7 — Compatibilidad y coexistencia

- **FR24:** El workflow `topic-cycle` original funciona sin cambios tras la implementación de `topic-cycle-v3`.
- **FR25:** `topic-cycle-v3` puede activarse por flag en `config.yaml` o por invocación explícita del nombre del workflow.
- **FR26:** Los artefactos de `topic-cycle-v3` conviven en el mismo directorio de temas que los de `topic-cycle` sin conflictos de nombres.

---

## Non-Functional Requirements

### Confiabilidad y resiliencia

- **NFR01:** El estado del pipeline se persiste en disco tras completar cada paso. Si la ejecución es interrumpida, el docente puede reanudar desde el último checkpoint completado sin reprocesar pasos anteriores.
- **NFR02:** Si `chroma-mcp` no está disponible al iniciar Paso 1a, el sistema reporta el error con instrucciones de diagnóstico y detiene la ejecución (no degrada silenciosamente a generación sin grounding).
- **NFR03:** Los checkpoints (post Paso 1c, post Paso 2) persisten el estado aprobado aunque la sesión sea interrumpida — el docente no pierde su trabajo de revisión.

### Correctitud bibliográfica

- **NFR04:** Toda cita en `topic-extract.md` debe incluir libro, autor y sección o número de página verificable. Citas sin referencia completa deben marcarse explícitamente como "referencia incompleta".
- **NFR05:** El sistema no puede generar el plan de generación (Paso 2) sin que `topic-extract.md` tenga al menos una fuente bibliográfica verificada en la sección `fuentes`.

### Compatibilidad con sistema existente

- **NFR06:** Los 4 agentes refactorizados producen output en los mismos formatos que sus versiones anteriores (misma estructura de archivos, mismo schema de filminas, mismo formato de guías).
- **NFR07:** Los cambios no introducen dependencias nuevas que no estén ya presentes en el entorno de producción (excepción: `chroma-mcp`, que ya está configurado).
- **NFR08:** El tiempo de generación total de un tema completo con `topic-cycle-v3` no supera en más del 50% el tiempo equivalente con `topic-cycle` v2, considerando los checkpoints como tiempo controlado por el docente (no tiempo de sistema).

### Mantenibilidad

- **NFR09:** El esquema de `topic-extract.md` está documentado formalmente (secciones, tipos, obligatoriedad). Cualquier modificación al esquema requiere actualización de la documentación y de todos los agentes consumidores.
- **NFR10:** `topic-cycle-v3` está implementado como archivo de workflow independiente. No modifica los archivos de `topic-cycle` ni de los agentes de forma que rompa su uso independiente.

---

## Epics de Alto Nivel

| Epic | Descripción | Agentes/artefactos afectados |
|---|---|---|
| **E1 — Pipeline base v3** | Implementar `topic-cycle-v3` con los 7 pasos, checkpoints y persistencia de estado | `topic-cycle-v3` (nuevo), `topic-designer` (refactor) |
| **E2 — Bibliographic-first** | Integrar ChromaDB como Paso 1a/1b obligatorio; implementar esquema de `topic-extract.md` | `topic-designer`, `topic-extract.md` schema |
| **E3 — Coherencia curricular** | Implementar Paso 0 con consulta al registro de cursada y reporte de superposiciones | `topic-designer`, registro de temas |
| **E4 — Niveles de densidad** | Implementar generación en 3 niveles; parametrizar por invocación | `class-writer` (refactor), `study-guide-writer` (refactor) |
| **E5 — Renovación de año anterior** | Implementar comparación y reúso de filminas previas | `topic-designer`, lógica de diff |
| **E6 — Agentes downstream** | Refactorizar `study-guide-writer` y `create-teacher-guide` para consumir `topic-extract.md` | `study-guide-writer`, `create-teacher-guide` |

---

## Assumptions & Constraints

### Supuestos

- `chroma-mcp` está configurado y operativo en `.vscode/mcp.json` y la colección `edu_knowledge` contiene los libros de la materia.
- El registro de temas dados en la cursada 2026 existe y está accesible para el Paso 0 (ya sea como archivo o como metadata en los artefactos de temas previos).
- El docente dispone de al menos 5-10 minutos para revisar el `topic-extract.md` en cada checkpoint.
- Las filminas del año anterior (cuando se proveen) están en el formato de salida estándar de `topic-cycle` v2.

### Restricciones

- **Inmutabilidad del schema registry v3:** No se modifican los schemas de salida de las filminas.
- **Sin cambios al pipeline de publicación:** `slides_pipeline.py` permanece sin modificaciones.
- **Sin cambios a agentes de calidad:** `writing-validator`, `student-simulator` y agentes de testing no se modifican en v1.
- **Aditivo/opt-in obligatorio:** El sistema existente debe funcionar sin cambios. Zero modificaciones destructivas.
- **Cursada en curso:** La implementación debe poder desplegarse parcialmente (tema a tema) sin requerir migración de temas ya generados.

---

*PRD generado con el workflow `bmad-create-prd`. Versión completada: 2026-05-23.*
*Próximo paso recomendado: crear epics y stories (`bmad-create-epics-and-stories`) o validar PRD (`bmad-validate-prd`).*

