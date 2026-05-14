# Diseño — Tema 09: Variables, Binding y Ámbito

> **Agente:** Lic. Marcos 🗂️ — Topic Designer  
> **Fecha:** 2026-05-11  
> **Estado:** 🔲 Borrador — pendiente de aprobación docente  
> **Duración:** **240 min (2 clases de 120 min)**  
> **Lenguaje principal:** TypeScript  
> **Lenguajes de contraste:** Python (binding dinámico, tipado duck), Kotlin (val/var, null safety), Go (zero values, punteros seguros), Rust (ownership como binding explícito), Haskell (bindings inmutables)  
> **Fuente primaria:** Sebesta — *Concepts of Programming Languages* (Pearson 2019), Cap. 5–6  
> **Fuentes secundarias:** Gabbrielli & Martini — *Programming Languages: Principles and Paradigms* (Springer 2023), Cap. 4, 7, 16; Louden & Lambert — *Programming Languages: Principles and Practices* (2012), Cap. 7, 10; Filminas UNTDF 2024  
> **Bloque IA (Clase 1):** Errores de ámbito en código generado. Variables globales silenciosas  
> **Bloque IA (Clase 2):** Aliases y mutabilidad como fuente de bugs en LLMs. Type narrowing como guardrail  

---

## 1. Contexto en el Plan

**Posición:** Tema 09 de 15 — Bloque post-OO, pre-tipos  
**Duración expandida:** 2 clases × 120 min = **240 min totales**  
**Tópico del plan mínimo:** Entidades y ligaduras (VI.9)  
**Conexiones:**  
- → Tema 08 (OO TypeScript): el `this`, los objetos son variables con atributos; paso de objetos por referencia  
- → Tema 10 (Tipos de Datos): el tipo es uno de los atributos de la variable; union types, discriminated unions  
- → Tema 14 (Sistemas de Tipos): binding estático de tipos en TypeScript, inferencia, gradual typing  

---

## 2. Objetivos de Aprendizaje

Al finalizar las 2 clases el alumno debe poder:

| # | Objetivo | Nivel Bloom |
|---|----------|-------------|
| OA1 | Describir la variable como 5-tupla `<nombre, dirección, tipo, valor-i, valor-d>` | Recordar |
| OA2 | Distinguir los 6 momentos de binding: diseño, implementación, compilación, linkeo, carga, ejecución | Comprender |
| OA3 | Clasificar variables según sus 4 categorías de tiempo de vida y zona de almacenamiento | Analizar |
| OA4 | Comparar ámbito estático vs. dinámico: reglas de resolución, ventajas y problemas | Analizar |
| OA5 | Analizar aliases: identificar sus fuentes (punteros, parámetros ref, uniones), razonar sobre sus implicancias en verificación formal y análisis estático | Analizar |
| OA6 | Analizar closures: comparar binding profundo vs. superficial, evaluar consecuencias en el ciclo de vida de variables y en la semántica de programas funcionales | Analizar |
| OA7 | Comparar garbage collection (reference counting vs. mark-sweep) con gestión manual de memoria | Analizar |
| OA8 | Explicar gradual typing y el rol de TypeScript como lenguaje gradualmente tipado | Comprender |
| OA9 | Contrastar variables mutables (imperativo) con bindings inmutables (funcional) | Analizar |
| OA10 | Aplicar reglas de ámbito estático y type narrowing en código TypeScript | Aplicar |
| OA11 | Detectar errores de ámbito, aliases y mutabilidad en código generado por IA | Evaluar |

---

## 3. Tópicos, Tiempo Estimado y Distribución por Clase

### Clase 1 (120 min) — Variable, Binding, Almacenamiento y Ámbito

| # | Tópico | Tiempo | Fuente |
|---|--------|--------|--------|
| 3.1 | Variable como abstracción. La 5-tupla | 10 min | Sebesta §5.3, filminas |
| 3.2 | Atributos: nombre, dirección, tipo, valor-i, valor-d | 12 min | Sebesta §5.3.1–5.3.4, filminas |
| 3.3 | Binding: definición y 6 tiempos de vinculación | 15 min | Sebesta §5.4, filminas |
| 3.4 | Binding de tipos: estático vs. dinámico + inferencia | 12 min | Sebesta §5.4.1–5.4.2, Gabbrielli §8 |
| 3.5 | Binding de almacenamiento: 4 categorías de variables | 18 min | Sebesta §5.4.3, filminas |
| 3.6 | Ámbito estático vs. dinámico | 15 min | Sebesta §5.5, Gabbrielli §4.3 |
| 3.7 | Entorno de referencia. Constantes. Inicialización | 8 min | Sebesta §5.6–5.8, filminas |
| — | **Bloque IA:** globales silenciosas, `var` hoisting, prompts seguros | 12 min | — |
| — | Buffer / preguntas | 8 min | — |
| **Total** | | **110 min + 10 buffer** | |

### Clase 2 (120 min) — Aliases, Closures, GC, Gradual Typing y Variables en FP

| # | Tópico | Tiempo | Fuente |
|---|--------|--------|--------|
| 3.8 | Aliases: definición, fuentes (punteros, ref params, union types) | 15 min | Sebesta §5.3.3, Louden §7.7 |
| 3.9 | Closures: entorno léxico capturado, ciclo de vida extendido | 18 min | Sebesta §10, Gabbrielli §7.4, Louden §10.3 |
| 3.10 | Garbage Collection: reference counting vs. mark-sweep | 18 min | Sebesta §6.11, Louden §10.5 |
| 3.11 | Gradual typing: TypeScript como caso paradigmático | 15 min | Gabbrielli §16.9 |
| 3.12 | Variables en programación funcional: sin mutabilidad | 12 min | Sebesta §5.8 (FP), Gabbrielli §11 |
| 3.13 | Contraste multilenguaje: Python, Kotlin, Go, Rust — gestión de memoria moderna | 10 min | Sebesta §5.4.3, Gabbrielli §16 |
| — | **Bloque IA:** aliases y mutabilidad, type narrowing como guardrail | 12 min | — |
| — | Buffer / preguntas | 10 min | — |
| **Total** | | **110 min + 10 buffer** | |

---

## 4. Desarrollo de Contenidos — Clase 1

### 4.1 Variable como Abstracción

