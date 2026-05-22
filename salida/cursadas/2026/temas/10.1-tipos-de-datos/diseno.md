# Diseño de Clase — Tema 10.1
## Sistemas de Tipos — Parte 1: Fundamentos y Tipos Primitivos

> **Estado:** BORRADOR — pendiente aprobación docente
> **Generado:** 2026-05-22
> **Agente:** Lic. Marcos 🗂️ (Topic Designer)
> **Fuentes consultadas:** Sebesta (2019) Cap. 6, Gabbrielli & Martini (2023) Cap. 8, Louden & Lambert (2012) Cap. 8 — vía ChromaDB MCP

---

## Metadata del Tema

| Campo | Valor |
|-------|-------|
| Número de tema | 10.1 |
| Nombre | Sistemas de Tipos — Parte 1: Fundamentos y Tipos Primitivos |
| Módulo | VII — Sistemas de Tipos |
| Semana | 10 |
| Clase | 1 |
| **Duración (constraint)** | **120 minutos** |
| Perfil docente | profesor-teorico |
| Lenguaje principal | TypeScript |
| Lenguajes de contraste | Haskell (tipos estáticos), C (tipos primitivos), Python (tipado dinámico) |
| Sibling topic | 10.2 — Tipos Compuestos y Polimorfismo (próxima clase) |

---

## Objetivos de Aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Definir** qué es un tipo de dato desde tres perspectivas: diseño, corrección y compilación (Gabbrielli & Martini, §8.1).
2. **Clasificar** los tipos primitivos/escalares de un lenguaje (numéricos, boolean, char, enumeración, intervalo) y sus representaciones internas.
3. **Distinguir** type checking estático vs. dinámico y fuertemente tipado vs. débilmente tipado.
4. **Contrastar** equivalencia por nombre (nominal) vs. equivalencia estructural con ejemplos en TypeScript y C.
5. **Identificar** cómo TypeScript implementa cada concepto y qué lo diferencia de C, Python y Haskell.

---

## Mapa Conceptual del Tema

```
¿Qué es un tipo?
   ├── Razones para los tipos (diseño / corrección / implementación)
   ├── Tipos primitivos / escalares
   │    ├── Numéricos: integer, float, decimal
   │    ├── Boolean
   │    ├── Character / String
   │    ├── Enumeración
   │    └── Intervalo / Ordenados (ordinales)
   ├── Type Checking
   │    ├── Estático (compile-time)
   │    └── Dinámico (run-time)
   ├── Strong typing vs. weak typing
   └── Equivalencia de tipos
        ├── Por nombre (nominal)
        └── Estructural
```

---

## Estructura de Clase (120 min)

### Bloque 1 — ¿Qué es un tipo de dato y para qué existe? (20 min)

**Concepto central (Sebesta §6.1 + Gabbrielli §8.1):**

> *"A data type defines a collection of data values and a set of predefined operations on those values."* — Sebesta (2019, p. 235)

**Tres razones por las que los tipos existen en los lenguajes (Gabbrielli & Martini, §8.1):**

1. **A nivel de diseño** — apoyo a la organización conceptual del problema
2. **A nivel de programa** — apoyo a la corrección (detectar errores en desarrollo)
3. **A nivel de traducción** — apoyo a la implementación eficiente

**Línea histórica:** Fortran (solo arrays + numéricos) → ALGOL 68 (tipos primitivos + composición libre) → lenguajes modernos con sistemas de tipos ricos.

**Actividad (5 min):** ¿En qué se diferencia el tipo de una variable en Python vs. TypeScript? ¿Cuándo se detecta un error de tipo en cada uno?

---

### Bloque 2 — Tipos Primitivos: el catálogo (30 min)

**Marco general (Louden & Lambert §8.1):**

> *"At the most basic level, virtually every data value expressible in a programming language has an implicit type."* (p. 328)

#### 2.1 Tipos Numéricos

