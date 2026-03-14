# Diseño del Tema 03 — Introducción a Programación Funcional con TypeScript

> ✅ **APROBADO** por Matías Gel — 2026-03-13  
> Estado: Listo para generar minuta, filminas y TP  
> Este documento está congelado hasta que se complete el ciclo de clase.

**Duración total de la clase:** 120 minutos

**Objetivos de aprendizaje**

1. Comprender los principios centrales de la programación funcional: funciones puras, inmutabilidad, recursividad, composición y funciones de orden superior.
2. Relacionar estos principios con prácticas concretas en TypeScript (y contrastar con paradigmas imperativos/OO vistos previamente).
3. Identificar ventajas y limitaciones de la programación funcional en aplicaciones reales (p.ej. programación reactiva, manejo de efectos, testabilidad).
4. Introducir conceptos avanzados como evaluación perezosa y mónadas de forma intuitiva, con énfasis en su rol para el manejo de efectos.

---

## Estructura de la clase (120 min)

### 1) Arranque & motivación (10 min)
- Repaso rápido: ¿qué vimos hasta ahora sobre paradigmas (imperativo, OO)?
- Pregunta detonante: ¿por qué a veces la lógica se expresa mejor con funciones en lugar de objetos/estado?
- Mini-caso: transformación de datos (p.ej. filtrar + map + reduce) y por qué la inmutabilidad reduce errores.

### 2) Fundamentos de la Programación Funcional (20 min)
- **Funciones puras**: definición y ejemplos contrastando con funciones con efectos secundarios.
  - Ejemplo TS: función pura vs función que modifica un arreglo global.
- **Inmutabilidad**: por qué importa, cómo lograrla en JS/TS (const, spread, librerías inmutables).
- **Recursión** como sustituto de loops imperativos. Recursión de cola (tail recursion) y limitaciones en JS.

### 3) Funciones de orden superior y clausuras (25 min)
- Definición y ejemplos: `map`, `filter`, `reduce`, `forEach` (JS/TS).
- Construcción de funciones generadoras (factory functions) y uso de clausuras para mantener estado limpio.
- Ejercicio breve (en clase): implementar `filter` y `map` desde cero usando callbacks.

### 4) Composición, aplicación parcial y currificación (20 min)
- ¿Qué es componer funciones? Ejemplo práctico con `compose` / `pipe`.
- Aplicación parcial: `partial` y `bind` vs currificación.
- Ejercicio: construir una tubería de transformación de datos (p.ej. limpiar + validar + formatear) usando composición.

### 5) Manejo de efectos y evaluación perezosa (10 min)
- Problema: efectos secundarios y borde de la pureza funcional.
- Estrategia: separar la lógica pura de las interacciones con el mundo (IO, logs, estado compartido).
- Breve demostración de evaluación perezosa (lazy): ejemplo mínimo con generadores en TS para construir pipelines de datos que no se evalúan hasta ser consumidos.
  - Nota: esta sección es ilustrativa; la profundización queda para el tema 05.

### 6) Introducción a mónadas (15 min)
- Intuición: las mónadas como patrón para encadenar cálculos con contexto (opcionalidad, errores, asíncrono).
- Ejemplo sencillo en TS: `Maybe` / `Option` y `Either`.
- Relación con promesas (Promise como mónada) y con `async/await`.

### 7) Cierre y preguntas (10 min)
- Recapitulación de los conceptos clave.
- Conexión con próximos temas: `04 – Aspectos Avanzados de Programación Funcional` y `05 – Mónadas en TypeScript`.
- Actividad de cierre: qué cambios propondrías en tu forma de programar después de esta clase.

---

## Recursos y referencias (material de consulta)

- **`material/03-Funcional-Intro/Introducción a la Programación Funcional.pdf`** — base conceptual y ejemplos de código.
- **`material/03-Funcional-Intro/351-423.pdf`** — capítulos que abordan funciones puras, inmutabilidad y composición.
- **`material/03-Funcional-Intro/647-702.pdf`** — secciones sobre mónadas y manejo de efectos.
- **Notas clave**:
  - En TS usar `readonly` y métodos inmutables de arreglos.
  - En el ejercicio de composición, preferir pequeños pasos reutilizables.

---

## Actividades propuestas (TPs / ejercicios)

1. **Ejercicio en clase (para hacer en pareja)**: Implementar una mini-librería de transformaciones de arreglos (`map`, `filter`, `reduce`, `compose`) y usarla para resolver un problema de filtrado / formateo. El objetivo es producir una *pipe* de funciones que lea datos, los transforme y devuelva un resultado (ej. limpieza + agregación de un dataset tipo “encuesta”).
2. **TP principal (pipeline funcional)**: Diseñar y entregar un módulo pequeño que:
   - incluya una implementación funcional de `compose/pipe` + `map/filter/reduce`;
   - resuelva un caso real (por ejemplo: procesar respuestas de encuesta, limpiar datos y calcular métricas);
   - incluya tests simples que demuestren que las funciones son puras y el pipeline es determinista.
3. **Lectura recomendada (post-clase)**: capítulo sobre mónadas/efectos (tema 05) y un artículo breve sobre lazy evaluation y generadores en JS/TS.

---

## Link con el plan mínimo

- Este tema cubre los ítems de **“Paradigma funcional”** del plan mínimo, específicamente:
  - Funciones puras, inmutabilidad, recursividad.
  - Funciones de orden superior, clausuras y ámbito léxico.
  - Composición de funciones, aplicación parcial, currificación.
  - Introducción a mónadas y manejo de efectos.

---

## Nota de scope

Este diseño se limita a los tópicos listados arriba. **No se profundiza en programación reactiva (RxJS) ni en teoría categórica**; esos tópicos quedan reservados para el tema 04 y 05.
