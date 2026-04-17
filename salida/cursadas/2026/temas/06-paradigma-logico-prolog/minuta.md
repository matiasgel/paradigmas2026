# Minuta de Clase — Tema 06: Paradigma Lógico: Prolog — Clase 1 de 3

**Materia:** Paradigmas y Lenguajes de Programación 2026  
**Docente:** Matías Gel — UNTDF / IDEI  
**Duración:** 120 minutos  
**Clase en el ciclo:** 1 de 3 (Introducción al Paradigma Lógico)  
**Generado por:** Dr. Roberto (class-writer) — 2026-04-17  

---

## Resumen Ejecutivo

Esta clase introduce el paradigma lógico a través de Prolog. El hilo conductor es la **base de conocimiento familiar**: una estructura simple que permite demostrar hechos, reglas, consultas, trazado de resolución y recursión en 120 minutos. El foco es conceptual y práctico — muchos ejemplos, trazados en pizarrón y ejercicios cortos en clase.

---

## Estructura Temporal

| Bloque | Minutos | Filminas | Actividad |
|--------|---------|----------|-----------|
| B1 — Motivación | 0–15 | F-01 a F-05 | Exposición + pregunta abierta |
| B2 — Fundamentos | 15–35 | F-06 a F-12 | Exposición con ejemplos |
| B3 — Sintaxis Prolog | 35–60 | F-13 a F-20 | Demo en vivo + construcción incremental |
| B4 — Trazado | 60–85 | F-21 a F-28 | Pizarrón participativo |
| B5 — Comparación | 85–95 | F-29 a F-31 | Discusión guiada |
| B6 — Ejercicios | 95–105 | F-32 a F-34 | Práctica guiada |
| B7 — Cierre | 105–120 | F-35 a F-38 | Resumen + anticipo |

---

## B1 — Motivación (0–15 min)

### Entrada: pregunta disparadora (2 min)

Comenzar con la pregunta sin contexto:

> *"¿Cómo escribirían en Python una función que, dada una persona, encuentre todos sus nietos? Piensen 30 segundos."*

Dejar que los alumnos piensen. No dar la respuesta todavía.

### Presentación del paradigma (5 min) — F-01, F-02

Mostrar **F-01**: el cuarto paradigma. Remarcar que cada paradigma tiene una *metáfora central*:
- Imperativo → receta de cocina
- Funcional → transformación matemática
- Lógico → **experto consultado**

Pasar a **F-02**: mostrar el problema de la familia. Escribir en el pizarrón el árbol:
```
Ana → Carlos → Laura
Ana → Carlos → Pedro
Ana → Beatriz → Tomás
```

Mostrar la solución Python (F-02): código que *busca* la respuesta.  
Luego mostrar la solución Prolog: código que *declara* las relaciones.

**Retomar la pregunta inicial:** ahora con el contexto, ¿ven la diferencia?

### Declarativo vs. Imperativo (4 min) — F-03

**F-03**: tabla comparativa. Señalar especialmente:
- En Prolog no escribimos el *algoritmo de búsqueda* — el motor lo hace
- La misma base sirve para múltiples consultas distintas

### Historia y aplicaciones (4 min) — F-04, F-05

**F-04** rápido — mostrar que Prolog tiene 50 años y sigue vivo.  
**F-05** — por qué estudiarlo hoy: grafos de conocimiento, neuro-simbólico, bases relacionales.

Citar a Sebesta: *"The study of logic programming can broaden a programmer's perspective..."*

---

## B2 — Fundamentos Teóricos (15–35 min)

### Lógica proposicional — repaso (4 min) — F-06

**F-06**: mostrar los conectivos. No profundizar — los alumnos los conocen.  
Señalar la correspondencia con Prolog:
- `∧` → `,` en el cuerpo de una regla
- `→` → `:-`
- `¬` → `\+` (se verá en Clase 2)

### Cálculo de predicados (6 min) — F-07

**F-07**: explicar por qué la lógica proposicional no alcanza:

> *"¿Cómo digo 'alguien es madre de alguien' en lógica proposicional? No puedo — necesito predicados."*

Dibujar en pizarrón:
```
madre(ana, carlos)   ← predicado binario
pez(trucha)          ← predicado unario
suma(2, 3, 5)        ← predicado ternario
```

Señalar la diferencia entre cuantificación universal (variables en reglas) y existencial (consultas).

### Cláusulas de Horn (6 min) — F-08

**F-08**: la forma fundamental de Prolog.

Escribir en pizarrón la forma general:
```
H :- B₁, B₂, ..., Bₙ.
```

Mostrar los tres tipos:
1. Hecho: `madre(ana, carlos).` — sin cuerpo
2. Regla: `abuelo(X,Z) :- progenitor(X,Y), progenitor(Y,Z).`
3. Consulta: `?- abuelo(ana, Z).` — sin cabeza

### Resolución conceptual (4 min) — F-09

**F-09**: el motor de Prolog en términos simples.  
No entrar en detalles matemáticos. La idea clave:

> *"Prolog tiene un motor que prueba si una consulta es consecuencia lógica de la base. Lo hace por resolución hacia atrás (backward chaining)."*

