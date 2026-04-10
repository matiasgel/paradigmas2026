# Reporte de Scope y Lenguaje — Guardrail Académico
**Tema:** 05 — Mónadas en TypeScript  
**Course ID:** paradigmas-2026  
**Fecha:** 2026-04-10  
**Agente:** academic-guardrail 🛡️  
**Prerequisito:** Loops 1, 2 y 3 completados  

---

## CHECK 1 — Lenguaje Informal

### Metodología

Se revisaron: `diseno.md`, `minuta.md`, `filminas.md`, `guia-estudio.md`, `guiaprofesor.md`.

**Criterio de excepción aplicado:** Las analogías explicativas (`sobre certificado`, `cadena de montaje`, `caja con reglas`) se clasifican como recurso pedagógico válido y NO se marcan como informalidad.

---

### Hallazgos

| # | Documento | Ubicación | Expresión detectada | Tipo | Severidad | Juicio |
|---|-----------|-----------|---------------------|------|-----------|--------|
| L-01 | `minuta.md` | F-18 (línea de diálogo del docente) | `"Neither is always better — depende del contexto"` | Codeswitching inglés/español en material académico | 🔴 Alta | INFORMALIDAD |
| L-02 | `guiaprofesor.md` | Sección "Señales de alerta" | `"suele generar un '¡ahh!' colectivo"` | Expresión coloquial en documento académico interno | 🟡 Media | INFORMALIDAD LEVE |
| L-03 | `filminas.md` | F-06 (cuerpo de filmina) | `"La magia: flatMap se encarga del cortocircuito"` | Uso retórico de "la magia" | 🟢 Baja | EXCEPCIÓN — recurso retórico pedagógico estándar; no se contempla corrección |
| L-04 | `filminas.md` / `guia-estudio.md` | F-06 / Bloque 1.2 | `"el sobre certificado 📨"` | Emoji en texto académico destinado a alumnos | 🟢 Baja | EXCEPCIÓN — decora una analogía pedagógica; los emojis en material de soporte visual tienen precedente aceptable |

---

### Detalle de hallazgo L-01 (AUTO-FIX aplicado)

**Documento:** `minuta.md`  
**Contexto:** Guión de diálogo del docente para la filmina F-18 (Either vs try/catch).

| Campo | Texto |
|-------|-------|
| **Original** | `> "Dos filosofías para el manejo de errores. Neither is always better — depende del contexto."` |
| **Corrección** | `> "Dos filosofías para el manejo de errores. Ninguna es siempre mejor — depende del contexto."` |
| **Justificación** | El docente se dirige al aula en español. Intercalar una frase completa en inglés en el guión de clase transmite informalidad e inconsistencia con el registro académico de la materia. |
| **Acción** | ✅ AUTO-FIX aplicado (solo reformulación; estructura, contenido técnico y tabla siguientes no modificados) |

---

### Detalle de hallazgo L-02 (MANUAL)

**Documento:** `guiaprofesor.md`  
**Contexto:** Bloque 4 — descripción del efecto pedagógico al revelar que `Promise.then` es `flatMap`.

| Campo | Texto |
|-------|-------|
| **Original** | `"El momento de revelar que Promise.then es un flatMap suele generar un '¡ahh!' colectivo. Aprovecharlo para fijar el concepto."` |
| **Corrección sugerida** | `"El momento de revelar que Promise.then es un flatMap suele producir una reacción de comprensión súbita en el grupo. Aprovechar ese instante para consolidar el concepto."` |
| **Justificación** | La guía del docente es un documento de uso profesional interno; aunque su registro puede ser más relajado, la expresión `¡ahh! colectivo` está por debajo del estándar de formalidad de los demás documentos del conjunto. |
| **Acción** | ⚠️ Corrección recomendada (no auto-fix — es decisión editorial del docente) |

---

## CHECK 2 — Desviación de Scope

### Metodología

Se contrastó el contenido efectivo de `minuta.md`, `filminas.md` y `guia-estudio.md` contra las secciones de alcance de `diseno.md`: "§3 — Incluye" y "§3 — No incluye".

---

### Conceptos marcados como **No incluye** en diseno.md — verificación

