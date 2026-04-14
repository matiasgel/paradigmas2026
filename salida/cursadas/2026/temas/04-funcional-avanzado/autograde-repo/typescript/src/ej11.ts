// Ejercicio 11 — Middleware como HOF (6 pts)
// Trazabilidad: F-22, F-23

export type Request = { headers: Record<string, string>; body: unknown; meta: { logs: string[] } };
export type Response = { status: number; body: unknown };
export type Handler = (req: Request) => Response;
export type Middleware = (handler: Handler) => Handler;

// Si authorization header es "Bearer <secret>", continúa. Si no, 401.
export function withAuth(secret: string): Middleware {
  throw new Error("TODO: implementar");
}

// Agrega "[prefix] request" a req.meta.logs antes de llamar al handler.
export function withLogging(prefix: string): Middleware {
  throw new Error("TODO: implementar");
}
