# Diseño de Clase — Tema 13B: Módulos, Interfaces y Genéricos

> **Estado:** 🟡 EN PRODUCCION (minuta.md + filminas.md generadas el 2026-06-28)
> **Diseñador:** Dr. Roberto ✍️ (class-writer) — corrección de drift
> **Fecha:** 2026-06-28
> **Módulo:** X | **Semana:** 13 | **Clase:** 1 de 1
> **Duración:** 120 minutos (constraint absoluto de generación)

---

## ⚠️ Drift detectado

El tema se llama **"Módulos, Interfaces y Genéricos"** en `topic.yaml` (Clase 13B), pero el `clase_dada.txt` (607 líneas) contiene la clase sobre **"Subprogramas: del contrato a la ejecución"** — subprogramas como abstracción de acción, contrato, perfil/protocolo, parámetros formales/reales, modos de pasaje (in/out/inout), mecanismos (valor, referencia, valor-resultado, nombre), pass-by-sharing, callbacks, sobrecarga, dispatch estático/dinámico, genéricos, activation records, dynamic/static link y async.

Existe un tema "gemelo" `13-subprogramas-parametros-sobrecarga` (Clase 13A) cuyo `clase_dada.txt` trata sobre TAD/módulos/interfaces/genéricos — lo inverso. Pareciera que los dos `clase_dada.txt` están **intercambiados** entre las carpetas 13.

**Decisión operativa:** se mantiene el nombre del tema de `topic.yaml` para consistencia con el sistema, pero `filminas.md` y `minuta.md` son fieles al `clase_dada.txt` (subprogramas). Se sugiere al docente revisar si los `clase_dada.txt` de las dos carpetas 13 están intercambiados, o si el título del tema debe renombrarse a "Subprogramas: del contrato a la ejecución".

---

## Datos del Tema

| Campo | Valor |
|-------|-------|
| Número | 13 (Clase 13B) |
| Nombre (topic.yaml) | Módulos, Interfaces y Genéricos |
| Contenido real | Subprogramas: del contrato a la ejecución |
| Módulo curricular | X — Abstracción y Modularidad |
| Duración | 120 minutos |
| Lenguaje principal | TypeScript |
| Lenguajes de contraste | Go, Rust, Swift, Kotlin |
| Libro principal | Sebesta 2019, Cap. 9 (Subprograms) y Cap. 10 (Implementing Subprograms) |
| Bibliografía complementaria | Gabbrielli & Martini 2023, Cap. 7 (Procedures/Functions) |
| Nivel v3 | 2 — Estándar |

---

## Alcance Curricular Obligatorio

Este tema cubre el contenido efectivamente dictado en `clase_dada.txt`:

1. El subprograma como abstracción de acción: contrato, definición vs. llamada.
2. Procedimiento vs. función: intención, resultado, composición.
3. Perfil y protocolo: verificación estática de llamadas.
4. Modos de pasaje: in, out, inout — dirección del flujo de información.
5. Intención y permiso mínimo: consultar, modificar, consumir, producir.
6. Efectos observables en el contrato moderno: retorno, mutación, falla, suspensión, cancelación.
7. Mecanismos de pasaje: valor, resultado, valor-resultado, referencia, nombre.
8. Pass-by-value en Go, aliasing mutable en Rust, inout en Swift.
9. Pass-by-sharing: separar variable y objeto; mutabilidad compartida.
10. Callbacks como parte del contrato: síncrono, suspendible, escapante.
11. Herramientas de variación: sobrecarga, unión sellada, genérico/trait, interfaz dinámica.
12. Selección de implementación: compilación vs. ejecución.
13. Sobrecarga en Kotlin; impl Trait vs. dyn Trait en Rust.
14. Abstracción genérica: especialización, implementación compartida, preservación selectiva.
15. Activation record: componentes, calling sequence, call y return.
16. async como extensión del modelo de ejecución.
17. Dynamic link vs. static link.
18. Síntesis: las decisiones de diseño están conectadas.

---

## Fuera de Scope

Esto está fuera de scope del contenido real de la clase:

- Módulos, interfaces y genéricos como tema central (el título del tema no coincide con el contenido — ver "⚠️ Drift detectado").
- TADs (Tipo Abstracto de Datos) como desarrollo completo.
- Sistemas de tipos avanzados (higher-kinded types, dependent types).
- Optimización de llamadas a nivel de compilador (inlining, tail-call optimization) como tema propio.
- Corrutinas y concurrencia estructurada como desarrollo completo (aparece async como extensión del modelo, no como eje).
- Gestión de memoria más allá del stack de activación (heap, garbage collection).

