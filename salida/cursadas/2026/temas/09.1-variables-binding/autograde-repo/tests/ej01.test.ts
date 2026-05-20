import { describe, it, expect } from "vitest";
import { swap, rotateLeft, doubleAll, findAndReplace } from "../src/ej01";

describe("Ej01 — L-value y R-value: variables como contenedores", () => {

  // --- swap ---
  describe("swap", () => {
    it("intercambia dos posiciones de un array de números", () => {
      const arr = [1, 2, 3, 4];
      swap(arr, 0, 3);
      expect(arr).toEqual([4, 2, 3, 1]);
    });
    it("funciona con strings", () => {
      const arr = ["a", "b", "c"];
      swap(arr, 0, 2);
      expect(arr).toEqual(["c", "b", "a"]);
    });
    it("swap del mismo índice no modifica el array", () => {
      const arr = [10, 20, 30];
      swap(arr, 1, 1);
      expect(arr).toEqual([10, 20, 30]);
    });
    it("modifica el array original (misma referencia)", () => {
      const arr = [5, 3, 8];
      const ref = arr;
      swap(arr, 0, 2);
      expect(ref).toEqual([8, 3, 5]);
    });
    it("swap adyacentes", () => {
      const arr = [7, 8, 9];
      swap(arr, 1, 2);
      expect(arr).toEqual([7, 9, 8]);
    });
  });

  // --- rotateLeft ---
  describe("rotateLeft", () => {
    it("[1,2,3,4] → [2,3,4,1]", () => {
      const arr = [1, 2, 3, 4];
      rotateLeft(arr);
      expect(arr).toEqual([2, 3, 4, 1]);
    });
    it("array de 1 elemento no cambia", () => {
      const arr = [42];
      rotateLeft(arr);
      expect(arr).toEqual([42]);
    });
    it("array vacío no lanza error", () => {
      expect(() => rotateLeft([])).not.toThrow();
    });
    it("modifica el array original (misma referencia)", () => {
      const arr = ["x", "y", "z"];
      const ref = arr;
      rotateLeft(arr);
      expect(ref).toEqual(["y", "z", "x"]);
    });
    it("doble rotación", () => {
      const arr = [1, 2, 3];
      rotateLeft(arr);
      rotateLeft(arr);
      expect(arr).toEqual([3, 1, 2]);
    });
  });

  // --- doubleAll ---
  describe("doubleAll", () => {
    it("[1,2,3] → [2,4,6]", () => {
      const arr = [1, 2, 3];
      doubleAll(arr);
      expect(arr).toEqual([2, 4, 6]);
    });
    it("array vacío no lanza error", () => {
      const arr: number[] = [];
      doubleAll(arr);
      expect(arr).toEqual([]);
    });
    it("modifica el original (L-value in-place)", () => {
      const arr = [5, 10];
      const ref = arr;
      doubleAll(arr);
      expect(ref).toEqual([10, 20]);
    });
    it("funciona con ceros", () => {
      const arr = [0, 1, 0];
      doubleAll(arr);
      expect(arr).toEqual([0, 2, 0]);
    });
    it("funciona con números negativos", () => {
      const arr = [-1, -2, 3];
      doubleAll(arr);
      expect(arr).toEqual([-2, -4, 6]);
    });
  });

  // --- findAndReplace ---
  describe("findAndReplace", () => {
    it("reemplaza todas las ocurrencias y retorna el conteo", () => {
      const arr = [1, 2, 1, 3, 1];
      expect(findAndReplace(arr, 1, 9)).toBe(3);
      expect(arr).toEqual([9, 2, 9, 3, 9]);
    });
    it("retorna 0 si no hay ocurrencias", () => {
      const arr = [1, 2, 3];
      expect(findAndReplace(arr, 5, 0)).toBe(0);
      expect(arr).toEqual([1, 2, 3]);
    });
    it("funciona con strings", () => {
      const arr = ["a", "b", "a"];
      expect(findAndReplace(arr, "a", "z")).toBe(2);
      expect(arr).toEqual(["z", "b", "z"]);
    });
    it("modifica el array original", () => {
      const arr = [1, 1];
      const ref = arr;
      findAndReplace(arr, 1, 2);
      expect(ref).toEqual([2, 2]);
    });
    it("un solo reemplazo", () => {
      const arr = [1, 2, 3];
      expect(findAndReplace(arr, 2, 99)).toBe(1);
      expect(arr).toEqual([1, 99, 3]);
    });
  });
});

