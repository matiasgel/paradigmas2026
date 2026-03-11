# Density Report — Tema 01: Conceptos Introductorios + Intro a TypeScript

> **Agente:** academic-guardrail 🛡️ — Dimensión DENSIDAD COGNITIVA + FORMALIDAD
> **Fecha:** 2026-03-10
> **Perfil docente:** profesor-teorico
> **Perfil densidad guia:** student-guide (umbrales más permisivos — la guía es intencionalmente más extensa que la minuta)
> **auto-fix aplicado:** academic_guardrail_enabled = true
> **Estado:** 1 auto-fix aplicado · sin violaciones de densidad · sin formalidad critica

---

## Verificación de formalidad por documento

### minuta.md

El lenguaje informal en la minuta corresponde a **scripts de discurso del docente** (dentro de bloques `> *"..."*`), no al texto descriptivo. Este uso es intencional y apropiado. El texto descriptivo de la minuta mantiene registro formal.

**Veredicto:** ✅ Formalidad apropiada.

### filminas.md

Las filminas usan lenguaje directo y conciso. Las citas en tiempo presente ("↓", "→") y las notas de contraste son formato de presentación. No hay informalismos en el cuerpo del texto.

**Veredicto:** ✅ Formalidad apropiada.

### diseno.md

Documento de planificación interna con lenguaje formal consistente.

**Veredicto:** ✅ Formalidad apropiada.

### guia-estudio.md — 1 anglicismo corregido

**G-FORM-01 [auto-fixed]:** `"tiene un match natural con el paradigma funcional"` → anglicismo "match" reemplazado por "correspondencia".

Nota sobre vocabulario técnico aceptado:
- `prompt`, `output`, `input`, `codebase`, `linting` → anglicismos técnicos de uso establecido en la industria y la academia hispanohablante de informática. Aceptados en este perfil de documento.

**Veredicto:** ✅ Formalidad apropiada (post auto-fix G-FORM-01).

### tp.md

El register informal en las instrucciones al alumno ("Tenés 30 minutos y 1 intento") es tuteo institucional apropiado para materiales de evaluación universitaria argentina.

**Veredicto:** ✅ Formalidad apropiada.

---

## Verificación de densidad cognitiva

### Perfil aplicado: profesor-teorico + student-guide (guia-estudio.md)

**Umbrales del perfil:**
- Minuta: alta densidad aceptada (documento interno del docente)
- Filminas: media densidad (máx. 7 ítems por filmina)
- Guia-estudio: alta verbosidad aceptada por diseño (student-guide profile)
- TP: densidad de pregunta individual aceptable

| Documento | Densidad estimada | Evaluación |
|-----------|------------------|-----------|
| `diseno.md` | Media-alta | ✅ Apropiada — documento técnico de referencia |
| `minuta.md` | Alta | ✅ Apropiada — 120 min de clase, 5 bloques |
| `filminas.md` | Media (por filmina) | ✅ 29 filminas distribuidas en 5 bloques — ninguna excede 7 ítems conceptuales |
| `guia-estudio.md` | Alta (intencionalmente) | ✅ Profile student-guide — verbosidad para claridad ✓ |
| `tp.md` | Media (por pregunta) | ✅ 10 preguntas de 4 opciones — carga cognitiva equilibrada |

**Filmina más densa:** F-09 (tabla de 4 paradigmas × 5 columnas) — dentro del límite aceptable para una tabla de referencia en clase.

**Sección más densa de guia-estudio.md:** Sección 3.3 (ejemplo comparativo LC-3 / C / TypeScript) — alta densidad intencionalmente justificada por el valor pedagógico del ejemplo. ✅

**Veredicto general:** ✅ Sin violaciones de densidad cognitiva.

---

## Auto-fix aplicado (academic_guardrail_enabled = true)

| ID | Archivo | Tipo | Corrección |
|----|---------|------|-----------|
| G-FORM-01 | guia-estudio.md | Anglicismo en documento académico | "match natural" → "correspondencia natural" |

---

## Resumen ejecutivo Guardrail

| Check | Estado |
|-------|--------|
| Scope — todos los documentos | ✅ Sin desviaciones |
| Formalidad — minuta, filminas, diseno, tp | ✅ Apropiada |
| Formalidad — guia-estudio.md | ✅ Post auto-fix G-FORM-01 |
| Densidad cognitiva — todos los documentos | ✅ Dentro de umbrales |
| Vocabulario técnico (prompt, output, etc.) | ✅ Aceptado (perfil tech academic) |
