# Clase: Introducción a Programación Funcional con TypeScript
**Materia:** Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI
**Tema:** 03 | **Módulo:** II
**Duración:** 120 minutos | **Fecha:** ___________

> **Cómo usar esta minuta:** Cada sección corresponde exactamente a una filmina.
> Los momentos (▶) son acciones secuenciales dentro de esa filmina.
> El texto entrecomillado es lo que decís en voz alta.
> El código está inline — no necesitás abrir `filminas.md` para dar la clase.

---

## Objetivos de la Clase

- OA-1: Explicar la diferencia entre computación por transformación de estado vs computación por reescritura de expresiones
- OA-2: Enunciar los tres pilares del paradigma funcional: funciones puras, inmutabilidad, transparencia referencial
- OA-3: Escribir funciones puras en TypeScript usando `const`, arrow functions, sin efectos colaterales
- OA-4: Usar `map`, `filter` y `reduce` en TypeScript como sustitutos de los loops imperativos
- OA-5: Justificar por qué cada restricción funcional mejora la predecibilidad del código
- OA-6: Reconocer en Clojure la expresión pura de los mismos conceptos
- OA-7: Trazar el origen del paradigma desde el λ-cálculo y explicar su entrada en los multiparadigma

---

## BLOQUE A0 — Historia: del Entscheidungsproblem al funcional (20 min)

### [F-01] Portada del tema

**Tiempo:** 1 min

**▶ Al mostrar la portada**
> "Hoy arrancamos el Módulo II — el paradigma funcional. Antes de escribir una sola línea de código, vamos a entender de dónde viene este paradigma. No voy a empezar con TypeScript todavía."
> "El origen es una pregunta matemática de 1928. Parece filosófica, pero define dos modelos de computación que todavía usamos hoy — incluyendo la CPU de cualquier computadora y el lenguaje que vamos a ver hoy."

**→ Transición:** "Empecemos en Berlin, 1928. David Hilbert."

---

### [F-02] El origen: una pregunta de 1928

**Tiempo:** 2 min

**▶ Al mostrar el título y la cita de Hilbert**
> "Primer Congreso Internacional de Matemáticas, 1928. Hilbert plantea lo que él llama el Entscheidungsproblem — el problema de la decisión."
> "La pregunta es esta" — leer en voz alta: _"¿Existe un procedimiento mecánico que, dado cualquier enunciado matemático, determine si es verdadero o falso?"_
> "Mecánico quiere decir: un algoritmo. Un proceso que cualquier persona — o cualquier máquina — pueda ejecutar siguiendo pasos."

**▶ Al señalar la sección "Por qué importa"**
> "Hilbert buscaba algo enorme: demostrar que toda la matemática podía fundamentarse de forma completa y decidible. Si existía ese procedimiento, la matemática era como un termómetro: metías un enunciado y salía verdadero o falso."
> "Pero mirá la última línea: _la respuesta llegó en 1936, desde dos lugares a la vez, sin coordinación_. Eso es lo que hace interesante esta historia."

💬 **Pregunta:** "¿Qué sería un enunciado matemático en este contexto?"
- Si responden bien: "Exacto — cualquier afirmación formal, como 'el número 17 es primo', o 'esta función siempre termina'."
- Si no responden: "Por ejemplo: 'el número 37 es primo'. ¿Existe un procedimiento mecánico para decidirlo? Sí, probar divisores. Pero, ¿existe uno para **cualquier** enunciado posible? Esa es la pregunta difícil."

**→ Transición:** "Veamos quién respondió primero — desde Cambridge, Inglaterra."

---

### [F-03] Alan Turing — La Máquina (Cambridge, 1936)

**Tiempo:** 3 min

**▶ Al mostrar "El modelo" — el diagrama de la Máquina de Turing**
> "Alan Turing tiene 24 años en 1936. Trabaja en Cambridge, no con Hilbert — inventó su solución de forma independiente."
> "Su modelo de computación: imaginá una cinta infinita dividida en celdas, como una cinta de papel. Una cabeza que puede leer el símbolo en la celda actual, escribir un símbolo nuevo, moverse a izquierda o derecha, y cambiar de estado."
> "Eso es todo. Con eso, Turing define qué significa 'computar'."
> Señalar el concepto clave: "Computar, para Turing, es **modificar el estado de la cinta** paso a paso. El cómputo es mutación secuencial."

**▶ Al mostrar "El resultado" — el halting problem**
> "Y con ese modelo demostró algo brillante y frustrante al mismo tiempo: el Halting Problem."
> "¿Existe un programa que, dado cualquier otro programa y su input, determine si ese programa termina o entra en loop infinito? La respuesta es **no** — ningún algoritmo puede hacer eso en el caso general."
> "Y eso es suficiente para responder a Hilbert: si no podemos decidir si un programa termina, no podemos decidir todos los enunciados matemáticos."

**▶ Al mostrar "El legado en LP"**
> "Pero lo importante para nosotros es el **legado**: Máquina de Turing → arquitectura von Neumann → paradigma imperativo."
> "Toda CPU ejecuta instrucciones que modifican registros y memoria. Eso es la Máquina de Turing implementada en silicio."

💬 **Pregunta:** "¿Y eso es exactamente lo que hace la CPU de cualquier computadora?"
- Respuesta esperada: sí. Confirmar: "Sí. `mov eax, 5` — escribir 5 en el registro eax. Eso es la Máquina de Turing."

**→ Transición:** "Ese mismo año, 1936, en Princeton, New Jersey, Alonzo Church llegó a la misma respuesta por un camino completamente distinto."

---

### [F-04] Alonzo Church — El λ-cálculo (Princeton, 1936)

**Tiempo:** 3 min

**▶ Al mostrar "El modelo"**
> "Church no inventó una máquina. Church inventó un lenguaje matemático. Lo llamó lambda-cálculo."
> "En el λ-cálculo, todo es función. No hay variables que cambien de valor, no hay estados, no hay memoria. Solo hay expresiones — y el cómputo es **reemplazar una expresión por su equivalente**."
> "Cito textualmente de la filmina: _el cómputo es sustitución de expresiones_. Eso es lo opuesto a la Máquina de Turing."

**▶ Al mostrar el ejemplo de β-reducción**
> "El ejemplo más simple de sustitución es esto. Si tengo `(λx. x*x) 3`, el λ-cálculo dice: sustituí `x` por `3` → obtenés `3*3` → obtenés `9`. Ningún estado cambió. Solo reemplazaste una expresión por su valor."

**▶ Al mostrar "El legado en LP"**
> "Church llegó a la misma conclusión que Turing: el Entscheidungsproblem no tiene solución general."
> Señalar la línea: "Y el legado: λ-cálculo → Lisp (1958) → paradigma funcional. McCarthy en MIT tomó el λ-cálculo y lo convirtió en un lenguaje de programación."

💬 **Pregunta:** "¿Y qué tiene que ver el λ-cálculo con que hoy escribamos `n => n * 2` en TypeScript?"
- Si responden bien: "Exacto. Eso es una lambda. La sintaxis cambió, la idea es la misma."
- Si no responden: "La notación `n => n * 2` en JavaScript/TypeScript es una función anónima — lambda. La palabra 'lambda' viene directamente de este cálculo de 1936."

**→ Transición:** "¿Cuál de los dos modelos es más poderoso?"

---

### [F-05] Dos filosofías de computación — tabla comparativa

**Tiempo:** 3 min

**▶ Al mostrar la Tesis Church-Turing y el párrafo introductorio**
> "La Tesis Church-Turing dice lo siguiente: todo lo que se puede computar con la Máquina de Turing, también se puede computar con el λ-cálculo. Y viceversa."
> "Son **equivalentes en poder**. Ninguno puede resolver problemas que el otro no pueda. El Halting Problem es insoluble para ambos."

**▶ Al recorrer la tabla fila por fila**
Señalar cada fila y leer en voz alta:

| | Imperativo | Funcional |
|---|---|---|
| Computar es… | Modificar estado de la cinta/memoria | Reducir una expresión a su forma normal |
| Elemento central | Variable mutable + asignación | Función + sustitución |
| Control de flujo | Instrucciones, loops | Recursión, composición |
| Primer lenguaje | Fortran (1957) | Lisp (1958) |

