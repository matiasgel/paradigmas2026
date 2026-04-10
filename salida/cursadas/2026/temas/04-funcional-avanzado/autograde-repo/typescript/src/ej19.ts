// Ejercicio 19 — Integrador TypeScript
// Trazabilidad: F-35, F-36

export type Orden = {
  id: number;
  cliente: string;
  total: number;
  categoria: string;
  activa: boolean;
};

export type Result<T, E = string> =
  | { ok: true; value: T }
  | { ok: false; error: E };

export const ok = <T>(value: T): Result<T, never> => ({ ok: true, value });
export const err = <E>(error: E): Result<never, E> => ({ ok: false, error });

/**
 * Clasifica una orden:
 * - Si no es activa → err("inactiva")
 * - Si categoría no es "elect" → err("categoría incorrecta")
 * - Si total ≤ 200 → err("monto insuficiente")
 * - Si pasa todo → ok(total)
 * Evaluar en ese orden de prioridad.
 */
export function clasificarOrden(o: Orden): Result<number, string> {
  // TODO: Implementar
  throw new Error("TODO: Implementar clasificarOrden");
}

/**
 * Clasifica cada orden, filtra los ok y suma los valores.
 */
export function totalElectActivos(ordenes: Orden[]): number {
  // TODO: Implementar
  throw new Error("TODO: Implementar totalElectActivos");
}

/**
 * Clasifica cada orden y retorna estadísticas:
 * - aprobadas: cantidad de ok
 * - rechazadas: cantidad de errores
 * - total: suma de los valores ok
 */
export function resumenClasificacion(ordenes: Orden[]): {
  aprobadas: number;
  rechazadas: number;
  total: number;
} {
  // TODO: Implementar
  throw new Error("TODO: Implementar resumenClasificacion");
}
