# Filminas - Clase 13B - Modulos, Interfaces y Genericos

> Duracion: 120 minutos
> Ritmo objetivo: 3-4 minutos por filmina fuente
> Fuente completa derivada del Tema 13

---

### [F-00] Portada 13B

@tipo: portada

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

### [F-01] Tipos de Datos Abstractos (ADT)

@tipo: concepto-abstracto

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

### [F-02] Código TypeScript: Stack con `private` - codigo 1/3

@tipo: codigo

# Código TypeScript: Stack con `private` - codigo 1/3

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
```

---

### [F-03] Código TypeScript: Stack con `private` - codigo 2/3

@tipo: codigo

# Código TypeScript: Stack con `private` - codigo 2/3

```typescript
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
```

---

### [F-04] Diseño rápido: interfaz de Stack

@tipo: socratica

# Diseño rápido: interfaz de Stack

## Actividad de 4 minutos

- Elegí cinco operaciones públicas esenciales.
- Identificá dos detalles que deben permanecer privados.
- Escribí una invariante que la interfaz debe proteger.

> Puesta en común: una respuesta por grupo y justificación breve.

---

### [F-05] Código TypeScript: Stack con `private` - codigo 3/3

@tipo: codigo

# Código TypeScript: Stack con `private` - codigo 3/3

```typescript

// pila.datos         // ← Error TS2341: 'datos' is private ✓
// pila.datos[0] = 99 // ← Error TS2341: no acceso directo ✓
```

---

### [F-06] Socrática: ¿Qué Debe Exponer la Interfaz?

@tipo: socratica

# ¿Qué Debería Exponer la Interfaz de una Stack?

## Preguntas para el aula

- ¿`toArray()` viola el information hiding? ¿Expone la representación?
- ¿`at(index)` convierte la Stack en un Array con acceso aleatorio?
- ¿Qué criterio usás para decidir qué operaciones son *esenciales* del ADT?

---

### [F-07] Socrática: ¿Qué Debe Exponer la Interfaz? - codigo 1/2

@tipo: codigo

# Socrática: ¿Qué Debe Exponer la Interfaz? - codigo 1/2

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
```

---

### [F-08] Socrática: ¿Qué Debe Exponer la Interfaz? - codigo 2/2

@tipo: codigo

# Socrática: ¿Qué Debe Exponer la Interfaz? - codigo 2/2

```typescript
}
```

---

### [F-09] Separación Interfaz / Implementación

@tipo: concepto-abstracto

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

`[Sebesta, §11.2 · Louden, §11.3, pp. 503–509]`

```typescript
export interface IStack<T> { ... }            // contrato observable
export class ArrayStack<T> implements IStack<T> { ... }   // impl. A
export class LinkedStack<T> implements IStack<T> { ... }  // impl. B
```

---

### [F-10] Código TypeScript: `interface` + `class` Separadas - codigo 1/2

@tipo: codigo

# Código TypeScript: `interface` + `class` Separadas - codigo 1/2

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
```

---

### [F-11] Cambio de implementacion sin cambiar clientes

@tipo: socratica

# Cambio de implementacion sin cambiar clientes

## Actividad de 4 minutos

- Reemplazá `ArrayStack` por `LinkedStack` conceptualmente.
- ¿Qué archivos deberían recompilarse?
- ¿Qué parte del contrato debe permanecer estable?

> Puesta en común: una respuesta por grupo y justificación breve.

---

### [F-12] Código TypeScript: `interface` + `class` Separadas - codigo 2/2

@tipo: codigo

# Código TypeScript: `interface` + `class` Separadas - codigo 2/2

```typescript

  push(item: T): void       { this.elementos.push(item); }
  pop(): T | undefined      { return this.elementos.pop(); }
  peek(): T | undefined     { return this.elementos.at(-1); }
  get size(): number        { return this.elementos.length; }
  isEmpty(): boolean        { return this.elementos.length === 0; }
}
```

---

### [F-13] DEFINITION MODULE vs. IMPLEMENTATION MODULE (Modula-2)

@tipo: concepto-abstracto

# Módulos Clásicos: Modula-2 (Louden §11.3)

## DEFINITION MODULE — el contrato público

## IMPLEMENTATION MODULE — los detalles ocultos

> El cliente **solo puede compilar contra** el DEFINITION MODULE — nunca ve el IMPLEMENTATION MODULE

`[Louden, §11.3, pp. 503–509]`

---

### [F-14] DEFINITION MODULE vs. IMPLEMENTATION MODULE (Modula-2) - codigo 1/2

@tipo: codigo

# DEFINITION MODULE vs. IMPLEMENTATION MODULE (Modula-2) - codigo 1/2

```modula2
DEFINITION MODULE Stack;
  TYPE Stack;     (* tipo abstracto — representación oculta al cliente *)
  PROCEDURE Push(VAR s: Stack; x: INTEGER);
  PROCEDURE Pop(VAR s: Stack): INTEGER;
  PROCEDURE IsEmpty(VAR s: Stack): BOOLEAN;
