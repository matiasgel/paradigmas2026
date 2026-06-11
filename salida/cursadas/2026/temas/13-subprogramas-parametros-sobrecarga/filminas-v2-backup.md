# Filminas - Tema 13A: Subprogramas, Parametros y Sobrecarga

> Curso: Paradigmas y Lenguajes de Programación · UNTDF IDEI 2026
> Cobertura: F-00 a F-18
> Referencia principal: Sebesta, *Concepts of Programming Languages*, Caps. 9, 10, 11, 12
> Referencias auxiliares: Gabbrielli-Martini §5.3, §7 · Louden §11
> Lenguaje principal: TypeScript | Contraste: Kotlin, Python, C, Modula-2
> Pipeline: v3 ? Clase: 1 ? 120 min ? Derivado del Tema 13

---


### [F-00] Portada 13A

@tipo: portada
@imagen: none

# CLASE 13A

## Subprogramas, Parámetros y Sobrecarga

- Fundamentos de subprogramas: procedimiento vs. función
- Variables locales: stack-dynamic vs. static
- Pasaje de parámetros: modos y métodos
- Closures y subprogramas de orden superior
- Sobrecarga y polimorfismo paramétrico
- Implementación: activation records y stack

---

### [F-01] Subprograma: La Unidad de Abstracción de Comportamiento

@tipo: concepto-abstracto
@imagen: none

# Subprograma: Unidad de Abstracción de Comportamiento

## Definición (Sebesta §9.1)

> "Un subprograma tiene una sola entrada y, salvo en el caso de la recursividad, el subprograma en ejecución es el único activo."

## Características fundamentales

- **Única entrada**: el flujo siempre inicia desde el mismo punto de definición
- **Llamador suspende**: quien invoca cede el control temporalmente
- **Retorno de control**: al completarse, vuelve al punto de invocación
- **Parámetro formal**: definido en el encabezado — `function f(x: number)`
- **Parámetro real (actual)**: provisto en el sitio de llamada — `f(42)`

`[Sebesta, §9.1, p. 389]`

---

### [F-02] Procedimiento vs. Función

@tipo: tabla-comparativa
@imagen: none

# Procedimiento vs. Función

| Criterio | Procedimiento | Función |
|----------|--------------|---------|
| **Propósito** | Producir un efecto lateral | Computar y retornar un valor |
| **Retorna** | `void` / nada | Un valor tipado |
| **Ada** | `procedure P(...)` | `function F(...) return T` |
| **C** | `void f(...)` | `int f(...)` |
| **Python** | `def p()` → retorna `None` | `def f(): return v` |
| **Haskell** | *(solo funciones puras)* | `f :: A -> B` |
| **TypeScript** | `function p(): void` | `function f(): T` |

> La distinción es **semántica** en la mayoría de lenguajes; en Ada es **sintáctica y obligatoria**

`[Gabbrielli/Martini, §5.1 · Sebesta, §9.1]`

---

### [F-03] Perfil y Protocolo

@tipo: concepto-abstracto
@imagen: none

# Perfil y Protocolo de un Subprograma

## Perfil de parámetros (Sebesta §9.1)

- Número, orden y **tipos** de los parámetros formales
- Ejemplo: `(peso: number, altura: number)` → perfil de `calcularIMC`

## Protocolo

- Perfil de parámetros **+** tipo de retorno
- Ejemplo: `(number, number) → number`
- En TypeScript: `(peso: number, altura: number): number`

## Equivalencias terminológicas

- Haskell: **type signature** — `calcIMC :: Float -> Float -> Float`
- Java/C#: **method signature** — nombre + perfil (sin tipo de retorno)
- Ada: **subprogram specification** — spec + tipo de retorno obligatorio

`[Sebesta, §9.1, pp. 392–394]`

---

### [F-04] Variables Locales: Stack-Dynamic vs. Static

@tipo: concepto-abstracto
@imagen: none

# Variables Locales: Duración ≠ Alcance

## Stack-Dynamic (default en lenguajes modernos)

- Creadas al invocar → existen en el **activation record** del frame actual
- Destruidas al retornar → liberadas del stack automáticamente
- **Soporte para recursividad**: cada llamada tiene su propio frame independiente
- TS, Python, Kotlin, Java, Go — usan este modelo

## Variables Estáticas Locales

- Asignadas UNA vez al inicio → persisten entre llamadas (*history-sensitive*)
- `static int contador = 0;` en C/C++ dentro de función
- Fortran 77: **estáticas por defecto** → sin recursividad por diseño de lenguaje
- Útiles para contadores o caches entre llamadas sucesivas

