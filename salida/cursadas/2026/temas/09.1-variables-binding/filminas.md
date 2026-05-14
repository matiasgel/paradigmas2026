# Filminas — Tema 09.1: Variables, Binding y Ámbito

> **Agente:** Dr. Roberto ✍️ — Class Writer
> **Fecha:** 2026-05-14
> **Revisión:** 2026-05-14 (v2 — separación código/teoría, sin imágenes generadas)
> **Tema:** 09.1 — Variables, Binding y Ámbito
> **Duración:** 120 min (1 clase)
> **Lenguaje principal:** TypeScript
> **Fuente:** diseno.md — Lic. Marcos 🗂️
> **Estado:** 🔲 Borrador — pendiente de revisión docente

---

## PORTADA

---

### [F-00] Portada

@tipo: portada
@imagen: none

# Variables, Binding y Ámbito

Paradigmas y Lenguajes de Programación — Clase 09.1
Universidad Nacional de Tierra del Fuego — Instituto IDEI · 2026

---

## BLOQUE 1 — Variable como Abstracción

---

### [F-01] Von Neumann: el origen de la variable

@tipo: concepto-abstracto
@imagen: none

# La arquitectura Von Neumann es la base de toda variable

## Dos componentes fundamentales

- **Memoria:** colección de celdas numeradas — cada celda tiene una **dirección** (su posición física) y un **contenido** (el valor almacenado)
- **Procesador:** lee y escribe celdas usando instrucciones de máquina; opera siempre sobre direcciones numéricas

## El problema que resuelven los lenguajes de programación

- En lenguaje máquina el programador trabaja con **direcciones numéricas** como `0x7fff5b20`
- Esto es propenso a errores, ilegible y dependiente del hardware específico
- Los lenguajes introducen una capa de **abstracción**: reemplazan las direcciones físicas por **nombres simbólicos**

## La variable como abstracción de celda

- Una variable **nombra** una dirección de memoria — el programador escribe `x` en lugar de `0x7fff5b20`
- El compilador o runtime decide qué celda real usar — el programador no necesita saberlo
- La **sentencia de asignación** (`x = 42`) corresponde a la operación de escritura destructiva del procesador

## ¿Por qué "destructiva"?

- Escribir en una celda **destruye** el valor anterior — no hay historial automático
- La inmutabilidad (`const`, `val`, `let` en Rust) es una restricción artificial del **lenguaje**, no del hardware

---

### [F-02] La abstracción en capas

@tipo: tabla
@imagen: none

# Los lenguajes ocultan la celda de memoria detrás de la variable

## Correspondencia entre el hardware y el lenguaje

| Elemento concreto (hardware) | Abstracción en el lenguaje |
|---|---|
| Celda de memoria física | Variable |
| Dirección numérica de la celda | Nombre / identificador (`x`, `contador`, `limite`) |
| Escritura destructiva de la celda | Sentencia de asignación (`x = 42`) |
| Múltiples celdas contiguas | Variable de tipo compuesto (array, struct, objeto) |
| Celda de solo-lectura | Variable constante (`const`, `val`) |

## Lo que el compilador/runtime hace por nosotros

- Asignar y liberar celdas de memoria (gestión del binding de almacenamiento)
- Traducir el nombre simbólico a la dirección real en cada acceso
- Verificar que el uso del nombre es consistente con el tipo declarado

---

### [F-03] Los seis atributos de una variable

@tipo: tabla
@imagen: none

# Una variable no es solo un nombre — tiene seis atributos interdependientes

## Sebesta §5.3 — formalización en 5-tupla extendida

| Atributo | Notación | Descripción |
|---|---|---|
| **Nombre** | — | Identificador simbólico; puede no existir (variable anónima como `_` en Python) |
| **Dirección** | L-value | Celda(s) de memoria asociada(s); puede cambiar en recursión (múltiples frames) |
| **Tipo** | — | Rango de valores + operaciones legales + representación binaria en memoria |
| **Valor** | R-value | Contenido codificado almacenado según el tipo; puede ser indefinido |
| **Tiempo de vida** | lifetime | Período durante el que la variable está vinculada a una dirección de memoria |
| **Ámbito** | scope | Rango de instrucciones donde el nombre es visible y puede ser referenciado |

## La 5-tupla canónica (condensada)

Algunos textos agrupan tiempo de vida con ámbito y lo expresan como:
`Variable = <nombre, dirección, tipo, L-valor, R-valor>`

Cada atributo se **vincula** en un momento distinto — eso es el **binding**.

---

### [F-04] L-value y R-value — el doble rol de una variable

@tipo: concepto-abstracto
@imagen: none

# Una variable puede aparecer como destino o como fuente de datos

## Los dos roles en una sentencia de asignación

- **L-value** (Left value): la variable aparece como **destino** de la asignación
  - Representa la **dirección de memoria** donde se almacenará el resultado
  - El compilador necesita saber *dónde* escribir
  - Ejemplo: `x` en `x = y + 1` — necesitamos la dirección de x

- **R-value** (Right value): la variable aparece como **fuente** de datos
  - Representa el **contenido** almacenado en la celda
  - El compilador necesita saber *qué valor* leer
  - Ejemplo: `y` en `x = y + 1` — necesitamos el valor de y

## Regla general

- En el **lado izquierdo** de `=`: la variable actúa como L-value (dirección)
- En el **lado derecho** de `=`: la variable actúa como R-value (contenido)
- Una variable **siempre tiene L-value** mientras exista en memoria
- Una variable **tiene R-value válido** solo si fue inicializada

## ¿Qué pasa con las constantes?

- `const PI = 3.14` tiene L-value (la celda donde está almacenado el 3.14)
- Pero el lenguaje **prohíbe usarla como L-value** en una nueva asignación
- `PI = 2.71` → error de compilación, no error de hardware

---

### [F-05] L-value y R-value — código TypeScript

@tipo: codigo
@imagen: none

# En `x = y`: x denota dirección (L-value), y denota contenido (R-value)

```typescript
let contador: number = 42;
//  ↑ nombre   ↑ tipo    ↑ R-value inicial (contenido: 42)
//  dirección (L-value) asignada por el runtime — invisible al programador
//  ámbito: el bloque donde está declarado

let resultado: number;

resultado = contador + 1;
//  ↑ L-value: dirección de resultado (destino de escritura)
//              ↑ R-value: contenido de contador (fuente de lectura)

// Lo que hace el runtime paso a paso:
//   1. Leer contenido de la celda contador  → 42
//   2. Sumarle 1                              → 43
//   3. Escribir 43 en la celda resultado
```

---

### [F-06] L-value y R-value — código Python

@tipo: codigo
@imagen: none

# Python expone el L-value con id() — muestra la dirección real del objeto

