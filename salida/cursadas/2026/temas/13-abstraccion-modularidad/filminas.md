# Filminas — Tema 13: Estructuración de Programas (Módulo X)

> Curso: Paradigmas y Lenguajes de Programación · UNTDF IDEI 2026
> Cobertura: F-00 a F-38
> Referencia principal: Sebesta, *Concepts of Programming Languages*, Caps. 9, 10, 11, 12
> Referencias auxiliares: Gabbrielli-Martini §5.3, §7 · Louden §11
> Lenguaje principal: TypeScript | Contraste: Kotlin, Python, C, Modula-2
> Pipeline: v3 · Clases: 2 × 120 min · Generado: 2026-06-08

---

## PORTADA GENERAL

---

### [F-00] Portada

@tipo: portada
@imagen: none
@slide-artefact: tipo=NONE, descripcion="Portada del tema con título, módulo, institución y bibliografía"

# Estructuración de Programas

### Módulo X — Abstracción Procedural, Modularidad y Genéricos

Paradigmas y Lenguajes de Programación · Semana 13 · UNTDF IDEI 2026

*Bibliografía: Sebesta — Caps. 9, 10, 11, 12 · Gabbrielli §5, 7 · Louden §11*

---

## AGENDA

---

### [F-01] Agenda: 2 Clases del Módulo X

@tipo: tabla
@imagen: none
@slide-artefact: tipo=TABLE, descripcion="Tabla con dos filas (Clase 13A y 13B), columnas: Clase, Contenido principal, Duración"

# Dos Clases — 240 Minutos

| # | Clase | Contenido | Duración |
|---|-------|-----------|----------|
| **13A** | Subprogramas, Parámetros y Sobrecarga | Fundamentos · Variables Locales · Pasaje · Closures · Overloading · Activation Records | 120 min |
| **13B** | Módulos, Interfaces y Genéricos | ADTs · Interfaz/Impl · Módulos · Compilación · Genéricos · Síntesis | 120 min |

> *"La abstracción permite ignorar detalles irrelevantes. La modularidad permite distribuir la complejidad."*

---

## CLASE 13A — Subprogramas, Parámetros y Sobrecarga

---

### [F-02] Portada 13A

@tipo: portada
@imagen: none
@slide-artefact: tipo=NONE, descripcion="Portada de Clase 13A con subtítulo y lista de temas principales"

# CLASE 13A

## Subprogramas, Parámetros y Sobrecarga

- Fundamentos de subprogramas: procedimiento vs. función
- Variables locales: stack-dynamic vs. static
- Pasaje de parámetros: modos y métodos
- Closures y subprogramas de orden superior
- Sobrecarga y polimorfismo paramétrico
- Implementación: activation records y stack

---

### [F-03] Subprograma: La Unidad de Abstracción de Comportamiento

@tipo: concepto-abstracto
@imagen: none
@slide-artefact: tipo=NONE, descripcion="Definición formal de subprograma con cinco características numeradas: única entrada, llamador suspende, retorno de control, parámetro formal, parámetro real"

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

### [F-04] Procedimiento vs. Función

@tipo: tabla-comparativa
@imagen: none
@slide-artefact: tipo=TABLE, descripcion="Tabla comparativa de procedimiento vs función por criterio (propósito, retorno) y por lenguaje: Ada, C, Python, Haskell, TypeScript"

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

### [F-05] Perfil y Protocolo

@tipo: concepto-abstracto
@imagen: none
@slide-artefact: tipo=NONE, descripcion="Diagrama textual mostrando la relación entre perfil (número, orden y tipos de parámetros) y protocolo (perfil + tipo de retorno), con ejemplo TypeScript de calcularIMC"

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

### [F-06] Variables Locales: Stack-Dynamic vs. Static

@tipo: concepto-abstracto
@imagen: none
@slide-artefact: tipo=TABLE, descripcion="Tabla comparando stack-dynamic vs static local con filas: duración, soporte recursión, lenguajes, comportamiento entre llamadas"

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

### [F-07] Código TypeScript: Función Pura vs. Procedimiento

@tipo: codigo
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="Dos funciones TypeScript: registrarAcceso (void, efecto lateral) y calcularIMC (number, pura). Comentarios marcando perfil y protocolo"

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

### [F-08] Métodos de Pasaje de Parámetros

