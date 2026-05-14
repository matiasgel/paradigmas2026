# Filminas — Tema 09.2: Aliases, Closures, GC y Tipos

> **Agente:** Dr. Roberto ✍️ — Class Writer
> **Fecha:** 2026-05-14
> **Revisado:** 2026-05-14 — enriquecido con bibliografía oficial vía ChromaDB (Sebesta, Gabbrielli-Martini, Louden-Lambert) — 8 filminas nuevas
> **Tema:** 09.2 — Aliases, Closures, GC y Tipos
> **Duración:** 120 min (1 clase)
> **Lenguaje principal:** TypeScript
> **Fuente:** diseno.md + ChromaDB (Sebesta §5.3.3, §6.11, §9.5, §10.6, §15; Gabbrielli §7.4, §8.11, §11, §16.9; Louden §7.7, §9.1, §10.3, §10.5)
> **Prerequisito:** Tema 09.1 — Variables, Binding y Ámbito (5-tupla, categorías, ámbito estático)
> **Estado:** ✅ Enriquecido con bibliografía oficial — pendiente de revisión docente

---

## PORTADA

---

### [F-00] Portada

@tipo: portada

# Aliases, Closures, GC y Tipos

Paradigmas y Lenguajes de Programación — Clase 09.2
Universidad Nacional de Tierra del Fuego — Instituto IDEI · 2026

---

## BLOQUE 1 — Aliases: Dos Nombres, Un Objeto

---

### [F-01] ¿Qué es un alias?

@tipo: concepto-abstracto

# Un alias: dos nombres vinculados a la misma celda de memoria

## Definición — Sebesta §5.3.3, Louden §7.7

Un **alias** ocurre cuando **dos o más nombres distintos** están vinculados a la **misma celda de memoria** en el mismo momento de la ejecución.

## La diferencia con una copia

- Una **copia** crea una celda nueva con el mismo contenido — dos objetos independientes, dos L-values distintos
- Un **alias** no crea nada nuevo — solo agrega un segundo nombre que apunta al mismo L-value
- Cambiar el objeto a través de **cualquiera** de los nombres afecta lo que ven **todos** los demás

## Por qué importa académicamente

- El compilador no puede optimizar bien código con aliases posibles: no sabe si dos variables se solapan
- Dificulta la **verificación formal**: las precondiciones de una función pueden cambiar si el argumento tiene un alias externo que lo modifica
- El análisis estático no puede probar ausencia de efectos laterales si hay aliases

## Fuentes principales de aliases en lenguajes modernos

- Asignación de referencias (`obj2 = obj1` en TypeScript, Python, Kotlin)
- Parámetros pasados por referencia (punteros en Go, referencias en C++)
- Variables de un mismo union type que comparten representación interna

---

### [F-02] Alias por asignación de referencia — TypeScript

@tipo: codigo

# La asignación de objetos no copia — crea un segundo nombre para el mismo objeto

```typescript
// Asignación de un objeto: obj2 es un ALIAS de obj1 — mismo L-value, mismo heap-object
const obj1 = { valor: 42, nombre: "config" };
const obj2 = obj1;          // NO se crea una copia — obj2 apunta a la misma celda

// Modificar a través del alias modifica el original:
obj2.valor = 99;
console.log(obj1.valor);    // 99 — obj1 fue modificado sin tocarlo directamente

// Comprobación: son la misma referencia (mismo L-value)
console.log(obj1 === obj2); // true — misma identidad de objeto

// Con primitivos, la asignación sí copia el valor:
let x = 42;
let y = x;    // y es una COPIA — x y y son L-values independientes
y = 99;
console.log(x);  // 42 — x no cambió
// Los primitivos no tienen alias por asignación — los objetos sí
```

---

### [F-03] Alias a través de parámetros — Kotlin y Go

@tipo: codigo

# Cuando pasamos un objeto a una función, el parámetro es un alias del argumento original

```kotlin
// Kotlin — el parámetro 'p' recibe la misma referencia que 'origen'
data class Punto(var x: Int, var y: Int)

fun desplazar(p: Punto, dx: Int) {
    p.x += dx   // modifica el objeto ORIGINAL a través del alias p
                // el caller no lo ve de forma obvia — fuente de bugs silenciosos
}

val origen = Punto(0, 0)
desplazar(origen, 5)
println(origen.x)  // 5 — origen fue modificado dentro de desplazar
```

```go
// Go — punteros explícitos: el alias es visible en la firma de la función
func duplicar(p *int) {
    *p *= 2  // desreferencia y modifica la variable original del caller
}

x := 10
duplicar(&x)     // &x: se pasa la dirección — p es alias de x
fmt.Println(x)   // 20 — x fue modificado a través del puntero
// En Go el alias es explícito (el & y el *): más visible que en Kotlin o TypeScript
```

---

### [F-04] Consecuencias de los aliases

@tipo: concepto-abstracto

# Los aliases introducen dependencias invisibles entre partes del programa

## El problema de razonabilidad local

Una función que recibe dos parámetros puede asumir que son independientes entre sí. Si son aliases del mismo objeto, ese supuesto falla silenciosamente:

```
función f(a, b):
    a.valor = 10
    b.valor = 20
    return a.valor + b.valor
```

Si `a` y `b` son aliases: `a.valor` es 20 cuando se lee (porque `b.valor = 20` también modificó `a`).
Resultado: 40 en lugar del 30 esperado. Sin ninguna advertencia.

## Impacto en verificación formal

- Las precondiciones de la lógica de Hoare no se pueden establecer correctamente si hay aliases
- El análisis estático no puede probar la ausencia de efectos laterales cuando existen aliases ocultos
- El compilador pierde oportunidades de optimización: no puede reordenar lecturas si hay aliases potenciales

## Impacto en concurrencia

- Dos threads con aliases al mismo objeto necesitan sincronización explícita
- Sin ella: **race condition** — el resultado depende del orden de ejecución, no determinístico

## La regla de diseño defensivo

- Las funciones puras no deberían modificar sus parámetros: reciben referencias pero no mutan el objeto
- Usar `readonly` en TypeScript / `val` en Kotlin para comunicar al compilador y al lector esa intención

---

### [F-04b] Alias por colisión en paso por referencia — tres escenarios de Sebesta §9.5

@tipo: concepto-abstracto

# Sebesta §9.5: el paso por referencia genera tres categorías de alias involuntarios, todas peligrosas

## Escenario 1 — Colisión entre parámetros actuales

Si dos posiciones de parámetro recibidas por referencia se invocan con el **mismo argumento**, ambos nombres internos son aliases del mismo objeto:

```cpp
// C++ — fun(a, a): x e y apuntan al mismo int en memoria
void fun(int& x, int& y) {
    x = 10;
    y = 20;    // si x e y son el mismo objeto: leer x devuelve 20, no 10
               // ¿cuánto vale x + y? 40 si son alias, 30 si son distintos
}
int a = 5;
fun(a, a);   // comportamiento dependiente de implementación — no definido en C++
```

## Escenario 2 — Parámetro y variable global

Si el argumento pasado por referencia coincide con una variable global accesible dentro de la función, hay dos caminos al mismo dato:

```cpp
int i = 3;              // variable global
void fun(int& a) {
    i = 99;             // modifica i a través del nombre global
                        // a también cambió — son aliases del mismo objeto
}
fun(i);                 // a es alias de i
```

## Escenario 3 — Elemento de array y array completo por referencia

```cpp
fun1(list[i], list);    // el primer parámetro es un alias de list[i]
                        // el segundo da acceso a todo el array — incluyendo list[i]
                        // si fun1 modifica list a través del segundo parámetro,
                        // el primer parámetro verá ese cambio en la siguiente lectura
```

## El diagnóstico de Sebesta §9.5

> "Otro problema del pasaje por referencia es que pueden crearse aliases. [...] Los problemas con estos tipos de aliasing son los mismos que en otras situaciones de aliasing: hacen que los programas sean difíciles de leer y mantener."
> — Sebesta §9.5

Sebesta §9.5.2.4 propone **pass-by-value-result** como alternativa que elimina estos tres escenarios: el parámetro recibe una copia al inicio y la escribe de vuelta al final — sin alias en ningún momento de la ejecución de la función.

---

### [F-05] `readonly` como guardrail contra aliases peligrosos

@tipo: codigo

# TypeScript detecta en compilación mutaciones involuntarias a través de aliases

```typescript
// Sin readonly — el parámetro es un alias del argumento y puede mutarlo
function procesarMal(data: number[]): number[] {
    data.push(99);   // muta el array ORIGINAL del caller — efecto lateral invisible
    return data;
}

// Con readonly — el compilador impide cualquier mutación del objeto recibido
function procesarBien(data: readonly number[]): number[] {
    // data.push(99);
    // ❌ Error: Property 'push' does not exist on type 'readonly number[]'
    return [...data, 99];   // crea un nuevo array — el original queda intacto
}

// Readonly<T> para objetos — protege todas las propiedades de primer nivel
type Config = Readonly<{ host: string; port: number }>;

function conectar(cfg: Config): void {
    // cfg.host = "otro";
    // ❌ Error: Cannot assign to 'host' because it is a read-only property
    console.log(`Conectando a ${cfg.host}:${cfg.port}`);
}
// readonly no impide la existencia del alias — impide la mutación a través de él
```

---

### [F-06] Shallow copy — el alias sobrevive en los niveles anidados

@tipo: codigo

# El spread operator `{...obj}` copia solo el primer nivel — los anidados siguen siendo aliases

```typescript
const original = {
    nombre: "Ana",
    config: { debug: true, retries: 3 },  // objeto anidado
    tags: ["admin", "user"]               // array anidado
};

// Shallow copy con spread: copia los valores del primer nivel
const copia = { ...original };

// Nivel 0: independiente ✅
copia.nombre = "Carlos";
console.log(original.nombre);          // "Ana" — sin cambios ✅

// Nivel 1 (objetos anidados): ALIAS ⚠️
copia.config.debug = false;
console.log(original.config.debug);   // false — original modificado ⚠️

// Nivel 1 (arrays anidados): ALIAS ⚠️
copia.tags.push("guest");
console.log(original.tags);           // ["admin", "user", "guest"] ⚠️

// Comprobación: el config anidado es el mismo objeto
console.log(original.config === copia.config);  // true — mismo L-value ⚠️
```

---

### [F-07] Deep copy con `structuredClone` — ningún nivel queda como alias

@tipo: codigo

# `structuredClone()` es la única forma estándar de obtener una copia completa en ES2022

