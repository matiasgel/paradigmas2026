# Diseño de Tema — Módulo I: Diseño Ágil + Python
## Tema 01 | Semanas 2–3 | Constraint: 180 min/sesión × 4 sesiones

> **STATUS:** `design` — Pendiente aprobación del docente  
> **Diseñado por:** Lic. Marcos 🗂️ (topic-designer)  
> **Fecha:** 2026-03-25  
> **Aprobado:** ☐ No aprobado aún

---

## 1. Identificación del Tema

| Campo | Valor |
|-------|-------|
| Número de tema | 01 |
| Nombre | Módulo I — Diseño Ágil + Python |
| Semanas de dictado | 2 y 3 |
| Sesiones | 4 (2 teóricas + 2 prácticas) |
| Duración por sesión | **180 min (constraint fijo — no negociable)** |
| Duración total módulo | 720 min (12 hs) |
| TP asociado | **TP 2 — Python + Prompting con Autograding** |
| Deadline TP2 | Semana 4, lunes 23:59 — `classroom.github.com/a/X4xiTEDQ` |
| Branch Git | `tema-01-diseno-agil-python` |

---

## 2. Fundamento Curricular — Plan Mínimo

Cubre íntegramente el **`plan-minimo.md` → Módulo I** (originalmente semanas 1–2 del programa institucional, adaptado a semanas 2–3 por inserción del Módulo 0 de nivelación):

| Tópico plan-minimo.md | Dónde se aborda |
|----------------------|-----------------|
| El Modelo Ágil para construcción de aplicaciones | T1-A (45 min) |
| Herramientas de desarrollo ágil | T1-A (45 min) |
| Entornos de desarrollo integrado (IDE) | T1-A (45 min) |
| Código autodocumentado y herramientas de extracción | T1-D + T2-C (30 + 30 min) |
| Construcción de aplicaciones en entornos integrados | P1-A/P1-B/P2-A (práctica completa) |
| Pautas y criterios para la transformación diseño-código | T1-D + T2-C |
| Lenguajes dinámicos para desarrollo de aplicaciones | T1-B/T1-C (90 min) |
| **Introducción al lenguaje Python** (sintaxis, tipos, funciones, colecciones) | T1-B + T1-C + T2-A + T2-B (180 min total) |

**Conexión con tema anterior:** Tema 00 (Semana 1) estableció setup GitHub (repo, SSH, Codespaces), Bootstrap 5 y prompting básico. Los alumnos ya tienen cuenta GitHub activa y TP2 asignado en Classroom — este módulo provee el conocimiento Python para resolverlo.

---

## 3. Evidencia Académica Incorporada

| Fuente | Hallazgo aplicado | Propuesta incorporada |
|--------|-------------------|-----------------------|
| Karymsakova et al. (Open Educ. Studies 2025) | Ciclos cortos teoría→práctica mejoran retención conceptual | P2: estructura de bloques 45'/45'/30'/20' en cada sesión |
| Fan et al. (IJSTEM 2025) | AI pair programming reduce ansiedad y mejora motivación vs enfoque tradicional | P5: GitHub Copilot habilitado en Codespaces desde sesión P1 |
| Alves & Cipriano (arXiv:2411.17855, 2024) | Estudiantes de primer año piden código completo sin comprensión previa | P1: PROMPTS.md obligatorio + demostración de comprensión previa al uso |
| Bekkering & Harrington (ISEDJ 2025) | GenAI supera textbook en 68% de casos: replantear rol de la bibliografía | P5: Copilot como herramienta de aprendizaje, no sustituto de comprensión |
| Prather (arXiv:2412.14732, 2024) | Marco de IA literacy aumenta uso crítico vs uso ingenuo | P1: IA literacy como hilo transversal desde el primer ejercicio |

---

## 4. Estructura Sesión por Sesión

### SESIÓN T1 — Semana 2, Teoría (180 min)

