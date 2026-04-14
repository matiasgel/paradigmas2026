// Ejercicio 2 — Composición con pipe y compose (6 pts)
// Trazabilidad: F-06, F-07

// Compone funciones de izquierda a derecha. Sin funciones → identidad.
export function pipe<T>(...fns: Array<(x: T) => T>): (x: T) => T {
  throw new Error("TODO: implementar");
}

// Compone funciones de derecha a izquierda. Sin funciones → identidad.
export function compose<T>(...fns: Array<(x: T) => T>): (x: T) => T {
  throw new Error("TODO: implementar");
}

// Pipeline que aplica trim, toLowerCase, y agrega @empresa.com si no tiene @.
export function normalizeEmail(raw: string): string {
  throw new Error("TODO: implementar con pipe");
}
