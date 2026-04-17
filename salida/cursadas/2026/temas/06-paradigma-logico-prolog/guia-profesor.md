# Guía del Profesor — Tema 06: Paradigma Lógico: Prolog — Clase 1 de 3

**Materia:** Paradigmas y Lenguajes de Programación 2026  
**UNTDF / IDEI | Docente:** Matías Gel  
**Preparada por:** Lic. Marcos (topic-designer) + Dr. Roberto (class-writer) — 2026-04-17  
**Documento:** orientación pedagógica profunda (distinto de la minuta operativa)  

---

## ¿Cuál es la diferencia entre esta guía y la minuta?

| Minuta (`minuta.md`) | Guía del profesor (este documento) |
|---|---|
| Script operativo: qué decir, cuándo, qué abrir | Marco pedagógico: por qué enseñar así, qué esperar |
| Granularidad: minuto a minuto | Granularidad: conceptos y estrategias |
| Uso: durante la clase | Uso: preparación y reflexión post-clase |

---

## 1. Marco Pedagógico del Tema

### 1.1 ¿Por qué el paradigma lógico es difícil de enseñar?

El paradigma lógico genera una de las mayores rupturas cognitivas de toda la materia. Los alumnos llegan con dos paradigmas internalizados (imperativo y funcional) y un modelo mental fuertemente centrado en el *control del flujo*. Prolog rompe ese modelo en tres dimensiones simultáneas:

1. **No hay algoritmo explícito** — el motor infiere, el programador declara
2. **No hay asignación** — `=` unifica, no asigna; una variable instanciada no puede cambiar
3. **El resultado puede ser múltiple** — no hay un `return`, hay éxito/falla + instanciaciones

La estrategia pedagógica de esta clase responde a esto con **una única base de conocimiento concreta** (la familia) que crece incrementalmente. Cada concepto nuevo (hechos → reglas → consultas → recursión) se construye sobre la misma base, lo que reduce la carga cognitiva y permite que el alumno se concentre en el concepto nuevo, no en un ejemplo nuevo.

### 1.2 Posicionamiento en la currícula

Esta es la primera clase del **tercer bloque paradigmático** de la materia:
```
Bloque 1: Imperativo (Python)         → Clases 01–03
Bloque 2: Funcional (TypeScript)      → Clases 04–06 (inmutabilidad, HOF, etc.)
Bloque 3: Lógico (Prolog)             → Clases 07–09 (esta es la 07 = T06 C1)
Bloque 4: OOP (Java/Kotlin)           → Clases 10–14
```

El alumno viene de trabajar con funciones puras, inmutabilidad y tipos — una preparación razonablemente buena para el paradigma lógico, porque Prolog también es sin estado. La diferencia que hay que resaltar: en funcional, el programador *controla la transformación*; en lógico, el programador *no controla nada* — describe y confía en el motor.

### 1.3 Objetivos de aprendizaje (Bloom revisado)

| Nivel Bloom | Evidencia de aprendizaje |
|---|---|
| Recordar | Nombra: hecho, regla, consulta, variable, átomo |
| Comprender | Explica con sus palabras qué hace el motor de Prolog al recibir `?- abuelo(ana, Z).` |
| Aplicar | Escribe correctamente `hermano/2`, `tio/2` desde cero |
| Analizar | Traza a mano una consulta de 3 pasos con backtracking |
| Evaluar | Justifica por qué Prolog es mejor o peor que Python para un problema dado |
| Crear | (Clase 3) — diseña una base de conocimiento original |

**En esta clase llegamos hasta "Aplicar/Analizar".**

---

## 2. Conceptos que los Alumnos Encuentran Más Difíciles

### 2.1 🔴 Dificultad Alta: `=` no es asignación

**Por qué cuesta:** los alumnos tienen años de `x = 5` como "guardar un valor en x". En Prolog:

```prolog
X = 5.         % instancia X a 5 — unificación exitosa
X = 6.         % falla si X ya vale 5 — no puede "reasignar"
```