@tipo: tabla-comparativa
@imagen: none
@slide-artefact: tipo=TABLE, descripcion="Tabla de 5 métodos de pasaje: columnas Método, Dirección de flujo, Descripción, Lenguajes que lo usan"

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

### [F-09] Código TypeScript: Pass-by-Value vs. Pass-by-Sharing

@tipo: codigo
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="Dos bloques: (1) primitivo number no cambia al llamar doblar(x), (2) array sí cambia al llamar agregarItem(lista, 99). Comentarios explicando el comportamiento"

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

### [F-10] Socrática: ¿Qué Pasa con Pass-by-Sharing?

@tipo: socratica
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="Función cambiarNombre que modifica obj.nombre (línea A) y luego reasigna obj (línea B). Pregunta: ¿qué imprime persona.nombre?"

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

### [F-11] Closures y Captura del Entorno Léxico

@tipo: codigo
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="makeAdder en TypeScript: retorna función que cierra sobre x. Dos instancias sumar5 y sumar10. Comentarios sobre activation record y GC"

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

### [F-12] Subprogramas como Parámetros: Funciones de Orden Superior

@tipo: codigo
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="TypeScript: tipos Predicado<T> y Transformacion<A,B> como tipos de función. Funciones filtrar y transformar que reciben funciones como parámetros. Pipeline: nums → pares → cuadrados"

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

### [F-13] Sobrecarga: Polimorfismo Ad Hoc

@tipo: concepto-abstracto
@imagen: none
@slide-artefact: tipo=TABLE, descripcion="Tabla comparativa de polimorfismo ad hoc (sobrecarga) vs paramétrico: columnas tipo, implementaciones, selección, ejemplo TypeScript"

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

### [F-14] Código TypeScript: Overload Signatures

@tipo: codigo
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="Tres overload signatures de procesar (string→string, number→number, boolean→string) seguidas de implementación unificada. Tres llamadas con tipos inferidos en compilación"

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

### [F-15] Socrática: Sobrecarga + Defaults → Ambigüedad

@tipo: socratica
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="Código C++ con dos declaraciones fun(): una con float b=0.0 y otra sin parámetros. Llamada fun() resulta ambigua. Contraste con TypeScript que evita el problema"

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

### [F-16] Polimorfismo Paramétrico y Subprogramas Genéricos

@tipo: concepto-abstracto
@imagen: none
@slide-artefact: tipo=NONE, descripcion="Definiciones formales de polimorfismo paramétrico y subprograma genérico citando Sebesta §9.9-9.10, con comparación de instanciaciones y beneficio de reutilización"

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

### [F-17] Código TypeScript: Generic Functions con Constraints

@tipo: codigo
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="Función primerElemento<T> con inferencia de tipo y función máximo<T extends Comparable<T>> con interface Comparable. Ejemplos de uso mostrando inferencia automática de T"

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

### [F-18] Diagrama: Activation Records y Stack de Llamadas

@tipo: diagrama
@imagen: none
@slide-artefact: tipo=SHAPE_DIAGRAM, descripcion="Diagrama de pila con tres activation records para factorial(3→2→1). Cada frame tiene nombre de función, variable n, retval, y dynamic link apuntando al frame inferior. Tope del stack arriba."

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

### [F-19] Implementación de Subprogramas: Semántica de Call/Return

@tipo: concepto-abstracto
@imagen: none
@slide-artefact: tipo=SHAPE_DIAGRAM, descripcion="Diagrama de dos columnas: pasos al llamar (CALL) y al retornar (RETURN), con numeración 1-5 en cada columna. Flechas entre llamador y subprograma"

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

### [F-20] Cierre 13A

@tipo: cierre
@imagen: none
@slide-artefact: tipo=TABLE, descripcion="Tabla resumen de 8 conceptos de la clase 13A con definición breve de cada uno. Última fila con anticipación de la clase 13B"

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

## CLASE 13B — Módulos, Interfaces y Genéricos en TypeScript

---

### [F-21] Portada 13B

@tipo: portada
@imagen: none
@slide-artefact: tipo=NONE, descripcion="Portada de Clase 13B con título y lista de temas principales"

# CLASE 13B

## Módulos, Interfaces y Genéricos en TypeScript

