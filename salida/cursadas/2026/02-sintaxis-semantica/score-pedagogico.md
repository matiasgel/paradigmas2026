# Score Pedagógico — Tema 02: Sintaxis y Semántica de Lenguajes
# Generado: 2026-03-11 | Agente: student-simulator + test-runner
# Modo: BATCH — 4 perfiles

---

## Resumen ejecutivo

| Perfil | En clase | Guía estudio | TP | **Score global** | Riesgo |
|--------|----------|--------------|-----|-----------------|--------|
| Estratégico | 84 | 88 | 82 | **85** | 🟢 Bajo |
| Ansioso | 59 | 68 | 55 | **61** | 🔴 Alto |
| Disperso | 46 | 52 | 42 | **47** | 🔴 Crítico |
| Recursero | 62 | 70 | 65 | **66** | 🟡 Medio |

**Umbral mínimo aprobación simulada:** 60/100
**Perfiles en riesgo de reprobación:** Ansioso (borderline), Disperso (crítico)

---

## Simulación por perfil

---

### 🎯 Perfil: ESTRATÉGICO — Score global: 85/100

#### En clase (84/100)

**Bloque 1 — Sintaxis y semántica (20 min)**
Llega con el contexto de Tema 01 fresco. La pregunta motivadora (*"¿cómo sabe el compilador que está mal?"*) activa su esquema previo inmediatamente. Clasifica los 3 casos TypeScript correctamente en la actividad de apertura. Anota la distinción error estático/dinámico como "dato útil para el parcial".
- Sub-score: 90/100

**Bloque 2 — Análisis léxico (25 min)**
La tabla de tokenización de `indice = 5 * contador + 1;` le resulta clara. Entiende la diferencia lexema/token. Puede que no tome nota del scanner como módulo separado — lo considera implícito.
- Sub-score: 82/100

**Bloque 3 — Gramáticas BNF/EBNF (35 min)**
Sigue bien la derivación hasta el paso 6-7. En el árbol de análisis, intenta atajar pasos intermedios. Puede omitir el nodo intermedio `<término>` en la derivación manual. Si el docente no frena, sale con una comprensión aproximada de EBNF.
- Sub-score: 72/100 ⚠️
- **Advertencia:** Riesgo de comprensión superficial de la diferencia BNF↔EBNF

**Bloque 4–5 — Semántica operacional (20 min)**
Comprende la idea de semántica como pipeline. Conecta con sistemas de tipos (anticipó Tema 03 internamente).
- Sub-score: 80/100

**Bloque 6 — LLMs y constrained decoding (15 min)**
Zona de máximo interés. Pregunta activamente sobre TypeScript y EBNF specs. Sale motivado.
- Sub-score: 92/100

#### Guía de estudio (88/100)
Lee la guía con los objetivos del §2 como checklist. Trabaja el ejemplo de derivación §4.3 verificando sus propios pasos de clase. Detecta que se saltó un paso en la derivación — lo corrige. Lee el glosario de forma rápida.
- Puntos débiles: puede saltear el §6 (EBNF extensiones) si no hay ejercicio asociado visible

#### TP (82/100)
- Ejercicio 1 (lectura BNF): 9/10 — detecta que `a = d;` no pertenece, explica bien
- Ejercicio 2 (derivación + árbol): 16/20 — árbol correcto, omite un nivel en derivación ⚠️
- Ejercicio 3 (ambigüedad): 14/15 — detecta ambigüedad, justificación algo breve
- Ejercicio 4 (escribir gramática): 13/15 — gramática válida, no cubre casos borde
- Ejercicio 5 (LLM experiment): 30/40 — ejecuta bien pero análisis de diferencia verbal/JSON superficial

---

### 😰 Perfil: ANSIOSO — Score global: 61/100

#### En clase (59/100)

**Bloque 1 — Sintaxis y semántica (20 min)**
La pregunta motivadora genera interés pero también ansiedad inmediata: *"¿cuántas cosas hay dentro del compilador que no sé?"*. Clasifica 2 de 3 casos correctamente. No levanta la mano aunque tiene dudas sobre el error dinámico.
- Sub-score: 72/100

**Bloque 2 — Análisis léxico (25 min)**
La tabla de tokens ayuda. Copia la tabla en su cuaderno textualmente. Confunde que un mismo string puede ser lexema de múltiples categorías. Pregunta al compañero de al lado en voz baja.
- Sub-score: 65/100

