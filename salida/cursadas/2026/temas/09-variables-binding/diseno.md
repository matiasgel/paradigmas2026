# DiseÃ±o â€” Tema 09: Variables, Binding y Ãmbito

> **Agente:** Lic. Marcos ðŸ—‚ï¸ â€” Topic Designer  
> **Fecha:** 2026-05-11  
> **Estado:** ðŸ”² Borrador â€” pendiente de aprobaciÃ³n docente  
> **DuraciÃ³n:** **240 min (2 clases de 120 min)**  
> **Lenguaje principal:** TypeScript  
> **Lenguajes de contraste:** Python (binding dinÃ¡mico, tipado duck), Kotlin (val/var, null safety), Go (zero values, punteros seguros), Rust (ownership como binding explÃ­cito), Haskell (bindings inmutables)  
> **Fuente primaria:** Sebesta â€” *Concepts of Programming Languages* (Pearson 2019), Cap. 5â€“6  
> **Fuentes secundarias:** Gabbrielli & Martini â€” *Programming Languages: Principles and Paradigms* (Springer 2023), Cap. 4, 7, 16; Louden & Lambert â€” *Programming Languages: Principles and Practices* (2012), Cap. 7, 10; Filminas UNTDF 2024  
> **Bloque IA (Clase 1):** Errores de Ã¡mbito en cÃ³digo generado. Variables globales silenciosas  
> **Bloque IA (Clase 2):** Aliases y mutabilidad como fuente de bugs en LLMs. Type narrowing como guardrail  

---

## 1. Contexto en el Plan

**PosiciÃ³n:** Tema 09 de 15 â€” Bloque post-OO, pre-tipos  
**DuraciÃ³n expandida:** 2 clases Ã— 120 min = **240 min totales**  
**TÃ³pico del plan mÃ­nimo:** Entidades y ligaduras (VI.9)  
**Conexiones:**  
- â†’ Tema 08 (OO TypeScript): el `this`, los objetos son variables con atributos; paso de objetos por referencia  
- â†’ Tema 10 (Tipos de Datos): el tipo es uno de los atributos de la variable; union types, discriminated unions  
- â†’ Tema 14 (Sistemas de Tipos): binding estÃ¡tico de tipos en TypeScript, inferencia, gradual typing  

---

## 2. Objetivos de Aprendizaje

Al finalizar las 2 clases el alumno debe poder:

| # | Objetivo | Nivel Bloom |
|---|----------|-------------|
| OA1 | Describir la variable como 5-tupla `<nombre, direcciÃ³n, tipo, valor-i, valor-d>` | Recordar |
| OA2 | Distinguir los 6 momentos de binding: diseÃ±o, implementaciÃ³n, compilaciÃ³n, linkeo, carga, ejecuciÃ³n | Comprender |
| OA3 | Clasificar variables segÃºn sus 4 categorÃ­as de tiempo de vida y zona de almacenamiento | Analizar |
| OA4 | Comparar Ã¡mbito estÃ¡tico vs. dinÃ¡mico: reglas de resoluciÃ³n, ventajas y problemas | Analizar |
| OA5 | Explicar aliases, sus fuentes y por quÃ© dificultan la verificaciÃ³n de programas | Comprender |
| OA6 | Describir closures como captura del entorno lÃ©xico y su relaciÃ³n con el ciclo de vida de variables | Comprender |
| OA7 | Comparar garbage collection (reference counting vs. mark-sweep) con gestiÃ³n manual de memoria | Analizar |
| OA8 | Explicar gradual typing y el rol de TypeScript como lenguaje gradualmente tipado | Comprender |
| OA9 | Contrastar variables mutables (imperativo) con bindings inmutables (funcional) | Analizar |
| OA10 | Aplicar reglas de Ã¡mbito estÃ¡tico y type narrowing en cÃ³digo TypeScript | Aplicar |
| OA11 | Detectar errores de Ã¡mbito, aliases y mutabilidad en cÃ³digo generado por IA | Evaluar |

---

## 3. TÃ³picos, Tiempo Estimado y DistribuciÃ³n por Clase

### Clase 1 (120 min) â€” Variable, Binding, Almacenamiento y Ãmbito

| # | TÃ³pico | Tiempo | Fuente |
|---|--------|--------|--------|
| 3.1 | Variable como abstracciÃ³n. La 5-tupla | 10 min | Sebesta Â§5.3, filminas |
| 3.2 | Atributos: nombre, direcciÃ³n, tipo, valor-i, valor-d | 12 min | Sebesta Â§5.3.1â€“5.3.4, filminas |
| 3.3 | Binding: definiciÃ³n y 6 tiempos de vinculaciÃ³n | 15 min | Sebesta Â§5.4, filminas |
| 3.4 | Binding de tipos: estÃ¡tico vs. dinÃ¡mico + inferencia | 12 min | Sebesta Â§5.4.1â€“5.4.2, Gabbrielli Â§8 |
| 3.5 | Binding de almacenamiento: 4 categorÃ­as de variables | 18 min | Sebesta Â§5.4.3, filminas |
| 3.6 | Ãmbito estÃ¡tico vs. dinÃ¡mico | 15 min | Sebesta Â§5.5, Gabbrielli Â§4.3 |
| 3.7 | Entorno de referencia. Constantes. InicializaciÃ³n | 8 min | Sebesta Â§5.6â€“5.8, filminas |
| â€” | **Bloque IA:** globales silenciosas, `var` hoisting, prompts seguros | 12 min | â€” |
| â€” | Buffer / preguntas | 8 min | â€” |
| **Total** | | **110 min + 10 buffer** | |

### Clase 2 (120 min) â€” Aliases, Closures, GC, Gradual Typing y Variables en FP