`[Sebesta, §9.2, pp. 394–396]`

---

### [F-05] Código TypeScript: Función Pura vs. Procedimiento

@tipo: codigo
@imagen: none

# Función Pura vs. Procedimiento en TypeScript

```typescript
// Procedimiento: efecto lateral, retorna void
function registrarAcceso(usuario: string): void {
  console.log(`[${new Date().toISOString()}] Acceso: ${usuario}`);
  // Sin valor de retorno — actúa sobre el entorno externo
}

// Función pura: computa y retorna un valor, sin efectos laterales
function calcularIMC(peso: number, altura: number): number {
  return peso / (altura * altura);
}

// Perfil:    (peso: number, altura: number)
// Protocolo: (number, number) → number

const imc: number = calcularIMC(70, 1.75);  // 22.857...
registrarAcceso("matias");                   // [timestamp] Acceso: matias
```

---

### [F-06] Métodos de Pasaje de Parámetros

@tipo: tabla-comparativa
@imagen: none

# Métodos de Pasaje de Parámetros

| Método | Flujo | Descripción | Lenguajes |
|--------|-------|-------------|-----------|
| **Pass-by-value** | in | Copia el valor; cambios no se propagan | C, Java (prim.), TypeScript (prim.) |
| **Pass-by-result** | out | Copia resultado al retorno | Ada (`out`) |
| **Pass-by-value-result** | in-out | Copia in + copia out al retorno | Ada (`in out`), FORTRAN |
| **Pass-by-reference** | in-out | Pasa dirección; cambios se propagan al original | C++ (`&`), Fortran, Ada (`access`) |
| **Pass-by-name** | — | Sustitución textual lazy (histórico) | Algol 60, Scala (by-name params) |

> En TypeScript: primitivos → pass-by-value · objetos → **pass-by-sharing** (referencia copiada, objeto compartido)

`[Sebesta, §9.5, pp. 403–420]`

---

### [F-07] Código TypeScript: Pass-by-Value vs. Pass-by-Sharing

@tipo: codigo
@imagen: none

# Pass-by-Value (Primitivos) vs. Pass-by-Sharing (Objetos)

```typescript
// Primitivos → copia del valor; el original no cambia
function doblar(n: number): number {
  n = n * 2;   // modifica la copia local únicamente
  return n;
}
let x = 10;
doblar(x);
console.log(x);   // 10 — sin cambio ✓

// Objetos → la referencia es copiada; el objeto es compartido
function agregarItem(arr: number[], item: number): void {
  arr.push(item);  // modifica el MISMO objeto en heap
}
const lista: number[] = [1, 2, 3];
agregarItem(lista, 99);
console.log(lista);  // [1, 2, 3, 99] — ¡sí cambió! ✓
```

---

### [F-08] Socrática: ¿Qué Pasa con Pass-by-Sharing?

@tipo: socratica
@imagen: none

# ¿TypeScript Pasa Objetos por Valor o por Referencia?

```typescript
function cambiarNombre(obj: { nombre: string }): void {
  obj.nombre = "cambiado";        // línea A: modifica la propiedad
  obj = { nombre: "nuevo obj" };  // línea B: reasigna la variable local
}

const persona = { nombre: "original" };
cambiarNombre(persona);
console.log(persona.nombre);  // ¿"original", "cambiado" o "nuevo obj"?
```

## Preguntas para el aula

- ¿Cuál de las dos líneas (A o B) afecta a `persona` fuera de la función?
- ¿La reasignación en la línea B cambia `persona`? ¿Por qué?
- ¿Cómo llamarías a este mecanismo? ¿Pass-by-value? ¿Pass-by-reference?

> **Respuesta**: imprime `"cambiado"`. La reasignación (B) afecta solo la copia local de la referencia — esto es **pass-by-sharing**.

---

### [F-09] Closures y Captura del Entorno Léxico

@tipo: codigo
@imagen: none

# Closures: Captura del Entorno Léxico

```typescript
// Closure: la función devuelta "cierra sobre" la variable x
function makeAdder(x: number): (y: number) => number {
  // x vive en el activation record de makeAdder
  // la función anónima lo captura → x sobrevive al retorno
  return (y: number): number => x + y;
}

const sumar5  = makeAdder(5);
const sumar10 = makeAdder(10);

console.log(sumar5(3));   // 8  ← x=5 capturado
console.log(sumar10(3));  // 13 ← x=10 capturado

// Cada closure tiene su propio entorno léxico con x independiente
// El GC mantiene vivo el scope de makeAdder mientras la closure exista
```