- ADTs formales: encapsulamiento e information hiding
- Interfaz vs. Implementación — separación estricta
- Módulos TypeScript: `import` / `export` explícito
- Compilación separada e independiente
- Librerías de módulos: npm y `@types`
- Estructuras de datos genéricas: `Stack<T>`, `Queue<T>`, `Map<K,V>`
- Síntesis del Módulo X

---

### [F-22] Tipos de Datos Abstractos (ADT)

@tipo: concepto-abstracto
@imagen: none
@slide-artefact: tipo=NONE, descripcion="Definición formal de ADT con tres propiedades. Principios: encapsulamiento, information hiding, separación de concerns. Ejemplos de ADTs fundamentales"

# Tipos de Datos Abstractos (ADT)

## Definición formal (Sebesta §11.1)

Un ADT es un tipo de dato que satisface:

1. La **representación interna** está **oculta** a los clientes
2. Las **operaciones** son accesibles solo a través de la **interfaz pública**
3. Las operaciones garantizan las **invariantes** del tipo

## Principios clave

- **Encapsulamiento**: datos + operaciones en una unidad cohesiva
- **Information hiding**: el cliente ve QUÉ hace, no CÓMO lo hace
- **Separación de concerns**: cambiar la implementación no afecta al cliente

## Ejemplos de ADTs fundamentales

- `Stack` — operaciones: `push`, `pop`, `peek`, `isEmpty`
- `Queue` — operaciones: `enqueue`, `dequeue`, `front`
- `Set` — operaciones: `add`, `has`, `delete`, `union`, `intersection`

`[Sebesta, §11.1, pp. 471–478]`

---

### [F-23] Código TypeScript: Stack con `private`

@tipo: codigo
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="Clase Stack<T> con campo private datos: T[]. Métodos push, pop, peek, size. Comentario mostrando error de compilación al intentar acceder a datos desde fuera"

# ADT Stack en TypeScript — `private` como Barrera de Abstracción

```typescript
class Stack<T> {
  private datos: T[] = [];  // representación oculta al cliente

  push(item: T): void {
    this.datos.push(item);
  }

  pop(): T | undefined {
    return this.datos.pop();
  }

  peek(): T | undefined {
    return this.datos[this.datos.length - 1];
  }

  get size(): number {
    return this.datos.length;
  }
}

const pila = new Stack<number>();
pila.push(10);
pila.push(20);
console.log(pila.peek());   // 20

// pila.datos         // ← Error TS2341: 'datos' is private ✓
// pila.datos[0] = 99 // ← Error TS2341: no acceso directo ✓
```

---

### [F-24] Socrática: ¿Qué Debe Exponer la Interfaz?

@tipo: socratica
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="Clase Stack parcial en TypeScript con métodos básicos. Comentarios con operaciones candidatas para la interfaz pública: clear, toArray, at(index), contains. Preguntas sobre cuáles violan information hiding"

# ¿Qué Debería Exponer la Interfaz de una Stack?

```typescript
class Stack<T> {
  private datos: T[] = [];
  push(item: T): void    { this.datos.push(item); }
  pop(): T | undefined   { return this.datos.pop(); }
  peek(): T | undefined  { return this.datos.at(-1); }
  get size(): number     { return this.datos.length; }

  // ¿Cuáles de estos deberían estar en la interfaz pública?
  // clear(): void                        // ← limpiar todo
  // toArray(): T[]                       // ← exponer representación
  // at(index: number): T | undefined     // ← acceso aleatorio
  // contains(item: T): boolean           // ← búsqueda interna
}
```

## Preguntas para el aula

- ¿`toArray()` viola el information hiding? ¿Expone la representación?
- ¿`at(index)` convierte la Stack en un Array con acceso aleatorio?
- ¿Qué criterio usás para decidir qué operaciones son *esenciales* del ADT?

---

### [F-25] Separación Interfaz / Implementación

@tipo: concepto-abstracto
@imagen: none
@slide-artefact: tipo=SHAPE_DIAGRAM, descripcion="Diagrama con rectángulo INTERFAZ (contrato público) a la izquierda, flecha implements al rectángulo IMPLEMENTACIÓN (detalles privados) a la derecha. Abajo: el cliente solo ve la interfaz"

# Separación Interfaz / Implementación

## El principio (Sebesta §11.2 · Louden §11.3)

- La **interfaz** declara el *qué*: operaciones con sus tipos
- La **implementación** define el *cómo*: estructuras de datos y algoritmos