| # | TÃ³pico | Tiempo | Fuente |
|---|--------|--------|--------|
| 3.8 | Aliases: definiciÃ³n, fuentes (punteros, ref params, union types) | 15 min | Sebesta Â§5.3.3, Louden Â§7.7 |
| 3.9 | Closures: entorno lÃ©xico capturado, ciclo de vida extendido | 18 min | Sebesta Â§10, Gabbrielli Â§7.4, Louden Â§10.3 |
| 3.10 | Garbage Collection: reference counting vs. mark-sweep | 18 min | Sebesta Â§6.11, Louden Â§10.5 |
| 3.11 | Gradual typing: TypeScript como caso paradigmÃ¡tico | 15 min | Gabbrielli Â§16.9 |
| 3.12 | Variables en programaciÃ³n funcional: sin mutabilidad | 12 min | Sebesta Â§5.8 (FP), Gabbrielli Â§11 |
| 3.13 | Contraste multilenguaje: Python, Kotlin, Go, Rust â€” gestiÃ³n de memoria moderna | 10 min | Sebesta Â§5.4.3, Gabbrielli Â§16 |
| â€” | **Bloque IA:** aliases y mutabilidad, type narrowing como guardrail | 12 min | â€” |
| â€” | Buffer / preguntas | 10 min | â€” |
| **Total** | | **110 min + 10 buffer** | |

---

## 4. Desarrollo de Contenidos â€” Clase 1

### 4.1 Variable como AbstracciÃ³n

**Contexto arquitectural:**  
La arquitectura Von Neumann tiene dos componentes clave: memoria (celdas con direcciÃ³n) y procesador. Los lenguajes abstraen eso:

| Elemento concreto | AbstracciÃ³n en LP |
|------------------|-------------------|
| Celda de memoria | **Variable** |
| DirecciÃ³n de celda | **Nombre/identificador** |
| ModificaciÃ³n destructiva | **Sentencia de asignaciÃ³n** |

**La variable como 5-tupla** (Sebesta Â§5.3 â€” formalizaciÃ³n central):

```
Variable = <nombre, Ã¡mbito, tipo, valor-i, valor-d>
```

- **nombre:** identificador simbÃ³lico (puede no existir: variables anÃ³nimas)  
- **Ã¡mbito:** rango de sentencias donde el nombre es visible  
- **tipo:** conjunto de valores posibles + operaciones legales  
- **valor-i (L-value):** direcciÃ³n de memoria asociada  
- **valor-d (R-value):** valor codificado almacenado en esa direcciÃ³n  

```typescript
// TypeScript â€” la 5-tupla en acciÃ³n
let contador: number = 42;
//   â†‘nombre  â†‘tipo    â†‘valor-d
// valor-i = direcciÃ³n de memoria asignada por el runtime (oculta)
// Ã¡mbito  = bloque donde estÃ¡ declarado

// TypeScript oculta el valor-i â€” no hay acceso directo a la direcciÃ³n
// Rust lo hace explÃ­cito de forma segura:
// let x = 42i32;           // binding: nombre x â†’ tipo i32 â†’ valor 42
// let addr = &x as *const i32;  // valor-i visible como puntero raw
```

```python
# Python â€” equivalente dinÃ¡mico: la 5-tupla con binding en runtime
contador = 42          # nombre: contador, tipo: int (inferido), valor-d: 42
id(contador)           # id() expone el valor-i (direcciÃ³n del objeto)
type(contador)         # int â€” binding de tipo dinÃ¡mico
```

```kotlin
// Kotlin â€” la 5-tupla con null safety integrada
var contador: Int = 42    // mutable â€” valor-i puede cambiar de valor-d
val limite: Int = 100     // inmutable â€” binding de valor-d fijo desde creaciÃ³n
```

> ðŸ“Œ **Sebesta Â§5.3.2:** Un mismo nombre puede tener distintas direcciones en distintos lugares del programa (funciones diferentes) o en distintos momentos de ejecuciÃ³n (recursiÃ³n). **L-value â‰  R-value** â€” esto es fundamental para entender aliases y paso por referencia.

---

### 4.2 Atributos de Variables

#### Nombre / Identificador

- Restricciones por lenguaje: longitud (Python sin lÃ­mite prÃ¡ctico, JavaScript sin lÃ­mite); convenciÃ³n: `camelCase` en TypeScript/Kotlin, `snake_case` en Python/Rust
- **Case sensitivity:** TypeScript, Python, Go, Rust â†’ distinguen mayÃºsculas. `Count` â‰  `count` â‰  `COUNT`
- **Palabras reservadas** vs. **palabras clave**: las reservadas no pueden usarse como nombres (TypeScript, Python, Kotlin, Rust); Go es mÃ¡s permisivo con algunas
- **Espacios de nombres:** TypeScript usa mÃ³dulos; Python usa mÃ³dulos + `__all__`; Rust usa `mod` explÃ­cito; Go usa paquetes con mayÃºscula para exportar

#### Tipo

Define: (a) rango de valores posibles, (b) operaciones legales, (c) representaciÃ³n interna.  
TypeScript extiende esto con **structural typing** â€” el tipo es compatible por estructura, no por nombre nominal.

#### Valor-d (R-value) y Valor-i (L-value)

El contenido codificado de la celda, interpretado segÃºn el tipo.  
En `x = y`: `x` denota direcciÃ³n (valor-i), `y` denota contenido (valor-d).

---

### 4.3 Binding (VinculaciÃ³n)

**DefiniciÃ³n (Sebesta Â§5.4):** Binding es la asociaciÃ³n entre una entidad del programa y un atributo. Ocurre en distintos momentos:

| Momento | DescripciÃ³n | Ejemplo |
|---------|-------------|---------|
| **Tiempo de diseÃ±o** | Significados posibles para sÃ­mbolos | `*` = multiplicaciÃ³n |
| **Tiempo de implementaciÃ³n** | Rango de valores para tipos primitivos | `int` de 32 o 64 bits segÃºn arquitectura |
| **Tiempo de compilaciÃ³n** | Variable â†’ tipo (C, Java, TypeScript) | `int count;` |
| **Tiempo de linkeo** | Llamada a librerÃ­a â†’ cÃ³digo del subprograma | `printf` en libc |
| **Tiempo de carga** | Variables globales â†’ celdas de memoria | variables estÃ¡ticas globales |
| **Tiempo de ejecuciÃ³n** | Variable â†’ valor | `count = count + 5` |

**Ejemplo integrador en TypeScript** â€” los mismos 6 momentos:
```typescript
let count: number;
count = count + 5;
// Tipos posibles para una variable    â†’ tiempo de diseÃ±o del lenguaje
// Tipo de count (number)              â†’ tiempo de compilaciÃ³n (inferencia TS)
// Rango de valores de number          â†’ tiempo de implementaciÃ³n (IEEE 754 float64)
// Valor de count                      â†’ tiempo de ejecuciÃ³n
// Significado del operador +          â†’ tiempo de compilaciÃ³n
// RepresentaciÃ³n interna del literal 5 â†’ tiempo de diseÃ±o del compilador
```

