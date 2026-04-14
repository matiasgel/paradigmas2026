// Tests — Ejercicio 11: Middleware como HOF
import { describe, it, expect } from "vitest";
import { withAuth, withLogging, Handler, Request } from "../src/ej11";

const baseHandler: Handler = (req) => ({ status: 200, body: { ok: true } });

function makeReq(authHeader?: string): Request {
  return {
    headers: authHeader ? { authorization: authHeader } : {},
    body: {},
    meta: { logs: [] },
  };
}

describe("withAuth", () => {
  it("continúa si token correcto", () => {
    const secured = withAuth("s3cret")(baseHandler);
    const res = secured(makeReq("Bearer s3cret"));
    expect(res.status).toBe(200);
  });
  it("401 si token incorrecto", () => {
    const secured = withAuth("s3cret")(baseHandler);
    const res = secured(makeReq("Bearer wrong"));
    expect(res.status).toBe(401);
    expect(res.body).toEqual({ error: "unauthorized" });
  });
  it("401 si no hay header", () => {
    const secured = withAuth("s3cret")(baseHandler);
    const res = secured(makeReq());
    expect(res.status).toBe(401);
  });
});

describe("withLogging", () => {
  it("agrega log al meta", () => {
    const logged = withLogging("api")(baseHandler);
    const req = makeReq();
    logged(req);
    expect(req.meta.logs).toContain("[api] request");
  });
  it("llama al handler y retorna su response", () => {
    const logged = withLogging("test")(baseHandler);
    const res = logged(makeReq());
    expect(res.status).toBe(200);
  });
});

describe("composición", () => {
  it("logging + auth juntos", () => {
    const pipeline = withLogging("app");
    const secured = withAuth("tok123");
    const handler = pipeline(secured(baseHandler));
    const req = makeReq("Bearer tok123");
    const res = handler(req);
    expect(res.status).toBe(200);
    expect(req.meta.logs).toContain("[app] request");
  });
});