## Beneficios directos

- **Sustitución**: cambiar `ArrayStack` por `LinkedStack` sin tocar al cliente
- **Testabilidad**: mockear la interfaz en tests unitarios
- **Paralelismo de desarrollo**: cliente y proveedor trabajan en paralelo
- **Compilación separada**: la interfaz es suficiente para compilar el cliente

## En TypeScript

```typescript
export interface IStack<T> { ... }            // contrato observable
export class ArrayStack<T> implements IStack<T> { ... }   // impl. A
export class LinkedStack<T> implements IStack<T> { ... }  // impl. B
```

`[Sebesta, §11.2 · Louden, §11.3, pp. 503–509]`

---

### [F-26] Código TypeScript: `interface` + `class` Separadas

@tipo: codigo
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="Módulo stack.ts con export interface IStack<T> (5 operaciones tipadas) y export class ArrayStack<T> implements IStack<T> con campo private readonly elementos: T[]"

# Interfaz y Clase en TypeScript — Módulo `stack.ts`

```typescript
// INTERFAZ: contrato público observable por el cliente
export interface IStack<T> {
  push(item: T): void;
  pop(): T | undefined;
  peek(): T | undefined;
  readonly size: number;
  isEmpty(): boolean;
}

// IMPLEMENTACIÓN: detalles internos ocultos al cliente
export class ArrayStack<T> implements IStack<T> {
  private readonly elementos: T[] = [];

  push(item: T): void       { this.elementos.push(item); }
  pop(): T | undefined      { return this.elementos.pop(); }
  peek(): T | undefined     { return this.elementos.at(-1); }
  get size(): number        { return this.elementos.length; }
  isEmpty(): boolean        { return this.elementos.length === 0; }
}
```

> El cliente importa `IStack<T>` y **nunca necesita saber** que la implementación usa un array

---

### [F-27] DEFINITION MODULE vs. IMPLEMENTATION MODULE (Modula-2)

@tipo: concepto-abstracto
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="Código Modula-2 con DEFINITION MODULE Stack (tipo abstracto + procedimientos) y IMPLEMENTATION MODULE Stack (RECORD con array + top, implementaciones). Nota: cliente solo compila contra DEFINITION MODULE"

# Módulos Clásicos: Modula-2 (Louden §11.3)

## DEFINITION MODULE — el contrato público

```modula2
DEFINITION MODULE Stack;
  TYPE Stack;     (* tipo abstracto — representación oculta al cliente *)
  PROCEDURE Push(VAR s: Stack; x: INTEGER);
  PROCEDURE Pop(VAR s: Stack): INTEGER;
  PROCEDURE IsEmpty(VAR s: Stack): BOOLEAN;
END Stack.
```

## IMPLEMENTATION MODULE — los detalles ocultos

```modula2
IMPLEMENTATION MODULE Stack;
  CONST MaxSize = 100;
  TYPE Stack = RECORD
    data : ARRAY[0..MaxSize-1] OF INTEGER;
    top  : INTEGER
  END;
  PROCEDURE Push(VAR s: Stack; x: INTEGER);
  BEGIN s.data[s.top] := x; INC(s.top) END Push;
END Stack.
```

> El cliente **solo puede compilar contra** el DEFINITION MODULE — nunca ve el IMPLEMENTATION MODULE

`[Louden, §11.3, pp. 503–509]`

---

### [F-28] Diagrama: Módulo con Dependencias Explícitas

@tipo: diagrama
@imagen: none
@slide-artefact: tipo=SHAPE_DIAGRAM, descripcion="Diagrama de módulos: main.ts en el centro con flechas import hacia stack.ts (IStack, ArrayStack) y utils/logger.ts (Logger). stack.ts con sección interfaz y sección implementación separadas"

# Módulo: Dependencias Explícitas

```
┌────────────────────────────────────────────────────────┐
│  main.ts                                               │
│  import { ArrayStack } from './stack'                  │
│  import type { IStack } from './stack'                 │
│  import { Logger } from './utils/logger'               │
└───────────────┬─────────────────────┬──────────────────┘
                │                     │
                ▼                     ▼
┌───────────────────────┐   ┌──────────────────────────┐
│  stack.ts             │   │  utils/logger.ts          │
│  ──── Interfaz ────   │   │  export class Logger      │
│  export IStack<T>     │   │  import 'date-fns' (npm)  │
│  ── Implementación ── │   └──────────────────────────┘
│  export ArrayStack<T> │
└───────────────────────┘
```