**Comparativa de binding de tipos en lenguajes modernos:**

| Lenguaje | Binding de tipo | Momento |
|----------|----------------|---------||
| TypeScript | EstÃ¡tico + inferencia | CompilaciÃ³n |
| Kotlin | EstÃ¡tico + inferencia | CompilaciÃ³n |
| Go | EstÃ¡tico + inferencia (`:=`) | CompilaciÃ³n |
| Rust | EstÃ¡tico + inferencia (Hindley-Milner) | CompilaciÃ³n |
| Python | DinÃ¡mico (+ type hints opcionales) | EjecuciÃ³n |
| JavaScript | DinÃ¡mico | EjecuciÃ³n |

---

### 4.4 Binding de Tipos

#### Binding EstÃ¡tico (DeclaraciÃ³n ExplÃ­cita)

```typescript
let i: number;          // TypeScript â€” explÃ­cito
let x = 5;              // TypeScript â€” inferencia: x: number
```

**Inferencia de tipos** (Gabbrielli Â§8): el compilador determina el tipo sin declaraciÃ³n explÃ­cita. TypeScript usa inferencia bidireccional:

```typescript
// Inferencia forward
const items = [1, 2, 3];     // number[]
const first = items[0];       // number

// Inferencia contextual
items.forEach(x => {          // x: number (inferido del contexto)
    console.log(x.toFixed(2));
});
```

```haskell
-- Haskell: inferencia total (Hindley-Milner)
f x y
  | x == True = y * y
  | otherwise = y / 2
-- El compilador infiere: f :: Bool -> Double -> Double
```

#### Binding DinÃ¡mico de Tipos

```python
x = [2, 3, 4, 5]        # x: list
x = "uno, dos, tres"     # x: str â€” binding de tipo cambiÃ³ en runtime
```

**Problema:** Errores de tipo no detectables en compilaciÃ³n; mayor overhead.

#### Gradual Typing (avance â€” profundizaciÃ³n en Clase 2 Â§3.11)

TypeScript es el ejemplo canÃ³nico: permite mezclar zonas con tipos estÃ¡ticos y dinÃ¡micas (`any`).

---

### 4.5 Binding de Almacenamiento: 4 CategorÃ­as

**Tiempo de vida:** perÃ­odo durante el cual la variable estÃ¡ vinculada a una direcciÃ³n especÃ­fica de memoria. *(Sebesta Â§5.4.3)*

#### CategorÃ­a 1 â€” Variables EstÃ¡ticas

Vinculadas antes de la ejecuciÃ³n, permanecen hasta el fin del programa.

```typescript
// TypeScript â€” variable de mÃ³dulo: estÃ¡tica en la prÃ¡ctica
let sesionesActivas = 0;        // vive toda la vida del mÃ³dulo
const VERSION = "1.0.0";        // estÃ¡tica e inmutable

// PatrÃ³n mÃ³dulo con estado estÃ¡tico:
let _cache: Map<string, string> | null = null;
export function getCache() {
    _cache ??= new Map();  // inicializaciÃ³n lazy â€” una sola vez
    return _cache;
}
```

```kotlin
// Kotlin â€” companion object (equivalente a static de clase)
class Sesion {
    companion object {
        private var contadorGlobal = 0   // estÃ¡tico de clase
        fun nuevaId() = ++contadorGlobal
    }
}
```

```go
// Go â€” package-level variable: estÃ¡tica
var sesionesActivas int = 0  // vive toda la vida del paquete
const version = "1.0.0"      // constante: binding en tiempo de compilaciÃ³n
```

**Ventajas:** Eficiencia (direcciÃ³n conocida en compilaciÃ³n), historial entre llamadas  
**Desventajas:** No soporta recursiÃ³n efectiva, ocupa memoria siempre

#### CategorÃ­a 2 â€” Variables DinÃ¡micas de Pila (Stack-dynamic)

Creadas al activar el subprograma, destruidas al retornar.

```typescript
function calcular(n: number): number {
    let resultado = 0;  // stack-dynamic
    let temp = n * 2;   // stack-dynamic
    return resultado + temp;
    // Al retornar: resultado y temp destruidas
}
```

**Permite recursiÃ³n** porque cada activaciÃ³n tiene su propio frame en la pila.  
**Stack Overflow:** la pila tiene tamaÃ±o mÃ¡ximo definido por el SO.

#### CategorÃ­a 3 â€” Variables DinÃ¡micas de Heap ExplÃ­citas

Asignadas y liberadas explÃ­citamente. En lenguajes modernos, la *gestiÃ³n* puede ser automÃ¡tica (GC) o garantizada por el compilador (ownership).

```typescript
// TypeScript â€” new asigna en heap; GC libera automÃ¡ticamente
class Nodo {
    constructor(
        public valor: number,
        public siguiente: Nodo | null = null
    ) {}
}
let cabeza = new Nodo(42);      // asignado en heap
cabeza = new Nodo(99);          // el Nodo(42) queda sin referencias â†’ GC lo libera
```

```kotlin
// Kotlin â€” igual que TypeScript: JVM GC gestiona el heap
data class Nodo(val valor: Int, val siguiente: Nodo? = null)
var cabeza: Nodo? = Nodo(42)
cabeza = Nodo(99)   // Nodo(42) â†’ eligible para GC
```

```rust
// Rust â€” heap explÃ­cita con ownership: el compilador garantiza la liberaciÃ³n
let elemento = Box::new(42);    // Box<i32> asigna en heap
// Al salir del scope: destructor automÃ¡tico â€” sin GC, sin leak posible
// Si se intenta usar despuÃ©s del drop â†’ error de compilaciÃ³n (borrow checker)
```

> **Contraste de paradigmas de gestiÃ³n:** TypeScript/Kotlin â†’ GC automÃ¡tico; Rust â†’ ownership + compile-time; C â†’ manual (malloc/free, propenso a leaks y dangling pointers)

#### CategorÃ­a 4 â€” Variables DinÃ¡micas de Heap ImplÃ­citas

Todos sus atributos (tipo, valor, direcciÃ³n) se establecen cuando se les asigna un valor. TÃ­pico de lenguajes con binding dinÃ¡mico de tipos.

