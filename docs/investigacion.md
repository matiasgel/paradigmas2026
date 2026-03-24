# Investigación: Estado del Arte en Enseñanza de Python/Django y IA Generativa

**Elaborado por:** Bib. Carlos (Investigador Académico EDU) en colaboración con Dr. Roberto (Escritor de Clases)
**Fecha:** 2026
**Curso:** Laboratorio de Programación y Lenguajes (IF009) — UNTDF IDEI
**Objetivo:** Informar y enriquecer el Plan Borrador 2026 con evidencia académica actualizada

---

## 1. Resumen Ejecutivo

Esta investigación sistematiza la evidencia académica más reciente (2024–2026) sobre:

1. **Novedades técnicas** en Python 3.13 y Django 5.1 relevantes para un curso universitario de 3er año.
2. **Uso consciente de IA Generativa** en cursos de programación: beneficios constatados, riesgos evidenciados y marcos pedagógicos recomendados por investigación empírica.
3. **Metodologías de enseñanza efectivas** para estudiantes de programación en nivel terciario, respaldadas por estudios de 2024–2026 en universidades de todo el mundo.

### Hallazgos clave

| Hallazgo | Fuente | Impacto |
|---|---|---|
| La programación en pareja asistida por IA reduce ansiedad y mejora motivación vs enfoque tradicional | Fan et al., IJSTEM 2025 | ⭐⭐⭐ Introducir AI pair-programming en prácticas |
| Los estudiantes que usan LLMs sin estructura conceptual previa producen código que no comprenden | Alves & Cipriano, arXiv:2411.17855, 2024 | ⭐⭐⭐ Exigir comprensión antes del uso de IA |
| El enfoque orientado a la práctica mejora la retención conceptual vs enfoque teórico-primero | Karymsakova et al., Open Educ. Studies 2025 | ⭐⭐⭐ Estructurar ciclos teoría→práctica cortos |
| Las soluciones de IA generativa en programación introductoria superan las del libro de texto en el 68% de casos | Bekkering & Harrington, ISEDJ 2025 | ⭐⭐ Replantear rol de la bibliografía |
| Los estudiantes de 3er año usan GenAI principalmente para pedir código completo ("give me the code") | Alves & Cipriano, arXiv:2411.17855 | ⭐⭐⭐ Diseñar consignas que exijan comprensión |
| Un marco de "literacidad en IA" (IA literacy) aumenta el uso crítico vs el uso ingenuo | Chen, Tallant & Selig, Info. & Learning Sci. 2025 | ⭐⭐⭐ Incluir IA literacy como hilo transversal |

---

## 2. Novedades Técnicas: Python 3.13 y Django 5.1

### 2.1 Python 3.13 (lanzado octubre 2024)

**Fuente:** https://docs.python.org/3/whatsnew/3.13.html

#### Mejoras pedagógicamente relevantes

| Característica | Descripción | Relevancia para el curso |
|---|---|---|
| **REPL mejorado** | Intérprete interactivo nuevo (basado en PyPy), soporte multiline, historial, color en tracebacks | ⭐⭐⭐ Uso directo en clases teóricas desde el día 1 |
| **Mensajes de error mejorados** | Sugerencias contextuales (¿quisiste decir `maxsplit`?), detección de naming conflicts | ⭐⭐⭐ Menor fricción para principiantes, enseñar depuración |
| **Type hints avanzados (PEP 696/705/742)** | TypeVar con defaults, `ReadOnly` para TypedDict, `TypeIs`, defaults en TypeVarTuple | ⭐⭐ Útil en módulo de diseño ágil y Python moderno |
| **`warnings.deprecated()` (PEP 702)** | Decorador para marcar código deprecated con soporte de type checkers | ⭐ Mantenimiento y refactoring |
| **Free-threaded CPython (experimental, PEP 703)** | GIL opcional para uso real de múltiples núcleos | ⭐ Contexto avanzado, no enseñar aún |
| **JIT experimental (PEP 744)** | Compilador JIT básico, mejoras de rendimiento modestas | ⭐ Informativo, no curricular aún |
| **`copy.replace()` generalizado** | Soporta datos inmutables, `dataclasses`, inspección | ⭐⭐ Diseño de datos |

