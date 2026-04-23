// Ejercicio 18 — Separar efectos puros de I/O
// Trazabilidad: F-32

export type Orden = {
  id: number;
  cliente: string;
  total: number;
  categoria: string;
  activa: boolean;
};

export type Regla = {
  nombre: string;
  condicion: (o: Orden) => boolean;
  porcentaje: number;
};

export type OrdenConDescuento = Orden & {
  descuento: number;
  totalFinal: number;
};

export type Resumen = {
  totalOriginal: number;
  totalFinal: number;
  ahorro: number;
  cantidad: number;
};

/**
 * PURA: calcula el precio con descuento.
 */
export function calcularDescuento(
  precio: number,
  porcentaje: number
): number {
  // TODO: Implementar
  throw new Error("TODO: Implementar calcularDescuento");
}

/**
 * PURA: aplica la primera regla cuya condición se cumple.
 * Si ninguna aplica, descuento = 0 y totalFinal = total.
 */
export function aplicarReglas(
  orden: Orden,
  reglas: Regla[]
): OrdenConDescuento {
  // TODO: Implementar
  throw new Error("TODO: Implementar aplicarReglas");
}

/**
 * PURA: genera un resumen agregado de las órdenes con descuento.
 */
export function generarResumen(
  ordenes: OrdenConDescuento[]
): Resumen {
  // TODO: Implementar
  throw new Error("TODO: Implementar generarResumen");
}