**Contexto arquitectural:**  
La arquitectura Von Neumann tiene dos componentes clave: memoria (celdas con dirección) y procesador. Los lenguajes abstraen eso:

| Elemento concreto | Abstracción en LP |
|------------------|-------------------|
| Celda de memoria | **Variable** |
| Dirección de celda | **Nombre/identificador** |
| Modificación destructiva | **Sentencia de asignación** |

**Los 6 atributos de una variable** (Sebesta §5.3 — formalización central):

Sebesta enumera seis atributos que caracterizan completamente una variable:

| Atributo | Notación | Descripción |
|----------|----------|-------------|
| **Nombre** | — | Identificador simbólico; puede no existir (variables anónimas) |
| **Dirección** | L-value | Celda(s) de memoria asociada(s); una variable puede tener distintas direcciones en distintos sitios del programa o en distintas activaciones recursivas |
| **Tipo** | — | Conjunto de valores posibles + operaciones legales + representación interna |
| **Valor** | R-value | Contenido codificado almacenado según el tipo |
| **Tiempo de vida** | lifetime | Período durante el cual la variable está vinculada a una dirección |
| **Ámbito** | scope | Rango de instrucciones donde el nombre es visible |

> **Distinción L-value / R-value (Sebesta §5.3.2):** en `x = y`, `x` denota dirección (L-value) e `y` denota contenido (R-value). Un mismo nombre puede tener distintos L-values en distintas invocaciones (recursión) o en distintos módulos. **L-value ≠ R-value** — esto es fundamental para entender aliases y paso por referencia.

Algunos textos condensan estos atributos en una **5-tupla** eliminando el tiempo de vida como atributo explícito (agrupándolo con el ámbito) o el nombre (variables anónimas). La tupla que usaremos:

```
Variable = <nombre, dirección, tipo, l-valor, r-valor>   [+ ámbito como atributo de contexto]
```

```typescript
// TypeScript — la 5-tupla en acción
let contador: number = 42;
//   ↑nombre  ↑tipo    ↑valor-d
// valor-i = dirección de memoria asignada por el runtime (oculta)
// ámbito  = bloque donde está declarado

// TypeScript oculta el valor-i — no hay acceso directo a la dirección
// Rust lo hace explícito de forma segura:
// let x = 42i32;           // binding: nombre x → tipo i32 → valor 42
// let addr = &x as *const i32;  // valor-i visible como puntero raw
```

```python
# Python — equivalente dinámico: la 5-tupla con binding en runtime
contador = 42          # nombre: contador, tipo: int (inferido), valor-d: 42
id(contador)           # id() expone el valor-i (dirección del objeto)
type(contador)         # int — binding de tipo dinámico
```

```kotlin
// Kotlin — la 5-tupla con null safety integrada
var contador: Int = 42    // mutable — valor-i puede cambiar de valor-d
val limite: Int = 100     // inmutable — binding de valor-d fijo desde creación
```

> 📌 **Sebesta §5.3.2:** Un mismo nombre puede tener distintas direcciones en distintos lugares del programa (funciones diferentes) o en distintos momentos de ejecución (recursión). **L-value ≠ R-value** — esto es fundamental para entender aliases y paso por referencia.

---

### 4.2 Atributos de Variables

#### Nombre / Identificador

El nombre de una variable participa en tres mecanismos formales que determinan cómo se resuelven las referencias:

- **Resolución de nombres:** el proceso por el que un compilador o intérprete mapea un identificador a la entidad que denota. En ámbito estático, esta resolución es en compilación; en dinámico, en ejecución.
- **Espacios de nombres (namespaces):** partición del espacio de identificadores para evitar colisiones. TypeScript usa módulos ES; Rust usa `mod` explícito con árbol de módulos; Go usa paquetes con visibilidad determinada por mayúscula/minúscula del identificador.
- **Aliasing de nombres:** un mismo objeto puede tener múltiples nombres (ver §5.1). La distinción entre el nombre y la entidad denotada es central para entender el comportamiento de programas con efectos secundarios.

> **Variables sin nombre (anónimas):** literales como `new Nodo(42)` crean objetos en heap sin asignarles nombre — tienen dirección (L-value) y valor (R-value) pero no nombre. Son heap-dynamic implícitas que solo son accesibles mientras exista al menos una referencia a ellas.

#### Tipo

Define: (a) rango de valores posibles, (b) operaciones legales, (c) representación interna.  
TypeScript extiende esto con **structural typing** — el tipo es compatible por estructura, no por nombre nominal.

#### Valor-d (R-value) y Valor-i (L-value)

El contenido codificado de la celda, interpretado según el tipo.  
En `x = y`: `x` denota dirección (valor-i), `y` denota contenido (valor-d).

---

### 4.3 Binding (Vinculación)

**Definición (Sebesta §5.4):** Binding es la asociación entre una entidad del programa y un atributo. Ocurre en distintos momentos:

| Momento | Descripción | Ejemplo |
|---------|-------------|---------|
| **Tiempo de diseño** | Significados posibles para símbolos | `*` = multiplicación |
| **Tiempo de implementación** | Rango de valores para tipos primitivos | `int` de 32 o 64 bits según arquitectura |
| **Tiempo de compilación** | Variable → tipo (C, Java, TypeScript) | `int count;` |
| **Tiempo de linkeo** | Llamada a librería → código del subprograma | `printf` en libc |
| **Tiempo de carga** | Variables globales → celdas de memoria | variables estáticas globales |
| **Tiempo de ejecución** | Variable → valor | `count = count + 5` |

**Ejemplo integrador en TypeScript** — los mismos 6 momentos:
```typescript
let count: number;
count = count + 5;
// Tipos posibles para una variable    → tiempo de diseño del lenguaje
// Tipo de count (number)              → tiempo de compilación (inferencia TS)
// Rango de valores de number          → tiempo de implementación (IEEE 754 float64)
// Valor de count                      → tiempo de ejecución
// Significado del operador +          → tiempo de compilación
// Representación interna del literal 5 → tiempo de diseño del compilador
```

**Comparativa de binding de tipos en lenguajes modernos:**

| Lenguaje | Binding de tipo | Momento |
|----------|----------------|---------|
| TypeScript | Estático + inferencia | Compilación |
| Kotlin | Estático + inferencia | Compilación |
| Go | Estático + inferencia (`:=`) | Compilación |
| Rust | Estático + inferencia (Hindley-Milner) | Compilación |
| Python | Dinámico (+ type hints opcionales) | Ejecución |
| JavaScript | Dinámico | Ejecución |

