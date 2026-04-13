# Minuta Clase 04 — Aspectos Avanzados de Programación Funcional
**Materia:** Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI
**Tema:** 04 | **Duración:** 120 minutos

## Objetivos de la clase

- OA-1: Comparar patrones funcionales entre Clojure y TypeScript.
- OA-2: Usar pipelines y composición para resolver problemas reales en TS.
- OA-3: Aplicar `partial`, `curry` y funciones de orden superior en APIs web.
- OA-4: Modelar errores con `Result` y `Maybe` en TypeScript.
- OA-5: Comprender recursión de cola en Clojure y su equivalencia en TS.

---

## Bloque 1 — Fundamentos avanzados (35 min)

### [F-01] Apertura y propósito
**Tiempo:** 3 min

- Presentar el objetivo: usar menos estado mutable y más composición.
- Conectar con problemas reales: validación de formularios, pipelines de API y middleware.
- Señalar que el foco es Clojure + TypeScript.

**Frase guía:** “Hoy veremos cómo los mismos patrones ayudan a construir código web más mantenible.”

---

### [F-02] Imperativo vs funcional
**Tiempo:** 4 min

- Comparar un procesamiento de órdenes con un bucle mutante y un pipeline declarativo.
- Mostrar la intención explícita de `filter`, `map`, `reduce`.

**Ejemplo TS:**
```typescript
const ordenes = [
  { id: 1, total: 120, activa: true },
  { id: 2, total: 50,  activa: false },
  { id: 3, total: 200, activa: true },
];

const totalActivas = ordenes
  .filter(o => o.activa)
  .map(o => o.total)
  .reduce((acc, total) => acc + total, 0);
```

**Énfasis:** el array original no muta.

---

### [F-03] Funciones puras e inmutabilidad
**Tiempo:** 5 min

- Definir función pura y mostrar la diferencia con efectos.
- Mostrar objeto inmutable y array nuevo con spread.

**Ejemplo TS:**
```typescript
const persona = { name: "Ana", age: 28 };
const personaActualizada = { ...persona, age: 29 };
```

**Punto clave:** el valor original permanece intacto.

---

### [F-04] Pipeline web en TypeScript
**Tiempo:** 5 min

- Mostrar un pipeline de validación y transformación de datos de formulario.

**Ejemplo TS:**
```typescript
const datosForm = { nombre: "Ana", email: "ana@test.com", edad: "27" };
const validators = [
  validateRequired("nombre"),
  validateEmail("email"),
  validateNumber("edad"),
];

const resultado = pipe(...validators)(datosForm);
```

**Énfasis:** cada paso devuelve un nuevo valor, no modifica `datosForm`.

---

### [F-05] `filter`, `map` y `reduce`
**Tiempo:** 5 min

- Explicar la firma y uso de cada operación.
- Usar un ejemplo de pipeline de métricas de órdenes.

**Ejemplo TS:**
```typescript
const totales = ordenes
  .filter(o => o.activa)
  .map(o => o.total)
  .reduce((a, b) => a + b, 0);
```

**Pregunta rápida:** ¿qué devuelve `filter`? ¿qué tipo tiene?

---

### [F-06] Composición y `pipe`
**Tiempo:** 5 min

- Construir funciones pequeñas y componerlas.

**Ejemplo TS:**
```typescript
type Transform<T> = (items: T[]) => T[];
const filterActivas: Transform<Orden> = items => items.filter(o => o.activa);
const mapTotales: Transform<Orden>  = items => items.map(o => o.total);
const sumar: (nums: number[]) => number = nums => nums.reduce((a, b) => a + b, 0);

const pipeline = (items: Orden[]) => sumar(mapTotales(filterActivas(items)));
```

**Mensaje:** la composición separa la intención del dato.

---

## Bloque 2 — Abstracciones y efectos (35 min)

### [F-07] `Result` en TypeScript
**Tiempo:** 5 min

- Introducir `Result<T, E>` como tipo algebraico.

