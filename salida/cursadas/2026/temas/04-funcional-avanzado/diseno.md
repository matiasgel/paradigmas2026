# Diseño del Tema 04 — Aspectos Avanzados de Programación Funcional

> ESTADO: REABIERTO
> Reabierto para rediseño de alcance y filminas.

Duración de clase: 120 minutos
Enfoque: profundizar en programación funcional con ejemplos en Clojure y TypeScript, centrándose en funciones de orden superior, aplicación parcial, currying, recursión de cola y otros patrones avanzados. Se evita la concurrencia para no sobrecargar el tema en 120 minutos.

## 1. Objetivos de aprendizaje

1. Entender cómo `higher-order functions` y `first-class functions` permiten construir abstracciones reutilizables.
2. Aprender a usar aplicación parcial y currying para crear APIs funcionales más expresivas.
3. Dominar la recursión de cola en Clojure como alternativa a bucles imperativos.
4. Aplicar funciones avanzadas de programación funcional en Clojure con claridad y composabilidad.
5. Comparar conceptos de Clojure con implementaciones idiomáticas en TypeScript, sin caer en temas de concurrencia.
6. Reconocer usos prácticos de los patrones funcionales en TypeScript en el desarrollo web: validación de formularios, composición de middleware/handlers y pipelines de transformación de datos.

## 2. Prerrequisitos

- Conocimiento de programación funcional básica en TypeScript (Tema 03).
- Comprensión de inmutabilidad, funciones puras, `map`, `filter`, `reduce`.
- Familiaridad básica con sintaxis de Clojure y estructura de listas.
- Conocimiento de tipos de función y alias en TypeScript.

## 3. Alcance del tema

### Incluye

- Funciones de orden superior en Clojure y TypeScript.
- Aplicación parcial (`partial application`) y currying como patrones de diseño.
- Recursión de cola y optimización de llamadas recursivas en Clojure.
- Patrones avanzados: `compose`, `pipe`, `memoization`, `pattern matching` simples.
- Modelado de datos con listas y s-expressions en Clojure.
- Ejemplos prácticos de `fold`/`reduce`, `unfold`, `map`, `filter` y `flatmap`.
- Uso práctico en TypeScript: validación de formularios, saneamiento de entradas, construcción de middleware/handlers y pipelines de transformación para APIs o UI.
- Diseño de pequeñas DSLs en Clojure usando funciones de orden superior.
- Traducción de conceptos a TypeScript para comparar estilos sin profundizar en concurrencia.

### No incluye

- Abordar concurrency, `core.async`, `STM` ni modelos de efectos asíncronos.
- Entrar en teoría categórica o construcción de compiladores.
- Cubrir todas las bibliotecas FP de JavaScript/TypeScript.
- Investigar frameworks de concurrencia o canales en Clojure.

## 4. Estructura de la clase (120 minutos)

### Bloque 1 — Funciones de orden superior y composición (35 min)

- Repaso rápido de `first-class functions`.
- Introducción a `map`, `filter`, `reduce` y `fold` en Clojure.
- Ejemplo guiado: pipeline con listas y transformación de datos en Clojure.
- Traducción a TypeScript: `compose`, `pipe`, y funciones puras.

### Bloque 2 — Aplicación parcial y currying (35 min)

- Concepto de función parcial y función curried.
- Ejemplos en Clojure con `lambda` y funciones de orden superior.
- Ejemplos en TypeScript con funciones generadoras de `handler`, validación de formularios y configuración de middleware.
- Actividad corta: construir un conjunto de funciones configurables con `partial` y `curry`, y aplicar esos patrones a una validación de formulario o pipeline de transformación de datos en una app web.

### Bloque 3 — Recursión de cola y patrones avanzados (30 min)

- Definición y ventaja de la recursión de cola.
- Ejemplo de función recursiva de cola en Clojure para recorridos y agregaciones.
- Transformar bucles imperativos en funciones recursivas de cola.
- Patrón `memoization` y `lazy sequences` simples en Clojure/TypeScript.

### Bloque 4 — Taller de aplicación y reflexión (20 min)

- Taller práctico: resolver un problema con Clojure usando `higher-order functions` y recursión de cola.
- Comparar la solución con una implementación en TypeScript.
- Cierre con preguntas clave y recomendaciones para aplicar estos patrones en el proyecto.

## 5. Actividades y artefactos

### Actividad 1 — Currying y aplicación parcial

- Construir funciones de validación y transformación de datos con `curry`.
- Crear funciones especializadas a partir de una definición genérica.
- Ejemplo: `make-validator`, `map-with`, `filter-by`.
- Aplicar el mismo patrón a un pipeline de procesamiento de solicitudes, validación de formularios o composición de middleware en TypeScript.

### Actividad 2 — Recursión de cola en Clojure

- Implementar `sum-tail`, `flatten-tail`, y `walk-list-tail`.
- Comparar con la versión imperativa y analizar claridad.
- Discutir cuándo la recursión de cola mejora el diseño funcional.

### Actividad 3 — Proyecto de clase

- Resolver un mini-problema de análisis de secuencias con funciones compuestas.
- En Clojure: usar funciones de orden superior para transformar listas de datos.
- En TypeScript: aplicar el mismo patrón a un caso web real, como transformar datos de formulario/API, encadenar validaciones y construir un pipeline de respuesta.

## 6. Recursos clave

- Ejemplos de Clojure centrados en listas, `lambda`, `let`, `defn`, `cond`.
- Fragmentos comparativos en TypeScript para `curry`, `compose`, `partial`.
- Notas sobre recursión de cola y cómo traducir ideas a JavaScript/TypeScript.
- Referencias internas: Tema 03 (fundamentos FP) y Tema 05 (mónadas en TS) para continuidad.

## 7. Indicadores de éxito

- El estudiante puede crear una función de orden superior que devuelva otra función.
- Puede explicar la diferencia entre aplicación parcial y currying.
- Puede implementar una función recursiva de cola en Clojure y justificar su uso.
- Puede comparar soluciones en Clojure y TypeScript sin mencionar concurrency.

## 8. Riesgos y mitigaciones

- Riesgo: los alumnos se distraen con sintaxis de Clojure. Mitigación: usar ejemplos cortos y directos, centrados en listas y funciones.
- Riesgo: confundir currying con composición. Mitigación: presentar ambos patrones con ejemplos paralelos claros.
- Riesgo: intentar abarcar demasiados temas avanzados. Mitigación: priorizar tres núcleos: HOF, partial/curry y tail recursion.

## 9. Notas para la producción posterior

- `minuta.md` debe reflejar los bloques como retos concretos y actividades de codificación.
- `filminas.md` debe mostrar código Clojure claro y compararlo con TypeScript en conceptos.
- `tp.md` debe pedir una implementación funcional y una breve justificación de la elección de patrones.
- `score-pedagogico.md` debe evaluar comprensión de currying, aplicación parcial y recursión de cola.

---

> Nota: El diseño ahora prioriza Clojure y patrones de programación funcional avanzados, y elimina la concurrencia para mantener el tema manejable en 120 minutos.