> "Mirá la fila 'Computar es…' — esa es la diferencia fundamental. No es una diferencia de sintaxis. Es una diferencia de **qué significa computar**."
> "Para uno, computar es modificar el estado del mundo. Para el otro, es encontrar el valor de una expresión."

**▶ Al mostrar la nota final (⚠️)**
> "Esto es importante: el λ-cálculo no nació para programar. Nació para demostrar que un problema matemático era imposible. La programación funcional es una consecuencia."

💬 **Pregunta:** "¿Entonces los dos paradigmas son lo mismo?"
- Si responden "sí": "Mismo poder de cómputo — cualquier programa que escribís en uno, podés escribirlo en el otro. Pero distintas herramientas mentales. Hay problemas donde uno es más natural que el otro."
- Si responden "no": "Depende qué comparan. En poder computacional son equivalentes. En expresividad para ciertos problemas, son radicalmente distintos."

**→ Transición:** "¿Cómo se convirtió el λ-cálculo en lenguajes reales? Historia rápida."

---

### [F-06] Recorrido de lenguajes funcionales — parte 1 (1958–1990)

**Tiempo:** 2 min

**▶ Al mostrar la tabla**
> "Recorrida rápida — no vamos a profundizar en cada uno, pero quiero que vean el patrón."
Recorrer cada fila señalando año y nicho actual:

| Año | Lenguaje | Nicho actual |
|---|---|---|
| 1958 | Lisp | IA simbólica, Emacs |
| 1973 | ML | Compiladores, inferencia de tipos |
| 1975 | Scheme | Educación — base teórica |
| 1986 | Erlang | Telecomunicaciones, WhatsApp |
| 1990 | Haskell | Finanzas cuantitativas, criptografía |

> "Erlang — WhatsApp usa Erlang en producción para 2 billones de usuarios. No es un lenguaje académico."
> "Haskell — el lenguaje puramente funcional más conocido. Sigue siendo referencia de rigor semántico en 2026."

**▶ Al mostrar la nota final**
> "La nota dice: _cada lenguaje nació para resolver un problema concreto, no como ejercicio académico_. Ese patrón se va a repetir con los modernos."

**→ Transición:** "Los últimos 20 años — donde aparecen blockchain e IA."

---

### [F-07] Recorrido de lenguajes funcionales — parte 2 (2003–2012)

**Tiempo:** 2 min

**▶ Al mostrar la tabla**
Recorrer cada fila señalando nicho:

| Año | Lenguaje | Nicho actual |
|---|---|---|
| 2003 | Scala | Big Data — Apache Spark, Kafka |
| 2005 | F# | Finanzas cuantitativas, .NET |
| 2007 | Clojure | Blockchain, concurrencia — Nubank |
| 2012 | Elixir | Web tiempo real, IoT, BEAM/Erlang |

> "Clojure — Rich Hickey, 2007. Dialecto de Lisp en la JVM. Lo vamos a usar hoy como referencia de funcional puro. Nubank — el banco digital más grande de Latinoamérica — corre en Clojure."
> "Scala — Apache Spark, que es el framework de procesamiento de datos más usado en big data industrial, está escrito en Scala."
> "Elixir — corre sobre la misma VM que Erlang. WhatsApp se construyó en Erlang; Discord usa Elixir."

**▶ Al mostrar la sección "Por qué esta época"**
> "¿Por qué exactamente en esta época? Señalar el texto: _los problemas de concurrencia y escala se volvieron inmanejables con estado mutable compartido_."
> "A mediados de los 2000s los CPUs dejaron de crecer en frecuencia de clock y pasaron a múltiples núcleos. Si tenés estado mutable y múltiples threads, necesitás locks, sincronización, y eso genera bugs difíciles de reproducir."
> "El funcional elimina ese problema de raíz: si nada muta, no hay nada para coordinar."

**→ Transición:** "¿Y cómo llegó al mainstream — a Java, TypeScript, Python?"

---

### [F-08] ¿Por qué el funcional entró en los lenguajes multiparadigma?

**Tiempo:** 3 min

**▶ Al mostrar la sección "La causa: el fin del clock scaling"**
> "A mediados de los 2000, Intel y AMD anunciaron algo que cambió el mundo del software: los procesadores dejaron de crecer en frecuencia. Llegaron al límite físico del consumo de energía y el calor."
> "En vez de hacer los procesadores más rápidos, empezaron a poner más núcleos: 2, 4, 8, 16. Para aprovecharlos, el software tiene que correr en paralelo."
> "Y ahí está el problema: si tenés estado mutable compartido entre threads, cualquier operación sobre ese estado puede pisar la de otro thread. Eso se llama condición de carrera. Son bugs que solo aparecen a veces, bajo carga, imposibles de reproducir."
> "El funcional los elimina de raíz: si ninguna función modifica nada, no hay nada que coordinar."

**▶ Al recorrer la tabla de adopción**
Señalar cada fila, leer año y qué incorporó:

| Lenguaje | Año | Qué incorporó |
|---|---|---|
| Java | 2014 (Java 8) | Lambdas, Stream API, `Optional` |
| JavaScript | 2015 (ES6) | Arrow functions, `.map()`, `.filter()`, `.reduce()` |
| TypeScript | desde 2012 | Todo JS + tipos estáticos, `readonly` |
| Python | desde 2.x | `map`, `filter`, `functools` |
| Rust | 2015 | Immutability by default, closures |
| Kotlin / Swift | 2011 / 2014 | `val`, colecciones funcionales |

> "TypeScript ya nació con soporte funcional. Hoy vamos a usarlo con restricciones funcionales explícitas."

**▶ Al mostrar la nota final**
> Leer: _"La tendencia no reemplazó al imperativo — lo enriqueció."_
> "I/O, base de datos, interfaz: imperativo. Transformación de datos, lógica de negocio, concurrencia: funcional. Los problemas modernos mezclan ambos."

**→ Transición:** "Antes de arrancar con el código, hay una frase que los va a acompañar todo el módulo."

---

### [F-09] Frase de anclaje

**Tiempo:** 1 min

**▶ Al mostrar la filmina — mostrarla en silencio 5-10 segundos antes de hablar**
> Leer la frase en voz alta lentamente:
> _"Si el paradigma imperativo es la Máquina de Turing hecha lenguaje… el funcional es el λ-cálculo de Church hecho lenguaje."_

> "Aprender ambos no es aprender dos herramientas. Es entender las dos formas fundamentales de formalizar la computación que existen desde 1936."

💬 **Para reflexionar — no esperar respuesta, dejar que lo piensen:**
> "¿Cuándo conviene computar modificando estado? ¿Cuándo conviene computar reduciendo expresiones?"

**→ Transición:** "Ahora sí — primer paso hacia el código. El mismo problema, dos formas de resolverlo."

---

## BLOQUE A — ¿Qué es el paradigma funcional? (10 min)

### [F-10] El mismo problema — versión imperativa

**Tiempo:** 3 min

**▶ Al mostrar el título y el código ❌**
> "El problema es clásico: dada la lista `[1, 2, 3, 4, 5, 6]`, quiero sumar el cuadrado de los números pares. Resultado esperado: `4 + 16 + 36 = 56`."
> "Primero, la forma imperativa — como lo haríamos en Algoritmos 1."

Señalar cada línea mientras la mencionan:
```typescript
const numeros = [1, 2, 3, 4, 5, 6];
let suma = 0;                           // ← acumulador mutable externo

for (let i = 0; i < numeros.length; i++) {  // ← loop
  if (numeros[i] % 2 === 0) {               // ← filtro inline
    suma += numeros[i] * numeros[i];         // ← mutación
  }
}
```

> Señalar `let suma = 0`: "Esta variable vive **antes** del loop, **durante** el loop, y **después** del loop. Cualquier código en ese scope puede leerla o modificarla."
> Señalar el `for`: "El loop dice *cómo* recorrer el array — índice, condición de parada, incremento. Pero lo que me interesa es *qué* hacer con cada elemento. Están mezclados."
> Señalar `suma +=`: "Y acá la mutación: en cada iteración, `suma` cambia. Para entender el resultado tengo que simular el estado en mi cabeza."

