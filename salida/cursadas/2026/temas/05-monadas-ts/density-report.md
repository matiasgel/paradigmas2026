# Reporte de Densidad Cognitiva — Guardrail Académico
**Tema:** 05 — Mónadas en TypeScript  
**Course ID:** paradigmas-2026  
**Perfil docente:** `profesor-teorico`  
**Fecha:** 2026-04-10  
**Agente:** academic-guardrail 🛡️  

---

## Parámetros de referencia — perfil `profesor-teorico`

| Métrica | Umbral |
|---------|--------|
| Palabras por filmina (prose) | ≤ 50 palabras |
| Conceptos nuevos por bloque (~20 min) | ≤ 5 conceptos |
| Duración estimada por filmina | 4–5 min |
| **Avalancha cognitiva** | > 4 conceptos nuevos en un bloque sin recap intermedio |

> El perfil `student-guide` (guia-estudio.md) acepta mayor verbosidad intencionalmente; se evalúa con criterios más lenientes.

---

## Curva de densidad por bloque temporal

### Documentos: `minuta.md` + `filminas.md`

| Bloque | Tiempo nominal | Filminas | Conceptos nuevos introducidos | Recap presente | Densidad (conceptos/20 min) | Estado |
|--------|---------------|----------|-------------------------------|----------------|----------------------------|--------|
| **B1 — Motivación** | 26 min | F-01 a F-07 (incl. F-06b, F-06c) | 1. Problema del encadenamiento / cortocircuito manual<br>2. `of` / `return` como envoltorio<br>3. `flatMap` / `bind` como encadenamiento + aplanamiento<br>4. Cortocircuito automático de mónada<br>5. `map` vs `flatMap` (doble envoltorio)<br>6. Los tres contextos: Maybe · Either · IO | Sí — F-07 (tabla contenedor) + F-06b (código antes/después) | 4.6 / 20 min | ⚠️ DENSO |
| **B2 — Maybe** | 25 min | F-08 a F-14 | 1. Tagged union `Just/Nothing`<br>2. Operaciones Maybe: `of`, `map`, `flatMap`<br>3. `some->` como Maybe implícito Clojure<br>4. `cats/maybe` como Maybe explícito Clojure | Sí — F-10 (pipeline), F-13 (comparación), F-14 (tabla) | 3.2 / 20 min | ✅ OK |
| **B3 — Either** | 25 min | F-15 a F-22 | 1. Tagged union `Left/Right`<br>2. `flatMap` para Either (propagación de error intacto)<br>3. Either vs `try/catch` (flujo explícito vs implícito)<br>4. `cats/either` + `mlet` en Clojure<br>5. Either idiomático sin cats: mapas `{:ok/:error}`<br>6. Filosofía: datos simples vs tipos formales | Sí — F-17 (aplicación), F-22 (tabla) | 4.8 / 20 min | ⚠️ DENSO |
| **B4a — IO** | 12 min | F-23 a F-26 | 1. `IO<T>` = thunk tipado (`{ run: () => T }`)<br>2. `.run()` como punto único de efectos (laziness)<br>3. `delay` / closures en Clojure — sin wrapper obligatorio | Sí — F-26 (tabla comparativa IO) | 5.0 / 20 min | ✅ OK |
| **B4b — Leyes + Ocultas + Jerarquía** | 14 min | F-27 a F-32 | 1. Ley 1: identidad izquierda<br>2. Ley 2: identidad derecha<br>3. Ley 3: asociatividad<br>4. `Promise` como (casi) mónada<br>5. `Array.flatMap` como mónada<br>6. Optional chaining `?.` como Maybe implícito<br>7. `some->` / `for` / `go` como patrones monádicos Clojure<br>8. Jerarquía Functor → Applicative → Monad | **No** — no hay filmina de recap entre las leyes y las mónadas ocultas | 11.4 / 20 min | 🔴 AVALANCHA |
| **B5 — Ecosistemas + IA** | 15 min | F-33 a F-38 | 1. fp-ts / Effect como industrialización del patrón<br>2. `cats` / `manifold` en Clojure | Sí — F-37/38 (síntesis + tablas decisión) | 2.7 / 20 min | ✅ OK |

