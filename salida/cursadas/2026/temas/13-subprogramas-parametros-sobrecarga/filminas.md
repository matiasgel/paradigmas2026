# Filminas - Clase 13A - Subprogramas, Parámetros y Sobrecarga

> Duración: 120 minutos
> Hilo conductor: del problema del acoplamiento a la representación, al módulo como frontera de visibilidad
> Fuente principal: `clase_dada.txt` (baseline de la clase dada)
> Lenguaje principal: TypeScript
> Trazabilidad bibliográfica: ver `minuta.md`

---

### [F-00] Portada 13A

@tipo: portada
@imagen: background
@prompt-imagen: Tres bloques geométricos apilados: un cubo bordó sobre dos losas gris oscuro, separados por una línea de fractura blanca que cruza horizontalmente la composición. A la derecha, tres cilindros delgados bordó de distinta altura alineados en fila. Flat design, bordó y gris oscuro, fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# CLASE 13A

## Módulos, interfaces y genéricos en TypeScript

- Del acoplamiento a la representación al TAD como contrato.
- Encapsulamiento, ocultamiento de información e interfaz pública.
- El módulo como frontera de visibilidad y compilación separada.
- Genéricos: reutilizar la abstracción sin mezclar tipos.

---

### [F-01] Ruta de la clase

@tipo: tabla

# Cuatro conceptos formales, cuatro preguntas

| Concepto formal | Pregunta que responde |
|---|---|
| TAD / ADT | ¿Qué significa usar un tipo sin ver su representación? |
| Interfaz | ¿Qué operaciones puede asumir el cliente? |
| Módulo | ¿Dónde se declara una frontera de visibilidad? |
| Genéricos | ¿Cómo reutilizar sin mezclar tipos? |

- Abstracción de datos, especificación pública, encapsulamiento modular y polimorfismo paramétrico.
- Cada concepto responde a una pregunta de diseño distinta.
- La clase recorre el problema que motiva cada uno y la construcción en TypeScript.

---

### [F-02] El problema: acoplamiento a la representación

@tipo: concepto-mixto

# Si el cliente conoce la representación interna, cambiar deja de ser libre

- El cliente deja de usar una pila y pasa a usar un array disfrazado.
- Cualquier cambio interno rompe código externo.
- La abstracción aparece cuando el cliente solo puede usar operaciones permitidas.

```typescript
// Cliente acoplado a un detalle interno:
// "la pila es un array"
// El cliente ya no usa una pila
// Usa un array disfrazado:
pila.datos[0] = 99
pila.datos.reverse()
```

---

### [F-03] TAD: Tipo Abstracto de Datos

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: Un rectángulo bordó con tres cajas grises anidadas en su interior, cada una con un pequeño círculo blanco en el centro. A la derecha del rectángulo, una columna vertical de tres íconos abstractos: un cuadrado, un triángulo y un círculo, todos bordó. Una línea de puntos gris separa el rectángulo de los íconos. Flat design, bordó y gris oscuro, fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Un TAD no se define por cómo guarda los datos

- Nombre + Operaciones + Semántica observable + Invariantes.
- El cliente ve el nombre del tipo, las operaciones y la semántica.
- Queda oculto cómo se almacena, los algoritmos auxiliares y el caso interno de pila vacía.

## Parte del TAD

| Qué ve el cliente | Qué queda oculto |
|---|---|
| Nombre del tipo: `Stack<T>` | Si usa array, lista o buffer |
| Operaciones: `push`, `pop`, `peek` | Algoritmos auxiliares |
| Semántica: LIFO | Cómo se mantiene el orden |
| Errores definidos: `pop()` puede no devolver elemento | Caso interno de pila vacía |

---

### [F-04] La pila como ejemplo mínimo

@tipo: tabla-comparativa

# LIFO es una invariante observable; el array no

- La pila es buena explicación de un ADT porque tiene una regla simple.
- Last In, First Out: invariante observable que el array no garantiza.

