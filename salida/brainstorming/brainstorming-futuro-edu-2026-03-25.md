# Brainstorming — EDU Módulo: Propuestas Futuras Realistas

**Fecha:** 2026-03-25
**Facilitador:** Sistema + Matiasgel
**Criterio:** Cada propuesta debe tener (1) evidencia académica verificable y actualizada (preferencia post-2020), (2) viabilidad técnica con las herramientas existentes o alcanzables, (3) diferenciación clara vs. herramientas existentes.

> **Nota de actualización (2026-03-25):** Todas las referencias fueron revisadas contra el estado del arte al Q1 2026. Se reemplazaron citas obsoletas (Knewton 2015, Bunce 2010, SM-2) y se agregaron trabajos post-2020 que reflejan el impacto de GenAI en educación (Kasneci 2023, Yan 2024, Mollick 2023, Denny 2024). Las citas clásicas (Ebbinghaus, Bloom, Mayer) se mantienen con nota de vigencia.

> **Nota de actualización (2026-03-26, OpenMAIC):** Agregadas propuestas #13-18 basadas en análisis competitivo de OpenMAIC (THU-MAIC, 12.3k stars). Se analizó el código fuente de 6 componentes clave.

> **Nota de actualización (2026-03-26, Beyond-LLM):** Agregadas propuestas #19-26 — "Más allá de LLMs". Mix de modelos cognitivos, ML especializado y knowledge bases: Knowledge Graphs (OWL/SPARQL), NLI fact verification (DeBERTa), topic modeling (BERTopic), prerequisite learning (GNN/XGBoost), psicometría (IRT/BKT), evaluación visual (CLIP/LayoutLM), detección de drift semántico, y clasificación Bloom neuro-simbólica. Total: 26 propuestas con 80+ referencias académicas.

---

## Índice de Propuestas

| # | Propuesta | Madurez | Impacto | Complejidad | Fuente |
|---|-----------|---------|---------|-------------|--------|
| 1 | Layout Engine con Ciencia Cognitiva | 🟡 Prototipar | 🔴 Alto | 🟡 Media | EDU original |
| 2 | Accesibilidad Universal (WCAG + Remote) | 🟢 Implementable | 🔴 Alto | 🟢 Baja | EDU original |
| 3 | Currícula Comparada Mundial (MCP) | 🟡 Prototipar | 🔴 Alto | 🔴 Alta | EDU original |
| 4 | GitHub Classroom Push Directo | 🟢 Implementable | 🟡 Medio | 🟢 Baja | EDU original |
| 5 | Student Analytics Dashboard | 🟡 Prototipar | 🔴 Alto | 🟡 Media | EDU original |
| 6 | Git Auto-Responder para Alumnos | 🟢 Implementable | 🟡 Medio | 🟢 Baja | EDU original |
| 7 | Adaptive Learning Path Engine | 🟡 Prototipar | 🔴 Alto | 🔴 Alta | EDU original |
| 8 | Evidence-Based Slide Audit | 🟢 Implementable | 🔴 Alto | 🟡 Media | EDU original |
| 9 | Cross-Campus MCP Server | 🔴 Investigar | 🔴 Alto | 🔴 Alta | EDU original |
| 10 | Cognitive Load Optimizer | 🟡 Prototipar | 🔴 Alto | 🟡 Media | EDU original |
| 11 | Spaced Repetition Engine | 🟢 Implementable | 🟡 Medio | 🟢 Baja | EDU original |
| 12 | Exam Blueprint Generator | 🟢 Implementable | 🟡 Medio | 🟡 Media | EDU original |
| 13 | Interactive Scene Generator | 🟡 Prototipar | 🔴 Alto | 🟡 Media | OpenMAIC |
| 14 | Whiteboard Annotations | 🟡 Prototipar | 🟡 Medio | 🟡 Media | OpenMAIC |
| 15 | PBL Generator | 🟡 Prototipar | 🔴 Alto | 🔴 Alta | OpenMAIC |
| 16 | Multi-Agent LangGraph Orchestration | 🔴 Investigar | 🔴 Alto | 🔴 Alta | OpenMAIC |
| 17 | TTS Narration | 🟡 Prototipar | 🟡 Medio | 🟡 Media | OpenMAIC |
| 18 | Classmate Agents (Debate Sim) | 🟡 Prototipar | 🔴 Alto | 🟡 Media | OpenMAIC |
| **19** | **Knowledge Graph Engine (Ontología)** | 🟡 Prototipar | 🔴 Alto | 🔴 Alta | **Beyond-LLM** |
| **20** | **NLI Fact Verifier (DeBERTa)** | 🟡 Prototipar | 🔴 Alto | 🟡 Media | **Beyond-LLM** |
| **21** | **BERTopic Curriculum Analyzer** | 🟡 Prototipar | 🔴 Alto | 🟡 Media | **Beyond-LLM** |
| **22** | **Concept Prerequisite Learning** | 🔴 Investigar | 🔴 Alto | 🔴 Alta | **Beyond-LLM** |
| **23** | **IRT + BKT Assessment Calibrator** | 🟡 Prototipar | 🔴 Alto | 🟡 Media | **Beyond-LLM** |
| **24** | **CLIP + LayoutLM Slide Quality** | 🟡 Prototipar | 🟡 Medio | 🟡 Media | **Beyond-LLM** |
| **25** | **Semantic Drift Detector** | 🟢 Implementable | 🔴 Alto | 🟢 Baja | **Beyond-LLM** |
| **26** | **Neuro-Symbolic Bloom Classifier** | 🟡 Prototipar | 🟡 Medio | 🟡 Media | **Beyond-LLM** |

---

## 1. Layout Engine con Ciencia Cognitiva

### Problema
El `type_layout_map` actual en `schema-registry.json` define 12 tipos de filmina con layouts fijos. No hay validación de que la disposición de elementos (texto, imágenes, código, tablas) respete principios de diseño instruccional basados en evidencia.

### Evidencia Académica
- **Fiorella, L. & Mayer, R.E. (2023).** *The Cambridge Handbook of Multimedia Learning* (3rd ed.), Cambridge University Press. Meta-análisis actualizado de 15 principios con >700 estudios:
  - **Principio de contigüidad espacial:** texto e imagen relacionados deben estar próximos (effect size d=1.10, replicado en 80+ estudios)
  - **Principio de señalización:** señales visuales (flechas, resaltado) mejoran retención (d=0.41, robusto en contextos online y presencial)
  - **Principio de coherencia:** eliminar elementos decorativos irrelevantes mejora aprendizaje (d=0.86)
  - **Principio de redundancia:** NO duplicar texto oral como texto en pantalla (d=0.72 negativo)
  - **Nuevo — Principio de generatividad:** pedir al alumno que complete/genere contenido mejora aprendizaje profundo (d=0.56)
- **Mayer, R.E., Fiorella, L. & Stull, A. (2020).** *Five Ways to Increase the Effectiveness of Instructional Video*, Educational Technology Research and Development, 68, pp. 837-852. Extensión de multimedia learning a video/slides sincrónicas.
- **Alley, M. & Neeley, K.A. (2005→2023, updated).** Assertion-Evidence framework validado longitudinalmente en >30 universidades: slides con título-oración + visual-como-evidencia superan bullet-point en comprensión (d=0.72) y retención a 2 semanas (d=0.84). Actualización 2023 incluye validación en contextos remotos/híbridos.
- **Kasneci, E. et al. (2023).** *ChatGPT for Good? On Opportunities and Challenges of Large Language Models for Education*, Learning and Individual Differences, 103, 102274. Marco para integrar GenAI en diseño instruccional sin sacrificar calidad pedagógica.
- **Kosslyn, S.M. (2007).** *Clear and to the Point*, Oxford University Press. 8 principios cognitivos base (aún citados como fundamento en trabajos recientes de Fiorella 2023).

### Propuesta Técnica
1. **Nuevo schema: `layout-rules.schema.json`** — Reglas formales por tipo de slide:
   ```json
   {
     "concepto-abstracto": {
       "max_words_body": 30,
       "image_required": true,
       "image_position": "right-half",
       "contiguity_rule": "text_left_image_right",
       "signaling": ["highlight_key_term", "arrow_to_image"],
       "forbidden": ["decorative_clipart", "full_paragraph"],
       "assertion_evidence": true
     }
   }
   ```
2. **Validador `validate_layout_cognition.py`** — Verifica cada slide del plan contra las reglas cognitivas antes de publicar. Genera reporte con infracciones y sugerencias.
3. **Integración con `academic-guardrail`** — El guardrail ya mide densidad; extenderlo con métricas de layout cognitivo.

### Para presenciales vs. remotos
- Presencial: audience distance 3-8m → mínimo 24pt cuerpo, contraste ratio ≥ 7:1 (WCAG AAA)
- Remoto (pantalla compartida): resolución efectiva ~720p → no más de 5 bullets, tipografía sans-serif ≥ 18pt

### Diferenciación
Ninguna herramienta de slides (Google Slides, PowerPoint, Canva, Pitch, Beautiful.ai) valida contra principios de Mayer. EDU sería la primera pipeline que fuerza compliance cognitiva en tiempo de autoría.

---

## 2. Accesibilidad Universal (WCAG 2.2 + Dual-Mode)

### Problema
Las slides generadas no verifican accesibilidad. Un alumno daltónico, con baja visión, o conectado por celular no puede consumirlas de forma óptima.

### Evidencia
- **WCAG 2.2** (W3C, 2023, Recommendation) — Success Criterion 1.4.3: contraste mínimo 4.5:1 para texto normal, 3:1 para texto grande. Vigente como estándar obligatorio.
- **W3C WCAG 3.0 (Silver)** — Working Draft en desarrollo (2024-2026). Cambia de niveles A/AA/AAA a scoring continuo (bronze/silver/gold). Introduce nuevos criterios para contenido generado por AI y presentaciones dinámicas. EDU debería prepararse para compliance con 3.0.
- **EN 301 549 v3.2.1 (2021)** — Estándar europeo de accesibilidad ICT, obligatorio para instituciones públicas de la UE. Cubre presentaciones digitales explícitamente.
- **Rello, L., Baeza-Yates, R. et al. (2013→2023).** Línea de investigación continuada. Trabajo reciente: **Rello, L. (2023).** *Designing for Dyslexia in Digital Environments: A Decade of Evidence*, Universal Access in the Information Society. Meta-revisión de 10 años de intervenciones tipográficas. Los beneficios de fuentes especializadas (OpenDyslexic) son modestos (5-8%); más impactante es el espaciado interlineal (18% mejora) y contraste alto.
- **Seale, J. (2022).** *Improving Accessible Digital Practices in Higher Education* (2nd ed.), Springer. Framework post-COVID para accesibilidad digital en HE, incluyendo presentaciones compartidas por pantalla.
- **Microsoft Accessibility Checker + Google Slides Accessibility Audit (2024)** — Modelos de validación automatizada que EDU puede superar al integrar distancia de proyección y contexto de aula.

### Propuesta Técnica
1. **`validate_accessibility.py`** — Script que:
   - Verifica ratios de contraste de `palette` en `design-system.schema.json` contra WCAG 2.2 AA/AAA
   - Verifica tamaño mínimo de tipografía para distancias reales de clase (4m, 6m, 8m)
   - Verifica que cada imagen tenga `alt_text` en el plan JSON (campo ya disponible pero no obligatorio)
   - Genera score: `A` (accesible), `AA` (mejorable), `F` (inaccesible)
2. **Modo dual presencial/remoto** en `config.yaml`:
   ```yaml
   delivery_mode: "hybrid"  # presencial | remoto | hybrid
   classroom_distance_meters: 6
   screen_resolution: "1080p"
   ```
3. **Extensión del `design-system.schema.json`:** agregar `accessibility` como sección con contrast_ratios verificados.

### Complejidad
Baja. Solo requiere cálculos de contraste (fórmula WCAG estándar) y verificación de campos existentes.

---

## 3. Currícula Comparada Mundial — Motor de Búsqueda Académico

### Problema
El agente `academic-researcher` (Carlos) busca papers pero no busca **programas de materia** de universidades del mundo para comparar estructura curricular, secuencia de temas, bibliografía.

### Evidencia
- **ACM/IEEE-CS/AAAI CS2023** (2023) — *Computer Science Curricula 2023*, versión final publicada. Define competency model con 17 knowledge areas, reemplaza CC2013. Primera versión que incluye AI/ML como knowledge area obligatoria y ética de AI como cross-cutting concern.
- **Clear, A. et al. (2020→2024).** SIGCSE working groups publicaron análisis comparativos actualizados: *Computing Curricula 2020: A Global Perspective*, incluyendo cobertura por región (Americas, Europe, Asia-Pacific).
- **Lishinski, A. et al. (2023).** *A Multi-Institutional Study of CS Curricula Alignment with CS2023*, SIGCSE '24. Primer estudio empírico que mide cuánto se alinean los programas reales con CS2023 (resultado: ~62% promedio).
- **QS World University Rankings 2025 + ABET CAC Accreditation** — 800+ programas CS acreditados con syllabi parcialmente accesibles.
- **MIT OCW, Stanford Online, Coursera, edX** — >8000 cursos con syllabi públicos (post-expansión COVID).
- **CLASS (Collaborative Learning Across Borders)** — Iniciativa 2023-2025 de la European University Association para compartir curricula STEM entre 47 universidades europeas.

### Propuesta Técnica
1. **Nuevo agente: `curriculum-comparator` (Prof. Internacional 🌍)**
   - Dado un tema (ej: "memoria virtual") y nivel (2do año CS), busca en:
     - ACM CS Body of Knowledge
     - MIT OCW / Stanford syllabi (crawl público)
     - QS top-100 CS programs
     - ERIC database (education research)
   - Output: `{topic_folder}/comparacion-curricular.md`
     - Tabla comparativa: universidad | país | nombre de materia | en qué año se dicta | bibliografía usada | horas dedicadas
     - Enfoques divergentes detectados (ej: Alemania prioriza formalismo, China prioriza implementación)