Justificación: la clase dura 120 minutos y el `clase_dada.txt` define el contrato institucional real: subprogramas desde el contrato visible hasta el mecanismo de ejecución.

---

## Objetivos de Aprendizaje

Al finalizar la clase, el estudiante podrá:

1. Explicar un subprograma como abstracción de acción que se razona por contrato, no por instrucciones.
2. Distinguir definición y llamada como roles distintos que forman un contrato.
3. Diferenciar procedimiento y función por intención, resultado y composición.
4. Usar perfil y protocolo para verificar llamadas sin leer el cuerpo.
5. Identificar modos de pasaje (in, out, inout) como dirección del flujo de información.
6. Relacionar intención (consultar, modificar, consumir, producir) con permiso mínimo.
7. Reconocer efectos observables (mutación, falla, suspensión, cancelación) en el contrato moderno.
8. Comparar mecanismos de pasaje (valor, resultado, valor-resultado, referencia, nombre) por ventajas y riesgos.
9. Explicar pass-by-value en Go, aliasing mutable restringido en Rust e inout en Swift.
10. Distinguir pass-by-sharing de pass-by-reference: separar variable y objeto.
11. Explicar un callback como parte del contrato del llamador, incluyendo síncrono, suspendible y escapante.
12. Comparar sobrecarga, unión sellada, genérico/trait e interfaz dinámica como herramientas de variación.
13. Diferenciar dispatch estático (impl Trait) y dinámico (dyn Trait) en Rust.
14. Explicar los costos de la abstracción genérica: especialización, implementación compartida, preservación selectiva.
15. Describir los componentes de un activation record y la secuencia call/return.
16. Explicar async como extensión del modelo de ejecución con máquina de estados reanudable.
17. Distinguir dynamic link (¿quién me llamó?) y static link (¿dónde busco variables no locales?).
18. Sintetizar que las decisiones de diseño del subprograma están conectadas: del contrato visible al mecanismo de ejecución.

---

## Bibliografía Principal

- Robert W. Sebesta, *Concepts of Programming Languages*, Pearson 2019.
  - Cap. 9: Subprograms — §9.2 Fundamentals, §9.5 Parameter-Passing Methods, §9.6 Parameters That Are Subprograms, §9.9 Overloaded Subprograms, §9.10 Generic Subprograms.
  - Cap. 10: Implementing Subprograms — §10.1 General Semantics of Calls and Returns, §10.2 Simple Subprograms, §10.4 Nested Subprograms (static link, dynamic link, ARI).
- Maurizio Gabbrielli & Simone Martini, *Programming Languages: Principles and Paradigms*, Springer 2023.
  - Cap. 7 (pp. 106-135): function vs. procedure, activation record fields, dynamic chain pointer / dynamic link.
  - Cap. 7 (pp. 136-282): parameter passing modes (by value, by reference, read-only), parameter passing discipline, cost of modes.
- Kenneth C. Louden & Kenneth A. Lambert, *Programming Languages: Principles and Practices*, Course Technology 2012. Apoyo terminológico sobre subprogramas y pasaje de parámetros.

Fuentes actuales para contrastes de lenguaje:

- Go Documentation: function parameters, pass-by-value semantics.
- Rust Documentation: ownership, borrowing, impl Trait vs. dyn Trait.
- Swift Language Guide: inout parameters, @escaping closures.
- Kotlin Documentation: function types, suspend modifiers, overloading.

---

## Estrategia Pedagógica

La clase sigue el hilo del `clase_dada.txt`: del contrato visible al mecanismo de ejecución. La progresión es deliberada:

1. **Contrato** (Bloque A): el subprograma como abstracción de acción. Se introduce la función `distancia` y la tabla definición-vs-llamada para mostrar que el cliente razona con información visible, no con el cuerpo.

2. **Parámetros** (Bloque B): la dirección del flujo (modos) antes que el mecanismo. Se presenta la tabla intención-permiso y la tabla de efectos observables para mostrar que el contrato moderno incluye más que el tipo de retorno.

3. **Lenguajes reales** (Bloque C): Go, Rust y Swift muestran tres decisiones distintas sobre pasaje de parámetros. No se enseña cada lenguaje: se usa cada uno para iluminar una decisión de diseño.

4. **Compartir** (Bloque D): pass-by-sharing separa variable y objeto. El ejemplo `usuario.roles.push` muestra que la mutación compartida sobrevive pero la reasignación local no.

5. **Callbacks** (Bloque E): un callback es parte del contrato del llamador. Kotlin distingue síncrono de suspendible; Swift marca @escaping para hacer visible la diferencia.

