# Tema 13: Estructuración de Programas (Módulo X)

## Metadatos

| Campo | Valor |
|-------|-------|
| Tema | 13 — Estructuración de Programas (Módulo X) |
| Clases | 2 × 120 min = 240 min totales |
| Semana | 13 |
| Libro principal | Sebesta — *Concepts of Programming Languages* (Pearson 2019) — Caps. 9, 10, 11, 12 |
| Complementarios | Gabbrielli/Martini — *Programming Languages: Principles and Paradigms* (2nd ed., Springer 2023) — Caps. 5, 7; Louden/Lambert — *Principles and Practices* (2012) — Cap. 11 |
| Objetivos Bloom | C1: definir; C2: explicar; C3: implementar en TS; C4: comparar; C5: evaluar diseño |
| Prerequisito | Tema 12 (Manejo de Excepciones), Tema 10–11 (Tipos de datos) |
| Lenguaje principal | TypeScript |

---

# CLASE 13A — Subprogramas, Parámetros y Sobrecarga (120 min)

## Apertura 13A (5 min) — [F-02]

Comenzar conectando con el tema anterior: así como el Tema 12 mostró cómo manejar situaciones anómalas en tiempo de ejecución, el Módulo X pregunta algo más fundamental: *¿cómo organizamos el código para que las fallas sean raras?* La respuesta es la **estructuración**: subprogramas, módulos e interfaces.

Enunciar la pregunta motivadora: *"¿Por qué ningún programa real se escribe en una única función?"* Dejar que el aula responda brevemente (legibilidad, reutilización, testeo). Luego afirmar: esas respuestas intuitivas son exactamente lo que formalizaremos en estas dos clases.

Presentar el plan de las dos clases con [F-01]. Hacer notar que la clase 13A cubre el nivel 1 (subprogramas) y la 13B sube al nivel 2 (ADTs) y nivel 3 (módulos).

---

## Bloque 1 — Fundamentos de Subprogramas (20 min)

### [F-03] Subprograma: Definición Formal

**Concepto central**: Sebesta (§9.1) define el subprograma como la unidad fundamental de abstracción de comportamiento. Sus propiedades son: única entrada, llamador que suspende su ejecución, y retorno de control al completarse. La definición de **parámetro formal** vs. **parámetro real (actual)** es esencial: el formal es la variable en el encabezado, el real es el valor en el sitio de llamada.

**¿Qué decirle al aula?** "Fíjense que Sebesta dice 'salvo en el caso de la recursividad'. ¿Por qué ese salvo? Porque con recursión, hay múltiples instancias del mismo subprograma ejecutando simultáneamente. Eso lo vamos a ver exactamente cuando lleguemos a los activation records."

**Pregunta socrática**: ¿Un método de una clase orientada a objetos es un subprograma? ¿Qué tiene de diferente al de Sebesta? (Respuesta: sí, con la adición del parámetro implícito `this`).

**Tiempo**: 5 min. Transición: "Ahora veamos cuántas *clases* de subprogramas hay."

---

### [F-04] Procedimiento vs. Función

**Concepto central**: La distinción entre procedimiento (efecto lateral, sin valor de retorno explícito) y función (computa un valor) es **semántica** en la mayoría de los lenguajes modernos. En Ada es **sintáctica y obligatoria** — hay dos palabras reservadas distintas. Python y TypeScript usan la misma sintaxis `def` / `function` para ambos: la diferencia viene del uso de `return`.

**¿Qué decirle al aula?** "Haskell representa el extremo: no existen procedimientos. Todo es una función pura. Si necesitás efectos laterales (imprimir algo, escribir un archivo), los modelás como valores dentro de la mónada IO. Es la posición más radical posible sobre esta distinción — y es coherente con el paradigma funcional puro que vimos en los primeros temas del curso."

**Tabla comparativa multilenguaje**: usar [F-04] para hacer la recorrida lengua por lenguaje. Es rápido — 2 minutos de tabla.

**Pregunta anticipada**: *¿En TypeScript, una función que retorna `void` y tiene efectos laterales es un procedimiento o una función?* Respuesta: semánticamente es un **procedimiento**, aunque TypeScript no tiene esa distinción sintáctica.

**Tiempo**: 5 min. Transición: "Para describir con precisión un subprograma, usamos dos conceptos: perfil y protocolo."

---

### [F-05] Perfil y Protocolo

**Concepto central**: El **perfil** (parameter profile) es el número, orden y tipos de los parámetros formales. El **protocolo** es el perfil más el tipo de retorno. Sebesta usa estos términos en §9.1 y los usa extensivamente al definir sobrecarga y polimorfismo. En TypeScript, el perfil y protocolo están codificados en el tipo de función: `(peso: number, altura: number) => number`.

**¿Qué decirle al aula?** "Cuando en Java dicen 'signature del método', están hablando del perfil (sin el tipo de retorno, en la definición estricta de Java). Cuando en Haskell escriben `f :: Int -> Int -> Bool`, están dando el protocolo completo. Son el mismo concepto con distinta nomenclatura según el libro o lenguaje."

**Ejemplo en pizarrón** (opcional): escribir `calcularIMC(70, 1.75)` y pedir a alguien del aula que identifique perfil, protocolo, parámetro formal y parámetro real.

