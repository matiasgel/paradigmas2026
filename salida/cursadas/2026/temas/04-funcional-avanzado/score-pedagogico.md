# Score Pedagógico — Tema 04: Aspectos Avanzados de Programación Funcional

**Generado:** 2026-04-09 | **Agente:** student-simulator (modo Batch — 4 perfiles)
**Fuentes:** calibración Tema 03 + minuta.md (42 filminas) + guia-estudio.md + tp.md (20 ejercicios)
**Metodología:** Simulación cognitiva por perfil basada en literatura académica (Mayer 2009, Sweller & Chen 2023, Mahatanankoon & Wolf 2021, Olipas 2022, Hoq et al. 2025)

---

## Resumen ejecutivo

| Métrica | Valor |
|---------|-------|
| **Score global cohorte** | **68/100** |
| Bloque más desafiante | B3 — Concurrencia y metaprogramación (57) |
| Bloque más accesible | B1 — Fundamentos avanzados (79) |
| Perfil con más riesgo | Disperso (score global: 48) |
| Perfil con más ventaja | Estratégico (score global: 83) |
| Zona de recuperación guía | Ansioso sube +14 pts con guía de estudio |
| TP predicción aprobación | 72% cohorte (≥60 pts) |

---

## Scores por perfil

### Estratégico 📊

| Dimensión | En clase | Guía autónoma | TP estimado |
|-----------|----------|---------------|-------------|
| B1 — Fundamentos avanzados | 90 | 93 | — |
| B2 — Abstracciones y efectos | 82 | 88 | — |
| B3 — Concurrencia y metaprog. | 72 | 80 | — |
| B4 — Práctica guiada | 85 | — | — |
| **Global** | **80** | **87** | **82-90/100** |

**Score global: 83**

- Bloque más bajo: B3 (72) — STM y agentes son conceptos nuevos sin paralelo directo en TS
- Misconceptions probables:
  - "core.async = Observable de RxJS" (simplificación excesiva)
  - "STM = database transaction" (analogía parcialmente correcta pero incompleta)
- Fortalezas: ADT y Result/Either conectan naturalmente con tipos que ya domina de Tema 03
- Alertas:
  - Retomar en Tema 05 la diferencia entre concurrencia cooperativa (go blocks) y preemptiva
  - Puede subestimar la complejidad de transducers por verlos como "map+filter optimizado"

### Ansioso 😰

| Dimensión | En clase | Guía autónoma | TP estimado |
|-----------|----------|---------------|-------------|
| B1 — Fundamentos avanzados | 72 | 82 | — |
| B2 — Abstracciones y efectos | 55 | 72 | — |
| B3 — Concurrencia y metaprog. | 40 | 58 | — |
| B4 — Práctica guiada | 60 | — | — |
| **Global** | **57** | **71** | **55-65/100** |

**Score global: 64**

- Bloque más bajo: B3 (40 en clase) — la dualidad canal/promesa + STM + agentes genera sobrecarga cognitiva
- Zona de recuperación: guía de estudio sube +14 pts (de 57 a 71)
- Misconceptions probables:
  - "Result y Maybe son lo mismo" (confunde ausencia con error)
  - Notación Clojure `(go (>! ch v))` genera ansiedad por densidad de paréntesis
  - "async/await ya es funcional" (confunde sintaxis limpia con pureza)
- Alertas:
  - Comunicar en clase: "La guía de estudio desarrolla cada concepto paso a paso — si hoy se pierden, ahí lo recuperan"
  - El scaffold visual de Result (3 estados: ok, error, pendiente) es crítico para este perfil
  - Ejercicios ej08 (Result) y ej09 (Maybe) del TP necesitan ejemplo resuelto en la guía antes de intentar

### Disperso 😶‍🌫️

| Dimensión | En clase | Guía autónoma | TP estimado |
|-----------|----------|---------------|-------------|
| B1 — Fundamentos avanzados | 65 | 68 | — |
| B2 — Abstracciones y efectos | 42 | 50 | — |
| B3 — Concurrencia y metaprog. | 28 | 38 | — |
| B4 — Práctica guiada | 50 | — | — |
| **Global** | **44** | **52** | **40-55/100** |