---

## Hallazgos problemáticos

### 🔴 HALLAZGO D-01 — Avalancha cognitiva en Bloque 4b

**Tipo:** [DENSIDAD-ALTA]  
**Ubicación:** `minuta.md` y `filminas.md` — Bloque 4, subbloque F-27 a F-32  
**Tiempo asignado en guiaprofesor.md:** "F-27 a F-29 (9 min) + F-30 a F-31 (3 min) + F-32 (2 min)" = 14 min

**Descripción:**  
El subbloque F-27–F-32 introduce formalmente las 3 leyes monádicas (una por una, con verificación de código en dos lenguajes) y luego, sin recap intermedio, presenta 6 instancias de "mónadas ocultas" en APIs conocidas más la jerarquía formal Functor → Applicative → Monad. Son **8 conceptos distintos** en 14 minutos.

Las leyes monádicas son el subbloque más abstracto de toda la clase (reconocido en guiaprofesor.md como "el subbloque más abstracto — ir lento"). Sin embargo, el tiempo asignado a las tres leyes es de 9 minutos, lo que implica ~3 minutos por ley incluyendo enunciado, comprensión y verificación en código en dos lenguajes. Esta asignación contradice la propia advertencia del guiaprofesor.

**Riesgo pedagógico:** Alto. Los alumnos que no hayan consolidado la diferencia `map`/`flatMap` (introducida en B1) alcanzarán este subbloque con comprensión frágil. Las leyes requieren que ese concepto esté afianzado. Sin margen temporal de absorción, se acumulan tres abstracciones de alto nivel (identidad izquierda como propiedad algebraica, identidad derecha, asociatividad) antes de que el grupo pueda procesarlas.

**Bloque inmediatamente posterior (F-30–F-31, 3 min):** Introduce 6 instancias de reconocimiento de patrones monádicos en APIs (Promise, Array.flatMap, `?.`, `some->`, `for`, `go`) en 3 minutos — menos de 30 segundos por instancia. Funciona como recap motivacional solo si las leyes ya fueron absorbidas.

**Acción recomendada:**
1. Separar las leyes monádicas como mini-recap explícito antes de pasar a mónadas ocultas (agregar F-29b: tabla de verificación de las 3 leyes con ✓/✓/✓ en verde).  
2. Reasignar el tiempo del bloque: las leyes merecen 12–14 min, no 9. Esto puede absorberse reduciendo B5 de 15 a 13 min, o comprimiendo la comparativa IO de Clojure (F-25/F-26, que tiene menor impacto pedagógico).
3. Las "mónadas ocultas" pueden presentarse como tabla resumen única (1 filmina) con 2 min de cierre rápido — bastará para el efecto de reconocimiento.

---

### ⚠️ HALLAZGO D-02 — Densidad de palabras en filminas conceptuales

**Tipo:** [DENSIDAD-ALTA]  
**Perfil aplicable:** `profesor-teorico` — ≤ 50 palabras/slide (prosa, sin contar código)  
**Filminas afectadas:**

| Filmina | Palabras estimadas (prosa) | Umbral | Estado |
|---------|---------------------------|--------|--------|
| F-06 ("¿Qué es una mónada?") | ~130 palabras | ≤ 50 | 🔴 Excede 2.6× |
| F-07 ("Analogía del contenedor") | ~90 palabras | ≤ 50 | 🔴 Excede 1.8× |
| F-06c ("De map a flatMap") | ~65 palabras | ≤ 50 | ⚠️ Excede 1.3× |
| F-17 (Validador formulario) | ~30 palabras prosa | ≤ 50 | ✅ OK (código por separado) |
| F-21 ("datos simples o mónadas") | ~55 palabras | ≤ 50 | ⚠️ Borderline |

