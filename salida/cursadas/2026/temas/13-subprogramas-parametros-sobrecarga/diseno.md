# Diseño de Clase — Tema 13: Subprogramas, Parámetros y Sobrecarga (Clase 13A)

> **Estado:** EN PRODUCCION
> **Diseñador:** Dr. Roberto ✍️ (class-writer) — corrección desde `clase_dada.txt`
> **Fecha:** 2026-06-28
> **Módulo:** X | **Semana:** 13 | **Clase Nº 1 de 1**
> **Nota de estado:** El `diseno.md` previo no existía en el topic_folder. Se crea desde cero, alineado al baseline `clase_dada.txt` y a las filminas/minuta corregidas. Estado `EN PRODUCCION` porque el contenido del `.txt` difiere del título nominal del tema (ver *Drift detectado*).

---

## Datos del Tema

| Campo | Valor |
|-------|-------|
| Número | 13 |
| Nombre | Subprogramas, Parámetros y Sobrecarga (Clase 13A) |
| Duración | 120 minutos (constraint absoluto, `topic.yaml: duration_min`) |
| Lenguaje principal | TypeScript |
| Lenguajes de contraste | — (la clase dada se centra en TypeScript) |
| Módulo curricular | X |
| Pipeline version | v3 |
| Source topic | 13-abstraccion-modularidad |

---

## Drift detectado vs. título nominal

El `clase_dada.txt` (baseline de la clase dada, 324 líneas) **no trata sobre subprogramas, parámetros ni sobrecarga**. Trata sobre:

- Tipo Abstracto de Datos (TAD/ADT).
- Encapsulamiento vs. ocultamiento de información.
- Implementación de `Stack<T>` en TypeScript.
- Interfaz pública y copia defensiva.
- Independencia de representación.
- Separación especificación/implementación.
- Módulo como frontera de visibilidad y compilación separada.
- Genéricos y restricciones (`T extends Comparable<T>`).

El `filminas.md` previo (respaldado en `filminas-prev-backup.md`) sí trataba sobre subprogramas, parámetros, sobrecarga, callbacks, async y activation records — pero **no reflejaba el `.txt`**. Siguiendo la instrucción docente de fidelidad al `clase_dada.txt`, las filminas y la minuta se reescribieron para reflejar el contenido real de la clase dada. El título del tema se conserva por consistencia con `topic.yaml`.

---

## Objetivos de Aprendizaje

Al finalizar esta clase el estudiante podrá:

1. **Explicar** el problema del acoplamiento a la representación y por qué rompe la abstracción.
2. **Definir** un Tipo Abstracto de Datos (TAD) por nombre, operaciones, semántica observable e invariantes.
3. **Clasificar** las operaciones de un TAD en constructoras, transformadoras y observadoras, justificando qué pertenece a la interfaz.
4. **Distinguir** encapsulamiento, ocultamiento de información, interfaz pública e invariante como cuatro preguntas de diseño distintas.
5. **Implementar** un TAD pila en TypeScript usando `#` para privacidad real y `T | undefined` para errores definidos.
6. **Aplicar** la copia defensiva para proteger la representación privada al exponer vistas.
7. **Justificar** la independencia de representación a partir de un contrato estable.
8. **Separar** especificación (`interface`) e implementación (`class`) en TypeScript.
9. **Explicar** el módulo como frontera de visibilidad y los cuatro tipos de imports.
10. **Usar** genéricos y restricciones (`T extends Comparable<T>`) para reutilizar abstracción sin mezclar tipos.

---

## Bibliografía de respaldo (ChromaDB, `--type material`)

Consultada en `_edu-knowledge/` vía `scripts/knowledge_base.py search`. No se cita inline en filminas (regla editorial); la trazabilidad completa vive en `minuta.md`.

- **Sebesta, R. W. — *Concepts of Programming Languages* (Pearson, 2019), Cap. 11, pp. 471-506.** Abstract data types, encapsulation, modules.
- **Sebesta, Cap. 9, pp. 389-440.** Generic subprograms, parametric polymorphism, ad hoc polymorphism (sobrecarga).
- **Gabbrielli, M. & Martini, S. — *Programming Languages: Principles and Paradigms* (Springer, 2nd ed., 2023), Cap. 9, pp. 283-294.** ADTs y módulos; imports y visibilidad.
- **Gabbrielli & Martini, Cap. 9, pp. 295-350.** Encapsulation and information hiding; módulos como partición estática.
- **Louden, K. C. & Lambert, K. A. — *Programming Languages: Principles and Practices* (Course Technology, 2012), Cap. 11, pp. 496-545.** ADT mechanisms and modules; modificabilidad, reusabilidad y seguridad.

---

## Plan de Filminas (16 slides)

| F-# | Título | Tipo | Duración |
|-----|--------|------|----------|
| F-00 | Portada 13A | portada | 3 min |
| F-01 | Ruta de la clase | tabla | 8 min |
| F-02 | El problema: acoplamiento a la representación | concepto-mixto | 8 min |
| F-03 | TAD: Tipo Abstracto de Datos | concepto-abstracto | 8 min |
| F-04 | La pila como ejemplo mínimo | tabla-comparativa | 7 min |
| F-05 | Operaciones de un TAD | tabla-comparativa | 7 min |
| F-06 | Encapsulamiento ≠ ocultamiento de información | tabla-comparativa | 8 min |
| F-07 | Implementación de Stack en TypeScript | codigo | 8 min |
| F-08 | ¿Qué debe exponer una interfaz? | tabla-comparativa | 8 min |
| F-09 | Copia defensiva | codigo | 7 min |
| F-10 | Independencia de representación | tabla-comparativa | 8 min |
| F-11 | Separación entre especificación e implementación | codigo | 8 min |
| F-12 | Módulo como frontera de visibilidad | concepto-mixto | 8 min |
| F-13 | Imports, dependencias y compilación separada | tabla-mixta | 8 min |
| F-14 | Genéricos | concepto-mixto | 8 min |
| F-15 | Repaso y cierre | cierre | 8 min |
| **Total** | | | **120 min** |

---

## Hilo conductor

Del problema del acoplamiento a la representación → al TAD como contrato → a la clasificación de operaciones → a la distinción encapsulamiento/ocultamiento → a la implementación en TypeScript → a la frontera de la interfaz → a la copia defensiva → a la independencia de representación → a la separación especificación/implementación → al módulo como frontera de visibilidad → a los imports y la compilación separada → a los genéricos como polimorfismo paramétrico → al repaso.

---

## Materiales producidos

- `filminas.md` — reescrito desde `clase_dada.txt` (backup previo en `filminas-prev-backup.md`).
- `minuta.md` — **CREADO desde cero**, per-filmina, autocontenida, suma 120 min.
- `diseno.md` — **CREADO desde cero** (no existía), estado `EN PRODUCCION`.

---

## Próximos pasos

1. Validación académica (guardrail) sobre `filminas.md` y `minuta.md`.
2. Generación de guía de estudio (handoff a `@edu-agent-study-guide-writer`).
3. Diseño de TP trazable a la minuta (handoff a `@edu-agent-tp-designer`).
4. Publicación de filminas (cuando el docente lo indique, vía `publish_loop.py`).