**Tiempo**: 5 min. Transición: "Los parámetros formales pueden ser de distintas clases según su duración. Veamos."

---

### [F-06] Variables Locales: Stack-Dynamic vs. Static

**Concepto central**: La distinción entre variables locales stack-dynamic (creadas en el activation record al invocar, destruidas al retornar) y variables estáticas locales (asignadas una vez, persisten entre llamadas) tiene implicaciones directas sobre **recursividad**. Fortran 77 usaba variables estáticas por defecto — y por eso no podía ser recursivo. Sebesta §9.2 explica que la recursividad requiere stack-dynamic: cada llamada necesita su propio frame con sus propias variables.

**¿Qué decirle al aula?** "Hay una tendencia a pensar que la recursividad 'siempre existió'. No — fue una decisión de diseño del lenguaje. FORTRAN 77 la prohibía *por diseño*, eligiendo eficiencia de memoria sobre flexibilidad expresiva. La elección del modelo de variables locales es una de las decisiones de diseño fundamentales de un lenguaje."

**Ejemplo en Python**: `def con_historia(): con_historia.llamadas = getattr(con_historia, 'llamadas', 0) + 1; return con_historia.llamadas` — atributo de función como simulación de static local.

**Pregunta anticipada**: *¿TypeScript tiene variables estáticas locales?* Respuesta: no directamente. Se puede simular con módulos (variable en scope de módulo, no exportada) o con closures.

**Tiempo**: 5 min. Transición: "Ahora que conocemos las partes del subprograma, veamos cómo se pasan los datos entre llamador y llamado."

---

## Bloque 2 — Pasaje de Parámetros (25 min)

### [F-07] Código TypeScript: Función Pura vs. Procedimiento

**Guion de código**: Mostrar `registrarAcceso` (procedimiento, `void`) y `calcularIMC` (función pura, retorna `number`). Señalar explícitamente el perfil `(peso: number, altura: number)` y el protocolo `(number, number) → number` como anotaciones. Hacer notar que TypeScript **fuerza** al programador a pensar en tipos — el perfil es literal en el código.

**Énfasis**: "La función `calcularIMC` no tiene efectos laterales: dados los mismos inputs, siempre produce el mismo output. Es **referencialmente transparente**. `registrarAcceso` no lo es: su efecto depende de cuándo se llama (el timestamp cambia)."

**Tiempo**: 3 min.

---

### [F-08] Tabla: Métodos de Pasaje de Parámetros

**Concepto central**: Los cinco métodos de pasaje (value, result, value-result, reference, name) difieren en la **dirección del flujo de información** y en el **momento de la copia**. Sebesta §9.5 dedica 17 páginas a esto porque es uno de los aspectos de diseño con mayor impacto en semántica y seguridad.

**¿Qué decirle al aula?** "Pass-by-name de Algol 60 es el más raro. En cada referencia al parámetro formal, se re-evalúa la expresión real. Esto permitía trucos como `swap(a[i], i)` — pero era notoriamente difícil de entender y predecir. Hoy solo sobrevive en lenguajes funcionales como los `by-name parameters` de Scala, que son la base de la evaluación lazy."

**Destacar para TS**: "TypeScript no tiene pass-by-reference en el sentido de C++. No podés pasar un número y que el llamado lo modifique. Podés *simular* pass-by-reference pasando un objeto mutable — eso es pass-by-sharing. La diferencia es sutil pero importante."

**Tiempo**: 5 min.

---

### [F-09] Código TypeScript: Pass-by-Value vs. Pass-by-Sharing

**Guion de código**: El ejemplo de `doblar(n: number)` muestra que el número no cambia fuera de la función. El ejemplo de `agregarItem(arr: number[], item: number)` muestra que el array sí cambia — porque se pasa la referencia al mismo objeto en heap.

**¿Qué decirle al aula?** "La pregunta que siempre surge es: '¿TypeScript pasa por valor o por referencia?' La respuesta correcta es: **por valor siempre** — pero el valor que se copia para objetos es una *referencia* (dirección de memoria), no el objeto en sí. Por eso se llama pass-by-sharing o pass-by-object-reference. Las propiedades del objeto son accesibles a través de la copia de referencia; la reasignación de la variable local no afecta al original."

**Conexión con la socrática siguiente**: "La siguiente filmina tiene un ejemplo que va a hacer que esto quede muy claro. Primero, ¿alguien puede predecir qué pasa si dentro de la función reasignamos el parámetro?"

**Tiempo**: 7 min.

---

### [F-10] Socrática: Pass-by-Sharing en TypeScript

**Guion socrático**: Mostrar el código de `cambiarNombre` con las dos líneas A (modifica propiedad) y B (reasigna variable). Dar 60 segundos al aula para discutir en pares. Luego preguntar: "¿Alguien dice 'cambiado'? ¿Alguien dice 'original'? ¿Alguien dice 'nuevo obj'?" Registrar las respuestas.

**Explicación**: "La línea A modifica la propiedad `nombre` del objeto apuntado por `obj`. Como `persona` y `obj` apuntan al mismo objeto, `persona.nombre` cambia. La línea B crea un nuevo objeto `{ nombre: 'nuevo obj' }` y reasigna la variable local `obj` para que apunte a él. Pero `persona` sigue apuntando al objeto original — con el `nombre` ya cambiado por la línea A. Resultado: 'cambiado'."

