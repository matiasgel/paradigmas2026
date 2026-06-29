# Filminas - Clase 13B - Modulos, interfaces y genericos

> Duracion: 120 minutos
> Hilo conductor: del dato abstracto a una frontera modular que puede evolucionar
> Fuente principal: Sebesta, capitulos 11 y 12
> Complementos: Louden/Lambert, capitulo 11; Gabbrielli/Martini, capitulo 9
> Lenguaje principal: TypeScript
> Frontera con 13A: no se reexplican pasaje de parametros, sobrecarga, closures ni activation records

---

### [F-00] Portada 13B

@tipo: portada
@prompt-imagen: Tres rectangulos horizontales conectados por lineas finas. Primero pequeno bordo, segundo mediano gris oscuro, tercero grande bordo claro. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin codigo, sin numeros. Alta resolucion.

# CLASE 13B

## Modulos, interfaces y genericos en TypeScript

- Hoy subimos de escala: de una operacion aislada a una frontera de cambio.
- La pregunta central es que debe ver el cliente y que debe quedar oculto.
- Sebesta guia la progresion: ADT -> encapsulamiento -> modulos -> compilacion separada.

---

### [F-01] Puente: 13A termina donde 13B empieza

@tipo: tabla

# 13B no repite subprogramas: los agrupa y les pone frontera

| En 13A vimos... | En 13B lo usamos para... |
|---|---|
| Perfil y protocolo de una operacion | Definir operaciones publicas de un ADT |
| Tipos de parametros y retornos | Especificar interfaces verificables |
| Generic functions | Construir tipos y modulos genericos |
| Costos de ejecucion | Decidir que detalles no deben filtrarse |

> La clase no vuelve a explicar el subprograma: lo toma como ladrillo basico.

---

### [F-02] Ruta de la clase

@tipo: tabla-comparativa

# La secuencia va de representacion oculta a interfaz compilable

| Bloque | Pregunta didactica | Resultado esperado |
|---|---|---|
| ADT | Que significa "usar" un tipo sin ver su representacion? | Distinguir contrato de estructura interna |
| Interfaz | Que operaciones puede asumir el cliente? | Disenar interfaces publicas pequenas |
| Modulo | Donde se declara una frontera de compilacion? | Leer import/export como dependencias |
| Genericos | Como reutilizar sin perder tipos? | Crear ADTs parametrizados con constraints minimos |

---

### [F-03] El problema: los clientes se pegan a detalles

@tipo: demo

# Si el cliente conoce la representacion, cambiar deja de ser libre

```typescript
// Cliente acoplado a un detalle interno: "la pila es un array".
pila.datos[0] = 99;
pila.datos.reverse();
```

- El cliente ya no usa una pila: usa un array disfrazado.
- Cualquier cambio interno rompe codigo externo.
- La abstraccion aparece cuando el cliente solo puede usar operaciones permitidas.

---

### [F-04] Sebesta: un ADT se define por operaciones, no por almacenamiento

@tipo: tabla-comparativa

# Un ADT oculta representacion y publica operaciones validas

| Parte del ADT | Que ve el cliente | Que queda oculto |
|---|---|---|
| Nombre del tipo | `Stack<T>` | Si usa array, lista o buffer |
| Operaciones | `push`, `pop`, `peek` | Algoritmos y estructuras auxiliares |
| Invariantes | "LIFO: sale lo ultimo que entro" | Como se mantiene ese orden |
| Errores definidos | `pop()` puede no devolver elemento | Caso interno de pila vacia |

---

### [F-05] Encapsular no alcanza si no se ocultan decisiones

@tipo: tabla-comparativa

# Encapsulamiento agrupa; information hiding protege cambios futuros

| Concepto | Pregunta que responde | Error comun |
|---|---|---|
| Encapsulamiento | Que datos y operaciones forman una unidad? | Poner todo en una clase enorme |
| Information hiding | Que decisiones internas pueden cambiar? | Exponer campos, arrays o conexiones |
| Interfaz publica | Que promesas recibe el cliente? | Publicar helpers por comodidad |
| Invariante | Que debe ser siempre cierto? | Permitir estados imposibles |

---

### [F-06] La pila enseña la idea porque tiene una regla simple

@tipo: tabla

# LIFO es una invariante observable, no un detalle de implementacion