**Ejemplo TS:**
```typescript
type Result<T, E> =
  | { status: "ok"; value: T }
  | { status: "error"; error: E };

const validarEmail = (email: string): Result<string, string> =>
  /@/.test(email)
    ? { status: "ok", value: email }
    : { status: "error", error: "Email inválido" };
```

---

### [F-08] Manejo explícito de errores
**Tiempo:** 5 min

- Comparar `throw` con `Result`.
- Mostrar cómo evitar excepciones atrapadas fuera de la firma.

**Ejemplo TS:**
```typescript
const procesarForm = (data: FormData): Result<User, string> => {
  const emailValid = validarEmail(data.email);
  if (emailValid.status === "error") return emailValid;

  return { status: "ok", value: { email: emailValid.value } };
};
```

---

### [F-09] `Maybe` / `Option`
**Tiempo:** 5 min

- Explicar ausencia segura de valor.

**Ejemplo TS:**
```typescript
type Maybe<T> = { some: true; value: T } | { some: false };
```

- Usar en búsqueda de usuario o campo opcional.

---

### [F-10] Validación funcional de formularios
**Tiempo:** 5 min

- Ejemplo práctico de pipeline de validadores reutilizables.

**Ejemplo TS:**
```typescript
const validateRequired = (field: keyof FormData) =>
  (data: FormData): Result<FormData, string> =>
    data[field]?.trim()
      ? { status: "ok", value: data }
      : { status: "error", error: `${field} es obligatorio` };
```

---

### [F-11] Currying y partial application
**Tiempo:** 5 min

- Definir `curry` y `partial`.
- Mostrar uso en configuradores de handlers.

**Ejemplo TS:**
```typescript
const curry = <A, B, C>(fn: (a: A, b: B) => C) =>
  (a: A) => (b: B) => fn(a, b);
```

---

### [F-12] Handlers web composables
**Tiempo:** 5 min

- Aplicar `partial` y `curry` a middlewares.

**Ejemplo TS:**
```typescript
const addHeader = (name: string, value: string) =>
  (req: Request) => ({ ...req, headers: { ...req.headers, [name]: value } });
```

---

## Bloque 3 — Recursión de cola y Clojure (30 min)

### [F-13] Recursión de cola en Clojure
**Tiempo:** 5 min

- Mostrar cómo evitar stack overflow con `recur`.

**Ejemplo Clojure:**
```clojure
(defn sum-tail [nums acc]
  (if (empty? nums)
    acc
    (recur (rest nums) (+ acc (first nums)))))
```

---

### [F-14] Equivalente idiomático en TS
**Tiempo:** 5 min

- Comparar con función recursiva segura en TS.

**Ejemplo TS:**
```typescript
const sumTail = (nums: number[], acc = 0): number =>
  nums.length === 0 ? acc : sumTail(nums.slice(1), acc + nums[0]);
```

---

### [F-15] Transducers conceptuales
**Tiempo:** 5 min

- Explicar la idea: transformar datos sin colecciones intermedias.
- Mostrar `comp` en Clojure.

**Ejemplo Clojure:**
```clojure
(def xf (comp (filter even?) (map #(* % %))))
```

---

### [F-16] Aplicación práctica en TS
**Tiempo:** 5 min

- Mostrar la idea de `pipe` para construir pipelines de datos web.
- Enfatizar reutilización y testabilidad en APIs.

---

### [F-17] Taller comparativo
**Tiempo:** 10 min

- Proponer ejercicio de clase: validar un formulario y calcular un resultado.
- Orientar a grupos a discutir tipos, pureza y composición.

---

## Bloque 4 — Cierre y reflexión (10 min)

### [F-18] Resumen y recomendaciones
**Tiempo:** 5 min

- Reforzar las ventajas de elegir la abstracción correcta.
- Conectar con el siguiente tema: monadas y patterns de control.

### [F-19] Preguntas clave
**Tiempo:** 5 min

- ¿Qué parte de este diseño ayuda más al desarrollo web?
- ¿Qué patrón usarían para una validación de múltiples campos?
