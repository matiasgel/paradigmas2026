import { describe, it, expect } from "vitest";
import {
  calcularDescuento,
  aplicarReglas,
  generarResumen,
  type Orden,
  type Regla,
} from "../src/ej18.js";

const reglas: Regla[] = [
  { nombre: "VIP", condicion: (o) => o.total > 500, porcentaje: 20 },
  { nombre: "Regular", condicion: (o) => o.total > 100, porcentaje: 10 },
];

describe("Ej18 — Separar efectos puros de I/O", () => {
  describe("calcularDescuento", () => {
    it("aplica porcentaje correctamente", () => {
      expect(calcularDescuento(200, 10)).toBe(180);
    });

    it("descuento 0 no modifica", () => {
      expect(calcularDescuento(100, 0)).toBe(100);
    });

    it("descuento 100 da cero", () => {
      expect(calcularDescuento(250, 100)).toBe(0);
    });
  });

  describe("aplicarReglas", () => {
    it("aplica primera regla que matchea (VIP)", () => {
      const o: Orden = { id: 1, cliente: "A", total: 600, categoria: "e", activa: true };
      const r = aplicarReglas(o, reglas);
      expect(r.descuento).toBe(20);
      expect(r.totalFinal).toBe(480);
    });

    it("aplica segunda regla si primera no matchea", () => {
      const o: Orden = { id: 2, cliente: "B", total: 200, categoria: "e", activa: true };
      const r = aplicarReglas(o, reglas);
      expect(r.descuento).toBe(10);
      expect(r.totalFinal).toBe(180);
    });

    it("sin match: descuento 0", () => {
      const o: Orden = { id: 3, cliente: "C", total: 50, categoria: "e", activa: true };
      const r = aplicarReglas(o, reglas);
      expect(r.descuento).toBe(0);
      expect(r.totalFinal).toBe(50);
    });

    it("preserva campos originales", () => {
      const o: Orden = { id: 4, cliente: "D", total: 200, categoria: "ropa", activa: false };
      const r = aplicarReglas(o, reglas);
      expect(r.id).toBe(4);
      expect(r.cliente).toBe("D");
      expect(r.categoria).toBe("ropa");
    });
  });

  describe("generarResumen", () => {
    it("agrega correctamente", () => {
      const ordenes = [
        { id: 1, cliente: "A", total: 600, categoria: "e", activa: true, descuento: 20, totalFinal: 480 },
        { id: 2, cliente: "B", total: 200, categoria: "e", activa: true, descuento: 10, totalFinal: 180 },
      ];
      const r = generarResumen(ordenes);
      expect(r.totalOriginal).toBe(800);
      expect(r.totalFinal).toBe(660);
      expect(r.ahorro).toBe(140);
      expect(r.cantidad).toBe(2);
    });

    it("array vacío", () => {
      expect(generarResumen([])).toEqual({ totalOriginal: 0, totalFinal: 0, ahorro: 0, cantidad: 0 });
    });
  });
});