**▶ Al mostrar "Identificar los problemas"**
> Leer cada punto con la clase: "acumulador mutable externo — ¿qué problema genera eso?"
> "No es testeable en aislamiento: si quiero testear esta lógica, necesito inicializar `suma`, correr el loop, observar el resultado final."
> "No es paralelizable: si dos threads corren partes del array, ¿sobre qué `suma` acumulan?"

**→ Transición:** "Ahora la misma operación, versión funcional."

---

### [F-11] El mismo problema — versión funcional

**Tiempo:** 4 min

**▶ Al mostrar el código ✅**
> "El mismo problema, la misma lista, el mismo resultado."

Señalar cada línea del pipeline:
```typescript
const numeros = [1, 2, 3, 4, 5, 6];

const suma = numeros
  .filter(n => n % 2 === 0)          // seleccionar pares: [2, 4, 6]
  .map(n => n * n)                    // elevar al cuadrado: [4, 16, 36]
  .reduce((acc, n) => acc + n, 0);   // sumar: 56
```

> "Línea 1: `filter(n => n % 2 === 0)` — quédate con los pares. El array original no cambia. Resultado: `[2, 4, 6]`."
> "Línea 2: `map(n => n * n)` — elevá cada uno al cuadrado. Nuevo array: `[4, 16, 36]`."
> "Línea 3: `reduce((acc, n) => acc + n, 0)` — sumá todos. Resultado: `56`."
> "Cada operación hace **una sola cosa**. Ninguna modificó `numeros`. El resultado vive en `suma` y no puede cambiar — es `const`."

**▶ Al mostrar "¿Qué ganamos?"**
> Leer la tabla con la clase y comentar cada fila:
- **Trazabilidad**: "Puedo leer de arriba a abajo y entender qué hace sin simular estado."
- **Testeable por partes**: "Puedo testear el `filter` solo, el `map` solo, el `reduce` solo."
- **Paralelizable**: "Ninguna operación modifica estado compartido — se puede distribuir."
- **Lee como una especificación**: "La línea dice *qué* quiero, no *cómo* iterar."

💬 **Pregunta:** "¿Cuál es más fácil de leer? ¿Cuál es más fácil de testear?"
- Dejar que respondan libremente. Si dicen imperativo es más fácil: "¿Más fácil de leer o más familiar? Son cosas distintas."

**→ Transición:** "¿Cómo modela el funcional la idea de computar? Hay un modelo matemático preciso."

---

### [F-12] El modelo funcional — cómputo como reescritura de expresiones

**Tiempo:** 3 min

**▶ Al mostrar el título y el párrafo del modelo**
> "En el modelo funcional, un programa no es _hacer cosas_ — es una expresión que se _reduce_ a un valor."
> "El término técnico es β-reducción. Viene del λ-cálculo de Church, §11.1 de Gabbrielli-Martini."

**▶ Al mostrar el ejemplo de reducción paso a paso**
Señalar cada flecha y leer en voz alta:
```
suma(suma(1, 2), suma(3, 4))
  → suma(3, suma(3, 4))     // sustituyo suma(1,2) por 3
  → suma(3, 7)               // sustituyo suma(3,4) por 7
  → 10                        // resultado final
```
> "¿Qué hice en cada paso? Reemplazar una expresión por su equivalente. No modifiqué nada. No hay variables cambiando."
> "Podría hacer estos pasos en cualquier orden — `suma(3,4)` antes que `suma(1,2)` — y el resultado sería el mismo. Eso es porque las subexpresiones son independientes."

**▶ Al mostrar "La consecuencia fundamental"**
> "Señalo este texto: _el mismo input siempre produce el mismo output_."
> "No depende del reloj. No depende de qué corrió antes. No depende del estado de la máquina. Solo depende de los argumentos."
> "Eso es lo que hace que el funcional sea testeabley predecible."

💬 **Pregunta:** "¿Y cómo hace I/O entonces? Si nada puede cambiar el estado, ¿cómo imprimís por pantalla?"
- Respuesta: "Muy buena pregunta. El I/O es el borde del sistema funcional. El Tema 05 cubre las mónadas — que son exactamente la solución a ese problema. Por ahora: pensemos en la lógica pura, sin I/O."

**→ Transición:** "Los tres principios que hacen que esto funcione en la práctica."

---

## BLOQUE B — Los tres pilares (20 min)

### [F-13] Pilar 1: Funciones puras — definición

**Tiempo:** 3 min

**▶ Al mostrar la definición**
> "Pilar 1: funciones puras. Definición formal — dos condiciones que tienen que cumplirse al mismo tiempo."
Señalar cada punto:
> "Condición 1: la salida depende **únicamente** de la entrada. Si llamo `f(3)` hoy y `f(3)` mañana, obtengo el mismo resultado."
> "Condición 2: no produce **efectos colaterales** observables. No modifica variables externas, no hace I/O, no lanza excepciones con side effects."
> "Las dos condiciones juntas. Si falta una, la función no es pura."

**▶ Al recorrer la tabla "¿Por qué importa?"**
Señalar cada fila:

| Propiedad | Consecuencia |
|---|---|
| Predecible | Mismos args → mismo resultado — siempre |
| Testeable en aislamiento | No necesita setup/teardown de estado |
| Segura en paralelo | No compite por estado compartido |
| Razonable localmente | Solo hay que leer la función para entenderla |

> "Testeable en aislamiento: para testear `sumar(a, b)`, no necesito inicializar ningún objeto, conectarme a una DB, ni setear ningún estado previo. Solo llamo a la función con los argumentos y verifico el resultado."
> "Segura en paralelo: si dos threads llaman a la misma función pura con los mismos argumentos, no pueden interferirse — cada una trabaja con sus propias variables locales."

**→ Transición:** "Ahora vemos cómo se ve en código — TypeScript primero, Clojure después."

---

### [F-14] Pilar 1: Funciones puras — impura vs pura en TypeScript

**Tiempo:** 4 min

**▶ Al mostrar el bloque ❌ (función impura)**
```typescript
let contador = 0;

const incrementar = (): number => {
  contador++;          // ← efecto colateral: modifica estado externo
  return contador;    // ← resultado depende del estado externo
};

incrementar(); // → 1
incrementar(); // → 2   ← mismo llamado, distinto resultado
```
> "`incrementar` no recibe ningún argumento. ¿De dónde saca el valor? De `contador`, que vive afuera."
> Señalar `contador++`: "Esta línea modifica algo que existe fuera de la función. Eso es un efecto colateral."
> Señalar las dos llamadas: "La llamo dos veces, sin cambiar nada. La primera vez devuelve 1, la segunda devuelve 2. **Mismo llamado, distinto resultado**. Eso viola la condición 1 de función pura."
> "Para testear esto, necesito asegurarme que `contador` vale 0 antes del test. Si otro test corrió antes y modificó `contador`, el resultado va a ser diferente."

**▶ Al mostrar el bloque ✅ (función pura)**
```typescript
const sumar = (a: number, b: number): number => a + b;

sumar(3, 4); // → 7   — siempre 7, sin importar cuándo se llame
sumar(3, 4); // → 7   — predecible como una función matemática
```
> "Todo lo que `sumar` necesita está en sus argumentos. No lee nada de afuera."
> Señalar las dos llamadas: "Dos veces con los mismos argumentos — siempre el mismo resultado. Para testear esto: `expect(sumar(3, 4)).toBe(7)`. Sin setup, sin teardown."
> "Y si corro esta función en 100 threads simultáneos — no hay problema. No hay nada para coordinar."

💬 **Pregunta:** "¿Toda función tiene que ser pura?"
- Si dicen "sí": "En lenguajes puramente funcionales como Haskell o Clojure, sí. En multiparadigma como TypeScript, lo que hacemos es **empujar los efectos al borde** — el I/O, la DB, la interfaz son impuros; la lógica de negocio es pura."