| Operación | Promesa observable | Detalle irrelevante |
|---|---|---|
| `push(x)` | Agrega x como próximo candidato a salir | Dónde se almacena |
| `pop()` | Devuelve y remueve el último agregado disponible | Cómo se mueve el índice interno |
| `peek()` | Observa sin remover | Si usa cache o cálculo directo |
| `isEmpty()` | Informa si hay elementos disponibles | Si guarda size o lo calcula |

---

### [F-05] Operaciones de un TAD

@tipo: tabla-comparativa

# Una interfaz no debería ser una lista arbitraria de métodos

- Una operación pública pertenece al TAD si respeta su semántica.
- `push`/`pop`/`peek` → sí son operaciones de pila.
- `at(index)` → rompe la abstracción de pila.

| Tipo de operación | Qué hace | Ejemplo en `Stack<T>` |
|---|---|---|
| Constructora | Crea valores del TAD | `new Stack<T>()`, `emptyStack()` |
| Transformadora | Cambia el estado abstracto | `push`, `pop`, `clear` |
| Observadora | Consulta sin romper la abstracción | `peek`, `isEmpty`, `size` |

---

### [F-06] Encapsulamiento ≠ ocultamiento de información

@tipo: tabla-comparativa

# Encapsular agrupa; ocultar información protege cambios futuros

| Concepto | Pregunta que responde | Error común |
|---|---|---|
| Encapsulamiento | ¿Qué datos y operaciones forman una unidad? | Poner todo en una clase enorme |
| Ocultamiento de información | ¿Qué decisiones internas pueden cambiar? | Exponer campos, arrays o conexiones |
| Interfaz pública | ¿Qué promesas recibe el cliente? | Publicar helpers por comodidad |
| Invariante | ¿Qué debe ser siempre cierto? | Permitir estados imposibles |

- No son sinónimos: responden a preguntas de diseño distintas.
- Confundirlos lleva a clases enormes o a exponer representación interna.

---

### [F-07] Implementación de Stack en TypeScript

@tipo: codigo

# TypeScript permite expresar el TAD con una clase genérica

- El cliente usa operaciones; no toca la estructura interna.
- `#items` es propiedad privada real en TypeScript.

```typescript
class Stack<T> {
  #items: T[] = []
  //# propiedad privada

  push(item: T): void {
    this.#items.push(item)
  }

  pop(): T | undefined {
    return this.#items.pop()
  }

  peek(): T | undefined {
    return this.#items.at(-1)
  }

  isEmpty(): boolean {
    return this.#items.length === 0
  }
}
```

---

### [F-08] ¿Qué debe exponer una interfaz?

@tipo: tabla-comparativa

# La interfaz debe respetar la semántica del TAD

- Si una operación revela la representación, deja de ser abstracción.

| Operación | ¿Conviene? | Motivo |
|---|---|---|
| `clear()` | Sí | Puede ser operación válida de pila |
| `toArray()` | Depende | Debe devolver copia o vista de solo lectura |
| `at(index)` | No | Convierte la pila en acceso aleatorio |

```typescript
export interface Stack<T> {
  push(item: T): void
  pop(): T | undefined
  peek(): T | undefined
  isEmpty(): boolean
  clear(): void
  toArray(): readonly T[]
}
```

---

### [F-09] Copia defensiva

@tipo: codigo

# La copia defensiva protege la representación privada

- Devolver el array interno expone la representación: mal diseño.
- Devolver una copia superficial preserva el encapsulamiento.

## Mal diseño

```typescript
class Stack<T> {
  #items: T[] = []

  toArray(): T[] {
    return this.#items // expone representación interna
  }
}
```

## Mejor diseño

```typescript
class Stack<T> {
  #items: T[] = []

  toArray(): readonly T[] {
    return [...this.#items] // copia superficial
  }
}
```

---

### [F-10] Independencia de representación

@tipo: tabla-comparativa

# Dos implementaciones pueden tener el mismo contrato

| Implementación | Representación interna | Cliente que usa `Stack<T>` |
|---|---|---|
| `ArrayStack<T>` | Array `T[]` | No cambia |
| `LinkedStack<T>` | Nodos enlazados | No cambia |
| `BoundedStack<T>` | Array con capacidad máxima | Cambia solo si cambia el contrato |
| `PersistentStack<T>` | Estructura inmutable compartida | No cambia si conserva LIFO |