> **Nota metodológica:** F-06 y F-07 son las filminas de mayor carga conceptual de B1. La alta densidad de palabras en estas slides puede aumentar la carga cognitiva extrínseca si se leen en pantalla. Se recomienda fragmentar F-06 en dos filminas: F-06 (analogía del sobre) y F-06-def (definición de trabajo).

**Acción recomendada:** Fragmentar F-06 en dos filminas (split no cambia contenido ni conceptos). Reducir la prosa en F-07 a solo la tabla + 1 frase de cierre; el desarrollo verbal pasa a la minuta.

---

### ⚠️ HALLAZGO D-03 — Inconsistencia temporal en guiaprofesor.md para Bloque 4

**Tipo:** [DENSIDAD-ALTA]  
**Documento:** `guiaprofesor.md`  
**Evidencia:**  
- El propio guiaprofesor.md alerta: *"Este es el subbloque más abstracto — ir lento"* para F-27 a F-29.  
- Pero le asigna solo 9 minutos para tres leyes formales verificadas en TypeScript **y** en Clojure REPL.  
- `diseno.md` asigna 9 minutos a las leyes (bloque más largo de B4), pero `diseno.md` es una estimación de diseño. La guiaprofesor debería ajustar el timing real hacia 12–14 min como mínimo.

**Riesgo docente:** Un docente que siga el timing al pie de la letra intentará cubrir Ley 3 en ~2 min en dos lenguajes. Experiencia de clase proyectada: el docente sale en tiempo del Bloque 4 pero sin haber consolidado las leyes.

**Acción recomendada:** Actualizar guiaprofesor.md B4 con el timing ajustado: Leyes (12 min) + Ocultas (4 min) + Jerarquía (2 min) = 18 min, absorbiendo 3 min del margen del Bloque 5.

---

### ⚠️ HALLAZGO D-04 — Autoevaluación guia-estudio.md: cobertura de Bloom incompleta

**Tipo:** [NIVEL]  
**Documento:** `guia-estudio.md` — Sección "Autoevaluación"  
**Perfil:** `student-guide`

**Análisis de niveles Bloom en la autoevaluación actual:**

| Pregunta | Nivel Bloom | Estado |
|---------|-------------|--------|
| Q1 — "¿Qué problema resuelve flatMap que map no?" | Comprender | ✅ |
| Q2 — "Implementá Maybe.flatMap" | Aplicar | ✅ |
| Q3 — "Diferencia some-> vs cats/maybe" | Comprender / Analizar | ✅ |
| Q4 — "Escribí la ley de asociatividad" | Recordar (parcial) | ⚠️ Recordar las leyes sí, pero es más "Comprender" que recuperación pura |
| Q5 — "¿Promise cumple las tres leyes?" | Analizar | ✅ |
| Q6 — Trace de pipeline Either | Aplicar / Analizar | ✅ |
| Q7 — "¿Por qué Clojure no necesita IO?" | Comprender | ✅ |
| Q8 — "Clasificá estas APIs" | Analizar | ✅ |

**Brecha detectada:** Falta una pregunta de **Recordar** puro (recuperación directa). El nivel más básico de Bloom — retener definiciones clave — no tiene pregunta explícita. Un alumno puede memorizar `flatMap` sin poder enunciar los constructores o las 3 mónadas.

**Pregunta sugerida a agregar (no auto-fix — es decisión editorial):**
> Q0 — "Nombrá las tres mónadas canónicas estudiadas en clase y el 'contexto' que agrega cada una (¿qué tipo de efecto o situación modela?)."  
> *Nivel:* Recordar → entrada natural al resto de la autoevaluación.

---

## Evaluación densidad guia-estudio.md (perfil student-guide)

