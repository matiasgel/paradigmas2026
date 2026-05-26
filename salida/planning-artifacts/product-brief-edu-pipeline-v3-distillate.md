---
title: "Product Brief Distillate: EDU Production Pipeline v3"
type: llm-distillate
source: "product-brief-edu-pipeline-v3.md"
created: "2026-05-23"
purpose: "Contexto token-eficiente para creación del PRD. Contiene overflow de la sesión de discovery: hints de requisitos, contexto técnico, restricciones, decisiones y preguntas abiertas para v2."
---

# Distillate — EDU Production Pipeline v3

## Sistema actual (contexto crítico para PRD)

- **24 agentes activos** en `salida/edu-standalone/_edu/agents/` organizados en 4 capas: Personas (7), Calidad (5), Testing (2), Internos (3) + especializados
- **Flujo central actual:** `topic-cycle` → `diseno.md → minuta.md → filminas.md → guia-estudio.md → tp.md`
- **4 agentes a refactorizar:** `topic-designer` (Marcos), `class-writer` (Roberto), `study-guide-writer` (Sofía), más el workflow `create-teacher-guide`
- **ChromaDB ya operativo:** colección `edu_knowledge`, configurada en `.env` via `EDU_CHROMA_PATH`, plugin `chroma-mcp` en `.vscode/mcp.json`; collection tiene material del curso + 12 refs académicas + 16 docs de herramientas
- **Principio cardinal del proyecto:** CERO modificaciones destructivas. Todo aditivo. Todo opt-in via flags en `config.yaml`. Ver `sprints-mejoras-edu-v2.md`
- **Hay dos copias del pipeline** (`scripts/slides_pipeline.py` vs `salida/edu-standalone/scripts/slides_pipeline.py`) — issue previo de `arquitectura-pipeline-filminas-v4.md` no relacionado con este brief pero a tener en cuenta para no romper

## Requisitos funcionales capturados (hints para el PRD)

### Pipeline paso a paso (BMAD-native)
- Cada agente DEBE producir primero un plan explícito (lista de pasos/secciones) antes de ejecutar
- El profesor aprueba o modifica el plan entre pasos — no al final
- Cada paso es una llamada atómica (no bloques de razonamiento largo)
- El profesor puede reordenar las filminas en el PASO 2 (plan de generación) antes de generar

### Artefacto intermedio `topic-extract.md`
- Esquema definido: secciones `fuentes`, `conceptos-clave`, `ejemplos-bibliograficos`, `tendencias`, `superposiciones-detectadas`
- Se persiste en el directorio del tema (p.ej. `salida/cursadas/2026/temas/{tema}/topic-extract.md`)
- Es consumido por los 4 agentes downstream — NO regeneran la extracción
- En v1 solo se genera para temas nuevos; en temas existentes es generación manual opcional

### Extracción bibliográfica (PASOS 1a/1b)
- **Libro principal:** primero busca en `config.yaml` de la materia (`primary_book`), si no está definido allí el profesor lo indica en el prompt de invocación
- **El prompt tiene precedencia sobre config** (el agente informa qué libro usó)
- **Libros complementarios:** todos los demás del corpus — enriquecen, no reemplazan
- **Criterio de vigencia:** si el libro tiene >5 años en el tema Y hay tendencias contradictorias del PASO 1c → marcar contenido como "a verificar"
- La extracción se hace via `chroma_query_documents` (chroma-mcp). Si `chroma-mcp` no está instalado → auto-instalar en primera llamada

### Investigación académica (PASO 1c)
- Web research sobre conceptos encontrados en el tópico
- Busca últimas tendencias, papers (DOI, ACM, IEEE, arXiv), evolución reciente
- `academic-researcher` (Carlos) ya existe y hace esto — integrarlo como paso obligatorio en el pipeline, no opcional

### Coherencia curricular (PASO 0)
- Consulta los temas ya dados en la cursada actual (detectables por carpetas en `topics_folder`)
- Detecta superposiciones conceptuales → ajusta estructura del tópico actual
- El profesor ve el reporte de superposiciones antes de continuar
- Potencial v2: también mirar temas futuros que asumen este como prerequisito

### Niveles de densidad
- **Nivel 1 — Introductorio:** filminas con conceptos clave y ejemplos directos; material del alumno introductorio; asume que el alumno no sabe nada del tema
- **Nivel 2 — Estándar:** filminas con desarrollo y contexto; material completo de cursada; nivel por defecto
- **Nivel 3 — Exhaustivo:** filminas completamente explicadas sin dejar nada implícito; material para estudio profundo o autoaprendizaje; ningún concepto queda sin desarrollar
- **Selección:** global por invocación en v1 (un solo nivel para todo el tema)
- **v2:** por sección individual del plan de generación
- El nivel se pasa como parámetro al workflow `topic-cycle-v3`

