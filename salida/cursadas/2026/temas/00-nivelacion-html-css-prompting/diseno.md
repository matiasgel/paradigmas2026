# Tema 00 — Nivelación HTML/CSS/Bootstrap 5/Prompting
## Diseño Pedagógico

**Curso:** IF009 — Laboratorio de Programación y Lenguajes  
**Institución:** UNTDF IDEI  
**Año:** 2026  
**Semana:** 1  
**Duración:** 180 min teoría + 180 min práctica = 6 horas totales  
**Estado:** ✅ Clase iniciada — filminas base ya presentadas, TP1 y TP2 ya entregados

---

## Objetivo General

Nivelar a los alumnos en HTML5, CSS3 y Bootstrap 5 como base para el desarrollo de aplicaciones web con Python/Django, integrando herramientas de IA (Copilot/Prompting) desde el primer día.

## Objetivos de Aprendizaje

Al finalizar esta unidad el alumno será capaz de:

1. **Construir páginas HTML5 semánticas** usando las etiquetas correctas (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`)
2. **Estilizar con CSS3** aplicando box model, selectores, flexbox, variables CSS y media queries
3. **Implementar un layout responsive con Bootstrap 5** usando el grid system (container/row/col), Navbar, Cards y Forms
4. **Usar IA asistida (Copilot)** para acelerar la escritura de HTML/CSS y documentar el proceso en PROMPTS.md
5. **Gestionar el trabajo con Git** realizando commits semánticos y descriptivos desde el inicio

---

## Alineación con Plan Mínimo

> **Módulo I — Diseño ágil y Python** (semanas 1-2): Nivelación previa necesaria para comprender el stack HTML+Django. Este módulo 0 provee la base tecnológica web que el alumno necesitará en los Módulos IV-VI (Django Templates, ORM, Vistas).

---

## Estructura de Clases

### Bloque Teoría (180 min) — Micro-ciclos

| Bloque | Tiempo | Contenido | Tipo |
|--------|--------|-----------|------|
| T1 | 45' | Prompting & IA: qué es GitHub Copilot, cómo dar buenos prompts, filosofía "IA como copiloto" | Conceptual + Demo |
| T2 | 45' | HTML5 semántico: estructura básica, elementos semánticos, validación W3C | Expositivo + Código |
| T3 | 30' | Box Model CSS + Flexbox: margin/padding/border, display flex, justify-content, align-items | Visual + Código |
| T4 | 20' | Preview TP1 + setup GitHub Classroom | Orientación práctica |
| Cierre | 10' | Preguntas, resumen, próxima clase | Consolidación |

### Bloque Práctica (180 min) — Laboratorio

| Bloque | Tiempo | Contenido | Tipo |
|--------|--------|-----------|------|
| P1 | 45' | Bootstrap 5: CDN, container/row/col-md-*, breakpoints sm/md/lg | Guiado + Ejercicio |
| P2 | 45' | Bootstrap Navbar + Cards + Forms: clases específicas, personalización CSS | Taller |
| P3 | 30' | Demo live TP1: armar index.html con Navbar, grid de Cards, Bootstrap CDN | Live coding |
| P4 | 20' | Setup GitHub Classroom: aceptar invitación TP1, primer commit | Individual |
| Cierre | 10' | Dudas, checklist de entrega | Consolidación |

---

## Contenidos Detallados

### HTML5 Semántico
- Estructura básica: `<!DOCTYPE html>`, `<html lang="es">`, `<head>`, `<body>`
- Meta tags obligatorios: `charset`, `viewport`, `description`
- Elementos semánticos: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`
- Formularios HTML5: `<form>`, `<input>` (types: text, email, password, submit), `<label>`, `<textarea>`, `<button>`
- Validación: W3C Validator (validator.w3.org)

### CSS3
- Box model: `margin`, `padding`, `border`, `width`, `height`, `box-sizing: border-box`
- Selectores: elemento, clase (`.nombre`), id (`#nombre`), combinados
- Flexbox: `display: flex`, `flex-direction`, `justify-content`, `align-items`, `flex-wrap`
- Variables CSS: `--primary-color`, `var(--primary-color)`
- Media queries: `@media (max-width: 768px)`, mobile-first approach
- Pseudo-clases: `:hover`, `:focus`, `:valid`, `:invalid` (feedback de formularios)

### Bootstrap 5
- Incluir via CDN: `<link>` CSS + `<script>` JS
- Grid system: `container` / `row` / `col-{breakpoint}-{n}` (12 columnas)
- Breakpoints: xs (0px), sm (576px), md (768px), lg (992px), xl (1200px)
- Navbar: `.navbar`, `.navbar-expand-lg`, `.navbar-brand`, `.navbar-toggler`, `.nav-link`
- Cards: `.card`, `.card-body`, `.card-title`, `.card-text`, `.card-img-top`, `.card-footer`
- Forms: `.form-control`, `.form-label`, `.btn`, `.btn-primary`, `.btn-outline-secondary`
- Utilidades: spacing (`m-`, `p-`, `mb-3`), display (`d-flex`, `d-none`), text (`text-center`, `text-muted`)

### Prompting con IA
- Qué es un prompt efectivo: contexto + tarea + restricciones + formato de salida
- Uso de GitHub Copilot en VS Code para HTML/CSS
- Documentación en PROMPTS.md: qué pedí, qué recibí, qué modifiqué
- Anti-pattern: pegar código sin entenderlo

---

## Evidencia de Aprendizaje

### TP1 — Blog Personal
- **Tipo:** Proyecto individual con GitHub Classroom
- **Entrega:** Via GitHub Classroom (link pendiente de alta)
- **Requerimientos mínimos:**
  - `index.html`: lista de posts como Cards Bootstrap, Navbar
  - `about.html`: sobre el autor
  - `contact.html`: formulario funcional con validación `:valid/:invalid`
  - `css/styles.css`: estilos custom con media queries
  - `PROMPTS.md`: documentación de prompts usados (al menos 5)
  - ≥ 5 commits semánticos en Git
- **Validación:** W3C HTML Validator sin errores

### TP2 — Python Autograding
- **Tipo:** Proyecto individual con autograding automático
- **Link:** classroom.github.com/a/X4xiTEDQ
- **Requerimientos:** 7 scripts Python (`src/`), tests en `tests/`, PROMPTS.md obligatorio

---

## Criterios de Evaluación (TP1)

| Criterio | Peso | Descripción |
|----------|------|-------------|
| Estructura HTML5 semántica | 25% | Uso correcto de elementos semánticos, sin divitis |
| Bootstrap 5 implementado | 25% | Grid responsive, Navbar, Cards, Forms con clases correctas |
| CSS custom | 20% | `styles.css` con media queries y ≥2 variables CSS |
| PROMPTS.md | 15% | Documentación real del proceso con IA |
| Git (commits) | 15% | ≥5 commits con mensajes descriptivos |

---

## Recursos de Referencia

| Recurso | URL | Tipo |
|---------|-----|------|
| W3Schools HTML | https://www.w3schools.com/html/ | Tutorial interactivo |
| W3Schools CSS | https://www.w3schools.com/css/ | Tutorial interactivo |
| Bootstrap 5 Docs | https://getbootstrap.com/docs/5.3/ | Documentación oficial |
| W3C Validator | https://validator.w3.org/ | Herramienta de validación |
| GitHub Classroom | https://classroom.github.com/ | Plataforma de entrega |

---

## Notas del Docente

- **Clase ya iniciada**: Las filminas base fueron presentadas usando el material de `HTML & CSS.pdf`
- **TP1 ya entregado**: Los alumnos tienen la consigna de TP1 (Blog HTML/CSS Bootstrap)
- **TP2 ya entregado**: El link de GitHub Classroom para TP2 Python ya fue compartido
- **Estrategia diferenciada**: Alumnos con experiencia previa en HTML/CSS pueden avanzar al TP1 directamente; alumnos sin experiencia usan los tutoriales de W3Schools como soporte
- **Memoria del simulador**: Ver investigación en `_edu-memory/material/investigacion/` — especialmente papers sobre scaffolding de IA y mobile-first pedagogy
