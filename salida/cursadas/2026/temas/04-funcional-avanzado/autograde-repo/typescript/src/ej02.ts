// Ejercicio 2 — Composición con pipe y compose
// Trazabilidad: F-09

/**
 * Compone funciones de izquierda a derecha.
 * pipe(f, g, h)(x) === h(g(f(x)))
 * pipe()(x) === x  (identidad)
 */
export function pipe(
  ...fns: Array<(arg: any) => any>
): (arg: any) => any {
  // TODO: Implementar con reduce
  throw new Error("TODO: Implementar pipe");
}

/**
 * Compone funciones de derecha a izquierda (orden matemático).
 * compose(f, g, h)(x) === f(g(h(x)))
 */
export function compose(
  ...fns: Array<(arg: any) => any>
): (arg: any) => any {
  // TODO: Implementar con reduceRight
  throw new Error("TODO: Implementar compose");
}