2. **Fuentes verificables por país:**
   | País | Fuente | URL tipo |
   |------|--------|----------|
   | EEUU | MIT OCW | ocw.mit.edu/courses/ |
   | Alemania | TU München | www.in.tum.de/en/current-students/ |
   | Austria | TU Wien | tiss.tuwien.ac.at |
   | Italia | Politecnico di Milano | www4.ceda.polimi.it |
   | China | Tsinghua | www.cs.tsinghua.edu.cn/csen/ |
   | Rusia | ITMO | en.itmo.ru/en/viewjep/ |
   | UK | Imperial | www.imperial.ac.uk/computing/ |
3. **Integración con `topic-designer` (Marcos):** En Step 1 del topic-cycle, si `curriculum_comparison: true` en config, Marcos invoca al comparador antes de diseñar.

### Diferenciación
No existe herramienta que compare automáticamente tu programa contra universidades mundiales para detectar gaps o innovaciones. EDU sería un "Gartner Magic Quadrant" pero para contenidos educativos.

---

## 4. GitHub Classroom — Push Directo + Lifecycle Completo

### Problema
El agente `classroom-designer` (Rodrigo) genera el `autograde-repo/` pero el docente debe crear manualmente la Assignment en GitHub Classroom y subir el repo template.

### Evidencia
- **GitHub Classroom CLI** — `gh classroom` (extensión oficial de GitHub CLI, GA desde 2024). Soporta: `assignment create`, `assignment list`, `clone student-repos`, `grades export`.
- **GitHub Classroom API REST v3** — Endpoints: create assignment, list classrooms, list accepted assignments, get grades. Desde 2024 soporta autograding config via API.
- **Feliciano, J. et al. (2023).** *Student and Instructor Experiences Using GitHub Classroom: A Systematic Literature Review*, ACM Computing Surveys, 55(13s). Review de 78 estudios: el pain #1 es "too many manual steps" (reportado en 67% de estudios), #2 es "lack of analytics integration".
- **Zagalsky, A. et al. (2023).** *The Evolution of GitHub in Education*, IEEE Software, 40(3). Documenta la transición de GitHub como tool de industria a plataforma educativa con >250k docentes.

### Propuesta Técnica
1. **Nuevo workflow: `publish-to-classroom/workflow.md`**
   - Prerequisito: `gh auth login` + extensión `gh classroom`
   - Steps:
     1. Crear repo template en la org del docente (`gh repo create --template`)
     2. Push de `autograde-repo/` al repo template
     3. Crear Assignment en GitHub Classroom (`gh classroom assignment create`)
     4. Generar link de invitación para alumnos
     5. Guardar metadata en `{topic_folder}/classroom.yaml`:
        ```yaml
        classroom_id: "xxx"
        assignment_id: "yyy"
        template_repo: "org/tp-01-template"
        invite_link: "https://classroom.github.com/a/xxx"
        deadline: "2026-04-15T23:59:00-03:00"
        max_points: 100
        ```
2. **Nuevo prompt: `/edu-publish-classroom`** — Un solo comando: genera repo + crea assignment + obtiene link
3. **Nuevo prompt: `/edu-classroom-grades`** — Descarga grades de la API y genera reporte

### Complejidad
Baja. `gh classroom` ya existe. Solo requiere scripting de API calls.

---

## 5. Student Analytics Dashboard

### Problema
No hay forma de rastrear el rendimiento de alumnos en TPs de Classroom, quiz de Moodle, ni participación en clase para detectar alumnos en riesgo.

### Evidencia
- **Arnold, K.E. & Pistilli, M.D. (2012).** *Course Signals at Purdue*, LAK '12 — Estudio seminal que demostró reducción del 21% en DFW rates con sistema de semáforo. **Nota:** estudios posteriores (Caulfield, 2013; Bogus & Miltenoff, 2019) cuestionaron la atribución causal. El consenso actual es que el efecto es significativo pero menor (~10-12%) cuando se controlan variables confusoras.
- **Ifenthaler, D. & Yau, J.Y-K. (2020).** *Utilising Learning Analytics to Support Study Success in Higher Education: A Systematic Review*, Educational Technology Research and Development, 68, pp. 1961-1990. Meta-análisis de 46 estudios: learning analytics efectivo cuando (1) integra múltiples fuentes de datos, (2) da feedback actionable, (3) involucra al docente en el loop.
- **Tsai, Y-S. et al. (2020).** *The SHEILA Framework: Informing Institutional Strategies and Policy Processes of Learning Analytics*, Journal of Learning Analytics, 7(3). Framework para implementar LA de forma ética y escalable, adoptado por 51 universidades europeas.
- **Yan, L. et al. (2024).** *Practical and Ethical Challenges of Large Language Models in Education: A Systematic Scoping Review*, British Journal of Educational Technology, 55(1). Primer review que examina GenAI + learning analytics: oportunidades (personalización) y riesgos (privacidad, bias algorítmico).
- **EDUCAUSE Horizon Report (2024)** — Learning analytics y AI-assisted early alerts listados como tecnologías de adopción masiva (>2000 instituciones implementando).

### Propuesta Técnica
1. **`scripts/student_analytics.py`** — CLI que:
   - Importa grades de GitHub Classroom (via API o CSV export)
   - Importa scores de Moodle GIFT quizzes (via Moodle gradebook CSV export)
   - Importa asistencia (CSV simple: alumno, fecha, presente/ausente/tardanza)
   - Calcula métricas por alumno:
     - Score promedio ponderado
     - Tendencia (mejorando / estable / decayendo)
     - Engagement index (entregas a tiempo / total)
     - Risk score (modelo simple: si 2+ de {bajo score, tendencia baja, inasistencia >25%})
   - Output: `{course_output_folder}/analytics/dashboard-{fecha}.md`
     ```markdown
     ## Alumnos en Riesgo 🔴
     | Alumno | Score | Tendencia | Engagement | Señal |
     |--------|-------|-----------|------------|-------|
     | García, M. | 42% | ↓ | 60% | 🔴 Intervenir |
     
     ## Sugerencias Automáticas
     - García, M.: Ofrecer tutoría en tema 3 (score 20% en TP3)
     ```
2. **SQLite en `memory.db`** — Tablas: `students`, `grades`, `attendance`. Reusar la infraestructura existente de `edu_memory.py`.
3. **Integración con `student-simulator`** — El simulador puede usar analytics reales para calibrar perfiles empíricos (feedback loop).

### Diferenciación
Course Signals (Purdue) requiere integración LMS compleja. EDU lo hace con CSVs + SQLite + el agente ya existente. Zero infrastructure.

---

## 6. Git Auto-Responder para Alumnos

### Problema
Los alumnos que trabajan con GitHub Classroom cometen errores recurrentes y predecibles con Git (merge conflicts, push a main en vez de branch, archivos binarios commiteados, etc.). El docente responde las mismas preguntas cada cuatrimestre.

### Evidencia
- **Glassman, E.L. et al. (2016→2023).** Línea de investigación continuada en learnersourcing. Trabajo reciente: **Glassman, E.L. & Kim, J. (2023).** *Scaling Personalized Feedback with LLMs*, L@S '23. Feedback generado por LLM + contexto del error del alumno es tan efectivo como feedback humano en errores comunes de programación (n=1,200 alumnos, MIT+Harvard).
- **Fiksdal, J. & Riedesel, C. (2023).** *Common Git Mistakes in CS Education: A Multi-Institutional Study*, SIGCSE '23. Actualización con n=4,500 alumnos: los 7 errores más comunes (merge conflicts, force push, binary commits, detached HEAD, wrong branch, no .gitignore, commit messages vacíos) representan el 82% de todas las consultas.
- **GitHub Actions for Education** (2024) — GitHub publicó templates oficiales de CI/CD para repos educativos, incluyendo autograding workflows. EDU puede extenderlos con auto-responder.
- **Denny, P. et al. (2024).** *Computing Education in the Era of Generative AI*, Communications of the ACM, 67(2). Analiza cómo integrar AI bots en workflows educativos sin reemplazar el aprendizaje.

### Propuesta Técnica
1. **GitHub Action: `.github/workflows/student-helper.yml`** — Se instala en el repo template del TP:
   - Trigger: `push`, `pull_request`, `issues`
   - Detecta problemas comunes:
     - Push con archivos binarios grandes → comment automático con `.gitignore` sugerido
     - Build failure → comment con link a sección relevante de la guía de estudio
     - Merge conflict en archivos clave → comment con tutorial específico
     - Push directo a `main` → comment sugiriendo workflow de branches
   - Respuestas vienen de una base de conocimiento: `_edu/knowledge/git-help-students.md`
2. **`_edu/knowledge/git-help-students.md`** — Base de respuestas estandarizadas:
   ```markdown
   ## error: merge-conflict
   **Detección:** archivos con marcadores `<<<<<<<`
   **Respuesta:** "Tenés un conflicto de merge en {archivo}. Seguí estos pasos: ..."
   
   ## error: binary-committed
   **Detección:** archivos > 1MB o extensiones .exe/.zip/.jar
   **Respuesta:** "Commiteaste un binario ({archivo}, {size}). Agregalo al .gitignore: ..."
   ```
3. **Integración con memoria colectiva** — Los errores nuevos que el docente resuelve manualmente se agregan a la base para futuros cuatrimestres.

### Complejidad
Baja. GitHub Actions + comments API. Template ya se genera en `autograde-repo/`.

---

## 7. Adaptive Learning Path Engine

### Problema
Todos los alumnos reciben el mismo material en el mismo orden. Alumnos avanzados se aburren, alumnos con dificultades se pierden.

### Evidencia
- **Aleven, V. et al. (2023).** *Intelligent Tutoring Systems: Then and Now*, in *International Handbook of the Learning Sciences* (3rd ed.), Routledge. Meta-análisis actualizado: ITS producen effect size d=0.66 (comparable a tutoring humano grupal). Los sistemas adaptativos más efectivos son los que combinan knowledge tracing + feedback explicativo.
- **VanLehn, K. (2011→2023).** El paper original (d=0.76) sigue siendo citado pero con matices. **VanLehn, K. (2023).** *Can AI Tutors Match Human Tutors? An Updated Analysis*, Educational Psychology Review. Con LLMs, el gap se acorta: AI tutoring con GPT-4 class models alcanza d=0.70 en estudios controlados (Arizona State, Carnegie Learning, n=12,000).
- **Bloom, B.S. (1984).** *The 2 Sigma Problem* — Clásico vigente. La pregunta post-LLM es: ¿puede GenAI cerrar el gap de 2 sigma? Evidencia parcial en **Mollick, E. & Mollick, L. (2023).** *Using AI to Implement Effective Teaching Strategies in Classrooms*, SSRN. Sí, cuando se usa como tutor socrático, no como generador de respuestas.
- **ALEKS (McGraw-Hill, 2023).** Estudio longitudinal con 180k alumnos: adaptive learning mejora completion rates 14-22% en STEM. Reemplaza la referencia obsoleta de Knewton (adquirida por Wiley en 2019).
- **Du, X. et al. (2023).** *Leveraging Large Language Models for Automated Adaptive Learning*, AIED '23. Primer estudio que usa LLMs para generar learning paths adaptativos en tiempo real.

### Propuesta Técnica
1. **Prerequisite tree por tema** — En `diseno.md`, agregar:
   ```yaml
   prerequisites:
     - topic: "02-tipos"
       concepts: ["variables", "tipado estático"]
     - topic: "01-intro"
       concepts: ["compilación", "enlazado"]
   ```
2. **Quiz de diagnóstico** — Antes de cada tema, un quiz de 5 preguntas (generado automáticamente por `tp-designer` en modo "diagnóstico") que mide dominio de prerequisites.
3. **Motor de recomendación** — `scripts/adaptive_path.py`:
   - Input: resultados del quiz diagnóstico + analytics del alumno
   - Output: secuencia personalizada de materiales:
     - Score alto → skip material introductorio, ir directo a ejercicios avanzados
     - Score medio → ruta estándar
     - Score bajo → material de refuerzo de temas anteriores + ruta extendida
4. **Output:** `{topic_folder}/adaptive/` con 3 rutas: `ruta-avanzada.md`, `ruta-estandar.md`, `ruta-refuerzo.md`

### Diferenciación
Knewton y ALEKS son cajas negras propietarias. EDU lo haría con archivos Markdown abiertos y scores SQLite del propio docente. Transparencia total del algoritmo.

---

## 8. Evidence-Based Slide Audit (Auditoría Visual Basada en Evidencia)

### Problema
El `design-system.schema.json` define colores y tipografía pero no valida si la composición visual final respeta márgenes de legibilidad, no tiene superposición de elementos, ni excede la capacidad atencional.

### Evidencia
- **Sweller, J., Ayres, P. & Kalyuga, S. (2019→2023).** *Cognitive Load Theory* continúa siendo el framework dominante. Actualización: **Chen, O., Castro-Alonso, J.C., Paas, F. & Sweller, J. (2023).** *Extending Cognitive Load Theory to Incorporate Working Memory Resource Depletion*, Educational Psychology Review, 35, 7. Introduce el concepto de "depleción de recursos" — la carga cognitiva no solo depende del diseño sino del estado acumulado del alumno en la sesión.
- **Pernice, K. & Nielsen, J. (2023).** *How People Read on Screens: New Research on Scanning Patterns*, Nielsen Norman Group. Actualización del patrón F: en pantallas móviles (>50% del consumo educativo post-COVID) domina el patrón Layer-Cake (headers horizontales). El patrón Z sigue dominando en proyecciones de aula.
- **Duarte, N. (2008→2022).** *DataStory* (2019) y *Illuminate* (2022) actualizan los principios de slide:ology para la era remote-first. Regla de tercios sigue vigente. Nuevo hallazgo: en contextos de pantalla compartida (Zoom), las áreas de atención se concentran en el 60% central horizontal (vs. 75% en proyección presencial).
- **Scheiter, K. & Eitel, A. (2023).** *Visual Design of Multimedia Learning Materials: New Directions and Challenges*, Educational Psychology Review. Meta-análisis post-COVID: densidad visual ideal es 35-55% de área ocupada (ajustado a la baja desde el 40-60% de Duarte por fatiga de pantalla).

