# Plan de Cursada — Laboratorio de Programación y Lenguajes (IF009)
## UNTDF — Instituto IDEI — 2026

> ⚠️ **DOCUMENTO DE TRABAJO** — Este plan puede modificarse hasta su confirmación final.
> Ancla institucional inmutable: `salida/cursadas/2026/plan-minimo.md`
> Generado: 2026-03-24 | Agente: Dr. Roberto (class-writer) | Docente: Matías Gel

---

## Base Documental

| Fuente | Descripción |
|--------|-------------|
| `salida/cursadas/2026/plan-minimo.md` | Programa institucional — 7 módulos obligatorios |
| `docs/investigacion.md` | Investigación académica — 12 papers, 8 propuestas (P1–P8) |
| `material/tema 01/TP 1.pdf` | TP 1: Blog HTML/CSS/Bootstrap — entrega via Git |
| `material/tema 01/TP 2.pdf` | TP 2: Python + Prompting — GitHub Classroom autograding |
| `material/tema 01/HTML & CSS.pdf` | Material de nivelación HTML/CSS |

---

## Propuestas de Investigación Incorporadas

Las siguientes propuestas del documento `docs/investigacion.md` se integran en este plan:

| Código | Propuesta | Integración |
|--------|-----------|-------------|
| **P1** | GenAI transversal desde semana 1 | Módulo 0: prompting intro + PROMPTS.md en todos los TPs |
| **P2** | Micro-ciclos 45'+45'+30'+20' | Estructura de cada clase teórica |
| **P3** | Proyecto integrador progresivo | BlogApp → evoluciona Módulo a Módulo |
| **P4** | TDD mandatorio desde Módulo II | TP 2 incluye tests, todos los TPs siguientes también |
| **P5** | AI pair programming en labs | Codespaces + Copilot habilitado en GitHub Classroom |
| **P6** | Python 3.13 + Django 5.1 | Stack oficial de la cursada |
| **P7** | Ruff + pre-commit | A partir del TP 2 |
| **P8** | REST expandido | Módulo VII ampliado a 2 semanas |

---

## Estructura de Evaluación

| Instancia | Descripción | Plataforma |
|-----------|-------------|------------|
| **TP 1** — Blog HTML/CSS | Blog personal con Bootstrap 5 | GitHub Classroom (≥5 commits significativos) |
| **TP 2** — Python + Prompting | 7 scripts + PROMPTS.md + tests | GitHub Classroom con autograding CI |
| **TP 3** — Django MVC | Módulo II/III integrado | GitHub Classroom con autograding |
| **TP 4** — ORM + Persistencia | CRUD completo con migrations | GitHub Classroom con autograding |
| **App Integradora I** | BlogApp: desde templates hasta auth | GitHub Classroom con autograding (semana 10) |
| **App Integradora II** | BlogApp + REST API | GitHub Classroom con autograding final (semana 16) |
| Parcial 1 | Semana 7 (teórico) | Presencial |
| Parcial 2 | Semana 13 (teórico) | Presencial |

> **GitHub Classroom en toda la cursada**: Todos los TPs y apps integradoras se entregan via
> GitHub Classroom. TP 1 usa repositorio template con checklist HTML/CSS. TPs 2–4 y apps
> integradoras incorporan GitHub Actions (`.github/workflows/autograding.yml`) con pytest.
> El alumno trabaja en su fork del template, hace push y ve feedback inmediato en el CI.
> GitHub Copilot habilitado en Codespaces de todos los repositorios.

---

## Política de IA Generativa (P1)

Basada en Prather et al. 2024, Jacobs 2025 y Frydenberg et al. 2025:

- **IA habilitada** en todos los TPs como herramienta de aprendizaje
- **Obligatorio** documentar prompts usados en `PROMPTS.md` por ejercicio
- **Patrón recomendado**: Role + Contexto + Tarea + Restricciones + Ejemplo
- **Prohibido**: copiar respuesta completa sin entender + adaptar en PROMPTS.md
- GitHub Copilot habilitado en Codespaces de todos los repositorios classroom