6. **Variación** (Bloque F): sobrecarga, trait, genérico e interfaz dinámica expresan variación distinta. Kotlin muestra sobrecarga entre cuerpos distintos; Rust separa impl Trait de dyn Trait.

7. **Genéricos** (Bloque G): la abstracción genérica tiene costos — especialización, implementación compartida, preservación selectiva.

8. **Ejecución** (Bloque H): el activation record materializa una llamada. Call y return administran el stack. async extiende el modelo con una máquina de estados. Dynamic link y static link responden preguntas diferentes.

9. **Cierre** (Bloque I): las decisiones de diseño están conectadas — del contrato visible al mecanismo de ejecución.

TypeScript es el lenguaje ancla. Go, Rust, Swift y Kotlin aparecen como contrastes para iluminar decisiones, no como tres clases paralelas.

---

## Plan de Filminas

| F-# | Título | Tipo | Duración |
|-----|--------|------|----------|
| F-00 | Subprogramas: del contrato a la ejecución | portada | — |
| F-01 | Un subprograma abstrae una acción | concepto-abstracto | 5 min |
| F-02 | Definición y llamada forman un contrato | tabla-mixta | 7 min |
| F-03 | Procedimiento vs. función | tabla-comparativa | 4 min |
| F-04 | Perfil y protocolo: verificar sin leer el cuerpo | concepto-mixto | 4 min |
| F-05 | La dirección del flujo: in, out, inout | concepto-abstracto | 4 min |
| F-06 | Intención y permiso mínimo | tabla | 5 min |
| F-07 | Efectos observables en el contrato moderno | tabla | 4 min |
| F-08 | Mecanismos de pasaje: tradeoffs | tabla-comparativa | 5 min |
| F-09 | Go — aislamiento de pass-by-value | concepto-mixto | 6 min |
| F-10 | Rust — aliasing mutable restringido | concepto-mixto | 6 min |
| F-11 | Swift — mutación explícita con inout | concepto-mixto | 6 min |
| F-12 | Pass-by-sharing: separar variable y objeto | concepto-mixto | 4 min |
| F-13 | Una matriz grande: copia vs. aliasing | tabla-comparativa | 4 min |
| F-14 | Un callback es parte del contrato | concepto-mixto | 5 min |
| F-15 | Síncrono, suspendible y escapante | concepto-mixto | 7 min |
| F-16 | Herramientas para expresar variación | tabla-comparativa | 5 min |
| F-17 | Kotlin — sobrecarga entre cuerpos distintos | concepto-mixto | 4 min |
| F-18 | Rust — impl Trait vs. dyn Trait | concepto-mixto | 5 min |
| F-19 | Abstracción genérica: costos de implementación | tabla-mixta | 6 min |
| F-20 | El activation record materializa una llamada | tabla | 5 min |
| F-21 | Call y return: administrar el stack | tabla-mixta | 5 min |
| F-22 | async extiende el modelo de ejecución | concepto-mixto | 5 min |
| F-23 | Dynamic link vs. static link | concepto-abstracto | 4 min |
| F-24 | Las decisiones de diseño están conectadas | cierre | 5 min |

**Total estimado:** 120 minutos.

---

## Distribución por Bloques

| Bloque | Filminas | Tema | Tiempo |
|--------|----------|------|--------|
| A | F-00 a F-04 | El subprograma como abstracción de acción | 20 min |
| B | F-05 a F-08 | Parámetros: modos, permisos y efectos | 18 min |
| C | F-09 a F-11 | Tres lenguajes, tres decisiones de pasaje | 18 min |
| D | F-12 a F-13 | Compartir objetos: copia vs. aliasing | 8 min |
| E | F-14 a F-15 | Callbacks: contrato, suspensión y escape | 12 min |
| F | F-16 a F-18 | Variación: sobrecarga, dispatch y trait | 14 min |
| G | F-19 | Abstracción genérica y sus costos | 6 min |
| H | F-20 a F-23 | Ejecución: activation records y async | 19 min |
| I | F-24 | Cierre: decisiones conectadas | 5 min |

La suma pedagógica es 120 min exactos. En generación de clase se debe priorizar F-02 (contrato), F-08 (mecanismos), F-10 (Rust), F-15 (callbacks) y F-20 (activation record) como filminas de mayor densidad conceptual.

---

## Secuencia Didáctica

### Bloque A — El subprograma como abstracción de acción

Objetivo: que el alumno razona por contrato, no por instrucciones.