**Señal de que hay confusión:** el alumno pregunta "¿cómo cambio el valor de X?" o intenta usar `X = X + 1`.

**Estrategia de corrección:**
- Decir explícitamente: "En Prolog una variable es como un casillero vacío. Una vez llenado, no se puede cambiar. Si necesito otro valor, uso otra variable."
- Mostrar el ejemplo fallido en vivo: `?- X = 5, X = 6.` → `false.`
- Conectar con el funcional: en Haskell tampoco se puede mutar — mismo principio, distinta mecánica.

**Cuándo anticiparlo:** en B3 cuando introducís términos (F-11) y de nuevo en B4 cuando mostrás el trazado con variables.

---

### 2.2 🔴 Dificultad Alta: Mayúscula/Minúscula — Variable vs. Átomo

**Por qué cuesta:** en Python no hay tal distinción. El alumno escribe `madre(Ana, Carlos)` creyendo que son constantes, pero son variables.

**Error típico:**
```prolog
madre(Ana, Carlos).   % ¡Error! Ana y Carlos son VARIABLES, no átomos
?- madre(Ana, X).     % Esto unifica con cualquier relación madre/2
```

**Estrategia de corrección:**
- Repetir la regla en cada código que escribís: "minúscula = átomo fijo, MAYÚSCULA = variable libre"
- Poner una nota en el pizarrón durante todo B3: `ana ← átomo | X ← variable`
- Si un alumno comete el error, no corregirlo directamente — preguntar: "¿Qué tipo de término es `Ana`?" y dejar que llegue solo.

---

### 2.3 🟡 Dificultad Media: El Supuesto del Mundo Cerrado (CWA)

**Por qué cuesta:** los alumnos interpretan `false` como "eso no existe en el mundo", no como "no lo sé".

**Error conceptual:**
```prolog
?- madre(pedro, X).
false.
% Alumno interpreta: "Pedro no tiene hijos"
% Correcto: "No sé si Pedro tiene hijos — no declaré esa relación"
```

**Estrategia:** analogía del investigador policial. Si el detective no tiene evidencia de que Fulano estuvo en el lugar, presume que no estuvo — no porque sea inocente, sino porque el sistema solo trabaja con lo que tiene.

---

### 2.4 🟡 Dificultad Media: La Variable como "incógnita" no como "contenedor"

**Por qué cuesta:** en imperativo la variable es un contenedor mutable. En Prolog es más cercana a la variable matemática: "existe algún X tal que..."

**Reencuadre útil:**
- En `?- madre(ana, X).` → preguntar "¿existe algún X tal que Ana es madre de X?"
- En la regla `abuelo(X, Z) :- progenitor(X, Y), progenitor(Y, Z).` → "para todo X, Y, Z tal que..."

---

### 2.5 🟢 Dificultad Baja (pero frecuente): El punto `.`

Muchos alumnos olvidan el punto al final. El intérprete queda esperando más entrada.

**Estrategia:** mencionar explícitamente en la primera demostración: "En Prolog todo termina con punto. Si el intérprete no responde, probablemente falta el punto."

---

## 3. Diagnóstico de Entrada Recomendado (5 min al inicio)

Antes de la clase, hacer estas dos preguntas orales para calibrar el grupo:

**Pregunta 1 (nivel Python):**
> "En Python, si tengo una lista de tuplas `(padre, hijo)` y quiero encontrar todos los nietos de alguien, ¿cómo lo harían?"

*Objetivo: ver si el grupo razona bien en imperativo. Si tienen dificultades aquí, simplificar los ejemplos Python en B1.*

**Pregunta 2 (nivel lógico):**
> "¿Alguien conoce algún lenguaje o herramienta que no requiera escribir cómo hacer las cosas, solo qué se quiere?"

*Objetivo: detectar si alguien viene con contexto de SQL, Prolog, Datalog, etc. Si hay alguien con experiencia, invitarlo a participar activamente en B4.*

---

## 4. Estrategias de Diferenciación