> **Constraint:** 180 min exactos. Bloques según propuesta P2: 45' + 45' + 30' + 20'.
> **Carga cognitiva:** T1-A y T1-B son bloques densos (30 min de material nuevo cada uno). T1-C y T1-D son consolidación + tools.

| Bloque | Duración | Contenido | Material |
|--------|----------|-----------|----------|
| **T1-A** | 45 min | **El Modelo Ágil**: manifesto ágil (2001), iteraciones cortas, feedback continuo. Comparación ciclo cascada vs ágil. Setup VS Code + extensiones Python esenciales: Pylance, Ruff extension, GitLens. GitHub Codespaces como entorno estándar del curso (devcontainer). | Filminas 1–12 |
| **T1-B** | 45 min | **Python 3.13 — Fundamentos**: sintaxis básica, tipos primitivos (`int`, `float`, `str`, `bool`, `None`), asignación, operadores (incluye `//`, `%`, `**`). **Novedades Python 3.13 pedagógicas**: nuevo REPL interactivo (multiline, historial, colores), mensajes de error contextuales ("¿quisiste decir `maxsplit`?"). Demo en vivo del REPL 3.13. Inmutabilidad de strings vs mutabilidad de listas. | Filminas 13–26 |
| **T1-C** | 30 min | **Control de flujo**: `if/elif/else`, `for` sobre secuencias, `while`, `range()`, `break`/`continue`, `match` (Python 3.10+, PEP 636). **Funciones**: `def`, `return`, `docstrings`, parámetros posicionales vs keyword, valores por defecto, `*args`, `**kwargs`. | Filminas 27–36 |
| **T1-D** | 20 min | **Ruff + PEP 8**: qué es un linter, por qué activarlo desde el primer script. Instalar Ruff en VS Code. Código autodocumentado: nombres descriptivos, funciones de responsabilidad única, convenciones PEP 8 (4 espacios, 79 chars, UpperCamelCase para clases, snake_case para funciones). Preview TP2. | Filminas 37–42 |

---

### SESIÓN P1 — Semana 2, Práctica (180 min)

> **Constraint:** 180 min. Laboratorio hands-on en Codespaces con GitHub Copilot habilitado.

| Bloque | Duración | Contenido | Modalidad |
|--------|----------|-----------|-----------|
| **P1-A** | 50 min | **Ejercicios guiados Python en Codespaces**: variables → funciones → loops. Ejercicios incrementales: calculadora simple, conversor de temperatura, generador de Fibonacci, clasificador de números. Docente muestra en pantalla, alumnos replican en paralelo. | Guiado (docente + pantalla) |
| **P1-B** | 50 min | **Prompting para Python**: demostración ChatGPT + Copilot. Patrón Role+Contexto+Tarea+Restricciones+Ejemplo aplicado a Python. Ejercicio: escribir código asistido → entenderlo línea a línea → modificarlo → documentarlo en `PROMPTS.md`. Énfasis: NO es válido copiar sin comprensión. | Demo + práctica individual |
| **P1-C** | 40 min | **GitHub Classroom TP2**: aceptar tarea, explorar estructura `src/` + `tests/` + `autograding.yml`. Leer los tests de pytest antes de escribir código (¿qué espera el test?). Completar primer script: `src/hello.py`. Push → ver primer CI verde. | Individual con pares |
| **P1-D** | 20 min | Revisión colectiva: ¿qué es un commit significativo? Análisis de mensajes de commit buenos vs malos. `git log --oneline` en pantalla del docente. Dudas TP2 frecuentes (ruta, imports, autograding). | Plenario |

---

### SESIÓN T2 — Semana 3, Teoría (180 min)

> **Constraint:** 180 min. Profundización y nuevos conceptos sobre base de semana 2.
> **Precondición:** Los alumnos ya tienen al menos 2/7 scripts del TP2 completados.