```python
contador = 42

# id() devuelve la dirección del objeto en el heap de Python
print(id(contador))     # ej: 140234567890  ← L-value (dirección)
print(type(contador))   # <class 'int'>      ← tipo vinculado en runtime
print(contador)         # 42                 ← R-value (contenido)

# Reasignación: Python crea un NUEVO objeto, no modifica el existente
contador = 43
print(id(contador))     # ← DIFERENTE al anterior: nueva celda, nueva dirección
# El objeto 42 sigue existiendo hasta que el GC lo recolecte

# Comparar con un objeto mutable:
lista = [1, 2, 3]
id_original = id(lista)
lista.append(4)
print(id(lista) == id_original)  # True — misma dirección, contenido modificado
```

---

### [F-07] La 5-tupla — TypeScript y Kotlin

@tipo: codigo
@imagen: none

# Los mismos atributos, distintas políticas de mutabilidad

```typescript
// TypeScript — tipo estático, dirección gestionada por el runtime
let x: number = 42;
//  nombre: x
//  tipo:   number (vinculado en compilación)
//  valor:  42 (R-value inicial)
//  dirección: asignada por V8 en tiempo de carga (no visible)
//  ámbito: bloque donde está declarado

const limite: number = 100;
//  binding de VALOR inmutable: el lenguaje prohíbe re-asignar limite
//  pero la celda de memoria sigue existiendo (tiene L-value)
```

```kotlin
// Kotlin — var (mutable) vs val (inmutable de valor)
var contador: Int = 42
//  var → el binding de valor puede cambiar: se puede re-asignar

val limite: Int = 100
//  val → binding de valor inmutable desde la creación
//  equivalente a TypeScript const para tipos primitivos
```

---

### [F-08] La 5-tupla — Rust y Go

@tipo: codigo
@imagen: none

# Rust expone el L-value; Go asigna zero-values automáticamente

```rust
// Rust — el L-value (dirección) es visible con punteros raw
let x = 42i32;
//  tipo inferido: i32
//  binding de almacenamiento: stack, liberado al salir del scope

let addr = &x as *const i32;
//  addr contiene la dirección física de x en el stack
//  esto es el L-value de x expuesto como dato del programa

// La inmutabilidad en Rust es la regla por defecto:
// let x = 42;      ← inmutable (por defecto)
// let mut y = 42;  ← mutable (requiere declaración explícita)
```

```go
// Go — zero values: toda variable tiene un valor inicial seguro
var n int       // n = 0  (nunca hay basura, nunca hay undefined)
var s string    // s = ""
var b bool      // b = false
var p *int      // p = nil

// Go NUNCA deja una variable con valor "basura"
// Esto elimina una clase entera de bugs de C/C++
```

---

## BLOQUE 2 — Binding: el momento de la vinculación

---

### [F-09] ¿Qué es el Binding?

@tipo: concepto-abstracto
@imagen: none

# Binding: la asociación entre una entidad y uno de sus atributos

## Sebesta §5.4 — definición formal

Un **binding** es la asociación entre una entidad del programa (variable, operador, identificador, etc.) y uno de sus atributos (tipo, valor, dirección, significado), establecida en un **momento determinado**.

## Tres preguntas clave sobre cualquier binding

1. **¿Qué** se está vinculando? (el atributo — tipo, valor, dirección...)
2. **¿Cuándo** ocurre la vinculación? (el momento — compilación, ejecución...)
3. **¿Es permanente o puede cambiar?** (inmutable vs. reasignable)

## ¿Por qué importa el momento del binding?

- **Binding temprano** (en compilación): más eficiente en ejecución, el compilador detecta errores antes de correr el programa; menos flexible para ciertos patrones
- **Binding tardío** (en ejecución): más flexible, permite duck typing y estructuras genéricas; costo en overhead y errores silenciosos en runtime

## El momento determina dónde se detectan los errores

- Un error de tipo con binding en compilación → **falla antes de ejecutar** (el compilador avisa)
- Un error de tipo con binding en ejecución → **falla mientras el usuario usa la app**

---

### [F-10] Los 6 tiempos de binding

@tipo: tabla
@imagen: none

# El binding puede ocurrir en 6 momentos distintos del ciclo de vida del programa

## Sebesta §5.4 — tabla de tiempos de vinculación

| Momento | ¿Qué se vincula? | Ejemplo concreto |
|---|---|---|
| **Diseño del lenguaje** | Significados posibles para símbolos y estructuras | `*` = multiplicación (no concatenación) |
| **Implementación del compilador** | Rango de valores de tipos primitivos | `number` en TS = IEEE 754 float64, 64 bits |
| **Compilación** | Variable → tipo; operador → semántica concreta | `let n: number` → n es float64 |
| **Linkeo** | Llamada a subprograma externo → código real | `console.log` → función de V8 runtime |
| **Carga del módulo** | Variables globales/estáticas → celdas de memoria | Variables de módulo al importar |
| **Ejecución** | Variable → valor concreto | `n = n + 5` (el valor cambia en runtime) |

## Lo que importa recordar

- Los tres primeros momentos son **pre-ejecución**: errores detectables antes de correr
- Linkeo y carga son **preparación del entorno de ejecución**
- Solo el último momento ocurre **dentro del programa en marcha**

---

### [F-11] Los 6 tiempos — análisis de un fragmento TypeScript

@tipo: codigo
@imagen: none

# Dos líneas de código activan cinco momentos de binding simultáneos

```typescript
let count: number;   // declaración — binding de tipo en compilación
count = count + 5;   // asignación — binding de valor en ejecución
```

```
Análisis de bindings en el fragmento:

Tipos posibles para variables     → DISEÑO DEL LENGUAJE (TypeScript spec)
  El lenguaje define qué tipos existen y qué operaciones son válidas.

Tipo de count (number)            → COMPILACIÓN
  El compilador vincula el identificador count con el tipo number.

Rango de valores de number        → IMPLEMENTACIÓN DEL COMPILADOR
  IEEE 754 float64: ±5×10⁻³²⁴ a ±1.8×10³⁰⁸ (64 bits).

Significado del operador +        → COMPILACIÓN
  Se resuelve la sobrecarga: number + number = suma numérica.

Representación del literal 5      → DISEÑO DEL COMPILADOR
  El compilador decide cómo representar el literal 5 en bytecode.

Valor de count                    → EJECUCIÓN (runtime)
  Solo cuando la línea se ejecuta, count toma el valor calculado.
```

---

## BLOQUE 3 — Binding de Tipos

---

### [F-12] Binding de tipos — estático vs. dinámico

@tipo: tabla-comparativa
@imagen: none

# ¿Cuándo se vincula el tipo de una variable?

## Dimensión 1: el momento del binding de tipo

| Característica | **Binding estático** | **Binding dinámico** |
|---|---|---|
| **Momento de vinculación** | Compilación (o declaración) | Ejecución — en cada asignación |
| **¿Puede cambiar el tipo?** | No — el tipo queda fijo para esa variable | Sí — puede ser `int`, luego `str` |
| **Detección de errores de tipo** | En compilación — antes de ejecutar | En runtime — cuando el programa corre |
| **Rendimiento** | Alto — sin costo extra en ejecución | Menor — el runtime verifica tipos en cada op |
| **Flexibilidad** | Menor — el tipo debe conocerse antes | Mayor — útil para scripting y DSLs |
| **Ejemplos de lenguajes** | TypeScript, Kotlin, Go, Rust, Java | Python, JavaScript, Ruby, Lua |

