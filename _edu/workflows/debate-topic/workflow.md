# Workflow: Debate de Tema (Party Mode EDU)

**Module:** edu
**Phase:** 3 — Producción de Temas
**Owner Agent:** course-planner (orquestadora)

---

## Overview

Sesión de debate multi-agente sobre el diseño o contenido de un tema. Elena convoca al equipo relevante y facilita una discusión estructurada donde cada agente aporta desde su rol antes de que el docente tome una decisión.

**Cuándo usarlo:**
- Antes de aprobar un `diseño.md` controversial o complejo
- Cuando hay tensión entre duración, scope y profundidad
- Para evaluar si el TP está bien balanceado respecto a la clase
- Para revisar si el material aprobado está desactualizado curricularmente

---

## Participantes disponibles

| Agente | Persona | Foco en el debate |
|--------|---------|-------------------|
| `topic-designer` | Lic. Marcos | Scope, duración, estructura del diseño |
| `class-writer` | Dr. Roberto | Claridad, narrativa, proporción clase/contenido |
| `tp-designer` | Aux. Valeria | Trazabilidad TP → clase, dificultad práctica |
| `curriculum-reviewer` | Prof. Ana | Actualización curricular, evidencia académica |
| `academic-researcher` | Bib. Carlos | Fuentes y referencias del tema |
| `student-simulator` | Estudiante | Perspectiva del alumno, dificultad cognitiva |
| `academic-guardrail` | Guardrail | Formalidad, densidad, scope final |

---

## Steps

### Step 1: Inicio del Debate
- **Agent:** course-planner (Elena)
- **Input:** Número de tema + pregunta o decisión a debatir
- **Action:** Elena presenta el tema, el contexto (diseño.md o material existente) y formula la pregunta central del debate
- **Output:** Agenda del debate con 2–4 puntos a resolver

### Step 2: Selección de Panel
- **Agent:** course-planner (Elena)
- **Rules:**
  - Mínimo 3 agentes, máximo 5
  - Por defecto: Marcos + Roberto + Valeria (el trío de producción)
  - Si hay duda curricular: sumar a Prof. Ana
  - Si hay duda de comprensión del alumno: sumar Simulador
  - Si hay duda de referencias: sumar Carlos
- **Output:** Panel confirmado para esta sesión

### Step 3: Ronda de Apertura
- **Orchestrator:** course-planner (Elena)
- **Action:** Cada agente del panel da su posición inicial sobre la pregunta central
- **Rules:**
  - Cada agente responde **desde su rol** — Marcos habla de scope, Roberto de narrativa, etc.
  - Respuestas breves: 3–5 líneas por agente
  - Elena modera: "Marcos, ¿qué decís sobre el scope?" → respuesta → "Roberto, ¿cómo ves vos la clase?"
- **Output:** Posiciones iniciales de cada agente

### Step 4: Ronda de Tensiones
- **Orchestrator:** course-planner (Elena)
- **Action:** Elena identifica los puntos de desacuerdo entre agentes y los pone en juego
- **Rules:**
  - Si Marcos dice "está fuera de scope" y Roberto dice "necesito ese ejemplo para la narrativa" → Elena los enfrenta: "Marcos, Roberto no puede narrar sin ese ejemplo. ¿Podemos acotarlo?"
  - Valeria puede interrumpir si el TP queda huérfano: "Si recortamos eso, el TP no tiene anclaje práctico."
  - El guardrail interviene SOLO al final si hay problemas de densidad o formalidad
- **Output:** Tensiones explicitadas y argumentos de cada lado

### Step 5: Ronda de Síntesis
- **Orchestrator:** course-planner (Elena)
- **Action:** Elena resume los puntos de consenso y los puntos irresueltos
- **Format:**
  ```
  ✅ CONSENSO: [lista de acuerdos del equipo]
  ⚠️  TENSIÓN IRRESUELTA: [puntos donde el equipo no coincide]
  📋 RECOMENDACIÓN DEL EQUIPO: [posición mayoritaria o más fundamentada]
  ```

### Step 6: Decisión del Docente
- **Agent:** course-planner (Elena)
- **Gate:** HALT — presentar síntesis al docente y ESPERAR
- **Prompt:** "🎓 {user_name}, el equipo debatió. ¿Cuál es tu decisión?"
- **Options:**
  - `[A]` Aprobar diseño/material tal como está
  - `[M]` Modificar según recomendación del equipo → volver al Step 1 del topic-cycle
  - `[R]` Rechazar y rediseñar desde cero
  - `[C]` Continuar debatiendo un punto específico → volver al Step 4

### Step 7: Registro
- **Agent:** course-planner (Elena)
- **Action:** Guardar síntesis del debate en `{topic_folder}/debate-[fecha].md`
- **Output:** Archivo de registro para trazabilidad de la decisión docente