| Tipo | Representación interna | TS | C | Python |
|------|----------------------|-----|---|--------|
| Integer | complemento a 2 (16/32/64 bits) | `number` (IEEE 754 double) / `bigint` | `int`, `long`, `short` | `int` (unbounded) |
| Float | IEEE 754 (single/double) | `number` | `float`, `double` | `float` |
| Decimal | BCD (COBOL, PL/I) | — | — | `decimal.Decimal` |

**TypeScript: un solo `number`** — ¿bug de diseño o elección consciente? (hereda de JS/IEEE 754)

```typescript
// TypeScript — float por defecto
const x: number = 0.1 + 0.2;  // 0.30000000000000004
console.log(x === 0.3);       // false — error clásico IEEE 754

// BigInt en TypeScript (ES2020)
const big: bigint = 9007199254740993n;  // más allá de Number.MAX_SAFE_INTEGER
```

#### 2.2 Boolean

*"Boolean types are perhaps the simplest of all types. Their range of values has only two elements."* — Sebesta (p. 265)

- Introducido en ALGOL 60; ausente en C89 (usa 0 / no-cero)
- En TypeScript: `true | false` — tipo primitivo propio
- Truco de C vs. TypeScript: `if (1)` compila en C, en TS da error de tipos

```typescript
// TS — estrictamente boolean
const flag: boolean = true;
// const flag2: boolean = 1;  // Error: Type 'number' is not assignable to type 'boolean'
```

#### 2.3 Character y String

- Char: 1 carácter (ASCII 7 bits, Latin-1 8 bits, Unicode UTF-16/UTF-32)
- TypeScript: no hay tipo `char` — solo `string` (secuencia de code units UTF-16)

```typescript
// TypeScript — string como primitivo (no objeto)
const c: string = "A";
const s: string = "paradigmas";
console.log(s.length);      // 10 (code units)
console.log("🦄".length);   // 2 — ¡un emoji = 2 code units!
```

#### 2.4 Enumeración

- Conjunto finito ordenado de valores con nombres simbólicos
- Gabbrielli & Martini: tipos **discretos** u **ordenados** — tienen predecesor y sucesor
- Pascal, Ada, C++, TypeScript todos la soportan

```typescript
// TypeScript enum — dos sabores
enum Color { Red, Green, Blue }         // numérico (Red=0, Green=1, Blue=2)
const enum Direction { Up, Down }       // const enum = inlineado (mejor performance)

// String enum — más type-safe
enum Status { Open = "OPEN", Closed = "CLOSED" }
```

**Contraste con C:** `enum` en C es simplemente `int` — no hay seguridad de rango.

#### 2.5 Tipos Ordenados (Discretos)

> *"The boolean, character, integer, enumeration and interval types are examples of ordered types (or discrete types). They are equipped with a well-defined concept of total order and possess a concept of predecessor and successor."* — Gabbrielli & Martini (§8.3.10)

- Útiles como índices de array y variables de control en iteraciones acotadas
- Ada los llama "discrete types" y los usa para índices tipados de arrays

---

### Bloque 3 — Type Checking: ¿Cuándo y cómo se validan los tipos? (30 min)

**Marco conceptual (Louden & Lambert §8.6):**

> *"Type checking is the process by which a translator verifies that all constructs in a program make sense in terms of the types of its constants, variables, procedures, and other entities."*

#### 3.1 Checking Estático vs. Dinámico

| Dimensión | Estático | Dinámico |
|-----------|----------|----------|
| Cuándo ocurre | Tiempo de compilación / análisis | Tiempo de ejecución |
| Ejemplos | TypeScript (tsc), Java, Haskell, C | Python, JavaScript, Ruby, Lisp/Scheme |
| Ventaja | Errores antes de ejecutar, optimizaciones | Más flexibilidad, prototipado rápido |
| Desventaja | Requiere declaraciones o inferencia | Errores visibles solo al ejecutar |

```typescript
// TypeScript: error estático
function suma(a: number, b: number): number {
    return a + b;
}
// suma("hola", 2);  // Error en compile-time: Argument of type 'string' not assignable to 'number'
```

