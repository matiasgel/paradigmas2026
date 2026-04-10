import { describe, it, expect } from "vitest";
import { ok, err, mapResult, flatMapResult, dividir } from "../src/ej08.js";

describe("Ej08 — Result<T, E>", () => {
  describe("mapResult", () => {
    it("aplica fn cuando es ok", () => {
      expect(mapResult(ok(10), (x) => x * 2)).toEqual({ ok: true, value: 20 });
    });

    it("propaga error sin modificar", () => {
      expect(mapResult(err("fallo"), (x: number) => x * 2)).toEqual({ ok: false, error: "fallo" });
    });

    it("cambia el tipo del value", () => {
      expect(mapResult(ok(42), String)).toEqual({ ok: true, value: "42" });
    });
  });

  describe("flatMapResult", () => {
    it("aplica fn que retorna ok", () => {
      expect(flatMapResult(ok(10), (x) => ok(x + 5))).toEqual({ ok: true, value: 15 });
    });

    it("aplica fn que retorna error", () => {
      expect(flatMapResult(ok(10), (_) => err("boom"))).toEqual({ ok: false, error: "boom" });
    });

    it("propaga error sin ejecutar fn", () => {
      const fn = (x: number) => ok(x * 2);
      expect(flatMapResult(err("original"), fn)).toEqual({ ok: false, error: "original" });
    });
  });

  describe("dividir", () => {
    it("divide correctamente", () => {
      expect(dividir(10, 2)).toEqual({ ok: true, value: 5 });
    });

    it("retorna error al dividir por cero", () => {
      expect(dividir(10, 0)).toEqual({ ok: false, error: "División por cero" });
    });

    it("funciona con decimales", () => {
      const r = dividir(7, 2);
      expect(r.ok).toBe(true);
      if (r.ok) expect(r.value).toBe(3.5);
    });
  });

  describe("composición", () => {
    it("encadena dividir con mapResult", () => {
      const r = dividir(10, 2);
      expect(mapResult(r, (x) => x * 3)).toEqual({ ok: true, value: 15 });
    });

    it("encadena dos dividir con flatMapResult", () => {
      const r = flatMapResult(dividir(100, 4), (x) => dividir(x, 5));
      expect(r).toEqual({ ok: true, value: 5 });
    });
  });
});