---

## Distribución Semanal

### MÓDULO 0 — Nivelación, Setup y Prompting *(Semana 1 — 6 hs)*

**Objetivo:** Emparejar el nivel del grupo en herramientas fundamentales antes de entrar en Python y Django.

#### Semana 1 — Teoría (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| T1 | 45' | Presentación de la cursada. Stack 2026: Python 3.13 + Django 5.1 + Bootstrap 5 + GitHub |
| T2 | 45' | **Prompting efectivo**: qué es un LLM, por qué el prompt importa, patrones básicos (Zero-shot, Few-shot, Role+Contexto+Tarea) |
| T3 | 30' | **HTML5 semántico**: DOCTYPE, estructura, etiquetas semánticas (`<header>`, `<main>`, `<article>`, `<section>`, `<footer>`), validación W3C |
| T4 | 20' | Cierre + preview TP 1 + GitHub setup (crear cuenta, SSH, primer repo) |

#### Semana 1 — Práctica (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| P1 | 45' | Bootstrap 5: CDN, grid de 12 columnas, breakpoints, componentes principales (Navbar, Card, Button, Form) |
| P2 | 45' | CSS3: box model, flexbox, variables CSS, media queries, `:valid`/`:invalid` |
| P3 | 30' | **Demo en vivo**: construir el esqueleto del TP 1 (index.html + navbar + cards) con Copilot |
| P4 | 20' | GitHub Classroom: aceptar tarea TP 1, primer commit, flujo de trabajo |

**TP 1 — Blog HTML/CSS/Bootstrap**
- Entrega: semana 2, lunes 23:59
- Plataforma: **GitHub Classroom** — repositorio template con estructura fija, ≥5 commits significativos
- Codespaces habilitado con GitHub Copilot
- Requisitos: `index.html`, `about.html`, `contact.html`, `assets/styles.css`, README.md
- Criterios: HTML válido (W3C), Bootstrap correcto, responsivo, formulario con validación HTML5
- Workflow CI: validación de archivos requeridos (`autograding.yml` con script de estructura)

---

### MÓDULO I — Diseño Ágil + Python *(Semanas 2–3 — 12 hs)*
*Cubre: plan-minimo.md → Módulo I completo*

**Objetivo:** Introducir el modelo ágil y los fundamentos de Python 3.13 con enfoque en código limpio y prompting asistido.

#### Semana 2 — Teoría (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| T1 | 45' | El Modelo Ágil: iteraciones cortas, feedback continuo. IDEs: VS Code + extensiones Python |
| T2 | 45' | **Python 3.13**: sintaxis básica, tipos, condicionales, funciones. Novedades 3.13 (mensajes de error mejorados, REPL) |
| T3 | 30' | Colecciones: listas, tuplas, diccionarios, sets. Comprensiones |
| T4 | 20' | Introducción a Ruff (linter), pre-commit hooks, código autodocumentado |

#### Semana 2 — Práctica (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| P1 | 50' | Ejercicios guiados Python en Codespaces: variables, funciones, loops |
| P2 | 50' | Prompting para Python: demostración ChatGPT + Copilot, corrección de lógica |
| P3 | 40' | **GitHub Classroom autograding**: aceptar TP 2, explorar estructura `src/` + `tests/` + `autograding.yml` |

#### Semana 3 — Teoría (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| T1 | 45' | Módulos y paquetes Python. `__init__.py`, importaciones, `requirements.txt` |
| T2 | 45' | Funciones de orden superior, lambdas, decoradores básicos |
| T3 | 30' | Type hints (Python 3.10+): `str`, `list[int]`, `dict[str, float]`, `Optional` |
| T4 | 20' | Cierre + patrones de prompting para debugging |

#### Semana 3 — Práctica (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| P1 | 60' | Taller TP 2: completar ejercicios en Codespaces, ver CI correr |
| P2 | 40' | Documentar prompts en PROMPTS.md (patrón Role+Contexto+Tarea+Restricción+Ejemplo) |
| P3 | 40' | Revisión colectiva: commits significativos, mensajes de commit |