```python
# Python: error dinámico (solo al ejecutar la línea)
def suma(a, b):
    return a + b

print(suma("hola", 2))  # TypeError solo al ejecutar
```

#### 3.2 Strong Typing vs. Weak Typing (Sebesta §6.14)

> *"A language is strongly typed if type errors are always detected."* — Sebesta (p. 292)

| Lenguaje | Tipado | Justificación |
|----------|--------|---------------|
| Haskell | Fuertemente estático | Sin coerciones implícitas; inferencia Hindley-Milner |
| TypeScript | Fuertemente estático (con escape hatches: `any`, `as`) | Superset de JS que añade tipos |
| Java | Fuertemente estático | Salvo algunas coerciones numéricas implícitas |
| C | Débilmente estático | Coerciones silenciosas (int ↔ char ↔ pointer con cast) |
| Python | Fuertemente dinámico | Tipos chequeados en run-time, pero sin coerciones implícitas |
| JavaScript | Débilmente dinámico | Coerciones implícitas masivas (`"5" + 3 === "53"`) |

```typescript
// TypeScript escape hatch — `any` destruye el type checking
let x: any = "texto";
x = 42;        // OK, pero perdemos seguridad
x.noExiste();  // Sin error estático — peligroso

// `unknown` — alternativa más segura a `any`
let y: unknown = "texto";
// y.toUpperCase(); // Error: Object is of type 'unknown'
if (typeof y === "string") {
    y.toUpperCase();  // OK — narrowing
}
```

#### 3.3 Eje IA Generativa (15 min integrados en bloque 3)

**Prompt para el aula:**
> "Tengo este código TypeScript. ¿Por qué TypeScript acepta `any` si destruye el type checking? ¿Cómo podría refactorizarlo para preservar la seguridad?"

**Reflexión docente:** Los LLMs tienden a generar `any` como solución fácil a errores de tipo. Un desarrollador que entiende el sistema de tipos puede rechazar esas sugerencias y pedir código más seguro.

---

### Bloque 4 — Equivalencia de Tipos: ¿Cuándo son "el mismo tipo"? (25 min)

**Marco (Louden & Lambert §8.5 + Gabbrielli & Martini §8.x):**

#### 4.1 Equivalencia por Nombre (Nominal)

Dos tipos son equivalentes **si y solo si tienen el mismo nombre** (o son declarados juntos).

```typescript
// TypeScript — equivalencia nominal con classes
class Celsius { constructor(public value: number) {} }
class Fahrenheit { constructor(public value: number) {} }

function calentar(t: Celsius): Celsius {
    return new Celsius(t.value + 10);
}

const temp = new Fahrenheit(32);
// calentar(temp);  // Error — Fahrenheit no es Celsius, aunque tienen la misma estructura
```

#### 4.2 Equivalencia Estructural

Dos tipos son equivalentes **si tienen la misma estructura** (mismos campos/tipos), sin importar el nombre.

```typescript
// TypeScript — usa equivalencia ESTRUCTURAL para interfaces/types
interface Punto2D { x: number; y: number; }
interface Coordenada { x: number; y: number; }  // mismo shape

function mover(p: Punto2D): void { console.log(p.x, p.y); }

const c: Coordenada = { x: 3, y: 4 };
mover(c);  // ✅ OK — structural typing (duck typing estático)
```

**TypeScript usa structural typing** — filosofía "si camina como un pato y grazna como un pato, es un pato".  
**Java/C# usan nominal typing** — para ser `Comparable`, hay que declarar explícitamente `implements Comparable`.

#### 4.3 Comparación en lenguajes

| Lenguaje | Modelo de equivalencia |
|----------|----------------------|
| TypeScript | Estructural (interfaces) + Nominal (classes con private) |
| Haskell | Nominal (newtype) + Estructural (type aliases) |
| C | Estructural para `struct` (nombres ignorados por compilador en asignación compatible) |
| Java | Nominal (clases e interfaces) |
| C++ | Nominal para clases; estructural para templates |