```python
# Python â€” el caso mÃ¡s claro: la variable no existe hasta la asignaciÃ³n
x = [1, 2, 3]          # x: list, todos sus atributos vinculados aquÃ­
x = "uno, dos, tres"   # x: str â€” todos los atributos (tipo+valor+dir) cambian
x = 42                 # x: int
type(x)                # int â€” binding de tipo determinado en runtime
```

```typescript
// TypeScript con 'any' â€” se aproxima a Cat. 4 (pero desaconsejado)
let x: any = [1, 2, 3];
x = "uno, dos, tres";   // binding de tipo cambia â€” TypeScript permite con any

// Con tipos: TypeScript es Cat. 2/3 â€” el tipo queda fijo desde la declaraciÃ³n
let items: number[] = [1, 2, 3];  // tipo fijado en compilaciÃ³n (no Cat. 4 real)
```

---

### 4.6 Ãmbito (Scope)

**DefiniciÃ³n:** Rango de instrucciones donde el nombre de una variable es visible.

#### Ãmbito EstÃ¡tico (LÃ©xico)

Introducido por ALGOL 60. Determinado en **tiempo de compilaciÃ³n**.

**Algoritmo de resoluciÃ³n:**
1. Buscar en Ã¡mbito local â†’ 2. Buscar en el bloque padre estÃ¡tico â†’ ... â†’ Error de compilaciÃ³n si no se encuentra

```typescript
let x = 10;  // Ã¡mbito: mÃ³dulo

function externa() {
    let y = 20;
    function interna() {
        let z = 30;
        console.log(x);  // âœ… antepasado estÃ¡tico: mÃ³dulo
        console.log(y);  // âœ… antepasado estÃ¡tico: externa
    }
    // console.log(z);  // âŒ z no visible aquÃ­
}
```

**Problema de Ã¡mbito estÃ¡tico (Sebesta Â§5.5.5):**  
Variables del programa principal son visibles en **todos** los procedimientos â†’ acceso involuntario a demasiados datos. Tendencia a crear mÃ¡s variables globales de las necesarias.

#### Ãmbito DinÃ¡mico

Determinado en **tiempo de ejecuciÃ³n** segÃºn la cadena de llamadas.

**Algoritmo:** buscar en la declaraciÃ³n local â†’ subprograma que llamÃ³ â†’ antepasados dinÃ¡micos â†’ Runtime Error si no se encuentra.

**Problemas (Sebesta Â§5.5.4):**
- Variables locales del llamador son visibles en el llamado â†’ sin protecciÃ³n
- Imposibilidad de verificaciÃ³n estÃ¡tica de tipos para no-locales
- Acceso mÃ¡s lento que Ã¡mbito estÃ¡tico
- Programas difÃ­ciles de leer (hay que rastrear la cadena de llamadas)

**ConclusiÃ³n Sebesta:** Ãmbito estÃ¡tico produce programas mÃ¡s legibles, confiables y rÃ¡pidos. Por eso reemplazÃ³ al dinÃ¡mico en la mayorÃ­a de los dialectos modernos de Lisp.

---

### 4.7 Entorno de Referencia. Constantes. InicializaciÃ³n

**Entorno de referencia:** colecciÃ³n de todos los identificadores visibles en una sentencia dada.

**Constantes:**
```typescript
const PI = 3.14159;           // binding inmutable: referencia y valor
const CONFIG = { debug: false }; // binding inmutable de referencia; objeto mutable
```

**InicializaciÃ³n** (Sebesta Â§5.4.3): binding variable â†’ valor en el momento del binding de almacenamiento.

| Lenguaje | Comportamiento con variables no inicializadas |
|----------|----------------------------------------------|
| C | Variables estÃ¡ticas â†’ 0; locales â†’ basura (undefined behavior) |
| Java | NumÃ©ricas â†’ 0; booleanas â†’ false; objetos â†’ null |
| TypeScript (`strict: true`) | Detecta usos antes de asignaciÃ³n en compilaciÃ³n |
| Python | Cada asignaciÃ³n inicializa; uso sin asignaciÃ³n â†’ NameError |

---

### 4.8 â€” Bloque IA Clase 1 (12 min): Errores de Ãmbito

#### PatrÃ³n 1: `var` hoisting silencioso

```typescript
// CÃ³digo generado tÃ­pico por IA (malas prÃ¡cticas):
function procesar(activo: boolean) {
    if (activo) {
        var resultado = "ok";   // â† IA usa var (corpus pre-ES6)
    }
    console.log(resultado);     // undefined â€” no ReferenceError
    // Con let â†’ ReferenceError explÃ­cito y correcto
}
```

#### PatrÃ³n 2: Variable global silenciosa

```typescript
// IA genera efecto secundario implÃ­cito:
let total = 0;  // global oculta
function acumular(n: number) {
    total += n;  // muta global sin advertencia
    return total;
}

// Correcto â€” sin efectos secundarios:
function acumularPuro(total: number, n: number): number {
    return total + n;
}
```

#### PatrÃ³n 3: Shadowing inesperado

```typescript
const limite = 100;
function validar(items: number[]) {
    const limite = items.length;  // â† shadowing silencioso
    return items.filter(x => x < limite);  // Â¿quÃ© limite?
}
```

**Prompt seguro:**
```
"TypeScript strict mode. Declara todo con let/const (nunca var).
Sin variables globales â€” todas las dependencias son parÃ¡metros explÃ­citos.
Declara el tipo de cada parÃ¡metro."
```

---

## 5. Desarrollo de Contenidos â€” Clase 2

### 5.1 Aliases (Â§3.8)

**DefiniciÃ³n (Sebesta Â§5.3.3, Louden Â§7.7):** Un alias ocurre cuando dos nombres distintos estÃ¡n vinculados al mismo objeto (misma celda de memoria) en el mismo momento.

**Fuentes de aliases:**

1. **Referencias de objeto en TypeScript** (fuente mÃ¡s comÃºn hoy):

2. **ParÃ¡metros por referencia** (Kotlin, Go):

```kotlin
// Kotlin â€” los objetos se pasan por referencia (alias implÃ­cito)
data class Punto(var x: Int, var y: Int)
fun desplazar(p: Punto, dx: Int) { p.x += dx }  // alias: p apunta al mismo objeto
val origen = Punto(0, 0)
desplazar(origen, 5)
println(origen.x)  // 5 â€” Â¡el objeto fue modificado a travÃ©s del alias!
```