## Nota sobre TypeScript

TypeScript tiene binding estático (tipo fijo en compilación), pero compila a JavaScript (binding dinámico). El tipado de TS **desaparece en runtime** — solo existe en el código fuente y en el compilador.

---

### [F-13] Binding de tipos — fuerte vs. débil

@tipo: tabla-comparativa
@imagen: none

# ¿Qué tan estricto es el sistema al mezclar tipos incompatibles?

## Dimensión 2: la fuerza del tipado (ortogonal al momento)

| Característica | **Tipado fuerte** | **Tipado débil** |
|---|---|---|
| **Conversiones implícitas** | No — o solo conversiones "seguras" y predecibles | Sí — coerciones arbitrarias en cualquier operación |
| **Comportamiento ante mezcla** | Error explícito (compilación o excepción en runtime) | Resultado silencioso posiblemente incorrecto |
| **Trazabilidad de bugs** | Alta — el error aparece cerca de la causa real | Baja — el error aparece lejos de donde está el problema |
| **Ejemplos de lenguajes** | Haskell, Rust, Python, TypeScript strict | C (muchas coerciones), JavaScript, PHP |

## Las dos dimensiones son ortogonales — se combinan en cuatro formas

| | Fuerte | Débil |
|---|---|---|
| **Estático** | TypeScript, Java, Kotlin, Rust | C (tipos fijos, muchas coerciones) |
| **Dinámico** | Python (tipo cambia, sin coerciones silenciosas) | JavaScript (tipo cambia Y hay coerciones) |

---

### [F-14] Inferencia de tipos — concepto

@tipo: concepto-abstracto
@imagen: none

# El compilador deduce el tipo sin que el programador lo declare explícitamente

## ¿Qué es la inferencia de tipos?

- Es la capacidad del compilador de **deducir el tipo de una expresión** a partir de su contexto
- El programador no declara el tipo — el compilador lo determina en compilación
- El binding de tipo sigue ocurriendo en compilación (tipado **estático**) — solo cambia quién lo declara

## Dos formas de inferencia

- **Unidireccional (flujo hacia adelante):** el tipo se deduce del valor asignado
  - `const items = [1, 2, 3]` → el compilador infiere `number[]`
- **Bidireccional (contextual):** el tipo se deduce del contexto donde se usa el valor
  - `items.forEach(x => x.toFixed(2))` → `x` se infiere como `number` por el tipo de `items`

## Ventajas e implicaciones

- **Menos verbosidad** sin perder los beneficios del tipado estático
- El compilador puede **rechazar código incorrecto** aunque no haya anotaciones de tipo
- Si la inferencia falla por ambigüedad, el compilador pide una anotación explícita

## Diferencia fundamental con tipado dinámico

- La inferencia es **en compilación** — no hay overhead en runtime
- El tipo **no cambia** durante la ejecución una vez inferido
- En tipado dinámico el tipo se determina en runtime y puede cambiar libremente

---

### [F-15] Inferencia de tipos — TypeScript

@tipo: codigo
@imagen: none

# TypeScript infiere tipos en compilación — no requiere declaraciones explícitas

```typescript
// Inferencia simple: el tipo se deduce del valor inicial
const items = [1, 2, 3];
//    ↑ inferido: number[]  (el compilador analiza el array literal)

const first = items[0];
//    ↑ inferido: number  (acceso indexado a number[] devuelve number)

const total = items.reduce((acc, x) => acc + x, 0);
//    ↑ inferido: number  (el acumulador inicial 0 determina el tipo)

// Inferencia bidireccional (contextual):
items.forEach(x => {
//            ↑ x: number — inferido por el tipo de items (number[])
    console.log(x.toFixed(2));   // ✅ toFixed existe en number
    // console.log(x.length);    // ❌ Error: number no tiene .length
    //   el compilador detecta el error sin anotación explícita
});
```

---

### [F-16] Binding dinámico de tipo — Python

@tipo: codigo
@imagen: none

# En Python el tipo se vincula en cada asignación — puede cambiar completamente

```python
# Python: binding dinámico — el tipo se determina en runtime

x = [2, 3, 4]
print(type(x))          # <class 'list'>
print(id(x))            # ej: 140234567890

# Reasignación: x pasa a ser str — el tipo cambió completamente
x = "uno, dos, tres"
print(type(x))          # <class 'str'>
print(id(x))            # ← DIFERENTE: nuevo objeto en heap

# Python ES fuertemente tipado: no permite operaciones incompatibles sin conversión
x + 42          # TypeError: can only concatenate str (not "int") to str
                # el error aparece en runtime, no en compilación

# Para mezclar, se requiere conversión explícita:
x + str(42)     # ✅  → "uno, dos, tres42"
int("5") + 42   # ✅  → 47
```

---

### [F-17] Coerciones — JavaScript (tipado débil)

@tipo: codigo
@imagen: none

# JavaScript convierte tipos automáticamente — los resultados son contraintuitivos

```javascript
// JavaScript realiza coerciones implícitas sin avisar

// + con string: el número se convierte a string (concatenación)
"5" + 3      // → "53"   (number 3 → string "3" → concatenación)
"5" + true   // → "5true"

// - siempre es aritmético: el string se convierte a number
"5" - 3      // → 2      (string "5" → number 5 → resta)
"5" * 2      // → 10

// == hace coerciones, === no
0 == false   // → true   (false se convierte a 0)
0 === false  // → false  (sin coerción, tipos diferentes)
"" == false  // → true
null == undefined   // → true   (caso especial del estándar)
null === undefined  // → false

// Los casos más famosos:
[] + []      // → ""
[] + {}      // → "[object Object]"
{} + []      // → 0  (en algunos contextos de evaluación)
```

---

### [F-18] Coerciones — TypeScript strict y Python

@tipo: codigo
@imagen: none

# TypeScript strict y Python rechazan la mezcla de tipos incompatibles

```typescript
// TypeScript strict — error de compilación al mezclar tipos
const a: string = "5";
const b: number = 3;

a + b;
// Error TS2365: Operator '+' cannot be applied to types 'string' and 'number'
// El error aparece en el editor, antes de ejecutar cualquier código

// Si queremos concatenar, la conversión debe ser explícita:
a + b.toString();   // ✅  → "53"  (conversión explícita, intención clara)
String(b) + a;      // ✅  → "35"
```

```python
# Python (dinámico + fuerte) — excepción explícita en runtime
"5" + 3
# TypeError: can only concatenate str (not "int") to str
# Python no silencia el error — lo convierte en excepción inmediata

# La conversión debe ser explícita (igual que TypeScript):
"5" + str(3)    # ✅  → "53"
int("5") + 3    # ✅  → 8
```

---

## BLOQUE 4 — Binding de Almacenamiento

---

### [F-19] Las 4 categorías de variables

@tipo: tabla
@imagen: none