**Diagrama en pizarrón** (si hay tiempo): dibujar dos cajas (persona y obj) apuntando al mismo objeto en heap, luego la reasignación de obj a un nuevo objeto.

**Pregunta anticipada**: *¿Cómo hago para que un método TypeScript simule pass-by-result (que el llamado "devuelva" un valor modificando la variable del llamador)?* Respuesta: no se puede con primitivos en TS; se usa `return` o un objeto de salida.

**Tiempo**: 10 min. Transición: "Pasemos a un mecanismo muy relacionado con el pasaje de parámetros: las closures."

---

## Bloque 3 — Closures y Subprogramas de Orden Superior (15 min)

### [F-11] Closures y Captura del Entorno Léxico

**Concepto central**: Una **closure** es un subprograma junto con el **entorno de referencia** en el que fue creado (Sebesta §9.12). Cuando `makeAdder` retorna, su activation record normalmente se destruiría. Pero como la función anónima retornada capturó la variable `x`, el entorno de `makeAdder` sobrevive en el heap mientras la closure exista — el GC lo mantiene vivo.

**¿Qué decirle al aula?** "Esto conecta directamente con lo que vimos sobre variables locales stack-dynamic. La variable `x` de `makeAdder` *normalmente* viviría en el stack y desaparecería al retornar. Pero como la closure la captura, el runtime la mueve al heap. Los lenguajes con closures tienen que hacer este trabajo automáticamente."

**Conexión con paradigma funcional**: "En los primeros temas del curso vimos closures en el paradigma funcional. Ahora las vemos desde la perspectiva de la implementación: ¿qué hace el runtime para que funcionen? La respuesta es: captura el entorno léxico y lo sobrevive en el heap."

**Ejemplo en Kotlin** (comparativo): `val sumar5 = { y: Int -> y + 5 }` — lambda que captura un valor del scope exterior si se necesita.

**Tiempo**: 8 min.

---

### [F-12] Subprogramas como Parámetros: HOF

**Concepto central**: TypeScript permite pasar funciones como argumentos con **tipos de función** explícitos: `(item: T) => boolean`. Esto es lo que Sebesta §9.11 llama "subprograms as parameters". El tipo `Predicado<T>` y `Transformacion<A,B>` son tipos de primera clase en TS — se pueden asignar a variables, pasar a funciones, retornar desde funciones.

**¿Qué decirle al aula?** "El punto pedagógico clave aquí es el tipo del parámetro. En `filtrar<T>(arr: T[], pred: Predicado<T>)`, el parámetro `pred` tiene tipo `(item: T) => boolean`. Esto es exactamente la definición formal de un subprograma con su protocolo. TypeScript convierte el protocolo del subprograma en el tipo del parámetro. Eso es elegante."

**Pregunta rápida**: "¿Podría pasar `console.log` como argumento a `filtrar`? ¿Por qué o por qué no?" (Respuesta: no, porque `console.log` tiene tipo `(...data: any[]) => void`, que no es compatible con `(item: T) => boolean`).

**Tiempo**: 7 min. Transición: "Ahora estudiemos el mecanismo que permite al mismo nombre servir para distintos tipos: la sobrecarga."

---

## Bloque 4 — Sobrecarga y Polimorfismo (25 min)

### [F-13] Sobrecarga: Polimorfismo Ad Hoc

**Concepto central**: Sebesta §9.8 distingue claramente: la sobrecarga es **polimorfismo ad hoc** — distintas implementaciones para distintos tipos, seleccionadas en tiempo de compilación por los tipos de los argumentos. No debe confundirse con el polimorfismo paramétrico (genéricos) donde hay UNA implementación que funciona para múltiples tipos mediante un parámetro de tipo `<T>`.

**¿Qué decirle al aula?** "Sebesta dice algo provocador: 'los subprogramas sobrecargados no necesitan comportarse de manera similar'. El operador `+` en Python suma números pero concatena strings — son operaciones completamente distintas, solo unidas por el nombre. Eso es ad hoc: conveniente para el programador, pero potencialmente confuso. El polimorfismo paramétrico, en cambio, garantiza que la función hace lo mismo para todos los tipos."

**Tabla comparativa ad hoc vs. paramétrico**: recorrer las tres filas de [F-13] con un ejemplo concreto para cada una.

**Tiempo**: 7 min.

---

### [F-14] Código TypeScript: Overload Signatures

**Guion de código**: Las tres overload signatures son **contratos de tipo** — el compilador las usa para inferir el tipo de retorno en cada sitio de llamada. La implementación unificada es más permisiva: acepta `string | number | boolean`. La implementación no es visible externamente a los efectos del tipado.

**¿Qué decirle al aula?** "En TypeScript, las overload signatures son estrictamente para el sistema de tipos. En runtime, solo existe la implementación. Esto es diferente de C++ donde el compilador genera código real para cada overload. En TS, vos sos responsable de la implementación unificada — el compilador te exige que sea más permisiva que las signatures."

