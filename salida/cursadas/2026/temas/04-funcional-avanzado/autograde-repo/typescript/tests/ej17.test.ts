import { describe, it, expect } from "vitest";
import { procesarLote, filtrarAsync } from "../src/ej17.js";

describe("Ej17 — async/await", () => {
  describe("procesarLote", () => {
    it("transforma todos los items", async () => {
      const result = await procesarLote([1, 2, 3], async (x) => x * 10);
      expect(result).toEqual([10, 20, 30]);
    });

    it("array vacío", async () => {
      const result = await procesarLote([], async (x: number) => x);
      expect(result).toEqual([]);
    });

    it("transforma con operación async", async () => {
      const result = await procesarLote(["a", "b"], async (s) => s.toUpperCase());
      expect(result).toEqual(["A", "B"]);
    });
  });

  describe("filtrarAsync", () => {
    it("filtra con predicado async", async () => {
      const result = await filtrarAsync([1, 2, 3, 4, 5], async (x) => x % 2 === 0);
      expect(result).toEqual([2, 4]);
    });

    it("ninguno pasa el filtro", async () => {
      const result = await filtrarAsync([1, 3, 5], async (x) => x % 2 === 0);
      expect(result).toEqual([]);
    });

    it("todos pasan el filtro", async () => {
      const result = await filtrarAsync([2, 4, 6], async (x) => x % 2 === 0);
      expect(result).toEqual([2, 4, 6]);
    });

    it("preserva el orden", async () => {
      const result = await filtrarAsync([5, 1, 4, 2, 3], async (x) => x > 2);
      expect(result).toEqual([5, 4, 3]);
    });
  });
});