**Bloque 3 — Gramáticas BNF/EBNF (35 min) 🔴**
**ZONA DE SATURACIÓN COGNITIVA.** Al llegar a la derivación paso 4, ya perdió el hilo de qué es `<expr>` y qué es `<término>`. Intenta seguir copiando pero no entiende qué está derivando. El árbol sintáctico genera confusión adicional (¿nodo terminal vs no-terminal?).
- Sub-score: 40/100 🔴
- **Señal visible:** Para de tomar notas. Mira la pantalla sin copiar. Posible desconexión.
- **Intervención recomendada:** Pausa en el paso 5 de la derivación. Preguntar explícitamente: *"¿Me siguen hasta acá?"*

**Bloque 4–5 — Semántica operacional (20 min)**
Se recupera levemente con el pipeline (más intuitivo que BNF). Entiende que el compilador tiene etapas.
- Sub-score: 60/100

**Bloque 6 — LLMs (15 min)**
Se relaja. El ejemplo de ChatGPT con JSON schema le resulta concreto. Se reactiva.
- Sub-score: 70/100

#### Guía de estudio (68/100)
Lee con más calma que en clase. El §4.3 (derivación con tabla) le permite releer paso a paso. Logra seguir hasta el paso 8 de 10. El glosario lo usa activamente. El §5 (árbol sintáctico ASCII) le cuesta interpretarlo sin animación.
- Mejora estimada respecto a clase: +9 puntos
- Puntos débiles: árbol sintáctico ASCII difícil de leer sin guía

#### TP (55/100) ⚠️
- Ejercicio 1: 7/10 — detecta 3 de 4 casos, `d` fuera del lenguaje no lo ve
- Ejercicio 2 (derivación): 10/20 — deriva 6 pasos, comete error en paso 7, árbol incompleto 🔴
- Ejercicio 3 (ambigüedad): 7/15 — identifica que hay dos árboles pero no explica implicancia
- Ejercicio 4 (escribir gramática): 9/15 — gramática con producción recursiva a izquierda ⚠️
- Ejercicio 5 (LLM): 22/40 — ejecuta experimento pero no distingue bien los resultados

---

### 😶 Perfil: DISPERSO — Score global: 47/100 🔴

#### En clase (46/100)

**Bloque 1 — Sintaxis y semántica (20 min)**
La pregunta motivadora lo conecta momentáneamente. Clasifica 1 de 3 casos correctamente. Confunde error de compilación con error de runtime sistemáticamente. No tiene claro qué vio en Tema 01.
- Sub-score: 52/100
- **Gap detectado:** Prerequisito Tema 01 no consolidado — necesita retoma explícita

**Bloque 2 — Análisis léxico (25 min)**
La tabla de tokenización es visual y lo ayuda. Copia la tabla. Entiende que `indice` es un identificador. No retiene que el scanner es el que detecta los lexemas.
- Sub-score: 58/100

**Bloque 3 — Gramáticas BNF/EBNF (35 min) 🔴**
**DESCONEXIÓN TOTAL a partir del paso 3.** Abre el celular. No copia. Si el docente hace contact visual, asiente sin entender. No distingue regla de producción de instancia derivada.
- Sub-score: 22/100 🔴
- **Comportamiento observable:** Deja de participar. Puede hacer pregunta administrativa: *"¿está grabada la clase?"*

**Bloque 4–5 — Semántica operacional (20 min)**
Parcialmente presente. Entiende "hay etapas en el compilador" a nivel superficial.
- Sub-score: 38/100

**Bloque 6 — LLMs (15 min)**
Se reactiva fuertemente. El ejemplo práctico de ChatGPT lo engancha. Sale de la clase con la idea de constrained decoding pero sin el sustento teórico.
- Sub-score: 68/100

#### Guía de estudio (52/100)
Abre la guía antes del TP. Lee §2 objetivos (no procesa). Lee §4.2 (ejemplo tokenización — comprende). Intenta §4.3 derivación — abandona en paso 4. Va directo a §9 glosario para buscar respuestas del TP.
- Patrón: lectura fragmentaria orientada a resolver el TP puntualmente

#### TP (42/100) 🔴
- Ejercicio 1: 5/10 — solo 2 de 4 casos correctos, justificaciones vacías
- Ejercicio 2 (derivación): 6/20 — copia parcialmente el ejemplo de la guía, árbol incompleto 🔴
- Ejercicio 3 (ambigüedad): 5/15 — responde "hay dos formas" sin explicar
- Ejercicio 4 (escribir gramática): 6/15 — gramática incompleta, falta caso base
- Ejercicio 5 (LLM): 20/40 — ejecuta el experimento con ChatGPT pero no analiza diferencias