- El cliente no debe saber si la pila usa array, nodos o buffer.
- Cambiar la representación interna no rompe a quien depende del contrato.

---

### [F-11] Separación entre especificación e implementación

@tipo: codigo

# La interfaz dice qué promete; la implementación decide cómo se cumple

```typescript
export interface Stack<T> {
  push(item: T): void
  pop(): T | undefined
  peek(): T | undefined
  readonly size: number
}

export class ArrayStack<T> implements Stack<T> {
  #items: T[] = []

  push(item: T): void {
    this.#items.push(item)
  }

  pop(): T | undefined {
    return this.#items.pop()
  }

  peek(): T | undefined {
    return this.#items.at(-1)
  }

  get size(): number {
    return this.#items.length
  }
}
```

---

### [F-12] Módulo como frontera de visibilidad

@tipo: concepto-mixto

# Un módulo decide qué nombres salen al exterior

- `exportado` → parte de la frontera pública.
- `no exportado` → detalle interno del módulo.
- TypeScript separa contrato y cuerpo con `interface` y `class`.

```typescript
// stack.ts
export type { Stack }
export { ArrayStack }

class NodeStack<T> implements Stack<T> {
  // Implementación alternativa interna.
}

function validarCapacidad(max: number): void {
  // Helper privado del módulo.
}
```

```typescript
export interface IStack<T> {
  push(item: T): void;
  pop(): T | undefined;
  peek(): T | undefined;
  readonly size: number;
}

export class ArrayStack<T> implements IStack<T> {
  private readonly datos: T[] = [];
  push(item: T): void { this.datos.push(item); }
  pop(): T | undefined { return this.datos.pop(); }
  peek(): T | undefined { return this.datos.at(-1); }
  get size(): number { return this.datos.length; }
}
```

---

### [F-13] Imports, dependencias y compilación separada

@tipo: tabla-mixta

# Compilación separada no significa compilar a ciegas: el compilador necesita contratos

| Import | Tipo de dependencia | Pregunta |
|---|---|---|
| `import type { Stack }` | Dependencia estática de tipos | ¿Alcanza con el contrato? |
| `import { ArrayStack }` | Dependencia de implementación | ¿Es correcto acoplarme a ella? |
| `import { compare } from "./order.js"` | Dependencia funcional | ¿Pertenece a este módulo? |
| `import "./polyfill"` | Dependencia por efecto lateral | ¿Está documentada? |

```typescript
import type { Stack } from "./stack.js"
export function mover<T>(origen: Stack<T>, destino: Stack<T>): void {
  while (origen.size > 0) {
    const item = origen.pop()
    if (item !== undefined) destino.push(item)
  }
}
```

---

### [F-14] Genéricos

@tipo: concepto-mixto

# Un genérico reutiliza la abstracción sin mezclar tipos

- Sin genéricos: `NumberStack`, `StringStack`, `UserStack`.
- Con genéricos: `Stack<T>` parametriza el tipo una sola vez.

```typescript
const numeros = new ArrayStack<number>()
numeros.push(10)
numeros.push("hola") // error: string no es number
const n = numeros.pop() // number | undefined
```

## Interfaces como restricciones

```typescript
interface Comparable<T> {
  compareTo(other: T): number
}

class SortedSet<T extends Comparable<T>> {
  #items: T[] = []
  add(item: T): void {
    this.#items.push(item)
    this.#items.sort((a, b) => a.compareTo(b))
  }
}
```

---

### [F-15] Repaso y cierre

@tipo: cierre
@imagen: background
@prompt-imagen: Cuatro losas gris oscuro dispuestas en escalera descendente de izquierda a derecha, cada una con un pequeño cubo bordó sobre su superficie. Una línea de puntos bordó conecta los cuatro cubos formando una trayectoria descendente. Flat design, bordó y gris oscuro, fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Cuatro ideas para llevarse

- Un **TAD** protege una representación.
- Una **interfaz** transforma decisiones en promesas.
- Un **módulo** controla qué nombres son públicos.
- Un **genérico** reutiliza la abstracción sin mezclar tipos.

## Próxima clase

- Del módulo aislado a la composición de abstracciones.