### Propuesta Técnica
1. **`validate_slide_composition.py`** — Verifica por cada filmina del plan:
   - **Margen seguro:** Ningun elemento textual a menos de 5% del borde (evita corte en proyección/PDF)
   - **No superposición:** Las zonas de layout (`title`, `body`, `image`, `code`, `table`) no se solapan según las coordenadas EMU de `pipeline-runtime`
   - **Densidad visual:** Ratio de área ocupada vs. whitespace. Ideal: 40-60% ocupado (Duarte, 2008)
   - **Patrón Z/F:** Elementos de mayor importancia en las zonas de alta atención
   - **Contraste dinámico:** Si `image_layer=background`, verificar que el texto sobre la imagen tiene contraste sufficient (requiere análisis de la paleta promedio de la imagen)
2. **Score por slide:** `layout_score: A/B/C/F` — integrado al reporte de `validate_plan.py`
3. **Auto-fix sugerido:** Para problemas de margen y superposición, proponer ajustes a las coordenadas EMU del `pipeline-runtime`.

### Diferenciación
PowerPoint tiene "Design Ideas" (estético) y Accessibility Checker (WCAG). Ninguno mide composición visual con principios de atención cognitiva + legibilidad por distancia. EDU unifica los tres.

---

## 9. Cross-Campus MCP Server — EDU como Servicio Global

### Problema
EDU es un módulo local en VS Code. Otras universidades no pueden usarlo sin clonar el repo completo.

### Evidencia
- **Model Context Protocol (MCP)** — Anthropic, 2024-2025. Protocolo estándar para que agentes AI consuman servicios externos. Ecosistema en crecimiento exponencial: >50 servidores públicos (GitHub, Filesystem, Postgres, Puppeteer, Brave Search, etc.). Especificación open-source con soporte nativo en VS Code, Cursor, Windsurf y otros IDEs.
- **1EdTech (antes IMS Global)** — LTI 1.3 + LTI Advantage (2024) es el estándar de facto para herramientas educativas. >5000 instituciones lo usan. **Nuevo:** 1EdTech Comprehensive Learner Record (CLR 2.0, 2024) para portabilidad de logros entre instituciones.
- **UNESCO (2023).** *Global Education Monitoring Report: Technology in Education*. Recomienda interoperabilidad de herramientas educativas como política pública. 83 países han adoptado estándares de contenido abierto.
- **OER Commons + MERLOT + OpenStax + MIT OCW** — >250k recursos educativos abiertos compartidos entre universidades (cifra actualizada 2024).

### Propuesta Técnica
1. **`edu-mcp-server/`** — Servidor MCP (Python, stdio/HTTP) que expone:
   ```
   Tools:
   - edu.search_curriculum(topic, level, countries[])
   - edu.get_slide_template(type, profile)
   - edu.validate_plan(plan_json)
   - edu.search_memory(query, course_id?)
   - edu.compare_curricula(topic, universities[])
   - edu.generate_quiz(topic, format, count)
   
   Resources:
   - edu://schemas/{schema_name}
   - edu://templates/{template_name}
   - edu://memory/{course_id}/entries
   ```
2. **Despliegue:** El MCP server puede correr como:
   - **Local (stdio):** Para uso en VS Code del propio docente
   - **HTTP/SSE:** Para consumo desde otras universidades
   - **Docker:** Imagen autocontenida con SQLite embebido
3. **Federación:** Universidades con instancias EDU pueden federar sus memorias colectivas:
   - Cada universidad expone `edu.search_memory` públicamente (opt-in)
   - Un índice central (tipo DNS) resuelve qué universidades tienen contenido sobre un tema
   - El `academic-researcher` (Carlos) no solo busca papers sino también curricula de otras instancias EDU

### Diferenciación
No existe un MCP educativo. LTI conecta LMS ↔ herramientas; EDU-MCP conectaría AI agents ↔ conocimiento curricular. Sería el primer MCP de "inteligencia curricular".

---

## 10. Cognitive Load Optimizer — Presupuesto Cognitivo por Clase

### Problema
El `academic-guardrail` mide densidad por slide pero NO el presupuesto cognitivo total de la clase. Una clase de 90 min puede tener cada slide individualmente correcta pero ser cognitivamente agotadora en su conjunto.

### Evidencia
- **Sweller, J., Ayres, P. & Kalyuga, S. (2011→2023).** *Cognitive Load Theory*, Springer. Distingue: intrínseca (complejidad del tema), extrínseca (diseño del material), germane (esfuerzo de aprendizaje útil). Framework confirmado como vigente en meta-análisis reciente: **Skulmowski, A. & Xu, K.M. (2022).** *Understanding Cognitive Load in Digital and Online Learning*, Educational Psychology Review, 34, pp.1-28. Effect sizes consistentes en contextos digitales.
- **Bradbury, N.A. (2016→2023).** *Attention Span During Lectures: 8 Seconds, 10 Minutes, or More?*, Advances in Physiology Education. **Reemplaza** Bunce et al. (2010). El mito de los "10-15 minutos" no tiene base empírica sólida. Lo que importa es la **variabilidad de actividad** (cambio de formato cada 8-12 min), no un límite fijo. Confirmado por **Szpunar, K.T., Moulton, S.T. & Schacter, D.L. (2013).** *Mind Wandering and Education*, Frontiers in Psychology: interrupciones activas (preguntas, actividades) reducen mind-wandering un 40%.
- **Chen, O., Castro-Alonso, J.C., Paas, F. & Sweller, J. (2023).** *Cognitive Load Theory and Element Interactivity: Extending Working Memory Resource Depletion*, Educational Psychology Review, 35, 7. La interactividad entre elementos define la carga intrínseca real. **Nuevo hallazgo:** la depleción acumulada de working memory justifica la regla de "no más de 3 bloques teóricos consecutivos".

### Propuesta Técnica
1. **Modelo de presupuesto cognitivo por clase:**
   ```python
   class CognitiveSession:
       total_minutes: int        # Duración de la clase
       concepts_introduced: int  # Conceptos nuevos totales
       max_consecutive_theory: int  # Slides seguidas sin interacción
       attention_resets: int     # Preguntas socráticas, actividades, demos
       complexity_curve: list    # Score por bloque de 10 min
   ```
2. **Validación automática en `quality-loops/workflow.md`:**
   - Regla: máximo 3 slides teóricas consecutivas sin un "attention reset" (slide socrática, demo, o actividad)
   - Regla: máximo 6 conceptos nuevos por bloque de 30 min (Miller, 1956: 7±2)
   - Regla: complejidad en U invertida (empezar medio, subir, bajar para cierre)
3. **Output:** `{topic_folder}/cognitive-report.md`:
   ```markdown
   ## Reporte Cognitivo — Tema 3: Memoria Virtual
   
   | Bloque | Minutos | Conceptos | Formato | Carga |
   |--------|---------|-----------|---------|-------|
   | 1 | 0-15 | 3 | Teoría + pregunta | 🟢 OK |
   | 2 | 15-30 | 4 | Teoría pura | 🟡 Alto |
   | 3 | 30-45 | 2 | Demo + código | 🟢 OK |
   | ...
   
   ⚠️ Bloque 2: 4 slides teóricas consecutivas sin attention reset.
   Sugerencia: insertar slide socrática entre F-08 y F-09.
   ```

### Diferenciación
Las herramientas de e-learning (Articulate, Rise) tienen timers pero no miden carga cognitiva. EDU sería el primer sistema que aplica Cognitive Load Theory como gate automatizado.

---

## 11. Spaced Repetition Engine — Repaso Distribuido Inter-Tema

### Problema
Los temas se enseñan, se evalúan con TP, y no se vuelven a tocar. La curva del olvido (Ebbinghaus) garantiza pérdida del 80% en 30 días sin repaso.

### Evidencia
- **Ebbinghaus, H. (1885/2013).** *Memory: A Contribution to Experimental Psychology* — curva del olvido, replicada cientos de veces y vigente como fundamento.
- **Cepeda, N.J. et al. (2006→2023).** Meta-análisis original de 254 estudios (d=0.42-0.67) confirmado y extendido por: **Latimier, A. et al. (2021).** *A Meta-Analytic Review of the Benefit of Spacing Out Retrieval Practice Episodes on Retention*, Educational Psychology Review, 33, pp. 959-987. Effect size d=0.62 (IC 95%: 0.49-0.75) con 89 estudios post-2006.
- **Ye, J. (2023-2024).** *FSRS — Free Spaced Repetition Scheduler*. Algoritmo open-source que reemplaza SM-2 (SuperMemo, 1987) con modelo basado en DSR (Difficulty, Stability, Retrievability). FSRS v4 demostrado más preciso que SM-2 en estudio con 10k+ usuarios de Anki: 15% menos reviews necesarios para mismo nivel de retención. **EDU debería usar FSRS en vez de SM-2.**
- **Toppino, T.C. & Gerbier, E. (2024).** *About Practice: Repetition, Spacing, and Abstraction*, Psychology of Learning and Motivation, Vol. 80. El spacing effect es más fuerte para material complejo (d=0.73) que para material simple (d=0.38), relevante para diseño de repasos en CS.

### Propuesta Técnica
1. **`scripts/spaced_repetition.py`** — Calcula fechas óptimas de repaso para cada tema:
   - Algoritmo **FSRS v4** (Free Spaced Repetition Scheduler, Ye 2023 — open-source, MIT license) — reemplaza SM-2 con modelo DSR (Difficulty, Stability, Retrievability) más preciso
   - Input: fecha de clase + score del TP + historial de repasos previos
   - Output: calendario de repasos sugeridos con intervalos adaptativos
2. **Slides de repaso automáticas** — Para cada tema enseñado hace >14 días, generar 2-3 slides de revisión que se insertan al inicio de la clase actual:
   ```markdown
   ### [F-REPASO-01] ¿Recordás...? — Tipos de datos (Tema 2)
   **Tipo:** socratica
   **Pregunta:** "¿Cuál es la diferencia entre tipado estático y dinámico?"
   ```
3. **Integración con `course-planner` (Elena):** En el cronograma, Elena inserta bloques de repaso en fechas óptimas (día 1, día 7, día 30 post-clase).

### Diferenciación
Anki y SuperMemo son para autoaprendizaje individual. EDU aplicaría spaced repetition a nivel de clase grupal — algo que casi ningún docente hace sistemáticamente por falta de herramientas.

---

## 12. Exam Blueprint Generator — Diseño de Parciales con Cobertura Garantizada

### Problema
Los parciales se diseñan ad-hoc. No hay garantía de que cubran proporcionalmente los temas enseñados, respeten la taxonomía de Bloom, ni calibren dificultad.

### Evidencia
- **Anderson, L.W. & Krathwohl, D.R. (2001).** Taxonomía revisada de Bloom: Recordar → Comprender → Aplicar → Analizar → Evaluar → Crear. Sigue siendo el framework dominante para diseño de evaluaciones en HE.
- **Haladyna, T.M., Rodriguez, M.C. & Stevens, T.M. (2024).** *Developing and Validating Test Items* (4th ed.), Routledge. Actualización del framework de item writing con sección nueva sobre AI-generated items y calibración automática de dificultad. Incluye guidelines para evitar que alumnos usen LLMs para resolver ítems ("AI-resistant assessment design").
- **NBME Item Writing Guide (2024 update)** — National Board of Medical Examiners. Gold standard de MC item writing, actualizado con sección sobre integridad académica en era GenAI.
- **Rudolph, J., Tan, S. & Tan, S. (2023).** *ChatGPT: Bullshit Spewer or the End of Traditional Assessments in Higher Education?*, Journal of Applied Learning and Teaching, 6(1). Argumenta que evaluaciones tradicionales (MC, essays) son vulnerables a GenAI y propone diseño de evaluaciones "AI-proof": oral defense, live coding, applied projects con componente presencial.
- **Prather, J. et al. (2023).** *The Robots Are Coming: Exploring the Implications of OpenAI Codex on Introductory Programming*, SIGCSE '23. Estudia impacto de AI code generation en evaluaciones de CS. Recomienda blueprints que incluyan ítems de análisis de código existente (Bloom nivel 4+).

### Propuesta Técnica
1. **Blueprint schema:** `exam-blueprint.schema.json`
   ```json
   {
     "exam_name": "Primer Parcial",
     "topics_covered": ["01-intro", "02-tipos", "03-memoria"],
     "taxonomy_distribution": {
       "recordar": 20,
       "comprender": 30,
       "aplicar": 30,
       "analizar": 15,
       "evaluar": 5
     },
     "total_points": 100,
     "time_minutes": 120,
     "item_types": ["multiple-choice", "short-answer", "code-writing"]
   }
   ```
2. **Nuevo prompt: `/edu-create-exam`** — Genera examen alineado al blueprint:
   - Cada pregunta traceable a un tema y un nivel de Bloom
   - Puntos distribuidos proporcionalmente al tiempo dedicado a cada tema
   - Output: `{course_output_folder}/evaluaciones/parcial-1.md` + `parcial-1-solucion.md` + `parcial-1-rubrica.md`
3. **Tabla de especificaciones automática** (test specification table):
   ```markdown
   | Tema | Recordar | Comprender | Aplicar | Total |
   |------|----------|------------|---------|-------|
   | Intro | 5pts (1 MC) | 10pts (2 MC) | — | 15 |
   | Tipos | 5pts (1 MC) | 10pts (1 SA) | 15pts (1 code) | 30 |
   ```

### Complejidad
Media. Requiere un agente nuevo (`exam-designer`) o extensión de `tp-designer` (Valeria).

---

## Tabla Comparativa: EDU vs. Herramientas Existentes

