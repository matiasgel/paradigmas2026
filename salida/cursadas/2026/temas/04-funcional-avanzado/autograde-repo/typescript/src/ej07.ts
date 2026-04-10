// Ejercicio 7 — Algebraic Data Types (tipo suma)
// Trazabilidad: F-14

export type Circle = { kind: "circle"; radius: number };
export type Rectangle = { kind: "rectangle"; width: number; height: number };
export type Triangle = { kind: "triangle"; base: number; height: number };
export type Shape = Circle | Rectangle | Triangle;

/**
 * Calcula el área de la forma geométrica.
 */
export function area(s: Shape): number {
  // TODO: Implementar con switch sobre s.kind
  throw new Error("TODO: Implementar area");
}

/**
 * Calcula el perímetro de la forma geométrica.
 * Triángulo: asumí isósceles con lados = sqrt((base/2)² + height²)
 */
export function perimetro(s: Shape): number {
  // TODO: Implementar
  throw new Error("TODO: Implementar perimetro");
}

/**
 * Retorna una descripción: "<kind>: area=X.XX"
 * Usar toFixed(2) para el área.
 */
export function describir(s: Shape): string {
  // TODO: Implementar
  throw new Error("TODO: Implementar describir");
}