---

### 4.4 Binding de Tipos

#### Binding Estático (Declaración Explícita)

```typescript
let i: number;          // TypeScript — explícito
let x = 5;              // TypeScript — inferencia: x: number
```

**Inferencia de tipos** (Gabbrielli §8): el compilador determina el tipo sin declaración explícita. TypeScript usa inferencia bidireccional:

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

#### Binding Dinámico de Tipos

```python
x = [2, 3, 4, 5]        # x: list
x = "uno, dos, tres"     # x: str — binding de tipo cambió en runtime
```

**Problema:** Errores de tipo no detectables en compilación; mayor overhead.

#### Gradual Typing (avance — profundización en Clase 2 §3.11)

TypeScript es el ejemplo canónico: permite mezclar zonas con tipos estáticos y dinámicas (`any`).

---

#### Tipado Fuerte vs. Débil — Dimensión Ortogonal (Sebesta §5.4.2, Gabbrielli §8.3)

**Esta dimensión es ortogonal a estático/dinámico.** Un lenguaje puede ser estático y débil (C), estático y fuerte (Haskell, Rust), dinámico y fuerte (Python), o gradual (TypeScript).

| | **Tipado fuerte** | **Tipado débil** |
|---|---|---|
| **Definición** | Cada operación verifica compatibilidad de tipos; no hay conversiones implícitas inseguras | Se permiten conversiones implícitas arbitrarias; el sistema "coacciona" el tipo |
| **Error de tipo** | Error en compilación o excepción en runtime | Comportamiento silencioso (resultado incorrecto sin aviso) |
| **Ejemplos** | Haskell, Rust, Python, TypeScript (strict) | C, JavaScript, PHP |

**Coerciones** (conversiones implícitas de tipo): cuando el compilador o runtime convierte automáticamente un tipo en otro para satisfacer una operación:

```typescript
// TypeScript — coerciones explícitas (strong) vs. JavaScript (weak):

// JavaScript (débil) — coerciones implícitas silenciosas:
// "5" + 3   →  "53"   (number coercionado a string)
// "5" - 3   →  2      (string coercionada a number)
// null + 1  →  1      (null coercionado a 0)

// TypeScript (strong) — el mismo código es error de compilación:
const a: string = "5";
const b: number = 3;
// a + b  →  Error TS2365: Operator '+' cannot be applied to types 'string' and 'number'
// Se requiere conversión explícita: Number(a) + b  →  8
```

```python
# Python — fuerte y dinámico: rechaza coerciones implícitas inseguras
x = "5"
y = 3
# x + y  →  TypeError: can only concatenate str (not "int") to str
# Explícito requerido: int(x) + y  →  8
```

```c
// C — débil y estático: permite coerciones arbitrarias sin aviso
int i = 65;
char c = i;        // i coercionado a char silenciosamente → 'A'
float *fp = &i;    // puntero a int interpretado como puntero a float: undefined behavior
```

> **Implicación para diseño de LP (Gabbrielli §8.3):** El tipado fuerte es la tendencia dominante en lenguajes modernos porque los errores de tipo son detectables estáticamente o generan excepciones explícitas. El tipado débil sacrifica seguridad por conveniencia (interoperabilidad C-legacy, scripting rápido). Rust lleva el tipado fuerte al extremo: **no hay coerciones implícitas de ningún tipo** — toda conversión es una llamada explícita (`.into()`, `as`, `From::from()`).

**Widening vs. Narrowing (conversiones seguras e inseguras):**
```typescript
// Widening (ensanchamiento) — siempre seguro, puede ser implícito:
let i: number = 42;
let f: number = i;         // number → number: trivial (TypeScript usa float64 para todo)

// En Java (analogía): int → long → float → double (sin pérdida de información)

// Narrowing (estrechamiento) — potencialmente inseguro, siempre explícito:
let n: number = 3.14;
let truncado: number = Math.trunc(n);  // 3 — debe ser explícito
// En Rust: i64 as i32  →  truncación, explícito obligatorio
```

---

### 4.5 Binding de Almacenamiento: 4 Categorías

**Tiempo de vida:** período durante el cual la variable está vinculada a una dirección específica de memoria. *(Sebesta §5.4.3)*

#### Categoría 1 — Variables Estáticas

Vinculadas antes de la ejecución, permanecen hasta el fin del programa.

```typescript
// TypeScript — variable de módulo: estática en la práctica
let sesionesActivas = 0;        // vive toda la vida del módulo
const VERSION = "1.0.0";        // estática e inmutable

// Patrón módulo con estado estático:
let _cache: Map<string, string> | null = null;
export function getCache() {
    _cache ??= new Map();  // inicialización lazy — una sola vez
    return _cache;
}
```

```kotlin
// Kotlin — companion object (equivalente a static de clase)
class Sesion {
    companion object {
        private var contadorGlobal = 0   // estático de clase
        fun nuevaId() = ++contadorGlobal
    }
}
```

```go
// Go — package-level variable: estática
var sesionesActivas int = 0  // vive toda la vida del paquete
const version = "1.0.0"      // constante: binding en tiempo de compilación
```

**Ventajas:** Eficiencia (dirección conocida en compilación), historial entre llamadas  
**Desventajas:** No soporta recursión efectiva, ocupa memoria siempre

#### Categoría 2 — Variables Dinámicas de Pila (Stack-dynamic)

Creadas al activar el subprograma, destruidas al retornar.

```typescript
function calcular(n: number): number {
    let resultado = 0;  // stack-dynamic
    let temp = n * 2;   // stack-dynamic
    return resultado + temp;
    // Al retornar: resultado y temp destruidas
}
```

**Permite recursión** porque cada activación tiene su propio frame en la pila.  
**Stack Overflow:** la pila tiene tamaño máximo definido por el SO.

**Activation Record (Registro de Activación) — Sebesta §9.3:**  
Cada llamada a subprograma crea un *activation record* (o *stack frame*) con la siguiente estructura típica:

```
┌───────────────────────────────────┐
│  Parámetros del subprograma       │ ← accesibles por nombre en el cuerpo
│  Variables locales (stack-dynamic)│ ← creadas al activar, destruidas al retornar
│  Valor de retorno                 │
│  Static link (enlace estático)    │ ← apunta al activation record del padre léxico
│  Dynamic link (enlace dinámico)   │ ← apunta al activation record del llamador
│  Dirección de retorno             │
└───────────────────────────────────┘
```

