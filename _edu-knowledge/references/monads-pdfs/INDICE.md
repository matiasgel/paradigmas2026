# Índice de Referencias — Mónadas en TypeScript, Clojure y Programación Funcional

> Recopilación académica para el tema de **Funcional Avanzado** de Paradigmas y Lenguajes de Programación 2026.
> Artículos descargados: 2026-04-09

---

## Papers Fundacionales

| # | Archivo | Referencia | Relevancia |
|---|---------|-----------|------------|
| 1 | `moggi-1991-notions-of-computation-and-monads.pdf` | Moggi, E. (1991). *Notions of Computation and Monads*. Information and Computation, 93(1), 55–92. | **Fundacional** — Define formalmente las mónadas como estructura para modelar computaciones con efectos. Base teórica de todas las implementaciones posteriores. |
| 2 | `wadler-1995-monads-for-functional-programming.pdf` | Wadler, P. (1995). *Monads for Functional Programming*. In J. Jeuring & E. Meijer (Eds.), Advanced Functional Programming, LNCS 925, Springer. | **Fundacional** — Introduce las mónadas a programadores funcionales con 3 ejemplos: excepciones, estado y salida. Paper clásico para docencia. |

## Mónadas en TypeScript / Lenguajes Imperativos

| # | Archivo | Referencia | Relevancia |
|---|---------|-----------|------------|
| 3 | `anderlind-asberg-2023-monadic-programming-imperative-languages.pdf` | Anderlind, J. & Åsberg, M. (2023). *Monadic Programming in Imperative Languages*. Master's Thesis, Chalmers University of Technology. | **Directamente relevante** — Implementa mónadas (Maybe, Either, IO, State) en lenguajes imperativos incluyendo JavaScript/TypeScript. Compara con Haskell. |
| 4 | `thiemann-2023-intrinsically-typed-sessions-callbacks.pdf` | Thiemann, P. (2023). *Intrinsically Typed Sessions with Callbacks (Functional Pearl)*. Proc. ACM Program. Lang. (ICFP). arXiv:2303.01278. | **TypeScript** — Implementa session types usando reader monad y monad transformer en TypeScript. Ejemplo de mónadas en producción. |
| 5 | `pennanen-2024-pragmatic-functional-programming-evaluation.pdf` | Pennanen, A. (2024). *Pragmaattisen funktionaalisen ohjelmoinnin arviointi* [Evaluación de Programación Funcional Pragmática]. Thesis, Theseus (Finlandia). | **TypeScript + fp-ts** — Evalúa programación funcional pragmática con TypeScript, incluyendo fp-ts y sus abstracciones monádicas (Option, Either, TaskEither). |

## Sistemas de Efectos y Mónadas (Multi-lenguaje incl. Clojure)

| # | Archivo | Referencia | Relevancia |
|---|---------|-----------|------------|
| 6 | `paju-jarvi-2023-modern-landscape-managing-effects.pdf` | Paju, J. & Järvi, J. (2023). *The Modern Landscape of Managing Effects for the Working Programmer*. Master's Thesis, University of Turku. | **Mónadas + Effect Systems** — Compara mónadas, monad transformers, algebraic effects y effect handlers. Cubre ZIO monad, Either monad. Menciona TypeScript. |
| 7 | `lindley-wu-kiselyov-plotkin-2019-algebraic-effects-handlers.pdf` | Lindley, S., Wu, N., Kiselyov, O. & Plotkin, G. (2019). *Programming and Reasoning with Algebraic Effects and Effect Handlers*. Shonan Meeting Report No. 146. | **Clojure + Efectos Algebraicos** — Workshop report que menciona implementaciones en Clojure. Presenta free monads y su relación con effect handlers. |
| 8 | `muckenschnabel-2024-combining-effects-dependent-types.pdf` | Mückenschnabel, M. (2024). *Combining Effects with Dependent Types*. Master's Thesis, Charles University, Prague. | **Composición de mónadas** — Analiza el problema de composición de mónadas y alternativas (algebraic effects). Menciona Clojure transient data structures. |

## Free Monads y Álgebra Abstracta

| # | Archivo | Referencia | Relevancia |
|---|---------|-----------|------------|
| 9 | `vandenberg-schrijvers-dedecker-2023-functional-modeling-algebra.pdf` | van den Berg, B., Schrijvers, T. & Dedecker, P. (2023). *Applications of Functional Modeling with Abstract Algebra: Higher-Order Effects and Automatic Differentiation*. KU Leuven. | **Free monads + Clojure/Elm** — Usa recursion schemes para interpretar free monads. Menciona Clojure y Elm en contexto de web development funcional. |
| 10 | `landon-2024-survey-practical-haskell-monads.pdf` | Landon, P. (2024). *A Survey of Practical Haskell: Parsing, Interpreting, and Testing*. Honors Thesis, Seattle Pacific University. | **Monads for effectful programming** — Cubre IO monad, State monad, parsing monádico. Útil como referencia comparativa Haskell vs TS/Clojure. |

---

## Libros Relevantes (no descargados — con copyright)

| Referencia | Contenido relevante |
|-----------|---------------------|
| Martin, R.C. (2023). *Functional Design: Principles, Patterns, and Practices*. Pearson. | Capítulos sobre mónadas y monoides **en Clojure**. Uncle Bob explica FP usando Clojure. |
| Kereki, F. (2023). *Mastering JavaScript Functional Programming*, 3rd ed. Packt. | Capítulos sobre functors, monads y containers **en JavaScript/TypeScript**. |
| Jansen, R.H. (2019). *Hands-On Functional Programming with TypeScript*. Packt. | Functors y monads **en TypeScript**. Algebraic data types. |
| Riscutia, V. (2019). *Programming with Types: Examples in TypeScript*. Manning. | Higher-kinded types, functors y monads **en TypeScript**. |
| Granin, A. (2024). *Functional Design and Architecture: Examples in Haskell*. Manning. | Free monads, STM, efecto monádico. Menciona **Clojure**. |
| Widman, J. (2022). *Learning Functional Programming*. O'Reilly. | Functors, monads, Cats library. Perspectiva multi-lenguaje incluyendo **Clojure**. |

---

## Notas de Uso Pedagógico

- **Para introducir mónadas**: arrancar con Wadler (1995) por claridad expositiva → luego Moggi (1991) para formalismo.
- **Para implementar en TS**: Anderlind & Åsberg (2023) tiene código directo → Pennanen (2024) cubre fp-ts en producción.
- **Para Clojure**: la biblioteca principal es [cats (funcool/cats)](https://github.com/funcool/cats), que implementa mónadas como protocolo Clojure. No hay papers académicos específicos, pero Martin (2023) lo cubre en capítulos dedicados.
- **Para debatir alternativas a mónadas**: Paju & Järvi (2023) compara monads vs algebraic effects → Lindley et al. (2019) profundiza.