**Demostración en vivo** (si hay laptop en el aula): mostrar que `procesar([1,2])` da error de compilación aunque la implementación no tiene una rama para arrays. El compilador rechaza la llamada porque no hay signature compatible.

**Tiempo**: 8 min.

---

### [F-15] Socrática: Ambigüedad con Defaults

**Guion socrático**: Mostrar el ejemplo C++ de `void fun(float b = 0.0)` y `void fun()`. Preguntar: "Si el compilador ve `fun()`, ¿cuál de las dos llama?" Dar 30 segundos. Respuesta: es ambiguo — el compilador C++ emite un error de ambigüedad.

**¿Por qué TypeScript lo evita?**: La implementación unificada es única. No hay dos funciones reales — solo las signatures de tipos. No puede haber ambigüedad porque en runtime hay una sola función.

**Pregunta reflexiva**: "¿Cuándo preferirían sobrecargar en lugar de usar un genérico?" Guiar hacia: cuando los comportamientos son genuinamente distintos (concatenar vs. sumar) vs. cuando es el mismo algoritmo para distintos tipos (sort).

**Tiempo**: 5 min.

---

### [F-16] Polimorfismo Paramétrico y Genéricos

**Concepto central**: Sebesta §9.9 dice que los subprogramas genéricos toman **parámetros de tipo** que aparecen en las expresiones de tipo de los parámetros. La clave diferencial con la sobrecarga: hay UNA implementación que el compilador instancia para cada tipo concreto usado.

**¿Qué decirle al aula?** "Piensen en `sort<T>`. En C++, el compilador genera código máquina distinto para `sort<int>`, `sort<string>` y `sort<float>`. En TypeScript (que compila a JS), no hay especialización real — hay una sola función en runtime. Pero el sistema de tipos te garantiza en compilación que los tipos son correctos. Es la misma idea conceptual implementada de manera muy diferente bajo el capó."

**Tiempo**: 5 min. Transición a código.

---

### [F-17] Código TypeScript: Generic Functions con Constraints

**Guion de código**: `primerElemento<T>` muestra la inferencia automática de tipo. `máximo<T extends Comparable<T>>` muestra que el constraint `extends` exige que T tenga el método `compareTo`. Esto conecta con el diseño de interfaces del tipo (C5 — evaluar): ¿qué constraint es el mínimo necesario para que la función funcione?

**¿Qué decirle al aula?** "El `extends` en el parámetro de tipo es un constraint, no una herencia. Estoy diciendo: T puede ser cualquier tipo, siempre que implemente la interfaz `Comparable<T>`. Esto es una forma de diseño muy explícito: la función declara exactamente qué necesita del tipo T, ni más ni menos."

**Tiempo**: 5 min. Transición: "Ahora vamos al nivel de la máquina: ¿cómo se implementa todo esto en memoria?"

---

## Bloque 5 — Implementación: Activation Records (25 min)

### [F-18] Diagrama: Activation Records y Stack de Llamadas

**Concepto central**: Un **activation record** (AR) es la estructura en el stack que contiene los datos de una invocación activa de un subprograma: parámetros, variables locales, dirección de retorno y **dynamic link** (puntero al AR del llamador). El dynamic chain pointer de Gabbrielli (§5.3.3) es exactamente el `dynamic link` de Sebesta §10.3.

**¿Qué decirle al aula?** "Miren el diagrama de `factorial(3)`. Hay tres activation records en el stack simultáneamente — uno para `factorial(3)`, uno para `factorial(2)` y uno para `factorial(1)`. Cada uno tiene su propia variable `n`. Es POR ESTO que la recursividad funciona: cada llamada tiene su propio espacio de variables. Si las variables fueran estáticas (como en Fortran 77), el segundo `factorial` sobreescribiría el `n` del primero."

**Recorrer el diagrama**: "El dynamic link de `factorial(1)` apunta a `factorial(2)`. El de `factorial(2)` apunta a `factorial(3)`. El de `factorial(3)` apunta a `main`. Cuando se resuelve `factorial(1)` y retorna, su AR se libera. Luego `factorial(2)` puede completar el cálculo `2 * 1 = 2`. Y así sucesivamente."

**Pregunta anticipada**: *¿Hay un límite para la profundidad de la recursividad?* Respuesta: sí — el límite del stack. En Node.js (TypeScript), es aproximadamente 10.000-15.000 llamadas dependiendo del tamaño del AR. Excederlo produce **Stack Overflow**.

**Tiempo**: 12 min.

---

### [F-19] Semántica de Call/Return

**Concepto central**: Los pasos de call y return que describe Sebesta §10.1 son la especificación de lo que hace el runtime a nivel de instrucciones de máquina. El compilador genera estas instrucciones automáticamente. Comprender estos pasos ayuda a entender el costo de las llamadas a función, las optimizaciones como tail-call elimination, y errores como stack overflow.

**¿Qué decirle al aula?** "Cuando TypeScript compila a JavaScript y JavaScript se ejecuta en el motor V8 de Node.js o del browser, estos pasos ocurren en microsegundos. El motor V8 tiene un JIT compiler que puede optimizar tail calls — si la última operación de una función es una llamada recursiva, puede reutilizar el mismo activation record. Así se evita el stack overflow para recursión de cola. TypeScript lo soporta desde ES2015."

