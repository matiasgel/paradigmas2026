# Score Pedagógico — Tema 03
## Introducción a Programación Funcional con TypeScript

**Agente:** student-simulator 🎓 + test-runner 🧪  
**Fecha:** 2026-03-13  
**Perfiles utilizados:** Calibración `_edu-memory/calibracion-simulador/tema-02-calibracion.yaml` (adaptada a Tema 03)  
**Artefactos simulados:** minuta.md · filminas.md · guia-estudio.md (doble perspectiva: en clase + estudio autónomo)

---

## Resumen Ejecutivo

| Perfil | Score en clase | Score guía autónoma | Score TP | Score global |
|--------|---------------|--------------------|----|---|
| 🔵 Estratégico | 82/100 | 88/100 | 85/100 | **85/100** |
| 🟡 Ansioso | 59/100 | 71/100 | 73/100 | **68/100** |
| 🔴 Disperso | 47/100 | 55/100 | 62/100 | **55/100** |
| ⚫ Recursero | 52/100 | 60/100 | 71/100 | **61/100** |
| **Promedio cohort** | **60/100** | **68/100** | **72/100** | **67/100** |

### 🚦 Semáforo de riesgo

| Bloque | Riesgo | Perfiles en zona crítica |
|--------|--------|--------------------------|
| B1 Motivación (10 min) | 🟢 Bajo | — |
| B2 Funciones puras & inmutabilidad (20 min) | 🟡 Medio | Ansioso, Disperso |
| B3 HOF & clausuras (30 min) | 🟡 Medio | Disperso |
| B4 Composición & currificación (20 min) | 🟠 Medio-alto | Ansioso, Disperso, Recursero |
| B5 Efectos & lazy evaluation (10 min) | 🟡 Medio | Ansioso |
| B6 Mónadas (20 min) | 🔴 Alto | Ansioso, Disperso, Recursero |
| B7 Cierre (10 min) | 🟢 Bajo | — |

---

## Simulación por Perfil

---

### 🔵 PERFIL ESTRATÉGICO — Score: 85/100

**Base de calibración:** Mahatanankoon & Wolf (2021) — estrategia deep learning; Tema 02 scores promedio 0.79.

#### Experiencia en clase

| Bloque | Predicción conductual | Score simulado |
|--------|----------------------|---------------|
| B1 | Lee la agenda antes de que el docente la explique. Conecta inmediatamente con Tema 01. | 90/100 |
| B2 | Entiende funciones puras rápido. **Alerta:** puede pensar que "ya le llegó" y dejar de prestar atención al ejemplo de `crearContador`. | 85/100 |
| B3 | Disfruta el ejercicio de `frecuencias` con `reduce`. Implementa la solución en 6 min. | 88/100 |
| B4 | **Zona de máximo interés**: currificación lo fascina — conecta con matemática. Pero puede confundir `compose` vs `pipe` en dirección bajo presión de tiempo. | 80/100 |
| B5 | Generadores: ya los conoce del Tema 01. Pregunta sobre relación con Iterators de ES6. | 82/100 |
| B6 | Mónadas: capta la intuición de Promise como mónada. **Alerta:** puede oversimplificar "mónada = Promise" y no entender `Maybe`/`Either` más adelante. | 75/100 |

**Comportamiento típico en clase:**
> *"Profe, ¿la currificación en TypeScript es igual que en Haskell? Porque vi que en Haskell todas las funciones son currificadas por defecto y acá hay que hacerlo manual..."*

**Riesgos para Tema 03:**
- subvalora los ejercicios HOF (los considera "simples") → puede no internalizarlos
- oversimplifica mónadas: "es como una Promise"

---

#### Experiencia estudiando solo (guía-estudio.md)

**Modalidad:** Lee primero §1 (Objetivos) y §9 (Puntos clave). Luego va a las secciones que no dominó en clase.

**Fortalezas al estudiar:**
- Secciones §3–§5 (fundamentos, HOF, composición): las recorre rápido, confirma comprensión
- §5.2 Generadores: hace correr el código en local

**Zona de esfuerzo:**
- §7 Mónadas: la guía tiene `Maybe` y `Either` bien explicados. Le lleva 20-30 min pero lo entiende.

**Score guía:** 88/100 — la guía le resulta muy útil para consolidar mónadas.

---

#### Simulación de TP (tp-quiz.gift)

**Estrategia:** Lee las 15 preguntas, responde primero las que conoce (P1-P8), vuelve a las que lo hicieron dudar.

**Predicción de respuestas:**
- P1 (funciones puras): ✅ responde B — 98% certeza  
- P5 (map resultado): ✅ — 95%  
- P11 (clausura — cuántos contextos): ⚠️ puede confundirse entre "3" y "2" — 70%  
- P14 (Promise como mónada): ✅ — 90% (la guía lo refuerza)  
- P15 (pipe de 3 funciones, resultado): ✅ — 85%  