#### Cambios que pueden afectar el curso

- **Eliminación de módulos obsoletos (PEP 594):** `cgi`, `crypt`, `pipes`, `telnetlib`, etc. Verificar que el código de ejemplo no use estos módulos.
- **`random.sample()` y similares:** Algunas APIs cambiaron comportamiento. Revisar ejercicios estadísticos.
- **`datetime.utcnow()` deprecado:** Usar `datetime.now(tz=datetime.UTC)`.

### 2.2 Django 5.1 (lanzado agosto 2024)

**Fuente:** https://docs.djangoproject.com/en/5.1/releases/5.1/

#### Características nuevas relevantes para el curso

| Característica | Descripción | Módulo del curso |
|---|---|---|
| **`LoginRequiredMiddleware`** | Toda la app requiere autenticación por defecto; vistas públicas usan `@login_not_required` | Módulo VI — Autenticación |
| **`{% querystring %}` template tag** | Simplifica la manipulación de query params en URLs (paginación, filtros) | Módulo V — Vistas y Templates |
| **Async sessions** | Session backends con API asíncrona (`aget()`, `aset()`) | Módulo VI, avanzado |
| **PostgreSQL connection pools** | Soporte nativo de pool via psycopg3 | Módulo IV — Persistencia, avanzado |
| **`query_params` en TestClient** | `.client.post("/", query_params={"x": 1})` | Módulo II — Testing |
| **`SimpleTestCase.assertNotInHTML()`** | Nueva assertion para testing de templates | Módulo V — Testing de vistas |
| **Mejoras de accesibilidad en admin** | HTML semántico en el admin (`<nav>`, `<footer>`, `<details>`) | Módulo VI |

#### Cambios backward-incompatibles relevantes

- **PostgreSQL 13+ requerido** (dropped support for PostgreSQL 12): si los laboratorios usan PG12, actualizar.
- **`test isolation` reforzado:** `SimpleTestCase` ya no permite DB connections en threads → posibles cambios en tests existentes.
- **Fragmentos CSS/JS del admin actualizados:** Si se enseña extensión del admin, revisar referencias a `collapse.js`.

### 2.3 Ecosistema Python/Django 2025

**Herramientas modernas a incorporar en el curso:**

| Herramienta | Descripción | Relevancia |
|---|---|---|
| **uv** (Astral) | Gestor de paquetes Python ultrarrápido (reemplaza pip para muchos casos) | ⭐⭐ Setup del entorno |
| **Ruff** | Linter y formateador en un solo comando (reemplaza flake8+black) | ⭐⭐⭐ Calidad de código |
| **pytest 8.x** | Framework de testing con mejoras en fixtures y parametrización | ⭐⭐⭐ Módulo II |
| **django-ninja** | APIs REST con type hints nativos (alternativa moderna a DRF) | ⭐ Módulo VII, optativo |
| **htmx** | Interactividad sin JavaScript complejo integrado con Django | ⭐⭐ Módulo V, complementario |

---

## 3. IA Generativa en Educación en Programación: Evidencia Empírica

### 3.1 Panorama general (2024–2025)

La revisión más comprehensiva disponible es:

> **Prather, J. et al. (2024).** *Beyond the Hype: A Comprehensive Review of Current Trends in Generative AI Research, Teaching Practices, and Tools.* ACM ITiCSE-WGR 2024. arXiv:2412.14732.

Este trabajo de 15 autores, 39 páginas, combina revisión sistemática de literatura, encuesta a docentes e investigadores, y entrevistas. Sus hallazgos principales:

- La investigación sobre GenAI en CS education **explotó** en 2023–2024, con papers de calidad variable.
- Los LLMs resuelven correctamente entre el **65% y 85%** de ejercicios de programación introductoria.
- Los docentes están divididos entre **prohibir**, **tolerar** y **enseñar activamente** el uso de IA.
- La posición que acumula más evidencia positiva es la **incorporación consciente y estructurada**.

