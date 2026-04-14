// Tests — Ejercicio 2: Composición pipe/compose
import { describe, it, expect } from "vitest";
import { pipe, compose, normalizeEmail } from "../src/ej02";

const inc = (x: number) => x + 1;
const doble = (x: number) => x * 2;
const triple = (x: number) => x * 3;

describe("pipe", () => {
  it("compone izquierda a derecha", () => {
    expect(pipe(inc, doble)(3)).toBe(8);
  });
  it("sin funciones es identidad", () => {
    expect(pipe<number>()(5)).toBe(5);
  });
  it("una sola función", () => {
    expect(pipe(doble)(4)).toBe(8);
  });
  it("tres funciones", () => {
    expect(pipe(inc, doble, triple)(1)).toBe(12);
  });
});

describe("compose", () => {
  it("compone derecha a izquierda", () => {
    expect(compose(inc, doble)(3)).toBe(7);
  });
  it("sin funciones es identidad", () => {
    expect(compose<number>()(5)).toBe(5);
  });
  it("tres funciones", () => {
    expect(compose(triple, doble, inc)(1)).toBe(12);
  });
});

describe("normalizeEmail", () => {
  it("trim + lowercase + agrega dominio", () => {
    expect(normalizeEmail("  ANA  ")).toBe("ana@empresa.com");
  });
  it("trim + lowercase sin agregar dominio", () => {
    expect(normalizeEmail("  Bob@test.com  ")).toBe("bob@test.com");
  });
  it("string vacío agrega dominio", () => {
    expect(normalizeEmail("  ")).toBe("@empresa.com");
  });
});