---

### 🎲 Perfil: RECURSERO — Score global: 66/100

#### En clase (62/100)

**Bloque 1 — Sintaxis y semántica (20 min)**
Clasifica los casos correctamente usando patrón reconocido ("el compilador lo detecta = sintaxis"). No entiende por qué, pero la regla funciona para la actividad.
- Sub-score: 68/100

**Bloque 2 — Análisis léxico (25 min)**
La tabla de tokens le parece útil como plantilla. La anota como "formato para el TP".
- Sub-score: 65/100

**Bloque 3 — Gramáticas BNF/EBNF (35 min)**
Sigue la derivación como procedimiento mecánico. Copia los pasos sin entender qué símbolo no-terminal está expandiendo. Ante el árbol sintáctico, lo copia como figura.
- Sub-score: 52/100
- **Patrón:** Copia forma, no entiende función

**Bloque 4–5 — Semántica operacional (20 min)**
Presta atención selectiva. Anota "pipeline: lexer → parser → semantic → code gen".
- Sub-score: 60/100

**Bloque 6 — LLMs (15 min)**
Alta atención. Ya usó constrained decoding (Outlines/Instructor) sin saber que tiene ese nombre. Se engancha.
- Sub-score: 82/100

#### Guía de estudio (70/100)
Lee §4.3 (ejemplo derivación) como plantilla para copiar en el TP. Lee §7 (LLMs) con interés real. El glosario lo usa para buscar definiciones textuales para copiar en respuestas abiertas.

#### TP (65/100)
- Ejercicio 1: 8/10 — aplica patrón "¿lo rechaza el compilador?" correctamente
- Ejercicio 2 (derivación): 15/20 — copia estructura del ejemplo guía, adapta con éxito parcial
- Ejercicio 3 (ambigüedad): 10/15 — identifica ambigüedad, explicación copiada de glosario
- Ejercicio 4 (escribir gramática): 10/15 — gramática basada en el ejemplo del TP Ej.1, no generaliza
- Ejercicio 5 (LLM): 22/40 — ejecuta bien, análisis superficial pero registra diferencias observadas

---

## Análisis transversal

### Bloques por dificultad simulada (promedio 4 perfiles)

| Bloque | Score promedio | Semáforo |
|--------|---------------|----------|
| Bloque 1 — Sintaxis/Semántica | 70.5 | 🟡 |
| Bloque 2 — Análisis léxico | 67.5 | 🟡 |
| Bloque 3 — BNF/EBNF | **46.5** | 🔴 |
| Bloque 4–5 — Semántica formal | 59.8 | 🟡 |
| Bloque 6 — LLMs | 78.0 | 🟢 |

### Ejercicios del TP por dificultad

| Ejercicio | Score promedio | Nota |
|-----------|---------------|------|
| Ej. 1 — Lectura BNF | 7.3/10 | ✅ |
| Ej. 2 — Derivación + árbol | **11.8/20** | ⚠️ Mayor dificultad |
| Ej. 3 — Ambigüedad | 9.0/15 | ⚠️ |
| Ej. 4 — Escribir gramática | 9.5/15 | ⚠️ |
| Ej. 5 — LLM experiment | **23.5/40** | 🟡 |

### Intervenciones recomendadas para el docente

1. **Bloque 3 es el cuello de botella universal.** Todos los perfiles bajan ahí.
   Sugerencia: agregar pausa explícita en el paso 4–5 de la derivación. Preguntar al grupo: *"¿Qué símbolo no-terminal acabo de expandir?"*

2. **El árbol sintáctico ASCII en la guía de estudio es difícil de leer** para ansioso y disperso.
   Sugerencia: complementar con una versión animada o con colores en filminas para el próximo año.

3. **El Ejercicio 2 del TP es el de mayor riesgo de error.** La derivación paso a paso requiere práctica guiada.
   Sugerencia: agregar un ejercicio de práctica intermedio en la guía de estudio antes del TP.

4. **El Bloque 6 (LLMs) funciona como gancho de reenganche.** Usar esta dinámica para reforzar BNF/EBNF:
   *"¿Por qué el LLM necesita una gramática EBNF para generar JSON válido? Volvamos al Bloque 3..."*