```typescript
const original = {
    nombre: "Ana",
    config: { debug: true, retries: 3 },
    tags: ["admin", "user"]
};

// Deep copy — ES2022 — copia completa en todos los niveles
const copia = structuredClone(original);

// Nivel 0: independiente ✅
copia.nombre = "Carlos";
console.log(original.nombre);          // "Ana" ✅

// Nivel 1 (objetos): independiente ✅
copia.config.debug = false;
console.log(original.config.debug);   // true ✅ — sin alias

// Nivel 1 (arrays): independiente ✅
copia.tags.push("guest");
console.log(original.tags);           // ["admin", "user"] ✅

// Comprobación: objetos distintos en todos los niveles
console.log(original.config === copia.config);  // false ✅ — L-values distintos
console.log(original.tags === copia.tags);      // false ✅

// Nota: structuredClone no copia funciones, símbolos ni prototipos
// Para esos casos: JSON.parse(JSON.stringify(obj)) (limitado) o librerías como lodash.cloneDeep
```

---

## BLOQUE 2 — Closures: el Entorno que Viaja con la Función

---

### [F-08] ¿Qué es una closure?

@tipo: concepto-abstracto

# Closure = función + entorno léxico capturado en el momento de su creación

## Definición — Sebesta §10, Gabbrielli §7.4

Una **closure** es la combinación de:
1. Una **función** (su código ejecutable)
2. El **entorno léxico** en el que fue definida — el conjunto de nombres y sus valores visibles en ese punto del código fuente

## ¿Por qué existe el concepto?

Sin closures, una función puede acceder solo a:
- Sus propios parámetros (Categoría 2 — stack-dynamic)
- Sus variables locales (Categoría 2 — stack-dynamic)
- Variables globales (Categoría 1 — static)

Con closures, además puede acceder a las **variables del scope exterior** aunque ese scope haya cerrado (de ahí el nombre "closure" — cierre).

## El ciclo de vida extendido

- Las variables **locales ordinarias** viven en el stack — se destruyen cuando la función retorna
- Las variables **capturadas por una closure** no pueden vivir en el stack: deben migrar al **heap**
- Viven mientras **al menos una closure** mantenga una referencia a ellas
- El GC las libera cuando ninguna closure las alcanza — es la Categoría 3 del Tema 09.1

## La conexión con Tema 09.1

- Las closures aplican **deep binding**: el entorno se captura al **crear** la closure, no al llamarla
- Las variables capturadas son exactamente las variables **heap-dynamic implícitas** (Categoría 3)

---

### [F-09] Closure en TypeScript — contador con estado compartido

@tipo: codigo

# El activation record de `crearContador` se destruye, pero `cuenta` sigue viva en el heap

```typescript
function crearContador(inicio: number) {
    // `cuenta` es una variable local — candidata a migrar al heap
    // porque las funciones anidadas la capturan en sus closures
    let cuenta = inicio;

    return {
        incrementar: () => ++cuenta,  // closure 1: captura `cuenta` — lectura y escritura
        decrementar: () => --cuenta,  // closure 2: captura la MISMA `cuenta`
        valor:       () => cuenta     // closure 3: captura `cuenta` — solo lectura
    };
}

const c = crearContador(10);
// crearContador() ya retornó — su activation record fue destruido del stack
// pero `cuenta` sigue viva en el heap porque `c` la referencia

console.log(c.incrementar());  // 11
console.log(c.incrementar());  // 12
console.log(c.decrementar());  // 11
console.log(c.valor());        // 11

// Las tres closures COMPARTEN la misma celda heap de `cuenta`
// Son aliases de la misma variable — pero aliases controlados y encapsulados
```

---

### [F-10] ¿Por qué `cuenta` no se destruye? — ciclo de vida de variables capturadas

@tipo: concepto-abstracto

# La variable capturada migra del stack al heap y vive mientras exista la closure

## Variables locales ordinarias — tiempo de vida de stack

- Se crean cuando se llama a la función (se apila el activation record)
- Viven exactamente mientras la función está ejecutando
- Se destruyen automáticamente cuando la función retorna (se desapila el frame)
- Sin costo de GC — la liberación es inmediata e implícita al desapilar

## Variables capturadas por closure — tiempo de vida de heap

- El compilador o runtime detecta que la variable "escapa" al scope de la función
- La variable **migra al heap** para poder sobrevivir más allá del activation record
- Vive mientras **al menos una closure activa** tenga una referencia a ella
- El GC la libera cuando **ninguna closure** la referencia — lo mismo que cualquier objeto heap

## ¿Qué significa "escapar" al heap?

Una variable "escapa" cuando su lifetime debe ser mayor que el del activation record que la contiene. Esto ocurre cuando:
- Una función anidada la captura (closure)
- Se retorna una referencia a ella
- Se almacena en una estructura de datos con mayor lifetime

## Implicación práctica para el alumno

Si una closure se mantiene viva indefinidamente, **todas las variables que captura** también se mantienen vivas. Una closure que acumula datos puede crecer indefinidamente en memoria — conecta directamente con los conceptos de GC que veremos a continuación.

---

### [F-10b] La closure como solución al problema del dangling reference — Gabbrielli §7.4

@tipo: concepto-abstracto

# ¿Por qué las variables capturadas no pueden vivir en el stack? — la justificación formal de Gabbrielli

## La pregunta que Gabbrielli plantea en §7.4

Cuando una función `F` retorna una función interna `gg` que captura la variable local `x`, surge un conflicto con el ciclo de vida del stack:

> "Cuando el resultado de F() se asigna a gg, la clausura que forma su valor apunta a un entorno que contiene el nombre x. Pero este entorno es local a F y será destruido al terminar su ejecución. ¿Cómo es posible, entonces, invocar gg posteriormente sin producir una referencia colgante a x?"
> — Gabbrielli & Martini §7.4

En C, retornar un puntero a una variable local produce exactamente eso: un **dangling reference** — apunta a stack memory ya reciclada. Es un bug.

## La solución: migración al heap garantizada por el runtime

1. En tiempo de compilación, el compilador detecta que `x` **escapa** del scope de `F` (es capturada por `gg`).
2. `x` se aloja en el **heap** desde el inicio — no en el stack frame de `F`.
3. El closure object `gg` contiene una referencia directa a esa celda heap.
4. Cuando `F` retorna y su stack frame se destruye, `x` en heap **sigue viva**.
5. El GC libera `x` solo cuando ninguna closure la referencie.

## La definición formal de Gabbrielli §7.4

> "Clausuras: las estructuras de datos compuestas por un fragmento de código y un entorno de evaluación, denominadas clausuras, constituyen el modelo canónico para implementar la llamada por nombre y todas aquellas situaciones en que una función debe pasarse como parámetro o retornarse como resultado."
> — Gabbrielli & Martini §7.4

Una closure es un par **(código, entorno)**: el código es el cuerpo de la función; el entorno es la representación del contexto léxico en que fue definida, incluyendo las celdas heap de las variables capturadas.

## La diferencia con C: bug vs. garantía estructural

| | C (sin closures) | TypeScript/Python/Go/Kotlin |
|---|---|---|
| Variable local retornada por referencia | Dangling reference — bug | Imposible — el runtime garantiza heap |
| Detección | Runtime (crash/corrupción silenciosa) | Compile-time (Rust) o runtime-safe (resto) |
| Responsabilidad | El programador | El runtime/compilador |

---

### [F-11] Closure en Python — `nonlocal` para escritura

@tipo: codigo

# Python requiere declarar `nonlocal` explícitamente para escribir en la variable capturada

```python
def crear_acumulador(inicio: int):
    total = inicio   # variable del scope externo — candidata a ser capturada

    def agregar(n: int) -> int:
        nonlocal total    # REQUERIDO para ESCRIBIR en total
                          # sin nonlocal: Python crea una variable LOCAL `total` nueva
                          # y al leerla antes de asignarle → UnboundLocalError
        total += n
        return total

    def obtener() -> int:
        return total      # LECTURA: no necesita nonlocal — solo accede al valor

    return agregar, obtener

agregar, obtener = crear_acumulador(0)
print(agregar(5))   # 5  — total: 0 + 5
print(agregar(3))   # 8  — total: 5 + 3
print(agregar(2))   # 10 — total: 8 + 2
print(obtener())    # 10 — el estado persiste entre llamadas

# crear_acumulador() ya retornó hace rato — `total` sigue viva en heap
```

---

### [F-12] Closures en Go y Kotlin

@tipo: codigo

# Go y Kotlin soportan closures de primera clase — misma semántica de captura que TypeScript

```go
// Go — closure que captura una variable del scope de crearContador
func crearContador(inicio int) func() int {
    cuenta := inicio   // variable local — migra al heap por la closure

    return func() int {
        cuenta++       // captura y modifica cuenta — closure de lectura/escritura
        return cuenta
    }
}

c := crearContador(10)
fmt.Println(c())  // 11
fmt.Println(c())  // 12
// La función retornada "lleva consigo" a cuenta en el heap
```

```kotlin
// Kotlin — lambda que captura una variable del scope externo
fun crearContador(inicio: Int): () -> Int {
    var cuenta = inicio  // var (mutable) porque la lambda necesita modificarla

    return { ++cuenta }  // closure: captura y modifica cuenta en cada llamada
}

val contar = crearContador(10)
println(contar())  // 11
println(contar())  // 12
```

---

### [F-13] C no tiene closures — la limitación por contraste

@tipo: concepto-abstracto

# En C los function pointers no capturan entorno — toda variable no-local debe ser global

## La limitación de C — Gabbrielli §7.4

C permite pasar punteros a funciones, pero esos punteros solo contienen la **dirección de inicio del código**. No existe ninguna estructura de datos para guardar el entorno en el que se definió la función.

## Consecuencias de no tener closures

- Si una función necesita acceder a estado entre llamadas → debe usar **variable global** o una **estructura de datos** pasada manualmente como parámetro extra (`void*` genérico)
- El programador debe gestionar manualmente el ciclo de vida de ese estado
- La composición funcional es posible solo por convención — no hay soporte del lenguaje

## Lo que hace el runtime de lenguajes modernos en lugar del programador

En TypeScript, Python, Go y Kotlin, el runtime detecta automáticamente:
1. Qué variables escapan (son capturadas por closures)
2. Las mueve al heap
3. Les aplica GC cuando ya no son alcanzables

En C, todo ese trabajo recae en el programador. La comparación revela exactamente cuánto valor aporta el runtime de un lenguaje moderno.

## La regla práctica

Si ves código C que simula closures con `static` dentro de una función, tiene el mismo problema que `var` en loops de JavaScript: una sola variable compartida entre todas las "instancias" de la función — no hay forma de tener estado independiente por llamada sin usar estructuras pasadas por parámetro.

---

### [F-14] Deep binding vs. Shallow binding — el contrato de las closures

@tipo: concepto-abstracto

# El momento en que se captura el entorno define completamente el comportamiento de la closure

## Deep binding (binding profundo) — la norma en todos los lenguajes modernos

- El entorno se captura **en el momento de crear la closure**
- Los nombres y sus valores "se congelan" en ese instante
- La closure lleva consigo una referencia al entorno tal como era cuando fue creada
- Comportamiento: **predecible e intuitivo** — la closure siempre ve el entorno de su creación
- Todos los lenguajes modernos usan deep binding: TypeScript, Python, Go, Kotlin, Haskell, Rust