> La closure es un **subprograma + su entorno de referencia** en el momento de creación

`[Sebesta, §9.12, pp. 439–440]`

---

### [F-10] Subprogramas como Parámetros: Funciones de Orden Superior

@tipo: codigo
@imagen: none

# Subprogramas como Parámetros (Higher-Order Functions)

```typescript
type Predicado<T>        = (item: T) => boolean;
type Transformacion<A,B> = (item: A) => B;

function filtrar<T>(arr: T[], pred: Predicado<T>): T[] {
  return arr.filter(pred);
}

function transformar<A, B>(arr: A[], fn: Transformacion<A, B>): B[] {
  return arr.map(fn);
}

const nums      = [1, 2, 3, 4, 5, 6];
const pares     = filtrar(nums, n => n % 2 === 0);     // [2, 4, 6]
const cuadrados = transformar(pares, n => n ** 2);     // [4, 16, 36]
```

> El tipo del parámetro `pred` es un **tipo de función**: `(item: T) => boolean`

`[Sebesta, §9.11, pp. 435–437]`

---

### [F-11] Sobrecarga: Polimorfismo Ad Hoc

@tipo: concepto-abstracto
@imagen: none

# Sobrecarga: Polimorfismo Ad Hoc

## Definición (Sebesta §9.8)

> "Un subprograma sobrecargado es uno que tiene el **mismo nombre** que otro subprograma en el mismo entorno de referencia."

> "Los subprogramas sobrecargados **no necesitan comportarse de manera similar**."

## Ad hoc vs. paramétrico

| | Ad hoc (sobrecarga) | Paramétrico (genérico) |
|--|---------------------|------------------------|
| Implementaciones | Múltiples distintas | Una única genérica |
| Selección | Por tipos de argumentos en compilación | Por parámetro de tipo `<T>` |
| Ejemplo TS | `procesar(string)` vs `procesar(number)` | `identidad<T>(x: T): T` |

## Advertencia (Sebesta §9.8)
- Sobrecarga + parámetros por defecto → **ambigüedad posible** en el sitio de llamada

`[Sebesta, §9.8, pp. 429–432]`

---

### [F-12] Código TypeScript: Overload Signatures

@tipo: codigo
@imagen: none

# Overload Signatures en TypeScript

```typescript
// Overload signatures — contratos de tipo (SIN implementación)
function procesar(input: string): string;
function procesar(input: number): number;
function procesar(input: boolean): string;

// Implementación unificada — más permisiva que las signatures
function procesar(input: string | number | boolean): string | number {
  if (typeof input === 'string')  return input.toUpperCase();
  if (typeof input === 'number')  return input * 2;
  return input ? 'verdadero' : 'falso';
}

procesar("hola");   // → string: "HOLA"
procesar(21);       // → number: 42
procesar(true);     // → string: "verdadero"
// procesar([1,2]); // Error TS: no hay signature para array ✓
```

> TypeScript selecciona la signature correcta en **tiempo de compilación** por tipo de argumento

---

### [F-13] Socrática: Sobrecarga + Defaults → Ambigüedad

@tipo: socratica
@imagen: none

# Sobrecarga + Parámetros por Defecto: ¿Quién Gana?

## Caso en C++ (Sebesta §9.8)

```cpp
// C++ — ambas declaraciones son válidas individualmente
void fun(float b = 0.0);  // puede llamarse fun() por el default
void fun();               // también acepta fun()

fun();  // ← AMBIGUO: el compilador no puede decidir cuál usar
```

## Preguntas para el aula

- ¿Por qué TypeScript evita este problema con sus overload signatures?
- ¿Cuándo es preferible usar genéricos en lugar de sobrecarga?
- ¿La sobrecarga de `+` en Python (para `int` y `str`) es ad hoc o paramétrica?

> **En TypeScript**: la implementación unificada siempre es más permisiva → el compilador no enfrenta ambigüedad al resolver la signature correcta.

`[Sebesta, §9.8, pp. 430–431]`

---

### [F-14] Polimorfismo Paramétrico y Subprogramas Genéricos

@tipo: concepto-abstracto
@imagen: none

# Polimorfismo Paramétrico y Genéricos

## Definición (Sebesta §9.9)