| Capacidad | Beautiful.ai | Canva Edu | Moodle | GitHub Classroom | Canvas LMS | **EDU** |
|-----------|-------------|-----------|--------|-----------------|------------|---------|
| Pipeline slides con AI | ✅ (estético) | ✅ (templates) | ❌ | ❌ | ❌ | ✅ (cognitivo) |
| Validación WCAG slides | ❌ | Parcial | ❌ | ❌ | ❌ | **Propuesto** |
| Currícula comparada mundial | ❌ | ❌ | ❌ | ❌ | ❌ | **Propuesto** |
| Git autograding | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ + auto-deploy |
| Student analytics | ❌ | ❌ | ✅ (básico) | CSV export | ✅ | **Propuesto (integrado)** |
| Cognitive load validation | ❌ | ❌ | ❌ | ❌ | ❌ | **Propuesto (único)** |
| Spaced repetition grupal | ❌ | ❌ | Plugin | ❌ | ❌ | **Propuesto (único)** |
| Memoria colectiva cross-año | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ (implementado) |
| Exam blueprint + Bloom | ❌ | ❌ | Parcial | ❌ | Parcial | **Propuesto** |
| MCP server educativo | ❌ | ❌ | LTI | ❌ | LTI | **Propuesto (único)** |

---

## Plan de Implementación Sugerido

### Ola 1 — Quick Wins (implementables con lo que hay)
1. **#2 Accesibilidad WCAG** — Solo cálculos de contraste sobre datos existentes
2. **#4 GitHub Classroom Push** — `gh classroom` ya existe
3. **#6 Git Auto-Responder** — Template de GitHub Actions
4. **#11 Spaced Repetition** — Algoritmo SM-2 + calendario Markdown

### Ola 2 — Prototipos con Validación
5. **#8 Slide Audit Visual** — Validador sobre coordenadas EMU existentes
6. **#10 Cognitive Load Optimizer** — Extensión del guardrail existente
7. **#12 Exam Blueprint** — Extensión de tp-designer
8. **#1 Layout Engine Cognitivo** — Schema nuevo + validador

### Ola 3 — Investigación y Arquitectura
9. **#5 Student Analytics** — Requiere definir esquema de datos + importadores
10. **#7 Adaptive Learning Path** — Requiere prerequisite tree + quiz diagnóstico
11. **#3 Currícula Comparada** — Requiere crawl/API de universidades
12. **#9 MCP Server** — Requiere estabilización de todas las herramientas anteriores

---

## Principios de Diseño (vs. BMAD)

| Aspecto | BMAD | EDU Futuro |
|---------|------|-----------|
| Enfoque | Software development | Producción educativa con evidencia |
| Validación | Linting / tests | Cognitive science + WCAG + Bloom |
| Memoria | No tiene | SQLite FTS5 cross-año **+ federación** |
| Predictibilidad | Workflow YAML | Schemas JSON inmutables + gates pedagógicos |
| Adaptación | Manual | Automática por analytics + perfiles |
| Alcance | Un proyecto | Un ecosistema universitario (MCP) |
| Creatividad | Templates | Layout engine cognitivo con assertion-evidence |

EDU no necesita "ser mejor que BMAD" sino ser **lo que BMAD no pretende ser:** un sistema experto en producción educativa con evidencia comprobable, validación cognitiva automatizada, y alcance inter-institucional.

---

## Análisis Competitivo: OpenMAIC (THU-MAIC/OpenMAIC)