> El compilador lee las dependencias y puede **recompilar solo los módulos desactualizados**

`[Louden, §11.1, pp. 496–500]`

---

### [F-29] Compilación Separada vs. Compilación Independiente

@tipo: tabla-comparativa
@imagen: none
@slide-artefact: tipo=TABLE, descripcion="Tabla comparativa: columnas Compilación Separada vs Compilación Independiente. Filas: definición, verificación de tipos cruzada, acceso a interfaz, detección de errores, ejemplos de lenguaje"

# Compilación Separada vs. Compilación Independiente

| Característica | Compilación Separada | Compilación Independiente |
|----------------|----------------------|---------------------------|
| **Qué es** | Cada módulo compila por separado pero con acceso a interfaces de otros | Cada unidad compila sin saber nada de otras unidades |
| **Verificación de tipos** | Sí: el compilador chequea contra la interfaz exportada | No: sin chequeo cruzado en compilación |
| **Acceso a interfaz** | Requiere `.d.ts` / DEFINITION MODULE / headers | No requiere nada externo |
| **Detección de errores** | En **tiempo de compilación** | Solo en enlace o ejecución |
| **Lenguajes** | TypeScript (`.d.ts`), Ada, Modula-2, C++ con headers | C clásico sin headers, FORTRAN original |
| **Ventaja** | Seguridad de tipos entre módulos | Máxima independencia física |

`[Louden, §11.1, pp. 498–502 · Sebesta, §11.5]`

---

### [F-30] Código TypeScript: `import` / `export` y `tsconfig`

@tipo: codigo
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="Tres archivos: stack.ts (exports), colecciones.ts (re-exports con export type), main.ts (import y import type). Fragmento de tsconfig.json con module ES2022 y moduleResolution Node16"

# Módulos TypeScript: `import` / `export`

```typescript
// stack.ts — módulo exportador
export interface IStack<T> { push(item: T): void; pop(): T | undefined; }
export class ArrayStack<T> implements IStack<T> { /* ... */ }

// colecciones.ts — re-exportación selectiva
export type { IStack } from './stack';      // solo el tipo (sin runtime cost)
export { ArrayStack } from './stack';       // la clase con su implementación

// main.ts — módulo cliente
import { ArrayStack } from './colecciones';
import type { IStack } from './colecciones';  // solo para el compilador

const s: IStack<string> = new ArrayStack<string>();
s.push("paradigmas");
console.log(s.pop());   // "paradigmas"
```

```json
// tsconfig.json — configuración de resolución de módulos
{ "compilerOptions": { "module": "ES2022", "moduleResolution": "Node16" } }
```

---

### [F-31] Librerías de Módulos: npm y `@types`

@tipo: concepto-abstracto
@imagen: none
@slide-artefact: tipo=HIERARCHY, descripcion="Jerarquía: npm registry (nivel 1) → paquete date-fns (nivel 2) → módulos internos (nivel 3). A la derecha: DefinitelyTyped (@types) con archivos .d.ts para paquetes JS sin tipos propios"

# Librerías de Módulos en TypeScript / Node.js

## El ecosistema npm

- **npm registry**: 2.5 millones de paquetes públicos disponibles
- Cada paquete = colección de módulos con `package.json` como manifiesto
- Instalación: `npm install date-fns` → `node_modules/date-fns/`

## `@types` — DefinitelyTyped

- Paquetes JavaScript sin tipos propios → definiciones en `@types/`
- Ejemplo: `npm install --save-dev @types/lodash`
- Archivos `.d.ts`: **declaration files** — solo tipos, sin implementación
- Equivalente moderno del **DEFINITION MODULE** de Modula-2

## Resolución de módulos en TypeScript

```typescript
import { format } from 'date-fns';            // módulo npm
import { calcularIMC } from './imc';          // módulo local relativo
import type { Config } from './types/app';    // solo tipo (sin runtime)
```

---

### [F-32] Código TypeScript: `Stack<T>` Genérico Completo

@tipo: codigo
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="Implementación completa de Stack<T> con métodos push, pop, peek, contains (predicado), size, isEmpty y toArray (readonly). Ejemplos de uso con Stack<number>"