## Shallow binding (binding superficial) — ámbito dinámico

- El entorno se resuelve **en el momento de llamar a la función**, no al crearla
- Los nombres se buscan en la pila de llamadas activa en ese momento
- La misma closure puede dar resultados distintos según dónde se la invoque
- LISP clásico (versiones pre-Scheme) usaba shallow binding con ámbito dinámico
- Prácticamente abandonado por hacer el código muy difícil de razonar

## La implicación práctica para el alumno

Con deep binding, el comportamiento de una closure es **local y cerrado**: depende solo de dónde fue definida en el código fuente, no de cómo llegó la ejecución hasta ella. Eso es exactamente lo que permite razonar sobre el código sin seguir toda la cadena de llamadas.

---

### [F-14b] `makeAdder` — el ejemplo canónico de Sebesta §10.6.4

@tipo: codigo

# Sebesta §10.6.4: dos closures sobre el mismo parámetro — dos celdas heap completamente independientes

```typescript
// Sebesta §10.6.4 — adaptado a TypeScript
// makeAdder captura su parámetro `x` — cada llamada crea una celda heap distinta

const makeAdder = (x: number) => (n: number): number => x + n;
// La función retornada es una closure que captura `x` del scope de makeAdder
// makeAdder se llama dos veces → dos ejecuciones → dos celdas heap para `x`

const add10 = makeAdder(10);   // closure 1: x = 10 en heap — celda A
const add5  = makeAdder(5);    // closure 2: x = 5  en heap — celda B (independiente)

// Cada closure lee su propia celda — sin interferencia:
console.log(add10(1));    // 11 — celda A: x=10, n=1
console.log(add5(7));     // 12 — celda B: x=5,  n=7
console.log(add10(10));   // 20 — celda A sigue siendo x=10
console.log(add5(5));     // 10 — celda B sigue siendo x=5
```

## El análisis de Sebesta

> "La variable x referenciada en la función clausura está ligada al parámetro enviado a makeAdder. La función makeAdder se invoca dos veces: una con el parámetro 10 y otra con el parámetro 5, produciendo dos clausuras diferentes."
> — Sebesta §10.6.4

- Cada llamada a `makeAdder` crea su propio activation record con su propio `x`
- `x` es un **parámetro** — cada invocación genera una celda nueva en heap (binding fresco)
- Las dos closures son **completamente independientes** — no son aliases entre sí

## Contraste con `crearContador` (F-09)

| | `makeAdder` | `crearContador` |
|---|---|---|
| Fuente del valor capturado | Parámetro de la función | Variable local de la función |
| ¿Compartido entre closures? | No — celda nueva por llamada | Sí — las tres closures comparten `cuenta` |
| Mutabilidad del capturado | Inmutable (solo lectura) | Mutable (lectura y escritura) |
| Uso típico | Currificación, partial application | Estado encapsulado, módulo con estado |

---

### [F-15] El bug clásico de `var` en loops — el código problemático

@tipo: codigo

# `var` es función-scope: existe UNA SOLA variable para todo el loop — todas las closures la comparten

```typescript
// var declara una variable en el scope de la FUNCIÓN CONTENEDORA, no del bloque
// Hay exactamente UNA variable `i` para todo el loop
const funcs: (() => number)[] = [];

for (var i = 0; i < 3; i++) {
    funcs.push(() => i);   // TODAS las closures apuntan a la MISMA `i` (deep binding)
                           // pero `i` es una sola celda de memoria — son aliases de ella
}

// En este punto: i === 3 (el loop terminó — i llegó a 3)
// Todas las closures leen la misma celda que ahora contiene 3:
console.log(funcs[0]());   // 3 — esperábamos 0
console.log(funcs[1]());   // 3 — esperábamos 1
console.log(funcs[2]());   // 3 — esperábamos 2

// El deep binding no es el bug — la captura es correcta
// El bug es que var comparte la MISMA celda entre todas las iteraciones
```

---

### [F-16] Corrección con `let` — una variable independiente por iteración

@tipo: codigo

# `let` es block-scope: cada iteración del bloque crea una variable nueva e independiente

```typescript
// let crea una nueva variable `j` en CADA iteración del bloque for
const funcs2: (() => number)[] = [];

for (let j = 0; j < 3; j++) {
    funcs2.push(() => j);   // cada closure captura su PROPIA `j` — celda distinta en heap
}

// Tres variables `j` distintas en el heap — tres closures, tres celdas independientes:
console.log(funcs2[0]());   // 0 ✅ — la j de la iteración 0
console.log(funcs2[1]());   // 1 ✅ — la j de la iteración 1
console.log(funcs2[2]());   // 2 ✅ — la j de la iteración 2

// Alternativa funcional — evita el problema por diseño:
// Array.from crea un nuevo binding `k` por cada elemento — nunca se comparte
const funcs3 = Array.from({ length: 3 }, (_, k) => () => k);
console.log(funcs3[0]());   // 0 ✅
console.log(funcs3[1]());   // 1 ✅
console.log(funcs3[2]());   // 2 ✅

// Regla práctica: en TypeScript moderno, nunca usar var.
// let y const tienen semántica de scope predecible.
```

---

## BLOQUE 3 — Garbage Collection: Memoria Automática

---

### [F-17] El problema de la memoria en heap

@tipo: concepto-abstracto

# El heap no tiene un mecanismo automático de liberación como el stack

## Revisión: categorías de variables y liberación (Tema 09.1)

- **Categoría 1 — static:** el compilador calcula el espacio en compilación, nunca se libera durante la ejecución
- **Categoría 2 — stack-dynamic:** el runtime libera automáticamente al desapilar el activation record
- **Categorías 3 y 4 — heap-dynamic:** alguien debe decidir explícitamente cuándo liberar

## El problema fundamental del heap

En el stack, el "cuándo liberar" está determinado por el control de flujo: cuando la función retorna, el frame se destruye. En el heap, no hay frame. Las celdas se crean con `new`/`malloc` y permanecen hasta que algo las libere.

## El dilema fundamental

- **Liberar demasiado pronto** → dangling pointer: una referencia apunta a memoria ya liberada. Crash o corrupción de datos silenciosa. Los bugs de este tipo son los más difíciles de encontrar.
- **Liberar demasiado tarde** → memory leak: la memoria nunca se recupera. El proceso crece hasta agotar la RAM del sistema.
- **No liberar manualmente** → necesitamos un mecanismo automático: el **Garbage Collector**

## La pregunta que todo GC debe responder

¿Cuándo se puede liberar una celda del heap de forma segura?

Respuesta: cuando **no existe ninguna referencia viva a ella** — es inaccesible desde el programa.

El desafío es detectar esa condición de forma eficiente y correcta sin detener el programa.

---

### [F-18] Cuatro estrategias de gestión de memoria

@tipo: tabla-comparativa

# Estrategias de gestión de memoria — comparación de enfoques

| Estrategia | Quién libera | Cuándo libera | Ejemplos | Problema principal |
|---|---|---|---|---|
| **Manual** | El programador (`free`, `delete`) | Cuando el programador lo decide | C, C++ | Dangling pointers, double-free, memory leaks |
| **Reference Counting** | El runtime (contador por celda) | Cuando el contador cae a 0 | Python, Swift, PHP | No resuelve ciclos de referencia |
| **Mark-and-Sweep** | El GC | Cuando el allocator necesita espacio | Java, JavaScript/V8, Go | Pausa el programa (stop-the-world) |
| **Ownership + Drop** | El compilador (análisis estático) | Al salir del scope — garantía en compilación | Rust | Modelo de programación más restrictivo |

---

### [F-19] Reference Counting — la idea central

@tipo: concepto-abstracto

# Cada celda del heap lleva un contador de cuántas referencias activas la apuntan

## El invariante del algoritmo

```
ref_count(celda) = cantidad de variables/campos que apuntan a esa celda en este momento
```

- Cuando se crea una nueva referencia a la celda → `ref_count += 1`
- Cuando una referencia existente se destruye o se reasigna → `ref_count -= 1`
- Cuando `ref_count == 0` → la celda es inaccesible → **liberar inmediatamente**

## Ventajas del Reference Counting

- **Determinístico**: la liberación ocurre en el instante exacto en que el contador llega a 0
- **Sin stop-the-world**: no hay que pausar el programa para recoger basura
- **Predecible**: en Python, `del x` libera la celda de forma inmediata si no hay otras referencias
- **Localizado**: el costo de GC se distribuye a lo largo del tiempo, no se concentra en un ciclo

## La limitación fundamental

El algoritmo asume que `ref_count == 0` equivale a "inaccesible". Esa equivalencia es verdadera **en ausencia de ciclos**.

Si dos objetos se apuntan mutuamente, sus contadores nunca llegan a 0 aunque el programa no pueda alcanzarlos — son inaccesibles pero el RC no los libera. Es una **fuga de memoria estructural** del algoritmo.

---

### [F-19b] Las ventajas y los dos problemas fundamentales del RC — Sebesta §6.11 + Louden §10.5

@tipo: concepto-abstracto

# Sebesta y Louden coinciden en el diagnóstico: RC y mark-sweep son procesos opuestos, cada uno resuelve lo que el otro no puede

## Las ventajas del RC — Sebesta §6.11.7.1

Sebesta describe el RC como **incremental**: la reclamación ocurre en el instante exacto en que una celda se vuelve inaccesible.

1. **Sin stop-the-world**: no hay ciclo de GC que pause el programa — la liberación se intercala con la ejecución normal.
2. **Determinístico**: el momento de liberación es predecible — útil para recursos con destructores (archivos, sockets, conexiones de red).
3. **Local**: la decisión de liberar la toma cada celda por su propio contador — no se requiere trazar el grafo completo.

## El primer problema: overhead de mantenimiento — Louden §10.5

> "Sin embargo, el costo de mantener los contadores de referencia no es el peor defecto de este esquema."
> — Louden & Lambert §10.5

Cada asignación de referencia requiere dos operaciones: incrementar el contador del nuevo destino y decrementar el del anterior. En bucles tight o estructuras de datos funcionales con muchas copias, este overhead puede ser considerable.

## El segundo problema: ciclos de referencia — Louden §10.5 (el peor defecto)

> "Aún más grave es que las referencias circulares pueden provocar que la memoria sin referencias nunca sea liberada."
> — Louden & Lambert §10.5

Louden ilustra con una lista circular: si el último nodo apunta al primero, al eliminar la referencia externa cada nodo sigue teniendo `ref_count ≥ 1`. Ningún contador llega a cero. La memoria **nunca se libera**.

## El diagnóstico de Sebesta §6.11.7

Sebesta clasifica los problemas como dos polês opuestos:

| Algoritmo | Fortaleza | Debilidad |
|---|---|---|
| Reference Counting | Incremental, determinístico, sin stop-the-world | No resuelve ciclos; overhead por operación |
| Mark-and-Sweep | Resuelve ciclos; sin overhead por operación | Stop-the-world; no incremental (clásico) |

> "Estos dos enfoques de recolección de basura son, en muchos aspectos, procesos opuestos."
> — Sebesta §6.11.7

Los GC modernos (Python, Swift, V8) combinan ambos o hibridan técnicas para capturar las fortalezas de cada uno.

---

### [F-20] Reference Counting — seguimiento del contador en Python

@tipo: codigo

# Python usa RC internamente — `sys.getrefcount` permite observar el contador en tiempo real

```python
import sys

# Crear el objeto: ref_count = 1 (la variable `lista` lo referencia)
lista = [1, 2, 3]
print(sys.getrefcount(lista))   # 2 — getrefcount mismo crea una referencia temporal

# Agregar segunda referencia: ref_count = 2
alias = lista
print(sys.getrefcount(lista))   # 3

# Agregar referencia en una estructura:
contenedor = [lista]
print(sys.getrefcount(lista))   # 4

# Eliminar referencias una a una:
del contenedor           # ref_count → 3
del alias                # ref_count → 2
# En este punto: solo `lista` referencia el objeto → ref_count = 1

del lista
# ref_count → 0 → el runtime libera [1, 2, 3] INMEDIATAMENTE
# No hay que esperar ningún ciclo de GC
# Este es el comportamiento determinístico del RC
```

---

### [F-21] El problema de los ciclos de referencia

@tipo: concepto-abstracto

# Cuando dos objetos se apuntan mutuamente, ningún contador llega a 0 aunque sean inaccesibles

## El escenario del ciclo

Un grafo de objetos donde cada nodo apunta al siguiente, y el último apunta al primero:

```
Estado inicial:
  ref_count(A) = 2  (variable externa `a` + B.siguiente apuntan a A)
  ref_count(B) = 2  (variable externa `b` + A.siguiente apuntan a B)

Se eliminan las variables externas:
  del a  →  ref_count(A) = 1  (B todavía apunta a A — no llega a 0)
  del b  →  ref_count(B) = 1  (A todavía apunta a B — no llega a 0)

El programa ya no puede alcanzar A ni B desde ninguna variable activa.
Son INACCESIBLES. Pero ref_count(A) = 1 y ref_count(B) = 1.
Con RC puro: NUNCA se liberan → MEMORY LEAK permanente.
```

## Por qué es un problema real y frecuente

Las estructuras circulares son muy comunes en la práctica:
- Listas doblemente enlazadas (siguiente y previo)
- Árboles con punteros al nodo padre
- Grafos generales con ciclos
- Objetos de UI con referencias bidireccionales (parent/child)

## Las soluciones adoptadas en los lenguajes reales

Cada lenguaje resuelve esto de forma distinta:
- **Python:** RC + cycle detector separado en el módulo `gc`
- **Swift:** ARC + el programador declara referencias `weak` para romper ciclos manualmente
- **Rust:** el borrow checker **prohíbe** los ciclos mutables en compilación — el problema no puede existir
- **JavaScript/V8:** usa Mark-and-Sweep que detecta ciclos correctamente por diseño

---

### [F-22] Ciclo de referencia en TypeScript — código con nodos mutuamente enlazados

@tipo: codigo

# Dos nodos que se apuntan mutuamente — ciclo que RC puro no podría liberar

```typescript
class Nodo {
    nombre: string;
    siguiente: Nodo | null = null;
    previo:    Nodo | null = null;

    constructor(nombre: string) {
        this.nombre = nombre;
    }
}

// Crear dos nodos con referencias mutuas — ciclo de referencia:
const a = new Nodo("A");
const b = new Nodo("B");

a.siguiente = b;   // A → B   (si usáramos RC: ref_count(B) sube a 2)
b.previo    = a;   // B → A   (si usáramos RC: ref_count(A) sube a 2)

// Si TypeScript/V8 usara RC puro y elimináramos las referencias externas:
//   a = null → ref_count(A) = 1 (B.previo lo apunta)  → no se libera
//   b = null → ref_count(B) = 1 (A.siguiente lo apunta) → no se libera
//   Ambos son inaccesibles pero el RC nunca los liberaría — MEMORY LEAK

// V8 usa Mark-and-Sweep — los detecta como inaccesibles y los libera correctamente ✅
// No se necesitan referencias weak explícitas como en Swift/ARC
```

---

### [F-23] Mark-and-Sweep — la idea general

@tipo: concepto-abstracto

# Marcar todo lo alcanzable desde el programa, liberar todo lo que no se marcó

## El problema que resuelve

Reference Counting no puede detectar ciclos porque razona localmente (contador por objeto). Mark-and-Sweep ignora los contadores y pregunta globalmente: ¿se puede llegar a este objeto desde algún punto activo del programa?

## Las raíces del grafo de objetos

Las raíces son los puntos de entrada desde donde el GC comienza el trazado:
- Variables activas en todos los activation records del stack
- Variables globales del programa
- Registros de la CPU con referencias

## Fase 1 — Mark (Marcar)

A partir de cada raíz, el GC realiza un traversal transitivo del grafo de referencias:
- Si puede llegar a un objeto (directa o transitivamente desde una raíz) → lo **marca como alcanzable**
- Si no puede llegar a él → queda **sin marcar** (será liberado)

## Fase 2 — Sweep (Barrer)

Recorre TODO el heap:
- Celda **marcada** → sigue viva → desmarcarla para el próximo ciclo
- Celda **no marcada** → es inaccesible desde el programa → **liberar**

## La ventaja clave sobre RC

Un ciclo entre A y B que no sea alcanzable desde ninguna raíz queda sin marcar en ambos objetos → ambos se liberan en el sweep. El problema de los ciclos desaparece.

## El costo: stop-the-world

Durante las fases mark y sweep, el programa se pausa. Si el heap es grande, la pausa es perceptible. Los GC modernos (V8, Go) minimizan esta pausa con técnicas incrementales y concurrentes.

---

### [F-23b] Los tres defectos del mark-and-sweep y la compactación como solución — Gabbrielli §8.11

@tipo: concepto-abstracto

# Gabbrielli §8.11 identifica tres defectos estructurales del mark-and-sweep clásico y describe cómo la compactación resuelve uno de ellos

## Defecto 1 — Fragmentación externa (compartido con RC)

> "La técnica de mark-and-sweep padece tres defectos principales. En primer lugar, y esto también es válido para el conteo de referencias, es causa asintótica de fragmentación externa: los objetos vivos y los que ya no lo son se mezclan arbitrariamente en el heap, lo que puede hacer imposible alojar un bloque grande aunque el espacio libre total sea suficiente."
> — Gabbrielli & Martini §8.11

Los objetos vivos y los inaccesibles quedan entremezclados en memoria. La suma de huecos puede ser suficiente para una nueva alocación, pero no hay ningún bloque contiguo disponible.

## Defecto 2 — Stop-the-world (a diferencia de RC)

El algoritmo clásico pausa el programa durante las dos fases. A diferencia del RC (incremental), el mark-and-sweep acumula trabajo y lo ejecuta todo junto. En heaps grandes: pausas de cientos de milisegundos inaceptables para aplicaciones interactivas.

## Defecto 3 — Actualización de punteros tras compactación

Si se añade compactación para resolver la fragmentación, todos los punteros a objetos movidos deben actualizarse. El costo es proporcional al número de referencias en el grafo — potencialmente muy alto.

## La solución a la fragmentación: compactación (Gabbrielli §8.11)

> "Para evitar la fragmentación causada por la técnica mark-and-sweep, se puede modificar la fase de barrido convirtiéndola en una fase de compactación. Los objetos vivos se mueven de modo que queden contiguos, dejando así un bloque contiguo de memoria libre."
> — Gabbrielli & Martini §8.11

```
ANTES (heap fragmentado tras varios ciclos de GC):
  [Obj1][ libre ][ Obj2 ][ libre ][Obj3][ libre ][ libre ]

DESPUÉS DE COMPACTACIÓN (objetos vivos movidos a posiciones contiguas):
  [Obj1][ Obj2 ][Obj3][          LIBRE CONTIGUO          ]

COSTO: actualizar todos los punteros a Obj1, Obj2, Obj3 con sus nuevas direcciones
BENEFICIO: una única zona libre contigua — toda alocación nueva es trivial
```

## Cómo lo resuelve V8 en la práctica

V8 usa **semi-space copying** en el New Space: los objetos vivos se copian al semi-space vacío (“to”), y al terminar los roles se intercambian. El semi-space “from” queda completamente libre en un solo paso. Es compactación sin actualizaciones in-place — a costa de que la mitad del New Space siempre esté reservada como zona de copia.

---

### [F-24] Mark-and-Sweep — trazado del algoritmo sobre un heap de ejemplo

@tipo: codigo

# Seguimiento paso a paso de mark y sweep sobre un heap con ciclo inaccesible

```
Estado inicial del heap — antes del GC:

  Raíces activas:   x → Obj1,   y → Obj3

  Obj1 ─── referencia ──► Obj2
  Obj3                              (sin referencias entre sí)
  Obj4 ─── referencia ──► Obj5
  Obj5 ─── referencia ──► Obj4     ← ciclo: Obj4 ↔ Obj5

  (Obj4 y Obj5 no son alcanzables desde ninguna raíz)

──────────────────────────────────────────────────────────────
FASE MARK — trazado desde las raíces:

  Desde x → Obj1 ✓   (marcado)
    Obj1.ref → Obj2 ✓ (marcado transitivamente)
  Desde y → Obj3 ✓   (marcado)
  Obj4, Obj5: no alcanzables → sin marcar

──────────────────────────────────────────────────────────────
FASE SWEEP — recorrido del heap completo:

  Obj1 ✓ → vivo, desmarcar
  Obj2 ✓ → vivo, desmarcar
  Obj3 ✓ → vivo, desmarcar
  Obj4   → LIBERAR  (inaccesible — aunque forma ciclo con Obj5)
  Obj5   → LIBERAR  (inaccesible — aunque forma ciclo con Obj4)

Estado final del heap: Obj1, Obj2, Obj3 — compactados
El ciclo Obj4 ↔ Obj5 fue liberado correctamente ✅
```

---

### [F-25] GC generacional en V8 — el principio

@tipo: concepto-abstracto

# La mayoría de los objetos mueren jóvenes — el GC puede explotar ese patrón

## La hipótesis generacional

Evidencia empírica en lenguajes con GC: la gran mayoría de los objetos tienen un ciclo de vida muy corto. Son creados para una operación intermedia y luego abandonados: resultados de `map`/`filter`, objetos temporales de request, closures de un solo uso. Pocos objetos sobreviven mucho tiempo.

## La estrategia: dividir el heap en generaciones