**→ Transición:** "Para que una función sea pura, los datos que maneja no pueden cambiar. Segundo pilar: inmutabilidad."

---

### [F-15] Pilar 1: Funciones puras — en Clojure

**Tiempo:** 2 min

**▶ Al mostrar el bloque "función pura en Clojure"**
```clojure
(defn sumar [a b]
  (+ a b))

(sumar 3 4)  ; → 7
(sumar 3 4)  ; → 7 — siempre
```
> "En Clojure, la sintaxis es `(defn nombre [parámetros] cuerpo)`. No hay `return` — el cuerpo es la expresión y su valor es el resultado."
> "Noten que la función `sumar` se llama exactamente igual que en TypeScript — misma idea, sintaxis distinta."

**▶ Al mostrar el bloque "cuadrado-de-par?"**
```clojure
(defn cuadrado-de-par? [n]
  (if (even? n)
    (* n n)
    nil))

(cuadrado-de-par? 4)   ; → 16
(cuadrado-de-par? 3)   ; → nil
```
> "El `if` en Clojure es una **expresión** — siempre devuelve un valor. No hay `if` que no devuelva nada."
> "No hay `return` — el resultado del `if` es el resultado de la función."

**▶ Al mostrar "Por qué Clojure facilita la pureza"**
> "Punto clave: `def` en Clojure crea una ligadura nueva — no modifica la anterior. No existe el concepto de reasignación de variable."
> "Las estructuras de datos no tienen métodos mutadores. Si querés 'modificar' una lista, el lenguaje te da una lista nueva."

**→ Transición:** "Segundo pilar: inmutabilidad. Veamos TypeScript primero."

---

### [F-16] Pilar 2: Inmutabilidad — TypeScript

**Tiempo:** 4 min

**▶ Al mostrar el primer bloque — `const` básico**
```typescript
const x = 10;
// x = 20;  // ❌ Error de compilación

const numeros = [1, 2, 3];
// numeros = [4, 5, 6];  // ❌ Error: la referencia no puede cambiar
```
> "`const` impide reasignar la **referencia** — la variable no puede apuntar a otro valor. Pero no impide modificar el contenido."

**▶ Al mostrar el bloque ⚠️ (trampa de `const`)**
```typescript
const numeros = [1, 2, 3];
numeros.push(4);  // ✅ Compila — pero es mutación oculta
console.log(numeros); // [1, 2, 3, 4]
```
> "Acá está la trampa. Esto **compila sin error**. `const` protege la variable de ser reasignada, pero no protege el contenido del array."
> "`numeros.push(4)` modifica el array en su lugar. Si otra parte del código tenía una referencia a ese mismo array, ahora ve un array diferente sin haberlo pedido."
> "Eso es estado mutable oculto — y es exactamente lo que queremos evitar."

**▶ Al mostrar el bloque ✅ (estilo funcional con spread)**
```typescript
const numeros = [1, 2, 3] as const;  // readonly array
const masNumeros = [...numeros, 4];   // nuevo array

console.log(numeros);     // [1, 2, 3]   — intacto
console.log(masNumeros);  // [1, 2, 3, 4]
```
> "El spread `[...numeros, 4]` no toca `numeros`. Crea un array nuevo con todos los elementos de `numeros` más el `4`."
> "`as const` le dice a TypeScript que el array es `readonly` — el compilador va a rechazar cualquier intento de mutarlo."
> "Ahora tenemos dos arrays: el original intacto y el nuevo. Cualquier función que tenía referencia al original sigue viendo `[1, 2, 3]`."

💬 **Pregunta:** "¿No es más lento crear nuevos arrays en cada operación?"
- Respuesta: "En la mayoría de los casos, no — los engines de JavaScript modernos están muy optimizados para esto. Y lo importante: el costo de un bug por estado mutable en producción es casi siempre mucho más caro que el overhead de memoria."

**→ Transición:** "En Clojure, esto no es opt-in — es el único modo posible."

---

### [F-17] Pilar 2: Inmutabilidad nativa en Clojure

**Tiempo:** 3 min

**▶ Al mostrar el bloque principal**
```clojure
(def numeros '(1 2 3))

(def mas-numeros (conj numeros 4))

(println numeros)       ; → (1 2 3)     ← intacta, siempre
(println mas-numeros)   ; → (4 1 2 3)   ← nueva lista
```
> "`conj` agrega un elemento a una colección. En Clojure, esto **siempre devuelve una colección nueva**. No existe la opción de modificar la original."
> Señalar el `println numeros`: "Después de `conj`, `numeros` sigue siendo `(1 2 3)`. Porque es imposible que cambie."
> "En TypeScript tuvimos que escribir `as const` y disciplinarnos para no usar `push`. En Clojure no hay esa opción — el lenguaje garantiza que no existe."

**▶ Al mostrar "Structural sharing"**
> "Podrían pensar: si cada operación crea una estructura nueva, ¿no es carísimo en memoria?"
> "La respuesta es Structural Sharing — las estructuras persistentes de Clojure comparten nodos internos entre versiones. `mas-numeros` no copia los `1, 2, 3` — solo agrega un puntero al nodo nuevo. La versión anterior se comparte."
> "Es eficiente **y** seguro en múltiples threads — ningún thread puede ver un estado intermedio de una estructura que otro está construyendo."

**▶ Al mostrar la tabla comparativa final**
| | TypeScript | Clojure |
|---|---|---|
| Inmutabilidad | Opt-in (`as const`, `readonly`) | **Nativa — siempre** |
| Quién la garantiza | El programador (disciplina) | El lenguaje (diseño) |

> "Esta distinción entre disciplina y diseño va a ser central cuando lleguemos al Bloque D."

💬 **Pregunta:** "¿Cómo 'cambia' el estado de una aplicación Clojure si nada puede mutar?"
- Respuesta: "El estado nuevo se pasa como argumento a la siguiente función. En vez de modificar una variable, creás una versión nueva del estado y la pasás a la siguiente llamada. Eso se llama _estado como valor_ — el Tema 04 lo profundiza."

**→ Transición:** "Tercer pilar — transparencia referencial. Es la consecuencia de los dos anteriores."

---

### [F-18] Pilar 3: Transparencia referencial

**Tiempo:** 4 min

**▶ Al mostrar la definición**
> "Transparencia referencial: una expresión tiene esta propiedad si puede ser **reemplazada por su valor** sin cambiar el comportamiento del programa."
> "Esto es exactamente lo que hicimos en la β-reducción. Reemplazamos `suma(1,2)` por `3` y el programa siguió siendo correcto."
> "Si una función es pura y los datos son inmutables — los dos pilares anteriores — entonces sus expresiones son automáticamente referencialmente transparentes."

**▶ Al mostrar el ejemplo ✅ (transparente)**
```typescript
const cuadrado = (n: number): number => n * n;

const a = cuadrado(3) + cuadrado(3);  // → 18
const b = 9 + 9;                       // → 18 — equivalente
```
> "Puedo reemplazar `cuadrado(3)` por `9` en cualquier parte del código y el resultado es idéntico."
> "`cuadrado` cumple los dos pilares: solo usa `n` (función pura) y no modifica nada (sin side effects)."

**▶ Al mostrar los contraejemplos ❌**
```typescript
Date.now()    // ← distinto valor cada vez
Math.random() // ← distinto valor cada vez
console.log() // ← efecto colateral (I/O)
```
> "Si reemplazo `Date.now()` por el valor que devolvió la primera vez — el programa se comporta diferente. La segunda llamada debería dar otro timestamp."
> "`Date.now()` no es referencialmente transparente. Tampoco `Math.random()`. Tampoco `console.log()` — tiene un efecto colateral observable."
> "Estas funciones no son puras. Son el borde del sistema funcional."

**▶ Al mostrar "¿Por qué importa?"**
> Leer cada punto:
- **Memoización automática**: "El compilador puede cachear el resultado de `cuadrado(3)`. Si ya lo calculó una vez, lo guarda y lo reutiliza."
- **Evaluación lazy**: "Puede postergar el cálculo hasta que el valor realmente se necesite."
- **Razonar localmente**: "Para entender una expresión, solo necesito leer esa expresión — no el historial de estados del programa."