| Criterio | Estado | Observación |
|----------|--------|-------------|
| Mayor verbosidad permitida | ✅ | La guía es intencionalmente extendida — apropiado para el perfil |
| Ejemplos worked-out para Maybe | ✅ | Pipeline completo con tipos, casos Just y Nothing, salida anotada |
| Ejemplos worked-out para Either | ✅ | Validador de formulario con casos válido e inválido, trazado de ejecución |
| Ejemplos worked-out para IO | ✅ | Pipeline readLine → greet con explicación de lazy vs eager |
| Ejemplos worked-out para List monad | N/A | List monad no está en el scope principal (F-31 es solo mención rápida) |
| Secciones de autoevaluación con pirámide Bloom | ⚠️ | Buena cobertura general; falta nivel Recordar — ver D-04 |

---

## Evaluación densidad guiaprofesor.md (señales de alerta y timing)

| Criterio | Estado | Observación |
|----------|--------|-------------|
| Señales de alerta suficientes para puntos de alta dificultad | ✅ | 5 señales documentadas con acción concreta; cubren los puntos más críticos (map vs flatMap, leyes, debate TS vs Clojure, pragmatismo monádico) |
| Timing realista para Bloques 1–3 | ✅ | B1 (26 min), B2 (25 min), B3 (25 min) — ajustados y alcanzables |
| Timing realista para Bloque 4 completo | ⚠️ | B4 total = 25 min: IO-TS (6) + IO-Clojure (5) + Leyes (9) + Ocultas (3) + Jerarquía (2). El sub-bloque de leyes con advertencia "ir lento" con solo 9 min es inconsistente — ver D-03 |
| Timing realista para Bloque 5 | ✅ | 15 min para fp-ts/Effect + IA + debate + síntesis — alcanzable |

---

## Score general de densidad cognitiva

| Componente | Score | Color |
|-----------|-------|-------|
| Bloque 1 — B1 Motivación | 75 | 🟡 |
| Bloque 2 — B2 Maybe | 96 | 🟢 |
| Bloque 3 — B3 Either | 75 | 🟡 |
| Bloque 4a — B4a IO | 90 | 🟢 |
| Bloque 4b — B4b Leyes+Ocultas | 45 | 🔴 |
| Bloque 5 — B5 Ecosistemas | 96 | 🟢 |
| Densidad de palabras por filmina | 72 | 🟡 |
| Guia-estudio (student-guide profile) | 86 | 🟢 |
| Timing guiaprofesor.md | 72 | 🟡 |

### Score ponderado final

$$\text{Score} = \frac{75 + 96 + 75 + 90 + 45 + 96 + 72 + 86 + 72}{9} = \frac{707}{9} \approx 78.6$$

---

## 🟡 SCORE FINAL DENSIDAD: **79 / 100 — AMARILLO**

> **Semáforo:** 🟡 AMARILLO — Material políticamente viable para ser dictado, con un punto de riesgo alto localizado (B4b) que puede mitigarse con un split de filminas y rebalanceo de timing. No requiere revisión estructural del tema.

### Resumen de acciones requeridas por prioridad

| Prioridad | Hallazgo | Acción | Documento |
|-----------|----------|--------|-----------|
| 🔴 P1 | D-01 — Avalancha B4b (8 conceptos/14 min sin recap) | Agregar filmina recap F-29b entre leyes y ocultas; ajustar timing leyes a 12 min | `minuta.md`, `filminas.md`, `guiaprofesor.md` |
| ⚠️ P2 | D-02 — F-06 excede 2.6× límite palabras/slide | Fragmentar F-06 en F-06 (analogía) + F-06-def (definición); reducir prosa F-07 | `filminas.md` |
| ⚠️ P3 | D-03 — Inconsistencia timing guiaprofesor B4 | Actualizar timing B4: Leyes 12 min, rebalancear con B5 | `guiaprofesor.md` |
| 🟢 P4 | D-04 — Bloom gap (sin Recordar en autoevaluación) | Agregar Q0 de Recordar en sección Autoevaluación | `guia-estudio.md` |

---

*Generado por academic-guardrail 🛡️ — paradigmas-2026 — 2026-04-10*