En lugar de barrer todo el heap en cada ciclo, dividir el heap en zonas según la "edad" de los objetos:
- **Generación joven (Young Gen / Nursery):** objetos recién creados → GC muy frecuente, sobre un espacio pequeño → muy rápido
- **Generación vieja (Old Gen / Tenured):** objetos que sobrevivieron varios ciclos → GC infrecuente → más costoso pero ocurre raramente

## Promoción de objetos

Un objeto que sobrevive un número configurable de ciclos en la generación joven se **promueve** a la generación vieja. A partir de ese momento ya no es barrido frecuentemente.

## Compactación del heap

Después del sweep en la generación joven, los objetos vivos se **compactan** — se reubican en posiciones contiguas de memoria. Esto elimina la fragmentación del heap y mejora la localidad de caché.

## El resultado práctico

El 90% de los ciclos de GC solo barren la generación joven (unos pocos megabytes) y duran menos de 1 ms. Los ciclos sobre la generación vieja son raros y se pueden ejecutar de forma incremental o concurrente.

---

### [F-26] GC generacional en V8 — estructura del heap

@tipo: codigo

# Layout interno del heap de V8 (Node.js / Chrome / TypeScript compilado a JS)

```
Heap de V8:
┌────────────────────────────────────────────────────────────────┐
│  New Space (Generación joven)                                  │
│  ┌─────────────────────┬─────────────────────┐                 │
│  │  Semi-space "from"  │  Semi-space "to"    │  Scavenger GC   │
│  │  (objetos activos)  │  (espacio libre)    │  frecuente,     │
│  │                     │                     │  muy rápido     │
│  └─────────────────────┴─────────────────────┘                 │
│  Capacidad: ~1-8 MB según configuración                        │
├────────────────────────────────────────────────────────────────┤
│  Old Space (Generación vieja)                                  │
│  ┌───────────────────────────────────────────────────────┐     │
│  │  objetos promovidos — sobrevivieron en New Space      │     │
│  │  Mark-Compact incremental + concurrent               │     │
│  │  Capacidad: cientos de MB — GC infrecuente           │     │
│  └───────────────────────────────────────────────────────┘     │
├────────────────────────────────────────────────────────────────┤
│  Code Space (código JIT compilado)                             │
│  Large Object Space (objetos > 512KB — no se compactan)        │
│  Map Space (descriptores de forma de objetos)                  │
└────────────────────────────────────────────────────────────────┘

Minor GC (Scavenger): evacúa New Space — semi-space copying, muy rápido
Major GC (Mark-Compact): mark + sweep + compact en Old Space — concurrent
```

---

## BLOQUE 4 — Gradual Typing: TypeScript como Caso Paradigmático

---

### [F-27] El espectro del tipado

@tipo: concepto-abstracto

# El tipado no es una dicotomía binaria — existe un espectro continuo entre estático y dinámico

## Tipado estático puro

- Los tipos se verifican **en compilación**, antes de ejecutar el programa
- Si hay un error de tipos → el programa no compila → no puede ejecutarse con ese error
- El programador debe anotar los tipos explícitamente (o el compilador los infiere)
- Ejemplos: Java, C, Haskell, Rust, C++

## Tipado dinámico puro

- Los tipos se verifican **en ejecución**, cuando se ejecuta la operación específica
- El programa compila siempre — los errores de tipos son excepciones en runtime
- No se necesitan anotaciones — el tipo se determina por el valor que tenga la variable en ese momento
- Ejemplos: Python (sin mypy), Ruby, Scheme, Smalltalk, JavaScript puro

## Tipado gradual — la tercera vía

- Permite mezclar: algunas partes tienen tipos estáticos, otras usan `any` (tipo dinámico)
- El programador elige la cobertura según la criticidad de cada módulo o función
- El compilador verifica lo que está tipado, no objeta lo que es `any`
- Ejemplos: TypeScript, Groovy, Dart, Python con mypy, PHP 8+

## La base teórica

El tipado gradual fue formalizado por Jeremy Siek y Walid Taha en 2006. TypeScript lo implementó de forma práctica y a escala industrial — es el caso paradigmático más influyente de la historia reciente del diseño de lenguajes.

---

### [F-27b] El origen académico del gradual typing — Gabbrielli §16.9 y Siek & Taha (2006)

@tipo: concepto-abstracto

# El gradual typing no es solo una característica de TypeScript — es un campo de investigación formal con base teórica rigorosa

## La motivación histórica — Gabbrielli §16.9

> "A medida que el número de proyectos de software de gran escala desarrollados con lenguajes de tipado dinámico creció con el tiempo, los usuarios advirtieron que sacrificar las verificaciones estáticas en favor de la rapidez de prototipado era un trato desfavorable. En el tipado estático, un tipo puede verse como un contrato que tanto el proveedor como el usuario del código deben respetar."
> — Gabbrielli & Martini §16.9

El problema práctico: proyectos en JavaScript o Python crecían hasta cientos de miles de líneas y los beneficios del tipado dinámico quedaban eclipsados por la dificultad de mantener código sin contratos de tipos explícitos.

## La definición formal de Gabbrielli §16.9

> "En el tipado gradual, los usuarios pueden modular la cantidad de información de tipos que proporcionan en sus programas, indicando qué elementos deben verificarse estáticamente y cuáles en tiempo de ejecución."
> — Gabbrielli & Martini §16.9

La palabra clave es **modular**: el programador decide qué partes del código tienen garantías estáticas y qué partes quedan dinámicas.

## La base formal — Siek & Taha (2006)

El artículo "Tipado gradual para lenguajes funcionales" (Siek & Taha, Scheme Workshop, 2006) introdujo:
- Un tipo especial `?` (tipo dinámico) — compatible con cualquier tipo en compilación
- La relación de **consistencia de tipos** (`∼`): `T ∼ ?` para cualquier `T` — más débil que la igualdad de tipos
- **Cast implícito automático**: el compilador inserta verificaciones en los límites entre código tipado y no tipado — si el cast falla en tiempo de ejecución, se lanza una excepción

## Corrección formal del sistema de tipos y TypeScript — Gabbrielli §16.9

Gabbrielli distingue el tipado gradual **formalmente correcto** (las garantías de tipos se preservan completamente en tiempo de ejecución) del enfoque de TypeScript, que es **deliberadamente incompleto**: acepta ciertos programas con potenciales errores de tipo por razones de usabilidad y compatibilidad con JavaScript. Esta decisión de diseño está documentada en la especificación oficial: TypeScript no garantiza la corrección completa del sistema de tipos. El tipo `unknown` (F-30b) es la herramienta más cercana al tipado gradual formalmente correcto que TypeScript ofrece.

---

### [F-28] Tipado estático, dinámico y gradual — comparación

@tipo: tabla-comparativa

# Los tres enfoques de tipado — características clave

| Característica | Estático puro | Dinámico puro | Gradual (TypeScript) |
|---|---|---|---|
| Verificación de tipos | Compilación | Ejecución | Compilación donde hay tipos |
| Error de tipos | No compila | Excepción en runtime | Error de compilación (si hay tipo) |
| Anotaciones | Obligatorias (o inferidas) | No existen (o ignoradas) | Opcionales — elección del programador |
| Escape hatch | No existe | Todo es dinámico | `any` — explícito y auditable |
| Detección de null | En compilación | Runtime crash | Con `strictNullChecks` activado |
| Migración desde JS | No aplica | No aplica | Incremental, archivo por archivo ✅ |
| Adecuado para | Sistemas críticos, equipos grandes | Scripting, prototipado rápido | Proyectos en crecimiento |

---

### [F-29] TypeScript — nivel 0: `any` implícito

@tipo: codigo

# Sin tipos explícitos: TypeScript es compatible con JavaScript puro — sin ninguna garantía

```typescript
// Sin strict mode: TypeScript infiere `any` para parámetros sin anotación
// El código compila — es válido como punto de partida en una migración desde JS

function sumar(a, b) {
    // TypeScript informa: Parameter 'a' implicitly has an 'any' type.
    // (solo con noImplicitAny o strict: true — de lo contrario, silencioso)
    return a + b;   // sin verificación — puede ser número, string, lo que sea
}

sumar(1, 2);         // 3   — comportamiento esperado
sumar("1", 2);       // "12" — concatenación de strings — sin error en compilación
sumar({}, []);       // "[object Object]" — TypeScript no objeta

// Con strict: true en tsconfig.json →
// Error: Parameter 'a' implicitly has an 'any' type.
// Ese error es la señal de que el código necesita anotaciones

// Nivel 0 es el punto de entrada de toda migración JS → TS:
// Renombrar .js → .ts ya es válido en nivel 0, sin cambiar ninguna línea
```

---

### [F-30] TypeScript — nivel 1 y nivel 2: tipos parciales y strict mode

@tipo: codigo

# De cobertura parcial a cobertura total — la migración incremental en acción

```typescript
// ────────────────────────────────────────────
// Nivel 1: tipos en la interfaz pública
// ────────────────────────────────────────────
function sumarSeguro(a: number, b: number): number {
    return a + b;   // el compilador garantiza que a y b son numbers en compilación
}

sumarSeguro(1, 2);      // ✅ 3
// sumarSeguro("1", 2); // ❌ Error: Argument of type 'string' is not assignable to type 'number'

// ────────────────────────────────────────────
// Nivel 2: strict mode — cobertura total
// tsconfig.json: { "compilerOptions": { "strict": true } }
// ────────────────────────────────────────────
// Activa: noImplicitAny, strictNullChecks, strictFunctionTypes,
//         strictBindCallApply, strictPropertyInitialization, noImplicitThis

function buscarUsuario(id: number): string | null {
    if (id === 1) return "Ana";
    return null;    // el return type incluye null — obligatorio declararlo
}

const nombre = buscarUsuario(2);
// Sin strictNullChecks: nombre.toUpperCase() — compila, crash en runtime
// Con strictNullChecks: nombre.toUpperCase() — ❌ Error: 'nombre' is possibly 'null'
console.log(nombre?.toUpperCase() ?? "no encontrado");  // ✅ manejo explícito de null
```

---

### [F-30b] `unknown` vs `any` — el tipo gradual seguro en TypeScript

@tipo: codigo

# `any` desactiva el sistema de tipos; `unknown` lo preserva — dos escape hatches con semánticas opuestas

## La diferencia conceptual

- **`any`**: TypeScript suspende completamente la verificación de tipos. El programador puede hacer cualquier cosa con el valor sin que el compilador objete. Corresponde al tipo dinámico `?` de Siek & Taha pero sin garantías de runtime.
- **`unknown`**: TypeScript sabe que el valor existe pero no conoce su tipo. **Obliga al programador a hacer narrowing antes de cualquier operación** — si no, el compilador rechaza el código.