- El **static link** implementa el acceso a variables no locales en ámbito estático (sube la cadena de padres léxicos)
- El **dynamic link** permite restaurar el frame anterior al retornar
- En **recursión**, cada llamada genera un frame independiente → las variables locales no se comparten entre llamadas

```typescript
function factorial(n: number): number {
    // 'n' y el valor de retorno: stack-dynamic
    // Cada llamada recursiva tiene su propio 'n' en su propio frame
    if (n <= 1) return 1;
    return n * factorial(n - 1);
    // Al retornar: este frame destruido, frame del llamador restaurado vía dynamic link
}
```

#### Categoría 3 — Variables Dinámicas de Heap Explícitas

Asignadas y liberadas explícitamente. En lenguajes modernos, la *gestión* puede ser automática (GC) o garantizada por el compilador (ownership).

```typescript
// TypeScript — new asigna en heap; GC libera automáticamente
class Nodo {
    constructor(
        public valor: number,
        public siguiente: Nodo | null = null
    ) {}
}
let cabeza = new Nodo(42);      // asignado en heap
cabeza = new Nodo(99);          // el Nodo(42) queda sin referencias → GC lo libera
```

```kotlin
// Kotlin — igual que TypeScript: JVM GC gestiona el heap
data class Nodo(val valor: Int, val siguiente: Nodo? = null)
var cabeza: Nodo? = Nodo(42)
cabeza = Nodo(99)   // Nodo(42) → eligible para GC
```

```rust
// Rust — heap explícita con ownership: el compilador garantiza la liberación
let elemento = Box::new(42);    // Box<i32> asigna en heap
// Al salir del scope: destructor automático — sin GC, sin leak posible
// Si se intenta usar después del drop → error de compilación (borrow checker)
```

> **Contraste de paradigmas de gestión:** TypeScript/Kotlin → GC automático; Rust → ownership + compile-time; C → manual (malloc/free, propenso a leaks y dangling pointers)

#### Categoría 4 — Variables Dinámicas de Heap Implícitas

Todos sus atributos (tipo, valor, dirección) se establecen cuando se les asigna un valor. Típico de lenguajes con binding dinámico de tipos.

```python
# Python — el caso más claro: la variable no existe hasta la asignación
x = [1, 2, 3]          # x: list, todos sus atributos vinculados aquí
x = "uno, dos, tres"   # x: str — todos los atributos (tipo+valor+dir) cambian
x = 42                 # x: int
type(x)                # int — binding de tipo determinado en runtime
```

```typescript
// TypeScript con 'any' — se aproxima a Cat. 4 (pero desaconsejado)
let x: any = [1, 2, 3];
x = "uno, dos, tres";   // binding de tipo cambia — TypeScript permite con any

// Con tipos: TypeScript es Cat. 2/3 — el tipo queda fijo desde la declaración
let items: number[] = [1, 2, 3];  // tipo fijado en compilación (no Cat. 4 real)
```

---

### 4.6 Ámbito (Scope)

**Definición:** Rango de instrucciones donde el nombre de una variable es visible.

#### Ámbito Estático (Léxico)

Introducido por ALGOL 60. Determinado en **tiempo de compilación**.

**Algoritmo de resolución:**
1. Buscar en ámbito local → 2. Buscar en el bloque padre estático → ... → Error de compilación si no se encuentra

```typescript
let x = 10;  // ámbito: módulo

function externa() {
    let y = 20;
    function interna() {
        let z = 30;
        console.log(x);  // ✅ antepasado estático: módulo
        console.log(y);  // ✅ antepasado estático: externa
    }
    // console.log(z);  // ❌ z no visible aquí
}
```

**Problema de ámbito estático (Sebesta §5.5.5):**  
Variables del programa principal son visibles en **todos** los procedimientos → acceso involuntario a demasiados datos. Tendencia a crear más variables globales de las necesarias.

#### Ámbito Dinámico

Determinado en **tiempo de ejecución** según la cadena de llamadas.

**Algoritmo:** buscar en la declaración local → subprograma que llamó → antepasados dinámicos → Runtime Error si no se encuentra.

**Problemas (Sebesta §5.5.4):**
- Variables locales del llamador son visibles en el llamado → sin protección
- Imposibilidad de verificación estática de tipos para no-locales
- Acceso más lento que ámbito estático
- Programas difíciles de leer (hay que rastrear la cadena de llamadas)

**Conclusión Sebesta:** Ámbito estático produce programas más legibles, confiables y rápidos. Por eso reemplazó al dinámico en la mayoría de los dialectos modernos de Lisp.

> **Nota histórica (Sebesta §5.5.1):** El ámbito estático fue introducido por **ALGOL 60** — uno de los aportes más influyentes de ese lenguaje. Los primeros dialectos de **Lisp** usaban ámbito dinámico (facilita implementación con lista de asociaciones); **Common Lisp** (1984) adoptó ámbito estático como default. Hoy Emacs Lisp mantiene dinámico opcionalmente. El `this` de JavaScript tiene semántica de ámbito **dinámico** (se resuelve en tiempo de llamada), de ahí que TypeScript recomiende arrow functions para capturarlo léxicamente.

---

#### Agujeros de Ámbito (Scope Holes) — Sebesta §5.5.5

Cuando una variable local de un bloque anidado **tiene el mismo nombre** que una variable del bloque envolvente, la variable exterior queda **oculta** en el bloque interior. El rango de instrucciones donde la variable exterior es visible pero no accesible por nombre se llama **agujero de ámbito**.

```typescript
let x = 10;           // x exterior — ámbito: módulo completo

function procesarLista(items: number[]): void {
    // Aquí x exterior es visible: 10
    for (const item of items) {
        const x = item * 2;   // x interior — oculta x exterior
        // "scope hole" de x exterior: empieza aquí
        console.log(x);       // 20, 40, ... — x interior
        // "scope hole" de x exterior: termina al salir del bloque for
    }
    // x exterior visible nuevamente: 10
    console.log(x);
}
```