| Concepto prohibido | ¿Aparece? | Documento | Veredicto |
|--------------------|-----------|-----------|-----------|
| Teoría de categorías formal (endofunctores, morfismos naturales) | No | — | ✅ CONFORME |
| Monad transformers (implementación) | Solo mención en FAQ guiaprofesor.md como "lectura complementaria" | `guiaprofesor.md` | ✅ CONFORME — diseno.md permite la mención |
| Free monads / algebraic effects / effect handlers | No | — | ✅ CONFORME |
| Implementación completa de fp-ts/Effect | No — solo uso, no reimplementación | `guia-estudio.md`, `filminas.md` | ✅ CONFORME |
| Haskell como lenguaje de implementación | Solo contraste notacional (type classes) en jerarquía Functor→Monad | `guia-estudio.md`, `filminas.md` | ✅ CONFORME — diseno.md permite "contraste notacional mínimo (1 filmina)" |

---

### Conceptos marcados como **obligatorios** en diseno.md — verificación de omisión

| Concepto obligatorio | ¿Presente? | Documento(s) | Cobertura |
|----------------------|------------|--------------|-----------|
| Motivación: encadenamiento con null/nil | ✅ | minuta F-02 a F-05, filminas F-02 a F-05, guia-estudio B1 | Completa |
| Construcción inductiva: map → flatMap → leyes | ✅ | minuta F-06c, filminas F-06c, guia-estudio §1.3 | Completa |
| Maybe en TS y Clojure (lado a lado) | ✅ | minuta F-08 a F-14, filminas F-08 a F-14, guia-estudio B2 | Completa |
| Either en TS y Clojure (lado a lado) | ✅ | minuta F-15 a F-22, filminas F-15 a F-22, guia-estudio B3 | Completa |
| IO en TS y Clojure (lado a lado) | ✅ | minuta F-23 a F-26, filminas F-23 a F-26, guia-estudio B4 | Completa |
| Leyes monádicas verificadas en TS y Clojure | ✅ | minuta F-27 a F-29, filminas F-27 a F-29, guia-estudio §B4(cont.) | Completa |
| Mónadas "escondidas": Promise, Array.flatMap, `?.` | ✅ | minuta F-30/31, filminas F-30/31, guia-estudio §B4(cont.) | Completa |
| fp-ts / Effect (mención) | ✅ | filminas F-33/34, guia-estudio B5 | Completa |
| Bloque IA (15 min) | ✅ | minuta/filminas F-35, guia-estudio B5 | Completa |
| Comparativas TS vs Clojure por mónada | ✅ | filminas F-14, F-22, F-26; tablas en todas las guías | Completa |

---

### Borderline — Applicative en jerarquía

| Ítem | Detalle | Juicio |
|------|---------|--------|
| `Applicative` en jerarquía Functor→Monad | Aparece en tabla de guia-estudio.md y filmina F-32 como nivel intermedio | ✅ CONFORME — diseno.md §5 "Cierre" dice explícitamente: "jerarquía Functor → Applicative → Monad". No es desvío. |

---

### Cobertura de guia-estudio.md vs contenido de clase

| Criterio | Estado | Observación |
|----------|--------|-------------|
| Cubre solo lo acordado en clase — sin adelantar T06 | ✅ | Ninguna referencia prematura a FP en Python (T06 se adelanta solo en el cierre de guiaprofesor.md como mención) |
| No incluye material de clases anteriores fuera de contexto | ✅ | Las referencias a T03/T04 son de prerequisito (sección "Conceptos previos"), no contenido nuevo |
| Nivel Bloom en autoevaluación (Recordar → Comprender → Aplicar → Analizar) | ⚠️ PARCIAL | La autoevaluación cubre bien Comprender (Q1, Q3, Q7), Aplicar (Q2, Q6) y Analizar (Q5, Q8). Sin embargo, falta al menos una pregunta de **Recordar** puro (ej.: "¿Cuáles son las tres mónadas canónicas vistas en clase?" / "Enumerá las tres leyes monádicas"). Ver density-report.md §Guia-estudio. |

---

## Juicio final — CHECK 1 y CHECK 2

| Check | Color | Score | Resumen |
|-------|-------|-------|---------|
| Lenguaje informal | 🟢 VERDE | 92/100 | 1 informalidad corregida automáticamente (L-01). 1 corrección editorial recomendada (L-02). Analogías y recursos pedagógicos: conformes. |
| Desviación de scope | 🟢 VERDE | 97/100 | Sin desvíos reales. Todo contenido obligatorio de diseno.md está presente. Conceptos prohibidos (teoría formal, monad transformers en profundidad, free monads) ausentes. Única observación: autoevaluación en guia-estudio falta nivel Recordar. |

---

## Acciones aplicadas

### AUTO-FIX ejecutado

**Archivo:** `minuta.md` — hallazgo L-01  
**Cambio:** `"Neither is always better"` → `"Ninguna es siempre mejor"`

---

*Generado por academic-guardrail 🛡️ — paradigmas-2026 — 2026-04-10*
