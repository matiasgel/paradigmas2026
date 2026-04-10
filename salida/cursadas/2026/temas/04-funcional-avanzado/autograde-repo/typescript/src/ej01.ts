// Ejercicio 1 — Pipeline filter/map/reduce
// Trazabilidad: F-06, F-07, F-08

export type Orden = {
  id: number;
  cliente: string;
  total: number;
  categoria: string;
  activa: boolean;
};

/**
 * Filtra las órdenes activas, extrae sus totales y los suma.
 * Restricción: usar solo filter, map, reduce. Sin variables mutables.
 */
export function filtrarActivasYSumar(ordenes: Orden[]): number {
  // TODO: Implementar
  throw new Error("TODO: Implementar filtrarActivasYSumar");
}

/**
 * Filtra las órdenes activas y devuelve un array con sus totales.
 */
export function obtenerTotalesActivas(ordenes: Orden[]): number[] {
  // TODO: Implementar
  throw new Error("TODO: Implementar obtenerTotalesActivas");
}