💬 **Pregunta:** "¿Y si necesito la hora actual? ¿Tengo que abandonar el funcional?"
- Respuesta: "No — lo que hacés es manejar el efecto en el borde del sistema. La lógica de negocio es pura; el efecto de pedir `Date.now()` ocurre en la capa I/O. El Tema 05 — mónadas — es exactamente la solución formal a este problema."

**→ Transición:** "Tres pilares completos. Ahora vamos a programar en TypeScript con estos principios aplicados explícitamente."

---

## BLOQUE C — TypeScript en modo funcional (25 min)

### [F-19] Las reglas del modo funcional en TypeScript

**Tiempo:** 2 min

**▶ Al mostrar la tabla de restricciones**
> "Vamos a establecer un contrato para el Bloque C. TypeScript no nos obliga a esto — lo elegimos nosotros para entender el paradigma."
Señalar cada fila y justificar:

| Restricción | Por qué |
|---|---|
| Sin `let` ni `var` | Una variable reasignable rompe la trazabilidad |
| Sin `for` / `while` | Mezcla cómo iterar con qué hacer |
| Sin `push`, `splice`, mutación | El array cambia y afecta código que no lo esperaba |
| Sin `class` con estado mutable | Estado encapsulado oculto |
| Solo `const` + arrow functions | Las funciones son valores |

> "Estas no son reglas arbitrarias. Cada una es consecuencia directa de uno de los tres pilares."
> "Cuando lleguemos a Clojure, van a ver que ahí el lenguaje las impone — acá las imponemos nosotros."

**▶ Al mostrar la nota importante**
> "Leer en voz alta: _La disciplina autoimpuesta enseña más que la disciplina del compilador, porque obliga a entender el porqué._"

**→ Transición:** "Primera herramienta: `map`."

---

### [F-20] `map` — el problema (código imperativo)

**Tiempo:** 2 min

**▶ Al mostrar el código ❌**
```typescript
const numeros = [1, 2, 3, 4, 5];
const dobles: number[] = [];          // ← acumulador mutable externo

for (const n of numeros) {            // ← loop: detalle de cómo iterar
  dobles.push(n * 2);                 // ← mutación del acumulador
}
// dobles = [2, 4, 6, 8, 10]
```
> "El problema que quiero resolver: transformar cada número de la lista en su doble."
> Señalar `const dobles: number[] = []`: "Acumulador vacío al inicio — ya estamos creando estado mutable."
> Señalar el `for`: "El loop dice cómo recorrer el array. No dice qué quiero hacer."
> Señalar `dobles.push(n * 2)`: "Mutación en cada vuelta. Si el loop es largo, `dobles` va cambiando en cada paso."

**▶ Al mostrar los tres problemas listados**
> "Tres problemas: acumulador mutable externo que puede ser tocado desde afuera; mezcla de iteración y lógica; hay que simular el loop mentalmente para entender qué produce."
> "Pregunta: ¿qué quiero hacer? Transformar cada elemento. ¿Qué describe este código? Cómo iterar."

**→ Transición:** "La solución funcional."

---

### [F-21] `map` — la solución funcional

**Tiempo:** 3 min

**▶ Al mostrar el código ✅**
```typescript
const numeros = [1, 2, 3, 4, 5];

const dobles = numeros.map(n => n * 2);
// → [2, 4, 6, 8, 10]

console.log(numeros); // [1, 2, 3, 4, 5]  ← intacto
```
> "`map` toma el array y una función. Por cada elemento, aplica la función y pone el resultado en un nuevo array."
> Señalar `n => n * 2`: "Esta es la función pura que pasan como argumento. Solo toma `n` y devuelve `n * 2`. Sin efectos colaterales. Sin leer nada de afuera."
> Señalar el `console.log(numeros)`: "El array original `numeros` no cambió. `map` nunca modifica el array original."
> "`map` es una función de **orden superior** — recibe una función como argumento. Eso es posible porque en el paradigma funcional las funciones son valores como cualquier número o string."

**▶ Al mostrar la sección "Por qué `map` y no `for`"**
> "`map` dice el **QUÉ**: transformar cada elemento aplicando esta función. La iteración es un detalle de implementación — `map` la abstrae."
> "Comparar mentalmente con el código anterior: el `for` tenía que decir — inicializar index, verificar condición, incrementar. Nada de eso tiene que ver con 'calcular dobles'."

💬 **Pregunta:** "¿Qué devuelve `map` si el array original tiene 5 elementos?"
- Respuesta: "Siempre un array nuevo con exactamente el mismo número de elementos — la función se aplicó a cada uno."

**→ Transición:** "¿Qué pasa cuando quiero quedarme solo con algunos elementos?"

---

### [F-22] `filter` — seleccionar sin mutar

**Tiempo:** 4 min

**▶ Al mostrar el código ✅ básico**
```typescript
const numeros = [1, 2, 3, 4, 5, 6];

const pares = numeros.filter(n => n % 2 === 0);
// → [2, 4, 6]

console.log(numeros); // [1, 2, 3, 4, 5, 6]  ← intacto
```
> "`filter` toma un **predicado** — una función que devuelve `true` o `false`. Por cada elemento, si el predicado devuelve `true`, lo incluye en el nuevo array."
> Señalar `n => n % 2 === 0`: "Este predicado es puro. Solo recibe `n` y devuelve si es par."
> "`filter` puede devolver un array más corto que el original — a diferencia de `map` que siempre devuelve uno del mismo tamaño."

**▶ Al mostrar el bloque "El predicado es una función pura"**
> "Notar que `n => n % 2 === 0` es una arrow function — una lambda — pasada como argumento. Segundo caso de función de orden superior."
> "El predicado podría ser cualquier función que devuelva `boolean`. Lo que importe es que sea pura."

**▶ Al mostrar el bloque "Encadenamiento: filter + map"**
```typescript
const cuadradosDePares = [1, 2, 3, 4, 5, 6]
  .filter(n => n % 2 === 0)   // [2, 4, 6]
  .map(n => n * n);            // [4, 16, 36]
```
> "Este es el encadenamiento funcional. El resultado de `filter` entra directo a `map`."
> "Sin variables intermedias. Sin estado. Sin acumuladores."
> "Y van a reconocer este código — es exactamente la primera parte del ejemplo del Bloque A donde calculamos `suma` de cuadrados de pares."

💬 **Pregunta:** "Si la lista original tiene 6 elementos y el predicado acepta 3, ¿cuántos elementos tiene el resultado?"
- Respuesta: "3."
> "Y si luego encadeno `map`, ¿cuántos?"
- Respuesta: "Sigue siendo 3 — `map` no filtra, transforma."

**→ Transición:** "¿Cómo acumulo valores sin un acumulador mutable externo?"

---

### [F-23] `reduce` — el problema (código imperativo)

**Tiempo:** 2 min

**▶ Al mostrar el código ❌**
```typescript
const numeros = [1, 2, 3, 4];
let suma = 0;                        // ← acumulador externo mutable

for (const n of numeros) {
  suma += n;                         // ← mutación en cada iteración
}
// suma = 10
```
> "`suma` vive **afuera** del loop. Antes de que empiece: `suma = 0`. Durante: cambia en cada vuelta. Después del loop: `suma = 10`. Pero el loop y la variable `suma` son accesibles desde el mismo scope."

**▶ Al mostrar "El problema: state leakage"**
> "Tres problemas señalados en la filmina:"
> - "Primero: `suma` existe antes y después del loop — puede ser leída o modificada desde afuera."
> - "Segundo: si el loop está en una función larga, `suma` 'contamina' el scope local — hace el código más difícil de razonar."
> - "Tercero: para paralelizar este loop, necesitaría un mutex o lock para proteger `suma` de condiciones de carrera."

**→ Transición:** "En `reduce`, el acumulador viaja adentro."

---

### [F-24] `reduce` — la solución funcional

**Tiempo:** 4 min