# El tiempo de vida y el mecanismo de almacenamiento definen cuatro categorías

## Sebesta §5.4.3 — cuatro categorías según binding de almacenamiento

| Categoría | ¿Cuándo se vincula la dirección? | ¿Cuándo se libera? | Zona de memoria | ¿Permite recursión? |
|---|---|---|---|---|
| **1 — Estáticas** | Antes de ejecutar el programa | Al terminar el programa | Segmento estático | ❌ |
| **2 — Stack-dynamic** | Al activar el subprograma | Al retornar del subprograma | Pila de llamadas | ✅ |
| **3 — Heap explícitas** | Al ejecutar `new` / `Box::new` | Al ejecutar GC / `drop` | Heap | ✅ |
| **4 — Heap implícitas** | En cualquier sentencia de asignación | Al ejecutar GC | Heap | ✅ |

## ¿Por qué las estáticas no permiten recursión efectiva?

- En Cat. 1, todas las llamadas a la misma función **comparten la misma celda de memoria**
- Si una función se llama a sí misma, la segunda llamada sobreescribe los valores de la primera
- Las invocaciones no pueden coexistir con variables independientes — no hay frames separados

---

### [F-20] Categoría 1 — Variables estáticas — concepto

@tipo: concepto-abstracto
@imagen: none

# Las variables estáticas existen desde el inicio del programa hasta el final

## Características

- Su dirección de memoria es **conocida en tiempo de compilación**
- La celda se reserva **antes de que el programa empiece** y no se libera hasta que termina
- No hay overhead de allocate/deallocate en cada llamada a función

## Cuándo usar variables estáticas

- **Constantes del módulo**: valores que no cambian durante toda la ejecución
- **Configuración**: parámetros cargados al inicio que aplican a todo el módulo
- **Cache / estado compartido**: valores que deben persistir entre llamadas a la misma función

## La restricción de recursión

- En C, FORTRAN y otros lenguajes con asignación estática para locales, la función no puede llamarse a sí misma de forma útil
- Cada llamada trabaja con **la misma celda** de memoria para sus variables locales
- FORTRAN 77 prohíbe la recursión directamente por esta razón

## En lenguajes modernos

- TypeScript, Python, Java, Go y Kotlin usan Cat. 2 (stack-dynamic) para las variables locales
- La estática existe para variables de módulo, constantes globales y `companion object` en Kotlin

---

### [F-21] Categoría 1 — Variables estáticas — TypeScript

@tipo: codigo
@imagen: none

# En TypeScript, las variables de módulo tienen binding de almacenamiento estático

```typescript
// Variables de módulo: binding de almacenamiento antes de ejecución
const VERSION = "1.0.0";      // constante estática — dirección fija desde carga
let sesionesActivas = 0;       // variable estática mutable — existe todo el tiempo de vida

// Patrón de inicialización lazy (una sola vez en toda la vida del módulo):
let _cache: Map<string, string> | null = null;

export function getCache(): Map<string, string> {
    // _cache se inicializa la primera vez que se llama a getCache()
    // Las llamadas siguientes reutilizan la misma instancia (misma celda)
    _cache ??= new Map();
    return _cache;
}

// Traza de ejecución:
//   1ra llamada: _cache === null → se crea el Map → _cache apunta al Map
//   2da+ llamada: _cache !== null → se devuelve el mismo Map
//
// Si getCache() fuera recursiva, _cache podría verse en estado parcial
// desde las invocaciones intermedias — ese es el problema de Cat. 1 + recursión
```

---

### [F-22] Categoría 1 — Kotlin companion object

@tipo: codigo
@imagen: none

# En Kotlin, el companion object es el espacio estático de la clase

```kotlin
class Sesion private constructor(val id: Int) {

    companion object {
        // companion object = espacio estático de la clase Sesion
        // Sus propiedades y funciones existen desde que la clase se carga

        private var contadorGlobal = 0   // estática — un binding por toda la JVM

        fun nueva(): Sesion {
            contadorGlobal++             // modifica la celda compartida por todos
            return Sesion(contadorGlobal)
        }

        fun totalSesiones(): Int = contadorGlobal
    }
}

// Uso:
val s1 = Sesion.nueva()           // id = 1, contadorGlobal = 1
val s2 = Sesion.nueva()           // id = 2, contadorGlobal = 2
println(Sesion.totalSesiones())   // 2 — contadorGlobal es la misma celda para todos
```

---

### [F-23] Categoría 2 — Stack-dynamic — concepto

@tipo: concepto-abstracto
@imagen: none

# Las variables stack-dynamic se crean al entrar al subprograma y se destruyen al salir

## Características

- El **binding de almacenamiento** ocurre cuando el subprograma es llamado (no antes)
- Una nueva celda de memoria se reserva en la **pila de llamadas** (call stack)
- Al retornar del subprograma, la celda se **libera automáticamente**

## Por qué son la norma en lenguajes modernos

- **Sin gestión manual de memoria**: el sistema controla el ciclo de vida
- **Sin basura**: la celda se libera exactamente cuando ya no se necesita
- **Sin interferencia entre llamadas**: cada llamada tiene sus propias celdas

## La pila de llamadas (call stack)

- Estructura LIFO (Last In, First Out): la última función en llamarse es la primera en retornar
- Cada llamada agrega un **frame** (registro de activación) con las variables locales
- Los frames no se comparten — cada invocación tiene los suyos propios

## ¿Por qué permiten recursión?

- Cada llamada recursiva genera un **frame nuevo** en la pila
- Las variables de diferentes invocaciones coexisten en frames distintos, sin interferencia
- No importa que sea la misma función — si hay frame propio, hay variables propias

---

### [F-24] Categoría 2 — Stack-dynamic — código TypeScript

@tipo: codigo
@imagen: none

# Cada llamada a calcular() crea sus propias variables locales en la pila

```typescript
function calcular(n: number): number {
    // Al entrar a calcular(): se reservan dos celdas en la pila
    let resultado = 0;   // celda propia de ESTA llamada
    let temp = n * 2;    // celda propia de ESTA llamada

    console.log(`temp = ${temp}`);
    return resultado + temp;
    // Al retornar: las celdas de resultado y temp son DESTRUIDAS
    // Si se llama calcular() otra vez, se crean nuevas celdas (nuevas direcciones)
}

// Estas dos llamadas son completamente independientes:
calcular(5);   // crea sus propias celdas: resultado=0, temp=10
calcular(7);   // crea sus propias celdas: resultado=0, temp=14

// No hay interferencia entre las dos invocaciones:
// la temp de calcular(5) y la temp de calcular(7) son celdas diferentes
```

---

### [F-25] Categoría 2 — por qué la recursión es posible

@tipo: concepto-abstracto
@imagen: none

# La pila de llamadas apila frames independientes — esa es la clave

## Lo que ocurre en factorial(3)

Cuando el programa llama `factorial(3)`, la pila crece así:

```
PILA DE LLAMADAS:
  ┌─────────────────────┐  ← tope (más reciente)
  │ factorial(1)        │    n = 1  (su propia celda)
  ├─────────────────────┤
  │ factorial(2)        │    n = 2  (su propia celda)
  ├─────────────────────┤
  │ factorial(3)        │    n = 3  (su propia celda)
  ├─────────────────────┤
  │ main / llamador     │
  └─────────────────────┘  ← base
```

## El proceso paso a paso

1. `factorial(3)` se llama → **push** del frame con `n = 3`
2. Llama a `factorial(2)` → **push** del frame con `n = 2`
3. Llama a `factorial(1)` → **push** del frame con `n = 1`
4. `factorial(1)` retorna 1 → **pop** del frame de `factorial(1)`
5. `factorial(2)` recibe 1, calcula `2 * 1 = 2`, retorna 2 → **pop**
6. `factorial(3)` recibe 2, calcula `3 * 2 = 6`, retorna 6 → **pop**

## Para Tema 13

Los detalles internos del frame — static link, dynamic link, dirección de retorno — se estudian en Abstracción Procedural.

---

### [F-26] Categoría 2 — factorial recursivo — código

@tipo: codigo
@imagen: none

# Cada llamada tiene su propia copia de n en su propio frame

```typescript
function factorial(n: number): number {
    // CADA llamada a factorial() tiene su propia celda para n
    // La n de factorial(3) y la n de factorial(2) son celdas distintas

    if (n <= 1) return 1;   // caso base: retorna, libera el frame

    return n * factorial(n - 1);
    //     ↑ usa la n de ESTE frame
    //         ↑ crea un NUEVO frame para n-1
}

console.log(factorial(3));  // 6

// Traza de ejecución:
//   factorial(3): espera a factorial(2)
//     factorial(2): espera a factorial(1)
//       factorial(1): n <= 1 → retorna 1 (sin llamada recursiva más)
//     factorial(2): recibe 1, calcula 2*1=2, retorna 2
//   factorial(3): recibe 2, calcula 3*2=6, retorna 6
```

---

### [F-27] Categorías 3 y 4 — Heap — concepto

@tipo: concepto-abstracto
@imagen: none

# El heap almacena objetos de ciclo de vida controlado, no ligado al flujo del programa

## ¿Qué es el heap?

- Región de memoria donde los objetos pueden **sobrevivir más allá del subprograma** que los creó
- A diferencia de la pila, el ciclo de vida del objeto no está ligado al flujo de llamadas
- El programador o el runtime decide cuándo liberar la memoria

## Categoría 3 — Heap explícita

- El programador solicita la memoria explícitamente (`new`, `Box::new`, `malloc`)
- La liberación puede ser:
  - **Automática (GC):** Java, TypeScript, Python, Go → el runtime detecta cuando no hay referencias
  - **Manual:** C → `free()` explícito — riesgo de memory leaks y use-after-free
  - **Ownership:** Rust → el compilador determina cuándo liberar, sin GC y sin errores

## Categoría 4 — Heap implícita

- **Toda** asignación puede cambiar el tipo, el valor Y la dirección del objeto
- El binding de almacenamiento ocurre en cada asignación, sin que el programador lo solicite
- Ejemplo canónico: Python — cualquier reasignación crea un nuevo objeto en el heap

## Trade-offs

| | Heap explícita | Heap implícita |
|---|---|---|
| **Control del programador** | Alto | Bajo |
| **Riesgo de error** | Memory leaks (sin GC) | Menor |
| **Flexibilidad del tipo** | Moderada | Máxima |

---

### [F-28] Categoría 3 — Heap explícita — TypeScript y Rust

@tipo: codigo
@imagen: none

# TypeScript usa GC; Rust usa ownership — ambos son heap explícita

```typescript
// TypeScript: new crea el objeto en el heap; el GC lo libera automáticamente
class Nodo {
    constructor(
        public valor: number,
        public siguiente: Nodo | null = null
    ) {}
}

let cabeza = new Nodo(42);
// cabeza → Nodo(42) en el heap  (nueva dirección)

cabeza = new Nodo(99);
// cabeza → Nodo(99) en el heap  (nueva dirección)
// Nodo(42) ya no tiene referencias → el GC lo recolectará
// El programador no necesita liberar memoria manualmente
```

```rust
// Rust: drop() automático al salir del scope — sin GC, determinístico
fn main() {
    let elemento = Box::new(42i32);
    // elemento → valor 42 en el heap (Box gestiona la dirección)

    println!("{}", elemento);  // 42

}  // fin del scope → destructor de Box se llama automáticamente
   // la memoria se libera AQUÍ, sin GC, sin memory leak posible
```

---

### [F-29] Categoría 4 — Heap implícita — Python

@tipo: codigo
@imagen: none

# En Python, toda asignación puede cambiar tipo, valor y dirección simultáneamente

```python
# Python: heap implícita — cada asignación puede cambiar todos los atributos

x = [1, 2, 3]
print(type(x), id(x))     # <class 'list'>  140234567890

x = "uno, dos, tres"
print(type(x), id(x))     # <class 'str'>   140234567999  ← todo cambió
#  ↑ tipo cambió:   list → str
#  ↑ dirección cambió: nueva celda en el heap
#  ↑ valor cambió:  [1,2,3] → "uno, dos, tres"

x = 42
print(type(x), id(x))     # <class 'int'>   140234568100

# El objeto [1,2,3] anterior quedó sin referencias
# El GC de Python lo recolecta eventualmente

# Comparar con Cat. 1 o Cat. 2:
# En Cat. 1/2 el tipo es fijo y la dirección no cambia durante la vida de la variable
```

---

## BLOQUE 5 — Ámbito

---

### [F-30] Ámbito estático — concepto y algoritmo

@tipo: concepto-abstracto
@imagen: none

# El ámbito estático se resuelve en compilación usando la estructura léxica del código

## ¿Qué es el ámbito (scope)?

El **ámbito** de una variable es el rango de instrucciones del programa donde el nombre de esa variable es **visible y puede ser usado**.

- Un nombre es "visible" si puede aparecer en una expresión sin causar error de nombre no definido
- El ámbito **estático** (o **léxico**) usa la estructura del código fuente para determinar la visibilidad
- Es el modelo de todos los lenguajes modernos: TypeScript, Python, Java, Go, Rust

## Algoritmo de resolución de ámbito estático

1. Buscar el nombre en el **ámbito local** (el bloque `{}` actual)
2. Si no se encuentra → subir al **bloque padre estático** (el bloque que lo contiene en el código)
3. Continuar hacia afuera, nivel por nivel, hasta el **ámbito global del módulo**
4. Si no se encuentra en ningún nivel → **error de compilación** (nombre no declarado)

## Origen histórico

Introducido por **ALGOL 60** en 1960 — fue una revolución: por primera vez el significado de un nombre podía determinarse sin ejecutar el programa.

## ¿Por qué "estático"?

Porque la resolución ocurre en **tiempo de compilación** — el analizador semántico puede determinar a qué declaración corresponde cada uso de un nombre, sin correr el código.

