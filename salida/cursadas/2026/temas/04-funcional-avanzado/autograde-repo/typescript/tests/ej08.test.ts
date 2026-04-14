// Tests — Ejercicio 8: Currying
import { describe, it, expect } from "vitest";
import { curry2, curry3 } from "../src/ej08";

describe("curry2", () => {
  it("curry de suma", () => {
    const cAdd = curry2((a: number, b: number) => a + b);
    expect(cAdd(3)(4)).toBe(7);
  });
  it("curry de hasMinLength", () => {
    const cMin = curry2((min: number, str: string) => str.length >= min);
    expect(cMin(8)("password123")).toBe(true);
    expect(cMin(8)("short")).toBe(false);
  });
  it("reutilizar funciones parciales", () => {
    const cMul = curry2((a: number, b: number) => a * b);
    const doble = cMul(2);
    const triple = cMul(3);
    expect(doble(5)).toBe(10);
    expect(triple(5)).toBe(15);
  });
});

describe("curry3", () => {
  it("curry de 3 argumentos", () => {
    const cSum3 = curry3((a: number, b: number, c: number) => a + b + c);
    expect(cSum3(1)(2)(3)).toBe(6);
  });
  it("aplicación parcial escalonada", () => {
    const cConcat = curry3((a: string, b: string, c: string) => a + b + c);
    const ab = cConcat("a")("b");
    expect(ab("c")).toBe("abc");
  });
});
