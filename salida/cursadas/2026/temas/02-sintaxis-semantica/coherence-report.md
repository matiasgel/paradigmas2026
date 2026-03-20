# Coherence Report — Tema 02: Sintaxis y Semántica de Lenguajes

**Agente:** coherence-fixer 🔗  
**Fecha:** 2026-03-20  
**Documentos revisados:** diseno.md, minuta.md, filminas.md, guia-estudio.md, tp.md  
**Prerequisito:** Loop 1 completado ✅

---

## Resumen

| Categoría | Cantidad | Estado |
|-----------|----------|--------|
| [CO-AUTO] Auto-corregibles | 1 | ✅ aplicado |
| [CO-REVIEW] Requieren aprobación | 2 | ⏳ pendiente |

---

## [CO-AUTO] — Correcciones aplicadas automáticamente

### CO-01 · filminas.md · línea 14 — Estado de aprobación del input

- **Problema:** El encabezado de `filminas.md` dice `(REDISEÑO — pendiente de aprobación)` pero `diseno.md` figura con `**Estado:** APROBADO`.
- **Causa:** Las filminas fueron generadas antes de que el docente aprobara el rediseño; el metadata no se actualizó.
- **Corrección:** `(REDISEÑO — APROBADO)`
- **Estado:** ✅ auto-corregido

---

## [CO-REVIEW] — Requieren aprobación del docente

### CO-02 · filminas.md · F-01 — Suma de tiempos en la agenda

- **Problema:** La tabla de la filmina F-01 (Agenda) lista 6 bloques que suman **107 minutos**, pero el label final dice `**Total:** 120 minutos`.  
  - Bloques: 20 + 20 + 30 + 10 + 12 + 15 = **107 min**  
  - Total clase: **120 min** (incluye apertura 5 min + cierre/buffer 13 min)
- **Impacto:** Estudiantes pueden calcular la suma y notar la diferencia (13 min no aparecen en la tabla).
- **Opciones de corrección:**
  - A) Agregar fila `| Apertura + Cierre | 13 | Conexión Tema 01 + preguntas finales + buffer |`
  - B) Cambiar el label por `**Total bloques:** 107 min · *Clase completa: 120 min (incluye apertura y cierre)*`
  - C) Mantener como está (el "Total: 120 minutos" expresa la duración de la clase, no la suma de la tabla)
- **Recomendación del agente:** Opción A — agrega transparencia sin quitar información
- **Estado:** ⏳ pendiente aprobación docente

---

### CO-03 · guia-estudio.md · sección 4.3.3 — Metasímbolos BNF vs. EBNF

- **Problema:** La sección `4.3.3 El metalenguaje BNF` incluye en su tabla los símbolos `.`, `*` y `+` como metasímbolos de **BNF**, pero:
  - `.` (fin de definición) no es un metasímbolo estándar BNF en ninguna referencia del curso
  - `*` y `+` son extensiones **EBNF**, no BNF puro
  - La filmina F-14 (fuente canónica de la clase) solo lista `::=`, `|`, `< >` como metasímbolos BNF
- **Inconsistencia con filminas:** Un estudiante que compara F-14 con la sección 4.3.3 verá símbolos extra sin explicación.
- **Corrección sugerida:** Retirar `.`, `*`, `+` de la tabla BNF de la sección 4.3.3 y añadir una nota: *"`*` y `+` son extensiones EBNF — ver sección 4.4."*
- **Estado:** ⏳ pendiente aprobación docente

---

## Verificación de referencias de filminas en guia-estudio.md

| Referencia | Filmina existe | OK |
|------------|----------------|----|
| F-02, F-03, F-04, F-05, F-06, F-06b | ✅ todas presentes | ✅ |
| F-07 a F-11 | ✅ todas presentes | ✅ |
| F-12 a F-20 | ✅ todas presentes | ✅ |
| F-19, F-20 | ✅ presentes | ✅ |
| F-21, F-22, F-23 | ✅ todas presentes | ✅ |
| F-24 a F-28 | ✅ todas presentes | ✅ |
| F-29 a F-34 | ✅ todas presentes | ✅ |

**Resultado: 0 referencias rotas** ✅

---

## Verificación de referencias de filminas en tp.md

| Sección TP | Filminas | OK |
|------------|----------|----|
| A — Léxico | F-07 a F-11 | ✅ |
| B — Sintaxis vs. Semántica | F-02 a F-06b | ✅ |
| C — BNF Conceptos | F-12 a F-15 | ✅ |
| D — BNF Derivaciones | F-16 a F-17 | ✅ |
| E — Ambigüedad | F-18 | ✅ |
| F — EBNF | F-19 a F-20 | ✅ |
| G — Aplicaciones | F-30, F-32, F-34 | ✅ |