**▶ Al mostrar el código ✅**
```typescript
const numeros = [1, 2, 3, 4];

const suma = numeros.reduce(
  (acc, n) => acc + n,  // función: acumulador actual + elemento → nuevo acumulador
  0                      // valor inicial del acumulador
);
// suma = 10
```
> "`reduce` toma dos cosas: la función acumuladora y el valor inicial."
> Señalar `(acc, n) => acc + n`: "Esta función recibe el acumulador actual `acc` y el elemento actual `n`, y devuelve el nuevo acumulador."
> Señalar el `0`: "El acumulador empieza en `0`. En la primera vuelta: `acc=0`, `n=1`, devuelve `1`. Segunda vuelta: `acc=1`, `n=2`, devuelve `3`. Y así."
> "El acumulador solo vive **dentro de `reduce`**. Nadie puede tocarlo desde afuera. Cuando `reduce` termina, ya no existe — su resultado está en `suma`."

**▶ Al mostrar "Por qué `reduce` resuelve el problema"**
> "Tres puntos clave:"
> - "El acumulador solo existe dentro de `reduce` — no hay state leakage."
> - "Se pasa como argumento explícito en cada llamada — el estado es visible en la firma de la función."
> - "Es paralizable: `reduce` puede dividir el array y combinar parciales."

**▶ Al mostrar "`reduce` es el más general"**
> "Este es el punto más interesante: `map` y `filter` son casos especiales de `reduce`."
> "La operación de `map` es: `reduce` donde el acumulador es un array y en cada paso agrego el elemento transformado."
> "En Haskell y ML, `reduce` se llama `fold`. 'Doblar' una colección en un valor."
> "El nombre `fold` viene del λ-cálculo — literalmente 'plegamos' la lista."

💬 **Pregunta:** "¿Por qué se llama `reduce`?"
- Respuesta: "Porque reduce una colección a un único valor. Array de N elementos → un solo valor."

**→ Transición:** "¿Cómo componemos `filter`, `map` y `reduce` en un pipeline reutilizable?"

---

### [F-25] Composición de funciones — `pipe`

**Tiempo:** 5 min

**▶ Al mostrar el bloque "Encadenamiento directo"**
```typescript
const resultado = [1, -2, 3, -4, 5]
  .filter(n => n > 0)   // [1, 3, 5]
  .map(n => n * 2);      // [2, 6, 10]
```
> "El encadenamiento que vimos es una forma de composición. El resultado de un paso entra al siguiente. Sin variables."
> "Pero el encadenamiento con `.` solo funciona para arrays y depende de que los métodos estén en el array. Si quiero componer funciones arbitrarias, necesito algo más general."

**▶ Al mostrar la implementación de `pipe`**
```typescript
const pipe = <T>(...fns: Array<(x: T) => T>) =>
  (valor: T): T =>
    fns.reduce((v, fn) => fn(v), valor);
    // ← pipe usa reduce internamente
```
> "Esta es la implementación de `pipe`. Recibe cualquier cantidad de funciones y devuelve una función que las aplica en secuencia."
> Señalar `fns.reduce((v, fn) => fn(v), valor)`: "El acumulador es el valor actual. En cada paso, aplica la siguiente función al valor actual. Eso es `reduce` sobre una lista de funciones."
> "Los pilares se componen entre sí: `pipe` usa `reduce` para componer funciones."

**▶ Al mostrar el uso de `pipe`**
```typescript
const procesarPositivos = pipe(
  (nums: number[]) => nums.filter(n => n > 0),
  (nums: number[]) => nums.map(n => n * 2),
  (nums: number[]) => nums.filter(n => n < 8),
);

procesarPositivos([1, -2, 3, -4, 5]);  // → [2, 6]
procesarPositivos([-1, 4, 2, -3]);     // → [4] (reutilizable)
```
> "`procesarPositivos` es una función — es un **valor**. La defino una vez y la reutilizo con distintos inputs."
> "Señalar que se llama dos veces con distintas listas — el pipeline es reutilizable."
> "Cada función del pipeline es pura y testeable por separado."

**▶ Al mostrar "Por qué `pipe` importa"**
> "Este es el patrón central del funcional industrial: construir transformaciones complejas desde piezas pequeñas y puras."
> "Cada pieza: testeable en aislamiento. La combinación: predecible y legible."

💬 **Pregunta:** "¿Es lo mismo que el encadenamiento con punto?"
- Respuesta: "Similar, pero `pipe` es más general. Funciona con cualquier función, no solo métodos de array. Y el pipeline resultante es una función — un valor que podés pasar como argumento a otra función."

**→ Transición:** "Antes de Clojure, conectemos todo."

---

### [F-26] Por qué las restricciones existen — resumen

**Tiempo:** 3 min

**▶ Al mostrar la tabla completa**
Señalar cada fila y leer la columna "Sin esta restricción…":

| Restricción | Pilar que protege | Sin esta restricción… |
|---|---|---|
| Sin `let` / `var` | Inmutabilidad | Variables reasignables = estado mutable oculto |
| Sin `for` / `while` | Funciones puras + abstracción | Loop mezcla iteración con lógica |
| Sin `push` / mutación | Inmutabilidad | Efectos en colecciones se propagan impredeciblemente |
| Sin `class` con estado | Funciones puras | El estado encapsulado rompe la transparencia referencial |
| Solo `const` | Transparencia referencial | Si un nombre cambia de valor, no es transparente |

> "Cada restricción protege uno de los tres pilares. No son reglas de estilo — son consecuencias."
> "Sin `let`: si la variable puede cambiar, no puedo saber su valor solo de leer la línea donde se define."
> "Sin `push`: si el array puede cambiar en cualquier momento, ninguna función puede asumir que el array que recibió va a seguir siendo el mismo."

**▶ Al mostrar "En TypeScript: disciplina elegida"**
> "En TypeScript, `eslint` con las reglas correctas puede ayudar a verificar algunas de estas restricciones. Pero no todas."

**▶ Al mostrar "En Clojure: garantizadas por el lenguaje"**
> "En Clojure el compilador y el runtime hacen que las tres primeras sean **imposibles de violar**. No es disciplina — es una propiedad del sistema."
> "Eso es lo que vamos a ver en el próximo bloque."

**→ Transición:** "Ahora veamos qué pasa cuando el lenguaje hace el trabajo por vos."

---

## BLOQUE D — Clojure: el funcional puro (20 min)

### [F-27] Contexto de Clojure

**Tiempo:** 3 min

**▶ Al mostrar la tabla de propiedades de diseño**
> "Clojure, 2007. Rich Hickey estaba harto de los bugs de concurrencia en sistemas Java."
> "Diseñó un lenguaje donde esos bugs son **imposibles por diseño**. No más difíciles — imposibles."
> "Nubank, el banco digital más grande de Latinoamérica, corre en Clojure. Datomic, el motor de base de datos con historia inmutable, está escrito en Clojure."

Recorrer la tabla de propiedades:
| Propiedad | Descripción |
|---|---|
| Inmutabilidad estructural | Todas las estructuras son persistentes e inmutables por defecto |
| Todo es expresión | No hay sentencias — todo tiene un valor |
| Funciones como valores | No hay diferencia entre función y dato |
| Sintaxis Lisp | `(función arg1 arg2)` — el λ-cálculo directamente |
| Concurrencia segura | Las referencias mutables son explícitas y coordinadas |

> "La propiedad 'Todo es expresión' es importante: no hay `if` que no devuelva un valor. No hay `for` que no devuelva nada. Todo el código es una expresión que se evalúa."

**→ Transición:** "La sintaxis va a ser diferente a todo lo que vieron. Cinco minutos de adaptación y después es muy legible."

---

### [F-28] Sintaxis básica de Clojure

**Tiempo:** 4 min

**▶ Al mostrar el bloque "Aritmética y definición"**
```clojure
(+ 1 2)    ; → 3
(* 3 4)    ; → 12
(def x 5)  ; define una constante
```
> "La regla es una sola: `(función arg1 arg2 ...)`. El operador o función va **primero**, siempre."
> "En TypeScript escribimos `1 + 2`. En Clojure: `(+ 1 2)`. El `+` va adelante."
> "Al principio incomoda. Pero tiene una ventaja: hay **una sola forma** de escribir cualquier cosa. En TypeScript podés llamar a una función como `f(x)`, como método `obj.f()`, con template strings, con `new`. En Clojure: siempre `(f arg)`."