```typescript
// ─────────────────────────────────────────────────────────────────
// `any` — el compilador no objeta nada — crash en runtime posible
// ─────────────────────────────────────────────────────────────────
function procesarAny(valor: any): string {
    return valor.toUpperCase();    // ✅ para TypeScript — TypeError en runtime si valor es number
    // `any` anula TODAS las garantías del sistema de tipos
}

// ─────────────────────────────────────────────────────────────────
// `unknown` — requiere narrowing antes de cualquier operación
// ─────────────────────────────────────────────────────────────────
function procesarUnknown(valor: unknown): string {
    // return valor.toUpperCase(); // ❌ Error: Object is of type 'unknown'
    if (typeof valor === "string") {
        return valor.toUpperCase();  // ✅ — narrowed a string
    }
    if (typeof valor === "number") {
        return valor.toFixed(2);     // ✅ — narrowed a number
    }
    return String(valor);            // ✅ — String() funciona con cualquier tipo
}

// ─────────────────────────────────────────────────────────────────
// Uso canónico de `unknown`: datos externos y catch blocks
// ─────────────────────────────────────────────────────────────────
async function fetchJSON(url: string): Promise<unknown> {
    const r = await fetch(url);
    return r.json();   // unknown: no sabemos qué estructura retorna el servidor
    // El caller DEBE hacer narrowing — correcto por diseño del sistema de tipos
}

// Desde TypeScript 4.0: el bloque catch usa `unknown` por defecto (opción de compilador: useUnknownInCatchVariables)
try {
    JSON.parse("datos-invalidos");
} catch (e: unknown) {
    // e.message;          // ❌ Error: Object is of type 'unknown'
    if (e instanceof Error) {
        console.log(e.message);  // ✅ — narrowed a Error
    }
}
```

## La regla práctica en proyectos con `strict: true`

| Situación | Tipo recomendado | Motivo |
|---|---|---|
| Migración gradual desde JS | `any` (transitorio) | Compatibilidad — marcar con TODO |
| Datos de red / JSON.parse / catch | `unknown` | Fuerza verificación antes de uso |
| Interop con librerías sin types | `any` con cast documentado | No hay alternativa |
| Cualquier otro caso | Tipo concreto o union type | Sin escape hatch |

---

### [F-31] Type Narrowing — ¿qué es y por qué existe?

@tipo: concepto-abstracto

# TypeScript refina el tipo de una variable en cada rama del control de flujo

## El problema que resuelve

Un union type como `string | number | null` permite que una variable sea cualquiera de esos tipos. Pero para usar `toUpperCase()`, necesitamos saber que es `string`. Para usar `toFixed()`, que es `number`. Sin verificar, el compilador (con strict) rechaza el código.

## ¿Qué es el type narrowing?

Es el proceso por el cual TypeScript **estrecha** (narrows) el tipo de una variable dentro de cada rama de control de flujo, basándose en las condiciones que se verificaron en las ramas anteriores.

## Los guardas de tipo más comunes en TypeScript

- `typeof x === "string"` → en esa rama, TypeScript sabe que x es `string`
- `x === null` → en esa rama, TypeScript sabe que x es `null`
- `x instanceof Clase` → en esa rama, TypeScript sabe que x es `Clase`
- `"propiedad" in x` → TypeScript sabe que x tiene esa propiedad
- Narrowing exhaustivo con `switch` + `default: never` → el compilador detecta casos faltantes

## La garantía formal

Dentro de cada rama del narrowing, TypeScript garantiza estáticamente que el tipo es el esperado — no es necesario hacer cast. Si se agrega un nuevo caso al union type y no se actualiza el código, el compilador lo detecta.

## La conexión con los aliases

Type narrowing es el mecanismo que permite usar union types de forma segura — transforma en error de compilación lo que sin strict sería un crash en runtime, potencialmente difícil de reproducir.

---

### [F-32] Type Narrowing con `typeof` e `instanceof`

@tipo: codigo

# TypeScript restringe el tipo en cada rama — los métodos disponibles cambian según la rama

```typescript
type Resultado = string | number | null;

function formatear(r: Resultado): string {
    if (r === null) {
        return "—";             // aquí TypeScript sabe: r es null — ✅
    }
    if (typeof r === "number") {
        return r.toFixed(2);    // aquí TypeScript sabe: r es number — ✅
        //     ^ r.toUpperCase() daría error — number no tiene ese método
    }
    return r.toUpperCase();     // aquí TypeScript sabe: r es string (único tipo restante) — ✅
    // Si olvidáramos la rama de null → r podría ser null aquí → error de compilación
}

// instanceof — para clases con herencia
class Perro { ladrar()  { return "Guau"; } }
class Gato  { maullar() { return "Miau"; } }

function hacerSonido(animal: Perro | Gato): string {
    if (animal instanceof Perro) {
        return animal.ladrar();  // Perro en esta rama ✅
    }
    return animal.maullar();     // Gato: único tipo restante ✅
}
```

---

### [F-33] Type Narrowing exhaustivo con `switch` y el patrón `never`

@tipo: codigo

# El compilador detecta en compilación si falta un caso al agregar un nuevo tipo al union

```typescript
type Forma = "círculo" | "cuadrado" | "triángulo";

function área(f: Forma, lado: number): number {
    switch (f) {
        case "círculo":
            return Math.PI * lado ** 2;
        case "cuadrado":
            return lado ** 2;
        case "triángulo":
            return (Math.sqrt(3) / 4) * lado ** 2;
        default:
            // Si el tipo Forma creciera: "círculo" | "cuadrado" | "triángulo" | "rectángulo"
            // y olvidáramos agregar el case "rectángulo":
            // TypeScript llega aquí con f: "rectángulo" — NO es never
            // El cast a never fuerza el error de compilación:
            const _exhaustive: never = f;
            //    ^^^^^^^^^^^^^^^^^^^^^^^^^
            // Error: Type '"rectángulo"' is not assignable to type 'never'
            throw new Error(`Forma no manejada: ${String(_exhaustive)}`);
    }
    // Con este patrón: agregar un caso al tipo sin actualizar el switch → error inmediato en IDE
}
```

---

### [F-34] Gradual typing en proyectos grandes — impacto real

@tipo: tabla-comparativa

# TypeScript en producción — qué cambia en cada nivel de cobertura

| Aspecto | JavaScript puro | TypeScript gradual | TypeScript strict |
|---|---|---|---|
| Detección de errores de tipo | Solo en runtime | En compilación (partes tipadas) | En compilación (todo) |
| Refactoring seguro | Muy difícil — puede romper silencioso | Parcialmente seguro | Seguro — el compilador verifica |
| Migración desde JS | No aplica | Incremental — archivo por archivo ✅ | Requiere cobertura total previa |
| Null crashes | Muy frecuentes | Reducidos donde hay tipos | Eliminados con strictNullChecks |
| Tiempo de detección | Runtime en producción | Build en CI | IDE en tiempo real |
| Adecuado para equipo | Pequeño y ágil | En crecimiento | Grande o sistema crítico |

---

## BLOQUE 5 — Variables en Programación Funcional

---

### [F-35] Variables en FP puro — sin mutabilidad

@tipo: concepto-abstracto

# En el paradigma funcional puro no existen variables mutables — solo bindings definitivos

## El contraste fundamental — Sebesta §5.8, Gabbrielli §11

**En LP imperativos (C, Java, TypeScript imperativo):**
- Las variables son **celdas de memoria mutables** con un L-value y un R-value
- La asignación `x = 5` es una operación **destructiva**: sobreescribe el R-value de la celda en la dirección L-value
- El mismo nombre puede tener distintos valores en distintos momentos de la ejecución

**En LP funcionales puros (Haskell, Erlang, Clojure):**
- No existen variables mutables — existen **bindings**
- Un binding es una asociación nombre → valor, **definitiva dentro de su scope**
- No hay L-value modificable: `x = 5` no asigna a una celda, declara que `x` es `5` en ese scope
- Una vez establecido, el binding no puede cambiar

## La computación como reescritura de expresiones

En FP puro, computar no significa "modificar el estado de celdas de memoria". Significa **reescribir expresiones** hasta obtener un valor. El resultado es idéntico sin importar cuántas veces se evalúe la expresión — esto se llama **transparencia referencial**.

## Por qué esto importa

- Sin estado mutable → sin efectos laterales → sin aliases peligrosos por definición
- El razonamiento ecuacional funciona: si `f(x) = 10`, entonces cualquier `f(x)` en el programa puede reemplazarse por `10` sin cambiar el comportamiento
- Las funciones son predecibles: su resultado depende **solo** de sus argumentos, nunca del estado externo

---

### [F-35b] Transparencia referencial — la definición formal y sus consecuencias

@tipo: concepto-abstracto

# Sebesta §7.4 y Louden §9.1 definen la propiedad formal que hace razonable el código funcional

## La definición de Sebesta §7.4

> "Un programa tiene la propiedad de transparencia referencial si dos expresiones cualesquiera con el mismo valor pueden sustituirse mutuamente en cualquier punto del programa sin afectar su comportamiento."
> — Sebesta §7.4

## La definición equivalente de Louden §9.1 — la regla de sustitución

> "Dos expresiones cualesquiera en un programa que tengan el mismo valor pueden reemplazarse mutuamente en cualquier lugar del programa sin alterar el resultado."
> — Louden & Lambert §9.1

Ambas dicen lo mismo: el valor de una expresión depende **solo de sus partes**, nunca de cuándo ni cuántas veces se evalúe.

## La conexión con los efectos laterales — Sebesta §7.4

> "Como los lenguajes funcionales puros no tienen variables, los programas escritos en ellos son referencialmente transparentes. Las funciones en un lenguaje funcional puro no pueden tener estado, que de otro modo estaría almacenado en variables locales."
> — Sebesta §7.4

Un **efecto lateral** es toda modificación que una función realiza sobre algo fuera de su entorno local: variables globales, parámetros mutables, archivos, I/O. La transparencia referencial **implica** la ausencia de efectos laterales y viceversa.

## Las consecuencias formales

1. **Razonamiento ecuacional**: si `f(x) = 10`, entonces `f(x)` puede sustituirse por `10` en cualquier parte del programa — sin sorpresas por estado externo.
2. **Memoización válida**: el compilador puede cachear `f(5) = 25` y no recalcularlo. Solo es válido si `f` es referencialmente transparente.
3. **Reordenamiento seguro**: el compilador puede evaluar `f(a)` y `g(b)` en cualquier orden si ambas son puras. Habilita optimizaciones y paralelismo.
4. **Pruebas aisladas**: una función pura se prueba completamente con sus argumentos — sin setup de estado global, sin teardown.

## La conexión con aliases (Bloque 1 de esta clase)

Los aliases sobre objetos mutables rompen la transparencia referencial:
- Si `a` y `b` son aliases del mismo objeto mutable y `f(a)` modifica ese objeto,
- entonces `f(b)` después de `f(a)` produce un resultado diferente aunque `a === b`.
- `f` ya no es función de su argumento — es función del estado del heap.

La inmutabilidad (Bloque 5) elimina esta categoría de problemas **por diseño**: si los objetos no se pueden mutar, los aliases son inofensivos.