| Operacion | Promesa al cliente | Detalle que no importa |
|---|---|---|
| `push(x)` | Agrega `x` como proximo candidato a salir | Donde se almacena fisicamente |
| `pop()` | Devuelve el ultimo elemento agregado disponible | Como se mueve el indice interno |
| `peek()` | Observa sin remover | Si hay cache o calculo directo |
| `isEmpty()` | Informa si `pop` tendria elemento | Si se guarda `size` o se calcula |

---

### [F-07] TypeScript puede expresar el ADT con una clase generica

@tipo: codigo

# `private` impide que el cliente dependa del array interno

```typescript
class Stack<T> {
  private readonly datos: T[] = [];

  push(item: T): void {
    this.datos.push(item);
  }

  pop(): T | undefined {
    return this.datos.pop();
  }

  peek(): T | undefined {
    return this.datos.at(-1);
  }
}
```

---

### [F-08] Pregunta de diseno: que debe exponer una Stack?

@tipo: demo

# La interfaz debe respetar la semantica del ADT

```typescript
class Stack<T> {
  push(item: T): void
  pop(): T | undefined
  peek(): T | undefined

  clear(): void
  toArray(): readonly T[]
  at(index: number): T | undefined
}
```

- `clear` puede ser una operacion legitima.
- `toArray` solo es seguro si devuelve copia o vista de solo lectura.
- `at(index)` rompe la idea de pila: convierte LIFO en acceso aleatorio.

---

### [F-09] Independencia de representacion: dos cuerpos, mismo contrato

@tipo: tabla-comparativa

# El cliente no debe saber si la pila usa array o nodos enlazados

| Implementacion | Representacion interna | Cliente que usa `Stack<T>` |
|---|---|---|
| `ArrayStack<T>` | `T[]` y operaciones sobre el final | No cambia |
| `LinkedStack<T>` | Nodo con `value` y `next` | No cambia |
| `BoundedStack<T>` | Array con capacidad maxima | Solo cambia si el contrato agrega overflow |
| `PersistentStack<T>` | Estructura inmutable compartida | No cambia si `push/pop` conservan semantica |

---

### [F-10] Regla de lectura: mirar primero el contrato

@tipo: demo

# Antes de leer el cuerpo, preguntamos que promete la interfaz

```typescript
const pila: IStack<string> = crearPila();

pila.push("a");
pila.push("b");
const x = pila.pop(); // "b" o undefined
```

- El tipo `IStack<string>` dice que operaciones existen.
- La variable no revela la clase concreta.
- El cuerpo de `crearPila` puede cambiar sin cambiar este cliente.

---

### [F-11] Interfaz e implementacion tienen responsabilidades distintas

@tipo: tabla-comparativa

# La interfaz dice "que"; la implementacion decide "como"

| Nivel | Contiene | Cambia cuando... |
|---|---|---|
| Interfaz | Nombres, tipos, errores y significado observable | Cambia la promesa publica |
| Implementacion | Estructuras, algoritmos, caches y adaptadores | Cambia una decision interna |
| Cliente | Llamadas permitidas por la interfaz | Necesita otra capacidad publica |
| Tests de contrato | Casos que toda implementacion debe pasar | Cambia la semantica prometida |

---

### [F-12] TypeScript separa contrato y cuerpo con `interface` y `class`

@tipo: codigo

# El cliente puede depender de `IStack<T>`, no de `ArrayStack<T>`

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

### [F-13] TypeScript tiene dos niveles de privacidad

@tipo: tabla-comparativa

# `private` protege en compilacion; `#campo` protege tambien en runtime

| Recurso | Cuando actua | Que impide |
|---|---|---|
| `private datos` | TypeScript, antes de emitir JS | Acceso tipado desde clientes |
| `#datos` | JavaScript en runtime | Acceso real desde fuera de la clase |
| `readonly` | TypeScript | Reasignar una referencia |
| Copia defensiva | Runtime | Que el cliente modifique la coleccion interna |

> Para explicar ADTs alcanza `private`; para proteger runtime conviene `#`.

---

### [F-14] Un modulo selecciona que nombres salen al exterior

@tipo: codigo

# `export` convierte una decision interna en parte de la frontera publica

```typescript
// stack.ts
export type { IStack };
export { ArrayStack };

class NodeStack<T> implements IStack<T> {
  // No exportada: implementacion alternativa interna.
}

function validarCapacidad(max: number): void {
  // No exportada: helper privado del modulo.
}
```