**▶ Al mostrar el bloque "Listas de datos"**
```clojure
'(1 2 3 4 5)     ; lista de datos — el apóstrofe evita la evaluación

(first '(1 2 3)) ; → 1
(rest  '(1 2 3)) ; → (2 3)
(count '(1 2 3)) ; → 3
```
> "El apóstrofe antes de la lista le dice a Clojure: no evalúes esto como código — es dato."
> "Sin el apóstrofe, `(1 2 3)` se interpretaría como 'llamar a la función `1` con argumentos `2` y `3`' — que falla."

**▶ Al mostrar el bloque "Definición de funciones"**
```clojure
(defn cuadrado [x]   ; defn: nombre + vector de parámetros + cuerpo
  (* x x))

(cuadrado 5)  ; → 25
```
> "`defn` es la forma de definir funciones con nombre. El vector `[x]` son los parámetros."
> "No hay `return` — el cuerpo de la función **es** la expresión, y su valor es el resultado automáticamente."

💬 **Pregunta:** "¿Los paréntesis no se vuelven confusos cuando hay muchos anidados?"
- Respuesta: "Al principio sí. Los editores modernos (VS Code, IntelliJ) los colorean por nivel de anidamiento. Con algunas horas de práctica la mente los parsea automáticamente."

**→ Transición:** "Las funciones que ya conocen — `map`, `filter`, `reduce` — en Clojure."

---

### [F-29] `map`, `filter`, `reduce` en Clojure

**Tiempo:** 5 min

**▶ Al mostrar el bloque `map`**
```clojure
(map #(* % 2) '(1 2 3 4 5))
;; → (2 4 6 8 10)
;;   El original '(1 2 3 4 5) no cambia — nunca puede cambiar
```
> "Misma idea que en TypeScript — `map` aplica una función a cada elemento."
> Señalar `#(* % 2)`: "Esta es una función anónima abreviada. El `%` es el argumento — equivale a `(fn [x] (* x 2))`."
> "Comparar con TypeScript: `nums.map(n => n * 2)`. La diferencia es solo sintáctica."
> "El comentario dice 'el original no cambia'. No porque nos disciplinemos — porque es **imposible**."

**▶ Al mostrar el bloque `filter`**
```clojure
(filter even? '(1 2 3 4 5 6))
;; → (2 4 6)
;;   even? es una función pura predefinida: (even? 4) → true
```
> "`even?` es una función normal en Clojure — no es un operador especial. Cualquier función que devuelva `boolean` puede ser predicado de `filter`."
> "El signo de pregunta `?` es parte del nombre — convención de Clojure para funciones que devuelven booleano `(predicate? x)`."

**▶ Al mostrar el bloque `reduce`**
```clojure
(reduce + 0 '(1 2 3 4))
;; → 10
;;   + es una función normal que se pasa como argumento
;;   0 es el valor inicial del acumulador
```
> "Acá está la diferencia más importante con TypeScript: el `+` es una función como cualquier otra."
> "En TypeScript, `+` es un operador del lenguaje — no lo podés pasar como argumento a otra función. En Clojure, `+` es simplemente `(defn + [a b] ...)` — es un dato, es un valor, es pasable."

**▶ Al mostrar el pipeline con `->>` macro**
```clojure
(->> '(1 2 3 4 5 6)
     (filter even?)        ; → (2 4 6)
     (map #(* % %))        ; → (4 16 36)
     (reduce + 0))          ; → 56
```
> "La macro `->>` es el equivalente al encadenamiento con `.` de TypeScript."
> "Lee de arriba a abajo: empieza con la lista, filtra pares, eleva al cuadrado, suma."
> "El resultado es `56` — exacto al ejemplo del Bloque A."

💬 **Pregunta:** "¿`even?` es una función normal que puedo escribir yo?"
- Respuesta: "Sí. `(defn par? [n] (= (mod n 2) 0))` — y la podés pasar a `filter` igual que `even?`."

**→ Transición:** "Las funciones anónimas — `fn` y la notación `#()`."

---

### [F-30] Funciones anónimas en Clojure — `fn`

**Tiempo:** 3 min

**▶ Al mostrar la forma completa con `fn`**
```clojure
(fn [x] (* x x))          ; función anónima: eleva al cuadrado

;; Aplicación inmediata:
((fn [x y] (+ x y)) 3 4)  ; → 7
;; equivale a: (λx.λy. x+y) 3 4 → 7
```
> "`fn` define una función sin nombre. Los parámetros entre corchetes, el cuerpo a continuación."
> Señalar la aplicación inmediata: "Puedo definif una función y aplicarla en el mismo lugar. Los paréntesis externos significan 'evaluar esto como función con estos argumentos'."
> "El comentario lo dice explícitamente: esto es el λ-cálculo escrito en sintaxis Lisp."

**▶ Al mostrar la forma abreviada `#()`**
```clojure
#(* % 2)      ; equivale a (fn [x] (* x 2)) — % es el único argumento
#(+ %1 %2)    ; dos argumentos: %1 y %2
#(* % %)      ; cuadrado: % multiplicado por sí mismo
```
> "Para funciones cortas, la notación `#()` es más compacta. El `%` es el primer argumento, `%2` el segundo."
> "Pero `fn` es más legible para funciones de más de una línea."

**▶ Al mostrar "Funciones como valores de primera clase"**
```clojure
;; Una función puede retornar una función
(defn multiplicador [factor]
  (fn [x] (* x factor)))    ; devuelve una función

((multiplicador 3) 7)  ; → 21
```
> "Este es currying manual. `multiplicador` recibe un `factor` y devuelve una función que multiplica por ese factor."
> "Llamar `(multiplicador 3)` devuelve la función `(fn [x] (* x 3))`. Luego la aplico con `7` → `21`."
> "En TypeScript sería: `const multiplicador = (factor: number) => (x: number) => x * factor`. Mismo concepto, sintaxis diferente."

💬 **Pregunta:** "¿Puedo guardar una función en una variable en Clojure?"
- Respuesta: "Sí: `(def doble (fn [x] (* x 2)))`. Después `(doble 5)` → `10`. Las funciones son valores — se guardan igual que números o strings."

**→ Transición:** "Ya tenemos los dos lenguajes. La comparativa final."

---

### [F-31] Comparativa completa TypeScript ↔ Clojure

**Tiempo:** 3 min

**▶ Al mostrar la tabla**
> "Vamos a recorrer fila por fila. Les pido que lean alternadamente — un estudiante lee la columna TypeScript, el siguiente lee Clojure."

Recorrer cada conceptofila con la clase:

| Concepto | TypeScript | Clojure |
|---|---|---|
| Valor inmutable | `const x = 5` | `(def x 5)` |
| Función pura con nombre | `const f = (x: number) => x * 2` | `(defn f [x] (* x 2))` |
| Función anónima | `(x) => x * 2` | `(fn [x] (* x 2))` o `#(* % 2)` |
| Aplicación inmediata | `((x) => x * 2)(5)` | `((fn [x] (* x 2)) 5)` |
| Map | `arr.map(fn)` | `(map fn coll)` |
| Filter | `arr.filter(pred)` | `(filter pred coll)` |
| Reduce | `arr.reduce(fn, init)` | `(reduce fn init coll)` |
| Pipeline | `.filter().map()` o `pipe()` | `(->> coll (filter) (map))` |
| **Inmutabilidad de colecciones** | **Opt-in** (`as const`) | **Nativa — siempre** |
| **Garantía de pureza** | **Disciplina del programador** | **Diseño del lenguaje** |

> "Las últimas dos filas son las más importantes. Señalarlas."
> "Inmutabilidad: en TypeScript es opt-in. En Clojure es nativa — no hay opción de mutación."
> "Garantía de pureza: en TypeScript elegimos ser funcionales. En Clojure el lenguaje nos obliga."