---

### [F-36] Haskell — el binding es definitivo

@tipo: codigo

# En Haskell no existe "reasignar" — la computación es declaración de relaciones, no modificación

```haskell
-- En Haskell, `let x = 5` declara que x ES 5 en este scope — no que x TIENE el valor 5
let x = 5       -- x está vinculado a 5 para siempre en este scope
-- x = 6        -- ILEGAL: no existe el concepto de reasignación
                -- Error: Multiple declarations of 'x'

-- La "iteración" en FP no usa un contador mutable — usa recursión con binding fresh:
sumaLista :: [Int] -> Int
sumaLista []     = 0                     -- caso base: lista vacía → 0
sumaLista (x:xs) = x + sumaLista xs     -- x es un binding nuevo en cada llamada recursiva
                                         -- no es la misma celda modificada — es un binding diferente

-- Versión con fold — sin ninguna variable mutable explícita:
suma = foldl (+) 0 [1, 2, 3, 4, 5]     -- suma = 15

-- En Haskell, si quisieras "cambiar" el valor de x necesitarías un binding nuevo:
let y = x + 1  -- y está vinculado a 6 — x sigue siendo 5
               -- no es "x = x + 1" — es un nombre completamente nuevo
```

---

### [F-37] `val` vs. `var` — Scala y Kotlin

@tipo: codigo

# Scala y Kotlin distinguen explícitamente entre binding inmutable y variable mutable

```scala
// Scala — dos palabras clave, dos semánticas completamente distintas

val y = 5    // val: binding inmutable — como const en TypeScript
             // no puede reasignarse — el compilador lo garantiza

var x = 5    // var: variable mutable — como let en TypeScript
             // puede reasignarse libremente

x = 10       // ✅ válido — x es var
// y = 10   // ❌ Error: reassignment to val — el compilador rechaza esto

// En estilo funcional en Scala: siempre val, salvo que la mutación sea necesaria
// val comunica intención: "este valor no va a cambiar después de este punto"
```

```kotlin
// Kotlin — misma distinción, misma semántica

val inmutable = 42    // binding definitivo — no puede reasignarse
var mutable   = 42    // variable mutable — puede reasignarse

mutable = 100         // ✅
// inmutable = 100    // ❌ Val cannot be reassigned

// Para colecciones: la inmutabilidad también existe en el tipo
val lista     = listOf(1, 2, 3)        // lista inmutable — no se puede agregar ni quitar
val listaMut  = mutableListOf(1, 2, 3) // lista mutable — permite push, remove, etc.
```

---

### [F-38] TypeScript funcional — `reduce` vs. loop imperativo

@tipo: codigo

# El estilo funcional evita la mutación explícita usando transformaciones de datos en cadena

```typescript
const numeros = [1, 2, 3, 4, 5];

// ────────────────────────────────────────────
// Estilo imperativo — muta el acumulador en cada iteración
// ────────────────────────────────────────────
let suma = 0;
for (const x of numeros) {
    suma += x;   // suma cambia su valor (R-value) en cada iteración
                 // suma es una variable en el sentido imperativo: L-value modificable
}
console.log(suma);   // 15

// ────────────────────────────────────────────
// Estilo funcional — solo bindings nuevos, sin mutación visible
// ────────────────────────────────────────────
const sumaFuncional = numeros.reduce((acc, x) => acc + x, 0);
// En cada llamada al callback: acc y x son parámetros nuevos (bindings fresh)
// No hay ninguna variable que se mute — hay una cadena de aplicaciones de función
console.log(sumaFuncional);   // 15

// Transformación completa en cadena — sin estado mutable en ningún paso:
const resultado = [1, 2, 3, 4, 5]
    .filter(x => x % 2 === 0)    // [2, 4] — nuevo array, el original no cambia
    .map(x => x * 10)             // [20, 40] — nuevo array
    .reduce((a, b) => a + b, 0);  // 60 — binding final
// Cada transformación produce un valor nuevo — ningún paso modifica el anterior
```

---

### [F-39] `Readonly<T>` y objetos inmutables en TypeScript

@tipo: codigo

# TypeScript provee herramientas de compilación para garantizar inmutabilidad en objetos

```typescript
// Readonly<T> — el compilador impide cualquier mutación de las propiedades del objeto
type ConfigApp = Readonly<{
    host: string;
    port: number;
    debug: boolean;
}>;

const cfg: ConfigApp = { host: "localhost", port: 3000, debug: false };
// cfg.debug = true;
// ❌ Error: Cannot assign to 'debug' because it is a read-only property

// ReadonlyArray<T> — array inmutable: no se puede push, pop ni asignar por índice
const COLORES: ReadonlyArray<string> = ["rojo", "verde", "azul"];
// COLORES.push("amarillo");  // ❌ Property 'push' does not exist on type 'readonly string[]'
// COLORES[0] = "naranja";    // ❌ Index signature only permits reading

// as const — convierte literales en tipos inmutables ultra-estrictos
const LIMITES = { min: 0, max: 100 } as const;
// LIMITES.min = -1;
// ❌ Cannot assign to 'min' because it is a read-only property
// Tipo inferido: { readonly min: 0; readonly max: 100 } — los valores son literales exactos

// Object.freeze() — inmutabilidad en runtime
const frozen = Object.freeze({ retries: 3 });
// frozen.retries = 5;  // TypeError en runtime en modo strict del motor JS
```

---

### [F-40] ¿Por qué la inmutabilidad reduce bugs?

@tipo: concepto-abstracto

# La inmutabilidad elimina la categoría más común de bugs de estado en programas grandes

## El origen del problema con el estado mutable compartido

En programas imperativos con objetos mutables compartidos:
- Una función puede modificar un objeto que otras partes del código asumen estable
- El bug puede aparecer lejos en el código del lugar donde ocurrió la modificación — difícil de rastrear
- En pruebas: las pruebas que pasan en aislamiento pueden fallar cuando se ejecutan en conjunto
- En concurrencia: dos threads que mutan el mismo objeto sin sincronización producen resultados no determinísticos

## La garantía que aporta la inmutabilidad

- Si un objeto es inmutable, **no puede haber aliases peligrosos**: cualquier referencia al objeto siempre ve el mismo valor
- No es necesario sincronizar accesos concurrentes — los datos nunca cambian
- Las funciones puras son aisladas: su resultado depende solo de sus argumentos, puede probarse sin importar el estado del resto del sistema

## La conexión con closures

Una closure sobre un binding inmutable es **inherentemente segura**:
- La closure puede leer el valor capturado — siempre el mismo
- No puede modificarlo → no puede producir efectos sobre el estado del caller
- Facilita la composición: `f(g(x))` no tiene sorpresas si `g` no muta `x`

## FP en TypeScript — el espectro práctico

TypeScript no es un LP puramente funcional. Pero permite adoptar un estilo funcional donde tiene sentido: `const` + `Readonly<T>` + `ReadonlyArray` + `reduce`/`map`/`filter` en lugar de loops con mutación. El resultado es código más predecible sin sacrificar expresividad.

---

## BLOQUE 6 — Contraste Multilenguaje: Gestión de Memoria Moderna

---

### [F-41] Cuatro lenguajes, cuatro estrategias de memoria

@tipo: tabla-comparativa

# Estado del arte en gestión de memoria — comparación 2026

| Aspecto | TypeScript / V8 | Python | Go | Rust |
|---|---|---|---|---|
| Estrategia de GC | GC generacional (Scavenger + Mark-Compact concurrent) | RC + cycle detector | GC concurrent tricolor incremental | Ownership + Drop — sin GC en runtime |
| Dangling pointer | Imposible (GC gestiona todo) | Imposible (GC gestiona todo) | Imposible (GC gestiona todo) | Imposible — borrow checker en compilación |
| Variable no inicializada | Error en compilación (strict) | `NameError` en runtime | Zero value automático | Error en compilación |
| Alias de objeto | Referencia implícita — invisible al programador | Referencia implícita — invisible al programador | Puntero explícito con `*` y `&` | Borrow controlado por el compilador |
| Ciclos de referencia | V8 Mark-Sweep los resuelve | Módulo `gc` cycle detector | GC concurrente los resuelve | Imposibles (mutables) — borrow checker |
| Pausa del programa | Minor GC <1ms / Major GC variable-incremental | RC incremental — impacto bajo | GC concurrent <1ms objetivo | Sin GC → sin pausa |

---

### [F-42] Rust: ownership — la idea central

@tipo: concepto-abstracto

# Rust garantiza seguridad de memoria sin GC en runtime mediante análisis estático en compilación

## El problema que Rust resuelve

- **C/C++:** seguros si el programador los usa correctamente. El compilador no ayuda. Dangling pointers, use-after-free y double-free son frecuentes y costosos.
- **Java / TypeScript / Go:** usan GC — seguros, pero con overhead en runtime y pausas impredecibles.
- **Rust:** elige una tercera vía: el compilador hace en tiempo de compilación el trabajo que el GC haría en runtime.

## El sistema de ownership

- Cada valor tiene **un único dueño** (owner) en cada momento de la ejecución
- Cuando el dueño sale del scope, el valor se destruye automáticamente (**Drop trait** — destructores determinísticos)
- La propiedad puede **transferirse** (move): el dueño anterior ya no puede usar el valor
- La propiedad puede **prestarse** (borrow): referencias temporales que el compilador verifica

## Las reglas del borrow checker — garantías en compilación

1. Puede haber **cualquier cantidad de referencias inmutables** (`&T`) al mismo tiempo (lectura compartida segura)
2. O puede haber **exactamente una referencia mutable** (`&mut T`) — pero no simultáneamente con referencias inmutables
3. Las referencias no pueden **vivir más tiempo** que el valor al que apuntan (no hay dangling references)

## El resultado

Sin GC en runtime → sin pausas → rendimiento predecible. Sin dangling pointers → verificado por el compilador, no por pruebas en runtime.

---

### [F-43] Rust — el borrow checker en acción

@tipo: codigo

# El compilador detecta errores de memoria que en C serían bugs silenciosos o crashes

```rust
// Drop automático — el compilador inserta la destrucción al salir del scope
fn nueva_sesion(id: u32) -> Vec<String> {
    let datos: Vec<String> = Vec::new();
    datos   // move: ownership transferido al caller — datos NO se destruye aquí
}           // si datos no se transfiriera, se destruiría aquí automáticamente (Drop)

// Dangling reference — error de compilación (en C sería un crash o corrupción):
fn referencia_invalida() {
    let referencia: &String;
    {
        let s = String::from("hola");
        referencia = &s;      // borrow de s — referencia vive mientras viva s
    }                         // s sale de scope → Drop → s destruida
    // println!("{}", referencia);
    // ❌ Error: `s` does not live long enough
    // Rust detecta en compilación que referencia apuntaría a memoria liberada
    // En C, esto compilaría y produciría comportamiento indefinido en runtime
}

// Move semantics — el compilador rastrea dónde está cada valor:
let v1 = vec![1, 2, 3];
let v2 = v1;              // ownership de v1 transferido a v2 (move)
// println!("{:?}", v1);  // ❌ Error: value borrowed here after move
println!("{:?}", v2);     // ✅ v2 es el único dueño
```

