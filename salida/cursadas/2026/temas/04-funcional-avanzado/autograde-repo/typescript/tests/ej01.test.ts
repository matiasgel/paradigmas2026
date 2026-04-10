import { describe, it, expect } from "vitest";
import { filtrarActivasYSumar, obtenerTotalesActivas, type Orden } from "../src/ej01.js";

const ordenes: Orden[] = [
  { id: 1, cliente: "Ana", total: 120, categoria: "elect", activa: true },
  { id: 2, cliente: "Boris", total: 50, categoria: "ropa", activa: false },
  { id: 3, cliente: "Carla", total: 200, categoria: "elect", activa: true },
  { id: 4, cliente: "Diana", total: 75, categoria: "ropa", activa: true },
];

describe("Ej01 — Pipeline filter/map/reduce", () => {
  describe("filtrarActivasYSumar", () => {
    it("suma los totales de las órdenes activas", () => {
      expect(filtrarActivasYSumar(ordenes)).toBe(395);
    });

    it("retorna 0 para array vacío", () => {
      expect(filtrarActivasYSumar([])).toBe(0);
    });

    it("retorna 0 si ninguna es activa", () => {
      const inactivas = ordenes.map((o) => ({ ...o, activa: false }));
      expect(filtrarActivasYSumar(inactivas)).toBe(0);
    });
  });

  describe("obtenerTotalesActivas", () => {
    it("retorna array de totales de las activas", () => {
      expect(obtenerTotalesActivas(ordenes)).toEqual([120, 200, 75]);
    });

    it("retorna array vacío para array vacío", () => {
      expect(obtenerTotalesActivas([])).toEqual([]);
    });
  });
});