**Conexión hacia la clase 13B**: "Ahora que entendemos cómo funciona un subprograma por dentro, en la próxima clase subimos un nivel: ¿cómo agrupamos subprogramas con los datos que manejan? La respuesta es el ADT."

**Tiempo**: 13 min.

---

## Cierre 13A (5 min) — [F-20]

Recorrer la tabla de cierre de [F-20]: los 8 conceptos con su definición breve. Hacer énfasis en las relaciones entre conceptos: stack-dynamic → habilita closures → habilita HOF → sobrecarga y genéricos son dos formas de polimorfismo.

Tarea o pregunta de reflexión para el intermedio: "Antes de la clase 13B, piensen: en un proyecto TypeScript real que hayan escrito o visto, ¿qué partes serían subprogramas, qué partes ADTs y qué partes módulos? Traigan un ejemplo."

---

# CLASE 13B — Módulos, Interfaces y Genéricos en TypeScript (120 min)

## Apertura 13B (5 min) — [F-21]

Retomar la reflexión del cierre 13A. Preguntar si alguien pensó en un ejemplo. Conectar: "En la 13A vimos el nivel 1 de abstracción — el subprograma. Hoy subimos al nivel 2 (ADT) y al nivel 3 (módulo). La jerarquía que vamos a construir al final de la clase es la síntesis del Módulo X."

---

## Bloque 6 — ADTs: Encapsulamiento e Information Hiding (20 min)

### [F-22] ADT: Definición Formal

**Concepto central**: Sebesta §11.1 define el ADT con tres propiedades: representación oculta, operaciones por interfaz, invariantes garantizadas. La diferencia entre un ADT y simplemente una clase con métodos es el **compromiso semántico**: el ADT se define por lo que *puede hacer* (operaciones), no por cómo está *implementado* (estructura de datos).

**¿Qué decirle al aula?** "¿Por qué importa ocultar la representación? Pensemos en `Stack`. Si expongo que internamente usa un array, el cliente puede hacer `stack.datos[0]` — y ahora depende de que sea un array. Mañana quiero cambiar a una lista enlazada para mejorar performance en ciertos casos: imposible sin romper al cliente. Si oculto la representación, puedo cambiarla sin que el cliente se entere."

**Pregunta anticipada**: *¿No es lo mismo que una clase con private en cualquier lenguaje OO?* Respuesta: la diferencia es que el ADT es un **concepto formal** anterior a la POO. Ada y Modula-2 tienen ADTs sin ser lenguajes orientados a objetos en sentido estricto. La POO adopta los ADTs como su mecanismo central, pero no los inventó.

**Tiempo**: 8 min.

---

### [F-23] Código TypeScript: Stack con `private`

**Guion de código**: Recorrer la clase `Stack<T>` con `private datos: T[]`. Hacer notar que `private` en TypeScript es un mecanismo de **compilación** — en runtime (JavaScript), la propiedad existe y podría accederse con `(pila as any).datos`. Para encapsulamiento **real** en runtime, usar campos privados con `#`: `#datos: T[] = []`.

**¿Qué decirle al aula?** "TypeScript `private` es una promesa al compilador, no al runtime. `#datos` (campo privado de clase ES2022) sí es privacidad real en JavaScript — el campo está en un WeakMap interno y es inaccesible desde fuera de la clase incluso con cast. Para código de producción donde la seguridad importa, usar `#`. Para la semántica que estudiamos (ADT), `private` es suficiente."

**Tiempo**: 7 min.

---

### [F-24] Socrática: ¿Qué Expone la Interfaz?

**Guion socrático**: Mostrar la clase con los cuatro candidatos comentados. Discusión en grupos de 2-3 sobre si `toArray()`, `at(index)`, `clear()` y `contains()` deben estar o no en la interfaz.

**Guia de respuesta**:
- `clear()`: operación válida — es una operación *del* ADT, no un detalle de implementación.
- `toArray()`: controversia — retorna una copia del estado; expone la *forma* de los datos pero no la estructura interna. Si retorna `readonly T[]`, está razonablemente encapsulado.
- `at(index)`: **viola** la semántica de Stack — convierte LIFO en acceso aleatorio. La Stack deja de ser una Stack.
- `contains()`: discutible — es una operación de búsqueda. Si es O(n), ¿debería estar en la interfaz? Depende del contrato que quieras garantizar.

**Principio rector**: "Una buena interfaz expone exactamente lo que el ADT promete semánticamente — ni más ni menos."

**Tiempo**: 5 min. Transición: "Ahora formalizamos esta separación entre interfaz e implementación con el mecanismo TypeScript real."

---

## Bloque 7 — Interfaz vs. Implementación; Compilación Separada (25 min)

### [F-25] Separación Interfaz / Implementación

**Concepto central**: El principio de separación (Sebesta §11.2, Louden §11.3) dice que la interfaz y la implementación son **unidades de compilación distintas**. El cliente compila contra la interfaz; cuando la implementación cambia, el cliente no necesita recompilarse si la interfaz no cambió.