**Score estimado en TP:** 13-14/15 (85-93%)

---

### 🟡 PERFIL ANSIOSO — Score: 68/100

**Base de calibración:** Olipas (2022) — ansiedad ante notación nueva; Mayer (2009) — carga cognitiva alta; Tema 02: bloque BNF fue zona crítica.

#### Experiencia en clase

| Bloque | Predicción conductual | Score simulado |
|--------|----------------------|---------------|
| B1 | El mini-caso de `promedioPositivos` lo relaja — código concreto y familiar. | 78/100 |
| B2 | **Zona de tensión inicial**: "¿Esta función modifica algo? ¿El `let` afuera es un efecto secundario?" — confusión entre variable léxica y efecto secundario. | 55/100 |
| B3 | HOF: se estabiliza con `map` y `filter` (los conoce de Tema 01). `reduce` le genera ansiedad — el ejemplo de `frecuencias` le parece complejo. | 62/100 |
| B4 | **Zona crítica**: currificación. "¿`addCurried(5)` devuelve una función o un número?" — confusión con la doble flecha `=>`. | 45/100 |
| B5 | Se recupera parcialmente. Los generadores se ven "raros" pero el docente dice que es ilustrativo. | 58/100 |
| B6 | **Zona de alivio sorprendente**: "¡Ah, `Promise.then()` es `flatMap`! eso ya lo uso!" — la analogía lo tranquiliza. `Maybe`/`Either` le genera nuevamente ansiedad. | 55/100 |

**Comportamiento típico en clase:**
> *"Profe, ¿la clausura `crearContador` es una función pura o impura? Porque captura `cuenta` pero la función la modifica..."*  
> *(Después de currificación)* → *"No entendí el `(a: number) => (b: number)` — ¿son dos funciones o una?"*

**Momento de mayor riesgo:**
Bloque 4 — si el docente pasa rápido por `compose(pipe(f, g), h)` sin explicar la notación paso a paso, el ansioso puede desconectarse emocionalmente el resto de la clase.

**Intervención recomendada en B4:**
> Detenerse en la notación `(g: (a: A) => B, f: (b: B) => C)` y preguntar al aula: *"¿Quién puede leer este tipo en voz alta?"* — reduce la carga extrínseca.

---

#### Experiencia estudiando solo (guía-estudio.md)

**Modalidad:** Lee linealmente desde §1. Vuelve dos veces a secciones que no entiende. Hace todos los ejercicios de autoevaluación.

**Fortalezas:**
- La §5.2 Currificación es más lenta que la minuta → le da el tiempo que necesitó en clase
- §8 Ejemplos trabajados paso a paso: los hace todos, lo tranquiliza

**Score guía:** 71/100 — sube notablemente respecto a clase. **La guía compensa la ansiedad en clase.**

**Observación crítica para el docente:**
> La guía es esencial para este perfil. Sin ella, el score de Tema 03 quedaría en ~55/100.

---

#### Simulación de TP (tp-quiz.gift)

**Estrategia:** Lee cada pregunta dos veces. Lleva más de 30 minutos (tiende a agotarse).

**Predicción de respuestas:**
- P3 (recursión → sin variables mutables): ✅ — 80% (lo entendió en guía)
- P7 (clausura — qué captura): ⚠️ — 55% — puede confundir con ámbito dinámico  
- P8 (currificación): ⚠️ — 45% — zona de mayor incertidumbre  
- P12 (mónadas): ✅ — 72% (Promise lo ancló)

**Score estimado en TP:** 9-11/15 (60-73%)

---

### 🔴 PERFIL DISPERSO — Score: 55/100

**Base de calibración:** Hoq et al. (2025) — misconceptions persitentes; atención intermitente; Tema 02: zona crítica fue BNF (score 0.30).

#### Experiencia en clase

| Bloque | Predicción conductual | Score simulado |
|--------|----------------------|---------------|
| B1 | El ejemplo visual de los dos estilos de código lo engancha (5/10 primeros minutos). Luego la historia del λ-cálculo lo desconecta. | 60/100 |
| B2 | Entiende "función pura = siempre mismo resultado" pero no internaliza el concepto de efecto secundario. `dobleExterno` le parece "igual" que `doble`. | 40/100 |
| B3 | Se reactiva con `map` y `filter` — los conoce de práctica. Pierde el hilo en la implementación manual de `reduce` con recursión. | 52/100 |
| B4 | **Zona de pérdida máxima**: `compose(pipe(...))` anidado. La notación abstracta lo desconecta completamente. | 28/100 |
| B5 | **Punto de reactivación**: generadores. "Ah, esto es como el `yield` que usé una vez en Python." | 55/100 |
| B6 | Se reactiva con Promise: "Eso lo uso todos los días." `Maybe`/`Either`: desconectado. "¿Para qué si ya tengo try/catch?" | 42/100 |