### Para alumnos que van adelantado (terminan ejercicios rápido):

Proponer estas preguntas de extensión:

1. `?- ancestro(X, X).` — ¿termina? ¿por qué? *(toca loops y el orden de cláusulas)*
2. ¿Cómo escribirías `profundidad_relacion(X, Y, N)` donde N es el número de saltos?  
   *(requiere aritmética — anticipo de Clase 2)*
3. ¿Qué pasa con `hermano(X, X).`? ¿Por qué devuelve `false`? *(toca `\=`)*

### Para alumnos con dificultades:

- Reducir los ejercicios a `hermano/2` solamente — que lo trace en papel antes de ejecutar
- Dar la base de conocimiento pre-cargada (no la construyen desde cero)
- Usar la analogía de la búsqueda en un árbol genealógico dibujado en papel

### Para alumnos con perfil matemático:

Mencionar brevemente:
- Prolog implementa Resolución SLD — basado en el trabajo de Robinson (1965) y Kowalski (1974)
- La completitud de la resolución para cláusulas de Horn
- La conexión con el método de refutación (proof by contradiction)

---

## 5. Errores del Docente a Evitar

| Error | Consecuencia | Alternativa |
|---|---|---|
| Formalizar cláusulas de Horn matemáticamente en B2 | Perder el 60% del grupo antes de ver código | Mantener B2 conceptual; la formalización es bibliografía |
| Usar predicados con nombres ambiguos (`p/2`, `q/2`) | Los alumnos no entienden el significado semántico | Siempre nombres del dominio: `madre`, `ancestro`, `hermano` |
| No hacer los trazados en el pizarrón | Los alumnos no construyen el modelo mental de resolución | El pizarrón en B4 es no negociable |
| Avanzar a unificación profunda en esta clase | Scope creep — ese tema es Clase 2 | Si surge la pregunta, decir "excelente pregunta — lo vemos en detalle la próxima" |
| Mostrar predicados built-in (`is/2`, `assert/1`) antes de hora | Confunde el modelo de "base estática" | Estos van en Clase 2 |

---

## 6. Evaluación Formativa Durante la Clase

### Técnica "salida de un minuto" (final de clase)

Pedir a los alumnos que escriban en papel:
1. **Una cosa** que quedó clara de la clase de hoy
2. **Una pregunta** que quedó sin responder

Recoger los papeles — usar las preguntas para arrancar la Clase 2.

### Preguntas de verificación de comprensión (durante la clase)

Usar estas preguntas en los momentos indicados:

| Momento | Pregunta | Respuesta esperada |
|---|---|---|
| Después de F-10 (base vs. inferencia) | "¿El archivo `.pl` hace algo solo?" | No — solo al consultar |
| Después de F-13 (hechos) | "¿Por qué `madre(Ana, Carlos)` es incorrecto si Ana y Carlos son personas?" | Ana y Carlos con mayúscula son variables |
| Después de F-16 (reglas) | "Lean en voz alta la regla `abuelo`" | "X es abuelo de Z si existe Y tal que..." |
| Después de F-24 (trazado abuelo) | "¿Cuántas soluciones tiene `?- abuelo(ana, Z).`?" | 3: laura, pedro, tomas |
| Después de F-26 (recursión) | "¿Por qué `ancestro` necesita dos cláusulas?" | Una para el caso directo, otra para la cadena |

### Indicadores de comprensión (observación)

El alumno **comprendió** cuando:
- Puede leer una regla en voz alta con "si existe algún..."
- Puede predecir el resultado de una consulta antes de ejecutarla
- Distingue `X = carlos` (átomo) de `X = Carlos` (variable) sin que se lo recuerden

El alumno **no comprendió** todavía cuando:
- Escribe `X = 5, X = X + 1` esperando que funcione
- Pregunta "¿dónde está el `main`?" o "¿cómo ejecuto el programa?"
- Confunde `false` como "imposible" vs. "no tengo evidencia"

---

## 7. Conexiones con Otros Temas de la Materia

### Con temas anteriores:

| Tema | Conexión con Prolog |
|---|---|
| Imperativo (B1 Python) | Contraste: Prolog elimina el control explícito que Python requiere |
| Tipos y sistemas de tipos (B2) | Los términos Prolog no tienen tipos explícitos — inferencia de tipo dinámico |
| Funcional (B3 TypeScript) | Inmutabilidad compartida; Prolog va más lejos: no hay estado en absoluto |
| Recursión (B3 funcional) | Recursión en Prolog es más natural — sin acumuladores forzados |

### Con temas siguientes:

| Tema | Preparación desde esta clase |
|---|---|
| Clase 2 — Unificación y backtracking | Base: el modelo de trazado de B4 es la preparación directa |
| Clase 3 — Listas y recursión | La recursión con `ancestro/2` es el template para la recursión sobre listas |
| Bloque OOP (Java) | Contraste: OOP es el paradigma más alejado — retomar la tabla de comparación |
| Metaprogramación (tema optativo) | `assert/retract` en Prolog = metaprogramación nativa |

---

## 8. Preguntas de Comprensión Profunda (para examen o discusión)

Estas preguntas van más allá de los ejercicios de clase y son adecuadas para evaluaciones sumativas:

**Nivel Comprender:**
1. ¿Cuál es la diferencia semántica entre estas dos bases de conocimiento?
   ```prolog
   % Base A            % Base B
   pez(trucha).        pez(trucha).
   animal(trucha).     animal(X) :- pez(X).
   ```
   *(Base A enumera; Base B generaliza — si agregamos `pez(salmon)`, Base B automáticamente lo hace animal)*

2. ¿Qué ocurre con `?- X = Y, Y = ana.`? ¿Y con `?- X = Y, Y = ana, X = carlos.`?

**Nivel Analizar:**
3. Dada la base:
   ```prolog
   p(a, b). p(b, c). p(c, a).
   q(X, Z) :- p(X, Y), q(Y, Z).
   q(X, Y) :- p(X, Y).
   ```
   ¿Qué ocurre con `?- q(a, c).`? ¿Y si invertimos el orden de las cláusulas de `q`?

4. ¿Por qué la siguiente definición de `ancestro` es problemática?
   ```prolog
   ancestro(X, Y) :- ancestro(X, Z), progenitor(Z, Y).
   ancestro(X, Y) :- progenitor(X, Y).
   ```

**Nivel Evaluar:**
5. Tenés que modelar las reglas de un juego de ajedrez para validar jugadas. ¿Prolog o Python? Justificá.
6. ¿Qué limitaciones tiene el Supuesto del Mundo Cerrado para modelar el mundo real? ¿En qué casos fallaría?

---

## 9. Extensiones para Alumnos Avanzados

### Extensión 1 — Prolog y SQL: el puente

Los alumnos con experiencia en bases de datos pueden ver la siguiente equivalencia:

| SQL | Prolog |
|---|---|
| Tabla `madre(id_madre, id_hijo)` | `madre(ana, carlos).` (hechos) |
| `SELECT hijo FROM madre WHERE madre = 'ana'` | `?- madre(ana, X).` |
| `JOIN` | Unificación de variables |
| `VIEW` (query guardado) | Regla Prolog |
| `RECURSIVE WITH` (CTE recursivo) | Regla recursiva (`ancestro/2`) |

### Extensión 2 — Datalog

Datalog es un subconjunto de Prolog sin functores — usado en análisis estático de programas (Doop, Soufflé) y en bases de datos deductivas. Si les interesa la aplicación industrial, Datalog es el camino.

### Extensión 3 — Prolog en el ecosistema Python

```python
# pyswip: interfaz Python ↔ SWI-Prolog
from pyswip import Prolog
prolog = Prolog()
prolog.assertz("madre(ana, carlos)")
prolog.assertz("abuelo(X,Z) :- madre(X,Y), madre(Y,Z)")
list(prolog.query("abuelo(ana, Z)"))
# → [{'Z': 'carlos'}]
```