**TP 2 — Python + Prompting con Autograding** *(entrega: semana 4, lunes 23:59)*
- Link: `https://classroom.github.com/a/X4xiTEDQ`
- Plataforma: GitHub Classroom con autograding CI (pytest automático en push)
- Requisitos: 7 scripts en `src/`, tests en `tests/`, ≥7 commits, `PROMPTS.md` completo
- Codespaces: GitHub Copilot habilitado en el devcontainer

---

### MÓDULO II — Pruebas Unitarias *(Semanas 4–5 — 12 hs)*
*Cubre: plan-minimo.md → Módulo II completo + P4 (TDD mandatorio)*

**Objetivo:** Incorporar TDD como práctica de desarrollo, no como técnica de verificación posterior.

#### Semana 4 — Teoría (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| T1 | 45' | Detección oportuna de errores. Taxonomía de pruebas. Pirámide de testing |
| T2 | 45' | **Prueba de Unidad**: definición, ciclo Red-Green-Refactor, assert semánticos |
| T3 | 30' | `unittest` vs `pytest`: fixtures, parametrize, markers |
| T4 | 20' | **TDD en la práctica**: escribir test primero, ver fallar, implementar |

#### Semana 4 — Práctica (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| P1 | 60' | Kata TDD guiada: FizzBuzz desde test |
| P2 | 40' | pytest con coverage: `pytest --cov=src tests/` |
| P3 | 40' | Integrar tests en GitHub Actions (introducción al CI como concepto) |

#### Semana 5 — Teoría (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| T1 | 45' | Mocking: `unittest.mock`, `MagicMock`, `patch`. Casos de uso |
| T2 | 45' | Introducción a `pytest-django`. Tests de modelos, vistas y URLs |
| T3 | 30' | TDD aplicado al proyecto integrador (BlogApp primera iteración) |
| T4 | 20' | Revisión TP 2 + presentación TP 3 |

#### Semana 5 — Práctica (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| P1 | 60' | Taller: escribir tests para módulos del TP 2 desde cero |
| P2 | 60' | GitHub Classroom TP 3: setup del repositorio, estructura Django básica |

---

### MÓDULO III — Frameworks WEB + Introducción a Django *(Semana 6 — 6 hs)*
*Cubre: plan-minimo.md → Módulo III. Nota: compartido conceptualmente con Módulo IV siguiente.*

#### Semana 6 — Teoría (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| T1 | 45' | Arquitectura web: capas de una aplicación, HTTP, request/response cycle |
| T2 | 45' | El **patrón MVC** y su implementación Django (MTV: Model-Template-View) |
| T3 | 30' | Frameworks: ventajas, convenciones sobre configuración. Django 5.1 novedades |
| T4 | 20' | **Git avanzado**: branches, pull requests, code review en GitHub |

#### Semana 6 — Práctica (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| P1 | 50' | `django-admin startproject blog . ` — estructura del proyecto, settings.py, `manage.py` |
| P2 | 50' | Primera view + URL: `HttpResponse`, `path()`, `include()` |
| P3 | 40' | Deploy en Codespaces: servidor de desarrollo, debug toolbar |

---

### MÓDULO IV — Persistencia + ORM *(Semanas 7–8 — 12 hs)*
*Cubre: plan-minimo.md → Módulo IV completo*

#### Semana 7 — Teoría (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| T1 | 45' | Concepto de persistencia. ORM vs SQL directo. Comparación: SQLAlchemy vs Django ORM |
| T2 | 45' | **Mapeo OO-Relacional en Django**: `Model`, campos, relaciones (`ForeignKey`, `ManyToMany`) |
| T3 | 30' | Migrations: `makemigrations`, `migrate`, historial de migraciones |
| T4 | 20' | **Parcial 1** — anuncio, temario, fecha (semana siguiente) |