**Consecuencias:**
- El acceso a la variable exterior no es posible dentro del agujero usando su nombre original
- Algunos lenguajes (Ada) permiten acceder a través de **nombres calificados** (`Paquete.x`); TypeScript no tiene esa salida
- Los linters modernos detectan shadowing: `@typescript-eslint/no-shadow` produce advertencia en el ejemplo anterior

```typescript
// ESLint: @typescript-eslint/no-shadow
// Warning: 'x' is already declared in the upper scope (line 1)
// Esto es evidencia de que el scope hole es un problema de legibilidad
// reconocido en la industria como bad practice
```

**Contraste con ámbito dinámico:** en ámbito dinámico no existen scope holes en el mismo sentido, porque la resolución usa la cadena de llamadas, no la estructura del texto del programa.

---

---

### 4.7 Entorno de Referencia. Constantes. Inicialización

**Entorno de referencia:** colección de todos los identificadores visibles en una sentencia dada.

**Constantes:**
```typescript
const PI = 3.14159;           // binding inmutable: referencia y valor
const CONFIG = { debug: false }; // binding inmutable de referencia; objeto mutable
```

**Inicialización** (Sebesta §5.4.3): binding variable → valor en el momento del binding de almacenamiento.

| Lenguaje | Comportamiento con variables no inicializadas |
|----------|----------------------------------------------|
| C | Variables estáticas → 0; locales → basura (undefined behavior) |
| Java | Numéricas → 0; booleanas → false; objetos → null |
| TypeScript (`strict: true`) | Detecta usos antes de asignación en compilación |
| Python | Cada asignación inicializa; uso sin asignación → NameError |

---

### 4.8 — Bloque IA Clase 1 (12 min): Errores de Ámbito

#### Patrón 1: `var` hoisting silencioso

```typescript
// Código generado típico por IA (malas prácticas):
function procesar(activo: boolean) {
    if (activo) {
        var resultado = "ok";   // ← IA usa var (corpus pre-ES6)
    }
    console.log(resultado);     // undefined — no ReferenceError
    // Con let → ReferenceError explícito y correcto
}
```

#### Patrón 2: Variable global silenciosa

```typescript
// IA genera efecto secundario implícito:
let total = 0;  // global oculta
function acumular(n: number) {
    total += n;  // muta global sin advertencia
    return total;
}

// Correcto — sin efectos secundarios:
function acumularPuro(total: number, n: number): number {
    return total + n;
}
```

#### Patrón 3: Shadowing inesperado

```typescript
const limite = 100;
function validar(items: number[]) {
    const limite = items.length;  // ← shadowing silencioso
    return items.filter(x => x < limite);  // ¿qué limite?
}
```

**Prompt seguro:**
```
"TypeScript strict mode. Declara todo con let/const (nunca var).
Sin variables globales — todas las dependencias son parámetros explícitos.
Declara el tipo de cada parámetro."
```

---

## 5. Desarrollo de Contenidos — Clase 2

### 5.1 Aliases (§3.8)

**Definición (Sebesta §5.3.3, Louden §7.7):** Un alias ocurre cuando dos nombres distintos están vinculados al mismo objeto (misma celda de memoria) en el mismo momento.

**Fuentes de aliases:**

1. **Referencias de objeto en TypeScript** (fuente más común hoy):

2. **Parámetros por referencia** (Kotlin, Go):

```kotlin
// Kotlin — los objetos se pasan por referencia (alias implícito)
data class Punto(var x: Int, var y: Int)
fun desplazar(p: Punto, dx: Int) { p.x += dx }  // alias: p apunta al mismo objeto
val origen = Punto(0, 0)
desplazar(origen, 5)
println(origen.x)  // 5 — ¡el objeto fue modificado a través del alias!
```

```go
// Go — punteros explícitos (seguros: sin aritmética de punteros)
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
console.log(obj1.valor);  // 99 — modificado a través del alias
```

**Consecuencias:**
- Hace difícil razonar sobre el programa (cambiar un nombre afecta otros)
- Dificulta la **verificación de programas** y el análisis estático
- El compilador no puede optimizar bien código con aliases potenciales

**TypeScript — detección con `readonly`:**
```typescript
function procesarPuro(data: readonly number[]): number[] {
    // data no puede ser modificado — sin aliases peligrosos
    return data.map(x => x * 2);
}
```

---

### 5.2 Closures: Entorno Léxico Capturado (§3.9)

**Definición (Sebesta §10, Gabbrielli §7.4):** Una closure es la combinación de una función y el entorno léxico en el que fue definida. Captura variables del ámbito externo aunque ese ámbito haya terminado de ejecutar.

**Por qué existen:** cuando una función accede a variables de un ámbito anidado pero no global, esas variables no pueden vivir solo en el activation record (que se destruye al retornar). Se almacenan en el **heap con duración extendida** (Sebesta §10).

```typescript
function crearContador(inicio: number) {
    let cuenta = inicio;  // ← capturada por closure

    return {
        incrementar: () => ++cuenta,  // closure sobre cuenta
        valor: () => cuenta           // closure sobre cuenta
    };
}

const c = crearContador(10);
console.log(c.incrementar());  // 11
console.log(c.incrementar());  // 12
// crearContador() ya retornó, pero cuenta sigue viva en heap
```

**Lenguajes modernos** con closures completas como TypeScript:

```python
# Python — closures con entorno capturado (como TypeScript)
def crear_contador(inicio: int):
    cuenta = [inicio]  # lista para mutación en Python 2; en Python 3 usar nonlocal
    def incrementar():
        nonlocal cuenta
        cuenta += 1
        return cuenta
    return incrementar

contar = crear_contador(10)
print(contar())  # 11
print(contar())  # 12  — cuenta persiste en heap
```

```go
// Go — closures de primera clase, igual que TypeScript
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
// Kotlin — lambdas con captura de entorno léxico
fun crearContador(inicio: Int): () -> Int {
    var cuenta = inicio
    return { ++cuenta }  // lambda captura 'cuenta'
}
```

> **Nota sobre C:** C no tiene closures verdaderas (Gabbrielli §7.4). Las funciones de callback (`void (*f)(int)`) no pueden capturar entorno — toda variable no-local debe ser global. Esto ilustra **por contraste** qué hace especial al closure: el binding del entorno léxico.

**Relación con el ciclo de vida de variables:**  
Las variables capturadas por una closure tienen tiempo de vida extendido — viven en el heap hasta que el closure es garbage-collected. Esto extiende el ciclo de vida más allá del frame de pila original.

