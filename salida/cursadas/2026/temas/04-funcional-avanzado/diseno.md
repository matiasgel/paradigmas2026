# Diseño del Tema 04 — Aspectos Avanzados de Programación Funcional

> Duración de clase: 120 minutos
> Enfoque: comparación aplicada entre TypeScript y Clojure, con atención a patrones avanzados, abstracciones funcionales y manejo de efectos.

## 1. Objetivos de aprendizaje

1. Comprender cómo se expresan los patrones funcionales avanzados en TypeScript y Clojure.
2. Analizar diferencias clave entre un lenguaje con tipado estructural estático y uno dinámico homoicónico.
3. Aplicar transformaciones de datos usando composabilidad, funciones puras, transducers y colecciones inmutables.
4. Diseñar una solución funcional que combine `higher-order functions`, `algebraic data types` y manejo de errores con `Result` / `Either`.
5. Identificar cuándo usar abstracciones de concurrencia y efectos en Clojure (`core.async`, `agents`, `STM`) versus promesas/async en TypeScript.

## 2. Prerrequisitos

- Conocimiento de programación funcional básica en TypeScript (Tema 03).
- Comprensión de inmutabilidad, funciones puras, `map`, `filter`, `reduce`.
- Familiaridad con sintaxis básica de TypeScript y conceptos de Clojure elementales.
- Entender tipos de unión y alias en TypeScript.

## 3. Alcance del tema

### Incluye

- Composición y pipes de funciones.
- Patrones avanzados de manipulación de colecciones: transducers en Clojure y equivalente en TypeScript.
- Algebraic data types en TypeScript y estructuras de datos funcionales en Clojure.
- Manejo de errores funcional: `Result` / `Either`, `Option` / `Maybe`.
- Inmutabilidad y estados definidos por datos.
- Abstracciones de concurrencia y efectos: `core.async`, `agents`, `STM`, y comparativa con `Promise` / `async-await` en TypeScript.
- Diseño de APIs funcionales en TypeScript con tipos genéricos y funciones de orden superior.
- Uso de macros de Clojure como herramienta de metaprogramación de dominio específico.

### No incluye

- Implementar un compilador funcional completo.
- Profundizar en teoría categórica formal ni demostraciones matemáticas de monadas.
- Cubrir todas las bibliotecas FP de JavaScript/TypeScript (sólo ejemplos representativos).
- Introducir Haskell como lenguaje principal; se usa sólo como contraste conceptual si es necesario.

## 4. Estructura de la clase (120 minutos)

### Bloque 1 — Fundamentos avanzados (35 min)

- Revisión rápida de funciones puras y valores inmutables.
- Composición de funciones y pipelines en TypeScript.
- Introducción al modelo de colecciones inmutables en Clojure.
- Ejemplo guiado: transformación de un flujo de datos con `map`/`filter`/`reduce` en TS y Clojure.

### Bloque 2 — Abstracciones y efectos (35 min)

- Algebraic data types en TypeScript: `type`, `union`, `interface` y `readonly`.
- Patrón `Result` / `Either` para manejo de errores sin excepciones.
- En Clojure: secuencias perezosas, transducers y `defrecord`.
- Ejercicio corto: modelar una operación de validación de formulario con resultados funcionales.

### Bloque 3 — Concurrencia y metaprogramación (30 min)

- Clojure `core.async` y canales: pipeline de datos y separación de responsabilidades.
- Actores leves vs STM: cuándo elegir cada modelo.
- TypeScript: `Promise`, `async/await`, `Observable` conceptual (no obligatorio), y efectos asíncronos puros.
- Ejemplo comparativo: consumir datos y aplicar transformaciones continuas en ambos lenguajes.

### Bloque 4 — Práctica guiada y reflexión (20 min)

- Taller en parejas: implementar en TypeScript y en Clojure el mismo problema funcional.
- Verificación cruzada: comparar soluciones, detectar similitudes y diferencias conceptuales.
- Cierre con preguntas clave y síntesis de diferencias entre los dos enfoques.

## 5. Actividades y artefactos

### Actividad 1 — Transformación de datos reales

- Input: lista de registros con valores de clientes, estados y resultados.
- Objetivo: aplicar filtro, mapeo y agregación funcional.
- Salida: función composable que produce una vista resumida.
- Tipo: discusión guiada + codificación en TypeScript.

### Actividad 2 — Manejo funcional de errores

- Construir una estructura `Result<T, E>` en TypeScript.
- En Clojure, usar `either`, `try` controlado y secuencias perezosas para procesar entradas.
- Validar entradas y encadenar operaciones sin romper la composición.

### Actividad 3 — Comparar modelos de concurrencia

- Pequeño caso de uso: lectura, transformación y publicación de eventos.
- En Clojure, bosquejar un pipeline con canales `core.async`.
- En TypeScript, diseñar la misma lógica con `Promise` y `async/await`.
- Discusión: cuándo la concurrencia funcional amplifica la claridad y cuándo agrega complejidad.

## 6. Recursos clave

- Código de ejemplo en TypeScript con tipos genéricos y funciones puras.
- Notebooks/Clojure REPL para experimentar con `transduce`, `lazy-seq`, y `core.async`.
- Fragmentos comparativos de Clojure y TypeScript para los patrones centrales.
- Referencias internas: Tema 03 (fundamentos FP) y Tema 05 (mónadas en TS).

## 7. Indicadores de éxito

- El estudiante puede explicar en voz alta una tubería de datos funcional y su equivalencia en Clojure y TypeScript.
- Puede identificar cuándo un error debe manejarse con un tipo funcional en vez de excepciones.
- Puede distinguir un modelo de concurrencia basado en canales de uno basado en promesas.
- Entiende por qué la inmutabilidad y las abstracciones puras son útiles en ambos lenguajes.

## 8. Riesgos y mitigaciones

- Riesgo: los estudiantes se enredan en la sintaxis de Clojure. Mitigación: usar ejemplos cortos y centrados en datos, no en macros complejas.
- Riesgo: intentar cubrir demasiadas bibliotecas FP. Mitigación: priorizar patrones nativos y conceptos antes que librerías externas.
- Riesgo: confundir abstracción con complejidad. Mitigación: mantener los ejemplos alineados con un mismo dominio simple.

## 9. Notas para la producción posterior

- `minuta.md` debe traducir los bloques en actividades de clase concretas y tiempos de ejecución.
- `filminas.md` debe incluir diagramas de tuberías de datos, comparativas lado a lado y código compacto.
- `tp.md` debe solicitar una implementación funcional y una reflexión sobre la elección de modelo de efectos.
- `score-pedagogico.md` debe evaluar comprensión de abstracciones, no sólo sintaxis.

---

> Nota: este diseño se orienta a que el tema no pierda foco en los patrones avanzados, y evita extenderse hacia teoría categórica o implementación de compiladores. Eso está fuera de scope del Tema 04.