#### Semana 7 — Práctica (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| P1 | 60' | Modelar BlogApp: `Post`, `Category`, `Comment` con relaciones |
| P2 | 60' | Django shell: operaciones CRUD manuales, `QuerySet` básico |

#### Semana 8 — Teoría (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| T1 | 45' | CRUD con Django ORM: `create()`, `filter()`, `exclude()`, `get()`, `update()`, `delete()` |
| T2 | 45' | Consultas avanzadas: `Q objects`, `annotate()`, `aggregate()`, `select_related()` |
| T3 | 30' | Django Admin: `ModelAdmin`, list_display, actions, customización |
| T4 | 20' | **Parcial 1** (escritura) |

#### Semana 8 — Práctica (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| P1 | 60' | TP 3 en Codespaces: implementar modelos con migrations |
| P2 | 60' | Tests de modelos con `pytest-django`: fixtures, `@pytest.mark.django_db` |

**TP 3 — Django MVC + ORM** *(entrega: semana 9, lunes 23:59)*
- Plataforma: GitHub Classroom con autograding (tests pytest-django automáticos)
- Requisitos: Modelos + admin + views básicas + tests ≥80% coverage

---

### MÓDULO V — Vistas, Templates + UI *(Semanas 9–11 — 18 hs)*
*Cubre: plan-minimo.md → Módulo V completo*

#### Semanas 9–10 — Contenido principal

| Tema | Contenido |
|------|-----------|
| Django Templates | Template Language, herencia (`{% extends %}`), bloques, filtros, tags |
| Vistas genéricas | `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` |
| Bootstrap + Django | Integrar Bootstrap 5 en templates Django — reutilizando lo de Módulo 0 |
| Formularios | `ModelForm`, `Form`, validación, `clean_*`, `is_valid()` |
| HTML5 + Django | `<form>`, CSRF token, redirect, messages framework |

#### Semana 10 — Entrega App Integradora I

