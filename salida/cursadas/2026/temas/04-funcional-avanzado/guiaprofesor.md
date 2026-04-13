# Guía del Profesor — Tema 04

## Aspectos Avanzados de Programación Funcional

> **Materia:** Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI
> **Clase:** 04 | **Duración:** 120 minutos

---

## Resumen ejecutivo

Este tema expone patrones avanzados de programación funcional con un enfoque aplicado al desarrollo web. El objetivo central es que los alumnos entiendan cómo la composición y el modelado explícito de errores ayudan a diseñar APIs y validaciones más robustas en TypeScript.

## Objetivos de la sesión

- Mostrar el valor práctico de `filter`, `map`, `reduce` y composición.
- Enseñar cómo `Result` y `Maybe` mejoran la robustez de la validación de formularios.
- Presentar `curry` y `partial` como herramientas para construir middlewares y handlers reutilizables.
- Comparar recursión de cola en Clojure con su equivalencia en TypeScript.

---

## Estructura de la clase

| Bloque | Tiempo | Resultado esperado |
| --- | --- | --- |
| Fundamentos | 35 min | Identificar pipelines y funciones puras en TS/Clojure |
| Abstracciones | 35 min | Diseñar validaciones y modelos de error explícitos |
| Recursión y composición | 30 min | Relacionar recursión de cola con código web reusable |
| Taller y cierre | 20 min | Aplicar conceptos en un caso práctico de formulario |

---

## Puntos clave para el docente

- Mantener el foco en la utilidad web: validación, middleware y pipelines de datos.
- Evitar caer en detalles de sintaxis de Clojure. Usar Clojure como contraste conceptual.
- No presentar la concurrencia como tema principal; usar Clojure como contraste funcional centrado en datos inmutables y recursión de cola.
- Reforzar que el valor está en la intención del código, no en la sintaxis.

---

## Desarrollo por bloque

### Bloque 1 — Fundamentos

- Comenzar con un ejemplo real en TypeScript: cálculo de totales en órdenes.
- Resaltar la diferencia entre mutar un arreglo y devolver nuevos arreglos.
- Usar `filter`/`map`/`reduce` para que los estudiantes vean la legibilidad.
- Pedirles que describan en voz alta qué hace cada paso.

### Bloque 2 — Efectos y errores

- Introducir `Result` con un ejemplo de validación de email.
- Explicar que no se trata de evitar excepciones a toda costa, sino de hacer explícito el flujo de error.
- Mostrar `Maybe` como herramienta para campos opcionales.
- Relacionar con un caso práctico de formulario de registro.

### Bloque 3 — Composición y recursión

- Mostrar `curry` y `partial` con handlers web.
- Construir un `compose` de middlewares que modifican un request.
- Explicar recursión de cola como técnica de control de stack en Clojure.
- Mostrar su equivalente en TS para reforzar la idea.

### Bloque 4 — Taller

- Proponer el ejercicio central: validar un formulario y construir un pipeline de datos.
- Enfatizar el tipo de salida: `Result<FormData, string>`.
- Pedir a los grupos que identifiquen qué funciones pueden ser puras.
- No es necesario terminar el código; lo importante es la estructura del pipeline.

---

## Errores frecuentes a corregir

- Confundir `Result` con `throw` y usar ambos en la misma función.
- Usar `for` mutando arrays en lugar de `filter` y `map`.
- Pensar que `partial` es solo “una forma rara de llamar funciones”; es una forma de preconfigurar pipelines.
- Sobrecomplicar la expresión Clojure. Si la clase se trabó en la sintaxis, volver al equivalente TS.

---

## Sugerencias de facilidades

- Si el grupo avanza rápido, pedirles que refactoren el pipeline de validación para devolver mensajes acumulados.
- Si el grupo se frena, simplificar el ejemplo a dos campos (`email` + `nombre`) y preguntarle al docente cómo se vería el flujo de datos.
- Usar la guía de estudio como material de referencia inmediata para los alumnos que quieran profundizar.

---

## Material de apoyo

- `diseno.md`: alcance y restricciones del tema.
- `minuta.md`: guion de clase.
- `filminas.md`: plan de presentación.
- `guia-estudio.md`: material de lectura y ejercicios para el alumno.

---

## Nota final

El propósito de este rediseño es que el tema 04 deje de ser un ejercicio académico aislado y se convierta en un ejemplo práctico útil para el desarrollo web con TypeScript. Mantener el foco en la aplicación práctica ayudará a que los estudiantes internalicen el valor real de la programación funcional.
