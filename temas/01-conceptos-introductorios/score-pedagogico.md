# Score Pedagógico — Tema 01: Conceptos Introductorios + Intro a TypeScript

> **Agente:** 🎓 Simulador de Alumno (student-simulator) + 🧪 test-runner
> **Fecha:** 2026-03-10
> **Modo:** Batch — 4 perfiles simultáneos
> **Inputs simulados:**
> - Experiencia en clase: `minuta.md` + `filminas.md` (120 min)
> - Autoestudio: `guia-estudio.md`
> **Materia:** Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI

---

## Metodología

Cada perfil simula un alumno real con características cognitivas y comportamentales empíricas documentadas en la literatura de educación superior (ERIC, ACM DL). Se evalúan 5 Objetivos de Aprendizaje (OA) en dos dimensiones:

- **Sub-score CLASE** (0–100): absorción estimada a partir de la experiencia en clase (minuta + filminas)
- **Sub-score GUÍA** (0–100): absorción estimada a partir del autoestudio de `guia-estudio.md`
- **Score OA** = promedio ponderado 50% clase + 50% guía
- **Score GLOBAL** = promedio de los 5 OA

**Predicción TP (0–10):** estimación de respuestas correctas en el quiz Moodle, considerando las 10 preguntas y sus trampas internas.

---

## Resultados por Perfil

---

### 🟢 Perfil 1 — ESTRATÉGICO

> *Alumno orientado a resultados. Trabaja desde el objetivo de evaluación hacia atrás. Eficiente en extraer información tabular y estructurada. Peligro: comprensión superficial de conceptos con alta densidad abstracta.*

#### Comportamiento en clase

- **Bloque 1:** Fotografía F-04 (tabla Sebesta) en los primeros 2 minutos. Crea un mnemónico mental: LECCPE (Legibilidad, Escribibilidad, Confiabilidad, Costo, Portabilidad, Eficiencia). Participa en la tensión IA/lenguajes porque ve valor para futuros prompts.
- **Bloque 2:** Copia la tabla de F-09 (4 paradigmas). Marca la columna "Base formal" como probable pregunta de examen. Procesa el cuello de botella Von Neumann como concepto de segundo orden — lo registra pero no lo internaliza.
- **Bloque 3:** Identifica que LC-3 está "para contexto", descarta profundizar. Subraya mentalmente que `acc` es el marcador de imperatividad en el C. Conecta con la clase.
- **Bloque 4:** Corre el código en Deno Playground. Entiende el pipeline desde F-16. Anota la comparación TS/Java/Python como probable pregunta.
- **Bloque 5:** Anota citas exactas de Schmidt & Runfola (20/50/30). Registra que P05 del TP probablemente apunte a la demo en vivo.

#### Comportamiento con la guía de estudio

- Va directo a la **Autoevaluación**. Resuelve las 8 preguntas como checklist.
- Lee el **Glosario** completo — lo usa como verificación de sus notas de clase.
- Vuelve a leer las secciones de teoría *solo donde falló* en la autoevaluación.
- No lee los recuadros `<details>` antes de intentar responder: usa la guía pedagógicamente bien.

#### Scores por OA

| OA | Descripción | Score CLASE | Score GUÍA | Score OA |
|----|-------------|------------|-----------|---------|
| OA1 | Justificar relevancia de paradigmas en era IA | 80 | 88 | **84** |
| OA2 | Identificar 4 paradigmas y lenguajes | 90 | 95 | **92** |
| OA3 | Distinguir imperativo vs funcional (mutación de estado) | 75 | 85 | **80** |
| OA4 | Escribir función básica con tipos en TypeScript | 85 | 82 | **83** |
| OA5 | Aplicar loop trust-but-verify | 80 | 82 | **81** |

**Score global: 84/100** 🟢

#### Predicción TP: **8–9/10**