END Stack.

IMPLEMENTATION MODULE Stack;
  CONST MaxSize = 100;
  TYPE Stack = RECORD
    data : ARRAY[0..MaxSize-1] OF INTEGER;
    top  : INTEGER
```

---

### [F-15] DEFINITION MODULE vs. IMPLEMENTATION MODULE (Modula-2) - codigo 2/2

@tipo: codigo

# DEFINITION MODULE vs. IMPLEMENTATION MODULE (Modula-2) - codigo 2/2

```modula2
  END;
  PROCEDURE Push(VAR s: Stack; x: INTEGER);
  BEGIN s.data[s.top] := x; INC(s.top) END Push;
END Stack.
```

---

### [F-16] Diagrama: Módulo con Dependencias Explícitas

@tipo: diagrama

# Módulo: Dependencias Explícitas

> El compilador lee las dependencias y puede **recompilar solo los módulos desactualizados**

`[Louden, §11.1, pp. 496–500]`

---

### [F-17] Diagrama: Módulo con Dependencias Explícitas - codigo 1/2

@tipo: codigo

# Diagrama: Módulo con Dependencias Explícitas - codigo 1/2

```text
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
```

---

### [F-18] Mapa de dependencias del modulo

@tipo: socratica

# Mapa de dependencias del modulo

## Actividad de 4 minutos

- Dibujá módulos como nodos y dependencias como flechas.
- Detectá un ciclo y proponé cómo romperlo.

> Puesta en común: una respuesta por grupo y justificación breve.

---

### [F-19] Diagrama: Módulo con Dependencias Explícitas - codigo 2/2

@tipo: codigo

# Diagrama: Módulo con Dependencias Explícitas - codigo 2/2

```text
│  ── Implementación ── │   └──────────────────────────┘
│  export ArrayStack<T> │
└───────────────────────┘
```

---

### [F-20] Compilación Separada vs. Compilación Independiente

@tipo: tabla-comparativa

# Compilación Separada vs. Compilación Independiente

`[Louden, §11.1, pp. 498–502 · Sebesta, §11.5]`

| Característica | Compilación Separada | Compilación Independiente |
|----------------|----------------------|---------------------------|
| **Qué es** | Cada módulo compila por separado pero con acceso a interfaces de otros | Cada unidad compila sin saber nada de otras unidades |
| **Verificación de tipos** | Sí: el compilador chequea contra la interfaz exportada | No: sin chequeo cruzado en compilación |
| **Acceso a interfaz** | Requiere `.d.ts` / DEFINITION MODULE / headers | No requiere nada externo |
| **Detección de errores** | En **tiempo de compilación** | Solo en enlace o ejecución |
| **Lenguajes** | TypeScript (`.d.ts`), Ada, Modula-2, C++ con headers | C clásico sin headers, FORTRAN original |
| **Ventaja** | Seguridad de tipos entre módulos | Máxima independencia física |

---

### [F-21] Código TypeScript: `import` / `export` y `tsconfig` - codigo 1/2

@tipo: codigo

# Código TypeScript: `import` / `export` y `tsconfig` - codigo 1/2

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

```

---

### [F-22] Código TypeScript: `import` / `export` y `tsconfig` - codigo 2/2

@tipo: codigo

# Código TypeScript: `import` / `export` y `tsconfig` - codigo 2/2

```typescript
const s: IStack<string> = new ArrayStack<string>();
s.push("paradigmas");
console.log(s.pop());   // "paradigmas"

// tsconfig.json — configuración de resolución de módulos
{ "compilerOptions": { "module": "ES2022", "moduleResolution": "Node16" } }
```

---

### [F-23] Librerías de Módulos: npm y `@types`

@tipo: concepto-abstracto

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

### [F-24] Código TypeScript: `Stack<T>` Genérico Completo - codigo 1/2