# `Stack<T>` Genérico — Implementación Completa

```typescript
class Stack<T> {
  private datos: T[] = [];

  push(item: T): void           { this.datos.push(item); }
  pop(): T | undefined          { return this.datos.pop(); }
  peek(): T | undefined         { return this.datos.at(-1); }
  get size(): number            { return this.datos.length; }
  isEmpty(): boolean            { return this.datos.length === 0; }

  // Método genérico: el predicado también opera sobre T
  contains(pred: (item: T) => boolean): boolean {
    return this.datos.some(pred);
  }

  // Shallow copy — preserva encapsulamiento sin exponer referencia interna
  toArray(): readonly T[]       { return [...this.datos]; }
}

const pila = new Stack<number>();
pila.push(1); pila.push(2); pila.push(3);
console.log(pila.contains(n => n > 2));  // true
console.log(pila.toArray());             // [1, 2, 3]
```

---

### [F-33] Código TypeScript: `Queue<T>` y `Map<K,V>` con Constraints

@tipo: codigo
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="Clase Queue<T extends Printable> con enqueue/dequeue/size/print y clase TypedMap<K extends string|number, V> con set/get/has. Ejemplos de uso con tipos concretos"

# Estructuras Genéricas con Constraints

```typescript
// Constraint: T debe implementar toString()
interface Printable { toString(): string; }

class Queue<T extends Printable> {
  private cola: T[] = [];
  enqueue(item: T): void   { this.cola.push(item); }
  dequeue(): T | undefined { return this.cola.shift(); }
  get size(): number       { return this.cola.length; }
  print(): void            { console.log(this.cola.map(x => x.toString())); }
}

// Constraint: K solo puede ser string o number (serializable como clave)
class TypedMap<K extends string | number, V> {
  private store = new Map<K, V>();
  set(key: K, value: V): void    { this.store.set(key, value); }
  get(key: K): V | undefined     { return this.store.get(key); }
  has(key: K): boolean           { return this.store.has(key); }
}

const mapa = new TypedMap<string, number>();
mapa.set("paradigmas", 2026);
console.log(mapa.get("paradigmas")); // 2026
```

---

### [F-34] Código TypeScript: Conditional Types y Mapped Types

@tipo: codigo
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="Conditional type EsArray<T>, TipoRetorno<F> con infer R. Mapped types SoloLectura<T> y Parcial<T>. Ejemplos con tipos concretos mostrando inferencia en compilación"

# Tipos Avanzados: Conditional y Mapped Types

```typescript
// Conditional type — decisión en tiempo de compilación
type EsArray<T> = T extends any[] ? true : false;
type A = EsArray<number[]>;    // true
type B = EsArray<string>;      // false

// infer — extraer el tipo de retorno desde la firma de una función
type TipoRetorno<F extends (...args: any[]) => any>
  = F extends (...args: any[]) => infer R ? R : never;

function calcularArea(r: number): number { return Math.PI * r * r; }
type R = TipoRetorno<typeof calcularArea>;   // number

// Mapped types — transformar todas las propiedades de un tipo T
type SoloLectura<T> = { readonly [K in keyof T]: T[K] };
type Parcial<T>     = { [K in keyof T]?: T[K] };

type Config = { host: string; port: number };
type ConfigRO = SoloLectura<Config>;
// → { readonly host: string; readonly port: number }
```

---

### [F-35] Jerarquía de Abstracción del Módulo X

@tipo: diagrama
@imagen: none
@slide-artefact: tipo=HIERARCHY, descripcion="Pirámide de tres niveles: base Subprograma (abstrae comportamiento), medio ADT (encapsula tipo + operaciones), cima Módulo (unidad de compilación con dependencias). Flechas hacia arriba indicando progresión"

# Tres Niveles de Abstracción — Módulo X

```
       ┌──────────────────────────────────────────────┐
       │               MÓDULO                         │  ← Nivel 3
       │   Unidad de compilación independiente        │
       │   import/export · dependencias · librería    │
       └──────────────────────┬───────────────────────┘
                              │  agrupa y controla
       ┌──────────────────────┴───────────────────────┐
       │               ADT                            │  ← Nivel 2
       │   Tipo + operaciones encapsuladas            │
       │   information hiding · invariantes garantizados│
       └──────────────────────┬───────────────────────┘
                              │  abstrae el comportamiento
       ┌──────────────────────┴───────────────────────┐
       │           SUBPROGRAMA                        │  ← Nivel 1
       │   Unidad de abstracción de comportamiento    │
       │   parámetros · retorno · perfil · protocolo  │
       └──────────────────────────────────────────────┘
```