| Pregunta | Predicción | Justificación |
|----------|-----------|---------------|
| P01 (Confiabilidad TS) | ✅ Correcta | Aprendió el vínculo Sebesta ↔ demo de errores |
| P02 (Trampa JVM) | ✅ Correcta | Alto nivel de alerta ante trampas; conoce el pipeline |
| P03 (Variable `acc`) | ✅ Correcta | Identificó `acc` explícitamente como marcador imperativo |
| P04 (Von Neumann → variable) | ✅ Correcta | Registró la tabla F-12 |
| P05 (Demo IA en clase) | ⚠️ Riesgo | Estaba tomando notas durante la demo — puede no recordar el detalle exacto de `let sum` |
| P06 (Bus CPU-memoria) | ✅ Correcta | Leyó y verificó en la guía |
| P07 (LISP 1960) | ✅ Correcta | Tiene la tabla histórica memorizada |
| P08 (Escalera, ¿qué se pierde?) | ✅ Correcta | Razona el trade-off sin dificultad |
| P09 (TS multiparadigma) | ✅ Correcta | Concepto claro desde F-20 y guía sección 4.5 |
| P10+ | — | — |

**Riesgo principal:** P05 (referencia específica a momento de clase). Recomendar que en la demo del docente se haga participar al alumno activamente para que no esté tomando notas.

---

### 🟡 Perfil 2 — ANSIOSO

> *Alumno de alta dedicación pero bajo umbral de sobrecarga cognitiva. Trabaja mucho más que el promedio, pero la ansiedad produce errores de segundo y tercer repaso. Copia todo en clase. Estudia la guía exhaustivamente. Peligro: confunde cantidad de estudio con calidad de comprensión.*

#### Comportamiento en clase

- **Bloque 1:** Copia toda la tabla Sebesta palabra por palabra desde F-04. Pierde comentarios del docente mientras escribe. Llega al Bloque 2 con media página de notas y cierta tensión.
- **Bloque 2:** El Von Neumann → imperativo le resulta abstracto. Escribe "variables = celdas de memoria (?)" con signo de pregunta. El cuello de botella de Von Neumann genera confusión: ¿es algo que hay que saber o solo contexto? Pierde el hilo durante la tabla F-09 porque sigue copiando F-07.
- **Bloque 3:** El código LC-3 genera un micro-pánico. Intenta copiarlo completo. El docente dice "no tienen que entenderlo" pero la ansiedad lo registra como "potencialmente entra". Se pierde la conexión C → TypeScript que se plantea al final del bloque.
- **Bloque 4:** La demo de TypeScript lo reconecta. Le resulta familiar. Ejecuta el código, lo entiende. La detección del error de tipos lo calma ("esto es confiabilidad, lo entiendo").
- **Bloque 5:** Copia los porcentajes exactos de Schmidt & Runfola. Anota "Fig. 8", "Fig. 12", "Fig. 14" como si pudieran ser datos exactos del TP.

#### Comportamiento con la guía de estudio

- Lee toda la guía de principio a fin, incluidos los recuadros de referencias bibliográficas.
- Lee el Glosario 3 veces completo.
- Realiza la Autoevaluación con alta ansiedad: verifica las respuestas inmediatamente después de cada pregunta, sin darle tiempo al procesamiento.
- Genera dudas por exceso de detalle: "¿'observable' en Q3 significa que el estado existe pero no se ve?"
- Estudia los años exactos (Church 1936, Robinson 1965) como si fueran datos de examen.

#### Scores por OA

| OA | Descripción | Score CLASE | Score GUÍA | Score OA |
|----|-------------|------------|-----------|---------|
| OA1 | Justificar relevancia de paradigmas en era IA | 65 | 78 | **71** |
| OA2 | Identificar 4 paradigmas y lenguajes | 68 | 82 | **75** |
| OA3 | Distinguir imperativo vs funcional (mutación de estado) | 50 | 68 | **59** |
| OA4 | Escribir función básica con tipos en TypeScript | 60 | 65 | **62** |
| OA5 | Aplicar loop trust-but-verify | 52 | 62 | **57** |

**Score global: 65/100** 🟡

#### Predicción TP: **6/10**

| Pregunta | Predicción | Justificación |
|----------|-----------|---------------|
| P01 (Confiabilidad TS) | ✅ Correcta | Conectó con la demo de errores (fue el momento de calma) |
| P02 (Trampa JVM) | ⚠️ Riesgo | Puede caer en la opción "parcialmente correcta" por ansiedad; sabe que algo intermedio existe |
| P03 (Variable `acc`) | ✅ Correcta | Copió el código de C en clase |
| P04 (Von Neumann → variable) | ⚠️ Riesgo | Copió la tabla F-12 pero con duda — puede equivocarse por segunda lectura ansiosa del enunciado |
| P05 (Demo IA en clase) | ⚠️ Riesgo | Tomaba notas durante la demo; no recuerda el nombre exacto de la variable `sum` |
| P06 (Bus CPU-memoria) | ✅ Correcta | Estudió la guía exhaustivamente; conoce la respuesta desde autoevaluación Q6 |
| P07 (LISP 1960) | ✅ Correcta | Tabla histórica memorizada |
| P08 (Escalera, ¿qué se pierde?) | ⚠️ Riesgo | Puede confundir "control/eficiencia" con "legibilidad" en el sentido de la pregunta |
| P09 (TS multiparadigma) | ✅ Correcta | Lo entiende bien |
| — | — | — |