### BASE vs. INFERENCIA — distinción clave (5 min) — F-10

**F-10**: **pausar aquí y enfatizar**. Esta es la confusión más común.

Abrir SWI-Prolog o SWISH. Mostrar:
1. Crear el archivo `familia.pl` con los hechos
2. Cargarlo con `consult('familia.pl').`
3. Hacer una consulta

Remarcar: **el archivo no hace nada solo**. Solo cuando hacemos la consulta el motor actúa.

**Pregunta a la clase:**
> *"Si agrego un hecho al archivo después de cargarlo, ¿la consulta lo ve?"*  
> *(Respuesta: No — hay que recargar. O usar `assert/1` — se verá en Clase 2)*

### Términos y Unificación preview (5 min) — F-11, F-12

**F-11**: tabla de tipos de términos. Recorrerla rápidamente.  
Ejercicio oral: *"¿Qué tipo es `ana`? ¿`X`? ¿`f(a, b)`? ¿`_`?"*

**F-12**: preview de unificación. Solo mostrar los ejemplos básicos.  
Dejar claro: `=` en Prolog no es asignación. Profundizar en Clase 2.

---

## B3 — Sintaxis Prolog en Vivo (35–60 min)

**Instrucción de ritmo:** en este bloque, cada concepto nuevo va seguido de código en vivo. El docente escribe en el editor, los alumnos ven la pantalla proyectada.

### Hechos (8 min) — F-13, F-14

**F-13**: construir la base paso a paso en el editor.

```prolog
% Escribir uno por uno, explicando cada línea
madre(ana, carlos).
```

Preguntar: *"¿Alguien me da el segundo hecho?"* → `madre(ana, beatriz).`  
Completar con el resto.

**F-14**: mostrar ejemplos de otros dominios brevemente. Idea: los hechos sirven para CUALQUIER dominio.

Ejercicio rápido:
> *"¿Cómo escribirían 'El libro Sebesta tiene 792 páginas'?"*  
> `libro(sebesta, 'Concepts of Programming Languages', 792).`

### Reglas (8 min) — F-15, F-16

**F-15**: construir `progenitor/2` en vivo.

```prolog
progenitor(X, Y) :- madre(X, Y).
```

Leer en voz alta. Luego agregar la segunda cláusula:
```prolog
progenitor(X, Y) :- padre(X, Y).
```

Explicar: dos cláusulas para el mismo predicado = OR.

Construir `abuelo/2`:
```prolog
abuelo(X, Z) :- progenitor(X, Y), progenitor(Y, Z).
```

**F-16**: leer la regla `abuelo` en voz alta con la clase:
> *"X es abuelo de Z si..."*  
Preguntar a un alumno que la complete.

### Consultas (9 min) — F-17, F-18

**F-17**: cargar la base. Hacer las consultas una por una:

```prolog
?- madre(ana, carlos).    % → true
?- madre(carlos, ana).    % → false
?- madre(ana, X).         % → X = carlos
```

Mostrar el `;` en acción:
```prolog
?- madre(ana, X).
X = carlos ;
X = beatriz.
```

**F-18**: explicar qué hace `;`. Luego mostrar `findall/3`:
```prolog
?- findall(X, madre(ana, X), L).
L = [carlos, beatriz].
```

### La base completa visual (5 min) — F-19, F-20

**F-19**: mostrar el archivo completo con toda la base. Pedir a un alumno que lea las reglas.

**F-20**: dibujar el árbol de relaciones en el pizarrón:
```
    Ana
   /    \
Carlos  Beatriz
/   \       \
Laura Pedro  Tomás
```

Mostrar cómo las consultas navegan este grafo.

---

## B4 — Trazado Manual (60–85 min)

**Instrucción:** este bloque es el más importante. Pizarrón obligatorio. Ritmo: participativo.

### Algoritmo de resolución (3 min) — F-21

**F-21**: mostrar el algoritmo en pasos simples. No formalizar demasiado.  
La idea que debe quedar: *"Prolog prueba de arriba a abajo, y si falla vuelve atrás."*

### Ejemplo 1 — consulta simple (4 min) — F-22

**F-22**: escribir en el pizarrón:

```
?- madre(ana, carlos).
```

Preguntar a la clase: *"¿Qué cláusula usa el motor?"*  
Trazar paso a paso. Mostrar que es trivial: unifica directo con el hecho.

### Ejemplo 2 — variable libre (6 min) — F-23

**F-23**: escribir:
```
?- madre(ana, X).
```

Trazar en pizarrón. Mostrar cómo X se instancia a `carlos` primero, luego backtracking y `beatriz`.  
**Preguntar:** *"¿Cuántas soluciones hay? ¿Por qué la cláusula de Beatriz no calza?"*

### Ejemplo 3 — regla derivada (8 min) — F-24, F-25

**F-24-25**: el ejemplo más complejo. Hacerlo despacio.

```
?- abuelo(ana, Z).
```