---

### [F-31] Ámbito estático — TypeScript

@tipo: codigo
@imagen: none

# La estructura de bloques determina qué nombres son visibles en cada punto

```typescript
let x = 10;  // ámbito: módulo (nivel 0)

function externa() {
    let y = 20;  // ámbito: función externa (nivel 1)

    function interna() {
        let z = 30;          // ámbito: función interna (nivel 2)

        // Resolución de cada nombre (algoritmo de búsqueda hacia afuera):
        console.log(x);  // 1. ¿x en nivel 2?  No
                         // 2. ¿x en nivel 1?  No
                         // 3. ¿x en nivel 0?  Sí → x = 10 ✅

        console.log(y);  // 1. ¿y en nivel 2?  No
                         // 2. ¿y en nivel 1?  Sí → y = 20 ✅

        console.log(z);  // 1. ¿z en nivel 2?  Sí → z = 30 ✅
    }

    // console.log(z); // ❌ z no existe en nivel 1 ni arriba — error de compilación
}

// console.log(y);     // ❌ y no existe en nivel 0 — error de compilación
```

---

### [F-32] Ámbito dinámico — comparativa

@tipo: tabla-comparativa
@imagen: none

# En el ámbito dinámico, la cadena de llamadas activas define la visibilidad

## Diferencia fundamental con el ámbito estático

| Característica | **Ámbito estático (léxico)** | **Ámbito dinámico** |
|---|---|---|
| **Momento de resolución** | Compilación | Ejecución |
| **¿Qué determina la visibilidad?** | Estructura léxica del código fuente | Cadena de llamadas activas en ese instante |
| **¿Verificable en compilación?** | ✅ Sí — el compilador valida todos los usos | ❌ No — depende del flujo de ejecución |
| **Legibilidad** | Alta — la visibilidad se ve en el código | Baja — hay que rastrear quién llamó a quién |
| **Lenguajes** | TypeScript, Python, Go, Rust, Java | Emacs Lisp (original), Perl `local`, shells POSIX |

## ¿Por qué el ámbito dinámico existe?

- En los primeros lenguajes (LISP original, SNOBOL) era la única opción — más fácil de implementar
- Útil para "inyectar" variables en funciones sin cambiar su firma (contexto implícito)
- Hoy es considerado una práctica problemática por dificultar el razonamiento sobre el código

## JavaScript: `this` tiene semántica dinámica en funciones regulares

El valor de `this` en una función regular depende de **cómo** se llama la función, no de dónde está escrita. Las arrow functions capturan `this` léxicamente.

---

### [F-33] Ámbito dinámico — `this` en JavaScript

@tipo: codigo
@imagen: none

# `this` en funciones regulares es dinámico — la arrow function lo captura léxicamente

```typescript
class Timer {
    delay = 1000;

    // ❌ Función regular: this es DINÁMICO — depende del contexto de llamada
    startConFunctionRegular() {
        setTimeout(function() {
            // this NO es la instancia Timer — lo perdió setTimeout
            // En strict mode: this === undefined
            console.log(this?.delay);   // undefined
        }, this.delay);
    }

    // ✅ Arrow function: this es LÉXICO — capturado en compilación
    startConArrow() {
        setTimeout(() => {
            // this ES la instancia Timer — garantizado por el ámbito léxico
            // El compilador sabe en compilación qué es this dentro de la arrow
            console.log(this.delay);    // 1000
        }, this.delay);
    }
}

const t = new Timer();
t.startConFunctionRegular();  // → undefined  (this dinámico, perdido en setTimeout)
t.startConArrow();            // → 1000       (this léxico, capturado en startConArrow)
```

---

### [F-34] Scope holes — shadowing — concepto

@tipo: concepto-abstracto
@imagen: none

# Una declaración local puede ocultar ("sombrear") una variable del bloque exterior

## ¿Qué es el shadowing?

- El **shadowing** ocurre cuando una declaración en un bloque interno usa el **mismo nombre** que una variable ya existente en un bloque exterior
- La variable interior **"oculta"** a la exterior dentro de su bloque
- La variable exterior cae en un **"scope hole"**: sigue existiendo, pero no es accesible dentro del bloque interno

## El mecanismo

- El algoritmo de resolución de ámbito **siempre prefiere** el binding más local
- Si encuentra el nombre en el bloque actual, **no continúa buscando** en los padres
- La variable exterior es inaccesible hasta que se sale del bloque interior donde fue sombreada

## Por qué es problemático

- El código parece estar usando la variable exterior pero en realidad usa la interior
- Los linters alertan sobre shadowing porque es fuente frecuente de bugs sutiles
- Los errores suelen detectarse en testing o en producción, no en compilación

## Herramientas para detectarlo

- **TypeScript + ESLint**: regla `@typescript-eslint/no-shadow` produce advertencia
- TypeScript por sí solo no bloquea el shadowing — requiere configuración explícita de ESLint
- Python: el shadow silencioso puede causar `UnboundLocalError` en casos extremos

---

### [F-35] Scope holes — shadowing — código

@tipo: codigo
@imagen: none

# Dos variables con el mismo nombre coexisten en scopes distintos sin interferir

```typescript
let x = 10;  // x del módulo (nivel 0)

function procesarLista(items: number[]): void {

    for (const item of items) {
        const x = item * 2;
        //    ↑ x LOCAL al bloque del for (nivel 2)
        //    ← SHADOW: oculta al x del módulo dentro de este bloque

        // "scope hole" de x exterior: comienza aquí ↑
        console.log(x);   // usa x LOCAL: 20, 40, 60, ...
    }
    // Aquí termina el scope hole

    console.log(x);   // x del módulo nuevamente visible: 10
}

procesarLista([10, 20, 30]);
// Salida:
//   20
//   40
//   60
//   10   ← x del módulo, nunca fue modificado

// ESLint con @typescript-eslint/no-shadow reportaría:
//   warning: 'x' is already declared in the upper scope (no-shadow)
```

---

## BLOQUE 6 — Entorno de Referencia e Inicialización

---

### [F-36] Entorno de referencia

@tipo: concepto-abstracto
@imagen: none

# El entorno de referencia es la "foto" de todos los nombres visibles en un punto del programa

## Definición (Sebesta §5.6)

El **entorno de referencia** en una sentencia dada es la **colección de todos los identificadores visibles** en ese punto: variables propias del bloque actual más todas las variables heredadas de los bloques padre.

## Variación a lo largo del programa

- El entorno de referencia **no es fijo** — cambia cada vez que se entra o sale de un bloque
- Al entrar a una función: se agrega su scope local al entorno
- Al salir de la función: ese scope se elimina del entorno
- Al entrar a un bloque `if`, `for`, etc.: se agrega el scope del bloque

## Componentes del entorno en TypeScript

- **Variables locales** del bloque actual
- **Parámetros** de la función actual
- **Variables de funciones externas** (capturadas por closure)
- **Variables del módulo** (top-level)
- **Identificadores globales** del runtime (`console`, `Math`, `undefined`, etc.)