**¿Qué decirle al aula?** "Esto es exactamente lo que pasa en un proyecto grande en TypeScript con `tsc --incremental`. Si cambio la implementación de `ArrayStack` sin tocar la interfaz `IStack`, TypeScript solo recompila el archivo de `ArrayStack`. Los módulos que usan `IStack` no necesitan recompilarse. En un proyecto de 500 archivos, esto es la diferencia entre un build de 30 segundos y uno de 3 minutos."

**Tiempo**: 5 min.

---

### [F-26] Código TypeScript: `interface` + `class` Separadas

**Guion de código**: Mostrar `IStack<T>` con 5 operaciones tipadas y `ArrayStack<T>` implementándola. El campo `private readonly elementos: T[]` es el detalle de implementación. El cliente que importa solo `IStack<T>` **nunca sabe** que el backing store es un array.

**¿Qué decirle al aula?** "La palabra `readonly` en `private readonly elementos` significa que la referencia al array no puede reasignarse, pero el array sí puede modificarse. Es parte del diseño de la implementación, no parte de la interfaz. El cliente no sabe nada de esto. Si mañana cambio a `private readonly elementos: LinkedList<T>`, el cliente no se entera — y eso es exactamente lo que queremos."

**Ejemplo práctico**: Si tuvieran que implementar tests para `ArrayStack`, ¿qué testearían? Solo las operaciones de `IStack<T>` — así los tests son independientes de la implementación.

**Tiempo**: 10 min.

---

### [F-27] DEFINITION MODULE vs. IMPLEMENTATION MODULE (Modula-2)

**Concepto central**: Louden §11.3 presenta el modelo de Modula-2 como la formalización clásica de la separación interfaz/implementación en módulos. El `DEFINITION MODULE` es análogo al archivo `stack.ts` con solo la `export interface`. El `IMPLEMENTATION MODULE` es análogo a `class ArrayStack` con los detalles.

**¿Qué decirle al aula?** "Modula-2 fue diseñado por Niklaus Wirth en los años 80 para enseñar exactamente este principio. TypeScript redescubrió la misma idea con `interface` + `class` en un ecosistema moderno. Los conceptos son los mismos; la sintaxis cambia. Si alguna vez trabajan con lenguajes de sistemas como Ada o Go, van a ver la misma separación bajo distintos nombres."

**Comparación Ada**: Ada usa `package specification` (equivalente al DEFINITION MODULE) y `package body` (equivalente al IMPLEMENTATION MODULE). Es esencialmente el mismo modelo.

**Tiempo**: 5 min.

---

### [F-28] Diagrama: Módulo con Dependencias Explícitas

**Guion**: Recorrer el diagrama de módulos: `main.ts` importa de `stack.ts` y `utils/logger.ts`. `stack.ts` tiene sección de interfaz y sección de implementación. `utils/logger.ts` importa del paquete npm `date-fns`.

**Punto clave**: Louden §11.1 dice que el mecanismo de módulos permite **documentar las dependencias** con imports explícitos. Esto es lo que le da al compilador la información para detectar módulos desactualizados y recompilar selectivamente.

**Contraejemplo**: En C sin headers, el módulo A puede usar funciones del módulo B sin ningún import explícito — el enlazador resuelve todo en link time. Esto hace imposible el análisis estático de dependencias y la verificación de tipos en compilación.

**Tiempo**: 5 min.

---

### [F-29] Compilación Separada vs. Independiente

**Guion de tabla**: Recorrer las 6 filas de la tabla comparativa. El punto central: la compilación separada agrega verificación de tipos cruzada entre módulos. La compilación independiente es más flexible físicamente pero sacrifica seguridad de tipos.

**¿Qué decirle al aula?** "TypeScript hace compilación separada: cuando compilás `main.ts`, el compilador lee los archivos `.d.ts` de las dependencias y verifica que los tipos son correctos. Si `stack.ts` exporta `push(item: T): void` y `main.ts` llama `push(item: T, extra: string)`, el compilador lo detecta. Eso es compilación separada con verificación de tipos. C clásico sin headers no hace eso — el error aparece en tiempo de enlace o peor, en runtime."

**Tiempo**: 5 min. Transición: "Veamos cómo TypeScript implementa esto con el sistema de módulos ES."

---

## Bloque 8 — Módulos en TypeScript: `import`/`export`, Librerías (25 min)

### [F-30] Código TypeScript: `import`/`export` y `tsconfig`

**Guion de código**: Tres archivos: `stack.ts` exporta, `colecciones.ts` re-exporta con `export type` (solo el tipo, eliminado en compilación), `main.ts` importa con `import type` (zero runtime cost).

**¿Qué decirle al aula?** "La distinción entre `import` e `import type` es importante para performance. `import type { IStack }` le dice al compilador: 'solo necesito este tipo para verificar tipos en compilación; no lo incluyas en el bundle JavaScript'. Esto reduce el tamaño del bundle final. Es una optimización que TypeScript hace automáticamente con `isolatedModules: true` en `tsconfig`."

**Sobre `tsconfig.json`**: El fragmento `"module": "ES2022"` y `"moduleResolution": "Node16"` le dicen al compilador cómo resolver los imports — qué archivos buscar, en qué orden, si usar `node_modules` o no. Hay cuatro estrategias principales; `Node16` es la recomendada para proyectos Node.js modernos.

