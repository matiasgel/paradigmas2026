import { describe, it, expect } from "vitest";
import { buggyVarLoop, fixedVarLoop, buggySum, fixedSum, fixedSumArray } from "../src/ej05";

describe("Ej05 — Detectar y corregir errores de binding y ámbito", () => {

  // --- 5a: var hoisting ---
  describe("buggyVarLoop vs fixedVarLoop", () => {
    it("buggyVarLoop(3) retorna [3,3,3] — demuestra que var comparte el binding", () => {
      expect(buggyVarLoop(3)).toEqual([3, 3, 3]);
    });

    it("buggyVarLoop(5) retorna [5,5,5,5,5]", () => {
      expect(buggyVarLoop(5)).toEqual([5, 5, 5, 5, 5]);
    });

    it("fixedVarLoop(3) retorna [0,1,2] — let crea binding independiente por iteración", () => {
      expect(fixedVarLoop(3)).toEqual([0, 1, 2]);
    });

    it("fixedVarLoop(0) retorna array vacío", () => {
      expect(fixedVarLoop(0)).toEqual([]);
    });

    it("fixedVarLoop(5) retorna [0,1,2,3,4]", () => {
      expect(fixedVarLoop(5)).toEqual([0, 1, 2, 3, 4]);
    });

    it("fixedVarLoop(1) retorna [0]", () => {
      expect(fixedVarLoop(1)).toEqual([0]);
    });
  });

  // --- 5b: shadowing ---
  describe("buggySum vs fixedSum", () => {
    it("buggySum([1,2,3]) retorna 0 — el shadowing impide acumular", () => {
      expect(buggySum([1, 2, 3])).toBe(0);
    });

    it("fixedSum([1,2,3]) = 6", () => {
      expect(fixedSum([1, 2, 3])).toBe(6);
    });

    it("fixedSum([]) = 0 (array vacío)", () => {
      expect(fixedSum([])).toBe(0);
    });

    it("fixedSum([5]) = 5 (un elemento)", () => {
      expect(fixedSum([5])).toBe(5);
    });

    it("fixedSum con negativos: [-1, -2, 3] = 0", () => {
      expect(fixedSum([-1, -2, 3])).toBe(0);
    });

    it("fixedSum([10, 20, 30]) = 60", () => {
      expect(fixedSum([10, 20, 30])).toBe(60);
    });
  });

  // --- 5c: suma sin variables globales ---
  describe("fixedSumArray", () => {
    it("suma básica: [1,2,3] = 6", () => expect(fixedSumArray([1, 2, 3])).toBe(6));
    it("array vacío → 0", () => expect(fixedSumArray([])).toBe(0));
    it("negativos: [-1,-2,3] = 0", () => expect(fixedSumArray([-1, -2, 3])).toBe(0));
    it("un solo elemento: [42] = 42", () => expect(fixedSumArray([42])).toBe(42));
    it("todos ceros: [0,0,0] = 0", () => expect(fixedSumArray([0, 0, 0])).toBe(0));
    it("[100, 200, 300] = 600", () => expect(fixedSumArray([100, 200, 300])).toBe(600));
  });
});