```go
// Go â€” punteros explÃ­citos (seguros: sin aritmÃ©tica de punteros)
func duplicar(p *int) { *p *= 2 }  // alias: p y la variable original apuntan al mismo int
x := 10
duplicar(&x)
fmt.Println(x)  // 20
```

3. **Referencias en TypeScript/JavaScript**:
```typescript
const obj1 = { valor: 42 };
const obj2 = obj1;     // obj1 y obj2 son aliases del mismo objeto en heap
obj2.valor = 99;
console.log(obj1.valor);  // 99 â€” modificado a travÃ©s del alias
```

**Consecuencias:**
- Hace difÃ­cil razonar sobre el programa (cambiar un nombre afecta otros)
- Dificulta la **verificaciÃ³n de programas** y el anÃ¡lisis estÃ¡tico
- El compilador no puede optimizar bien cÃ³digo con aliases potenciales

**TypeScript â€” detecciÃ³n con `readonly`:**
```typescript
function procesarPuro(data: readonly number[]): number[] {
    // data no puede ser modificado â€” sin aliases peligrosos
    return data.map(x => x * 2);
}
```

---

### 5.2 Closures: Entorno LÃ©xico Capturado (Â§3.9)

**DefiniciÃ³n (Sebesta Â§10, Gabbrielli Â§7.4):** Una closure es la combinaciÃ³n de una funciÃ³n y el entorno lÃ©xico en el que fue definida. Captura variables del Ã¡mbito externo aunque ese Ã¡mbito haya terminado de ejecutar.

**Por quÃ© existen:** cuando una funciÃ³n accede a variables de un Ã¡mbito anidado pero no global, esas variables no pueden vivir solo en el activation record (que se destruye al retornar). Se almacenan en el **heap con duraciÃ³n extendida** (Sebesta Â§10).

```typescript
function crearContador(inicio: number) {
    let cuenta = inicio;  // â† capturada por closure

    return {
        incrementar: () => ++cuenta,  // closure sobre cuenta
        valor: () => cuenta           // closure sobre cuenta
    };
}

const c = crearContador(10);
console.log(c.incrementar());  // 11
console.log(c.incrementar());  // 12
// crearContador() ya retornÃ³, pero cuenta sigue viva en heap
```

**Lenguajes modernos** con closures completas como TypeScript:

```python
# Python â€” closures con entorno capturado (como TypeScript)
def crear_contador(inicio: int):
    cuenta = [inicio]  # lista para mutaciÃ³n en Python 2; en Python 3 usar nonlocal
    def incrementar():
        nonlocal cuenta
        cuenta += 1
        return cuenta
    return incrementar

contar = crear_contador(10)
print(contar())  # 11
print(contar())  # 12  â€” cuenta persiste en heap
```

```go
// Go â€” closures de primera clase, igual que TypeScript
func crearContador(inicio int) func() int {
    cuenta := inicio  // capturada por la closure
    return func() int {
        cuenta++
        return cuenta
    }
}
contar := crearContador(10)
fmt.Println(contar())  // 11
fmt.Println(contar())  // 12
```

```kotlin
// Kotlin â€” lambdas con captura de entorno lÃ©xico
fun crearContador(inicio: Int): () -> Int {
    var cuenta = inicio
    return { ++cuenta }  // lambda captura 'cuenta'
}
```

> **Nota sobre C:** C no tiene closures verdaderas (Gabbrielli Â§7.4). Las funciones de callback (`void (*f)(int)`) no pueden capturar entorno â€” toda variable no-local debe ser global. Esto ilustra **por contraste** quÃ© hace especial al closure: el binding del entorno lÃ©xico.

**RelaciÃ³n con el ciclo de vida de variables:**  
Las variables capturadas por una closure tienen tiempo de vida extendido â€” viven en el heap hasta que el closure es garbage-collected. Esto extiende el ciclo de vida mÃ¡s allÃ¡ del frame de pila original.

**Binding superficial vs. profundo (Gabbrielli Â§7.4):**
- **Deep binding (VinculaciÃ³n profunda):** la closure captura el entorno en el momento de su creaciÃ³n â†’ TypeScript/JavaScript, Python, Haskell  
- **Shallow binding (VinculaciÃ³n superficial):** la funciÃ³n usa el entorno en el momento de la llamada â†’ algunos lenguajes con Ã¡mbito dinÃ¡mico

```typescript
// Deep binding en JavaScript/TypeScript â€” el clÃ¡sico bug de var en loops:
const funcs: (() => number)[] = [];
for (var i = 0; i < 3; i++) {
    funcs.push(() => i);  // â† var: captura referencia a i, no valor
}
console.log(funcs[0]());  // 3, no 0 â€” i ya llegÃ³ a 3

// CorrecciÃ³n con let (deep binding por bloque):
for (let j = 0; j < 3; j++) {
    funcs.push(() => j);  // â† let: nueva j por iteraciÃ³n
}
console.log(funcs[0]());  // 0 â€” correcto
```

---

### 5.3 Garbage Collection (Â§3.10)

**Contexto (Sebesta Â§6.11, Louden Â§10.5):** Las variables de heap implÃ­citas (CategorÃ­a 4) y objetos en TypeScript/Python son liberados automÃ¡ticamente. El GC determina cuÃ¡ndo una celda es "inaccesible" y la devuelve al pool.

**Dos tÃ©cnicas principales:**

#### Reference Counting (Conteo de referencias) â€” Enfoque *eager*

Cada celda mantiene un contador de referencias activas hacia ella. Cuando el contador llega a 0, la celda se libera inmediatamente.

```
[Objeto A] â†’ ref_count: 2
     â†‘           â†‘
 [x]         [y]      // x e y apuntan a A â†’ ref_count = 2

del x  â†’  ref_count = 1
del y  â†’  ref_count = 0 â†’ LIBERAR inmediatamente
```

**Problema crÃ­tico: referencias circulares** (Louden Â§10.5):
```typescript
// TypeScript â€” referencia circular:
class Nodo {
    siguiente: Nodo | null = null;
}
const a = new Nodo();
const b = new Nodo();
a.siguiente = b;
b.siguiente = a;  // â† ciclo: a â†’ b â†’ a
// Si se "eliminan" a y b del scope externo:
// ref_count(a) = 1 (b lo apunta), ref_count(b) = 1 (a lo apunta)
// Ninguno llega a 0 â†’ memory leak con reference counting puro
```