**Binding superficial vs. profundo (Gabbrielli §7.4):**
- **Deep binding (Vinculación profunda):** la closure captura el entorno en el momento de su creación → TypeScript/JavaScript, Python, Haskell  
- **Shallow binding (Vinculación superficial):** la función usa el entorno en el momento de la llamada → algunos lenguajes con ámbito dinámico

```typescript
// Deep binding en JavaScript/TypeScript — el clásico bug de var en loops:
const funcs: (() => number)[] = [];
for (var i = 0; i < 3; i++) {
    funcs.push(() => i);  // ← var: captura referencia a i, no valor
}
console.log(funcs[0]());  // 3, no 0 — i ya llegó a 3

// Corrección con let (deep binding por bloque):
for (let j = 0; j < 3; j++) {
    funcs.push(() => j);  // ← let: nueva j por iteración
}
console.log(funcs[0]());  // 0 — correcto
```

---

### 5.3 Garbage Collection (§3.10)

**Contexto (Sebesta §6.11, Louden §10.5):** Las variables de heap implícitas (Categoría 4) y objetos en TypeScript/Python son liberados automáticamente. El GC determina cuándo una celda es "inaccesible" y la devuelve al pool.

**Dos técnicas principales:**

#### Reference Counting (Conteo de referencias) — Enfoque *eager*

Cada celda mantiene un contador de referencias activas hacia ella. Cuando el contador llega a 0, la celda se libera inmediatamente.

```
[Objeto A] → ref_count: 2
     ↑           ↑
 [x]         [y]      // x e y apuntan a A → ref_count = 2

del x  →  ref_count = 1
del y  →  ref_count = 0 → LIBERAR inmediatamente
```

**Problema crítico: referencias circulares** (Louden §10.5):
```typescript
// TypeScript — referencia circular:
class Nodo {
    siguiente: Nodo | null = null;
}
const a = new Nodo();
const b = new Nodo();
a.siguiente = b;
b.siguiente = a;  // ← ciclo: a → b → a
// Si se "eliminan" a y b del scope externo:
// ref_count(a) = 1 (b lo apunta), ref_count(b) = 1 (a lo apunta)
// Ninguno llega a 0 → memory leak con reference counting puro
```

Python usa reference counting + **cycle detector** para resolver esto.

#### Mark-and-Sweep — Enfoque *lazy*

Difiere la liberación hasta que el allocator se queda sin espacio. Opera en dos fases:

1. **Mark (Marcar):** a partir de todas las raíces conocidas (stack, variables globales), trazar transitivamente todos los objetos alcanzables → marcarlos  
2. **Sweep (Barrer):** recorrer todo el heap; las celdas **no marcadas** son inaccesibles → liberar  

```
Roots: [x → Obj1, y → Obj3]

Heap antes de sweep:
  Obj1 ✓ (alcanzable desde x)
  Obj2   (no alcanzable → LIBERAR)
  Obj3 ✓ (alcanzable desde y)
  Obj4   (no alcanzable → LIBERAR)
```

**Ventaja:** Resuelve referencias circulares correctamente  
**Desventajas:** Pausas del programa durante GC (stop-the-world), fragmentación del heap

**V8 (Motor de TypeScript/JavaScript):** usa un GC generacional que combina ambas técnicas. Divide el heap en generación joven (minor GC frecuente) y generación vieja (major GC menos frecuente).

**Compactación:** además de liberar, algunos GCs mueven los objetos para eliminar fragmentación, actualizando todos los punteros.

---

### 5.4 Gradual Typing: TypeScript como Caso Paradigmático (§3.11)

**(Gabbrielli §16.9 — sección sobre TypeScript)**

**Motivación:** La dicotomía typing estático/dinámico es absoluta en muchos lenguajes. El **gradual typing** permite al programador elegir cuándo y dónde quiere verificación estática.

**TypeScript — el ejemplo canónico de gradual typing:**

```typescript
// Zona sin tipos (dinámico puro) — compatible con JavaScript
function sumar(a: any, b: any): any {
    return a + b;
}

// Zona con tipos (estático puro)
function sumarSeguro(a: number, b: number): number {
    return a + b;
}

// Zona intermedia — partial typing
function procesarElemento(elemento: unknown): string {
    if (typeof elemento === "string") {   // type narrowing
        return elemento.toUpperCase();    // aquí el tipo es string
    }
    return String(elemento);
}
```

**Gradual typing en la práctica:**

```typescript
// JavaScript existente → TypeScript gradual
// Paso 1: archivo .js renombrado a .ts — compila con any implícito
// Paso 2: agregar tipos donde sea más crítico
// Paso 3: habilitar strict: true para máxima cobertura

// tsconfig.json:
// { "strict": true }  ← cambia de gradual a completamente estático
```

**Gabbrielli:** TypeScript permite tomar una codebase JavaScript existente, agregarle anotaciones de tipo gradualmente, y compilar de vuelta a JavaScript (con optimizaciones y checks de runtime adicionales).

**Type Narrowing — binding de tipo en runtime dentro de tipos estáticos:**
```typescript
type Resultado = string | number | null;

function formatear(r: Resultado): string {
    if (r === null) return "—";           // narrowing: r: null
    if (typeof r === "number") return r.toFixed(2);  // r: number
    return r.toUpperCase();               // r: string (único restante)
}
```

---

### 5.5 Variables en Programación Funcional (§3.12)

**(Sebesta §5.8, Gabbrielli §11)**

**Contraste fundamental:** En los LP imperativos, las variables son celdas de memoria mutables. En los LP funcionales puros, **no existen variables mutables** — solo bindings inmutables.

```haskell
-- Haskell: NO hay variables. Solo bindings.
let x = 5      -- x se vincula a 5 PARA SIEMPRE en este scope
-- x = 6       -- ← ILEGAL: el binding no puede cambiar
```

**Implicación semántica (Gabbrielli §11):**
- En FP puro: la computación es **reescritura de expresiones** (no modificación de estado)
- No hay valor-i (L-value) porque no hay concepto de dirección modificable
- El binding es definitivo: más cercano a las constantes de LP imperativos que a sus variables

**Scala — `var` vs. `val`** (Gabbrielli §11):
```scala
var x = 5    // var: nombre que puede ser reasignado (variable imperativa)
val y = 5    // val: binding inmutable (como const en TypeScript)
```