**Pregunta anticipada**: *¿Cuál es la diferencia entre `export default` y `export`?* Respuesta: `export default` permite importar con cualquier nombre (`import Cualquier from './stack'`). `export` (named exports) exige el nombre exacto. La convención en TypeScript moderno es preferir named exports — son más seguros y se llevan mejor con los tree shakers de bundlers como webpack.

**Tiempo**: 15 min.

---

### [F-31] Librerías de Módulos: npm y `@types`

**Guion**: El ecosistema npm como la mayor librería de módulos del mundo. La analogía con DEFINITION MODULE de Modula-2 es exacta: los archivos `.d.ts` de `@types` son los contratos públicos de paquetes JavaScript que no tienen TypeScript nativo.

**¿Qué decirle al aula?** "DefinitelyTyped es una muestra extraordinaria de colaboración de la comunidad. Es un repositorio con más de 8.000 paquetes de definiciones de tipos, mantenido por voluntarios. Cuando instalás `@types/lodash`, obtenés exactamente el DEFINITION MODULE de lodash — los tipos de todas las funciones, sin el código de implementación."

**Ejemplo práctico**: `npm install date-fns` instala el paquete con TypeScript nativo (los tipos ya están incluidos). `npm install lodash` + `npm install -D @types/lodash` instala el paquete JS + las definiciones de tipos por separado.

**Tiempo**: 10 min. Transición: "Ahora combinamos módulos con el sistema de tipos genérico para construir estructuras de datos reutilizables."

---

## Bloque 9 — Estructuras de Datos Genéricas en TypeScript (25 min)

### [F-32] `Stack<T>` Genérico Completo

**Guion de código**: Mostrar la implementación completa de `Stack<T>` con todos los métodos. El método `contains(pred: (item: T) => boolean)` combina genéricos con HOF — el predicado también opera sobre `T`. El `toArray(): readonly T[]` retorna una copia inmutable — `readonly` impide modificaciones al array desde fuera.

**¿Qué decirle al aula?** "Noten que `readonly T[]` no significa que los objetos dentro del array sean inmutables — significa que no podés hacer `pila.toArray().push(algo)`. El `readonly` protege la *referencia al array*, no los objetos. Si `T` es un objeto mutable, sus propiedades siguen siendo mutables. Para inmutabilidad profunda, necesitarían `Readonly<T>` en cada elemento — tema para otro día."

**Tiempo**: 8 min.

---

### [F-33] `Queue<T>` y `Map<K,V>` con Constraints

**Guion de código**: `Queue<T extends Printable>` muestra un constraint en la clase entera — todos los elementos del queue deben implementar `toString()`. Esto permite el método `print()` sin saber el tipo concreto. `TypedMap<K extends string | number, V>` usa un union type como constraint — K solo puede ser string o number, que son los tipos de clave nativos de JavaScript Map.

**¿Qué decirle al aula?** "El constraint `K extends string | number` no es arbitrario. JavaScript (y por ende TypeScript) usa internamente strings como claves de objetos y maps. Restringir K a estos tipos garantiza que la clave sea serializable como string — importante si en algún momento queremos persistir el mapa en JSON o enviarlo por red."

**Kotlin comparativo**: 
```kotlin
class Queue<T : Comparable<T>> { ... }  // constraint con : en Kotlin
```

**Tiempo**: 10 min.

---

### [F-34] Conditional Types y Mapped Types

**Guion de código**: `EsArray<T>` como ejemplo mínimo de conditional type — una decisión en tiempo de compilación. `TipoRetorno<F>` con `infer R` muestra una técnica avanzada: extraer el tipo de retorno de una función sin conocerlo explícitamente. `SoloLectura<T>` y `Parcial<T>` son mapped types — transformaciones sobre todas las propiedades de un tipo.

**¿Qué decirle al aula?** "Esto es lo que TypeScript llama 'tipos de orden superior' — tipos que operan sobre otros tipos. `Parcial<T>` hace que todas las propiedades de `T` sean opcionales. `SoloLectura<T>` las hace `readonly`. Estos mismos tipos están en la biblioteca estándar de TypeScript como `Partial<T>` y `Readonly<T>`. Si alguna vez vieron esos nombres en código TypeScript y se preguntaron de dónde venían, ahora saben: son mapped types, exactamente como los que acabamos de escribir."

**Conexión con genéricos del bloque anterior**: "Los genéricos de clase (`Stack<T>`) operan sobre valores. Los conditional types operan sobre **tipos**. TypeScript tiene un sistema de tipos tan expresivo que podés escribir lógica en el nivel de los tipos — eso se llama 'programming at the type level'."

**Tiempo**: 7 min. Transición: "Ahora integramos todo con la síntesis del Módulo X."

---

## Cierre del Módulo X + Preview Concurrencia (20 min)

### [F-35] Jerarquía de Abstracción

**Guion**: Mostrar la pirámide de tres niveles. Conectar cada nivel con los bloques del día:
- Nivel 1 (Subprograma) → Clase 13A: perfil, protocolo, closures, activation records
- Nivel 2 (ADT) → Clase 13B primeros bloques: `Stack<T>` con `private`, `interface IStack<T>`
- Nivel 3 (Módulo) → Clase 13B últimos bloques: `import`/`export`, compilación separada, npm