Python usa reference counting + **cycle detector** para resolver esto.

#### Mark-and-Sweep â€” Enfoque *lazy*

Difiere la liberaciÃ³n hasta que el allocator se queda sin espacio. Opera en dos fases:

1. **Mark (Marcar):** a partir de todas las raÃ­ces conocidas (stack, variables globales), trazar transitivamente todos los objetos alcanzables â†’ marcarlos  
2. **Sweep (Barrer):** recorrer todo el heap; las celdas **no marcadas** son inaccesibles â†’ liberar  

```
Roots: [x â†’ Obj1, y â†’ Obj3]

Heap antes de sweep:
  Obj1 âœ“ (alcanzable desde x)
  Obj2   (no alcanzable â†’ LIBERAR)
  Obj3 âœ“ (alcanzable desde y)
  Obj4   (no alcanzable â†’ LIBERAR)
```

**Ventaja:** Resuelve referencias circulares correctamente  
**Desventajas:** Pausas del programa durante GC (stop-the-world), fragmentaciÃ³n del heap

**V8 (Motor de TypeScript/JavaScript):** usa un GC generacional que combina ambas tÃ©cnicas. Divide el heap en generaciÃ³n joven (minor GC frecuente) y generaciÃ³n vieja (major GC menos frecuente).

**CompactaciÃ³n:** ademÃ¡s de liberar, algunos GCs mueven los objetos para eliminar fragmentaciÃ³n, actualizando todos los punteros.

---

### 5.4 Gradual Typing: TypeScript como Caso ParadigmÃ¡tico (Â§3.11)

**(Gabbrielli Â§16.9 â€” secciÃ³n sobre TypeScript)**

**MotivaciÃ³n:** La dicotomÃ­a typing estÃ¡tico/dinÃ¡mico es absoluta en muchos lenguajes. El **gradual typing** permite al programador elegir cuÃ¡ndo y dÃ³nde quiere verificaciÃ³n estÃ¡tica.

**TypeScript â€” el ejemplo canÃ³nico de gradual typing:**

```typescript
// Zona sin tipos (dinÃ¡mico puro) â€” compatible con JavaScript
function sumar(a: any, b: any): any {
    return a + b;
}

// Zona con tipos (estÃ¡tico puro)
function sumarSeguro(a: number, b: number): number {
    return a + b;
}

// Zona intermedia â€” partial typing
function procesarElemento(elemento: unknown): string {
    if (typeof elemento === "string") {   // type narrowing
        return elemento.toUpperCase();    // aquÃ­ el tipo es string
    }
    return String(elemento);
}
```

**Gradual typing en la prÃ¡ctica:**

```typescript
// JavaScript existente â†’ TypeScript gradual
// Paso 1: archivo .js renombrado a .ts â€” compila con any implÃ­cito
// Paso 2: agregar tipos donde sea mÃ¡s crÃ­tico
// Paso 3: habilitar strict: true para mÃ¡xima cobertura

// tsconfig.json:
// { "strict": true }  â† cambia de gradual a completamente estÃ¡tico
```

**Gabbrielli:** TypeScript permite tomar una codebase JavaScript existente, agregarle anotaciones de tipo gradualmente, y compilar de vuelta a JavaScript (con optimizaciones y checks de runtime adicionales).

**Type Narrowing â€” binding de tipo en runtime dentro de tipos estÃ¡ticos:**
```typescript
type Resultado = string | number | null;

function formatear(r: Resultado): string {
    if (r === null) return "â€”";           // narrowing: r: null
    if (typeof r === "number") return r.toFixed(2);  // r: number
    return r.toUpperCase();               // r: string (Ãºnico restante)
}
```

---

### 5.5 Variables en ProgramaciÃ³n Funcional (Â§3.12)

**(Sebesta Â§5.8, Gabbrielli Â§11)**

**Contraste fundamental:** En los LP imperativos, las variables son celdas de memoria mutables. En los LP funcionales puros, **no existen variables mutables** â€” solo bindings inmutables.

```haskell
-- Haskell: NO hay variables. Solo bindings.
let x = 5      -- x se vincula a 5 PARA SIEMPRE en este scope
-- x = 6       -- â† ILEGAL: el binding no puede cambiar
```

**ImplicaciÃ³n semÃ¡ntica (Gabbrielli Â§11):**
- En FP puro: la computaciÃ³n es **reescritura de expresiones** (no modificaciÃ³n de estado)
- No hay valor-i (L-value) porque no hay concepto de direcciÃ³n modificable
- El binding es definitivo: mÃ¡s cercano a las constantes de LP imperativos que a sus variables

**Scala â€” `var` vs. `val`** (Gabbrielli Â§11):
```scala
var x = 5    // var: nombre que puede ser reasignado (variable imperativa)
val y = 5    // val: binding inmutable (como const en TypeScript)
```

**TypeScript funcional â€” inmutabilidad como prÃ¡ctica:**
```typescript
// Imperativo: muta estado
let suma = 0;
for (const x of [1, 2, 3]) suma += x;

// Funcional: sin mutaciÃ³n, solo bindings nuevos
const suma = [1, 2, 3].reduce((acc, x) => acc + x, 0);

// Objetos inmutables con readonly
type Config = Readonly<{
    host: string;
    port: number;
}>;
const cfg: Config = { host: "localhost", port: 8080 };
// cfg.host = "otro";  // âŒ Error: Cannot assign to 'host' because it is read-only
```

**Â¿Por quÃ© importa para IA?** Los LLMs tienden a generar cÃ³digo imperativo con mutaciÃ³n porque predomina en el corpus. El FP reduce bugs de aliasing y estado compartido.

---

### 5.6 GestiÃ³n de Memoria: Perspectiva Comparativa (Â§3.13)

**Â¿CÃ³mo los lenguajes modernos resuelven los problemas que C dejÃ³ expuestos?**

```typescript
// TypeScript/JavaScript â€” GC automÃ¡tico
// El programador NO gestiona memoria; V8 maneja todo
let sesion = { id: 1, datos: ["a", "b"] };  // heap
sesion = null;  // la referencia anterior queda sin refs â†’ GC la libera
// Imposible crear dangling pointer: el GC garantiza que un objeto vivo siempre es accesible
```