Útil para alumnos que quieren integrar razonamiento lógico en proyectos Python.

---

## 10. Tabla de Tiempos Críticos

Estos son los momentos donde el tiempo puede desbordarse y qué hacer:

| Riesgo | Señal de alerta | Intervención |
|---|---|---|
| B2 se extiende | Los alumnos hacen preguntas sobre lógica formal | "Anotamos esa pregunta y la cerramos en las próximas clases — avancemos al código" |
| B3 demo en vivo tarda | Problemas de instalación/conexión | Tener SWISH preparado como backup; el código ya en el editor |
| B4 trazado toma más tiempo | Los alumnos piden repetir pasos | Normal — es la parte más importante. Recortar B5 si es necesario |
| B6 ejercicios se extienden | El grupo quiere resolver todos | Parar con `hermano/2` como mínimo viable; el resto como tarea |

---

## 11. Recursos de Preparación del Docente

### Antes de la clase — lista de verificación:

- [ ] Probar el entorno SWI-Prolog/SWISH con la base `familia.pl` completa
- [ ] Tener `familia.pl` listo para abrir directamente (no teclear en clase)
- [ ] Releer Sebesta Cap. 16, pp. 703–730 (sintaxis y hechos/reglas)
- [ ] Rever los trazados de B4 — practicar hacerlos en 5 minutos en pizarrón
- [ ] Revisar la pregunta de salida: `bisabuelo(X, Z)` — ¿cuántas cláusulas?

### Bibliografía de preparación profunda:

- **Clocksin & Mellish** — *Programming in Prolog* (2003): Caps. 1–3 para la sintaxis y el modelo de ejecución que el alumno va a ver en Clase 2
- **Sebesta** — Cap. 16, pp. 730–760: resolución y backtracking (material de Clase 2 — conviene conocerlo de antemano)
- **Kowalski, R.** (1979) — "Algorithm = Logic + Control" — el artículo fundacional del paradigma lógico. Lectura opcional pero muy recomendable (acceso libre).

---

## 12. Archivo de Ejemplo Listo para Usar

Guardar como `familia.pl` en el directorio de trabajo de la clase:

```prolog
% ═══════════════════════════════════════════════════
%  familia.pl — BASE DE CONOCIMIENTO
%  Paradigmas y Lenguajes 2026 — Clase T06-C1
% ═══════════════════════════════════════════════════

% ─── HECHOS ─────────────────────────────────────────
madre(ana,     carlos).
madre(ana,     beatriz).
padre(carlos,  laura).
padre(carlos,  pedro).
madre(beatriz, tomas).

% ─── RELACIONES DIRECTAS ────────────────────────────
progenitor(X, Y) :- madre(X, Y).
progenitor(X, Y) :- padre(X, Y).

% ─── RELACIONES DERIVADAS ───────────────────────────
abuelo(X, Z) :-
    progenitor(X, Y),
    progenitor(Y, Z).

hermano(X, Y) :-
    progenitor(P, X),
    progenitor(P, Y),
    X \= Y.

tio(X, Z) :-
    hermano(X, Y),
    progenitor(Y, Z).

% ─── RECURSIÓN ──────────────────────────────────────
ancestro(X, Y) :- progenitor(X, Y).
ancestro(X, Y) :- progenitor(X, Z), ancestro(Z, Y).

% ─── DERIVADA DE RECURSIÓN ──────────────────────────
descendiente(X, Y) :- ancestro(Y, X).
```

**Sesión de carga y consultas de verificación:**
```
?- consult('familia.pl').
true.
?- abuelo(ana, Z).
Z = laura ; Z = pedro ; Z = tomas.
?- hermano(X, Y).
X = carlos, Y = beatriz ; X = beatriz, Y = carlos ;
X = laura, Y = pedro ;   X = pedro, Y = laura.
?- ancestro(ana, tomas).
true.
```

---

*Guía del profesor generada por: Lic. Marcos (topic-designer) — 2026-04-17*  
*Estado: borrador — pendiente de loop de validación*