## Relación con closures

- Una **closure** "congela" el entorno de referencia en el momento en que se crea la función
- El entorno capturado puede incluir variables que ya salieron del stack pero siguen vivas por la closure
- Esto se estudia en detalle en **Tema 09.2**

---

### [F-37] Constantes — concepto

@tipo: concepto-abstracto
@imagen: none

# Una constante es una variable cuyo binding de valor es inmutable

## Definición

Una **constante** es un identificador cuyo valor se fija en un momento determinado y el lenguaje **prohíbe modificarlo** después.

## Cuándo se fija el binding de valor

- **En compilación / declaración:** `const PI = 3.14159` — el valor es parte del código fuente
- **En tiempo de carga:** `const VERSION = pkg.version` — se determina al iniciar el módulo
- **En ejecución (primera asignación):** `val limite = calcularLimite()` en Kotlin — inmutable desde el momento de la asignación

## const en TypeScript: la referencia, no necesariamente el objeto

- Para **tipos primitivos** (`number`, `string`, `boolean`): `const` hace inmutable el valor
- Para **objetos y arrays**: `const` hace inmutable la **referencia** — el objeto interno puede mutar
- Para inmutabilidad profunda se necesita `Object.freeze()` o tipos `readonly` en TypeScript

## Por qué las constantes importan en binding

- Representan un **binding de R-value que no puede reasignarse**
- El L-value (dirección) sigue existiendo — la celda está ocupada durante toda la vida del módulo
- El compilador puede optimizar accesos a constantes porque su valor es conocido en compilación

---

### [F-38] Constantes — código TypeScript

@tipo: codigo
@imagen: none

# const inmutabiliza la referencia, no necesariamente el objeto

```typescript
// Caso 1: tipo primitivo — const hace inmutable el VALOR
const PI = 3.14159;
// PI = 2.71;  // ❌ Error: Assignment to constant variable

// Caso 2: objeto — const hace inmutable la REFERENCIA (dirección)
const CONFIG = { debug: false, maxRetries: 3 };
CONFIG.debug = true;    // ✅ válido: el objeto es mutable, solo la referencia es const
CONFIG.maxRetries = 5;  // ✅ válido
// CONFIG = { debug: true };  // ❌ Error: Cannot assign to 'CONFIG'

// Caso 3: inmutabilidad profunda con Object.freeze
const FROZEN = Object.freeze({ debug: false });
FROZEN.debug = true;
// En JavaScript: silencioso (el cambio se ignora sin error)
// En TypeScript strict: Error de tipo — readonly property

// Patrón recomendado para objetos de configuración inmutables:
const SETTINGS = Object.freeze({
    timeout: 5000,
    retries: 3,
} as const);
// 'as const' asegura que TypeScript trate todos los campos como literales de tipo
```

---

### [F-39] Inicialización — comparativa de lenguajes

@tipo: tabla-comparativa
@imagen: none

# ¿Qué pasa si se usa una variable antes de inicializarla?

## Sebesta §5.4.3 — comportamientos por lenguaje

| Lenguaje | Variable no inicializada | Momento de detección |
|---|---|---|
| **C** | Estáticas → 0 automático; locales → **basura** (contenido previo de la celda) | Ejecución (undefined behavior) |
| **C++** | Igual que C para primitivos; constructores para objetos | Ejecución |
| **Java** | Campos → valores por defecto (0, false, null); locales → error de compilación | Variables locales: compilación |
| **TypeScript strict** | **Error de compilación** — análisis de flujo detecta el camino sin inicialización | Compilación |
| **Python** | `NameError` — el intérprete lanza excepción al acceder | Runtime |
| **Go** | **Zero values automáticos**: 0, false, `""`, nil — nunca hay basura | Siempre seguro |
| **Rust** | Error de compilación — el compilador exige inicialización antes del primer uso | Compilación |

## TypeScript strict mode — análisis de flujo de tipos

```typescript
let n: number;
console.log(n);  // Error TS2454: Variable 'n' used before being assigned
// El compilador analiza el flujo y detecta que n puede no estar inicializada
```

---

## BLOQUE 7 — IA y Variables

---

### [F-40] La IA comete errores de scope

@tipo: socratica
@imagen: none

# ¿Por qué la IA genera código con errores de scope?

## La raíz del problema

- Los modelos de lenguaje aprenden de corpus de código extraído de la web
- El corpus incluye **millones de archivos pre-ES6** con `var`, variables globales y shadowing silencioso
- En JavaScript no-strict, muchos de estos errores **no generan excepciones** — el código "funciona" aunque sea incorrecto
- El modelo aprende que estos patrones son válidos porque el corpus los usa sin marcarlos como error

## Tres patrones concretos a reconocer

1. **`var` hoisting:** `var` se "iza" al inicio de la función — da `undefined` en lugar de `ReferenceError`
2. **Variable global silenciosa:** dependencias ocultas no declaradas como parámetro
3. **Shadowing inesperado:** ¿a qué variable se refiere realmente el código generado?

## Lo que veremos en las próximas filminas

Cada patrón tiene:
- Una explicación del **mecanismo** (por qué ocurre)
- Un ejemplo de **código incorrecto** que la IA suele generar
- La **versión correcta** y cómo pedirle a la IA que la genere

---

### [F-41] Patrón 1 — `var` hoisting — concepto

@tipo: concepto-abstracto
@imagen: none

# `var` tiene ámbito de función, no de bloque — y se "iza" al inicio

## ¿Qué es el hoisting?

- En JavaScript/TypeScript, las declaraciones `var` son **izadas** (*hoisted*) al inicio de la función
- El compilador mueve la declaración (no la inicialización) al principio del scope de función
- Esto significa que la variable **existe** desde el inicio de la función, aunque su valor sea `undefined`

## La diferencia entre `var`, `let` y `const`

| | **`var`** | **`let` y `const`** |
|---|---|---|
| **Ámbito** | Función (no respeta bloques `{}`) | Bloque (`{}`) |
| **Hoisting** | Sí — sube al inicio de la función | Sí — pero entra en Temporal Dead Zone |
| **Temporal Dead Zone** | No hay TDZ — da `undefined` antes de asignar | Hay TDZ — da `ReferenceError` antes de declarar |
| **Uso antes de declarar** | `undefined` (silencioso, difícil de rastrear) | `ReferenceError` (explícito, fácil de diagnosticar) |

## Temporal Dead Zone (TDZ)

- Con `let`/`const`, la variable existe en el scope pero **no puede usarse** hasta que se alcanza su declaración
- Usar la variable antes de su declaración lanza `ReferenceError` — un error explícito y localizable
- Con `var` no hay TDZ: cualquier uso antes de la asignación da `undefined` en silencio

---

### [F-42] Patrón 1 — `var` hoisting — código

@tipo: codigo
@imagen: none

# `var resultado` existe en toda la función — `let resultado` lanzaría error explícito