```python
# Python â€” GC con reference counting + cycle detector
sesion = {"id": 1, "datos": ["a", "b"]}  # heap
sesion = None   # ref_count â†’ 0 â†’ liberado inmediatamente (si no hay ciclos)
# sys.getrefcount() permite inspeccionar el conteo de referencias
```

```go
// Go â€” GC con escape analysis: el compilador decide stack vs. heap
type Sesion struct { ID int; Datos []string }
func nuevaSesion(id int) *Sesion {
    s := Sesion{ID: id}   // el compilador "escapa" s al heap porque retorna puntero
    return &s             // seguro: Go garantiza que s vive en heap
}                         // No hay dangling pointer â€” el compilador lo previene
```

```rust
// Rust â€” ownership: garantÃ­a en tiempo de compilaciÃ³n, sin GC
struct Sesion { id: u32, datos: Vec<String> }
impl Sesion {
    fn nueva(id: u32) -> Self { Sesion { id, datos: Vec::new() } }
    fn agregar(&mut self, item: String) { self.datos.push(item); }
}  // Al salir del scope: destructor automÃ¡tico (Drop trait), sin GC

// El borrow checker previene dangling pointers en compilaciÃ³n:
// let s = Sesion::nueva(1);
// let ref1 = &s;
// drop(s);           // â† Error: no se puede mover s mientras ref1 existe
// println!("{}", ref1.id);  // esto compilarÃ­a sin error en C (dangling)
```

| Aspecto | TypeScript | Python | Go | Rust |
|---------|------------|--------|-----|------|
| GestiÃ³n de memoria | GC (V8 generacional) | RC + cycle GC | GC (escape analysis) | Ownership + Drop |
| Variables estÃ¡ticas | MÃ³dule-level `let`/`const` | Module-level | Package-level `var` | `static` con lifetime `'static` |
| Acceso al valor-i | No directo (GC opaco) | `id()` expone direcciÃ³n | `&x` (puntero seguro) | `&x` (borrow) / `*mut x` (raw unsafe) |
| Variables sin inicializar | Error de compilaciÃ³n (strict) | NameError en runtime | Zero values (0, nil, "") | Error de compilaciÃ³n |
| Dangling pointer | Imposible (GC) | Imposible (GC) | Imposible (GC) | Imposible (borrow checker) |
| Aliases explÃ­citos | Referencias de objeto | Referencias de objeto | Punteros + interfaces | Borrows (inmutables o un mutable)|

---

### 5.7 â€” Bloque IA Clase 2 (12 min): Aliases, Mutabilidad y Type Narrowing

#### PatrÃ³n 1: IA genera alias de objeto sin advertencia

```typescript
// Prompt: "Duplica el objeto de configuraciÃ³n para modificarlo"
// IA genera (INCORRECTO â€” alias):
const configBackup = config;   // no es copia, es alias
configBackup.debug = true;     // modifica config tambiÃ©n!

// Correcto â€” shallow copy:
const configBackup = { ...config };

// Correcto â€” deep copy (objetos anidados):
const configBackup = JSON.parse(JSON.stringify(config));
// O con structuredClone():
const configBackup = structuredClone(config);
```

#### PatrÃ³n 2: IA genera closures con `var` (bug clÃ¡sico de binding)

```typescript
// Prompt: "Genera un array de funciones que retornen su Ã­ndice"
// IA con var (INCORRECTO):
const funcs = [];
for (var i = 0; i < 5; i++) {
    funcs.push(() => i);      // todas capturan la MISMA i
}
// funcs[0]() === 5, funcs[1]() === 5, etc.

// Correcto con let:
for (let i = 0; i < 5; i++) {
    funcs.push(() => i);      // cada iteraciÃ³n tiene su propia i
}
```

#### PatrÃ³n 3: Type narrowing como guardrail del cÃ³digo generado

```typescript
// IA genera (sin narrowing â€” puede crashear):
function procesar(valor: string | number) {
    return valor.toUpperCase();  // âŒ Error si valor es number
}

// Con narrowing â€” TypeScript obliga a manejar todos los casos:
function procesarSeguro(valor: string | number): string {
    if (typeof valor === "string") return valor.toUpperCase();
    return valor.toString();
}
// TypeScript verifica estÃ¡ticamente que todos los casos estÃ¡n cubiertos
```

---

## 6. Ejemplos Integradores

### Ejemplo 1: Las 4 categorÃ­as en un mÃ³dulo TypeScript

```typescript
// CategorÃ­a 1: estÃ¡tica (mÃ³dulo-level)
const VERSION = "1.0.0";
let sesionesActivas = 0;

class Sesion {
    // CategorÃ­a 3: heap-dynamic explÃ­cita
    private id: number;
    private datos: string[];

    constructor(id: number) {
        this.id = id;
        this.datos = [];  // array en heap
    }

    // CategorÃ­a 2: stack-dynamic
    agregar(item: string): void {
        let validado = item.trim();      // destruida al salir
        const ts = Date.now();           // destruida al salir
        this.datos.push(`${ts}: ${validado}`);
    }
}

function crearSesion(): Sesion {
    sesionesActivas++;
    return new Sesion(sesionesActivas);
    // CategorÃ­a 4: el objeto Sesion en heap, liberado por GC
}
```

### Ejemplo 2: Closure con ciclo de vida extendido

```typescript
function crearAcumulador(inicial: number) {
    let total = inicial;  // capturada â€” vivirÃ¡ en heap mientras exista la closure

    return {
        agregar: (n: number) => { total += n; },
        leer: () => total
    };
}

const acc = crearAcumulador(0);
acc.agregar(5);
acc.agregar(3);
console.log(acc.leer());  // 8
// total vive en heap aunque crearAcumulador() ya retornÃ³
```

### Ejemplo 3: Gradual typing progresivo

```typescript
// Fase 1: JavaScript puro (sin tipos)
function calcular(a, b) { return a + b; }  // any implÃ­cito

// Fase 2: Tipos parciales
function calcular(a: number, b): number { return a + b; }

// Fase 3: Tipos completos + strict
function calcular(a: number, b: number): number { return a + b; }
// 'calcular("hola", 3)' â†’ Error en compilaciÃ³n
```

