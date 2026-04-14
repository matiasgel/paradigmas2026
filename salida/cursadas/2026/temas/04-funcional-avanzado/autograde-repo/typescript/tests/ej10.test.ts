// Tests — Ejercicio 10: Result y validación encadenada
import { describe, it, expect } from "vitest";
import { chain, validateForm, handleResult, ok, err } from "../src/ej10";

describe("chain", () => {
  it("propaga error", () => {
    expect(chain(err("fallo"), () => ok({ name: "x", email: "x", password: "x" }))).toEqual({
      status: "error",
      error: "fallo",
    });
  });
  it("aplica validator si ok", () => {
    const data = { name: "Ana", email: "a@b.com", password: "12345678" };
    expect(chain(ok(data), d => ok(d))).toEqual({ status: "ok", value: data });
  });
});

describe("validateForm", () => {
  it("datos válidos", () => {
    const data = { name: "Ana", email: "ana@test.com", password: "12345678" };
    expect(validateForm(data)).toEqual({ status: "ok", value: data });
  });
  it("nombre vacío", () => {
    expect(validateForm({ name: "", email: "a@b.com", password: "12345678" })).toEqual({
      status: "error",
      error: "nombre requerido",
    });
  });
  it("email inválido", () => {
    expect(validateForm({ name: "Ana", email: "invalid", password: "12345678" })).toEqual({
      status: "error",
      error: "email inválido",
    });
  });
  it("password corta", () => {
    expect(validateForm({ name: "Ana", email: "a@b.com", password: "123" })).toEqual({
      status: "error",
      error: "contraseña muy corta",
    });
  });
  it("primer error gana", () => {
    const r = validateForm({ name: "", email: "bad", password: "1" });
    expect(r.status).toBe("error");
    if (r.status === "error") expect(r.error).toBe("nombre requerido");
  });
});

describe("handleResult", () => {
  it("200 si ok", () => {
    const data = { name: "Ana", email: "a@b.com", password: "12345678" };
    expect(handleResult(ok(data))).toEqual({ status: 200, body: { user: data } });
  });
  it("400 si error", () => {
    expect(handleResult(err("nombre requerido"))).toEqual({
      status: 400,
      body: { error: "nombre requerido" },
    });
  });
});