**Comportamiento típico en clase:**
> *(Durante B4, callado — no pregunta)*  
> *(Bloque 5)* → *"Profe, ¿la evaluación perezosa es lo mismo que async/await?"*  
> *(Bloque 6, sobre Maybe)* → *"¿Esto entra en el parcial?"*

**Señal de detección en B2 (recomendada):**
> *"¿Quién puede decirme por qué `dobleExterno` no es pura?"* — Si el disperso no puede responder, es señal de que perdió el hilo desde B2.

**Prerequisito gap detectado (viene del Tema 02):**
El disperso del Tema 02 tenía gap en "flujo compilador". En Tema 03 el gap relevante es: **no tiene claro qué es un "efecto secundario"** (lo confunde con "error"). La minuta lo trata explícitamente pero puede no retenerlo.

---

#### Experiencia estudiando solo (guía-estudio.md)

**Modalidad:** Solo estudia si hay evaluación próxima. Busca la sección de "Puntos clave" y "Autoevaluación" directamente.

**Lo que usa:** §9 Puntos clave, §10 Autoevaluación, §8 Ejemplos (los corre en local si tiene tiempo)

**Lo que no usa:** §3.1 (teoría de cómputo sin estado), §7 (mónadas), §12 (referencias)

**Score guía:** 55/100 — usa la guía como "chuleta", no como herramienta de comprensión profunda.

---

#### Simulación de TP (tp-quiz.gift)

**Estrategia:** Usa eliminación — descarta las respuestas que "suenan mal". Copia los ejemplos de código de la guía para responder preguntas de código.

**Predicción de respuestas:**
- P1 (funciones puras): ⚠️ — 60% — puede confundir con "función con un solo argumento" (opción D)  
- P5 (map resultado): ✅ — 80% — el ejemplo es concreto  
- P8 (currificación): ❌ — 35% — no comprendió el concepto  
- P10 (composición): ❌ — 40%  
- P14 (Promise como mónada): ✅ — 75% — es concreto y familiar  

**Score estimado en TP:** 7-9/15 (47-60%)

---

### ⚫ PERFIL RECURSERO — Score: 61/100

**Base de calibración:** Mahatanankoon & Wolf (2021) — estrategia shallow; Tema 02: zona de comodidad fue LLMs (score 0.80).

#### Experiencia en clase

| Bloque | Predicción conductual | Score simulado |
|--------|----------------------|---------------|
| B1 | Presente físicamente. Copia el ejemplo `promedioPositivos` en su cuaderno (o lo tuitea). | 65/100 |
| B2 | Anota "función pura = mismo resultado + no modifica". No entiende las implicaciones, pero tiene la frase para el examen. | 60/100 |
| B3 | Copia las implementaciones de `map`, `filter`, `reduce`. "¿De dónde saco `myMap` si lo necesito?" → "De npm." | 55/100 |
| B4 | Copia el ejemplo de `pipe`. Pregunta: "¿En la guía hay más ejemplos de compose?" | 50/100 |
| B5 | Generadores: los copia pero no entiende `yield`. "Esto parece raro." | 48/100 |
| B6 | Muy atento a Promise. "`.then()` es `flatMap`? ¿Eso cómo me ayuda en el TP?" | 55/100 |

**Comportamiento típico en clase:**
> *(B3)* → *"¿Hay una librería que ya tenga `pipe` y `compose` hecho?"* (referencia implícita a `ramda`, `fp-ts`)  
> *(B6)* → *"¿`Maybe` y `Either` son de TypeScript o hay que instalar algo?"*  
> *(Al final)* → *"¿Dónde dice en la guía cuáles son las preguntas que más salen?"*

**Patrón de riesgo en TP:**
El TP es un quiz Moodle con 15 preguntas de múltiple opción. El recursero **puede pasar el TP con 70%+ usando eliminación y guía**, sin haber comprendido la diferencia entre función pura e impura. Esto se detectará recién en las instancias de evaluación de composición o en Tema 05 (mónadas profundas).

**Trampa detectora recomendada:**
> Incluir en evaluaciones futuras (parcial): *"Explicá con tus palabras por qué `Date.now()` no es una función pura."* — El recursero no puede responder sin comprensión conceptual.

---

#### Experiencia estudiando solo (guía-estudio.md)

**Modalidad:** Busca §8 (Ejemplos trabajados) y §10 (Autoevaluación). Corre los ejemplos en TS Playground para copiar las respuestas del quiz.

**Qué logra:** entiende cómo funciona `map` en la práctica. No entiende por qué la pureza importa.

**Score guía:** 60/100 — usa la guía tácticamente para el TP.

---

#### Simulación de TP (tp-quiz.gift)