---

## 7. Conexiones al Plan MÃ­nimo

| TÃ³pico plan mÃ­nimo | Clase | Cobertura |
|-------------------|-------|-----------|
| Entidades y ligaduras (VI.9) | 1 | âœ… Completo: binding definition, 6 tiempos, atributos |
| Nombres y Ã¡mbito | 1 | âœ… EstÃ¡tico y dinÃ¡mico, entorno de referencia |
| CategorÃ­as de variables | 1 | âœ… Las 4 categorÃ­as con ejemplos |
| Binding de tipos | 1 | âœ… EstÃ¡tico/dinÃ¡mico/inferencia |
| InicializaciÃ³n | 1 | âœ… Comparativa entre lenguajes |
| Aliases | 2 | âœ… Fuentes, consecuencias, detecciÃ³n |
| Closures y entorno lÃ©xico | 2 | âœ… Deep binding, ciclo de vida extendido |
| GC (gestiÃ³n automÃ¡tica) | 2 | âœ… Reference counting + mark-sweep |
| Gradual typing / TypeScript | 2 | âœ… Gabbrielli Â§16.9 â€” caso canÃ³nico |
| Variables en FP vs. imperativo | 2 | âœ… Inmutabilidad, val vs. var |

---

## 8. Stack de Lenguajes

| Rol | Lenguaje | PropÃ³sito |
|-----|----------|-----------|
| **Principal** | TypeScript | Binding estÃ¡tico con inferencia, let/const/var, gradual typing, closures, readonly |
| **Contraste moderno â€” JVM** | Kotlin | `val`/`var`, null safety, companion objects, lambdas con captura |
| **Contraste moderno â€” sistemas** | Rust | Ownership como binding explÃ­cito, borrow checker, Drop automÃ¡tico |
| **Contraste moderno â€” concurrente** | Go | Escape analysis, punteros seguros, package-level statics, closures |
| **Contraste dinÃ¡mico** | Python | Binding dinÃ¡mico, duck typing, reference counting + cycle GC |
| **Contraste funcional** | Haskell | Bindings inmutables, inferencia Hindley-Milner, sin variables mutables |
| **Gradual typing** | Scala | `var` vs `val` â€” paradigma mixto imperativo/funcional |
| **Referencia histÃ³rica** | C | Solo para contexto (dangling, malloc/free) â€” nunca como ejemplo primario |

---

## 9. Materiales Requeridos

- [ ] Slides Clase 1: 5-tupla, binding times, 4 categorÃ­as, Ã¡mbito (a generar por Roberto)
- [ ] Slides Clase 2: aliases, closures, GC diagrams, gradual typing, FP immutability
- [ ] CÃ³digo TypeScript interactivo: ejemplos de closure, type narrowing, aliases
- [ ] Diagrama de memoria: stack vs. heap (con punteros y GC)
- [ ] `variables.pdf` UNTDF 2024 (ya en ChromaDB)

---

## 10. FAQ Anticipado

**P: Â¿El `const` de TypeScript es como `val` de Haskell?**  
R: No exactamente. `const` hace inmutable la **referencia**, no el objeto. `val` de Haskell/Scala hace el binding completamente inmutable. `Object.freeze()` en JavaScript + `readonly` en TypeScript se acerca mÃ¡s.

**P: Â¿Por quÃ© `var` todavÃ­a existe en TypeScript?**  
R: Retrocompatibilidad. `var` tiene hoisting de funciÃ³n; `let`/`const` tienen hoisting de bloque con Temporal Dead Zone (TDZ) â€” no pueden usarse antes de su declaraciÃ³n â†’ error de compilaciÃ³n.

**P: Â¿V8 (Node/browsers) usa GC generacional?**  
R: SÃ­. Divide el heap en "generaciÃ³n joven" (minor GC frecuente, cheap) y "generaciÃ³n vieja" (major GC infrecuente, costoso). La mayorÃ­a de los objetos muere joven (generational hypothesis).

**P: Â¿Una closure "previene" el GC de liberar las variables capturadas?**  
R: Exactamente. Mientras la closure exista y sea accesible, las variables que captura tienen referencias activas. El GC no las libera. Es la fuente clÃ¡sica de memory leaks accidentales en JavaScript largo-running.

**P: Â¿El Ã¡mbito dinÃ¡mico existe en algÃºn lenguaje moderno?**  
R: SÃ­. Algunos dialectos de Lisp, Emacs Lisp, y Perl (`local`). El `this` de JavaScript tiene semÃ¡ntica de Ã¡mbito dinÃ¡mico (determinado por el contexto de llamada). Por eso se usa arrow functions (`=>`) en TypeScript â€” capturan `this` lÃ©xicamente.

---

## 11. Fuentes Utilizadas

1. **Sebesta, R. W.** (2019). *Concepts of Programming Languages* (12th ed.). Pearson. Cap. 5 (Names, Bindings, Scopes), Cap. 6 (Â§6.11 GC), Cap. 10 (closures en implementaciÃ³n de subprogramas).  
2. **Gabbrielli, M. & Martini, S.** (2023). *Programming Languages: Principles and Paradigms* (2nd ed.). Springer. Cap. 4 (Names & Scope), Cap. 7 (closures, binding policy), Cap. 8 (type inference), Cap. 11 (FP paradigm), Cap. 16.9 (TypeScript como gradual typing).  
3. **Louden, K. C. & Lambert, K. A.** (2012). *Programming Languages: Principles and Practices* (3rd ed.). Course Technology. Cap. 7 (Â§7.7 aliases), Cap. 10 (Â§10.3 closures, Â§10.5 GC: reference counting + mark-sweep).  
4. **Filminas UNTDF 2024.** *Cuestiones semÃ¡nticas vinculadas a Variables.* (ingesta/variables.pdf)  
5. **TypeScript Handbook.** Variable Declarations, Type Narrowing. https://www.typescriptlang.org/docs/  

---

*Generado por Lic. Marcos ðŸ—‚ï¸ â€” Topic Designer (EDU)*  
*2 clases Ã— 120 min = 240 min | Fuentes: Sebesta Cap.5/6/10 + Gabbrielli Cap.4/7/8/11/16 + Louden Cap.7/10 + Filminas UNTDF 2024*  
*Estado: Borrador â€” requiere aprobaciÃ³n del docente*

---
