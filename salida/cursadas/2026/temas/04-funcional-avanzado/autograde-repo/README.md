# TP 04: Aspectos Avanzados de Programación Funcional

**Materia:** Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI
**Puntos totales:** 100 (20 ejercicios)
**Lenguajes:** TypeScript (60 pts) + Clojure (40 pts)

---

## Objetivo

Implementar soluciones funcionales que cubran pipelines, inmutabilidad, tipos algebraicos (`Result`, `Maybe`), transducers, concurrencia (`core.async`, STM) y composición. Cada ejercicio tiene tests automáticos que se ejecutan con cada push.

## Estructura del repo

```
typescript/           ← Ejercicios en TypeScript (1,2,3,7,8,9,13,14,17,18,19)
  src/ejXX.ts         ← Acá implementás las soluciones
  tests/ejXX.test.ts  ← Tests (NO modificar)

clojure/              ← Ejercicios en Clojure (4,5,6,10,11,12,15,16,20)
  src/tp04/ejXX.clj   ← Acá implementás las soluciones
  test/tp04/ejXX_test.clj  ← Tests (NO modificar)
```

## Setup local

### TypeScript

```bash
cd typescript
npm install
npx vitest run                          # correr todos los tests
npx vitest run tests/ej01.test.ts       # correr un ejercicio específico
npx vitest                              # modo watch
```

Requisitos: Node.js 20+

### Clojure

```bash
cd clojure
lein deps
lein test                               # correr todos los tests
lein test tp04.ej04-test                # correr un ejercicio específico
```

Requisitos: Java 21+, [Leiningen](https://leiningen.org/)

## Consignas

Cada archivo `src/ejXX.ts` o `src/tp04/ejXX.clj` tiene la consigna completa con los tipos y firmas de funciones. Solo tenés que implementar las funciones marcadas con `TODO`.

| Ej | Tema | Lenguaje | Pts |
|----|------|----------|-----|
| 1 | Pipeline filter/map/reduce | TS | 3 |
| 2 | Composición pipe/compose | TS | 5 |
| 3 | Inmutabilidad | TS | 3 |
| 4 | Pipeline ->> | Clojure | 3 |
| 5 | Secuencias perezosas | Clojure | 5 |
| 6 | Colecciones persistentes | Clojure | 3 |
| 7 | ADT tipo suma (Shape) | TS | 5 |
| 8 | Result\<T,E\> | TS | 6 |
| 9 | Maybe / Option | TS | 5 |
| 10 | Errores como datos | Clojure | 5 |
| 11 | Transducer básico | Clojure | 5 |
| 12 | Transducer vs pipeline | Clojure | 5 |
| 13 | API genérica funcional | TS | 7 |
| 14 | Funciones de orden superior | TS | 5 |
| 15 | core.async canales | Clojure | 6 |
| 16 | STM transacciones | Clojure | 6 |
| 17 | async/await | TS | 5 |
| 18 | Separar efectos puros | TS | 5 |
| 19 | Integrador TypeScript | TS | 6 |
| 20 | Integrador Clojure | Clojure | 7 |

## Cómo entregar

1. Aceptá el assignment desde el link que te mandó tu docente.
2. GitHub crea un repo privado en tu cuenta.
3. Cloná tu repo: `git clone <url-de-tu-repo>`
4. Implementá la solución en los archivos `src/`.
5. Hacé commit y push. GitHub Classroom ejecuta los tests automáticamente.
6. Verificá que el check ✅ aparece en tu repo antes de la fecha límite.

## Restricciones

- **No modifiques los archivos de test** (`tests/` ni `test/`).
- **No modifiques** `package.json`, `tsconfig.json`, `project.clj` ni el workflow de GitHub Actions.
- Usá solo las funciones y tipos que ya están definidos en cada archivo.
- En los ejercicios de TypeScript: **no usar `let`, `var` ni bucles `for`/`while`** salvo que se indique lo contrario.