**Riesgo principal:** Patrón de segunda-lectura ansiosa — en preguntas con opciones similares, el alumno elige la "más completa" aunque no sea la mejor. Particularmente P02 y P04.

---

### 🟡 Perfil 3 — DISPERSO

> *Alumno de inteligencia normal que no sostiene la atención en secuencias largas de conceptos abstractos. Se reconecta ante contenido práctico, provocador o visual. Aprende bien en clase cuando el docente hace preguntas abiertas, pero pierde el hilo en bloques expositivos extensos.*

#### Comportamiento en clase

- **Bloque 1:** Muy enganchado por "¿cuántos lenguajes existen? → 700+". Participa. Pierde el hilo en los 6 criterios de Sebesta (demasiados en secuencia). Recuerda "legibilidad" y "confiabilidad" como los más salientes.
- **Bloque 2:** Reconecta en el diagrama Von Neumann de F-08 (es visual). Se engancha con "¿se puede computar sin Von Neumann?" y la respuesta "cálculo lambda". Pierde la tabla F-09 de los 4 paradigmas (mucho texto en simultáneo). Sale del bloque sin internalizar bien las bases formales.
- **Bloque 3:** El LC-3 le resulta curioso como artefacto histórico, no lo procesa pedagógicamente. El código C lo ve pero no extrae la clave (`acc` = estado mutable). Se desconecta antes del cierre del bloque.
- **Bloque 4:** Re-enganche total. Escribe código en el Playground. Hace preguntas. Entiende la diferencia imperativo/funcional *haciendo*, no escuchando.
- **Bloque 5:** Máximo enganche — la demo de IA es su contexto nativo. Participa, hace comentarios. Sale de clase con buena impresión global pero sin consolidar los conceptos abstractos.

#### Comportamiento con la guía de estudio

- Abre la guía y va a la **sección de TypeScript** (Bloque 4) primero. Lee el código con interés.
- Salta la tabla histórica y las secciones 2.2 y 2.3 (Von Neumann, cuello de botella).
- Hace la autoevaluación de forma impulsiva sin leer la teoría previa — responde por intuición.
- No lee el Glosario como tal, pero inevitablemente lee algunas definiciones al buscar aclaraciones.
- Se pierde la conexión "Von Neumann → imperativo" que está mejor explicada en la sección 3.2 de la guía que en clase.

#### Scores por OA

| OA | Descripción | Score CLASE | Score GUÍA | Score OA |
|----|-------------|------------|-----------|---------|
| OA1 | Justificar relevancia de paradigmas en era IA | 82 | 72 | **77** |
| OA2 | Identificar 4 paradigmas y lenguajes | 52 | 58 | **55** |
| OA3 | Distinguir imperativo vs funcional (mutación de estado) | 62 | 57 | **59** |
| OA4 | Escribir función básica con tipos en TypeScript | 78 | 65 | **71** |
| OA5 | Aplicar loop trust-but-verify | 82 | 62 | **72** |

**Score global: 67/100** 🟡

#### Predicción TP: **5–6/10**

| Pregunta | Predicción | Justificación |
|----------|-----------|---------------|
| P01 (Confiabilidad TS) | ✅ Correcta | Recuerda el error en vivo — experiencia sensorial |
| P02 (Trampa JVM) | ✅ Correcta | Tiene buen radar para "esto suena raro" |
| P03 (Variable `acc`) | ⚠️ Riesgo | Puede responder `i` (también mutable, el índice del for) sin ver la diferencia semántica con `acc` |
| P04 (Von Neumann → variable) | ❌ Probable fallo | No consolidó este concepto ni en clase ni en la guía (la saltó) |
| P05 (Demo IA en clase) | ✅ Correcta | Estaba atento en el Bloque 5 — recuerda el `let sum` |
| P06 (Bus CPU-memoria) | ❌ Probable fallo | El distractor "GPU/VRAM" es muy efectivo para este perfil |
| P07 (LISP 1960) | ⚠️ Riesgo | Puede recordar "funciones" pero confundir con OO |
| P08 (Escalera, ¿qué se pierde?) | ⚠️ Riesgo | Intuye la respuesta pero puede elegir respuesta negativa incorrecta |
| P09 (TS multiparadigma) | ✅ Correcta | Practicó los tres estilos en clase |
| — | — | — |