### Reutilización de filminas del año anterior
- El profesor indica las filminas del año anterior en el prompt de activación (ruta o nombre del tema)
- El agente las compara con el nuevo `topic-extract.md`
- Produce reporte: qué conservar / qué actualizar / qué eliminar / qué agregar
- Genera filminas nuevas sobre esa base, no desde cero
- La historia queda en Git naturalmente (commits)

## Contexto técnico / restricciones

- **ChromaDB config:** en `.env` del proyecto (`EDU_CHROMA_PATH`). Rama `production` usa `C:\Users\matia\Documents\chroma_db` (Windows); en dev usa `~/.edu/chroma_db`
- **Nuevo workflow:** `topic-cycle-v3` — NO modifica `topic-cycle` existente. Ambos coexisten.
- **Agentes afectados:** se actualizan los 4 en `salida/edu-standalone/_edu/agents/`, respetando el schema de agentes BMAD
- **Workflows afectados:** `topic-cycle` (se crea v3), `create-teacher-guide` (se actualiza para consumir `topic-extract.md`)
- **Nuevo campo en `config.yaml`:** `primary_book: ""` (nombre o ID del libro principal en ChromaDB), `default_density_level: 2` (1/2/3)
- **Feature flags a agregar en `config.yaml`:** `bibliographic_extraction_enabled: true`, `curriculum_coherence_check_enabled: true`, `density_levels_enabled: true`, `previous_year_base_enabled: false`

## Preguntas abiertas para v2 (no bloquean v1)

- Niveles de densidad por sección individual (no solo global)
- Coherencia curricular bidireccional: también verificar si temas futuros asumen este como prerequisito
- Retrocompatibilidad automática: generar `topic-extract.md` para todos los temas existentes de 2026
- Versionar `topic-extract.md` como fuente de datos del knowledge graph (`knowledge_graph.py` ya existe)
- Calibración de la búsqueda ChromaDB: ¿cuántos chunks devolver por libro para no saturar el contexto?

## Ideas descartadas / no incluidas en v1

- Modificar el schema registry v3 — INMUTABLE por principio de arquitectura. No se toca.
- Cambiar el pipeline de publicación Google Slides — fuera de scope.
- Integrar los agentes de calidad (`writing-validator`, etc.) dentro del nuevo pipeline paso a paso — los calidad son posteriores al ciclo de producción, siguen siendo un paso separado.
- Pipeline por sección (generar filmina por filmina con confirmación individual) — demasiado granular para v1; el checkpoint es al nivel del plan completo.

## Escenarios de uso del profesor (para el PRD)

**Escenario A — Clase nueva sin material previo:**
`/topic-cycle-v3 tema="Tipos compuestos" nivel=2`
→ PASO 0 (coherencia) → PASO 1 (extracción ChromaDB) → PASO 1c (research) → muestra topic-extract.md → CHECKPOINT → PASO 2 (plan) → CHECKPOINT → genera filminas nivel 2 paso a paso

**Escenario B — Renovar clase del año anterior:**
`/topic-cycle-v3 tema="Polimorfismo" nivel=2 base-anterior="2025/temas/polimorfismo/filminas.md"`
→ igual que A pero en PASO 3 compara con las filminas 2025 antes de generar

**Escenario C — Clase introductoria rápida:**
`/topic-cycle-v3 tema="Herencia" nivel=1`
→ genera material simplificado para primera exposición

**Escenario D — Material de repaso para parcial:**
`/topic-cycle-v3 tema="Paradigma funcional" nivel=3`
→ genera filminas exhaustivas sin dejar nada sin explicar

## Artefactos de referencia del repositorio

- `salida/edu-standalone/_edu/config.yaml` — configuración del módulo
- `salida/edu-standalone/_edu/agents/` — agentes a modificar
- `salida/edu-standalone/_edu/workflows/topic-cycle/workflow.md` — workflow base
- `salida/edu-standalone/_edu/workflows/create-teacher-guide/workflow.md` — a actualizar
- `salida/edu-standalone/_edu/schemas/schema-registry.json` — INMUTABLE
- `salida/edu-standalone/scripts/knowledge_base.py` — interfaz ChromaDB (complementa chroma-mcp)
- `salida/planning-artifacts/sprints-mejoras-edu-v2.md` — principios de seguridad del sprint plan