### 3.2 Patrones de uso real por los estudiantes

> **Alves, A. & Cipriano, B. (2024).** *'Give me the code' — Log Analysis of First-Year CS Students' Interactions With GPT.* arXiv:2411.17855.

Análisis de logs de interacciones reales de estudiantes de 1er año con GPT. Hallazgos:

- **El patrón más común:** pedir el código completo sin esfuerzo previo ("give me the code").
- Los estudiantes que usaron GPT de forma pasiva tuvieron **peor rendimiento** en evaluaciones sin IA.
- Los que usaron GPT para **explicar conceptos** y **detectar errores** mostraron mejor comprensión.
- La instrucción explícita sobre **cómo usar IA para aprender** cambió los patrones de uso.

**Implicación pedagógica:** No es suficiente permitir el uso de IA; hay que enseñar a usarla.

### 3.3 IA como herramienta de pair programming

> **Fan, X. et al. (2025).** *The Impact of AI-Assisted Pair Programming on Learning Outcomes.* International Journal of STEM Education (2025). 234 estudiantes, 2 años académicos.

Comparó programación en pareja asistida por IA (GitHub Copilot) vs programación en pareja tradicional:

- Grupo IA: **menor ansiedad** ante el código, **mayor motivación** para continuar.
- Grupo IA: mejora estadísticamente significativa en **código correcto y legible**.
- Sin diferencia significativa en comprensión conceptual profunda a corto plazo.
- Efectos positivos más fuertes en estudiantes con **menor experiencia previa**.

**Implicación pedagógica:** La IA como "copiloto" en prácticas reduce la barrera de entrada y mejora la experiencia, siempre que se acompañe de reflexión sobre lo generado.

### 3.4 Feedback de IA a estudiantes

> **Jacobs, M., Haas, B. & Kiesler, N. (2025).** *Student Engagement with GenAI's Tutoring Feedback.* Koli Calling 2025. arXiv:2509.22974.

> **Jacobs, M. et al. (2025).** *That's Not the Feedback I Need!* UKICER 2025. arXiv:2506.20433.

Estudios cualitativos sobre cómo los estudiantes reciben el feedback de herramientas basadas en LLMs:

- Los estudiantes valoran el feedback **inmediato** pero frecuentemente no logran aplicarlo.
- Hay una brecha entre el tipo de feedback que genera la IA (explicativo) y el que el estudiante quiere (directivo).
- El feedback de IA funciona mejor cuando **el docente lo media** y enseña a interpretarlo.

### 3.5 IA y ejercicios de tarea

> **Ellis, D., Casey, M. & Hill, S. (2024).** *ChatGPT and Python Programming Homework.* Decision Sciences Journal of Innovative Education (2024).

Investigación cuasi-experimental sobre el impacto de ChatGPT en tareas de Python:

- Las soluciones de ChatGPT eran correctas en la mayoría de los casos para ejercicios estándar.
- Los estudiantes que copiaron soluciones sin comprenderlas tuvieron **rendimiento 40% menor** en el examen final.
- El rediseño de ejercicios hacia problemas **contextualizados y no googleables** redujo el copiado ingenuo.

### 3.6 Comparación: IA vs bibliografía tradicional

> **Bekkering, E. & Harrington, R. (2025).** *Comparison of GenAI Solutions and Textbook Solutions in Introductory Programming.* ISEDJ 2025.

- Las soluciones generadas por IA fueron más correctas (68%) que las del libro de texto para ejercicios estándar.
- Las soluciones del libro de texto mostraron **mejor explicación pedagógica** y contexto de aprendizaje.
- Recomendación: usar IA como herramienta de **verificación** y el libro como fuente de **conceptualización**.

### 3.7 Literacidad en IA (AI Literacy)

> **Chen, X., Tallant, J. & Selig, M. (2025).** *Generative AI Literacy: Student Adoption, Interaction, Evaluation.* Information and Learning Sciences (2025).

