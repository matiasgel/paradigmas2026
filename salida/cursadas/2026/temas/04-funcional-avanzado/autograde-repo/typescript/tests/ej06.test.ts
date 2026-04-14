// Tests — Ejercicio 6: Partial application
import { describe, it, expect } from "vitest";
import { partial, makeGreeter, makeRequiredValidator } from "../src/ej06";

describe("partial", () => {
  it("fija primer argumento", () => {
    const add = (a: number, b: number) => a + b;
    expect(partial(add, 5)(3)).toBe(8);
  });
  it("con strings", () => {
    const concat = (a: string, b: string) => a + b;
    expect(partial(concat, "hola ")("mundo")).toBe("hola mundo");
  });
});

describe("makeGreeter", () => {
  it("crea saludador", () => {
    expect(makeGreeter("Hola")("Ana")).toBe("Hola, Ana");
  });
  it("con otro saludo", () => {
    expect(makeGreeter("Chau")("Luis")).toBe("Chau, Luis");
  });
});

describe("makeRequiredValidator", () => {
  it("ok si no vacío", () => {
    expect(makeRequiredValidator("email")("ana@test.com")).toEqual({
      status: "ok",
      value: "ana@test.com",
    });
  });
  it("error si vacío", () => {
    expect(makeRequiredValidator("email")("")).toEqual({
      status: "error",
      error: "email es obligatorio",
    });
  });
  it("error si solo espacios", () => {
    expect(makeRequiredValidator("nombre")("   ")).toEqual({
      status: "error",
      error: "nombre es obligatorio",
    });
  });
});