**¿Qué decirle al aula?** "La jerarquía no es solo descriptiva — es prescriptiva. Al diseñar software, empezás en el nivel 1 (qué operaciones tenés) y subís. Si encontrás operaciones que comparten datos, las agrupás en un ADT (nivel 2). Si tenés múltiples ADTs que pertenecen a un dominio, los agrupás en un módulo (nivel 3). Es un proceso de diseño *bottom-up* — y también puede hacerse *top-down* partiendo del módulo."

**Tiempo**: 5 min.

---

### [F-36] Tabla Síntesis Módulo X

**Guion**: Recorrer las 8 filas de la tabla. Hacer énfasis en la columna "Tool TypeScript" — cada concepto tiene un mecanismo concreto en el lenguaje. La columna "Sebesta §" permite ubicar la lectura de referencia para cada concepto.

**Pregunta de revisión rápida**: "¿Cuál es la diferencia entre `<T>` en una función genérica y las overload signatures?" (Polimorfismo paramétrico vs. ad hoc). "¿Cuál es la diferencia entre `interface` y `class`?" (Contrato vs. implementación).

**Tiempo**: 5 min.

---

### [F-37] Socrática Final: Diseñar una API Pública

**Guion socrático**: El caso de `IUserRepository` es realista — es exactamente el tipo de diseño que enfrentarán en proyectos. Discusión guiada:
- `findById`, `save`, `delete` son claramente parte de la interfaz.
- `findAll()` — ¿debería estar? (Depende del contrato del repositorio.)
- `pool` (conexión a base de datos) — **no**, es un detalle de implementación.
- `cache` (caché en memoria) — **no**, es una optimización interna.

**¿Qué decirle al aula?** "Si exponés `pool` en la interfaz, estás diciendo que TODO repositorio debe tener un pool de conexiones. ¿Qué pasa con un `InMemoryUserRepository` para tests? No tiene pool. La interfaz quedaría rota. El principio: la interfaz solo expone lo que todos los implementadores pueden cumplir."

**Tiempo**: 5 min.

---

### [F-38] Cierre Módulo X + Preview Concurrencia

**Guion**: Celebrar el cierre del Módulo X — uno de los más ricos del curso. Hacer la pregunta de apertura del Módulo XI: *"¿Qué pasa cuando dos subprogramas se ejecutan al mismo tiempo?"* Dejar que el aula sugiera problemas: ¿qué pasa si dos funciones modifican el mismo objeto simultáneamente?

**Preview Módulo XI**: 
- **Race conditions**: dos hilos modifican el mismo dato sin coordinación
- **Semáforos y monitores**: mecanismos de coordinación clásicos (Sebesta Cap. 13)
- **async/await en TypeScript**: concurrencia basada en promesas y el event loop
- **Canales en Go, `asyncio` en Python**: modelos alternativos de concurrencia

**Cierre motivador**: "La estructura que construimos en el Módulo X — subprogramas bien encapsulados, con interfaces claras y módulos independientes — es exactamente la base que necesitamos para escribir código concurrente correcto. Sin encapsulamiento, la concurrencia es imposible de razonar. Con él, podemos analizar qué puede y qué no puede modificarse en paralelo."

**Tiempo**: 5 min.

---

## Referencias Bibliográficas

### Sebesta — *Concepts of Programming Languages* (Pearson 2019)

| Sección | Contenido | Clase |
|---------|-----------|-------|
| §9.1 | Fundamentals of Subprograms — perfil, protocolo | 13A B1 |
| §9.2 | Design Issues for Subprograms — variables locales, stack-dynamic vs. static | 13A B1 |
| §9.5 | Parameter-Passing Methods — pass-by-value, reference, result, value-result | 13A B2 |
| §9.8 | Overloaded Subprograms — ad hoc polymorphism, ambigüedad con defaults | 13A B4 |
| §9.9–9.10 | Generic Subprograms — polimorfismo paramétrico, reutilización | 13A B4 |
| §9.11 | Subprograms as Parameters — HOF, entorno de referencia | 13A B3 |
| §9.12 | Closures — captura del entorno léxico | 13A B3 |
| §10.1–10.3 | Implementing Subprograms — call/return, activation records, stack-dynamic | 13A B5 |
| §11.1 | Abstract Data Types — definición formal, encapsulamiento, information hiding | 13B B6 |
| §11.2 | Encapsulation Constructs — separación interfaz/implementación | 13B B7 |
| §11.5 | Separate and Independent Compilation | 13B B7 |

### Gabbrielli/Martini — *Programming Languages: Principles and Paradigms* (Springer 2023)

| Sección | Contenido | Clase |
|---------|-----------|-------|
| §5.1 | Procedures and Functions | 13A B1 |
| §5.3.3 | Stack Management — dynamic chain pointer, activation records | 13A B5 |
| §7 | Modularization and ADTs | 13B B6-7 |

### Louden/Lambert — *Programming Languages: Principles and Practices* (2012)

| Sección | Contenido | Clase |
|---------|-----------|-------|
| §11.1 | Modules and Compilation — dependencias explícitas, recompilación | 13B B8 |
| §11.3 | DEFINITION MODULE vs. IMPLEMENTATION MODULE (Modula-2) | 13B B7 |