**→ Transición:** "¿Qué diferencia práctica hace eso?"

---

### [F-32] La diferencia que importa: disciplina vs garantía

**Tiempo:** 2 min

**▶ Al mostrar el bloque TypeScript ❌-posible**
```typescript
const numeros = [1, 2, 3];
numeros.push(4);  // ← el compilador lo permite aunque lo "prohibimos"
                   // la inmutabilidad es una convención del equipo
```
> "Este código compila. No hay error. La restricción 'sin `push`' que declaramos al principio del Bloque C es una convención — no la hace cumplir el compilador."
> "Si alguien en el equipo no conoce la convención, o la olvida bajo presión, la violación no se detecta hasta que falla en producción."

**▶ Al mostrar el bloque Clojure**
```clojure
(def numeros '(1 2 3))
;; No existe ninguna operación para mutar 'numeros en su lugar
;; conj, cons, rest → todas crean nuevas colecciones
```
> "En Clojure no hay un `push`. No existe. No es que está desaconsejado — simplemente no existe en el API."
> "Es imposible violar la inmutabilidad — no porque el programador sea disciplinado, sino porque el diseño del lenguaje no da esa herramienta."

**▶ Al mostrar "La consecuencia"**
> "Cuando el código Clojure compila y corre, tenés una garantía formal: ninguna función modificó una estructura compartida. No es fe en el equipo — es una propiedad del sistema."
> Leer la nota final: _"En TypeScript, confías en la disciplina del equipo. En Clojure, confías en el diseño del lenguaje."_

💬 **Pregunta rápida:** "¿Para qué dominio elegirían Clojure sobre TypeScript?"
- Respuesta esperada: sistemas financieros, críticos, alta concurrencia, donde la correctitud es no negociable.

**→ Transición:** "Síntesis y cierre."

---

## BLOQUE E — Integración y cierre (15 min)

### [F-33] Línea de tiempo — síntesis visual

**Tiempo:** 3 min

**▶ Al mostrar la tabla**
> "Recorrida rápida como síntesis — ya conocen todos estos puntos, ahora los vemos como historia continua."
Señalar con el cursor cada hito y dar una frase por fila:

| Año | Hito |
|---|---|
| 1936 | "Church y Turing — dos modelos, misma respuesta a Hilbert" |
| 1958 | "Lisp — el λ-cálculo se convierte en lenguaje" |
| 1973–75 | "ML y Scheme — inferencia de tipos y educación" |
| 1985–86 | "Miranda y Erlang — concurrencia por actores" |
| 1990 | "Haskell — primer funcional puro de referencia" |
| 2003–05 | "Scala, F# — Big Data y .NET" |
| 2007 | "Clojure — funcional puro moderno, blockchain" |
| 2011–15 | "Kotlin, Rust, ES6, Java 8 — funcional en todos los multiparadigma" |
| 2015+ | "TypeScript funcional — el paradigma en el ecosistema web" |

> Señalar la tabla completa: "90 años desde Church y Turing hasta TypeScript funcional que usamos hoy."

💬 **Pregunta para reflexión (no esperar respuesta):**
> "¿Qué va a aparecer en la fila 2030 o 2035 de esta tabla? ¿Qué problema industrial aún no resuelto va a necesitar un nuevo paradigma?"

**→ Transición:** "El debate de la clase."

---

### [F-34] Pregunta de debate

**Tiempo:** 8 min

**▶ Al mostrar la pregunta en la filmina**
> Leer en voz alta:
> _"Si TypeScript permite el estilo funcional pero no lo obliga, ¿tiene sentido aprender Clojure o Haskell? ¿O alcanza con disciplina y convenciones en TypeScript?"_
> "Tómense un minuto para pensar la respuesta. Después abrimos el debate."
> (Esperar 60 segundos en silencio — dejar que piensen)

**▶ Arrancar el debate — señalar los ejes**
> "Los cuatro ejes de la filmina:"

**Eje 1 — Escala del equipo:**
> "La disciplina individual no escala. 5 personas en un proyecto pueden acordar 'sin push'. ¿50? ¿Nuevo integrante que aprendió TypeScript con `push`? ¿Alguien bajo presión de fecha límite? La garantía del lenguaje vale más que la convención del equipo cuando la escala crece."

**Eje 2 — Dominio de aplicación:**
> "El sistema de trading de un banco. Un error de concurrencia puede costar millones o perder datos de clientes. ¿Confían en la disciplina del equipo? ¿O prefieren la garantía del compilador?"
> "Una landing page de marketing con TypeScript — ¿vale la pena la fricción de Clojure?"

**Eje 3 — Profundidad de comprensión:**
> "Usar `map` en TypeScript sin entender por qué no usar `for` es mecánico. Programar una semana en Haskell o Clojure donde el compilador rechaza cada intento de mutación fuerza a entender el paradigma a nivel visceral."
> "Después de eso, cuando volvés a TypeScript, lo usás mejor."

**Eje 4 — Interoperabilidad:**
> "TypeScript tiene acceso al ecosistema npm — millones de paquetes. Clojure tiene la JVM — todas las librerías Java. Rust tiene WASM y sistemas de tiempo real. La elección también depende del ecosistema."

**▶ Cerrar el debate**
> "No hay respuesta única. La pregunta 'Clojure vs TypeScript' tiene una respuesta que empieza con 'depende del'."
> "Lo importante: entender los dos les da la capacidad de elegir correctamente para cada problema."

💬 **Si surge la pregunta "¿Cuándo uso Clojure?"**
- Respuesta: "Concurrencia masiva, integridad del dato como requerimiento crítico, sistemas distribuidos con alta frecuencia de escrituras concurrentes. Nubank no eligió Clojure por moda."

**→ Transición:** "Cierre."

---

### [F-35] Cierre — síntesis y próximas clases

**Tiempo:** 4 min

**▶ Al mostrar "Los tres hilos que conectan toda la clase"**
> "Tres ideas que conectan los 120 minutos de hoy."

Señalar cada punto y ampliar una frase:
1. **El origen**: "Church y Turing, 1936. La misma respuesta al mismo problema por caminos opuestos. Imperativo: computa modificando estado. Funcional: computa reduciendo expresiones."
2. **Los tres pilares**: "Funciones puras + inmutabilidad + transparencia referencial. No son reglas de estilo — son consecuencias del modelo de Church. Juntos hacen el código predecible, testeable y paralelizable."
3. **De la teoría al código**: "TypeScript nos deja elegir ser funcionales. Clojure nos obliga. La diferencia es disciplina vs diseño del lenguaje."

**▶ Al mostrar la tabla "Próximas clases"**
| Tema | Contenido |
|---|---|
| **Tema 04** | Aspectos avanzados: currying, aplicación parcial, tipos algebraicos, pattern matching |
| **Tema 05** | Mónadas — cómo manejar `null`, errores e I/O sin romper los tres pilares |

> "Tema 04 va a profundizar en TypeScript funcional — currying, composición avanzada, tipos algebraicos."
> "Tema 05 resuelve la pregunta que quedó abierta: '¿cómo hace I/O el paradigma funcional sin romper los pilares?' La respuesta son las mónadas."

**▶ Al mostrar la sección TP**
> "El trabajo práctico del tema va a salir en la próxima clase — tipo y fecha de entrega los confirmo entonces. Vayan practicando `map`, `filter`, `reduce` sin `for` ni `push`."

**Al cerrar la filmina:**
> "Gracias. Preguntas."

---

## Resumen ejecutivo (últimas líneas antes de salir)

> Si se termina la clase y hay que resumir en 30 segundos:
> "(1) Church y Turing, 1936: dos modelos equivalentes, dos filosofías opuestas — imperativo y funcional.
> (2) Tres pilares: funciones puras, inmutabilidad, transparencia referencial — código predecible, testeable, paralelizable.
> (3) TypeScript nos deja elegir; Clojure nos obliga."

**Próxima clase:** Tema 04 — Aspectos Avanzados de Programación Funcional
**Pendiente:** Confirmar tipo y fecha del TP → usar `/edu-create-tp` para generarlo