**TypeScript funcional — inmutabilidad como práctica:**
```typescript
// Imperativo: muta estado
let suma = 0;
for (const x of [1, 2, 3]) suma += x;

// Funcional: sin mutación, solo bindings nuevos
const suma = [1, 2, 3].reduce((acc, x) => acc + x, 0);

// Objetos inmutables con readonly
type Config = Readonly<{
    host: string;
    port: number;
}>;
const cfg: Config = { host: "localhost", port: 8080 };
// cfg.host = "otro";  // ❌ Error: Cannot assign to 'host' because it is read-only
```

**¿Por qué importa para IA?** Los LLMs tienden a generar código imperativo con mutación porque predomina en el corpus. El FP reduce bugs de aliasing y estado compartido.

---

### 5.6 Gestión de Memoria: Perspectiva Comparativa (§3.13)

**¿Cómo los lenguajes modernos resuelven los problemas que C dejó expuestos?**

```typescript
// TypeScript/JavaScript — GC automático
// El programador NO gestiona memoria; V8 maneja todo
let sesion = { id: 1, datos: ["a", "b"] };  // heap
sesion = null;  // la referencia anterior queda sin refs → GC la libera
// Imposible crear dangling pointer: el GC garantiza que un objeto vivo siempre es accesible
```

```python
# Python — GC con reference counting + cycle detector
sesion = {"id": 1, "datos": ["a", "b"]}  # heap
sesion = None   # ref_count → 0 → liberado inmediatamente (si no hay ciclos)
# sys.getrefcount() permite inspeccionar el conteo de referencias
```

```go
// Go — GC con escape analysis: el compilador decide stack vs. heap
type Sesion struct { ID int; Datos []string }
func nuevaSesion(id int) *Sesion {
    s := Sesion{ID: id}   // el compilador "escapa" s al heap porque retorna puntero
    return &s             // seguro: Go garantiza que s vive en heap
}                         // No hay dangling pointer — el compilador lo previene
```

```rust
// Rust — ownership: garantía en tiempo de compilación, sin GC
struct Sesion { id: u32, datos: Vec<String> }
impl Sesion {
    fn nueva(id: u32) -> Self { Sesion { id, datos: Vec::new() } }
    fn agregar(&mut self, item: String) { self.datos.push(item); }
}  // Al salir del scope: destructor automático (Drop trait), sin GC

// El borrow checker previene dangling pointers en compilación:
// let s = Sesion::nueva(1);
// let ref1 = &s;
// drop(s);           // ← Error: no se puede mover s mientras ref1 existe
// println!("{}", ref1.id);  // esto compilaría sin error en C (dangling)
```

| Aspecto | TypeScript | Python | Go | Rust |
|---------|------------|--------|-----|------|
| Gestión de memoria | GC (V8 generacional) | RC + cycle GC | GC (escape analysis) | Ownership + Drop |
| Variables estáticas | Módule-level `let`/`const` | Module-level | Package-level `var` | `static` con lifetime `'static` |
| Acceso al valor-i | No directo (GC opaco) | `id()` expone dirección | `&x` (puntero seguro) | `&x` (borrow) / `*mut x` (raw unsafe) |
| Variables sin inicializar | Error de compilación (strict) | NameError en runtime | Zero values (0, nil, "") | Error de compilación |
| Dangling pointer | Imposible (GC) | Imposible (GC) | Imposible (GC) | Imposible (borrow checker) |
| Aliases explícitos | Referencias de objeto | Referencias de objeto | Punteros + interfaces | Borrows (inmutables o un mutable)|

---

### 5.7 — Bloque IA Clase 2 (12 min): Aliases, Mutabilidad y Type Narrowing

#### Patrón 1: IA genera alias de objeto sin advertencia

```typescript
// Prompt: "Duplica el objeto de configuración para modificarlo"
// IA genera (INCORRECTO — alias):
const configBackup = config;   // no es copia, es alias
configBackup.debug = true;     // modifica config también!

// Correcto — shallow copy:
const configBackup = { ...config };

// Correcto — deep copy (objetos anidados):
const configBackup = JSON.parse(JSON.stringify(config));
// O con structuredClone():
const configBackup = structuredClone(config);
```

#### Patrón 2: IA genera closures con `var` (bug clásico de binding)

```typescript
// Prompt: "Genera un array de funciones que retornen su índice"
// IA con var (INCORRECTO):
const funcs = [];
for (var i = 0; i < 5; i++) {
    funcs.push(() => i);      // todas capturan la MISMA i
}
// funcs[0]() === 5, funcs[1]() === 5, etc.

// Correcto con let:
for (let i = 0; i < 5; i++) {
    funcs.push(() => i);      // cada iteración tiene su propia i
}
```

#### Patrón 3: Type narrowing como guardrail del código generado

```typescript
// IA genera (sin narrowing — puede crashear):
function procesar(valor: string | number) {
    return valor.toUpperCase();  // ❌ Error si valor es number
}

// Con narrowing — TypeScript obliga a manejar todos los casos:
function procesarSeguro(valor: string | number): string {
    if (typeof valor === "string") return valor.toUpperCase();
    return valor.toString();
}
// TypeScript verifica estáticamente que todos los casos están cubiertos
```

---

## 6. Ejemplos Integradores

### Ejemplo 1: Las 4 categorías en un módulo TypeScript

```typescript
// Categoría 1: estática (módulo-level)
const VERSION = "1.0.0";
let sesionesActivas = 0;

class Sesion {
    // Categoría 3: heap-dynamic explícita
    private id: number;
    private datos: string[];

    constructor(id: number) {
        this.id = id;
        this.datos = [];  // array en heap
    }

    // Categoría 2: stack-dynamic
    agregar(item: string): void {
        let validado = item.trim();      // destruida al salir
        const ts = Date.now();           // destruida al salir
        this.datos.push(`${ts}: ${validado}`);
    }
}

function crearSesion(): Sesion {
    sesionesActivas++;
    return new Sesion(sesionesActivas);
    // Categoría 4: el objeto Sesion en heap, liberado por GC
}
```

### Ejemplo 2: Closure con ciclo de vida extendido

