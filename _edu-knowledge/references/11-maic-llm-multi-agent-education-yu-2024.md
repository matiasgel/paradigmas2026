# MAIC: From MOOC to Massive AI-empowered Course

**Referencia:** Yu, J., Zhang, Z., Zhang-Li, D., Tu, S., et al. (2024). "From MOOC to MAIC: Reshaping Online Teaching and Learning through LLM-driven Agents." arXiv:2409.03512. Publicado en JCST 2026 (DOI: 10.1007/s11390-025-6000-0).

**Institución:** Tsinghua University — School of Education + Dept. of Computer Science.

**Escala del estudio:** 500+ estudiantes, 100,000+ registros de aprendizaje, 3 meses de despliegue, 2 cursos (TAGI + HSU).

---

## Concepto Central

MAIC propone evolucionar de MOOC (Massive Open Online Course) a un modelo donde **sistemas multi-agente LLM** construyen un "aula aumentada por IA", balanceando:

- **Escalabilidad** (scalability): servir a miles de estudiantes
- **Adaptabilidad** (adaptivity): personalización que MOOC no ofrece

El paradigma es "1 Student + N AI Agents" — un alumno interactúa con múltiples agentes (profesor IA, asistente IA, compañeros IA) que adaptan la enseñanza en tiempo real.

### Relevancia para EDU

EDU implementa un modelo análogo pero para **producción de cursos presenciales asistida por agentes**: múltiples agentes especializados (Elena, Roberto, Marcos, Valeria, etc.) producen material pedagógico coordinadamente. MAIC valida experimentalmente que este enfoque multi-agente mejora la calidad educativa.

---

## Arquitectura del Sistema

### 3.1 Teaching Side: Course Preparation Workflow

Dos etapas (Read + Plan) para transformar slides estáticos en recursos de aprendizaje estructurados.

#### Read Stage (Extracción)

1. **Slides Content Extraction**: mLLM (GPT-4V) extrae contenido textual (P_t) y visual (P_v) de cada slide.
2. **Structure Extraction**: Descripción comprehensiva de cada página + taxonomía de conocimiento en árbol.

**Paralelismo EDU:** El pipeline de filminas de EDU hace exactamente esto: `filminas.md` → `parse_filminas.py` → `plan-filminas.json` (extracción estructurada de cada filmina con layouts, elementos, notas de orador).

#### Plan Stage (Generación)

3. **Function Generation**: Acciones de enseñanza como lenguaje de representación:
   - `ShowFile` — mostrar slide
   - `ReadScript` — lectura de guión
   - `AskQuestion` — pregunta activa al alumno
   - Cada acción: T = (type, value)

4. **Agent Generation**: Instructor proporciona información personalizada → se construyen agentes customizados (Teacher Agent, TA Agent) con RAG sobre materiales del curso.

**Paralelismo EDU:** EDU genera `minuta.md` (script del profesor) y puede producir preguntas integradas vía TPs. Los agentes EDU (Roberto, Valeria) son equivalentes a los Function Generators de MAIC.

---

### 3.2 Learning Side: Multi-agent Classroom Environment

#### Taxonomía de Interacciones (Schwanke 1981)

| Categoría | Código | Descripción |
|---|---|---|
| Teaching & Initiation | TI | Instrucción del profesor + feedback del alumno |
| In-depth Discussion | ID | Deliberación, Q&A iterativo, comprensión conceptual |
| Emotional Companionship | EC | Motivación, ambiente positivo, sustento emocional |
| Classroom Management | CM | Orden, organización, direccionamiento del discurso |

#### 4 Agentes-Compañero (Classmate Agents)

| Agente | Roles | Función |
|---|---|---|
| Class Clown | TI, EC, CM | Creatividad, ambiente lúdico, redirigir atención |
| Deep Thinker | TI, ID | Preguntas profundas, extender límites intelectuales |
| Note Taker | TI, CM | Resumir puntos clave, organización cognitiva |
| Inquisitive Mind | TI, EC | Cultura de indagación, pensamiento crítico |

**Paralelismo EDU:** El Simulador Pedagógico de EDU implementa perfiles de alumnos similares (el que no entiende, el avanzado, el distraído) para testing pre-despliegue. MAIC valida que esta diversidad de "personalidades" mejora el engagement.

#### Session Controller

- **Class State Receptor**: Captura diálogo en curso, historial H_t, materiales cubiertos P_t.
- **Manager Agent**: Meta-agente oculto que decide qué agente actúa y qué acción ejecuta: f_L: S_t → (a_t, T).
- Tiempo de espera τ entre acciones para permitir intervención del alumno.

**Paralelismo EDU:** En EDU, el Course Planner (Elena) funciona como Manager Agent, orquestando qué agente interviene en cada fase del ciclo de producción.

---

## Evaluación Técnica

### Teaching: Script Generation

| Método | Tone | Clarity | Supportive | Matching | Overall |
|---|---|---|---|---|---|
| S2T (Nguyen 2023) | 3.88 | 3.93 | 3.23 | 3.63 | 3.67 |
| SCP (Zheng 2024) | 4.03 | 4.24 | 3.38 | 3.93 | 3.90 |
| **MAIC-FuncGen** | **4.00** | **4.25** | **3.57** | **4.18** | **4.00** |
| MAIC sin visual | 3.78 | 3.73 | 3.44 | 3.51 | 3.61 |
| MAIC sin contexto | 3.97 | 4.00 | 3.38 | 4.03 | 3.84 |
| **Human** | 4.02 | 4.07 | 3.38 | 3.98 | **3.86** |