Dibujar el árbol de derivación (**F-25**) en el pizarrón:
```
        abuelo(ana, Z)
       /               \
  Y=carlos           Y=beatriz
  /      \               \
Z=laura  Z=pedro       Z=tomas
```

Preguntar a la clase en cada paso: *"¿Qué cláusula prueba Prolog ahora?"*

### Ejemplo 4 — recursión (9 min) — F-26, F-27, F-28

**F-26**: introducir `ancestro/2`. Escribir en pizarrón las dos cláusulas.  
Leer caso base y caso recursivo en voz alta.

**F-27**: trazar `?- ancestro(ana, pedro).`  
Mostrar cómo el caso base falla primero, luego el recursivo tiene éxito.

**F-28**: comparar con Python en pantalla.  
Remarcar: en Prolog la recursión emerge de las reglas. No hay `for`, no hay `return`.

**⚠️ Advertencia:** *"¿Qué pasa si pongo el caso recursivo antes del base?"*  
Demostración rápida: riesgo de bucle infinito. El **orden importa**.

---

## B5 — Comparación de Paradigmas (85–95 min)

### Tabla comparativa (5 min) — F-29

**F-29**: recorrer la tabla.  
Preguntar: *"¿Qué característica del paradigma lógico les parece más poderosa?"*

### ¿Cuándo usar Prolog? (3 min) — F-30

**F-30**: ejemplos de dominio. Mencionar que no es el mejor lenguaje para todo.

### Prolog e IA moderna (2 min) — F-31

**F-31**: brevísimo. Conectar con el contexto de 2026: knowledge graphs, neuro-simbólico.

---

## B6 — Ejercicios Rápidos (95–105 min)

### Ejercicio 1: hermano/2 (4 min) — F-32

**F-32**: enunciar. Dar 2 minutos para que los alumnos escriban en papel.  
Pedir solución a un alumno. Escribir en el editor, probar.

**Trampa pedagógica:** preguntar qué pasa sin `X \= Y`.  
Demo rápida: devuelve "X es hermano de sí mismo" → indeseable.

### Ejercicio 2: trazado hermano (3 min) — F-33

**F-33**: trazar `?- hermano(carlos, Z).` rápidamente.  
Señalar que el `\= Y` hace fallar la primera solución (Z = carlos).

### Ejercicio 3: tío y descendiente (3 min) — F-34

**F-34**: mostrar `tio/2` y `descendiente/2`.  
Remarcar: `descendiente` solo necesita una cláusula porque *reutiliza* `ancestro`.  
Punto pedagógico: en Prolog se compone conocimiento.

---

## B7 — Cierre (105–120 min)

### Resumen de los 5 conceptos (4 min) — F-35

**F-35**: recorrer los 5 puntos con la clase.  
Mostrar la base completa que construimos juntos.

### Confusiones comunes (4 min) — F-36

**F-36**: repasar la tabla de confusiones.  
Énfasis en **CWA** (Supuesto del Mundo Cerrado):  
> *"false no significa imposible — significa 'no lo sé'"*

### Anticipo Clase 2 (3 min) — F-37

**F-37**: presentar los temas de la próxima clase.  
Dejar la pregunta abierta:
> *"¿Qué pasa con `?- ancestro(X, X).`? Piénsenlo. Lo vemos en Clase 2."*

### Recursos y tarea (4 min) — F-38

**F-38**: mostrar SWISH online. Recomendar instalar SWI-Prolog.

**Tarea para casa:**
1. Cargar la base familiar en SWISH
2. Agregar `bisabuelo(X, Z)` — ¿cuántas cláusulas?
3. Agregar una generación más y probar las consultas

**Código de la clase disponible en:** repositorio GitHub del curso.

---

## Notas de Gestión de Tiempo

- **Si el grupo es rápido:** extender B4 con un ejemplo adicional (e.g. `?- hermano(X, Y).` completo)
- **Si el grupo está confundido con F-10 (base vs. inferencia):** reducir B2 (F-06 se puede omitir) y dar más tiempo a la demo en vivo
- **Si falta tiempo:** B5 se puede reducir a 5 min (solo F-29) sin perder comprensión
- **Buffer:** los últimos 5 min de B7 son flexibles

## Preguntas Frecuentes Anticipadas

| Pregunta | Respuesta |
|---|---|
| "¿Por qué `X` con mayúscula?" | Convención Prolog: MAYÚSCULA = variable, minúscula = átomo |
| "¿`=` asigna un valor?" | No — unifica. Si X ya tiene valor, falla. Profundizar en Clase 2 |
| "¿El orden de los hechos importa?" | Para correctitud no, para eficiencia sí. Para recursión puede causar ciclos |
| "¿Prolog se usa en la industria?" | Erlang derivó de él; IBM Watson; PLCs; sistemas expertos; Datalog |
| "¿Puede haber ciclos en la base?" | Sí, y causan bucles. `ancestro(X, X)` es un clásico. Se ve en Clase 2 |
| "¿Qué es `false.` al final de consulta?" | No hay más soluciones (no que sea imposible) |

---

*Minuta generada por: Dr. Roberto (class-writer) — 2026-04-17*  
*Estado: borrador — pendiente de revisión docente*