```typescript
// ❌ Código típico de IA entrenada en corpus pre-ES6:
function procesar(activo: boolean) {
    if (activo) {
        var resultado = "ok";   // ← var: scope de FUNCIÓN, no de bloque
    }
    // "var resultado" fue izada al inicio de procesar():
    // equivale a:
    //   var resultado;             // undefined
    //   if (activo) { resultado = "ok"; }

    console.log(resultado);   // undefined si activo = false — NO lanza error
    // El error silencioso puede ocurrir lejos de la causa real
}

// ✅ Con let: error explícito y localizable
function procesar2(activo: boolean) {
    if (activo) {
        let resultado = "ok";   // ← let: scope del BLOQUE if
    }
    // console.log(resultado); // ❌ ReferenceError: resultado is not defined
    //   El error aparece exactamente donde está el problema
}
```

---

### [F-43] Patrón 2 — Variable global silenciosa — concepto

@tipo: concepto-abstracto
@imagen: none

# Una función que modifica variables fuera de sus parámetros tiene efectos secundarios ocultos

## El problema de las dependencias implícitas

- Una **función pura** depende solo de sus parámetros y produce un resultado sin modificar el entorno externo
- Cuando una función accede a una variable declarada **fuera de su firma**, crea una **dependencia implícita**
- La IA tiende a generar este patrón porque en el corpus de entrenamiento es frecuente (código imperativo legacy)

## Por qué es problemático

- La **firma de la función** no refleja todas sus dependencias — el lector no puede entender qué hace sin leer el cuerpo
- El resultado de la función puede cambiar según el **orden de las llamadas anteriores** — no es predecible desde sus parámetros
- Las **pruebas unitarias** se complican: hay que inicializar el estado global antes de cada test
- Los **efectos secundarios** son invisibles para el compilador — no hay error de compilación

## Señales de alerta en código generado por IA

- Función que **modifica una variable declarada fuera** de su scope inmediato
- Función cuyo **resultado varía** según qué otras funciones se llamaron antes
- Variable `total`, `contador`, `estado` declarada en el módulo y modificada dentro de funciones

## La solución: parámetros explícitos

- Convertir la variable externa en parámetro hace la dependencia **visible en la firma**
- La función se vuelve predecible: mismos parámetros → mismo resultado

---

### [F-44] Patrón 2 — Variable global silenciosa — código

@tipo: codigo
@imagen: none

# La función oculta su dependencia en `total` — la firma no lo refleja

```typescript
// ❌ Código con efecto secundario implícito (generado por IA):
let total = 0;  // variable global oculta — no aparece en la firma

function acumular(n: number) {
    total += n;   // ← modifica estado externo sin declararlo en la firma
    return total; // ← el resultado depende de todas las llamadas anteriores
}

acumular(5);   // total = 5
acumular(3);   // total = 8
acumular(5);   // total = 13  (mismo argumento, resultado diferente)
```

```typescript
// ✅ Correcto — todas las dependencias son parámetros explícitos:
function acumularPuro(total: number, n: number): number {
    return total + n;   // mismos argumentos → siempre el mismo resultado
}

const r1 = acumularPuro(0, 5);    // → 5
const r2 = acumularPuro(r1, 3);   // → 8
const r3 = acumularPuro(r2, 5);   // → 13
// Predecible, testeable de forma aislada, sin estado oculto
```

---

### [F-45] Patrón 3 — Shadowing inesperado — código

@tipo: codigo
@imagen: none

# ¿A qué `limite` se refiere el filter? — la IA no siempre lo elige correctamente

```typescript
const limite = 100;  // limite del módulo (nivel 0)

// ❌ Código generado por IA con shadowing inesperado:
function validar(items: number[]) {
    const limite = items.length;   // ← SHADOW: nueva variable con el mismo nombre
    //                               oculta al limite = 100 del módulo

    return items.filter(x => x < limite);
    //                           ↑ ¿qué limite? → el LOCAL (items.length), NO el 100
    // Si items = [50, 120, 80] y items.length = 3:
    //   items.filter(x => x < 3)  → []  ← vacío (ningún elemento < 3)
    //   El comportamiento correcto sería filtrar los que son < 100
}

// ✅ Correcto — sin shadowing, intención explícita:
function validarSinShadow(items: number[], valorLimite: number): number[] {
    const cantidadItems = items.length;    // nombre diferente — sin shadow
    return items.filter(x => x < valorLimite);  // sin ambigüedad
}
```

---

### [F-46] Actividad — tres patrones mezclados

@tipo: socratica
@imagen: none

# ¿Cuántos errores ves? ¿A qué patrón pertenece cada uno?

```typescript
let limite = 100;
var total = 0;

function procesar(items: number[]) {
    if (items.length > 0) {
        var resultado = items[0] * 2;
    }
    for (const item of items) {
        const limite = item;
        total += limite;
    }
    console.log(resultado);
    return items.filter(x => x < limite);
}
```

## Consigna

**2 minutos — identificar en silencio:**

1. ¿Cuántos errores o problemas hay en este fragmento?
2. ¿A qué patrón corresponde cada uno?
3. ¿Cuál daría `undefined` sin error visible?

---

### [F-47] Prompt seguro para variables en TypeScript

@tipo: concepto-abstracto
@imagen: none

# Instrucciones explícitas al modelo producen código con buenas prácticas de scope

## El prompt

```
"TypeScript strict mode.
Declara todo con let/const (nunca var).
Sin variables globales — todas las dependencias
son parámetros explícitos con sus tipos declarados.
Declara el tipo de cada parámetro y el tipo de retorno."
```

## Por qué funciona cada restricción

- **`strict mode`**: activa detección de variables usadas antes de asignación (análisis de flujo de tipos)
- **`let/const` (nunca `var`)**: elimina el hoisting problemático — cualquier uso fuera de scope da `ReferenceError`
- **Parámetros explícitos**: el modelo entiende que no puede usar variables de fuera de la función
- **Tipos en firma**: el compilador puede verificar la corrección antes de ejecutar

## Por qué es necesario ser explícito

- Sin estas instrucciones, el modelo aplica el patrón estadísticamente más frecuente en su corpus
- Con estas restricciones, el modelo ve el contexto de uso y produce código más preciso
- Las restricciones también actúan como **documentación técnica del proyecto** para cualquier colaborador

---

## CIERRE

---

### [F-48] Cierre — tres ideas para llevarse

@tipo: cierre
@imagen: none

# Variables, Binding y Ámbito

## Tres ideas para llevarse

1. **La variable es una 5-tupla** — nombre, dirección, tipo, L-value, R-value — cada atributo tiene su propio binding y su propio momento

2. **Binding ocurre en 6 momentos** — cuanto antes ocurre, más eficiente y más verificable; cuanto más tarde, más flexible pero más riesgoso

3. **El ámbito estático es predecible** — se resuelve en compilación: cualquier error de visibilidad aparece antes de ejecutar el programa

## Próxima clase — Tema 09.2

**Aliases, Closures, GC y Tipos**
Las variables son entidades que se comparten, capturan y liberan.

## TP

Disponible en el aula virtual — ver consignas en `tp.md`.