**Estrategia:** Abre la guía en paralelo. Busca las preguntas que tienen código con `map`/`filter` y las identifica por tipo de output.

**Predicción de respuestas:**
- P1 (funciones puras): ✅ — 80% (tiene la frase memorizada)
- P2 (inmutabilidad): ✅ — 85% (el ejemplo `push` vs `spread` es visual)
- P5 (map): ✅ — 90% (lo corrió en playground)
- P8 (currificación): ⚠️ — 55% — puede confundir con aplicación parcial
- P13 (flatMap/bind): ⚠️ — 50% — terminología no consolidada
- P15 (pipe de 3 funciones): ✅ — 70% — copia el patrón

**Score estimado en TP:** 10-11/15 (67-73%)

---

## Scores por Bloque (Cohort)

| Bloque | Duración | Estratégico | Ansioso | Disperso | Recursero | Promedio |
|--------|----------|-------------|---------|----------|-----------|----------|
| B1 Motivación | 10 min | 90 | 78 | 60 | 65 | **73** |
| B2 Fundamentos | 20 min | 85 | 55 | 40 | 60 | **60** |
| B3 HOF & clausuras | 30 min | 88 | 62 | 52 | 55 | **64** |
| B4 Composición | 20 min | 80 | 45 | 28 | 50 | **51** |
| B5 Efectos/lazy | 10 min | 82 | 58 | 55 | 48 | **61** |
| B6 Mónadas | 20 min | 75 | 55 | 42 | 55 | **57** |
| B7 Cierre | 10 min | 90 | 72 | 65 | 68 | **74** |

### 🔴 Bloques de mayor riesgo cohort:
1. **B4 Composición & Currificación** → promedio **51/100** — Zona crítica global
2. **B6 Mónadas** → promedio **57/100** — Alta varianza entre perfiles
3. **B2 Fundamentos (efectos secundarios)** → promedio **60/100** — Particularmente crítico para Disperso

---

## Comparación con Tema 02

| Métrica | Tema 02 | Tema 03 | Δ |
|---------|---------|---------|---|
| Score promedio cohort | 68/100 | 67/100 | -1 (comparable) |
| Bloque más crítico | BNF/Gramáticas (51) | Composición/Curry (51) | Igual dificultad percibida |
| Perfil más en riesgo | Disperso (T02: 52) | Disperso (T03: 55) | Leve mejora (+3) |
| Perfil más beneficiado | Estratégico (T02: 82) | Estratégico (T03: 85) | Mejora (+3) |

---

## Recomendaciones para el Docente

### 🎯 Intervenciones de alto impacto (implementar antes de la clase)

**1. Bloque 4 — Currificación: agregar scaffolding visual**

La notación `(a: number) => (b: number): number` es el punto de mayor abandono del ansioso y el disperso. Antes de presentar la versión genérica, mostrar un paso intermedio:

```typescript
// Paso 1: función normal
const add = (a: number, b: number) => a + b;

// Paso 2: separar argumentos manualmente
const addStep = (a: number) => {
  return function(b: number) {
    return a + b;
  };
};

// Paso 3: versión arrow equivalente
const addCurried = (a: number) => (b: number) => a + b;
```

**Impacto estimado:** +8 puntos en ansioso, +12 puntos en disperso en B4.

---

**2. Bloque 2 — Pregunta de detección temprana (min 15)**

Lanzar al aula:
> *"¿Quién puede decirme por qué `const dobleExterno = (n) => n * factor` **no** es pura, si cada vez que la llamo con el mismo `n` me da el mismo resultado?"*

Respuesta correcta: depende de `factor`, que puede cambiar entre llamadas.

Si la mayoría no responde → pausar y repetir con ejemplo concreto (`factor = 2` → cambian `factor = 3`).

**Perfil más beneficiado:** Disperso — necesita la "sorpresa" para anclar el concepto.

---

**3. Bloque 6 — Estructura de 3 tiempos**

Para mónadas, usar estructura explícita:
1. *"El problema que resuelven"* (2 min — null pointer ya conocido)
2. *"Promise como mónada"* (8 min — ancla en conocimiento previo)
3. *"Maybe/Either como extensión"* (10 min — generalización)

No empezar con `type Option<A> = ...` directamente — genera ansiedad en el ansioso y desconexión en el disperso.

---

### ℹ️ Observaciones sin acción inmediata

- **Recursero:** El quiz Moodle puede aprobarse sin comprender el "por qué" de la pureza. Considerar incluir en el parcial una pregunta abierta sobre efectos secundarios.
- **Estratégico:** Zona de oversimplificación en mónadas ("mónada = Promise"). Retomar en Tema 05 con pregunta correctora.
- **Ansioso con guía:** La guía-estudio.md es especialmente valiosa para este perfil. Comunicar explícitamente en clase: *"Esta guía fue diseñada para repasar en casa lo que vemos hoy."*