```haskell
-- Haskell: nominal con newtype evita errores de tipo
newtype Metros = Metros Double
newtype Pies = Pies Double

convertir :: Metros -> Pies
convertir (Metros m) = Pies (m * 3.28084)

-- convertir (Pies 100.0)  -- Error de tipo en compile-time
```

---

### Bloque 5 — Síntesis y cierre (15 min)

**Mapa mental de cierre** — el docente reconstruye el mapa con participación del aula:

```
Sistema de Tipos
  ├── ¿Qué es un tipo? → valores + operaciones
  ├── ¿Para qué sirve? → diseño, corrección, implementación
  ├── Tipos primitivos: numérico, bool, char, enum, ordinal
  ├── Type checking: estático ↔ dinámico
  ├── Strong vs. weak typing
  └── Equivalencia: nominal ↔ estructural
```

**Pregunta de cierre:** ¿Por qué TypeScript tiene `any` si su objetivo es el type checking estático? ¿Qué patrón de diseño del lenguaje revela esto?

---

## Tópicos del Plan Mínimo cubiertos

| Tópico Plan Mínimo | Sección de clase |
|-------------------|-----------------|
| Sistemas de tipos | Bloques 1, 3, 4 |
| Tipos primitivos y su representación | Bloque 2 |
| Type checking estático / dinámico | Bloque 3.1 |
| Strong typing | Bloque 3.2 |
| Equivalencia de tipos (nominal / estructural) | Bloque 4 |

---

## Conexiones con otros temas

| Dirección | Tema | Conexión |
|-----------|------|----------|
| ← Prerequisito | T09.1 Variables, Binding y Ámbito | Los tipos se ligan a variables en el binding |
| ← Prerequisito | T01 Intro + TypeScript | TypeScript ya fue presentado como lenguaje con tipos |
| → Siguiente (10.2) | Tipos Compuestos y Polimorfismo | Arrays, records, unions, option types, type constructors |
| → Futuro | T14 Sistemas de Tipos y Polimorfismo | Polimorfismo paramétrico, generics, Hindley-Milner |

---

## Material Bibliográfico

### Fuente principal
- **Sebesta, R.W.** (2019). *Concepts of Programming Languages* (12ª ed.). Pearson.
  - Capítulo 6: *Data Types* (pp. 235–295): §6.1–6.4, §6.13, §6.14, §6.15

### Fuentes de enriquecimiento (ChromaDB)
- **Gabbrielli, M. & Martini, S.** (2023). *Programming Languages: Principles and Paradigms* (2ª ed.). Springer.
  - Capítulo 8: *Structuring Data* (pp. 199–266): Definición de tipo, razones, escalares, tipos discretos, type checking, equivalencia
- **Louden, K.C. & Lambert, K.A.** (2012). *Programming Languages: Principles and Practices* (3ª ed.). Course Technology.
  - Capítulo 8: *Data Types* (pp. 325–385): §8.1 Data Types and Type Info, §8.5 Type Equivalence, §8.6 Type Checking

---

## Notas de Diseño / Alcance

> **Fuera de scope para esta clase (10.1):**
> - Tipos compuestos (arrays, records, unions, pointers) → T10.2
> - Coerción y conversión de tipos → T10.2
> - Tipos algebraicos / tipos suma → T10.2
> - Polimorfismo paramétrico y generics → T14
> - Inferencia de tipos (Hindley-Milner) → T14

> **Advertencia de scope creep:** El tipo `string` en TypeScript tiene ~50 métodos. En esta clase se presenta como *tipo primitivo* — sus operaciones y el tipo `String` (objeto) son T10.2.

---

## Aprobación

| Estado | Fecha | Responsable |
|--------|-------|-------------|
| 🔲 BORRADOR | 2026-05-22 | Marcos (Topic Designer) |
| ⬜ APROBADO | — | Matías Gel (Docente) |