Actividades:
- Introducir el subprograma como abstracción de acción con punto de entrada único y retorno de control.
- Mostrar la función `distancia` y la tabla definición-vs-llamada para distinguir roles.
- Contrastar procedimiento y función por intención, resultado y composición.
- Presentar perfil y protocolo como herramientas de verificación estática.

### Bloque B — Parámetros: modos, permisos y efectos

Objetivo: que el alumno entienda que la dirección del flujo precede al mecanismo.

Orden:
1. Modos in, out, inout como dirección del flujo de información.
2. Tabla intención-permiso: consultar, modificar, consumir, producir.
3. Efectos observables: retorno, mutación, falla, suspensión, cancelación.
4. Mecanismos: valor, resultado, valor-resultado, referencia, nombre — con ventajas y riesgos.

### Bloque C — Tres lenguajes, tres decisiones

Objetivo: iluminar decisiones de diseño de pasaje con lenguajes reales.

- Go: pass-by-value aísla al llamador; modificar el formal no modifica el argumento.
- Rust: &mut exige acceso exclusivo; el borrow checker rechaza aliasing mutable.
- Swift: inout distingue entrada mutable de retorno; & en la llamada hace visible la mutación.

### Bloque D — Compartir objetos

Objetivo: distinguir pass-by-sharing de pass-by-reference.

- Pass-by-sharing: la mutación compartida sobrevive; la reasignación local no.
- Una matriz grande muestra el compromiso entre copia y aliasing.

### Bloque E — Callbacks

Objetivo: tratar el callback como parte del contrato del llamador.

- Un callback es un subprograma recibido como parámetro; el contrato debe aclarar frecuencia, fallo y retención.
- Kotlin distingue callback síncrono de suspendible con `suspend`.
- Swift marca @escaping para hacer visible que un callback puede ejecutarse después.

### Bloque F — Variación y dispatch

Objetivo: comparar herramientas de variación y momentos de selección.

- Tabla de herramientas: sobrecarga, unión sellada, genérico/trait, interfaz dinámica.
- Kotlin: sobrecarga resuelve entre cuerpos distintos en compilación.
- Rust: impl Trait (estático, especialización) vs. dyn Trait (dinámico, indirección).

### Bloque G — Abstracción genérica

Objetivo: mostrar que la abstracción genérica tiene costos de implementación.

- Especialización por tipo, implementación compartida, preservación selectiva de tipos.
- Código `identidad<T>` y `esTipo<T>` en TypeScript.

### Bloque H — Ejecución

Objetivo: bajar el contrato al mecanismo de ejecución.

- Componentes del activation record: parámetros, locales, dirección de retorno, dynamic link, valor de retorno, static link.
- Calling sequence: preparar, crear, transferir, ejecutar, retornar, liberar.
- Ejemplo `sumar(2, 3)` y su AR concreto.
- async: máquina de estados reanudable; conserva estado sin mantener el stack síncrono.
- Dynamic link (¿quién me llamó?) vs. static link (¿dónde busco variables no locales?).

### Bloque I — Cierre

Objetivo: sintetizar que las decisiones de diseño están conectadas.

Tabla de seis preguntas: ¿qué acepta y retorna?, ¿cómo circulan datos?, ¿qué efectos produce?, ¿puede retener callbacks?, ¿cómo selecciona implementación?, ¿cómo se ejecuta? — del contrato visible al mecanismo de ejecución.

---

## Criterios de Aprobación del Diseño

El diseño queda aprobado si:

- Es fiel al `clase_dada.txt` (subprogramas: del contrato a la ejecución).
- Documenta el drift título-vs-contenido de forma visible.
- Mantiene 120 minutos como constraint real.
- Usa TypeScript como lenguaje principal.
- Usa Go, Rust, Swift y Kotlin como contrastes, sin convertirlos en clases paralelas.
- No reexplica módulos/interfaces/genéricos como tema central (no están en el `clase_dada.txt`).
- Evita scope creep hacia concurrencia completa, GC o optimización de compilador.

---

## Plan de Generación Posterior

Si el docente aprueba este diseño:

1. `filminas.md` y `minuta.md` ya generadas (2026-06-28) — fieles al `clase_dada.txt`.
2. El docente debe revisar el drift título-vs-contenido y decidir: renombrar el tema o intercambiar los `clase_dada.txt` de las carpetas 13.
3. Si se renombra el tema a "Subprogramas: del contrato a la ejecución", actualizar `topic.yaml` y regenerar `diseno.md` sin la sección de drift.
4. Si se intercambian los `clase_dada.txt`, regenerar filminas y minuta de ambas carpetas 13.
5. No incluir referencias bibliográficas inline dentro de las filminas; la trazabilidad queda en `minuta.md`.
