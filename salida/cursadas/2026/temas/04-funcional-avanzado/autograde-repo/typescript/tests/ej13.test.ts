// Tests — Ejercicio 13: Recursión de cola TS
import { describe, it, expect } from "vitest";
import { sumList, factorial, findInTree, TreeNode } from "../src/ej13";

describe("sumList", () => {
  it("suma lista", () => {
    expect(sumList([1, 2, 3, 4, 5])).toBe(15);
  });
  it("vacío es 0", () => {
    expect(sumList([])).toBe(0);
  });
  it("un elemento", () => {
    expect(sumList([42])).toBe(42);
  });
});

describe("factorial", () => {
  it("factorial(5)", () => {
    expect(factorial(5)).toBe(120);
  });
  it("factorial(0)", () => {
    expect(factorial(0)).toBe(1);
  });
  it("factorial(1)", () => {
    expect(factorial(1)).toBe(1);
  });
  it("factorial(10)", () => {
    expect(factorial(10)).toBe(3628800);
  });
});

describe("findInTree", () => {
  const tree: TreeNode = {
    value: 1,
    children: [
      { value: 2, children: [{ value: 4, children: [] }] },
      { value: 3, children: [{ value: 5, children: [] }] },
    ],
  };
  it("encuentra valor existente", () => {
    expect(findInTree([tree], 4)).toBe(4);
  });
  it("encuentra raíz", () => {
    expect(findInTree([tree], 1)).toBe(1);
  });
  it("null si no existe", () => {
    expect(findInTree([tree], 99)).toBeNull();
  });
  it("null si vacío", () => {
    expect(findInTree([], 1)).toBeNull();
  });
});