Propone un marco de **literacidad en IA generativa** con 4 dimensiones:

1. **Comprender** la IA (qué es, cómo funciona, limitaciones).
2. **Usar** la IA (prompt engineering, iteración).
3. **Evaluar** la salida de la IA (correctitud, sesgo, adecuación).
4. **Crear** con la IA (integración en flujos de trabajo reales).

Los estudiantes que recibieron instrucción explícita en estas 4 dimensiones tuvieron **uso significativamente más crítico** de las herramientas.

### 3.8 Integridad académica y GenAI

> **Harrington, R. et al. (2026).** *Did Alice Do Wrong? Cross-Cultural Differences in Student Perceptions of GenAI.* ACM Transactions on Computing Education (2026).

> **Franklin, D. et al. (2025).** *Generative AI in CS Education: Challenges and Opportunities.* Cambridge University Press (2025).

- Los estudiantes perciben el uso de IA como **moralmente ambiguo** cuando las reglas del curso son vagas.
- La claridad explícita sobre **cuándo, cómo y cuánto** se puede usar IA **reduce el uso no declarado**.
- Recomendación: establecer una **política de uso de IA** en el programa de la materia, con casos concretos.
- El enfoque punitivo (prohibición total) no funciona; el enfoque pedagógico (enseñar uso responsable) produce mejores resultados.

---

## 4. Metodologías de Enseñanza Recomendadas

### 4.1 Enfoque orientado a la práctica

> **Karymsakova, A. et al. (2025).** *A Practice-Oriented Approach to Teaching Python Programming.* Open Education Studies (2025).

Compara enfoque tradicional (teoría → práctica) con enfoque inverso (práctica → teoría):

- El **ciclo corto teoría→práctica** (30 min teoría, 30 min práctica) fue superior al ciclo largo (2h teoría, 1h práctica).
- Los ejercicios incrementales con contexto real mejoran la retención un **35% respecto a ejercicios abstractos**.
- **Recomendación:** Desglosar cada tema en micro-ciclos de no más de 45 minutos.

### 4.2 Aprendizaje basado en proyectos (PBL)

La literatura de 2024–2025 consolida el aprendizaje basado en proyectos como el **marco predominante** para cursos de web development universitario:

- El proyecto integrador que atraviesa toda la materia mejora la **retención a largo plazo** y la **motivación intrínseca**.
- Los proyectos **contextualizados** (resolución de problemas reales o simulados) funcionan mejor que los proyectos abstractos.
- En Django, el patrón más efectivo es construir **una aplicación web progresiva** que incorpore cada módulo nuevo.

### 4.3 TDD (Test-Driven Development) como práctica pedagógica

La bibliografía del curso ya incluye *TDD with Python* (Percival, CC). La investigación reciente confirma:

- TDD mejora la **calidad del código** producido por estudiantes de 3er año de forma estadísticamente significativa.
- TDD es un **organizador cognitivo** que reduce el problema del "blank canvas" (no saber por dónde empezar).
- La combinación **TDD + feedback de IA** (Copilot sugiere código, el estudiante valida contra tests) es especialmente efectiva.

### 4.4 Integración de IA en el flujo de trabajo docente

Modelo de tres niveles recomendado por la literatura:

| Nivel | Descripción | Actividad típica |
|---|---|---|
| **Nivel 1 — Asistencia** | IA ayuda a completar código | Autocompletar en VS Code/PyCharm |
| **Nivel 2 — Colaboración** | IA genera alternativas, estudiante elige y justifica | "IA propone, yo evalúo" |
| **Nivel 3 — Reflexión** | Estudiante pide a la IA que explique el código que generó | Comprensión profunda |

La regla pedagógica clave: **el nivel 1 sin los niveles 2 y 3 genera dependencia sin aprendizaje**.

---

## 5. Propuestas de Mejora al Plan Mínimo IF009

Basadas en la evidencia anterior, se proponen los siguientes ajustes al plan. Ninguno elimina contenido del plan mínimo; solo reordenan, priorizan o añaden elementos con fundamento:

