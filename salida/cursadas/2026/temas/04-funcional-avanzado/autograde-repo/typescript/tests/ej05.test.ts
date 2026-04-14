// Tests — Ejercicio 5: flatMap y reduce avanzado
import { describe, it, expect } from "vitest";
import { todosLosRoles, rolesUnicos, indexarPorId } from "../src/ej05";

const users = [
  { name: "Ana", roles: ["admin", "editor"] },
  { name: "Luis", roles: ["editor"] },
  { name: "María", roles: ["viewer", "editor"] },
];

describe("todosLosRoles", () => {
  it("extrae todos los roles con duplicados", () => {
    expect(todosLosRoles(users)).toEqual(["admin", "editor", "editor", "viewer", "editor"]);
  });
  it("array vacío", () => {
    expect(todosLosRoles([])).toEqual([]);
  });
});

describe("rolesUnicos", () => {
  it("sin duplicados", () => {
    expect(rolesUnicos(users).sort()).toEqual(["admin", "editor", "viewer"]);
  });
});

describe("indexarPorId", () => {
  it("construye diccionario", () => {
    expect(indexarPorId([{ id: 1, nombre: "Ana" }, { id: 2, nombre: "Luis" }])).toEqual({
      1: "Ana",
      2: "Luis",
    });
  });
  it("array vacío", () => {
    expect(indexarPorId([])).toEqual({});
  });
});