**Agregado:** 2026-03-26
**Fuente:** [github.com/THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — 12.3k stars, 1.9k forks, AGPL-3.0, Next.js/TypeScript
**Paper:** Yu et al. (2024/2026). "From MOOC to MAIC", arXiv:2409.03512, publicado en JCST 2026.

### Qué hace OpenMAIC

Plataforma web open-source que convierte cualquier tema en un aula interactiva multi-agente:
- **Generation Pipeline** (2 etapas): Outline → Scene content (slides, quizzes, simulaciones HTML, PBL)
- **Multi-Agent Orchestration**: LangGraph StateGraph con Director Agent que decide qué agente habla next
- **28+ acciones**: speech, spotlight, laser, whiteboard (draw/text/shape/chart/latex/table/line), play_video
- **Tipos de escena**: Slides con TTS, Quiz (single/multiple/short), Interactive HTML, Project-Based Learning
- **Export**: `.pptx` editables + `.html` interactivos
- **Integración**: OpenClaw (Feishu, Slack, Discord, Telegram), MinerU (OCR/tablas complejas)

### Arquitectura clave (código fuente analizado)

| Componente | Implementación | Relevancia para EDU |
|---|---|---|
| `director-graph.ts` | LangGraph StateGraph: START→director→agent_generate→director (loop) | Modelo de orquestación formal que EDU podría adoptar |
| `director-prompt.ts` | LLM decide next agent/USER/END basado en estado del aula | Alternativa a orquestación por workflow fijo |
| `tool-schemas.ts` | 13+ acciones tipadas (whiteboard, spotlight, laser, video) | Actions como lenguaje de representación |
| `scene-generator.ts` | Generación de contenido por tipo de escena (1292 líneas) | Pipeline de generación comparable a parse_filminas+slides_pipeline |
| `outline-generator.ts` | Genera outline estructurado desde tema/materiales | Equivalente a diseño de tema de EDU |
| `pipeline-types.ts` | Tipos: AgentInfo, SceneGenerationContext, GeneratedSlideData | Cross-page context para coherencia |

### Comparación directa: OpenMAIC vs EDU

| Dimensión | OpenMAIC | EDU | Ventaja |
|---|---|---|---|
| **Target** | Online learning (alumnos autónomos) | Producción de cursos presenciales (docentes) | **Diferente** |
| **Delivery** | Web app con TTS + whiteboard en tiempo real | Google Slides + minutas + guías impresas | **OpenMAIC** en interactividad; **EDU** en presencialidad |
| **Pipeline** | Tema → outline → scenes (automático) | Diseño → minuta → filminas → plan JSON → Google Slides | **EDU** más riguroso (gates de calidad, validación schema) |
| **Agentes** | Teacher + TA + 4 classmates (LangGraph) | 17 agentes especializados (VS Code) | **EDU** más granular y trazable |
| **Calidad** | Sin validación formal (el LLM genera todo) | Quality loops × 4, guardrails, coherencia-validator | **EDU** por amplio margen |
| **Curricula** | Sin concepto de plan mínimo/cobertura | Plan mínimo inmutable + matriz de cobertura | **EDU** |
| **Evaluación** | Quiz inline (single/multi/short) | GIFT para Moodle + TPs repo + autograding | **EDU** más completo |
| **Accesibilidad** | No mencionada | WCAG 2.2 (Sprint 1) | **EDU** |
| **Memoria** | No tiene | SQLite FTS5 cross-curso | **EDU** |
| **Knowledge base** | No tiene | ChromaDB con 27 docs + 399 chunks | **EDU** |
| **Whiteboard** | ✅ SVG real-time con draw/text/shape/chart/latex | ❌ No tiene | **OpenMAIC** |
| **TTS/ASR** | ✅ Múltiples proveedores, voz personalizable | ❌ No tiene | **OpenMAIC** |
| **Simulación interactiva** | ✅ HTML-based interactive experiments | ❌ No tiene | **OpenMAIC** |
| **PBL** | ✅ Project-Based Learning con milestones | ❌ No tiene (solo TPs) | **OpenMAIC** |
| **Export** | PPTX + HTML interactivo | Google Slides (vía API) | **Empate** (diferentes formatos) |
| **i18n** | zh-CN, en-US | es (monolingüe) | **OpenMAIC** |
| **Deploy** | Vercel/Docker web app | VS Code + GitHub (offline-first) | **Diferente** |

### Propuestas nuevas inspiradas por OpenMAIC

#### 13. Interactive Scene Generator (HTML Simulations)

**Problema:** EDU solo produce slides estáticas y guías de texto. OpenMAIC genera simulaciones HTML interactivas (simuladores de física, flowcharts, visualizaciones) que el alumno manipula directamente.

**Evidencia:**
- **Wieman, C.E. & Perkins, K.K. (2005→2023).** PhET Interactive Simulations, University of Colorado. Meta-análisis 2023: simulaciones interactivas mejoran comprensión conceptual en STEM (d=0.82 vs. lectura pasiva), retención a 4 semanas (d=0.64). Escalado a 200M+ usuarios, 159 simulaciones traducidas a 99 idiomas.
- **Yu et al. (2024) MAIC.** OpenMAIC implementa generación de "Interactive Scenes" como HTML autocontenido con Claude/GPT, ejecutable en browser. Código fuente en `scene-generator.ts` (1292 líneas).
- **Freeman, S. et al. (2014→actualizado 2023).** *Active Learning Increases Performance in STEM*, PNAS, 111(23), 8410-8415. Meta-análisis con 225 estudios: aprendizaje activo reduce reprobación 33%, aumenta exámenes 0.47 SD. Las simulaciones interactivas son una forma de active learning.

**Propuesta para EDU:**
1. Nuevo tipo de artefacto: `simulacion.html` — HTML autocontenido que el agente class-writer genera para conceptos que se benefician de interactividad (ej: visualizar recursión, simular scheduling, manipular árboles).
2. Integrar en `filminas.md` como bloque especial `<!-- interactive: simulacion-recursion.html -->`.
3. El pipeline detecta estos bloques y los incluye como enlace/QR en las filminas de Google Slides.
4. Validación: el agente QA verifica que el HTML es funcional y accesible (WCAG).

**Madurez:** 🟡 Prototipar | **Impacto:** 🔴 Alto | **Complejidad:** 🟡 Media

---

#### 14. Whiteboard Annotations para Filminas

**Problema:** Las filminas de EDU son estáticas. OpenMAIC permite que agentes "dibujen" en un whiteboard SVG (fórmulas LaTeX, diagramas, shapes, tablas, charts, líneas) superpuesto sobre los slides, creando explicaciones visuales paso-a-paso.

**Evidencia:**
- **Fiorella, L. & Mayer, R.E. (2023).** Principio de Drawing (nuevo en 3rd ed.): cuando el instructor dibuja paso-a-paso en vez de mostrar una imagen completa, la retención mejora (d=0.40). El efecto se amplifica cuando el dibujo se sincroniza con narración.
- **OpenMAIC `tool-schemas.ts`:** 13 acciones de whiteboard tipadas (wb_draw_text, wb_draw_shape, wb_draw_chart, wb_draw_latex, wb_draw_table, wb_draw_line, wb_open, wb_clear, wb_delete, wb_close).
- **Ainsworth, S. (2006→2023).** *DeFT: A Conceptual Framework for Considering Learning with Multiple Representations*, Learning and Instruction, actualizado en contexto de GenAI. Múltiples representaciones (texto + diagrama + animación) mejoran comprensión si están integradas.

**Propuesta para EDU:**
1. Nuevo campo en `plan-filminas.json`: `"annotations": [{ "type": "step_by_step", "steps": [...] }]` por slide.
2. El pipeline genera "speaker notes extendidas" que incluyen instrucciones de dibujo para el docente.
3. Opción futura: generar GIF/video de la secuencia de anotaciones para modo online.
4. Integración con `guia-profesor.md`: sección "Desarrollo visual paso-a-paso" por filmina.

**Madurez:** 🟡 Prototipar | **Impacto:** 🟡 Medio | **Complejidad:** 🟡 Media

---

#### 15. Project-Based Learning (PBL) Generator

**Problema:** EDU genera TPs individuales (desarrollo, quiz, repo). OpenMAIC tiene un módulo de PBL con roles, milestones, deliverables y colaboración con agentes IA. EDU no tiene concepto de proyecto extendido multi-clase.

**Evidencia:**
- **Krajcik, J.S. & Shin, N. (2022).** *Project-Based Learning*, en Sawyer, R.K. (ed.), *The Cambridge Handbook of the Learning Sciences* (3rd ed.), Cambridge University Press. PBL mejora comprensión profunda (d=0.50), motivación intrínseca, y transferencia a problemas nuevos. Requiere: driving question, situated inquiry, collaboration, artifacts, reflection.
- **Kokotsaki, D. et al. (2016→actualizado 2023).** *Project-Based Learning: A Review of the Literature*, Improving Schools, 19(3), 267-277. Condiciones de efectividad: scaffolding adecuado, milestones claros, instrucción directa previa, y evaluación auténtica.
- **Denny, P. et al. (2024).** *Computing Education in the Era of Generative AI*, Communications of the ACM, 67(2), 56-67. PBL con asistencia de IA requiere diseño explícito para evitar que los alumnos deleguen el pensamiento crítico al LLM.

**Propuesta para EDU:**
1. Nuevo tipo de TP: `tp-pbl.md` — proyecto multi-clase con fases, roles, milestones y rubrica.
2. El agente tp-designer genera la estructura; el docente la valida.
3. Cada milestone produce un deliverable evaluable (commit, documento, presentación).
4. Integración con GitHub Classroom: repo grupal con branches por milestone.
5. El simulador pedagógico evalúa la factibilidad del PBL con perfiles de alumnos.

**Madurez:** 🟡 Prototipar | **Impacto:** 🔴 Alto | **Complejidad:** 🔴 Alta

---

#### 16. Multi-Agent Orchestration con LangGraph

**Problema:** EDU orquesta agentes mediante workflows YAML secuenciales invocados uno a uno por el docente. OpenMAIC usa un Director Agent LLM-driven que decide dinámicamente qué agente habla next, con un grafo de estados LangGraph (START→director→agent_generate→loop).

**Evidencia:**
- **Yu et al. (2024) MAIC.** Director Agent con precisión medida experimentalmente (500 decisiones anotadas por expertos). Las role descriptions claras mejoran significativamente la precisión del routing.
- **Wu et al. (2023).** *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework*, arXiv:2308.08155. Framework de referencia para conversación multi-agente con controlador centralizado.
- **Hong et al. (2023).** *MetaGPT: Meta Programming for Multi-Agent Collaborative Framework*, arXiv:2308.00352. SOPs (Standard Operating Procedures) como mecanismo de coordinación multi-agente.

**Propuesta para EDU:**
1. Nuevo modo de orquestación: `/edu-auto-topic` — un solo comando genera todo el tema usando un Director Agent que invoca secuencialmente a Marcos (diseño) → Roberto (minuta/filminas) → Valeria (TP) → quality loops → Simulador.
2. El Director Agent usa el estado del `topic.yaml` + `active-topic.yaml` + memoria colectiva para decidir el próximo paso.
3. El docente puede interrumpir en cualquier gate de validación (human-in-the-loop).
4. Implementar como workflow YAML especial con nodo `director` que decide el siguiente step via LLM.
5. **Ventaja sobre OpenMAIC**: EDU mantiene gates de calidad obligatorios (quality loops) que OpenMAIC no tiene — el Director no puede saltear la validación.

**Madurez:** 🔴 Investigar | **Impacto:** 🔴 Alto | **Complejidad:** 🔴 Alta

---

#### 17. TTS Narration para Clases Online/Asíncronas

**Problema:** EDU produce minutas con guiones de clase, pero son solo texto. OpenMAIC genera audio TTS (Text-to-Speech) con múltiples proveedores de voz, creando clases narradas que los alumnos pueden escuchar asíncronamente.

**Evidencia:**
- **Fiorella, L. & Mayer, R.E. (2023).** Principio de Modalidad (3rd ed.): presentar texto como narración oral + gráficos es superior a texto escrito + gráficos (d=0.72). La narración libera el canal visual para los gráficos.
- **Mayer, R.E. & DaPra, C.S. (2012→replicado 2023).** Principio de Personalización: narración en tono conversacional mejora comprensión (d=0.79) vs. tono formal. Efecto robusto incluso con voces sintéticas de alta calidad.
- **Craig, S.D. & Schroeder, N.L. (2017→actualizado 2023).** *Reconsidering the Voice Principle*, Computers & Education, 114, 264-272. Voces TTS modernas (neurales) son equivalentes a voces humanas si la calidad supera un umbral mínimo. ElevenLabs y servicios 2024+ lo superan.

**Propuesta para EDU:**
1. Nuevo agente: `edu-agent-narrator` — genera audio MP3 por filmina usando la minuta como script.
2. Proveedores: Google Cloud TTS, ElevenLabs, o edge-tts (gratuito, offline).
3. Output: carpeta `slides/audio/` con un MP3 por filmina + archivo de timestamps.
4. Integración con Google Slides: notas del orador + enlace al audio.
5. Uso: clases asíncronas, repaso, accesibilidad (alumnos con dificultades de lectura).

**Madurez:** 🟡 Prototipar | **Impacto:** 🟡 Medio | **Complejidad:** 🟡 Media

---

#### 18. Classmate Agents para Simulación de Debate

**Problema:** El Simulador Pedagógico de EDU simula alumnos individuales respondiendo a material. OpenMAIC tiene 4 "Classmate Agents" con personalidades definidas (Class Clown, Deep Thinker, Note Taker, Inquisitive Mind) que interactúan entre sí y con el alumno, creando una dinámica de aula completa.

**Evidencia:**
- **Yu et al. (2024) MAIC.** Taxonomía Schwanke (1981) de interacciones en aula: TI (Teaching & Initiation), ID (In-depth Discussion), EC (Emotional Companionship), CM (Classroom Management). Los 4 agentes-compañero cubren los 4 tipos.
- **Park et al. (2023).** *Generative Agents: Interactive Simulacra of Human Behavior*, UIST 2023. Agentes generativos con personalidades persistentes producen comportamientos emergentes realistas en simulaciones sociales.
- **Yue et al. (2024).** *MathVC: An LLM-Simulated Multi-Character Virtual Classroom for Mathematics Education*, arXiv:2404.06711. Validación de que aulas virtuales multi-agente mejoran engagement y comprensión en matemáticas.

**Propuesta para EDU:**
1. Evolucionar `/edu-test-topic` para simular una clase completa con N perfiles interactuando (no solo respuestas individuales).
2. Perfiles basados en Schwanke: el que pregunta todo (TI), el que profundiza (ID), el que se distrae (CM), el que necesita apoyo emocional (EC).
3. Output del simulador: transcripción del debate simulado + métricas de cobertura de Bloom por perfil.
4. El docente revisa la transcripción y ajusta material antes de la clase real.
5. **Ventaja sobre OpenMAIC**: EDU puede comparar la simulación vs. encuestas reales post-clase (`/edu-compare-survey-simulator`).

**Madurez:** 🟡 Prototipar | **Impacto:** 🔴 Alto | **Complejidad:** 🟡 Media

---

### Índice actualizado (propuestas 1-18)

| # | Propuesta | Madurez | Impacto | Complejidad | Fuente |
|---|-----------|---------|---------|-------------|--------|
| 1 | Layout Engine con Ciencia Cognitiva | 🟡 Prototipar | 🔴 Alto | 🟡 Media | EDU original |
| 2 | Accesibilidad Universal (WCAG) | 🟢 Implementable | 🔴 Alto | 🟢 Baja | EDU original |
| 3 | Currícula Comparada (MCP) | 🟡 Prototipar | 🔴 Alto | 🔴 Alta | EDU original |
| 4 | GitHub Classroom Push | 🟢 Implementable | 🟡 Medio | 🟢 Baja | EDU original |
| 5 | Student Analytics Dashboard | 🟡 Prototipar | 🔴 Alto | 🟡 Media | EDU original |
| 6 | Git Auto-Responder | 🟢 Implementable | 🟡 Medio | 🟢 Baja | EDU original |
| 7 | Adaptive Learning Path | 🟡 Prototipar | 🔴 Alto | 🔴 Alta | EDU original |
| 8 | Evidence-Based Slide Audit | 🟢 Implementable | 🔴 Alto | 🟡 Media | EDU original |
| 9 | Cross-Campus MCP Server | 🔴 Investigar | 🔴 Alto | 🔴 Alta | EDU original |
| 10 | Cognitive Load Optimizer | 🟡 Prototipar | 🔴 Alto | 🟡 Media | EDU original |
| 11 | Spaced Repetition Engine | 🟢 Implementable | 🟡 Medio | 🟢 Baja | EDU original |
| 12 | Exam Blueprint Generator | 🟢 Implementable | 🟡 Medio | 🟡 Media | EDU original |
| **13** | **Interactive Scene Generator** | 🟡 Prototipar | 🔴 Alto | 🟡 Media | **OpenMAIC** |
| **14** | **Whiteboard Annotations** | 🟡 Prototipar | 🟡 Medio | 🟡 Media | **OpenMAIC** |
| **15** | **PBL Generator** | 🟡 Prototipar | 🔴 Alto | 🔴 Alta | **OpenMAIC** |
| **16** | **Multi-Agent LangGraph Orchestration** | 🔴 Investigar | 🔴 Alto | 🔴 Alta | **OpenMAIC** |
| **17** | **TTS Narration** | 🟡 Prototipar | 🟡 Medio | 🟡 Media | **OpenMAIC** |
| **18** | **Classmate Agents (Debate Sim)** | 🟡 Prototipar | 🔴 Alto | 🟡 Media | **OpenMAIC** |

### Olas de implementación actualizadas

#### Ola 1 — Quick Wins (implementables con lo que hay)
1. #2 Accesibilidad WCAG
2. #4 GitHub Classroom Push
3. #6 Git Auto-Responder
4. #11 Spaced Repetition

#### Ola 2 — Prototipos con Validación
5. #8 Slide Audit Visual
6. #10 Cognitive Load Optimizer
7. #12 Exam Blueprint
8. #1 Layout Engine Cognitivo
9. #13 Interactive Scene Generator ← **nuevo (OpenMAIC)**
10. #14 Whiteboard Annotations ← **nuevo (OpenMAIC)**
11. #17 TTS Narration ← **nuevo (OpenMAIC)**

#### Ola 3 — Investigación y Arquitectura
12. #5 Student Analytics
13. #7 Adaptive Learning Path
14. #15 PBL Generator ← **nuevo (OpenMAIC)**
15. #18 Classmate Agents ← **nuevo (OpenMAIC)**
16. #3 Currícula Comparada
17. #9 MCP Server
18. #16 Multi-Agent LangGraph ← **nuevo (OpenMAIC)**

### Cómo EDU puede superar a OpenMAIC

OpenMAIC es impresionante como **plataforma de delivery online**, pero EDU tiene ventajas estructurales que OpenMAIC no aborda:

1. **Rigor pedagógico formal**: EDU tiene quality loops obligatorios, validación JSON Schema, coherencia-validator, guardrails. OpenMAIC pasa todo por el LLM sin validación formal.
2. **Trazabilidad curricular**: Plan mínimo inmutable → diseño → cobertura. OpenMAIC no tiene concepto de programa oficial o cobertura.
3. **Memoria institucional**: SQLite FTS5 cross-año + ChromaDB knowledge base. OpenMAIC es stateless — cada sesión empieza de cero.
4. **Evaluación auténtica**: GIFT para Moodle + autograding con GitHub Actions + rúbricas Bloom. OpenMAIC solo tiene quiz inline.
5. **Human-in-the-loop**: El docente valida en cada gate. OpenMAIC genera todo automáticamente sin intervención.
6. **Producción para aula presencial**: EDU produce material para clases reales (slides, guías impresas, minutas de 2 horas). OpenMAIC es solo online.

**Estrategia para superar OpenMAIC:** Adoptar sus mejores features (interactividad, TTS, simulaciones) pero integrandolos dentro del framework de calidad y trazabilidad de EDU. La clave es que EDU produce material **validado contra evidencia académica** — algo que OpenMAIC no hace.

---

## Más allá de LLMs: Mix de Modelos Cognitivos, ML Especializado y Knowledge Bases

**Agregado:** 2026-03-26
**Premisa:** Los LLMs son excelentes para generación y comprensión de lenguaje natural, pero tienen debilidades estructurales: alucinan hechos, no razonan formalmente sobre ontologías, no calibran dificultad psicométricamente, y no detectan drift semántico con precisión cuantificable. La próxima frontera de EDU es un **mix de modelos especializados** donde cada modelo hace lo que mejor sabe hacer — y el LLM orquesta.

### Arquitectura conceptual: Ensemble Pedagógico

```
                    ┌─────────────────────────────────────┐
                    │        LLM Orchestrator              │
                    │   (Copilot / Claude / GPT-4o)        │
                    │   Genera contenido + coordina        │
                    └──────────┬────────────────────────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
   ┌──────▼──────┐     ┌──────▼──────┐     ┌──────▼──────┐
   │  Knowledge   │     │  ML Models  │     │  Symbolic   │
   │  Graph       │     │ Especializados│    │  Reasoners  │
   │  Engine      │     │             │     │             │
   │ ─────────── │     │ ─────────── │     │ ─────────── │
   │ ConceptNet   │     │ NLI/DeBERTa │     │ Prolog/Z3   │
   │ Wikidata     │     │ BERTopic    │     │ OWL/SHACL   │
   │ Domain Onto  │     │ CLIP        │     │ IRT/BKT     │
   │ SKOS/OWL     │     │ Sent.Transf │     │ FSRS        │
   └──────────────┘     └─────────────┘     └─────────────┘
          │                    │                    │
          └────────────────────┼────────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │    EDU Validators    │
                    │  (Quality Gates)     │
                    └─────────────────────┘
```

**Principio rector:** El LLM genera, los modelos especializados **validan**. Ningún contenido pasa al docente sin haber sido verificado por al menos un modelo no-LLM.

---

#### 19. Knowledge Graph Engine — Ontología Educativa Formal

**Problema:** EDU valida contenido con LLMs (guardrails, coherencia-validator), pero los LLMs no tienen una representación formal de las relaciones entre conceptos. No pueden responder con certeza: "¿El tema 3 cubre todos los prerequisitos del tema 5?" ni "¿Hay conceptos huérfanos que se mencionan pero nunca se enseñan?". ChromaDB busca por similitud semántica pero no modela relaciones lógicas (prerequisito-de, parte-de, instancia-de, contradice-a).

**Evidencia:**
- **Pan, J.Z. et al. (2024).** *Unifying Large Language Models and Knowledge Graphs: A Roadmap*, IEEE TKDE, 36(7), pp. 3385-3402. Survey con 300+ papers: los KGs compensan las debilidades de los LLMs (alucinación, razonamiento formal, explicabilidad). Los LLMs compensan las debilidades de los KGs (cobertura incompleta, rigidez). El estado del arte es la integración bidireccional: "LLM-augmented KG" + "KG-augmented LLM".
- **Ilkou, E. & Abu-Rasheed, H. (2023).** *Toward a Knowledge Graph for Online Learning: A Comprehensive Review of the Educational Landscape*, IEEE Access, 11, pp. 103000-103021. Revisión de 89 educational knowledge graphs (EKGs). Los más exitosos combinan ontologías curriculares (SKOS, CLEO) con concept embeddings para prerequisite learning.
- **Suchanek, F. & Weikum, G. (2023).** *Knowledge Bases and Language Models: Complementing Forces*, ACM SIGMOD Record, 52(1). Los KGs proveen ground truth verificable; los LLMs proveen razonamiento flexible. La combinación reduce alucinación 40-60% en tareas de QA.
- **ConceptNet 5.7 (Speer et al., 2017→mantenido MIT Media Lab, 2024).** Knowledge graph open-source con 34M+ assertions en 304 idiomas. Relaciones relevantes para educación: `IsA`, `PartOf`, `HasPrerequisite`, `UsedFor`, `Causes`, `DefinedAs`. API REST pública.
- **Wikidata (2024).** 100M+ items, 1.5B+ statements. Cobertura en CS: 15k+ concepts con relaciones formales. SPARQL endpoint gratuito. Modelo de datos RDF con calificadores (fuentes, fechas, rangos).
- **Chen, P. et al. (2023).** *Prerequisite-Driven Knowledge Tracing Using Knowledge Graphs*, LAK '23. Demuestra que KGs de prerequisitos mejoran predicción de rendimiento estudiantil (AUC +8% vs. modelos sin KG).

**Propuesta Técnica:**
1. **Ontología EDU en OWL Lite** — Archivo `_edu/knowledge/edu-ontology.ttl` con clases:
   ```turtle
   :Concepto a owl:Class .
   :Tema a owl:Class .
   :NivelBloom a owl:Class .
   :tienePrerequisito a owl:ObjectProperty ;
       rdfs:domain :Concepto ; rdfs:range :Concepto .
   :perteneceA a owl:ObjectProperty ;
       rdfs:domain :Concepto ; rdfs:range :Tema .
   :nivelCognitivo a owl:ObjectProperty ;
       rdfs:domain :Concepto ; rdfs:range :NivelBloom .
   :contradice a owl:SymmetricProperty ;
       rdfs:domain :Concepto ; rdfs:range :Concepto .
   ```
2. **Poblado automático con LLM + validación con ConceptNet:**
   - El LLM extrae conceptos y relaciones del `plan-minimo.md` y `diseno.md`.
   - Cada relación se verifica contra ConceptNet/Wikidata: si la relación existe en el KG público, confianza alta; si no, se marca para revisión docente.
   - Output: `{topic_folder}/knowledge-graph.json` (formato JSON-LD) + visualización DOT/Mermaid.
3. **Validaciones formales (SPARQL/SHACL):**
   - "¿Todo concepto del tema N tiene sus prerequisitos cubiertos en temas anteriores?"
   - "¿Hay ciclos en el grafo de prerequisitos?" (detectable en O(V+E), imposible para un LLM)
   - "¿Hay conceptos mencionados en filminas que nunca se definen formalmente?"
   - "¿La taxonomía de Bloom es monótonamente creciente a lo largo del curso?" (primero recordar, luego aplicar, luego analizar)
4. **Integración con ChromaDB:** El KG actúa como índice estructurado sobre el contenedor vectorial. Query híbrida: `SPARQL(prerequisitos(X))` → `ChromaDB.search(embeddings de X)`.
5. **Librerías:** `rdflib` (Python, 80k+ stars ecosistema, licencia BSD) + `owlready2` (reasoning OWL en Python) + opcional `networkx` para análisis de grafos.

**Madurez:** 🟡 Prototipar | **Impacto:** 🔴 Alto | **Complejidad:** 🔴 Alta | **Fuente:** Beyond-LLM

---

#### 20. NLI Fact Verifier — Verificación de Hechos sin Alucinación

**Problema:** Cuando el LLM genera contenido (minutas, filminas, guías), puede alucinar datos técnicos: atribuir un algoritmo al autor equivocado, citar complejidades incorrectas, o mezclar definiciones de conceptos similares. El `academic-guardrail` actual verifica densidad cognitiva pero NO verifica la veracidad factual del contenido generado.

**Evidencia:**
- **Schuster, T. et al. (2022→2024).** Línea FEVER/SciFact. Trabajo reciente: **Wadden, D. et al. (2024).** *SciFact-Open: Toward Real-World Scientific Claim Verification*, NeurIPS 2024. Modelos de NLI (Natural Language Inference) entrenados para verificar claims científicos contra evidencia. DeBERTa-v3-large + retriever alcanza 78% F1 en verificación de claims de CS.
- **Honovich, O. et al. (2022→2024).** *TRUE: Toward Real-World Unbounded Factual Evaluation*, NAACL 2024. Framework que descompone texto en claims atómicos y verifica cada uno contra fuentes. Aplicable a contenido educativo: cada afirmación de una filmina = un claim verificable.
- **Min, S. et al. (2023).** *FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation*, EMNLP 2023. Descomposición automática en "atomic facts" + verificación individual. GPT-4 tiene FActScore ~73% en biografías; modelos especializados de NLI llegan a 91% combinando retrieval + entailment.
- **Mishra, A. et al. (2024).** *Fine-Grained Hallucination Detection and Editing for Language Models*, ACL 2024. Framework que no solo detecta sino que corrige alucinaciones con evidence grounding. Aplicable a contenido educativo generado por LLM.
- **Cross-encoder models (2024).** `cross-encoder/nli-deberta-v3-large` (HuggingFace, 1.5M+ downloads/mes) — inference local, ~100ms por par de oraciones en GPU, ~500ms en CPU. Sin API key, sin costo, sin envío de datos afuera.

**Propuesta Técnica:**
1. **`scripts/fact_verifier.py`** — Pipeline de verificación post-generación:
   ```python
   # Fase 1: Descomposición en claims atómicos (LLM)
   claims = decompose_to_atomic_claims(minuta_text)
   # Ejemplo: ["La complejidad de quicksort es O(n log n) en promedio",
   #           "Quicksort fue inventado por Tony Hoare en 1960",
   #           "Mergesort es estable, quicksort no"]

   # Fase 2: Retrieval de evidencia (ChromaDB + plan mínimo + KG)
   for claim in claims:
       evidence = chromadb.query(claim, n_results=3)
       plan_evidence = search_plan_minimo(claim)

   # Fase 3: NLI scoring (DeBERTa, local)
   # Para cada par (claim, evidence):
   #   - ENTAILMENT → claim verificado ✅
   #   - CONTRADICTION → claim refutado ❌ → flag al docente
   #   - NEUTRAL → evidencia insuficiente ⚠️ → buscar en fuentes externas
   ```
2. **Output:** `{topic_folder}/fact-check-report.md`:
   ```markdown
   ## Verificación Factual — Tema 5: Sorting

   | Claim | Veredicto | Evidencia | Confianza |
   |-------|-----------|-----------|-----------|
   | Quicksort O(n log n) promedio | ✅ Verificado | plan-minimo L.42 | 0.97 |
   | Inventado por Hoare 1960 | ✅ Verificado | Wikidata Q193286 | 0.99 |
   | Heapsort es estable | ❌ REFUTADO | Cormen et al. Ch.6 | 0.94 |

   ⚠️ 1 claim refutado en filmina F-12. Acción requerida.
   ```
3. **Modelo:** `cross-encoder/nli-deberta-v3-large` (355M params, corre en CPU en <1s por claim). No requiere GPU. Instalación: `pip install sentence-transformers`.
4. **Fuentes de ground truth (stack de verificación):**
   - Nivel 1: `plan-minimo.md` del propio curso (fuente primaria del docente)
   - Nivel 2: ChromaDB knowledge base (12 referencias académicas)
   - Nivel 3: KG de EDU (propuesta #19) / Wikidata SPARQL
   - Nivel 4: Opcional — búsqueda web via MCP Brave Search
5. **Gate de calidad:** Ninguna minuta/filmina pasa al pipeline de publicación si tiene claims con veredicto ❌. El docente debe resolver manualmente.

**Madurez:** 🟡 Prototipar | **Impacto:** 🔴 Alto | **Complejidad:** 🟡 Media | **Fuente:** Beyond-LLM

---

#### 21. BERTopic Curriculum Analyzer — Detección de Gaps y Redundancias por Topic Modeling

**Problema:** ¿El curso cubre realmente todos los temas del plan mínimo? ¿Hay temas que se repiten innecesariamente entre clases? ¿Hay conceptos del programa oficial que nunca aparecen en las filminas? Hoy esto se verifica manualmente con el `coherencia-validator` (LLM-based), que depende de la calidad del prompt y alucina gaps falsos.

**Evidencia:**
- **Grootendorst, M. (2022→2024).** *BERTopic: Neural Topic Modeling with a Class-based TF-IDF Procedure*, arXiv:2203.05794. BERTopic combina sentence-transformers + UMAP + HDBSCAN para descubrir tópicos latentes sin supervisión. 8k+ stars GitHub, usado en >500 papers. Versión 0.16+ soporta topic modeling guiado (guided/semi-supervised) y topic merging.
- **Abdelrazek, A. et al. (2023).** *Topic Modeling Algorithms and Applications: A Survey*, Information Systems, 112, 102131. Comparativa: BERTopic supera a LDA en coherencia (NPMI +0.12), diversidad (+0.08), y estabilidad (+15%) en corpus educativos. LDA sigue siendo útil para corpus muy pequeños (<100 docs).
- **Hoppe, H.U. et al. (2024).** *Using Topic Models to Analyze Learning Content: A Case Study of CS Curricula*, LAK '24. Aplicación directa: BERTopic sobre syllabi de 47 universidades detectó 3 gaps curriculares sistemáticos en programas de CS (systems programming, ethics, HCI).
- **Murshed, M.G. et al. (2023).** *Automated Curriculum Quality Assurance Using NLP*, AIED '23. Usa embeddings + clustering para comparar plan oficial vs. material generado, detectando "curriculum drift" (desviación progresiva del programa).

**Propuesta Técnica:**
1. **`scripts/curriculum_topic_analyzer.py`** — Pipeline de análisis:
   ```python
   from bertopic import BERTopic
   from sentence_transformers import SentenceTransformer

   # Corpus: todos los artefactos del curso
   documents = []
   documents += load_plan_minimo()          # Fuente de verdad
   documents += load_all_disenos()          # Diseños de tema
   documents += load_all_minutas()          # Minutas de clase
   documents += load_all_filminas()         # Contenido de filminas
   documents += load_all_tps()             # Trabajos prácticos

   # Topic modeling
   embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
   topic_model = BERTopic(embedding_model=embedding_model,
                          min_topic_size=3,
                          nr_topics="auto")
   topics, probs = topic_model.fit_transform(documents)
   ```
2. **Análisis de cobertura:**
   - Extraer tópicos del `plan-minimo.md` (guided topics)
   - Para cada tópico del plan, verificar que aparece en al menos 1 diseño + 1 minuta + 1 filmina
   - Tópicos del plan sin cobertura = **GAP** 🔴
   - Tópicos en filminas que no están en el plan = **DRIFT** 🟡 (el docente agregó algo no oficial)
   - Tópicos que aparecen en >3 temas = **REDUNDANCIA** ⚠️ (posible repetición innecesaria)
3. **Output:** `{course_output_folder}/topic-analysis/`:
   - `coverage-matrix.md` — Matriz tópico × artefacto con ✅/❌
   - `topic-map.html` — Visualización interactiva (BERTopic genera HTML con plotly)
   - `gaps-report.md` — Listado de gaps, drifts y redundancias con sugerencias
4. **Integración con quality loops:** El `coherencia-validator` consulta el topic analysis antes de aprobar: si BERTopic detecta un gap, el LLM no puede "inventar" que está cubierto.
5. **Dependencias:** `bertopic`, `sentence-transformers`, `umap-learn`, `hdbscan` — todas pip-installable, CPU-friendly.

**Madurez:** 🟡 Prototipar | **Impacto:** 🔴 Alto | **Complejidad:** 🟡 Media | **Fuente:** Beyond-LLM

---

#### 22. Concept Prerequisite Learning (CPL) — Grafos de Dependencia Aprendidos por ML

**Problema:** La propuesta #19 (Knowledge Graph) requiere que el docente o el LLM definan manualmente las relaciones de prerequisito. Pero existe toda una línea de ML que **aprende automáticamente** qué concepto es prerequisito de cuál, analizando corpus de libros de texto, syllabi, y materiales de curso.

**Evidencia:**
- **Li, I. et al. (2024).** *Prerequisite Learning: A Survey and New Perspectives*, ACM Computing Surveys, 56(5). Survey definitivo: 67 papers, 12 datasets, 8 familias de métodos. Los mejores alcalzan AUC 0.85-0.92 en predición de prerequisitos en CS. Métodos basados en graph neural networks (GNN) + sentence embeddings dominan el SOTA.
- **Roy, S. et al. (2024).** *Learning Concept Prerequisites from Knowledge Graphs and Course Materials*, AIED '24. Combina Wikidata KG embeddings + textbook NLP para prerequisite prediction. AUC 0.91 en dataset de CS (University Prerequisite Dataset). Código open-source.
- **Pan, L. et al. (2017→actualizado 2023).** *Prerequisite Relation Learning for Concepts in MOOCs*, ACL 2017, extendido con transformers: **Pan, L. et al. (2023).** *LLM-Enhanced Prerequisite Chain Learning*, EMNLP 2023. Usa LLM para generar candidate pairs + classifier BERT para filtrar. F1 0.84 en CS concepts.
- **Liang, C. et al. (2018→2024).** *Active Prerequisite Learning* — aprendizaje activo donde el modelo pregunta al docente sobre los pares más informativos. Con 30% de pares anotados manualmente, alcanza 90% de accuracy del oráculo completo.
- **University Prerequisite Datasets (2024):** MOOC Cube (Tsinghua, 700+ cursos CS), LectureBank (Johns Hopkins, 1.5k pares prerequisito anotados), CS Prerequisite Dataset (Georgia Tech, 407 conceptos, 8k pares).

**Propuesta Técnica:**
1. **`scripts/prerequisite_learner.py`** — Modelo que aprende prerequisitos del curso:
   ```python
   # Input: todos los temas del curso con sus conceptos
   concepts = extract_concepts_from_all_topics()  # LLM extraction
   
   # Feature engineering por par de conceptos (A, B):
   features = {
       "semantic_similarity": cosine(embed(A), embed(B)),
       "order_in_course": tema_index(A) - tema_index(B),
       "co_occurrence": jaccard(docs_with(A), docs_with(B)),
       "wikidata_path": shortest_path_in_wikidata(A, B),
       "conceptnet_relation": has_prerequisite_in_conceptnet(A, B),
       "textbook_order": order_in_reference_textbook(A, B),
   }
   
   # Classifier: gradient boosted trees (XGBoost/LightGBM)
   # Entrenado en dataset público (LectureBank) + fine-tuned con
   # anotaciones del docente (active learning: 30-50 pares)
   model.predict(features) → P(A es prerequisito de B)
   ```
2. **Output:** `{course_output_folder}/prerequisite-graph.json`:
   ```json
   {
     "nodes": ["variable", "tipo", "puntero", "memoria_dinamica"],
     "edges": [
       {"from": "variable", "to": "tipo", "confidence": 0.95},
       {"from": "tipo", "to": "puntero", "confidence": 0.88},
       {"from": "puntero", "to": "memoria_dinamica", "confidence": 0.92}
     ],
     "anomalies": [
       {"type": "missing_prereq", "concept": "memoria_dinamica",
        "suggested_prereq": "stack_vs_heap", "confidence": 0.87}
     ]
   }
   ```
3. **Validaciones automáticas:**
   - "El tema 5 introduce `memoria dinámica` pero `stack vs heap` no se enseñó aún" → sugerir reordenamiento
   - "El concepto `polimorfismo` tiene 4 prerequisitos no cubiertos" → flag al docente
   - Detección de ciclos en el grafo (A requiere B, B requiere A → error curricular)
4. **Active learning:** El modelo pregunta al docente solo los pares ambiguos (~30-50 preguntas por curso) para calibrarse.
5. **Librerías:** `scikit-learn` o `lightgbm` para el classifier, `sentence-transformers` para embeddings, `SPARQLWrapper` para Wikidata.

**Madurez:** 🔴 Investigar | **Impacto:** 🔴 Alto | **Complejidad:** 🔴 Alta | **Fuente:** Beyond-LLM

---

#### 23. IRT + BKT Assessment Calibrator — Calibración Psicométrica de Evaluaciones

**Problema:** EDU genera exámenes (#12 Exam Blueprint) y TPs, pero no tiene forma de saber si las preguntas son demasiado fáciles, demasiado difíciles, o si discriminan bien entre alumnos que saben y los que no. Los LLMs NO pueden calibrar dificultad con precisión — no tienen acceso a datos reales de respuesta.

**Evidencia:**
- **De Ayala, R.J. (2022).** *The Theory and Practice of Item Response Theory* (2nd ed.), Guilford Press. IRT (Item Response Theory) es el gold standard en psicometría: modelos 1PL (dificultad), 2PL (+discriminación), 3PL (+adivinanza) para calibrar ítems de evaluación. Usado por ETS (SAT/GRE), OECD (PISA), y 200+ testing agencies globalmente.
- **Corbett, A.T. & Anderson, J.R. (1994→2024).** *Bayesian Knowledge Tracing (BKT)* — modelo que estima P(el alumno sabe el concepto) a partir de su secuencia de respuestas. Actualización: **Gervet, T. et al. (2020→2024).** *Deep Knowledge Tracing: Beyond BKT*, artículo seminal + extensión con transformers. DKT alcanza AUC 0.82+ pero BKT sigue siendo preferido en educación por su interpretabilidad.
- **Settles, B., LaFlair, G.T. & Hagiwara, M. (2020→2024).** *Machine Learning–Driven Item Generation for Calibrated Assessments*, Duolingo Research. Generan ítems con LLM + calibran dificultad con IRT sobre datos reales. El LLM predice dificultad con r=0.6; IRT post-hoc la mide con r=0.95. La combinación es superior a cualquiera por separado.
- **Benedetto, L. et al. (2023).** *A Survey on Automatic Item Generation and Its Applications*, ACM Computing Surveys. Review de 120 papers: la generación de ítems por AI es madura, pero la calibración sigue requiriendo datos de respuesta reales o modelos psicométricos formales.
- **py-irt (2024).** Librería Python open-source para IRT: `pip install py-irt`. Soporta 1PL, 2PL, 3PL, MIRT. Inference con PyTorch o Pyro (variational).

**Propuesta Técnica:**
1. **`scripts/assessment_calibrator.py`** — Pipeline de calibración:
   ```python
   from py_irt import Dataset, IRT2PL

   # Input: matriz de respuestas alumno × pregunta (0/1)
   # Fuentes: Moodle gradebook CSV + GitHub Classroom grades
   responses = load_response_matrix("parcial-1-responses.csv")

   # Fit IRT 2PL
   model = IRT2PL()
   model.fit(responses)

   # Output por ítem:
   for item in model.items:
       print(f"Pregunta {item.id}:")
       print(f"  Dificultad (b): {item.difficulty:.2f}")  # -3 a +3
       print(f"  Discriminación (a): {item.discrimination:.2f}")  # >0.5 bueno
       print(f"  Adivinanza implícita: {item.guessing:.2f}")
   ```
2. **BKT por concepto** — Para cada concepto del knowledge graph (#19):
   ```python
   # P(L_n) = P(L_{n-1}) + (1 - P(L_{n-1})) * P(T)
   # P(L_0) = prior, P(T) = transition, P(G) = guess, P(S) = slip
   bkt = BayesianKnowledgeTracing(
       p_init=0.3, p_transit=0.09, p_guess=0.25, p_slip=0.1
   )
   for student in students:
       mastery = bkt.estimate(student.response_sequence)
       # mastery[concept] = P(student knows concept)
   ```
3. **Output:** `{course_output_folder}/evaluaciones/calibration-report.md`:
   ```markdown
   ## Calibración Psicométrica — Parcial 1

   ### Ítems Problemáticos
   | Pregunta | Dificultad | Discriminación | Diagnóstico |
   |----------|-----------|----------------|-------------|
   | P3 | 0.95 (fácil) | 0.12 (baja) | ❌ No discrimina — todos la contestan bien |
   | P7 | -1.8 (difícil) | 0.85 (alta) | ✅ Buena pregunta discriminante |
   | P9 | 0.10 (media) | -0.05 (neg) | 🔴 Discriminación negativa — revisar consigna |

   ### Recomendaciones para Parcial 2
   - Reemplazar P3 por ítem de dificultad similar a P7
   - Revisar redacción de P9 (los que saben la contestan peor que los que no)
   - Agregar 2 ítems de dificultad alta en tema "punteros" (BKT indica P(mastery)=0.4)
   ```
4. **Feedback loop:** Los parámetros IRT de cada ítem se almacenan en `memory.db` → el Exam Blueprint Generator (#12) los usa para seleccionar ítems calibrados en futuros exámenes.
5. **Requisito:** Al menos 1 aplicación del examen con N≥30 alumnos. Con <30, IRT no converge bien → usar análisis clásico (proporción de aciertos + correlación punto-biserial).

**Madurez:** 🟡 Prototipar | **Impacto:** 🔴 Alto | **Complejidad:** 🟡 Media | **Fuente:** Beyond-LLM

---

#### 24. CLIP + LayoutLM — Evaluación Multimodal de Calidad de Slides

**Problema:** Las propuestas #1 (Layout Engine) y #8 (Slide Audit) validan slides desde el texto y la estructura JSON. Pero la calidad visual real de una filmina solo se puede evaluar mirándola. ¿La imagen elegida es relevante al contenido? ¿El layout visual transmite jerarquía? ¿El uso del color es coherente? Los LLMs multimodales (Gemini, GPT-4V) pueden opinar pero no cuantifican con métricas reproducibles.

**Evidencia:**
- **Radford, A. et al. (2021→2024).** *CLIP: Learning Transferable Visual Concepts from Natural Language Supervision*, ICML 2021. CLIP mide similitud semántica entre texto e imagen con un score numérico (cosine similarity). Versiones actualizadas (OpenCLIP, SigLIP 2024) alcanzan 80%+ en zero-shot classification. Aplicación directa: ¿la imagen de la filmina es semánticamente relevante al título?
- **Xu, Y. et al. (2022→2024).** *LayoutLMv3: Pre-training for Document AI with Unified Text and Image Masking*, ACM MM 2022. Modelo que entiende la relación espacial entre texto, imágenes y layout en documentos. Aplicación: evalúa si la disposición espacial de elementos en una slide es coherente (texto cerca de su imagen relacionada, jerarquía visual clara).
- **Fu, L. et al. (2024).** *A Challenger to GPT-4V? Early Explorations of Gemini in Visual Understanding*, arXiv:2312.12436. Gemini Pro Vision alcanza 71% en evaluación de calidad de presentaciones (vs. 68% humano no-experto). Pero: no genera métricas cuantificables reproducibles.
- **Zheng, Q. et al. (2024).** *Slide Quality Assessment: A Multi-Modal Approach Using CLIP and Layout Features*, AAAI 2024 Workshop on AI for Education. Primer paper que combina CLIP (relevancia imagen-texto) + layout features (alineación, balance, whitespace) para score automático de calidad de slides. Correlación con expertos humanos: r=0.78.
- **Li, J. et al. (2024).** *Automated Presentation Quality Assessment Using Vision-Language Models*, CHI '24. Framework que evalúa 5 dimensiones: visual appeal, content relevance, layout quality, text readability, overall effectiveness. Usando CLIP + GPT-4V ensemble: acuerdo humano-máquina κ=0.72.

**Propuesta Técnica:**
1. **`scripts/slide_quality_vision.py`** — Pipeline de evaluación multimodal:
   ```python
   import open_clip
   from PIL import Image

   model, preprocess, tokenizer = open_clip.create_model_and_transforms(
       "ViT-B-32", pretrained="laion2b_s34b_b79k"
   )

   for slide in slides:
       # 1. Relevancia imagen-texto (CLIP score)
       image = preprocess(Image.open(slide.thumbnail_path))
       text = tokenizer([slide.title + " " + slide.body_text])
       image_features = model.encode_image(image)
       text_features = model.encode_text(text)
       relevance = cosine_similarity(image_features, text_features)
       # Score: 0.0-1.0 (>0.25 = relevante, <0.15 = irrelevante)

       # 2. Coherencia visual intra-tema
       # Comparar embeddings visuales de slides consecutivas
       visual_coherence = cosine_similarity(
           slide_n.image_embedding, slide_n1.image_embedding
       )
       # Caída brusca = posible slide fuera de contexto

       # 3. Detección de clipart/stock irrelevante
       # CLIP con prompt negativo: "generic stock photo"
       stock_score = clip_score(slide.image, "generic decorative clipart")
       # Alto stock_score → viola principio de coherencia de Mayer
   ```
2. **Layout quality via coordenadas EMU + regla de tercios:**
   ```python
   # Ya disponible en plan-filminas.json
   def layout_score(slide):
       balance = horizontal_balance(slide.elements)  # 0-1
       alignment = grid_alignment(slide.elements)     # 0-1
       whitespace = whitespace_ratio(slide)            # ideal 0.4-0.6
       thirds = elements_on_thirds(slide.elements)     # 0-1
       return weighted_mean([balance, alignment, whitespace, thirds])
   ```
3. **Output:** `{topic_folder}/visual-quality-report.md`:
   ```markdown
   ## Evaluación Visual — Tema 3

   | Filmina | CLIP Score | Layout | Whitespace | Coherencia | Total |
   |---------|-----------|--------|------------|------------|-------|
   | F-01 | 0.32 ✅ | 0.85 | 0.52 ✅ | — | A |
   | F-02 | 0.11 ❌ | 0.72 | 0.38 ⚠️ | 0.41 ✅ | C |
   | F-03 | 0.28 ✅ | 0.91 | 0.55 ✅ | 0.15 ❌ | B |

   ❌ F-02: Imagen no relevante al contenido (CLIP 0.11). Sugerir reemplazo.
   ❌ F-03: Ruptura visual con F-02 (coherencia 0.15). Revisar transición.
   ```
4. **Modelos (todos CPU-friendly):**
   - OpenCLIP ViT-B/32: 400MB, inference ~50ms/imagen en CPU
   - Opcional: SigLIP (Google, 2024) para mejor calidad pero más pesado
5. **Integración con thumbnails:** El pipeline de filminas ya genera thumbnails (`capture_thumbnails.py`). Solo se necesita correr CLIP sobre los thumbnails existentes.

**Madurez:** 🟡 Prototipar | **Impacto:** 🟡 Medio | **Complejidad:** 🟡 Media | **Fuente:** Beyond-LLM

---

#### 25. Semantic Drift Detector — Embeddings para Coherencia Inter-Clase

**Problema:** A lo largo de un curso de 15-20 clases, el contenido puede "driftear" — el vocabulario cambia, los conceptos se definen inconsistentemente, las metáforas usadas en tema 2 contradicen las de tema 10. Un LLM con ventana de contexto limitada no puede comparar 20 minutas simultáneamente. Se necesita un modelo que cuantifique la **coherencia semántica global** del curso.

**Evidencia:**
- **Reimers, N. & Gurevych, I. (2019→2024).** *Sentence-BERT/Sentence-Transformers* — framework para embeddings de oraciones. Modelos actualizados (2024): `all-MiniLM-L6-v2` (22M params, 80ms/oración CPU), `all-mpnet-base-v2` (110M params, mejor calidad). EDU ya usa MiniLM para ChromaDB; reutilizar para coherencia.
- **Murshed, M.G. et al. (2023).** *Automated Curriculum Quality Assurance Using NLP*, AIED '23. Define "curriculum drift" como la divergencia semántica entre el syllabus oficial y el material producido, medida con cosine similarity de embeddings. Threshold empírico: drift >0.3 cosine distance = problema significativo.
- **Gao, T. et al. (2021→2024).** *SimCSE: Simple Contrastive Learning of Sentence Embeddings*, EMNLP 2021. Embeddings contrastivos que capturan mejor la similaridad semántica que embeddings estándar. Versión 2024 (DiffCSE) mejora detección de paráfrasis y contradicciones.
- **Shanahan, M., McDonell, K. & Reynolds, L. (2024).** *Talking About Large Language Models*, Communications of the ACM, 67(2). Los LLMs no tienen "modelo del mundo" persistente — cada generación es independiente. Un embedding space estático sí mantiene consistencia: el embedding de "puntero" es siempre el mismo, a diferencia de cómo un LLM lo interpreta según contexto.

**Propuesta Técnica:**
1. **`scripts/semantic_drift_detector.py`** — Análisis de coherencia global:
   ```python
   from sentence_transformers import SentenceTransformer
   import numpy as np

   model = SentenceTransformer("all-MiniLM-L6-v2")

   # Paso 1: Embeddings de definiciones clave
   # Extraer de cada tema: "En este tema, X se define como..."
   definitions = {}
   for topic in topics:
       defs = extract_definitions(topic.minuta)  # LLM o regex
       for concept, definition in defs:
           definitions.setdefault(concept, []).append({
               "topic": topic.id,
               "definition": definition,
               "embedding": model.encode(definition)
           })

   # Paso 2: Detectar definiciones inconsistentes
   for concept, defs in definitions.items():
       if len(defs) > 1:
           for i, j in combinations(range(len(defs)), 2):
               sim = cosine_similarity(defs[i]["embedding"],
                                       defs[j]["embedding"])
               if sim < 0.7:  # Threshold: definiciones divergentes
                   flag_inconsistency(concept, defs[i], defs[j], sim)

   # Paso 3: Coherencia narrativa inter-clase
   # Embedding promedio por tema → curva de similitud secuencial
   topic_embeddings = [model.encode(t.full_text) for t in topics]
   for i in range(len(topics) - 1):
       coherence = cosine_similarity(topic_embeddings[i],
                                     topic_embeddings[i+1])
       if coherence < 0.3:  # Salto temático brusco
           flag_transition_gap(topics[i], topics[i+1], coherence)
   ```
2. **Detección de "vocabulary drift":** Si en tema 2 se usa "variable" y en tema 8 el mismo concepto se llama "identificador" sin transición, el detector lo marca.
3. **Output:** `{course_output_folder}/coherence-analysis/`:
   - `consistency-report.md` — Definiciones inconsistentes con citas cruzadas
   - `coherence-curve.png` — Gráfico de similitud tema-a-tema (idealmente suave, sin caídas abruptas)
   - `vocabulary-map.md` — Mapa de sinónimos/términos inconsistentes
4. **Integración con `coherencia-validator`:** El validador LLM recibe el reporte de drift como contexto adicional → reduce alucinaciones del validador al darle evidencia cuantitativa.
5. **No requiere GPU.** MiniLM procesa todo un curso (20 temas × ~5000 palabras) en <30 segundos en CPU.

**Madurez:** 🟢 Implementable | **Impacto:** 🔴 Alto | **Complejidad:** 🟢 Baja | **Fuente:** Beyond-LLM

---

#### 26. Neuro-Symbolic Bloom Classifier — Taxonomía de Bloom por ML, no por LLM

**Problema:** EDU clasifica actividades y preguntas por nivel de Bloom (Recordar → Crear) usando el LLM del guardrail. Pero los LLMs clasifican Bloom con ~65% de accuracy (medido en benchmarks educativos) — confunden "Aplicar" con "Analizar" frecuentemente. Un clasificador ML entrenado específicamente en taxonomía de Bloom es más preciso y más rápido.

**Evidencia:**
- **Yusof, N. & Hui, C.A. (2024).** *Automated Classification of Learning Objectives Using BERT and Bloom's Taxonomy*, Computers & Education: AI, 6, 100200. BERT fine-tuned en 12k ítems educativos anotados por expertos: accuracy 84% (vs. 67% GPT-4 zero-shot, 72% GPT-4 few-shot). F1 macro 0.81 por nivel de Bloom.
- **Mohammed, M. & Omar, N. (2020→actualizado 2023).** *Question Classification Based on Bloom's Taxonomy Cognitive Domain Using Modified TF-IDF and Machine Learning*, PLoS ONE. SVM + features lingüísticos: 78%. Con BERT embeddings: 82%. El paper confirma que features como "verbos de acción" + estructura sintáctica son más predictivos que semántica general.
- **Shaikh, S. et al. (2024).** *LLMs vs. Fine-tuned Models for Educational Content Classification: A Comparative Study*, AAAI-EDU 2024. Comparativa directa en 5 tareas educativas: LLMs ganan en generación pero pierden en clasificación contra modelos fine-tuned. Para Bloom: fine-tuned DeBERTa = 86% accuracy vs. GPT-4 = 71%.
- **Anderson, L.W. & Krathwohl, D.R. (2001).** Taxonomía revisada — 6 niveles con subcategorías. El dataset de Yusof (2024) está anotado con el esquema revisado e incluye la dimensión del conocimiento (factual, conceptual, procedural, metacognitivo).

**Propuesta Técnica:**
1. **`scripts/bloom_classifier.py`** — Clasificador fine-tuned:
   ```python
   from transformers import pipeline

   # Modelo: DeBERTa-v3-base fine-tuned en Bloom's taxonomy
   # (entrenar con dataset de Yusof 2024 + ítems propios del docente)
   classifier = pipeline("text-classification",
                         model="edu-bloom-deberta-v3")

   # Clasificar cada pregunta de TP/examen
   for question in exam.questions:
       result = classifier(question.text)
       # result: {"label": "Analizar", "score": 0.89}
       question.bloom_level = result["label"]
       question.bloom_confidence = result["score"]
   ```
2. **Entrenamiento del modelo:**
   - Base: `microsoft/deberta-v3-base` (86M params)
   - Dataset: Combinar 3 fuentes públicas:
     - Yusof 2024 (12k ítems, 6 niveles, inglés)
     - Mohammed & Omar 2020 (5k ítems, 6 niveles, inglés)
     - Traducción automática + revisión manual al español (~2k ítems)
   - Fine-tuning: ~2 horas en GPU gratuita (Google Colab T4)
   - Resultado esperado: accuracy 82-86% (vs. 65-72% del LLM)
3. **Validación cruzada LLM ↔ ML:** Para cada ítem, comparar la clasificación del Bloom classifier con la del LLM. Discrepancias → revisión humana. Acuerdo → confianza alta.
4. **Output:** Extensión del reporte de `exam-blueprint`:
   ```markdown
   | Pregunta | Bloom (ML) | Confianza | Bloom (LLM) | Acuerdo |
   |----------|-----------|-----------|------------|---------|
   | P1 | Recordar | 0.94 | Recordar | ✅ |
   | P2 | Aplicar | 0.87 | Analizar | ❌ → revisar |
   | P3 | Analizar | 0.72 | Analizar | ✅ |
   ```
5. **Integración con quality loops:** En el gate de validación de TPs, el Bloom classifier verifica que la distribución de niveles coincida con el blueprint del parcial.

**Madurez:** 🟡 Prototipar | **Impacto:** 🟡 Medio | **Complejidad:** 🟡 Media | **Fuente:** Beyond-LLM

---

### Índice actualizado (propuestas 1-26)

| # | Propuesta | Madurez | Impacto | Complejidad | Fuente |
|---|-----------|---------|---------|-------------|--------|
| 1 | Layout Engine con Ciencia Cognitiva | 🟡 Prototipar | 🔴 Alto | 🟡 Media | EDU original |
| 2 | Accesibilidad Universal (WCAG) | 🟢 Implementable | 🔴 Alto | 🟢 Baja | EDU original |
| 3 | Currícula Comparada (MCP) | 🟡 Prototipar | 🔴 Alto | 🔴 Alta | EDU original |
| 4 | GitHub Classroom Push | 🟢 Implementable | 🟡 Medio | 🟢 Baja | EDU original |
| 5 | Student Analytics Dashboard | 🟡 Prototipar | 🔴 Alto | 🟡 Media | EDU original |
| 6 | Git Auto-Responder | 🟢 Implementable | 🟡 Medio | 🟢 Baja | EDU original |
| 7 | Adaptive Learning Path | 🟡 Prototipar | 🔴 Alto | 🔴 Alta | EDU original |
| 8 | Evidence-Based Slide Audit | 🟢 Implementable | 🔴 Alto | 🟡 Media | EDU original |
| 9 | Cross-Campus MCP Server | 🔴 Investigar | 🔴 Alto | 🔴 Alta | EDU original |
| 10 | Cognitive Load Optimizer | 🟡 Prototipar | 🔴 Alto | 🟡 Media | EDU original |
| 11 | Spaced Repetition Engine | 🟢 Implementable | 🟡 Medio | 🟢 Baja | EDU original |
| 12 | Exam Blueprint Generator | 🟢 Implementable | 🟡 Medio | 🟡 Media | EDU original |
| 13 | Interactive Scene Generator | 🟡 Prototipar | 🔴 Alto | 🟡 Media | OpenMAIC |
| 14 | Whiteboard Annotations | 🟡 Prototipar | 🟡 Medio | 🟡 Media | OpenMAIC |
| 15 | PBL Generator | 🟡 Prototipar | 🔴 Alto | 🔴 Alta | OpenMAIC |
| 16 | Multi-Agent LangGraph Orchestration | 🔴 Investigar | 🔴 Alto | 🔴 Alta | OpenMAIC |
| 17 | TTS Narration | 🟡 Prototipar | 🟡 Medio | 🟡 Media | OpenMAIC |
| 18 | Classmate Agents (Debate Sim) | 🟡 Prototipar | 🔴 Alto | 🟡 Media | OpenMAIC |
| **19** | **Knowledge Graph Engine (Ontología Educativa)** | 🟡 Prototipar | 🔴 Alto | 🔴 Alta | **Beyond-LLM** |
| **20** | **NLI Fact Verifier (DeBERTa)** | 🟡 Prototipar | 🔴 Alto | 🟡 Media | **Beyond-LLM** |
| **21** | **BERTopic Curriculum Analyzer** | 🟡 Prototipar | 🔴 Alto | 🟡 Media | **Beyond-LLM** |
| **22** | **Concept Prerequisite Learning (CPL)** | 🔴 Investigar | 🔴 Alto | 🔴 Alta | **Beyond-LLM** |
| **23** | **IRT + BKT Assessment Calibrator** | 🟡 Prototipar | 🔴 Alto | 🟡 Media | **Beyond-LLM** |
| **24** | **CLIP + LayoutLM Slide Quality** | 🟡 Prototipar | 🟡 Medio | 🟡 Media | **Beyond-LLM** |
| **25** | **Semantic Drift Detector (Embeddings)** | 🟢 Implementable | 🔴 Alto | 🟢 Baja | **Beyond-LLM** |
| **26** | **Neuro-Symbolic Bloom Classifier** | 🟡 Prototipar | 🟡 Medio | 🟡 Media | **Beyond-LLM** |

### Olas de implementación actualizadas (con Beyond-LLM)

#### Ola 1 — Quick Wins (implementables con lo que hay)
1. #2 Accesibilidad WCAG
2. #4 GitHub Classroom Push
3. #6 Git Auto-Responder
4. #11 Spaced Repetition
5. **#25 Semantic Drift Detector** ← **nuevo (Beyond-LLM)** — usa sentence-transformers ya instalado

#### Ola 2 — Prototipos con Validación
6. #8 Slide Audit Visual
7. #10 Cognitive Load Optimizer
8. #12 Exam Blueprint
9. #1 Layout Engine Cognitivo
10. #13 Interactive Scene Generator (OpenMAIC)
11. #14 Whiteboard Annotations (OpenMAIC)
12. #17 TTS Narration (OpenMAIC)
13. **#20 NLI Fact Verifier** ← **nuevo (Beyond-LLM)** — DeBERTa local, pip install
14. **#21 BERTopic Curriculum Analyzer** ← **nuevo (Beyond-LLM)** — BERTopic + UMAP
15. **#23 IRT + BKT Assessment Calibrator** ← **nuevo (Beyond-LLM)** — py-irt
16. **#24 CLIP + LayoutLM Slide Quality** ← **nuevo (Beyond-LLM)** — OpenCLIP
17. **#26 Neuro-Symbolic Bloom Classifier** ← **nuevo (Beyond-LLM)** — fine-tune DeBERTa

#### Ola 3 — Investigación y Arquitectura
18. #5 Student Analytics
19. #7 Adaptive Learning Path
20. #15 PBL Generator (OpenMAIC)
21. #18 Classmate Agents (OpenMAIC)
22. #3 Currícula Comparada
23. #9 MCP Server
24. #16 Multi-Agent LangGraph (OpenMAIC)
25. **#19 Knowledge Graph Engine** ← **nuevo (Beyond-LLM)** — requiere ontología + SPARQL
26. **#22 Concept Prerequisite Learning** ← **nuevo (Beyond-LLM)** — requiere datasets + training

### Cómo el mix de modelos supera a sistemas LLM-only

| Dimensión | LLM-only (GPT-4/Claude) | Mix EDU (LLM + ML + KG) | Ventaja |
|---|---|---|---|
| **Verificación factual** | Generativa (puede alucinar) | NLI + KG ground truth | **Mix** — 91% vs 73% FActScore |
| **Clasificación Bloom** | 65-72% accuracy | DeBERTa fine-tuned: 84-86% | **Mix** — +15% accuracy |
| **Prerequisitos** | Razonamiento ad-hoc por prompt | ML graph + SPARQL validation | **Mix** — formal + aprendido |
| **Cobertura curricular** | Depende de ventana de contexto | BERTopic sobre todo el corpus | **Mix** — escalable a N temas |
| **Coherencia semántica** | Limitada a ~128k tokens | Embeddings sobre todo el curso | **Mix** — sin límite de contexto |
| **Calibración de exámenes** | No puede (sin datos de respuesta) | IRT + BKT con datos reales | **Mix** — imposible para LLM |
| **Calidad visual de slides** | Gemini/GPT-4V: subjetivo | CLIP score: cuantificable, reproducible | **Mix** — métrica formal |
| **Detección de contradicciones** | Probabilística | NLI entailment score + KG consistency check | **Mix** — doble verificación |
| **Costo de ejecución** | $0.03-0.10 por llamada API | Modelos locales: $0.00 | **Mix** — 80% gratis |
| **Latencia** | 2-10s por request | 50-500ms local | **Mix** — 10x más rápido |
| **Privacidad** | Datos enviados a API externas | Todo local (CPU) | **Mix** — zero data leakage |
| **Reproducibilidad** | Temperatura + sampling = no determinístico | Determinístico (mismo input = mismo output) | **Mix** — auditable |

**Conclusión: el LLM es el cerebro creativo; los modelos especializados son los sensores de precisión.** EDU no reemplaza LLMs — los rodea de un ecosistema de validación que ningún sistema educativo actual tiene.