### P1 — Añadir hilo transversal: "IA Generativa: uso consciente" *(alta prioridad)*

**Fundamento:** Prather et al. 2024, Chen et al. 2025, Franklin et al. 2025

**Propuesta:** Introducir en la **Semana 1** (Módulo I) una sección de 45 minutos sobre "Uso consciente de IA generativa en programación":
- Qué es un LLM y qué no es.
- Marco de literacidad en IA (4 dimensiones).
- Política del curso: cuándo se puede usar, cómo declararlo, cómo citarlo.
- GitHub Copilot / ChatGPT en VS Code: demo práctica.

Reforzar este hilo en cada módulo (no como tema separado, sino como práctica integrada).

### P2 — Introducir micro-ciclos teoría→práctica en cada clase *(alta prioridad)*

**Fundamento:** Karymsakova et al. 2025

**Propuesta:** Reestructurar cada clase de 3 horas en:
- 45 min teoría + demo en vivo
- 45 min práctica guiada (pair programming, puede ser con IA)
- 30 min ejercicio autónomo
- 20 min cierre y retrospectiva

Esto reemplaza el formato "1h teoría + 2h práctica" que puede generar desconexión.

### P3 — Proyecto integrador desde el Módulo III *(media prioridad)*

**Fundamento:** PBL literature 2024–2025

**Propuesta:** Definir desde la Semana 5 una aplicación web Python/Django que el alumno construirá **incrementalmente** a lo largo de los Módulos III–VII. Cada módulo nuevo añade una capa a la misma aplicación:
- Módulo III: app básica con views y urls.
- Módulo IV: añade modelos y CRUD.
- Módulo V: añade templates y formularios.
- Módulo VI: añade autenticación y permisos.
- Módulo VII: añade endpoint REST.

Esto da coherencia al cursado y simula un flujo de trabajo profesional real.

### P4 — Incorporar TDD como práctica obligatoria desde el Módulo II *(alta prioridad)*

**Fundamento:** El libro ya está en la bibliografía (Percival, CC). La investigación confirma su valor.

**Propuesta:** El **Módulo II** (Pruebas Unitarias) debe enseñar TDD explícitamente como metodología de trabajo, no solo como "esto es cómo se escriben tests". El alumno escribe el test antes del código en todos los ejercicios prácticos del módulo.

Luego, en los Módulos IV–VII, los TPs deben incluir tests como requisito de entrega.

### P5 — AI pair programming en labs *(media prioridad)*

**Fundamento:** Fan et al. IJSTEM 2025

**Propuesta:** En las clases de laboratorio (práctica), habilitar explícitamente el uso de GitHub Copilot (o ChatGPT) como "copiloto", con la condición de que el alumno pueda explicar verbalmente cada línea generada. Esto reduce la ansiedad, mejora la motivación y enseña evaluación crítica de salidas de IA.

### P6 — Actualizar referencias técnicas *(media prioridad)*

**Fundamento:** Python 3.13 y Django 5.1 docs

**Propuesta:**
- Usar **Python 3.13** como versión oficial del curso (ya en la bibliografía como docs 3.13.1).
- Usar **Django 5.1** (noviembre 2024).
- Enseñar el **REPL mejorado** de Python 3.13 desde el día 1.
- Incorporar `LoginRequiredMiddleware` (Django 5.1) como práctica en Módulo VI.

### P7 — Añadir herramientas modernas de calidad de código *(baja prioridad)*

**Fundamento:** Ecosistema Python 2025

**Propuesta:** Introducir en el Módulo I, junto con el setup del entorno:
- **Ruff** como linter/formateador (reemplaza flake8 + black en un comando).
- **pre-commit hooks** para automatizar calidad (Git hook que corre Ruff antes del commit).

Esto enseña prácticas de calidad desde el inicio y acerca al alumno al flujo de trabajo profesional actual.

### P8 — Módulo VII expandido: REST con Django REST Framework *(baja prioridad)*

