import { describe, it, expect } from "vitest";
import { just, nothing, mapMaybe, flatMapMaybe, buscar } from "../src/ej09.js";

describe("Ej09 — Maybe / Option", () => {
  describe("mapMaybe", () => {
    it("aplica fn cuando hay valor", () => {
      expect(mapMaybe(just(5), (x) => x * 2)).toEqual({ some: true, value: 10 });
    });

    it("retorna nothing cuando no hay valor", () => {
      expect(mapMaybe(nothing<number>(), (x) => x * 2)).toEqual({ some: false });
    });

    it("cambia tipo", () => {
      expect(mapMaybe(just(42), String)).toEqual({ some: true, value: "42" });
    });
  });

  describe("flatMapMaybe", () => {
    it("aplica fn que retorna just", () => {
      expect(flatMapMaybe(just(5), (x) => just(x + 1))).toEqual({ some: true, value: 6 });
    });

    it("aplica fn que retorna nothing", () => {
      expect(flatMapMaybe(just(5), (_) => nothing())).toEqual({ some: false });
    });

    it("propaga nothing sin ejecutar fn", () => {
      expect(flatMapMaybe(nothing<number>(), (x) => just(x + 1))).toEqual({ some: false });
    });
  });

  describe("buscar", () => {
    it("encuentra el primer elemento", () => {
      expect(buscar([1, 2, 3, 4], (x) => x > 2)).toEqual({ some: true, value: 3 });
    });

    it("retorna nothing si no hay match", () => {
      expect(buscar([1, 2, 3], (x) => x > 10)).toEqual({ some: false });
    });

    it("retorna nothing para array vacío", () => {
      expect(buscar([], (_) => true)).toEqual({ some: false });
    });

    it("busca con objetos", () => {
      const personas = [{ nombre: "Ana" }, { nombre: "Boris" }];
      expect(buscar(personas, (p) => p.nombre === "Boris")).toEqual({
        some: true,
        value: { nombre: "Boris" },
      });
    });
  });
});