> "El polimorfismo paramétrico es provisto por un subprograma que toma **parámetros genéricos** usados en expresiones de tipo que describen los tipos de los parámetros."

> "Un subprograma genérico es uno cuyo cómputo puede realizarse sobre datos de **distintos tipos** en distintas activaciones."

## Una implementación — múltiples instanciaciones

- `sort<T>` reemplaza `sortInt`, `sortString`, `sortFloat`...
- TypeScript: inferencia de tipos automática en la mayoría de casos
- C++: templates — instanciación explícita en tiempo de compilación

## Reutilización de software (Sebesta §9.10)

> "La reutilización del software puede ser grandemente facilitada por los subprogramas genéricos."

`[Sebesta, §9.9–9.10, pp. 432–438]`

---

### [F-15] Código TypeScript: Generic Functions con Constraints

@tipo: codigo
@imagen: none

# Generic Functions con Constraints en TypeScript

```typescript
// Sin constraint — T puede ser cualquier tipo
function primerElemento<T>(coleccion: T[]): T | undefined {
  return coleccion.length > 0 ? coleccion[0] : undefined;
}
const p1 = primerElemento([1, 2, 3]);    // T inferred: number → 1
const p2 = primerElemento(["a", "b"]);   // T inferred: string → "a"

// Con constraint: T debe satisfacer la interfaz Comparable<T>
interface Comparable<T> {
  compareTo(other: T): number;  // retorna -1, 0, o 1
}

function máximo<T extends Comparable<T>>(a: T, b: T): T {
  return a.compareTo(b) >= 0 ? a : b;
}
```

> `extends` en el parámetro de tipo impone un **constraint**: T debe satisfacer la interfaz

---

### [F-16] Diagrama: Activation Records y Stack de Llamadas

@tipo: diagrama
@imagen: none

# Activation Records — `factorial(3)` Recursivo

```
Stack de llamadas                    Código TypeScript
─────────────────────────            ───────────────────────────────────────
┌─────────────────────────┐ ← tope   function factorial(n: number): number {
│  AR: factorial(1)       │            if (n <= 1) return 1;
│  n = 1  │ retval: 1     │            return n * factorial(n - 1);
│  dynamic link ────────┐ │          }
├───────────────────────│─┤
│  AR: factorial(2)     │←┘
│  n = 2  │ retval: 2*1 │
│  dynamic link ────────┐ │
├───────────────────────│─┤
│  AR: factorial(3)     │←┘
│  n = 3  │ retval: 3*2 │
│  dynamic link → main  │
└─────────────────────────┘ ← base
```

> Cada llamada crea un **nuevo** activation record — así la recursividad es posible

`[Sebesta, §10.3, pp. 453–458 · Gabbrielli, §5.3.3]`

---

### [F-17] Implementación de Subprogramas: Semántica de Call/Return

@tipo: concepto-abstracto
@imagen: none

# Semántica de Call y Return (Sebesta §10.1)

## Al momento de la llamada (CALL)

1. Se crea un nuevo **activation record** (AR) en el stack
2. Se copian / pasan los **parámetros** al AR
3. Se guarda la **dirección de retorno** (program counter)
4. Se guarda el **dynamic link** (AR del llamador)
5. El control salta al **punto de entrada** del subprograma

## Al momento del retorno (RETURN)

1. Se evalúa el **valor de retorno** (si lo hay)
2. Se restaura el **stack pointer** al AR del llamador via dynamic link
3. Se restaura el **program counter** (dirección de retorno guardada)
4. El AR del subprograma se **libera** del stack

`[Sebesta, §10.1–10.3, pp. 441–458]`

---

### [F-18] Cierre 13A

@tipo: cierre
@imagen: none

# Cierre Clase 13A — Mapa de Conceptos

| Concepto | Clave |
|----------|-------|
| **Subprograma** | Única entrada, llamador suspende, retorno de control |
| **Perfil / Protocolo** | Tipos de params / perfil + tipo de retorno |
| **Stack-dynamic** | Variable local por frame → habilita recursión |
| **Pass-by-sharing** | Referencia copiada: propiedades mutables, reasignación local no |
| **Closure** | Subprograma + entorno léxico capturado en creación |
| **Sobrecarga** | Mismo nombre, distintas implementaciones (ad hoc) |
| **Genéricos** | Una implementación `<T>` para múltiples tipos |
| **Activation Record** | Frame con params, variables locales, return address, dynamic link |

## → Próxima clase: ADTs, Módulos e Interfaces en TypeScript

---
