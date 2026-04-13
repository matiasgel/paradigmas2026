# Guía de Estudio — Tema 04

## Aspectos Avanzados de Programación Funcional

> **Materia:** Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI
> **Clase:** 04 | **Duración estimada:** 4-5 horas

---

## Propósito

Esta guía acompaña el diseño aprobado del tema 04 y está orientada a que el alumno entienda el valor práctico de los patrones funcionales en desarrollo web, especialmente en TypeScript.

## Objetivos de aprendizaje

- Comprender la diferencia entre código imperativo y funcional.
- Usar `map`, `filter`, `reduce` y composición en pipelines reales.
- Modelar errores con `Result` y ausencias con `Maybe`.
- Aplicar `partial` y `curry` en validadores, handlers y middlewares.
- Entender la recursión de cola y su uso en algoritmos de procesamiento.

## Conceptos previos

- Función pura e inmutabilidad.
- Tipos básicos en TypeScript.
- Uso de arrays y objetos inmutables.
- Lectura básica de Clojure (`defn`, `->>`, `filter`, `map`).

---

## 1. Fundamentos funcionales en TypeScript

### 1.1 Qué es una función pura

Una función pura depende únicamente de sus parámetros y siempre devuelve el mismo resultado para los mismos valores. No debe leer ni modificar variables externas.

**Ejemplo:**
```typescript
const doble = (x: number) => x * 2;
```

### 1.2 Por qué la inmutabilidad importa

En aplicaciones web, el estado compartido puede causar bugs sutiles si varios componentes o requests leen y escriben la misma estructura.

```typescript
const usuario = { name: "Ana", age: 28 };
const actualizado = { ...usuario, age: 29 };
```

### 1.3 Pipeline de datos reales

Un pipeline permite transformar datos paso a paso sin mutar.

```typescript
type Orden = { id: number; total: number; activa: boolean };

const ordenes: Orden[] = [
  { id: 1, total: 120, activa: true },
  { id: 2, total: 50, activa: false },
  { id: 3, total: 200, activa: true },
];

const totalActivas = ordenes
  .filter(o => o.activa)
  .map(o => o.total)
  .reduce((acc, total) => acc + total, 0);
```

**Uso práctico:** cálculo de facturación, métricas de dashboard y transformaciones de resultados de API.

---

## 2. Validación funcional y `Result`

### 2.1 Modelo `Result` en TypeScript

Este patrón convierte el error en un valor explícito en lugar de ocultarlo en una excepción.

```typescript
type Result<T, E> =
  | { status: "ok"; value: T }
  | { status: "error"; error: E };
```

### 2.2 Ejemplo práctico de formulario

```typescript
type FormData = { nombre: string; email: string; edad: string };

type FormResult = Result<FormData, string>;

const validateRequired = (field: keyof FormData) =>
  (data: FormData): FormResult =>
    data[field].trim()
      ? { status: "ok", value: data }
      : { status: "error", error: `${field} es obligatorio` };
```

### 2.3 Pipeline de validadores

```typescript
const validateEmail = (data: FormData): FormResult =>
  /@/.test(data.email)
    ? { status: "ok", value: data }
    : { status: "error", error: "Email inválido" };

const validateForm = (data: FormData): FormResult => {
  const validators = [validateRequired("nombre"), validateRequired("email"), validateEmail];
  return validators.reduce((acc, validate) => {
    if (acc.status === "error") return acc;
    return validate(acc.value);
  }, { status: "ok", value: data } as FormResult);
};
```

**Aplicación real:** validación en frontend, APIs REST y servicios que procesan formularios.

---

## 3. Currying y middlewares en TypeScript

### 3.1 Currying

Currying convierte una función que recibe varios argumentos en una cadena de funciones que reciben argumentos uno a uno.

```typescript
const curry = <A, B, C>(fn: (a: A, b: B) => C) =>
  (a: A) => (b: B) => fn(a, b);
```

### 3.2 Middlewares y handlers composables

En desarrollo web, un middleware puede ser tratado como una función que recibe y devuelve un request o contexto.

```typescript
type Request = { headers: Record<string, string>; body: unknown };
type Middleware = (req: Request) => Request;

const addHeader = (name: string, value: string): Middleware =>
  req => ({ ...req, headers: { ...req.headers, [name]: value } });

const compose = (...fns: Middleware[]) =>
  (req: Request) => fns.reduce((acc, fn) => fn(acc), req);
```

**Uso práctico:** construir pipelines de request/response en servidores, validación de seguridad y procesamiento de datos.

---

## 4. Recursión de cola y Clojure

### 4.1 Recursión de cola en Clojure

```clojure
(defn sum-tail [nums acc]
  (if (empty? nums)
    acc
    (recur (rest nums) (+ acc (first nums)))))
```

### 4.2 Equivalente en TypeScript

```typescript
const sumTail = (nums: number[], acc = 0): number =>
  nums.length === 0 ? acc : sumTail(nums.slice(1), acc + nums[0]);
```

**Concepto clave:** el punto recursivo queda en cola, evitando acumulación extra de stack.

---

## 5. Ejercicios

### Ejercicio 1 — Validación de formulario funcional

Construir un flujo de validación que:
- Verifique campos obligatorios.
- Valide formato de email.
- Devuelva `Result<FormData, string>`.

### Ejercicio 2 — Pipeline de órdenes de venta

Dado un arreglo de órdenes, generar un reporte que:
- Filtre órdenes activas.
- Calcule el total por cliente.
- Retorne un objeto `{ [clienteId]: total }`.

### Ejercicio 3 — Handler composable

Implementar un middleware que:
- Agregue un header de tracing.
- Valide que el request tenga un token.
- Devuelva el request transformado.

---

## 6. Autoevaluación

- ¿Cuál es la diferencia entre `filter` y `map`?
- ¿Qué problema resuelve `Result`?
- ¿Por qué es útil `curry` en un middleware?
- ¿Cómo ayuda la recursión de cola a evitar stack overflow?

---

## Glosario

- **Pipeline:** cadena de transformaciones de datos.
- **`Result`:** tipo que modela éxito o error.
- **Currying:** descomposición de una función de varios argumentos en varias funciones de un argumento.
- **`Maybe`:** tipo que representa presencia o ausencia de valor.
- **Inmutabilidad:** no modificar valores existentes.