| Bloque | Duración | Contenido | Material |
|--------|----------|-----------|----------|
| **T2-A** | 45 min | **Colecciones Python**: `list`, `tuple`, `dict`, `set`. Mutabilidad vs inmutabilidad. Comprensiones de lista, dict y set (`[x**2 for x in range(10)]`, `{k: v for k, v in items}`). Funciones built-in: `enumerate()`, `zip()`, `sorted()` con `key=`, `len()`, `sum()`, `min()`, `max()`. | Filminas 43–56 |
| **T2-B** | 45 min | **Módulos y paquetes**: `import`, `from ... import`, `__init__.py`, estructura de proyecto Python. `requirements.txt`. **Funciones de orden superior**: `map()`, `filter()`, `sorted()` con `key=lambda`. **Lambdas**: `lambda x: x**2`. **Decoradores básicos**: `@property`, `@staticmethod`, `@functools.wraps`. Introducción — profundización en Módulo III. | Filminas 57–70 |
| **T2-C** | 30 min | **Type hints Python 3.10+** (PEP 484): `str`, `int`, `float`, `list[int]`, `dict[str, float]`, `Optional[X]` (`X \| None` post-3.10), `Union[A, B]`, `Any`. Anotaciones de retorno `-> tipo`. Por qué type hints mejoran legibilidad y cómo Ruff los valida. Solo lo necesario para TP2 y código autodocumentado. | Filminas 71–80 |
| **T2-D** | 20 min | **Patrones de prompting para debugging**: mostrar traceback a Copilot, pedir explicación línea a línea, prompt para refactoring de función, prompt para agregar type hints. Preview criterios de evaluación TP2. Reminder deadline semana 4. | Filminas 81–84 |

---

### SESIÓN P2 — Semana 3, Práctica (180 min)

> **Constraint:** 180 min. Taller TP2 intensivo + cierre módulo.

| Bloque | Duración | Contenido | Modalidad |
|--------|----------|-----------|-----------|
| **P2-A** | 60 min | **Taller TP2**: completar ejercicios `src/` en Codespaces, ver CI correr (push → GitHub Actions → pytest). Meta: resolver al menos 5/7 ejercicios con tests en verde. Docente circula. Copilot habilitado pero PROMPTS.md obligatorio. | Individual con pares |
| **P2-B** | 40 min | **PROMPTS.md obligatorio**: documentar mínimo 3 prompts completos (patrón Role+Contexto+Tarea+Restricción+Ejemplo). Revisión de calidad entre pares: ¿el prompt documenta el razonamiento real? ¿es reproducible? | Individual + revisión en pares |
| **P2-C** | 40 min | **Revisión colectiva de commits**: mínimo 7 commits con mensajes descriptivos. Análisis en pantalla: commit bien documentado vs commit vago ("fix", "update"). Comando `git log --oneline --graph`. Rebasing basic: squash de commits vacíos. | Plenario |
| **P2-D** | 20 min | **Retrospectiva Módulo I**: ¿qué conceptos quedaron más claros? ¿qué costó más? (votación anónima en pizarrón). Preview Módulo II: Testing y TDD — ¿qué es test-first development? Cómo los tests del TP2 son Red-Green-Refactor en acción. | Reflexión colectiva |

---

## 5. Objetivos de Aprendizaje

Al finalizar el Módulo I (Tema 01), el alumno debe ser capaz de:

| # | Objetivo | Nivel Bloom | Cómo se evalúa en TP2 |
|---|----------|-------------|----------------------|
| OA1 | Describir el modelo ágil y sus herramientas de apoyo (VS Code, Git, CI) | Recordar / Comprender | Flujo de trabajo: commits, CI verde |
| OA2 | Escribir funciones Python 3.13 correctas con tipos, condicionales y loops | Aplicar | Scripts en `src/` del TP2 |
| OA3 | Usar colecciones Python (`list`, `dict`, `set`, comprensiones) para resolver problemas concretos | Aplicar | Scripts más complejos del TP2 |
| OA4 | Organizar código Python en módulos con docstrings, Ruff-compliant y type hints básicos | Aplicar / Analizar | Estructura `src/tests/` del TP2 |
| OA5 | Usar GitHub Copilot con prompts estructurados y documentar el proceso en `PROMPTS.md` | Aplicar | `PROMPTS.md` del TP2 (≥3 prompts) |
| OA6 | Explicar qué hace el código Python generado por IA antes de entregarlo | Comprender | Calidad de PROMPTS.md + demos en clase |

