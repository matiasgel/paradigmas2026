# Plan Borrador — Paradigmas y Lenguajes de Programación 2026

> 📋 **DOCUMENTO OPERATIVO** — Este plan puede modificarse durante el cursado.
> Se actualiza a medida que los temas avanzan en producción.
> Trazado desde: `plan-minimo.md` (IF020 — UNTDF / IDEI)
> Última actualización: 2026-03-09

---

## Datos Operativos

| Campo | Valor |
|-------|-------|
| Duración de clase | 120 minutos |
| Perfil docente | profesor-teorico |
| Total de semanas | 17 |
| Total de temas (con contenido) | 15 |
| Cobertura plan mínimo | 3/15 temas cerrados |

---

## Mapa de Temas

| # | Nombre | Módulo | Semana | Clase | Duración | Estado | Carpeta |
|---|--------|--------|--------|-------|----------|--------|---------|
| 01 | Conceptos Introductorios + Intro a TypeScript | I | 1 | 1 | 120 min | ✅ cerrado | `temas/01-conceptos-introductorios/` |
| 02 | Sintaxis y Semántica de Lenguajes | V | 1 | 2 | 120 min | 🔲 pendiente | `temas/02-sintaxis-semantica/` |
| 03 | Introducción a Programación Funcional con TypeScript | II | 2 | 1 | 120 min | � en-curso | `temas/03-intro-funcional-ts/` |
| 04 | Aspectos Avanzados de Programación Funcional | II | 3 | 1 | 120 min | 🔲 pendiente | `temas/04-funcional-avanzado/` |
| 05 | Mónadas en TypeScript | II | 4 | 1 | 120 min | 🔲 pendiente | `temas/05-monadas-ts/` |
| 06 | Paradigma Lógico: Prolog — Clase 1 (Introducción) | III | 5 | 1 | 120 min | ✅ cerrado | `temas/06-paradigma-logico-prolog/` |
| 07 | Paradigma Lógico: Prolog — Clase 2+3 (Unificación, Backtracking, Listas, Recursión) | III | 6 | 1 | 240 min | ✅ cerrado | `temas/07-paradigma-logico-avanzado/` |
| 08 | Paradigma OO con TypeScript | IV | 7 | 1 | 120 min | 🔲 pendiente | `temas/08-paradigma-oo-ts/` |
| — | **⚠️ SEMANA 8: Parcial Práctico Nº 1** (Paradigmas I–IV) | I–IV | 8 | — | — | 🗓️ evaluación | — |
| 09 | Variables, Binding y Ámbito | VI | 9 | 1 | 120 min | 🔲 pendiente | `temas/09-variables-binding/` |
| 10 | Tipos de Datos | VII | 10 | 1 | 120 min | 🔲 pendiente | `temas/10-tipos-de-datos/` |
| 11 | Estructuras de Control | VIII | 11 | 1 | 120 min | 🔲 pendiente | `temas/11-estructuras-control/` |
| 12 | Manejo de Excepciones | IX | 12 | 1 | 120 min | 🔲 pendiente | `temas/12-manejo-excepciones/` |
| 13 | Abstracción Procedural y Modularidad | X | 13 | 1 | 120 min | 🔲 pendiente | `temas/13-abstraccion-modularidad/` |
| 14 | Sistemas de Tipos y Polimorfismo | VII | 14 | 1 | 120 min | 🔲 pendiente | `temas/14-sistemas-tipos-polimorfismo/` |
| 15 | Concurrencia y Paralelismo | XI | 15 | 1 | 120 min | 🔲 pendiente | `temas/15-concurrencia-paralelismo/` |
| — | **⚠️ SEMANA 16: Parcial Práctico Nº 2** (Trabajo oral sobre lenguajes) | I–XI | 16 | — | — | 🗓️ evaluación | — |
| — | **⚠️ SEMANA 17: Cierre** (Trabajo final / Reunión de cátedra) | I–XI | 17 | — | — | 🗓️ cierre | — |

---

## Estado de Cobertura del Plan Mínimo

| Contenido Mínimo Institucional | Cubierto por Tema(s) |
|-------------------------------|----------------------|
| Sintaxis y semántica / semántica operacional | 02 |
| Entidades y ligaduras | 09 |
| Sistemas de tipos | 10, 14 |
| Niveles de polimorfismo | 08, 14 |
| Encapsulamiento y abstracción | 08, 13 |
| Intérpretes y compiladores | 02 |
| Criterios de diseño e implementación de LP | 01 |
| Paradigmas: imperativo, OO, funcional, lógico | 01, 03, 04, 05, 06, 07, 08 |
| Concurrencia y paralelismo | 15 |

---

## Leyenda de Estado

| Ícono | Significado |
|-------|-------------|
| 🔲 pendiente | No iniciado |
| 🔄 en-curso | En producción (diseño/clase/TP/calidad) |
| ✅ cerrado | Ciclo completo completado |
| 🗓️ evaluación | Semana de parcial (sin producción de tema) |
| 🗓️ cierre | Semana de cierre de cursada |

---

## Notas del Docente

<!-- Matías: Usá esta sección para notas personales sobre el plan -->
- Inicio de cursada: 9 de marzo de 2026
- Plan generado manualmente desde el cronograma del plan-minimo.md
- **2026-03-09:** Cambio curricular aprobado — TypeScript reemplaza Kotlin como lenguaje principal
- **Stack de lenguajes:**
  - **TypeScript** — lenguaje principal (todos los temas salvo T06)
  - **Python** — Tema 06 (funcional aplicado) + bloque IA de todos los temas
  - **Haskell** — contraste en temas funcionales (T03, T04, T05, T10, T14) — solo lectura
  - **C** — contraste imperativo (T01, T09, T11) — solo lectura
  - **Smalltalk** — contraste OO (T08) — solo lectura
  - **Prolog** — paradigma lógico (T07)
- **Eje IA Generativa:** bloque de 15–20 min en cada clase (ver curriculum-proposal.md para detalle)