- **BlogApp I**: modelos + admin + vistas géricas + templates Bootstrap + formularios
- Presentación en clase (15'/grupo), repositorio GitHub Classroom
- Criterio: funcionalidad completa, tests ≥75% coverage, commits ordenados

#### Semana 11 — Refactoring y deuda técnica

| Actividad | Descripción |
|-----------|-------------|
| Code review entre pares | Pull requests cruzados, comentarios de mejora |
| Ruff + pre-commit | Configurar linting automático en el repositorio |
| Refactoring guiado | Aplicar feedback de la entrega I |

---

### MÓDULO VI — Autorización y Autenticación *(Semanas 12–14 — 18 hs)*
*Cubre: plan-minimo.md → Módulo VI completo*

| Semana | Contenido teoría | Contenido práctica |
|--------|------------------|--------------------|
| 12 | Sesiones HTTP, cookies, `django.contrib.auth` | Login/logout/register en BlogApp |
| 13 | Permisos en modelos y vistas, `@login_required`, groups | **Parcial 2** + TP 4 inicio |
| 14 | Django Admin con permisos, vistas genéricas de usuario | Cierre TP 4 + code review |

**TP 4 — Auth + Admin completo** *(entrega semana 14)*
- Plataforma: GitHub Classroom autograding
- Requisitos: auth funcional, permisos por rol (author/reader/admin), tests de permisos

---

### MÓDULO VII — Servicios REST con Django *(Semanas 15–16 — 12 hs)*
*Cubre: plan-minimo.md → Módulo VII + P8 (REST expandido a 2 semanas)*

| Semana | Contenido teoría | Contenido práctica |
|--------|------------------|--------------------|
| 15 | API REST: principios, métodos HTTP, status codes, JSON. Django REST Framework: `Serializer`, `ViewSet`, Router | Construir API de posts (GET, POST, PUT, DELETE) en BlogApp |
| 16 | Autenticación en APIs: Token Auth vs JWT. Throttling, filtering, pagination. Consumo desde JS (`fetch`) | **Entrega App Integradora II**: BlogApp completa con REST API |

**App Integradora II — BlogApp completa**
- Django 5.1 + Bootstrap 5 + Django REST Framework
- Auth completa + admin + API REST consumida por una SPA simple en vanilla JS
- Tests ≥80% coverage total
- GitHub Classroom con autograding final

---

### SEMANA 17 — Cierre de Cursada

| Actividad | Descripción |
|-----------|-------------|
| Revisión de notas | Cálculo de promedios TPs + apps integradoras |
| Retrospectiva EDU | `_edu-memory/` — calibración para 2027 |
| Reunión de cátedra | Informe final institucional |

---

## Stack Tecnológico Oficial 2026

| Componente | Versión | Fuente |
|------------|---------|--------|
| Python | 3.13 | docs.python.org/3.13 |
| Django | 5.1 | docs.djangoproject.com/5.1 |
| Bootstrap | 5.3.3 | getbootstrap.com |
| Django REST Framework | 3.15 | django-rest-framework.org |
| pytest / pytest-django | última estable | docs.pytest.org |
| Ruff | 0.3+ | docs.astral.sh/ruff |
| GitHub Classroom + Codespaces | — | classroom.github.com |

---

## Bibliografía Obligatoria

| Autor | Año | Título | Acceso |
|-------|-----|--------|--------|
| Charles R. Severance | 2020 | Python para todos | https://do1.dr-chuck.com/pythonlearn/ES_es/pythonlearn.pdf |
| Python Software Foundation | 2024 | Python 3.13 documentation | https://docs.python.org/3/ |
| Mozilla Developer Network | 2024 | Aprende desarrollo web (HTML, CSS, Bootstrap) | https://developer.mozilla.org/es/docs/Learn |
| Django Software Foundation | 2024 | Documentación oficial Django 5.1 | https://docs.djangoproject.com/en/5.1/ |
| Harry J.W. Percival | 2024 | Test-Driven Development with Python | https://www.obeythetestinggoat.com/pages/book.html |
| GitHub, Inc | 2024 | GitHub Docs — Classroom + Actions | https://docs.github.com/es |
| Tom Christie | 2024 | Django REST Framework | https://www.django-rest-framework.org/tutorial/quickstart/ |

## Bibliografía Complementaria (Investigación)

| Paper | Año | Relevancia |
|-------|-----|------------|
| Prather et al. — *Beyond the Hype* | 2024 | GenAI en educación CS — marco general (P1) |
| Alves & Cipriano — *Give Me The Code* | 2024 | Prompting en 1er año — riesgos y beneficios |
| Jacobs — *Student Engagement* | 2025 | IA como tutor con feedback formativo |
| Fan et al. — *AI Pair Programming* | 2025 | Motivación y performance con Copilot (P5) |
| Karymsakova — *Practice-Oriented Python* | 2025 | Enseñanza orientada a práctica — Python |
| Bekkering & Harrington | 2025 | GenAI vs textbook para aprender programación |
| Frydenberg et al. | 2025 | Percepciones estudiantiles de IA + calidad código |

---

## Checklist de Confirmación

Antes de confirmar este plan, verificar:

- [ ] Distribución de semanas: 17 semanas cubre los 7 módulos institucionales
- [ ] TP 1 (HTML/CSS) cubre Material existente en `material/tema 01/` — crear repositorio template en GitHub Classroom
- [ ] TP 2 (Python autograding) tiene link de Classroom confirmado (`classroom.github.com/a/X4xiTEDQ`)
- [ ] TPs 3, 4 y Apps Integradoras I y II tienen repositorios template en GitHub Classroom
- [ ] Todos los repos tienen Codespaces + GitHub Copilot habilitado
- [ ] Stack (Python 3.13, Django 5.1, Bootstrap 5.3.3) disponible en Codespaces
- [ ] Política de IA redactada y comunicada a los alumnos desde semana 1
- [ ] Parciales: semana 8 (parcial 1) y semana 13 (parcial 2) — confirmar con calendario académico
