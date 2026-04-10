import { describe, it, expect } from "vitest";
import { clasificarOrden, totalElectActivos, resumenClasificacion, type Orden } from "../src/ej19.js";

const ordenes: Orden[] = [
  { id: 1, cliente: "Ana", total: 250, categoria: "elect", activa: true },
  { id: 2, cliente: "Boris", total: 80, categoria: "ropa", activa: false },
  { id: 3, cliente: "Carla", total: 420, categoria: "elect", activa: true },
  { id: 4, cliente: "Diana", total: 30, categoria: "ropa", activa: true },
  { id: 5, cliente: "Edwin", total: 175, categoria: "elect", activa: true },
];

describe("Ej19 — Integrador TypeScript", () => {
  describe("clasificarOrden", () => {
    it("aprueba orden activa elect con total > 200", () => {
      expect(clasificarOrden(ordenes[0])).toEqual({ ok: true, value: 250 });
    });

    it("rechaza inactiva", () => {
      expect(clasificarOrden(ordenes[1])).toEqual({ ok: false, error: "inactiva" });
    });

    it("rechaza categoría incorrecta", () => {
      expect(clasificarOrden(ordenes[3])).toEqual({ ok: false, error: "categoría incorrecta" });
    });

    it("rechaza monto insuficiente", () => {
      expect(clasificarOrden(ordenes[4])).toEqual({ ok: false, error: "monto insuficiente" });
    });
  });

  describe("totalElectActivos", () => {
    it("suma solo los aprobados", () => {
      expect(totalElectActivos(ordenes)).toBe(670);
    });

    it("retorna 0 si ninguno pasa", () => {
      const soloRopa = ordenes.filter((o) => o.categoria === "ropa");
      expect(totalElectActivos(soloRopa)).toBe(0);
    });

    it("array vacío", () => {
      expect(totalElectActivos([])).toBe(0);
    });
  });

  describe("resumenClasificacion", () => {
    it("cuenta aprobadas, rechazadas y total", () => {
      expect(resumenClasificacion(ordenes)).toEqual({
        aprobadas: 2,
        rechazadas: 3,
        total: 670,
      });
    });

    it("array vacío", () => {
      expect(resumenClasificacion([])).toEqual({ aprobadas: 0, rechazadas: 0, total: 0 });
    });
  });
});
