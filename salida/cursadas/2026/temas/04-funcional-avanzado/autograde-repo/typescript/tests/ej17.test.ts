// Tests — Ejercicio 17: Integrador TypeScript
import { describe, it, expect } from "vitest";
import { clasificarOrden, aplicarDescuento, procesarOrdenes, Orden } from "../src/ej17";

const ordenes: Orden[] = [
  { id: 1, cliente: "Ana", total: 250, categoria: "elect", activa: true },
  { id: 2, cliente: "Boris", total: 80, categoria: "ropa", activa: false },
  { id: 3, cliente: "Carla", total: 420, categoria: "elect", activa: true },
  { id: 4, cliente: "Diana", total: 50, categoria: "ropa", activa: true },
];

describe("clasificarOrden", () => {
  it("ok si activa y total > 100", () => {
    const r = clasificarOrden(ordenes[0]);
    expect(r.status).toBe("ok");
  });
  it("error si inactiva", () => {
    expect(clasificarOrden(ordenes[1])).toEqual({ status: "error", error: "orden inactiva" });
  });
  it("error si monto insuficiente", () => {
    expect(clasificarOrden(ordenes[3])).toEqual({ status: "error", error: "monto insuficiente" });
  });
});

describe("aplicarDescuento", () => {
  it("10% de descuento", () => {
    const desc = aplicarDescuento(10)(ordenes[0]);
    expect(desc.total).toBe(225);
    expect(desc.id).toBe(1);
  });
  it("0% no cambia", () => {
    expect(aplicarDescuento(0)(ordenes[0]).total).toBe(250);
  });
  it("no muta original", () => {
    aplicarDescuento(10)(ordenes[0]);
    expect(ordenes[0].total).toBe(250);
  });
});

describe("procesarOrdenes", () => {
  it("pipeline completo", () => {
    const result = procesarOrdenes(ordenes);
    expect(result.aprobadas).toHaveLength(2);
    expect(result.rechazadas).toHaveLength(2);
    expect(result.aprobadas[0].total).toBe(225);
    expect(result.aprobadas[1].total).toBe(378);
    expect(result.totalFinal).toBe(603);
  });
  it("vacío si no hay órdenes", () => {
    const result = procesarOrdenes([]);
    expect(result.aprobadas).toEqual([]);
    expect(result.rechazadas).toEqual([]);
    expect(result.totalFinal).toBe(0);
  });
});