**Hallazgos clave:**
- MAIC **supera a instructores humanos** (4.00 vs 3.86) en overall.
- Input visual **crítico**: sin visual cae a 3.61 (-0.39).
- Contexto entre slides mejora coherencia narrativa.
- LLMs mantienen tono instructivo y soporte emocional más consistente que humanos.

**Implicación para EDU:** Validación empírica de que el pipeline de filminas debe incluir información visual (thumbnails, descripciones de imágenes) además del texto — coherente con el uso de Gemini multimodal en el pipeline EDU.

### Learning: Manager Agent Precision

- Evaluado con 500 decisiones reales, anotadas por profesores expertos.
- Las **descripciones de rol** para cada agente mejoran significativamente la precisión del controller.
- Sin role descriptions: el LLM parcialmente compensa usando historial de chat, pero insuficiente.
- El agente teacher es más efectivo en pedagogía; el agente TA en safety — cada rol optimizado para su función.

**Implicación para EDU:** Confirma que los agentes EDU necesitan system prompts detallados con roles claros (ya implementado en `_edu/agents/`).

---

## Experimento Conductual (500+ estudiantes)

### Q1: Calidad del Curso

- Encuesta Community of Inquiry Framework (Garrison & Arbaugh 2007).
- "El instructor IA comunicó claramente los objetivos del curso": **4.12/5** (SD=0.66).
- "El instructor IA alentó explorar nuevos conceptos": **4.03/5** (SD=0.73).
- **Debilidad detectada**: "El instructor IA proporcionó feedback personalizado sobre fortalezas/debilidades": **3.51/5** (SD=0.94) — falta personalización adaptativa.

### Q2: Engagement Estudiantil

- Estudiantes prefieren **modo continuo** (sin interrupciones) vs modo interactivo.
- **61%** del comportamiento en clase = **búsqueda proactiva de conocimiento** (preguntas).
- **11%** = comportamientos de **gestión y control** (navegar slides, pedir explicaciones más simples).
- Citas de estudiantes: "La IA me hacía preguntas de seguimiento... como si realmente me guiara a pensar más profundamente."

### Q3: Resultados de Aprendizaje

**Test scores:**
- Module tests: 53.3% a 82.4% (rango por módulo).
- Asistencia promedio: 76.3% (modules), 73.3% (final).

**Correlación engagement → rendimiento:**

| Métrica | Frecuencia mensajes | Longitud mensajes |
|---|---|---|
| AvgQuiz (sin control) | 0.341*** | 0.202* |
| FinalExam (sin control) | 0.346*** | 0.333** |
| AvgQuiz (con control M1) | 0.206** | 0.177** |
| FinalExam (con control M1) | 0.174 | 0.235* |

**Conclusión:** Mayor engagement con agentes IA → mejores calificaciones. Correlación estadísticamente significativa (p<0.001 para frecuencia).

**Technology acceptance:** Aumento significativo post-curso (N=111, t=3.05, p=0.002). Mejoras en Habit, Effort Expectancy, Facilitating Conditions.

**Higher-order thinking:** Mejoras significativas en pensamiento abstracto (t=2.32, p=0.02) y pensamiento crítico (t=2.37, p=0.02).

---

## Consideraciones Éticas

1. **Privacidad**: Encriptación y anonimización de datos estudiantiles.
2. **Sesgo algorítmico**: Auditorías de fairness en personalización.
3. **Rol del docente**: Human-in-the-loop — instructores pueden intervenir en decisiones de la IA.
4. **Interacción social**: Agentes-compañero no reemplazan comunicación humana → recomendar modos mixtos.
5. **Precisión de contenido**: Revisión por expertos + mecanismo de reporte de errores por alumnos.

---

## Implicaciones para Sprints EDU

### Sprint 1 (Accesibilidad)
- MAIC confirma la necesidad de múltiples modos de interacción (continuo vs interactivo) para distintas preferencias de aprendizaje.

### Sprint 2 (Repetición Espaciada)
- Correlación engagement-rendimiento valida que testing frecuente mejora retención (cita de alumno: "si no hubiera test post-clase, no recordaría nada").

### Sprint 3 (Evaluar con IA)
- MAIC usa evaluación integrada con LLMs: module tests + final exam. Precedente directo.

### Sprint 4 (GitHub Classroom)
- Workflow de "Course Preparation" = modelo para automatizar deployment de repos.

### Sprint 5 (Simulación Avanzada)
- Los 4 Classmate Agents son un blueprint para evolucionar el Simulador Pedagógico de EDU con más perfiles basados en evidencia (Class Clown, Deep Thinker, Note Taker, Inquisitive Mind).

### Sprint 6 (Adaptativo + MCP)
- Session Controller de MAIC = modelo de referencia para el routing adaptativo de EDU.
- Manager Agent decision function f_L: S_t → (a_t, T) es formalizable como MCP tool routing.

---

## Referencias Cruzadas

- Schwanke (1981) — Taxonomía de interacciones en aula
- Garrison & Arbaugh (2007) — Community of Inquiry Framework
- Park et al. (2023) — Generative Agents (agentes sociales simulados)
- Wu et al. (2023) — AutoGen (multi-agent conversation framework)
- Qian et al. (2023) — ChatDev (multi-agent software development)
- Pal Chowdhury et al. (2024) — AutoTutor meets LLMs (pedagogical guardrails)
- Chen et al. (2024) — Chaining LLMs for private tutoring
- Yue et al. (2024) — MathVC (virtual classroom simulation)