---

### [F-15] Leer imports es leer dependencias entre modulos

@tipo: tabla

# Una dependencia explicita dice que otro contrato es necesario

| Import | Significado arquitectonico | Pregunta docente |
|---|---|---|
| `import type { IStack }` | Solo necesito el contrato en compilacion | Puedo evitar costo runtime? |
| `import { ArrayStack }` | Necesito la implementacion concreta | Es correcto acoplarme a ella? |
| `import { comparar } from "./orden.js"` | Uso otra unidad del programa | Esa dependencia pertenece aqui? |
| `import "./polyfill"` | Dependo de un efecto global | El efecto esta documentado? |

---

### [F-16] El modulo cliente deberia importar lo minimo necesario

@tipo: codigo

# `import type` permite depender de una interfaz sin traer codigo

```typescript
// cliente.ts
import type { IStack } from "./stack.js";

export function copiar<T>(origen: IStack<T>, destino: IStack<T>): void {
  while (origen.size > 0) {
    const item = origen.pop();
    if (item !== undefined) destino.push(item);
  }
}
```

- El modulo cliente conoce `IStack<T>`, no `ArrayStack<T>`.
- La interfaz visible alcanza para verificar llamadas.
- La implementacion concreta se decide en otra unidad.

---

### [F-17] Compilacion separada no significa compilar a ciegas

@tipo: tabla-comparativa

# Para compilar separado, el compilador necesita contratos

| Modelo | Que conoce cada unidad | Riesgo |
|---|---|---|
| Compilacion independiente | Solo su propio codigo | Errores aparecen al enlazar o ejecutar |
| Compilacion separada | Interfaces de las unidades usadas | Requiere mantener contratos disponibles |
| TypeScript moderno | `.ts` y `.d.ts` de dependencias | Tipos borrados en runtime |
| Modula-2/Ada | Definicion/spec separada del cuerpo | Cambio de spec recompila clientes |

---

### [F-18] Modula-2 muestra la separacion de forma clasica

@tipo: tabla-mixta

# El cliente compila contra la definicion, no contra el cuerpo

| Archivo | Rol |
|---|---|
| `DEFINITION MODULE Stack` | Publica tipo abstracto y operaciones |
| `IMPLEMENTATION MODULE Stack` | Define representacion y algoritmos |
| Cliente | Importa la definicion y no ve el record interno |

```modula2
DEFINITION MODULE Stack;
  TYPE Stack;
  PROCEDURE Push(VAR s: Stack; x: INTEGER);
  PROCEDURE Pop(VAR s: Stack): INTEGER;
END Stack.
```

---

### [F-19] Los archivos `.d.ts` publican una interfaz de compilacion

@tipo: tabla

# Un cliente puede compilar contra declaraciones, no contra cuerpos

| Pieza | Funcion |
|---|---|
| `stack.ts` | Contiene interfaz e implementacion fuente |
| `stack.d.ts` | Expone declaraciones de tipos |
| Cliente | Verifica llamadas contra esas declaraciones |
| Cuerpo compilado | Puede cambiar si conserva la interfaz declarada |

---

### [F-20] Los genericos vuelven reusable al ADT

@tipo: tabla-comparativa

# En 13B el generico parametriza tipos completos, no solo funciones

| Sin genericos | Con genericos |
|---|---|
| `NumberStack`, `StringStack`, `UserStack` | `Stack<T>` |
| Codigo duplicado por tipo | Una implementacion parametrizada |
| Mas riesgo de divergencia | Un solo contrato reusable |
| Cambios repetidos | Cambios en un punto |

---

### [F-21] `Stack<T>` conserva el tipo de cada elemento

@tipo: codigo

# El parametro `T` viaja por operaciones, retornos e invariantes

```typescript
const numeros = new ArrayStack<number>();
numeros.push(10);
const n = numeros.pop(); // number | undefined

const usuarios = new ArrayStack<Usuario>();
usuarios.push({ id: "u1", nombre: "Ada" });
const u = usuarios.peek(); // Usuario | undefined
```

- La estructura es la misma.
- El contrato cambia con el tipo de elemento.
- El compilador impide mezclar `Usuario` con `number`.

---

### [F-22] Un constraint solo aparece cuando el codigo lo necesita

@tipo: codigo

# Restringir `T` de mas reduce reutilizacion sin ganar seguridad

