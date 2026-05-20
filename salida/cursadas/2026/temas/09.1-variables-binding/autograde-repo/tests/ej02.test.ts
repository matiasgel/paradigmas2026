import { describe, it, expect } from "vitest";
import { parseAndAdd, onlyNumbers, groupByType, applyTwice } from "../src/ej02";

describe("Ej02 — Binding de tipos en TypeScript: tipado estático y coerciones", () => {

  // --- parseAndAdd ---
  describe("parseAndAdd", () => {
    it('"3" + "4" = 7', () => expect(parseAndAdd("3", "4")).toBe(7));
    it("con cero: \"0\" + \"5\" = 5", () => expect(parseAndAdd("0", "5")).toBe(5));
    it("decimales: \"1.5\" + \"2.5\" = 4", () => expect(parseAndAdd("1.5", "2.5")).toBe(4));
    it('"100" + "200" = 300', () => expect(parseAndAdd("100", "200")).toBe(300));
    it("lanza error si 'a' no es un número válido", () => {
      expect(() => parseAndAdd("abc", "4")).toThrow("invalid number");
    });
    it("lanza error si 'b' no es un número válido", () => {
      expect(() => parseAndAdd("3", "xyz")).toThrow("invalid number");
    });
    it("retorna un number, no un string", () => {
      expect(typeof parseAndAdd("1", "2")).toBe("number");
    });
  });

  // --- onlyNumbers ---
  describe("onlyNumbers", () => {
    it("filtra solo los numbers de una lista mixta", () => {
      expect(onlyNumbers([1, "hola", 2, true, 3.5])).toEqual([1, 2, 3.5]);
    });
    it("lista con solo strings retorna vacío", () => {
      expect(onlyNumbers(["a", "b"])).toEqual([]);
    });
    it("lista con solo numbers retorna todos", () => {
      expect(onlyNumbers([1, 2, 3])).toEqual([1, 2, 3]);
    });
    it("lista vacía retorna vacía", () => {
      expect(onlyNumbers([])).toEqual([]);
    });
    it("booleans NO son numbers", () => {
      expect(onlyNumbers([true, false, 0, 1])).toEqual([0, 1]);
    });
    it("conserva el orden", () => {
      expect(onlyNumbers([3, "x", 1, true, 2])).toEqual([3, 1, 2]);
    });
  });

  // --- groupByType ---
  describe("groupByType", () => {
    it("agrupa los tres tipos correctamente", () => {
      expect(groupByType(["a", 1, true, "b", 2])).toEqual({
        strings: ["a", "b"],
        numbers: [1, 2],
        booleans: [true],
      });
    });
    it("lista vacía retorna tres listas vacías", () => {
      expect(groupByType([])).toEqual({ strings: [], numbers: [], booleans: [] });
    });
    it("solo strings", () => {
      expect(groupByType(["x", "y"])).toEqual({
        strings: ["x", "y"], numbers: [], booleans: [],
      });
    });
    it("solo booleans", () => {
      expect(groupByType([true, false])).toEqual({
        strings: [], numbers: [], booleans: [true, false],
      });
    });
    it("conserva el orden dentro de cada grupo", () => {
      const r = groupByType([3, "z", 1, false, "a", true]);
      expect(r.numbers).toEqual([3, 1]);
      expect(r.strings).toEqual(["z", "a"]);
      expect(r.booleans).toEqual([false, true]);
    });
  });

  // --- applyTwice ---
  describe("applyTwice", () => {
    it("número: fn(fn(3)) con fn = *2 → 12", () => {
      expect(applyTwice((x: number) => x * 2, 3)).toBe(12);
    });
    it("suma 1 dos veces a 0 → 2", () => {
      expect(applyTwice((x: number) => x + 1, 0)).toBe(2);
    });
    it("string: agrega '!' dos veces → 'hola!!'", () => {
      expect(applyTwice((x: string) => x + "!", "hola")).toBe("hola!!");
    });
    it("función identidad: retorna el mismo valor", () => {
      expect(applyTwice((x: number) => x, 42)).toBe(42);
    });
    it("fn se invoca exactamente 2 veces", () => {
      let count = 0;
      applyTwice((x: number) => { count++; return x + 1; }, 0);
      expect(count).toBe(2);
    });
  });
});