@tipo: codigo

# Código TypeScript: `Stack<T>` Genérico Completo - codigo 1/2

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
```

---

### [F-25] Código TypeScript: `Stack<T>` Genérico Completo - codigo 2/2

@tipo: codigo

# Código TypeScript: `Stack<T>` Genérico Completo - codigo 2/2

```typescript
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

### [F-26] Laboratorio mental: publicar un paquete npm

@tipo: socratica

# Laboratorio mental: publicar un paquete npm

## Actividad de 4 minutos

- ¿Qué exportarías desde `index.ts`?
- ¿Qué aporta un archivo `.d.ts`?
- ¿Qué dependencia sería de desarrollo?

> Puesta en común: una respuesta por grupo y justificación breve.

---

### [F-27] Código TypeScript: `Queue<T>` y `Map<K,V>` con Constraints - codigo 1/2

@tipo: codigo

# Código TypeScript: `Queue<T>` y `Map<K,V>` con Constraints - codigo 1/2

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
```

---

### [F-28] Código TypeScript: `Queue<T>` y `Map<K,V>` con Constraints - codigo 2/2

@tipo: codigo

# Código TypeScript: `Queue<T>` y `Map<K,V>` con Constraints - codigo 2/2

```typescript
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

### [F-29] Código TypeScript: Conditional Types y Mapped Types - codigo 1/2

@tipo: codigo

# Código TypeScript: Conditional Types y Mapped Types - codigo 1/2

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

```

---

### [F-30] Código TypeScript: Conditional Types y Mapped Types - codigo 2/2

@tipo: codigo

# Código TypeScript: Conditional Types y Mapped Types - codigo 2/2

```typescript
// Mapped types — transformar todas las propiedades de un tipo T
type SoloLectura<T> = { readonly [K in keyof T]: T[K] };
type Parcial<T>     = { [K in keyof T]?: T[K] };

type Config = { host: string; port: number };
type ConfigRO = SoloLectura<Config>;
// → { readonly host: string; readonly port: number }
```

---

### [F-31] Jerarquía de Abstracción del Módulo X

@tipo: diagrama

# Tres Niveles de Abstracción — Módulo X

> Cada nivel construye sobre el anterior — la complejidad se doma por capas

`[Sebesta, Caps. 9, 11, 12 — síntesis del Módulo X]`

---

### [F-32] Jerarquía de Abstracción del Módulo X - codigo 1/2

@tipo: codigo

# Jerarquía de Abstracción del Módulo X - codigo 1/2

```text
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
```

---

### [F-33] Jerarquía de Abstracción del Módulo X - codigo 2/2

@tipo: codigo

# Jerarquía de Abstracción del Módulo X - codigo 2/2

```text
       ┌──────────────────────┴───────────────────────┐
       │           SUBPROGRAMA                        │  ← Nivel 1
       │   Unidad de abstracción de comportamiento    │
       │   parámetros · retorno · perfil · protocolo  │
       └──────────────────────────────────────────────┘
```

---

### [F-34] Comparacion de estructuras genericas

@tipo: socratica

# Comparacion de estructuras genericas

## Actividad de 4 minutos

- Compará `Stack<T>`, `Queue<T>` y `Map<K,V>`.
- ¿Qué constraints son realmente necesarios?
- ¿Qué operación rompe encapsulamiento?

> Puesta en común: una respuesta por grupo y justificación breve.

---

### [F-35] Tabla Síntesis — Módulo X

@tipo: tabla

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

### [F-36] Socrática Final: Diseñar una API Pública

@tipo: socratica

# Socrática Final: ¿Cómo Diseñás la Interfaz de un Módulo?

## Preguntas para el aula

- ¿Qué operaciones son esenciales vs. detalles de implementación?
- ¿Cómo cambia la interfaz si migrás de PostgreSQL a MongoDB?
- ¿Qué viola exponer `pool` en la interfaz pública?

---

### [F-37] Socrática Final: Diseñar una API Pública - codigo 1/2

@tipo: codigo

# Socrática Final: Diseñar una API Pública - codigo 1/2

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
```

---

### [F-38] Socrática Final: Diseñar una API Pública - codigo 2/2

@tipo: codigo

# Socrática Final: Diseñar una API Pública - codigo 2/2

```typescript
}
```

---

### [F-39] Cierre Módulo X — Preview Concurrencia

@tipo: cierre

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

- *→ Semana 14*