**Score global: 48**

- Bloque más bajo: B3 (28 en clase) — pierde el hilo en la transición canal→STM→agentes
- Prerequisito gap:
  - Inmutabilidad no consolidada de Tema 03 (arrastra "const = inmutable incluyendo contenido")
  - Efecto secundario no consolidado de Tema 01
- Misconceptions probables:
  - "const arr = [...] hace que el array sea inmutable" (confunde binding con contenido)
  - "transducer = pipeline con less code" (no capta la ganancia de eficiencia)
  - "go block = goroutine de Go" (analogía superficial)
- Alertas:
  - Pregunta detectora en B1 min~12: "Si hago `const a = [1,2]; a.push(3)`, ¿falla?" → detectar misconception
  - Punto de reactivación B2 F-15: Result como "tipo que obliga a pensar en errores" — conectar con experiencia de bugs
  - En B3 limitar a core.async básico — no intentar STM con este perfil en la misma clase
  - TP: ejercicios ej15 (core.async) y ej16 (STM) serán los más abandonados por este perfil

### Recursero 📝

| Dimensión | En clase | Guía autónoma | TP estimado |
|-----------|----------|---------------|-------------|
| B1 — Fundamentos avanzados | 72 | 75 | — |
| B2 — Abstracciones y efectos | 58 | 65 | — |
| B3 — Concurrencia y metaprog. | 48 | 55 | — |
| B4 — Práctica guiada | 62 | — | — |
| **Global** | **58** | **65** | **60-70/100** |

**Score global: 62**

- Bloque más bajo: B3 (48) — memoriza la sintaxis de core.async pero no la semántica de comunicación
- Zona de comodidad: pipeline filter/map/reduce (B1) conecta directamente con lo que ya vio en Tema 03
- Misconceptions probables:
  - "Transducer ahorra memoria porque usa menos funciones" (no capta evaluación lazy vs eager)
  - "STM es como un lock pero más lindo" (no capta el retry semántico)
- Alertas:
  - Puede aprobar ej01-ej06 sin entender composabilidad real — trampa detectora en parcial
  - Pregunta abierta: "¿Por qué `(transduce xf + 0 data)` no crea colecciones intermedias?"
  - TP: ejercicios integradores ej19 y ej20 serán el filtro real de comprensión vs memorización

---

## Análisis por bloque

### B1 — Fundamentos avanzados (F-01 a F-13) — Score cohorte: 79

**Fortaleza:** Pipeline filter/map/reduce conecta con conocimiento previo de Tema 03. Los 4 perfiles arrancan en zona accesible.

**Riesgo:** La transición a Clojure en F-11/F-12/F-13 puede generar caída de atención en disperso y ansioso por cambio de sintaxis.

**Intervención sugerida:** Antes de F-11, hacer pausa de 1 min: "Ahora vamos a ver lo mismo pero en Clojure — la idea es la misma, cambia la forma de escribirlo."

### B2 — Abstracciones y efectos (F-14 a F-24) — Score cohorte: 65

**Fortaleza:** ADT y Result son conceptos con alto valor práctico que motivan al estratégico y al recursero.

**Riesgo:** Transducers (F-19 a F-21) — concepto denso sin paralelo directo en la experiencia previa de la mayoría. La carga cognitiva intrínseca es alta (Sweller & Chen 2023).

**Intervención sugerida:**
- Para transducers: anclar con "imaginen que filter+map se ejecutan en una sola pasada" antes de mostrar la mecánica
- Para Result/Maybe: mostrar primero el problema (try/catch pierde información de tipo) y después la solución

### B3 — Concurrencia y metaprogramación (F-25 a F-34) — Score cohorte: 57

**Riesgo alto.** Es el bloque más denso conceptualmente: canales, go blocks, STM, agentes, async/await, efectos puros — todo en 30 min.

**Predicción:** Disperso y ansioso pierden el hilo después de F-28 (STM). El recursero retiene la sintaxis de core.async pero no la semántica.