---

## 6. Material de Referencia

### Bibliografía Base — Documentación Oficial Python

| Fuente | Tipo | Acceso |
|--------|------|--------|
| Python 3.13 Official Tutorial — Caps. 3, 4, 5, 6 | Documentación oficial | https://docs.python.org/3.13/tutorial/ |
| What's New in Python 3.13 | Documentación oficial | https://docs.python.org/3.13/whatsnew/3.13.html |
| PEP 8 — Style Guide for Python Code | Estándar Python | https://peps.python.org/pep-0008/ |
| PEP 484 — Type Hints | Estándar Python | https://peps.python.org/pep-0484/ |
| PEP 636 — Structural Pattern Matching Tutorial | Estándar Python | https://peps.python.org/pep-0636/ |
| Ruff Linter Documentation | Herramienta | https://docs.astral.sh/ruff/ |

> **PDFs descargables**: ver `material/tema 01/txt/python-fuentes-descarga.txt` para instrucciones de descarga.
> **Contenido ya extraído**: `material/tema 01/txt/python-tutorial-intro.txt`, `python-tutorial-controlflow.txt`, `python-whatsnew-313.txt`.

### Bibliografía Académica — en `material/init/`

| Archivo | Referencia APA | Sección relevante |
|---------|----------------|-------------------|
| `DeGruyter-OpenEduStudies-2025-Karymsakova-...` | Karymsakova et al. (2025). *Practice-Oriented Python Teaching*. Open Education Studies. | Metodología de ciclos T→P cortos |
| `Springer-IJSTEM-2025-Fan-AI-Pair-Programming-...` | Fan et al. (2025). *AI Pair Programming, Motivation, Anxiety, Performance*. IJSTEM. | AI pair programming en labs |
| `ISEDJ-2025-v23n1-Bekkering-Harrington-...` | Bekkering & Harrington (2025). *GenAI vs Textbook Programming*. ISEDJ, 23(1). | GenAI como herramienta vs bibliografía |
| `arXiv-2412.14732-Prather-2024-...` | Prather (2024). *Beyond the Hype: GenAI in CS Education*. arXiv:2412.14732. | Marco pedagógico GenAI |
| `arXiv-2411.17855-Alves-Cipriano-2024-...` | Alves & Cipriano (2024). *Give Me The Code: GPT in First Year*. arXiv:2411.17855. | Patrones de uso LLM primer año |
| `ISEDJ-2025-v23n4-Frydenberg-...` | Frydenberg (2025). *Student Perceptions of AI in Python*. ISEDJ, 23(4). | Calidad de código con IA |

### Material Específico del Tema — `material/tema 01/`

| Archivo | Descripción |
|---------|-------------|
| `TP 2.pdf` | TP2 — Python + Prompting (enunciado original) |
| `tp2-consigna.pdf` | TP2 — consigna detallada para alumnos |
| `txt/python-tutorial-intro.txt` | Python 3.13 Tutorial Cap. 3 extraído |
| `txt/python-tutorial-controlflow.txt` | Python 3.13 Tutorial Cap. 4 extraído |
| `txt/python-whatsnew-313.txt` | Novedades pedagógicas Python 3.13 |
| `txt/python-fuentes-descarga.txt` | Manifest de PDFs por descargar manualmente |

---

## 7. Scope Control — Eso está fuera de scope del Tema 01

Los siguientes temas NO pertenecen a este módulo:

| Tema | Dónde va | Justificación |
|------|----------|---------------|
| pytest / TDD / ciclo Red-Green-Refactor | **Módulo II** (Tema 02, Semanas 4–5) | Plan mínimo módulo separado |
| Clases y POO en Python | **Módulo IV** (Semanas 7–9) | Tema 04 |
| async/await, concurrencia, asyncio | Fuera del cuatrimestre 2026 | Nivel avanzado |
| Django / modelos / ORM | **Módulo III-IV** (Semanas 6–9) | Temas 03-04 |
| Type hints avanzados (Protocol, TypeVar) | Mencionar como preview, profundizar Tema 04 | Solo intro básica |
| GIL / free-threading (PEP 703) | Solo mención contextual en T1-B | Experimental en 3.13 |
| JIT compiler (PEP 744) | Solo mención, informativo | Sin relevancia curricular 2026 |
| pandas / numpy / scipy | No es parte de IF009 2026 | Fuera del plan |
| Virtual environments (`venv`) | Setup inicial en Tema 00 / GitHub Codespaces | Ya cubierto |

---

## 8. Evaluación del Tema

TP2 evalúa la totalidad de los OA de este módulo:

| Componente TP2 | Criterio | Peso |
|----------------|----------|------|
| 7 scripts en `src/` | Tests pytest en verde vía GitHub Actions CI | 60% |
| `PROMPTS.md` | ≥3 prompts completos (Role+Contexto+Tarea+Restricción+Ejemplo) | 20% |
| Commits Git | ≥7 commits con mensajes descriptivos | 20% |
| **Deadline** | **Semana 4, lunes 23:59** — `classroom.github.com/a/X4xiTEDQ` | — |

Criterio de calidad del código: Ruff sin errores, docstrings en todas las funciones, type hints en parámetros y retorno.

---

## 9. Notas del Diseñador

> **Marcos:** "Atención a los siguientes puntos antes de producir la clase:"

1. **TP2 ya fue asignado en semana 1**: Los alumnos recibieron el link en Classroom en tema 00. Algunos habrán avanzado solos — este módulo consolida y explica el "por qué" de lo que tienen que hacer. Hay espacio para alumnos adelantados en P1-C y P2-A.

2. **Python 3.13 REPL**: Demostrar en vivo en T1-B. Es el diferenciador visible más poderoso — los estudiantes ven de inmediato que 3.13 es mejor para aprender. No saltear este demo.

3. **Ruff desde el primer script**: Instalarlo en P1-A, no "después". Si esperamos al Módulo II para hablar de código limpio, creamos deuda técnica inmediata que es difícil de corregir.

4. **Semana 2 es la más densa**: Si el tiempo aprieta en T1, priorizar T1-B (Python fundamentos) sobre T1-A (Modelo Ágil). El modelo ágil puede comprimirse a 15 min si es necesario.

5. **TP2 tiene autograding**: Los alumnos pueden ver si sus tests pasan en tiempo real. Usarlo en P1-D como motivador ("push y ve el CI verde"). El feedback inmediato es un motivador poderoso (Fan et al. 2025).

6. **PROMPTS.md no es opcional**: Es parte de la evaluación TP2 con un 20% del peso. Introducirlo en P1-B y reforzarlo en P2-B.

---

## 10. Próximos Pasos del Flujo

```
[PASO ACTUAL] Step 1: Diseño (topic-designer, Marcos) ← estamos aquí
     ↓
Step 2: Ajuste diseño (opcional, antes de aprobación)
     ↓
Step 3: APROBACIÓN del docente ← confirmar para continuar
     ↓
Step 4: Clase (class-writer, Roberto) → genera minuta.md + filminas.md
     ↓
Step 4.5: Guía de estudio (study-guide-writer, Sofía) → guia-estudio.md
     ↓
Step 5: TP (tp-designer, Valeria) → tp.md
     ↓
Steps 6-8: Loops de calidad
```

**Para aprobar este diseño**, el docente debe confirmar:
- ¿La distribución de contenido entre las 4 sesiones es correcta?
- ¿El scope está bien delimitado (especialmente qué no entra)?
- ¿El peso de evaluación TP2 (60/20/20) es correcto?
- ¿Ajustar algo antes de pasar a clase-writer?