```typescript
function crearAcumulador(inicial: number) {
    let total = inicial;  // capturada — vivirá en heap mientras exista la closure

    return {
        agregar: (n: number) => { total += n; },
        leer: () => total
    };
}

const acc = crearAcumulador(0);
acc.agregar(5);
acc.agregar(3);
console.log(acc.leer());  // 8
// total vive en heap aunque crearAcumulador() ya retornó
```

### Ejemplo 3: Gradual typing progresivo

```typescript
// Fase 1: JavaScript puro (sin tipos)
function calcular(a, b) { return a + b; }  // any implícito

// Fase 2: Tipos parciales
function calcular(a: number, b): number { return a + b; }

// Fase 3: Tipos completos + strict
function calcular(a: number, b: number): number { return a + b; }
// 'calcular("hola", 3)' → Error en compilación
```

---

## 7. Conexiones al Plan Mínimo

| Tópico plan mínimo | Clase | Cobertura |
|-------------------|-------|-----------|
| Entidades y ligaduras (VI.9) | 1 | ✅ Completo: binding definition, 6 tiempos, atributos |
| Nombres y ámbito | 1 | ✅ Estático y dinámico, entorno de referencia |
| Categorías de variables | 1 | ✅ Las 4 categorías con ejemplos |
| Binding de tipos | 1 | ✅ Estático/dinámico/inferencia |
| Inicialización | 1 | ✅ Comparativa entre lenguajes |
| Aliases | 2 | ✅ Fuentes, consecuencias, detección |
| Closures y entorno léxico | 2 | ✅ Deep binding, ciclo de vida extendido |
| GC (gestión automática) | 2 | ✅ Reference counting + mark-sweep |
| Gradual typing / TypeScript | 2 | ✅ Gabbrielli §16.9 — caso canónico |
| Variables en FP vs. imperativo | 2 | ✅ Inmutabilidad, val vs. var |

---

## 8. Stack de Lenguajes

| Rol | Lenguaje | Propósito |
|-----|----------|-----------|
| **Principal** | TypeScript | Binding estático con inferencia, let/const/var, gradual typing, closures, readonly |
| **Contraste moderno — JVM** | Kotlin | `val`/`var`, null safety, companion objects, lambdas con captura |
| **Contraste moderno — sistemas** | Rust | Ownership como binding explícito, borrow checker, Drop automático |
| **Contraste moderno — concurrente** | Go | Escape analysis, punteros seguros, package-level statics, closures |
| **Contraste dinámico** | Python | Binding dinámico, duck typing, reference counting + cycle GC |
| **Contraste funcional** | Haskell | Bindings inmutables, inferencia Hindley-Milner, sin variables mutables |
| **Gradual typing** | Scala | `var` vs `val` — paradigma mixto imperativo/funcional |
| **Referencia histórica** | C | Solo para contexto (dangling, malloc/free) — nunca como ejemplo primario |

---

## 9. Materiales Requeridos

- [ ] Slides Clase 1: 5-tupla, binding times, 4 categorías, ámbito (a generar por Roberto)
- [ ] Slides Clase 2: aliases, closures, GC diagrams, gradual typing, FP immutability
- [ ] Código TypeScript interactivo: ejemplos de closure, type narrowing, aliases
- [ ] Diagrama de memoria: stack vs. heap (con punteros y GC)
- [ ] `variables.pdf` UNTDF 2024 (ya en ChromaDB)

---

## 10. FAQ Anticipado

**P: ¿El `const` de TypeScript es como `val` de Haskell?**  
R: No exactamente. `const` hace inmutable la **referencia**, no el objeto. `val` de Haskell/Scala hace el binding completamente inmutable. `Object.freeze()` en JavaScript + `readonly` en TypeScript se acerca más.

**P: ¿Por qué `var` todavía existe en TypeScript?**  
R: Retrocompatibilidad. `var` tiene hoisting de función; `let`/`const` tienen hoisting de bloque con Temporal Dead Zone (TDZ) — no pueden usarse antes de su declaración → error de compilación.

**P: ¿V8 (Node/browsers) usa GC generacional?**  
R: Sí. Divide el heap en "generación joven" (minor GC frecuente, cheap) y "generación vieja" (major GC infrecuente, costoso). La mayoría de los objetos muere joven (generational hypothesis).

**P: ¿Una closure "previene" el GC de liberar las variables capturadas?**  
R: Exactamente. Mientras la closure exista y sea accesible, las variables que captura tienen referencias activas. El GC no las libera. Es la fuente clásica de memory leaks accidentales en JavaScript largo-running.

**P: ¿El ámbito dinámico existe en algún lenguaje moderno?**  
R: Sí. Algunos dialectos de Lisp, Emacs Lisp, y Perl (`local`). El `this` de JavaScript tiene semántica de ámbito dinámico (determinado por el contexto de llamada). Por eso se usa arrow functions (`=>`) en TypeScript — capturan `this` léxicamente.

---

## 11. Fuentes Utilizadas

1. **Sebesta, R. W.** (2019). *Concepts of Programming Languages* (12th ed.). Pearson. Cap. 5 (Names, Bindings, Scopes), Cap. 6 (§6.11 GC), Cap. 10 (closures en implementación de subprogramas).  
2. **Gabbrielli, M. & Martini, S.** (2023). *Programming Languages: Principles and Paradigms* (2nd ed.). Springer. Cap. 4 (Names & Scope), Cap. 7 (closures, binding policy), Cap. 8 (type inference), Cap. 11 (FP paradigm), Cap. 16.9 (TypeScript como gradual typing).  
3. **Louden, K. C. & Lambert, K. A.** (2012). *Programming Languages: Principles and Practices* (3rd ed.). Course Technology. Cap. 7 (§7.7 aliases), Cap. 10 (§10.3 closures, §10.5 GC: reference counting + mark-sweep).  
4. **Filminas UNTDF 2024.** *Cuestiones semánticas vinculadas a Variables.* (ingesta/variables.pdf)  
5. **TypeScript Handbook.** Variable Declarations, Type Narrowing. https://www.typescriptlang.org/docs/  

---

*Generado por Lic. Marcos 🗂️ — Topic Designer (EDU)*  
*2 clases × 120 min = 240 min | Fuentes: Sebesta Cap.5/6/10 + Gabbrielli Cap.4/7/8/11/16 + Louden Cap.7/10 + Filminas UNTDF 2024*  
*Estado: Borrador — requiere aprobación del docente*

---