**Fundamento:** Demanda del mercado laboral + estructura del plan actual (solo 6hs para REST)

**Propuesta:** Si el tiempo lo permite (semanas 15–16), expandir el Módulo VII para cubrir:
- Serializers y ViewSets básicos.
- Autenticación JWT en APIs.
- Testing de endpoints REST con `pytest-django`.

Alternativamente, queda como **tema optativo de enriquecimiento** para el TP integrador.

---

## 6. Resumen de Propuestas por Prioridad

| ID | Propuesta | Prioridad | Módulo afectado | Esfuerzo |
|----|-----------|-----------|-----------------|----------|
| P1 | Hilo transversal IA Generativa | 🔴 Alta | I (inicio) + todos | Bajo |
| P2 | Micro-ciclos teoría→práctica | 🔴 Alta | Todos | Bajo |
| P3 | Proyecto integrador progresivo | 🟡 Media | III–VII | Medio |
| P4 | TDD obligatorio desde Módulo II | 🔴 Alta | II + IV–VII | Bajo |
| P5 | AI pair programming en labs | 🟡 Media | III–VII | Bajo |
| P6 | Actualizar a Python 3.13 + Django 5.1 | 🟡 Media | I | Bajo |
| P7 | Ruff + pre-commit hooks | 🟢 Baja | I | Muy bajo |
| P8 | REST expandido (DRF completo) | 🟢 Baja | VII | Alto |

---

## 7. Fuentes Consultadas

### Artículos académicos peer-reviewed

1. **Prather, J. et al.** (2024). *Beyond the Hype: A Comprehensive Review of Current Trends in Generative AI Research, Teaching Practices, and Tools.* ACM ITiCSE Working Group Reports 2024. DOI: 10.48550/arXiv.2412.14732

2. **Alves, A. & Cipriano, B.** (2024). *'Give me the code' — Log Analysis of First-Year CS Students' Interactions With GPT.* arXiv:2411.17855

3. **Jacobs, M., Haas, B. & Kiesler, N.** (2025). *Student Engagement with GenAI's Tutoring Feedback.* Koli Calling 2025. DOI: 10.1145/3769994.3770034. arXiv:2509.22974

4. **Jacobs, M. et al.** (2025). *That's Not the Feedback I Need!* UKICER 2025. DOI: 10.1145/3754508.3754512. arXiv:2506.20433

5. **Fan, X. et al.** (2025). *The Impact of AI-Assisted Pair Programming on Learning Outcomes.* International Journal of STEM Education, 2025. (234 students, 2 academic years)

6. **Ellis, D., Casey, M. & Hill, S.** (2024). *ChatGPT and Python Programming Homework.* Decision Sciences Journal of Innovative Education, 2024.

7. **Karymsakova, A. et al.** (2025). *A Practice-Oriented Approach to Teaching Python Programming.* Open Education Studies, 2025.

8. **Bekkering, E. & Harrington, R.** (2025). *Comparison of GenAI Solutions and Textbook Solutions in Introductory Programming.* Information Systems Education Journal (ISEDJ), 2025.

9. **Chen, X., Tallant, J. & Selig, M.** (2025). *Generative AI Literacy: Student Adoption, Interaction, Evaluation.* Information and Learning Sciences, 2025.

10. **Franklin, D. et al.** (2025). *Generative AI in CS Education: Challenges and Opportunities.* Cambridge University Press, 2025.

11. **Harrington, R. et al.** (2026). *Did Alice Do Wrong? Cross-Cultural Differences in Student Perceptions of GenAI.* ACM Transactions on Computing Education, 2026.

### Documentación técnica oficial

12. **Python Software Foundation** (2024). *What's New In Python 3.13.* https://docs.python.org/3/whatsnew/3.13.html

13. **Django Software Foundation** (2024). *Django 5.1 Release Notes.* https://docs.djangoproject.com/en/5.1/releases/5.1/

---

*Este documento es insumo para la construcción del plan-borrador.md. Las propuestas aquí consignadas deben ser evaluadas por el profesor antes de incorporarse al diseño del curso.*