**Riesgo principal:** Preguntas que requieren conexión abstracta (P04, P06) son su punto débil. E P03, donde hay dos variables mutables (`acc` e `i`) y hay que distinguir semánticamente.

---

### 🔴 Perfil 4 — RECURSERO

> *Alumno que gestiona su energía descargando y memorizando recursos: filminas, fotos de la pizarra, listas. Tiene buena capacidad de recall de listas y tablas pero no construye comprensión de las conexiones entre conceptos. Cumple con el TP pero con base frágil.*

#### Comportamiento en clase

- Descarga el PDF de filminas durante el Bloque 1. A partir de ahí presta atención intermitente: confirma que "lo tiene en el PDF".
- **Bloque 1:** Fotografía F-04 (tabla Sebesta). No escucha el ejemplo de tensión (Python vs C).
- **Bloque 2:** Screenshot de F-09 y F-10. No procesa la base formal del paradigma funcional (cálculo lambda) — solo anota "Haskell, Clojure, LISP".
- **Bloque 3:** Anota "`acc` = acumulador = imperativo". No sigue el razonamiento Von Neumann → asignación → estado.
- **Bloque 4:** Copia el diagrama del pipeline de F-16. No ejecuta el código en el Playground (sigue bajando recursos).
- **Bloque 5:** Copia los 3 porcentajes de F-21 (20/50/30) y el diagrama de proficiencia de F-22. No sigue la demo en vivo.

#### Comportamiento con la guía de estudio

- Escanea los encabezados (H2, H3) de toda la guía.
- Copia el Glosario completo en un documento propio — lo convertirá en flashcards.
- Va a la Autoevaluación y abre los `<details>` *antes* de responder para copiar las respuestas. No intenta resolver por propia cuenta.
- Guarda la sección 2.5 (tabla de 4 paradigmas) y la sección 1.4 (tabla Sebesta) como referencias.
- No lee los ejemplos de código comparativo ni la sección 3.3 (escalera de abstracciones).

#### Scores por OA

| OA | Descripción | Score CLASE | Score GUÍA | Score OA |
|----|-------------|------------|-----------|---------|
| OA1 | Justificar relevancia de paradigmas en era IA | 42 | 35 | **38** |
| OA2 | Identificar 4 paradigmas y lenguajes | 68 | 65 | **66** |
| OA3 | Distinguir imperativo vs funcional (mutación de estado) | 32 | 38 | **35** |
| OA4 | Escribir función básica con tipos en TypeScript | 42 | 30 | **36** |
| OA5 | Aplicar loop trust-but-verify | 30 | 28 | **29** |

**Score global: 41/100** 🔴

#### Predicción TP: **4–5/10**

| Pregunta | Predicción | Justificación |
|----------|-----------|---------------|
| P01 (Confiabilidad TS) | ✅ Correcta | Tiene F-04 en el PDF — recall directo |
| P02 (Trampa JVM) | ❌ Probable fallo | El lenguaje "parcialmente correcta" o "JVM de Google Chrome = V8" puede confundirlo; no procesó el pipeline en profundidad |
| P03 (Variable `acc`) | ✅ Correcta | Anotó "`acc` = acumulador = imperativo" — recall directo |
| P04 (Von Neumann → variable) | ✅ Correcta | Está en la tabla F-12 que tiene en el PDF |
| P05 (Demo IA en clase) | ❌ Probable fallo | No estaba atento a la demo en vivo — no recuerda `let sum` |
| P06 (Bus CPU-memoria) | ❌ Probable fallo | El distractor "GPU/VRAM" es muy efectivo para quien no procesó el concepto abstracto |
| P07 (LISP 1960) | ✅ Correcta | Tiene la tabla histórica F-03 en el PDF |
| P08 (Escalera, ¿qué se pierde?) | ⚠️ Riesgo | Puede confundir la dirección del trade-off |
| P09 (TS multiparadigma) | ⚠️ Riesgo | Copió F-20 pero puede confundir "no obliga" con "elige funcional por defecto" |
| — | — | — |

