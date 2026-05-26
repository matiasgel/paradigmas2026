# OpenMAIC — Plataforma Multi-Agent Interactive Classroom

**Fuente:** [github.com/THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)
**Autores:** THU-MAIC (Tsinghua University), basado en Yu et al. (2024) arXiv:2409.03512
**Licencia:** AGPL-3.0
**Estadísticas (marzo 2026):** 12.3k stars, 1.9k forks
**Stack:** Next.js 15 App Router, TypeScript 98.1%, LangGraph, Zustand, Tailwind CSS

## Resumen

OpenMAIC es la implementación open-source del paper MAIC ("From MOOC to MAIC"). Convierte cualquier tema en un aula interactiva con múltiples agentes IA (teacher, TA, classmates) que presentan contenido, dibujan en whiteboard, hacen quizzes y generan simulaciones interactivas.

## Arquitectura de Generación (2 etapas)

### Etapa 1: Outline Generation (`outline-generator.ts`, 187 líneas)

- Input: tema + materiales de referencia (PDF/texto/URL)
- Output: outline estructurado con secciones, sub-secciones y tipos de escena
- Tipos de escena disponibles: `slides`, `quiz`, `interactive`, `pbl`
- El LLM genera el outline en formato JSON tipado

### Etapa 2: Scene Generation (`scene-generator.ts`, 1292 líneas)

- Input: outline + contexto cross-página (`SceneGenerationContext`)
- Output: contenido detallado por escena (slides con elementos, quizzes con respuestas, HTML interactivo)
- Tipos de elementos de slide: `text`, `image`, `video`, `shape`, `chart`, `latex`, `line`
- `SceneGenerationContext` mantiene coherencia entre páginas (resúmenes previos, conceptos introducidos)

### Tipos clave (`pipeline-types.ts`, 72 líneas)

```typescript
interface GeneratedSlideData {
  elements: Array<TextElement | ImageElement | VideoElement | ShapeElement | ChartElement | LatexElement | LineElement>
  notes: string
  layout: string
}

interface SceneGenerationContext {
  previousSummaries: string[]      // Resúmenes de escenas anteriores
  introducedConcepts: string[]     // Conceptos ya presentados
  currentSection: string           // Sección actual del outline
  overallObjective: string         // Objetivo general de la clase
}

interface AgentInfo {
  id: string
  name: string
  role: string                     // "teacher" | "ta" | "classmate"
  description: string
  personality: string
}
```

## Orquestación Multi-Agent (LangGraph)

### Director Graph (`director-graph.ts`, 549 líneas)

Implementado como LangGraph `StateGraph` con la siguiente topología:

```
START → director → agent_generate → director → ... → END
```

**Estado del orquestador (`OrchestratorState`):**
- `messages`: Historial de mensajes del aula
- `storeState`: Estado persistente del classroom store (Zustand)
- `availableAgentIds`: Agentes que pueden participar
- `maxTurns`: Límite de turnos (configurable)
- `turnCount`: Turno actual
- `agentResponses`: Respuestas acumuladas
- `whiteboardLedger`: Estado del whiteboard (qué se ha dibujado)
- `shouldEnd`: Flag de terminación

**Nodo Director:**
- **Modo single-agent** (solo teacher): Determinístico (code-only), no usa LLM
- **Modo multi-agent** (teacher + TA + classmates): Usa LLM para decidir:
  - `AGENT:<id>` → el agente indicado toma el turno
  - `USER` → le toca al alumno (pausa)
  - `END` → fin de la secuencia
- El prompt del director incluye: descripciones de agentes, resumen de conversación, estado del whiteboard

**Nodo Agent Generate:**
- Recibe el agente seleccionado por el Director
- Genera contenido (speech + actions) usando el prompt del agente + contexto
- Las acciones son tipadas (ver Tool Schemas)

### Director Prompt (`director-prompt.ts`, 277 líneas)

Construye el prompt del Director con:
1. Descripciones de todos los agentes disponibles
2. Resumen de la conversación hasta el momento
3. Estado actual del whiteboard (qué elementos están dibujados)
4. Instrucciones de decisión (cuándo pasar turno, cuándo terminar)

## Sistema de Acciones (`tool-schemas.ts`, 68 líneas)

15 acciones tipadas que los agentes pueden realizar:

| Acción | Descripción |
|---|---|
| `speech` | Contenido hablado (+ TTS) |
| `spotlight` | Resaltar un elemento en la diapositiva |
| `laser` | Puntero láser animado |
| `wb_open` | Abrir whiteboard |
| `wb_draw_text` | Escribir texto en whiteboard |
| `wb_draw_shape` | Dibujar forma (rect, circle, triangle, arrow) |
| `wb_draw_chart` | Dibujar gráfico (bar, line, pie, scatter) |
| `wb_draw_latex` | Renderizar fórmula LaTeX |
| `wb_draw_table` | Dibujar tabla |
| `wb_draw_line` | Dibujar línea/flecha |
| `wb_clear` | Limpiar whiteboard |
| `wb_delete` | Eliminar elemento específico |
| `wb_close` | Cerrar whiteboard |
| `play_video` | Reproducir video embebido |

## Tipos de Escena

### Slides
- Elementos: texto, imágenes, video, shapes, charts, LaTeX, líneas
- Layout configurable
- Speaker notes para TTS

### Quiz
- Tipos: single choice, multiple choice, short answer
- Respuesta correcta + explicación almacenadas
- Grading por IA en tiempo real

### Interactive (HTML Simulations)
- HTML autocontenido generado por LLM
- Ejecutable en browser sin dependencias
- Ejemplos: simuladores de física, visualizadores de algoritmos, flowcharts interactivos

### Project-Based Learning (PBL)
- Estructura: driving question → milestones → deliverables
- Roles asignados a alumnos
- Scaffolding por agentes IA

## Agentes del Aula

### Teacher Agent
- Presenta contenido principal
- Usa whiteboard para explicaciones paso-a-paso
- Controla el ritmo de la clase

### Teaching Assistant (TA)
- Responde preguntas del alumno
- Ofrece explicaciones alternativas
- Monitorea comprensión

### Classmate Agents (4 arquetipos)
Basados en la taxonomía Schwanke (1981):
1. **Class Clown** — Emotional Companionship (EC): alivia tensión, hace analogías humorísticas
2. **Deep Thinker** — In-depth Discussion (ID): profundiza, conecta con otros temas
3. **Note Taker** — Teaching & Initiation (TI): resume, organiza, pide aclaraciones
4. **Inquisitive Mind** — Classroom Management (CM): pregunta "¿por qué?", cuestiona supuestos

## Integraciones

- **OpenClaw**: Chat integration con Feishu, Slack, Discord, Telegram
- **MinerU**: OCR y extracción de tablas complejas desde PDFs
- **TTS**: Múltiples proveedores (configurables), voz personalizable por agente
- **Export**: `.pptx` (editable) + `.html` (interactivo)
- **i18n**: zh-CN, en-US (extensible)

## Comparación con EDU

### Funcionalidades que EDU podría adoptar
1. **Interactive HTML Simulations** — generación de simuladores autocontenidos
2. **Whiteboard annotations** — anotaciones paso-a-paso sobre slides
3. **TTS narration** — audio para clases asíncronas
4. **PBL structured projects** — proyectos multi-clase con milestones
5. **Multi-agent orchestration** — Director Agent para flujos automáticos
6. **Classmate debate simulation** — simulación de dinámica de aula completa

### Ventajas de EDU que OpenMAIC no tiene
1. **Quality loops** — validación formal con guardrails y JSON Schema
2. **Plan mínimo curricular** — trazabilidad programa oficial → material
3. **Memoria colectiva** — SQLite FTS5 cross-año + ChromaDB knowledge base
4. **Evaluación auténtica multi-formato** — GIFT, TPs repo, autograding GitHub Actions
5. **Human-in-the-loop gates** — validación docente en cada etapa
6. **Producción presencial** — material para aula real (minutas 2h, guías impresas)
7. **WCAG accesibilidad** — validación de accesibilidad automatizada
8. **Evidence-based auditing** — slides auditadas contra principios cognitivos

## Relevancia para Sprints EDU

| Sprint | Feature OpenMAIC relevante |
|---|---|
| S3 (Evaluación) | Quiz con AI grading, PBL estructura |
| S4 (Interactividad) | HTML simulations, whiteboard annotations, TTS |
| S5 (Analytics) | Classmate agents para simulación predictiva |
| S6 (Escalabilidad) | Multi-agent orchestration con LangGraph |