> Cada nivel construye sobre el anterior — la complejidad se doma por capas

`[Sebesta, Caps. 9, 11, 12 — síntesis del Módulo X]`

---

### [F-36] Tabla Síntesis — Módulo X

@tipo: tabla
@imagen: none
@slide-artefact: tipo=TABLE, descripcion="Tabla síntesis de 8 conceptos del Módulo X con columnas: Concepto, Definición breve, Herramienta TypeScript, Referencia Sebesta"

# Síntesis del Módulo X

| Concepto | Definición breve | Tool TypeScript | Sebesta |
|----------|-----------------|----------------|---------|
| **Subprograma** | Única entrada + retorno de control | `function` / método | §9.1 |
| **Variables locales** | Stack-dynamic por frame; static = persistente | `let` / `const` | §9.2 |
| **Pasaje de params** | Primitivos: valor · Objetos: sharing | tipos explícitos | §9.5 |
| **Closures** | Subprograma + entorno léxico capturado | arrow functions | §9.12 |
| **Sobrecarga** | Mismo nombre, distintas implementaciones | overload signatures | §9.8 |
| **Genéricos** | Una impl. para múltiples tipos `<T>` | `<T extends ...>` | §9.9 |
| **ADT / `private`** | Representación oculta, ops. por interfaz | `class` + `private` | §11.1 |
| **Módulos** | Unidad de compilación con deps. explícitas | `import`/`export` | §11.5 |

---

### [F-37] Socrática Final: Diseñar una API Pública

@tipo: socratica
@imagen: none
@slide-artefact: tipo=CODE_BOX, descripcion="Interfaz parcial IUserRepository con findById, save, delete. Clase PostgresUserRepository con private pool y private cache. Preguntas sobre qué debe y no debe estar en la interfaz"

# Socrática Final: ¿Cómo Diseñás la Interfaz de un Módulo?

```typescript
// Módulo de persistencia — ¿qué debería ser parte de la interfaz?
export interface IUserRepository {
  findById(id: string): Promise<User | null>;
  save(user: User): Promise<void>;
  delete(id: string): Promise<boolean>;
  // ¿Qué más agregarías? ¿Qué NO debería estar acá?
}

class PostgresUserRepository implements IUserRepository {
  private pool: Pool;                    // ← ¿debería ser accesible al cliente?
  private cache: Map<string, User>;      // ← ¿y este detalle de performance?
  // ...
}
```

## Preguntas para el aula

- ¿Qué operaciones son esenciales vs. detalles de implementación?
- ¿Cómo cambia la interfaz si migrás de PostgreSQL a MongoDB?
- ¿Qué viola exponer `pool` en la interfaz pública?

---

### [F-38] Cierre Módulo X — Preview Concurrencia

@tipo: cierre
@imagen: none
@slide-artefact: tipo=NONE, descripcion="Slide de cierre con síntesis del recorrido del Módulo X (dos clases) y preview de Módulo XI sobre concurrencia con preguntas motivadoras"

# Módulo X — Completado ✓

## Recorrido del Módulo X

- **Clase 13A**: Subprogramas · Variables Locales · Pasaje de Parámetros · Closures · Sobrecarga · Activation Records
- **Clase 13B**: ADTs · Interfaz/Implementación · Módulos · Compilación Separada · Genéricos

## En la Bibliografía

- Sebesta Caps. 9, 10, 11, 12 — completados con grounding real ChromaDB
- Louden §11: DEFINITION/IMPLEMENTATION MODULE — separación clásica de módulos
- Gabbrielli §5.3: Activation Records con Dynamic Chain Pointer

## Preview — Módulo XI: Concurrencia

- ¿Qué pasa cuando dos subprogramas se ejecutan **al mismo tiempo**?
- ¿Cómo se comparten datos entre procesos sin corrupción?
- **Herramientas**: `async/await` en TypeScript · threads en Kotlin · `asyncio` en Python
- **Conceptos**: race conditions · semáforos · monitores · canales

*→ Semana 14*