**Riesgo principal:** P02, P05 y P06 combinadas representan 3 fallos casi seguros. La falta de procesamiento activo de conceptos hace que las trampas bien diseñadas lo afecten sistemáticamente.

---

## Resumen ejecutivo

| Perfil | Score Global | Predicción TP | Semáforo |
|--------|-------------|--------------|---------|
| Estratégico | **84/100** | 8–9/10 | 🟢 |
| Ansioso | **65/100** | 6/10 | 🟡 |
| Disperso | **67/100** | 5–6/10 | 🟡 |
| Recursero | **41/100** | 4–5/10 | 🔴 |
| **Promedio simulado** | **64/100** | **~6/10** | 🟡 |

---

## Sub-scores: Clase vs Guía de Estudio

| Perfil | Score CLASE | Score GUÍA | Δ (Guía mejora) |
|--------|------------|-----------|----------------|
| Estratégico | 82 | 86 | +4 |
| Ansioso | 59 | 71 | +12 |
| Disperso | 71 | 63 | −8 |
| Recursero | 43 | 39 | −4 |

**Observación clave:** La guía beneficia significativamente al Ansioso (que la estudia en profundidad) pero no compensa las debilidades del Disperso y el Recursero, quienes no la usan de forma efectiva.

---

## Objetivos con mayor riesgo de no alcanzar

| OA | Descripción | Score promedio | Riesgo |
|----|-------------|---------------|--------|
| OA3 | Distinguir imperativo vs funcional | **53/100** | 🔴 Alto |
| OA5 | Aplicar loop trust-but-verify | **60/100** | 🟡 Medio-alto |
| OA1 | Justificar relevancia de paradigmas | **68/100** | 🟡 Medio |
| OA4 | Escribir función TypeScript básica | **63/100** | 🟡 Medio |
| OA2 | Identificar 4 paradigmas | **72/100** | 🟢 Aceptable |

---

## Recomendaciones para el docente

### Ajustes en la clase (sin cambiar el diseño aprobado)

1. **Bloque 3 — Anunciar explícitamente el rol del LC-3:** Decir en voz alta: *"Este código NO hay que entenderlo — está acá para que lo vean y aprecien por qué existe C."* Reduce la ansiedad del perfil Ansioso sin cambiar el contenido.

2. **Bloque 4 — Hacer participar activamente al Recursero durante la demo:** En lugar de solo mostrar el Deno Playground, pedir a alguien del aula que tipee el código. Quien tipea (usualmente no el Recursero) sí consolida el aprendizaje; pero la instrucción activa reduce la tentación de "ya lo tengo en el PDF".

3. **Bloque 5 — Demo IA: preguntar qué variable es el marcador de imperatividad** (respuesta: `let sum`). Esto convierte el momento en un anchor memorable para P05 del TP, y beneficia especialmente al Estratégico que estaba tomando notas.

4. **Transición Bloque 2 → Bloque 3:** Agregar 60 segundos de consolidación: *"¿Alguien puede decir con sus palabras qué es una variable para Von Neumann?"* Beneficia al Disperso y al Ansioso sin costo de tiempo significativo.

### Ajustes en la guía de estudio

1. **Agregar un aviso al inicio de Bloque 3 en la guía:** Una nota al Disperso: *"Si saltaste las secciones 2.2 y 2.3, volvé a leerlas antes de esta sección — sin Von Neumann, los ejemplos de código pierden su sentido pedagógico."*

2. **Agregar una nota en Q7 de autoevaluación:** Aclarar que el Bloque 5 de la guía y la demo en vivo son complementarios — hay preguntas del TP que requieren el recuerdo de la demo.

### Para el diseño del TP (ya tiene tp.md, aplicar en la próxima versión)

- La trampa P02 (JVM) es muy efectiva para el Recursero. Mantenerla.
- La trampa P05 (referencia a demo en vivo) tiene el efecto pedagógico deseado: penaliza al alumno que no estuvo presente/atento. Mantenerla.
- Considerar agregar una pregunta sobre OA3 (mutación de estado) sin referencia de clase — el score promedio de este OA es el más bajo y el TP tiene solo P03 que lo toca tangencialmente.

---

*Simulación generada por student-simulator · testing pedagógico Tema 01 · UNTDF/IDEI 2026*