```typescript
interface Comparable<T> {
  compareTo(other: T): number;
}

class SortedSet<T extends Comparable<T>> {
  private readonly items: T[] = [];

  add(item: T): void {
    // El constraint existe porque ordenamos con compareTo.
  }
}
```

> Si la estructura solo apila y desapila, no necesita `Comparable<T>`.

---

### [F-23] Los constraints son contratos sobre capacidades

@tipo: tabla-comparativa

# Cada constraint debe corresponder a una operacion real

| Estructura | Operacion que exige capacidad | Constraint razonable |
|---|---|---|
| `Stack<T>` | Guardar y devolver elementos | Ninguno |
| `SortedSet<T>` | Ordenar sin comparador externo | `T extends Comparable<T>` |
| `IdentifiedSet<E>` | Buscar por identidad | `E extends { id: Id }` |
| `Serializer<T>` | Codificar y decodificar | Codec externo o interfaz explicita |

---

### [F-24] Devolver datos internos puede romper el ADT

@tipo: codigo

# Una copia de solo lectura preserva mejor el ocultamiento

```typescript
class Stack<T> {
  private readonly datos: T[] = [];

  toArray(): readonly T[] {
    return [...this.datos]; // copia superficial
  }
}
```

- El cliente no puede hacer `push` sobre el array retornado.
- La representacion interna no escapa.
- Si `T` es mutable, la copia no vuelve inmutable a cada objeto.

---

### [F-25] Caso integrador: `Set<T>` como modulo con interfaz

@tipo: tabla-mixta

# El cliente depende de operaciones, no de buckets internos

| Elemento | Debe ser publico? | Motivo |
|---|---|---|
| `add` | Si | Operacion central del conjunto |
| `has` | Si | Consulta observable |
| `buckets` | No | Representacion interna |
| `rehash` | No | Algoritmo auxiliar |

```typescript
export interface ISet<T> {
  add(item: T): void;
  has(item: T): boolean;
  delete(item: T): boolean;
}
```

---

### [F-26] Actividad breve: decidir una interfaz publica

@tipo: demo

# Si todo es publico, nada queda protegido

```typescript
export interface ISet<T> {
  add(item: T): void;
  has(item: T): boolean;
  delete(item: T): boolean;

  // Candidatos:
  // size(): number
  // values(): readonly T[]
  // rawBuckets(): T[][]
  // rehash(): void
}
```

> Pregunta: cuales son operaciones del tipo y cuales son detalles de representacion?

---

### [F-27] Cambiar una interfaz cambia el costo para clientes

@tipo: tabla-comparativa

# La compatibilidad depende de que promesa publica se modifica

| Cambio | Rompe clientes? | Lectura didactica |
|---|---|---|
| Optimizar algoritmo privado | No | Implementacion interna |
| Cambiar array por lista enlazada | No, si conserva contrato | Independencia de representacion |
| Agregar parametro obligatorio | Si | Cambia la interfaz |
| Cambiar significado sin cambiar tipo | Puede romper | Ruptura semantica |
| Quitar exportacion | Si | Cambio de interfaz publica |

---

### [F-28] Sintesis: cada nivel oculta una decision distinta

@tipo: tabla

# De subprograma a modulo, crece la frontera de abstraccion

| Nivel | Lo que abstrae | Lo que oculta |
|---|---|---|
| Subprograma | Una accion | Instrucciones y variables locales |
| ADT | Un conjunto de valores y operaciones | Representacion e invariantes internas |
| Interfaz | Capacidades esperadas | Implementaciones concretas |
| Modulo | Un conjunto cohesivo de nombres | Helpers, dependencias y estructura interna |
| Unidad de compilacion | Archivo o conjunto compilable | Cuerpo, helpers y dependencias internas |

---

### [F-29] Cierre 13B

@tipo: cierre
@prompt-imagen: Cinco cajas simples en columna ascendente, de gris claro a bordo oscuro, conectadas por una linea fina vertical. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin codigo, sin numeros. Alta resolucion.

# Modularidad es conservar libertad de cambio

- Un ADT protege una representacion mediante operaciones con sentido.
- Una interfaz publica transforma decisiones en promesas.
- Un modulo hace visibles solo los nombres necesarios.
- Un generico reutiliza la estructura sin mezclar tipos.

## Criterio final

Una decision es verdaderamente interna si puede cambiar sin romper clientes.
