# Reporte de Coherencia — Loop 2a (Detección)

**Tema:** 05 — Mónadas en TypeScript  
**Course ID:** paradigmas-2026  
**Fecha:** 2026-04-10  
**Agente:** 🔗 coherence-fixer  
**Estado:** ✅ LOOP 2b COMPLETADO — 6/6 fixes aplicados (2026-04-10)  
**Prerrequisito:** Loop 1 completado — 14 writing-fixes aplicados

---

## Metodología de revisión

Documentos leídos en versión post-fix (Loop 1):

| Documento | Secciones revisadas |
|---|---|
| `diseno.md` | Completo — Secciones 1–6 y estructura de bloques |
| `minuta.md` | Completo — F-01 a F-32 + resumen de F-33..F-42 |
| `filminas.md` | Completo — F-01 a F-42 |
| `guia-estudio.md` | Completo — Bloques 1–5, ejemplos trabajados, autoevaluación, glosario |
| `guiaprofesor.md` | Completo — Plan detallado, checklist, señales de alerta |

**Chequeos realizados:**
1. Terminología unificada entre documentos
2. Referencias cruzadas (filmina ↔ guia-estudio, filmina ↔ guiaprofesor)
3. Consistencia de ejemplos de código (nombres de funciones, tipos, variables)
4. Secuencia didáctica (orden de introducción de conceptos)
5. Nivel de profundidad / tiempos por bloque vs. diseno.md
6. Coherencia interna de guia-estudio.md (autoevaluación vs. contenido)

---

## Tabla de Hallazgos

| ID | Estado | Tipo | Doc A | Doc B | Descripción | Corrección sugerida |
|---|---|---|---|---|---|---|
| **C-01** | ✅ FIJADO | INCONSISTENCIA | `diseno.md` Secc. 3, tabla comparativa Maybe (Bloque 2) | `filminas.md` F-14 · `guia-estudio.md` Bloque 2.4 · `minuta.md` F-14 | `diseno.md` usa `(m/bind v f)` donde `m` es el alias de `cats.monad.maybe`. Esa función **no existe** en ese namespace — `bind` pertenece a `cats.core` (alias `mc`). Todos los otros cuatro documentos usan `(mc/bind v f)` correctamente, que coincide con la API real de la librería. Una ejecución en REPL con `(m/bind v f)` lanzaría `ClassNotFoundException`. | Corregir `diseno.md`: cambiar `(m/bind v f)` → `(mc/bind v f)` en la celda "Encadenamiento" de la tabla comparativa Maybe. |
| **C-02** | ✅ FIJADO | INCONSISTENCIA | `guia-estudio.md` — Bloque 4 (cont.), encabezado de subsección: `"Jerarquía: Functor → Applicative → Monad (F-32)"` | `filminas.md` F-32 — título: `"Jerarquía: Functor → Monad"` · `minuta.md` F-32 — encabezado: `"Jerarquía: Functor → Monad"` | El título omite `Applicative` en filminas y minuta, pero lo incluye en guia-estudio. El **cuerpo** de F-32 sí menciona Applicative, por lo que la omisión en el título es una inconsistencia parcial. Un alumno que busca la filmina por el título visto en la guia-estudio no encontrará el match exacto. | Unificar al título completo en los tres documentos: `"De Functor a Monad"` (ya usado como subtexto en F-32) o `"Jerarquía: Functor → Applicative → Monad"`. Recomendado: actualizar filminas.md F-32 y minuta.md F-32 al título completo. |
| **C-03** | ✅ FIJADO | INCONSISTENCIA | `guia-estudio.md` — Bloque 1, encabezado: `"(F-02 a F-07)"` | `guiaprofesor.md` — Bloque 1: `"F-01 a F-07 (incluyendo F-06b, F-06c)"` | La guia-estudio cita el rango de Bloque 1 como `F-02 a F-07` sin mención de F-06b y F-06c, que son filminas autónomas con 3 min cada una en minuta.md y contenido relevante (F-06b: código lado a lado; F-06c: diferencia técnica map vs flatMap). guiaprofesor los lista explícitamente. Un estudiante que repase por número de filmina podría pasar por alto dos filminas didácticamente críticas. | Actualizar guia-estudio.md: `"(F-02 a F-07)"` → `"(F-02 a F-07, incluye F-06b y F-06c)"` |
| **C-04** | ✅ FIJADO | DESAJUSTE | `diseno.md` — Bloque 1 duración: **20 min** (Apertura 5 + Encadenamiento 10 + Definición 5) | `minuta.md` — Bloque 1 suma de tiempos F-01..F-07c: **26 min** | El class-writer agregó F-06b (3 min) y F-06c (3 min) — filminas no contempladas en el diseño original — expandiendo Bloque 1 en 6 min. El total de clase según minuta supera en ~10 min el presupuesto de 120 min. | Actualizar `diseno.md` Bloque 1 a **26 min** y revisar si corresponde compensar en otro bloque o aceptar la extensión como mejora pedagógica documentada. |
| **C-05** | ✅ FIJADO | DESAJUSTE | `diseno.md` — Bloque 4 duración: **25 min** (IO-TS 7 + IO-Clj 7 + Leyes 6 + Escondidas 5) | `minuta.md` — Bloque 4 suma de tiempos F-23..F-32: **28 min** (IO 11 + Leyes 9 + Escondidas 5 + Jerarquía F-32 3) | Dos divergencias: (a) las leyes se expandieron de 6 a 9 min; (b) F-32 "Jerarquía" no tenía tiempo asignado en el diseño pero fue incluida en Bloque 4. La compresión de IO (-3 min respecto al diseño) compensa parcialmente, pero el neto es +3 min. | Actualizar `diseno.md` Bloque 4: agregar F-32 como ítem con 3 min, ajustar leyes a 9 min, comprimir IO a 6+5 min, total → 28 min. |
| **C-06** | ✅ FIJADO | DESAJUSTE | `diseno.md` — Sub-sección "Leyes monádicas" (Bloque 4): **6 min** | `minuta.md` — F-27 (3 min) + F-28 (3 min) + F-29 (3 min) = **9 min** | La minuta materializó las leyes en tres filminas separadas (definición + verificación TS + verificación Clojure), cada una con 3 min, sumando 9 min. El diseño estimaba 6 min para "enunciado + verificación en ambos lenguajes" sin discriminar filminas. La expansión es pedagógicamente justificada (verificación práctica en cada lenguaje), pero el diseño no la refleja. | Sub-tarea de C-05: dentro de la corrección de Bloque 4 en diseno.md, especificar "Leyes: 9 min (F-27 + F-28 + F-29)". |