**Intervención sugerida:**
- Declarar explícitamente: "De este bloque necesitan llevarse UNA idea: la concurrencia funcional evita locks compartiendo valores inmutables"
- Reducir la expectativa: esto se profundiza en temas siguientes
- F-33 (canal vs promesa) es la filmina clave de síntesis — asegurar que todos sigan ahí

### B4 — Práctica guiada (F-35 a F-42) — Score cohorte: 72

**Fortaleza:** El taller en parejas reactiva la atención de los 4 perfiles. El disperso se re-engancha con actividad práctica.

**Riesgo:** Si B3 dejó muchos conceptos sin consolidar, el taller puede ser frustrante. Los ejercicios integradores (F-35 a F-37) requieren combinar todo B1+B2.

**Intervención:** Ofrecer dos niveles de taller: (a) solo pipeline + Result; (b) pipeline + Result + async. El disperso hace (a), el estratégico ataca (b).

---

## Análisis de la guía de estudio

| Perfil | Score sin guía | Score con guía | Delta |
|--------|---------------|----------------|-------|
| Estratégico | 80 | 87 | +7 |
| Ansioso | 57 | 71 | **+14** |
| Disperso | 44 | 52 | +8 |
| Recursero | 58 | 65 | +7 |

**Hallazgo clave:** La guía de estudio tiene impacto compensatorio mayor en el perfil ansioso (+14 pts). Los ejemplos paso a paso de Result y Maybe (§2.2 y §2.3 de la guía) son los que más contribuyen a la recuperación.

**Recomendación:** Comunicar explícitamente en clase (F-42) que la guía desarrolla con más detalle los temas de B2 y B3.

---

## Análisis del TP

| Bloque TP | Ejercicios | Dificultad media | Predicción aprobación |
|-----------|-----------|-------------------|----------------------|
| B1 — Pipeline y composición | ej01-ej06 | Media-baja | 85% |
| B2 — ADT y errores | ej07-ej12 | Media | 70% |
| B3 — Concurrencia | ej15-ej18 | Alta | 55% |
| B4 — Integradores | ej19-ej20 | Alta | 50% |
| Transducers/HOF/API | ej11-ej14 | Media-alta | 60% |

**Predicción global aprobación (≥60/100): 72%**

**Ejercicios críticos:**
- ej08 (Result<T,E>) — discriminador entre comprensión real y superficial de ADT
- ej15 (core.async canales) — el más abandonado por disperso y ansioso
- ej19 (integrador TS) — combina pipeline + Result + async; filtro real de comprensión
- ej20 (integrador Clojure) — requiere dominio cruzado de todo el tema

---

## Predicciones de clase

### Riesgo alto
- **Bloque:** B3 — Concurrencia y metaprogramación
- **Perfiles en riesgo:** disperso, ansioso
- **Score cohorte promedio:** 57
- **Intervención:** Reducir expectativa explícitamente; anclar en una idea central (inmutabilidad → no locks); F-33 como filmina de síntesis obligatoria

### Zona activa
- **Bloque:** B1 — Fundamentos avanzados
- **Perfiles que se estabilizan:** todos (conecta con Tema 03)
- **Oportunidad:** Usar B1 como base sólida antes de la escalada de complejidad en B2-B3

### Zona de recuperación (guía)
- **Perfil:** ansioso
- **Temas:** Result/Maybe (B2) y concurrencia (B3)
- **Detalle:** El score del ansioso sube de 57 (clase) a 71 (guía autónoma). La guía cumple función compensatoria clave — debe comunicarse explícitamente.

---

## Sub-scores desglosados

| Perfil | En clase | Guía autónoma | TP estimado | Global |
|--------|----------|---------------|-------------|--------|
| Estratégico | 80 | 87 | 82-90 | **83** |
| Ansioso | 57 | 71 | 55-65 | **64** |
| Disperso | 44 | 52 | 40-55 | **48** |
| Recursero | 58 | 65 | 60-70 | **62** |
| **Cohorte** | **60** | **69** | **59-70** | **68** |

---

*Próxima calibración: post-clase-tema04-2026 (comparar con encuesta de satisfacción real)*
