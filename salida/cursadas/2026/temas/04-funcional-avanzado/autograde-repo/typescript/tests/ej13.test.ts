import { describe, it, expect } from "vitest";
import { chainResults, traverseResults, filterOk, ok, err } from "../src/ej13.js";

describe("Ej13 — API genérica funcional", () => {
  describe("chainResults", () => {
    it("encadena funciones que retornan ok", () => {
      const inc = (x: number) => ok(x + 1);
      const doble = (x: number) => ok(x * 2);
      expect(chainResults(3, [inc, doble])).toEqual({ ok: true, value: 8 });
    });

    it("propaga el primer error", () => {
      const inc = (x: number) => ok(x + 1);
      const falla = (_: number) => err("boom");
      const doble = (x: number) => ok(x * 2);
      expect(chainResults(3, [inc, falla, doble])).toEqual({ ok: false, error: "boom" });
    });

    it("sin funciones retorna ok con initial", () => {
      expect(chainResults(42, [])).toEqual({ ok: true, value: 42 });
    });

    it("error en la primera función", () => {
      const falla = (_: number) => err("inicio");
      expect(chainResults(1, [falla])).toEqual({ ok: false, error: "inicio" });
    });
  });

  describe("traverseResults", () => {
    it("todos ok → ok con array", () => {
      expect(traverseResults([ok(1), ok(2), ok(3)])).toEqual({ ok: true, value: [1, 2, 3] });
    });

    it("un error → retorna primer error", () => {
      expect(traverseResults([ok(1), err("x"), ok(3)])).toEqual({ ok: false, error: "x" });
    });

    it("array vacío → ok con array vacío", () => {
      expect(traverseResults([])).toEqual({ ok: true, value: [] });
    });

    it("primer error cuando hay múltiples", () => {
      expect(traverseResults([err("a"), err("b")])).toEqual({ ok: false, error: "a" });
    });
  });

  describe("filterOk", () => {
    it("extrae solo los valores ok", () => {
      expect(filterOk([ok(1), err("x"), ok(3), err("y")])).toEqual([1, 3]);
    });

    it("todos ok", () => {
      expect(filterOk([ok(10), ok(20)])).toEqual([10, 20]);
    });

    it("todos error → vacío", () => {
      expect(filterOk([err("a"), err("b")])).toEqual([]);
    });

    it("array vacío → vacío", () => {
      expect(filterOk([])).toEqual([]);
    });
  });
});