---

## Verificaciones sin hallazgo (pasaron limpio)

| Chequeo | Resultado |
|---|---|
| Nombres de funciones TypeScript en código (`findUser`, `getAddress`, `getPostal`, `validateName`, `validateEmail`, `validateAge`, `ioFlatMap`) | ✅ Idénticos en filminas, minuta y guia-estudio |
| Constructores Clojure `m/just`, `m/nothing`, `e/right`, `e/left` | ✅ Consistentes en todos los docs |
| `mc/mlet` y `mc/return` como API cats | ✅ Consistentes en filminas, minuta y guia-estudio |
| `some->` como término único para threading macro Clojure | ✅ Sin variaciones |
| Analogía del "sobre certificado 📨" para `of`/`flatMap` | ✅ Idéntica en filminas F-06 y guia-estudio Bloque 1.2 |
| Estructura `type IO<T> = { run: () => T }` | ✅ Idéntica en filminas F-23, minuta F-23, guia-estudio Bloque 4.1 |
| Estructura `type Either<E, T>` y convención "right is right" | ✅ Consistente en los cuatro docs |
| Secuencia didáctica Maybe → Either → IO | ✅ Mismo orden en todos los docs |
| Referencias a filminas en guia-estudio (F-08, F-14, F-15, F-22, F-23, F-27, F-30, F-32, F-35) | ✅ Todas las filminas citadas existen en filminas.md |
| Referencias en guiaprofesor a filminas (F-01..F-42) | ✅ Todas existen en filminas.md |
| Autoevaluación guia-estudio (8 preguntas) vs contenido previo de la guía | ✅ Todos los conceptos preguntados fueron introducidos antes |
| Preguntas clave guiaprofesor F-40 vs cierre diseno.md | ✅ Las 3 preguntas del diseño están incluidas; la minuta agrega 2 más (extensión no contradictoria) |

---

## Clasificación y severidad

| ID | Tipo | Severidad | Justificación |
|---|---|---|---|
| C-01 | INCONSISTENCIA | 🔴 ALTA | Código inválido en runtime: `(m/bind v f)` falla en REPL Clojure con `Exception` |
| C-02 | INCONSISTENCIA | 🟡 MEDIA | Título no coincide entre docs — alumno no puede correlacionar filmina citada en la guía |
| C-03 | INCONSISTENCIA | 🟡 MEDIA | Filminas F-06b y F-06c son pedagógicamente centrales (mapa vs flatMap) y no aparecen en el rango |
| C-04 | DESAJUSTE | 🟠 BAJA-MEDIA | El exceso de tiempo en Bloque 1 se acumula y compromete el total de 120 min de clase |
| C-05 | DESAJUSTE | 🟢 BAJA | Actualización contable del diseño; no afecta comprensión pero mantiene diseno.md desactualizado |
| C-06 | DESAJUSTE | 🟢 BAJA | Sub-ítem de C-05; la expansión es pedagógicamente correcta y no genera confusión |

---

## Resumen ejecutivo

| Tipo | Cantidad |
|---|---|
| INCOHERENCIA (contradicción conceptual entre docs) | 0 |
| REFERENCIA-ROTA (referencia a filmina o elemento inexistente) | 0 |
| INCONSISTENCIA (mismo concepto distinto nombre / API errónea) | 3 |
| DESAJUSTE (diferencia de tiempos / profundidad entre docs) | 3 |
| **TOTAL** | **6** |

**Documentos involucraddos:**
- `diseno.md`: 2 hallazgos (C-01, C-04 origen)
- `guia-estudio.md`: 2 hallazgos (C-02 origen, C-03 origen)
- `filminas.md` + `minuta.md`: afectados por C-02, C-04, C-05, C-06

**Prioridad de corrección:**
1. C-01 (código inválido) — corrección inmediata
2. C-02 y C-03 (referencias de alumno) — antes de distribuir guia-estudio
3. C-04, C-05, C-06 (actualización de diseño) — pueden agruparse en un solo commit

---

*Loop 2b completado: 6/6 correcciones aplicadas el 2026-04-10 por coherence-fixer.*  
*Próximo paso: Loop 3 — reference-validator.*
