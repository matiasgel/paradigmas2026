// Ejercicio 2 — Binding de tipos en TypeScript: tipado estático y coerciones (20 pts)
// Trazabilidad: OA2, OA5 — F-05, F-08, F-09, F-10
//
// TypeScript tiene binding de tipos ESTÁTICO (los tipos se establecen en compilación)
// y tipado FUERTE (no hay coerciones implícitas entre tipos incompatibles).
// Estas funciones explotan esas propiedades para escribir código seguro y correcto.

// 2a. Suma dos números dados como strings (5 pts).
// Convertir explícitamente a número antes de operar.
// Lanzar Error("invalid number") si alguno de los strings no representa un número válido
// (es decir, Number(s) resulta en NaN).
// parseAndAdd("3", "4") → 7
// parseAndAdd("1.5", "2.5") → 4
// parseAndAdd("abc", "4") → throws Error("invalid number")
export function parseAndAdd(a: string, b: string): number {
  throw new Error("TODO: implementar");
}

// 2b. Retorna solo los elementos de tipo number de la lista (5 pts).
// Usar typeof para type narrowing — TypeScript conoce el tipo dentro de cada rama.
// onlyNumbers([1, "hola", 2, true, 3.5]) → [1, 2, 3.5]
export function onlyNumbers(items: Array<string | number | boolean>): number[] {
  throw new Error("TODO: implementar");
}

// 2c. Agrupa los elementos por tipo (5 pts).
// Separar en tres listas según sean string, number o boolean. Conservar el orden.
// groupByType(["a", 1, true, "b", 2]) → { strings: ["a","b"], numbers: [1,2], booleans: [true] }
export interface TypeGroups {
  strings: string[];
  numbers: number[];
  booleans: boolean[];
}
export function groupByType(items: Array<string | number | boolean>): TypeGroups {
  throw new Error("TODO: implementar");
}

// 2d. Aplica una función dos veces al valor (5 pts).
// applyTwice(fn, value) = fn(fn(value))
// TypeScript garantiza en compilación que fn acepta y retorna el mismo tipo T que value.
// applyTwice((x: number) => x * 2, 3) → 12   (fn(fn(3)) = fn(6) = 12)
// applyTwice((x: string) => x + "!", "hola") → "hola!!"
export function applyTwice<T>(fn: (x: T) => T, value: T): T {
  throw new Error("TODO: implementar");
}