---

## BLOQUE 7 — Bloque IA: Aliases, Closures y Type Narrowing

---

### [F-44] IA Pattern 1 — el LLM genera un alias donde debería ir una copia

@tipo: codigo

# Prompt: "guardá una copia de config antes de modificarla" — la IA usa asignación simple

```typescript
// ❌ Código generado por IA — INCORRECTO:
// La IA asigna directamente: el "backup" es un alias, no una copia

const configBackup = config;    // NO es copia — es alias del mismo objeto heap
configBackup.debug = true;      // modifica config también — el backup es inútil

console.log(config.debug);      // true — el "original" fue modificado

// Por qué la IA comete este error:
// El LLM fue entrenado con mucho código JavaScript donde
// la asignación de objetos es común y la distinción copia/alias
// no siempre está explícita en el nombre de la variable
```

---

### [F-45] IA Pattern 1 — cómo detectar y corregir el alias invisible

@tipo: codigo

# Tres señales de alerta en código IA y las dos correcciones según la profundidad del objeto

```typescript
// ─────────────────────────────────────────────────────────────────
// Señales de que el código IA podría generar un alias no deseado:
// ─────────────────────────────────────────────────────────────────
// 1. const backup = objeto                   → alias (sin duda)
// 2. const copia = { ...objeto }             → alias en sub-objetos anidados
// 3. const arr = Array.from(originalArr)     → alias en cada elemento objeto
// 4. const arr2 = [...originalArr]           → alias en cada elemento objeto

// ─────────────────────────────────────────────────────────────────
// Corrección 1 — Shallow copy: cuando no hay propiedades de tipo objeto anidadas
// ─────────────────────────────────────────────────────────────────
const configBackup1 = { ...config };   // nivel 0 independiente — nivel 1+ sigue siendo alias

// ─────────────────────────────────────────────────────────────────
// Corrección 2 — Deep copy: cuando hay objetos o arrays anidados (ES2022)
// ─────────────────────────────────────────────────────────────────
const configBackup2 = structuredClone(config);  // todos los niveles son independientes

// Verificación rápida de independencia:
console.log(config === configBackup1);                   // false ✅ — nivel 0 distinto
console.log(config.nested === configBackup1.nested);     // true ⚠️  — nivel 1 sigue siendo alias
console.log(config === configBackup2);                   // false ✅
console.log(config.nested === configBackup2.nested);     // false ✅ — deep copy real
```

---

### [F-46] IA Pattern 2 — el LLM usa `var` en loops con closures

@tipo: codigo

# Prompt: "generá 5 funciones que retornen su índice" — la IA usa var y el resultado es siempre 5

```typescript
// ❌ Código generado por IA — INCORRECTO:
// Patrón frecuente en código LLM entrenado con JavaScript pre-ES6 o con código legacy

const funcs = [];
for (var i = 0; i < 5; i++) {
    funcs.push(() => i);   // TODAS las closures capturan la MISMA celda de memoria
                           // var es función-scope: i vive en el scope de la función contenedora
                           // no se crea una `i` nueva en cada iteración — hay una sola
}

// En este punto i === 5 (el loop terminó)
// Todas las closures leen la misma celda que ahora contiene 5:
console.log(funcs[0]());  // 5 — esperábamos 0
console.log(funcs[1]());  // 5 — esperábamos 1
console.log(funcs[4]());  // 5 — esperábamos 4

// El deep binding capturó correctamente la REFERENCIA a `i`
// El bug es que var hace que esa referencia sea compartida por todas las iteraciones
```

---

### [F-47] IA Pattern 2 — corrección con `let` y con estilo funcional

@tipo: codigo

# `let` block-scope y `Array.from` funcional son las dos soluciones correctas

```typescript
// ─────────────────────────────────────────────────────────────────
// Corrección 1: let — crea una variable j nueva en cada bloque de iteración
// ─────────────────────────────────────────────────────────────────
const funcs2: (() => number)[] = [];
for (let j = 0; j < 5; j++) {
    funcs2.push(() => j);   // cada closure captura su propia j — celda distinta en heap
}
// Cinco variables `j` distintas — cinco closures, cinco celdas independientes:
console.log(funcs2[0]());  // 0 ✅
console.log(funcs2[4]());  // 4 ✅

// ─────────────────────────────────────────────────────────────────
// Corrección 2: estilo funcional — el problema nunca existe con parámetros
// ─────────────────────────────────────────────────────────────────
// Array.from llama al callback con un parámetro `k` nuevo en cada invocación
// Los parámetros son bindings fresh — no se comparten entre llamadas
const funcs3 = Array.from({ length: 5 }, (_, k) => () => k);
console.log(funcs3[0]());  // 0 ✅
console.log(funcs3[4]());  // 4 ✅

// Alternativa con map sobre un array de índices:
const funcs4 = [0, 1, 2, 3, 4].map(k => () => k);
console.log(funcs4[0]());  // 0 ✅
// El parámetro `k` de cada llamada al callback es siempre un binding nuevo
```

---

### [F-48] IA Pattern 3 — código sin narrowing que puede crashear en runtime

@tipo: codigo

# Prompt: "función que formatee un string o number" — la IA aplica métodos de string sin verificar

```typescript
// ❌ Código generado por IA — INCORRECTO:
// El LLM asume que el argumento siempre será string aunque el tipo diga string | number

function formatear(valor: string | number): string {
    return valor.toUpperCase();
    //           ^^^^^^^^^^^^
    // ❌ TypeScript strict: Property 'toUpperCase' does not exist on type 'string | number'.
    //                       Property 'toUpperCase' does not exist on type 'number'.
}

// Por qué es peligroso en producción:
// - Sin strict mode o con `any`: el código compila sin advertencia
// - En runtime: TypeError: valor.toUpperCase is not a function
//   cuando se pasa un número — crash en producción

// Por qué la IA lo genera así:
// El LLM infiere del nombre de la función que suele recibir strings
// y aplica el método sin verificar — replica el patrón más común en los ejemplos de training
```

---

### [F-49] IA Pattern 3 — narrowing correcto y exhaustivo

@tipo: codigo

# TypeScript verifica en compilación que todos los tipos del union están cubiertos correctamente

```typescript
// ✅ Con narrowing — el compilador verifica cada rama:
function formatear(valor: string | number): string {
    if (typeof valor === "string") {
        return valor.toUpperCase();  // aquí: valor es string ✅ — .toUpperCase() existe
    }
    return valor.toFixed(2);         // aquí: valor es number ✅ — .toFixed() existe
    // TypeScript verifica que todos los tipos del union están cubiertos
}

// ─────────────────────────────────────────────────────────────────
// Switch exhaustivo con never — atrapa tipos agregados al union que se olvidan en el switch:
// ─────────────────────────────────────────────────────────────────
type Color = "rojo" | "verde" | "azul";

function codigoHex(c: Color): string {
    switch (c) {
        case "rojo":  return "#FF0000";
        case "verde": return "#00FF00";
        case "azul":  return "#0000FF";
        default:
            // Si se agrega "amarillo" al tipo Color y se olvida en el switch:
            // TypeScript llega aquí con c: "amarillo" — no es never
            // → Error: Type '"amarillo"' is not assignable to type 'never'
            // → El IDE lo marca en rojo de inmediato, antes de correr cualquier test
            const _never: never = c;
            throw new Error(`Color no manejado: ${String(_never)}`);
    }
}
```

---

## PREGUNTAS Y CIERRE

---

### [F-50] Pregunta socrática — ¿closure útil o fuga de memoria?

@tipo: socratica

# ¿Esta closure es un diseño correcto o una fuga de memoria encubierta?

```typescript
function registrarEventos(nombre: string) {
    const historial: string[] = [];   // crece sin límite con cada llamada

    return (evento: string) => {
        historial.push(evento);
        console.log(`[${nombre}] ${historial.length} eventos registrados`);
    };
}

const logApp = registrarEventos("App");
// logApp se mantiene viva durante toda la sesión
// historial crece con cada llamada a logApp(...)
```

## Para discutir en clase

- ¿En qué condiciones este diseño es correcto y útil?
- El GC puede liberar `historial`... ¿en qué condición exacta?
- Si `logApp = null`, ¿qué pasa con `historial` y con el string `nombre`?
- ¿Cómo refactorizar para limitar el crecimiento del historial (ej: solo últimos 100 eventos)?
- ¿Es esto un bug o es intencional? ¿Cómo saberlo sin ver el código que crea `logApp`?

---

### [F-51] Cierre — síntesis de la clase

@tipo: cierre

# Aliases · Closures · GC · Gradual Typing · Bindings FP

## Lo que vimos hoy

- **Aliases:** dos nombres, una celda de memoria. Fuentes: asignación de referencia, parámetros por referencia (tres escenarios de Sebesta §9.5), union types. Consecuencias en verificación formal y concurrencia. `readonly` como guardrail. Shallow copy con spread, deep copy con `structuredClone`.
- **Closures:** función + entorno léxico capturado (Gabbrielli §7.4: “pair code/environment”). Solución al dangling reference: migración al heap garantizada por el runtime. Deep binding: el entorno se congela al crear la closure. Ejemplo canónico de Sebesta: `makeAdder` (Sebesta §10.6.4). `let` crea celda nueva por iteración — `var` comparte una sola.
- **GC:** Reference Counting (incremental, determinístico; falla con ciclos — Louden §10.5). Mark-and-Sweep (resuelve ciclos; tres defectos de Gabbrielli §8.11: fragmentación, stop-the-world, actualización de punteros). Compactación como solución. V8 generacional: Scavenger + Mark-Compact. Rust: ownership sin GC.
- **Gradual Typing:** motivación histórica (Gabbrielli §16.9). Base formal: Siek & Taha 2006. `any` vs `unknown`: el tipo gradual seguro. Type narrowing: TypeScript estrecha el tipo en cada rama del control de flujo. TypeScript: intencionalmente unsound.
- **FP:** bindings inmutables. Transparencia referencial: definición formal Sebesta §7.4 + Louden §9.1. La inmutabilidad elimina los aliases peligrosos por diseño.

## Conexiones hacia adelante

- **Tema 10 — Tipos de Datos:** union types y discriminated unions — construyen directamente sobre type narrowing
- **Tema 11 — FP:** los bindings inmutables y la transparencia referencial son el fundamento del paradigma funcional puro
- **Tema 14 — Sistemas de Tipos:** TypeScript como gradual typing, inferencia de tipos, strict mode en profundidad

## Próxima clase

Tema 10 — Tipos de Datos: escalares, estructurados, uniones discriminadas y sistemas de tipos formales.
