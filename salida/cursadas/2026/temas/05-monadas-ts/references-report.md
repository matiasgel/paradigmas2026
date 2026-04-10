# Reporte de Validación de Referencias — Loop 3
## Tema 05: Mónadas en TypeScript

> **Agente:** 🔬 reference-validator  
> **Fecha de validación:** 2026-04-10  
> **Materia:** Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI — IF020  
> **Tema:** 05 — Mónadas en TypeScript  
> **Fuentes consultadas por referencia:** CrossRef, Semantic Scholar (vía búsqueda indirecta), Chalmers ODR, URLs directas con fetch

---

## Tabla de Referencias Verificadas

| ID | Documento | Referencia original | Estado | Observación | Corrección sugerida |
|----|-----------|---------------------|--------|-------------|---------------------|
| REF-01 | guia-estudio.md, guiaprofesor.md | Wadler, P. (1995). *Monads for Functional Programming*. [Disponible en `_edu-knowledge/references/monads-pdfs/`] | ✅ VERIFICADA | Archivo PDF local confirmado: `wadler-1995-monads-for-functional-programming.pdf`. Año 1995 correcto: publicado en J. Jeuring & E. Meijer (Eds.), *Advanced Functional Programming*, LNCS 925, Springer. Autor y título exactos. Paper canónico para enseñanza de mónadas. | Agregar editorial completa en la cita: Wadler, P. (1995). *Monads for Functional Programming*. In J. Jeuring & E. Meijer (Eds.), *Advanced Functional Programming*, LNCS 925, pp. 24–52. Springer. |
| REF-02 | guia-estudio.md, guiaprofesor.md | Anderlind & Åsberg (2023). *Monadic Programming in Imperative Languages*. Tesis de Chalmers sobre implementación de mónadas en JavaScript/TypeScript. [Disponible en `_edu-knowledge/references/monads-pdfs/`] | ⚠️ DATOS-INCORRECTOS | Archivo local confirmado: `anderlind-asberg-2023-monadic-programming-imperative-languages.pdf`. ODR Chalmers accesible: https://odr.chalmers.se/items/91bf8c4b-93dd-43ca-8ac2-8b0d2c310796. Año 2023, autores (Joakim Anderlind, Mårten Åsberg), título e institución **correctos**. **ERROR**: la glosa en guia-estudio.md y en guiaprofesor.md dice "implementación de mónadas en JavaScript/TypeScript". El abstract real de la tesis indica que las implementaciones son en **Rust** (via proc-macro system) y **C#** — no en JavaScript/TypeScript. Idem el INDICE.md local, que tiene el mismo error descriptivo. | Corregir la descripción tanto en guia-estudio.md como en guiaprofesor.md: reemplazar "implementación de mónadas en JavaScript/TypeScript" por "implementación de mónadas en **Rust y C#**". Cita completa correcta: Anderlind, J. & Åsberg, M. (2023). *Monadic Programming in Imperative Languages*. Master's Thesis, Department of Computer Science and Engineering, Chalmers University of Technology. URI: https://hdl.handle.net/20.500.12380/306361 |
| REF-03 | guia-estudio.md | funcool/cats: Documentación oficial — https://funcool.github.io/cats/latest/ | ✅ VERIFICADA | URL accesible. Contenido correcto: documentación oficial de la librería `cats` para Clojure (funcool). Implementa Maybe, Either, Monad, Applicative, etc. Nota: último release documentado 2018 (librería en modo mantenimiento mínimo). Pertinente al tema — es la librería usada en los ejemplos de Clojure del tema. | Agregar nota contextual en el material: la librería `cats` data de 2014-2018 y está en modo de mantenimiento mínimo. Para proyectos Clojure nuevos con mónadas, considerar mencionar también [meander](https://github.com/noprompt/meander) o patrones idiomáticos sin librería. |
| REF-04 | guia-estudio.md | fp-ts: Documentación — https://gcanti.github.io/fp-ts/ | ✅ VERIFICADA | URL accesible. Contenido correcto: documentación oficial de `fp-ts`, librería TypeScript para programación funcional tipada. Implementa Option, Either, TaskEither, pipe. Fuente técnica oficial pertinente. | Ninguna. |
| REF-05 | guia-estudio.md | Effect: Documentación — https://effect.website/ | ✅ VERIFICADA | URL accesible. Contenido correcto: documentación oficial de Effect (Effectful Technologies). Librería TypeScript moderna para composición de efectos con tipado exhaustivo. Pertinente como referencia de ecosistema industrial para mónadas en TS. | Ninguna. |

---

## Resumen Ejecutivo por Estado

| Estado | Cantidad | Referencias |
|--------|----------|-------------|
| ✅ VERIFICADA | 4 | REF-01 (Wadler 1995), REF-03 (cats), REF-04 (fp-ts), REF-05 (Effect) |
| ⚠️ DATOS-INCORRECTOS | 1 | REF-02 (Anderlind & Åsberg 2023 — glosa con lenguaje equivocado) |
| ❌ NO-VERIFICABLE | 0 | — |
| 🚫 FUENTE-PROHIBIDA | 0 | — |
| **TOTAL** | **5** | |

---

## Detalle de Documentos Revisados

| Documento | Referencias formales encontradas | Menciones informales de herramientas |
|-----------|----------------------------------|--------------------------------------|
| `guia-estudio.md` | REF-01, REF-02, REF-03, REF-04, REF-05 | fp-ts, Effect, cats (en tablas comparativas y código) |
| `guiaprofesor.md` | REF-01, REF-02 (Extractos clave de la bibliografía) | fp-ts, Effect, cats (en recomendaciones) |
| `diseno.md` | Ninguna formal | cats, fp-ts, Effect (menciones de alcance) |
| `minuta.md` | Ninguna formal | cats, fp-ts, Effect (menciones en guion) |
| `filminas.md` | Ninguna formal | cats, fp-ts, Effect (en código de filminas) |

---

## Hallazgo Principal: Error de Contenido en REF-02

El error más relevante del ciclo es la descripción incorrecta de la tesis de Anderlind & Åsberg (2023).

**Texto actual** (guia-estudio.md y guiaprofesor.md):
> "Tesis de Chalmers que implementa Maybe, Either y IO en **JavaScript/TypeScript** y evalúa si el patrón mejora la calidad del código en lenguajes imperativos."

**Realidad verificada** (Chalmers ODR, abstract oficial):
> La tesis implementa la interfaz propuesta en **Rust** (via proc-macro system) y **C#**. No hay implementación en JavaScript ni TypeScript. Los lenguajes mencionados en abstract y keywords son: Rust, C#, Haskell (como referencia).

**Impacto pedagógico:** Si un alumno busca la tesis esperando código TypeScript y encuentra solo Rust/C#, puede pensar que la referencia está equivocada o que el docente cometió un error. Esto afecta la credibilidad del material.

**Mismo error replicado en INDICE.md local** (`_edu-knowledge/references/monads-pdfs/INDICE.md`, fila 3): también dice "incluyendo JavaScript/TypeScript". Debe corregirse en ambos lugares.

---

## Recomendaciones para el Docente

### Acción obligatoria
1. **Corregir la glosa de REF-02** en `guia-estudio.md`, `guiaprofesor.md` e `INDICE.md`:
   - Reemplazar "JavaScript/TypeScript" → "**Rust y C#**"
   - Si se desea mantener relevancia directa para el tema TS/Clojure, considerar reemplazar REF-02 por:
     - Pennanen, A. (2024). *Pragmaattisen funktionaalisen ohjelmoinnin arviointi*. Theseus — **sí evalúa fp-ts en TypeScript** y está disponible localmente.
     - Thiemann, P. (2023). *Intrinsically Typed Sessions with Callbacks*. ICFP — **implementa mónadas en TypeScript** con reader monad.

### Acción recomendada
2. **Completar la cita de REF-01** con editorial y número de páginas para cita académica formal.
3. **Agregar nota de mantenimiento a cats** (REF-03): la librería no recibe actualizaciones desde 2018; en clase se puede mencionar que existe pero enfatizar los patrones idiomáticos sin librería (`some->`, mapas `{:ok/:error}`).

### Acción opcional
4. **Considerar agregar** como lectura complementaria opcional la fuente que SÍ evalúa mónadas en TypeScript directamente: Pennanen (2024) y Thiemann (2023) — ambas están disponibles en `_edu-knowledge/references/monads-pdfs/`.

---

## Referencias Adicionales Disponibles en la Knowledge Base (no citadas en el tema)

Los siguientes papers están en `_edu-knowledge/references/monads-pdfs/` y son relevantes pero no aparecen en el material del tema:

| Archivo | Referencia |
|---------|-----------|
| `moggi-1991-notions-of-computation-and-monads.pdf` | Moggi, E. (1991). *Notions of Computation and Monads*. Info & Computation, 93(1). |
| `thiemann-2023-intrinsically-typed-sessions-callbacks.pdf` | Thiemann, P. (2023). *Intrinsically Typed Sessions with Callbacks*. ICFP. |
| `pennanen-2024-pragmatic-functional-programming-evaluation.pdf` | Pennanen, A. (2024). *Pragmaattisen funktionaalisen ohjelmoinnin arviointi*. Theseus. |
| `paju-jarvi-2023-modern-landscape-managing-effects.pdf` | Paju, J. & Järvi, J. (2023). *The Modern Landscape of Managing Effects*. U. Turku. |

Estos podrían integrarse como lecturas complementarias adicionales, especialmente para alumnos que quieran profundizar en mónadas en TypeScript (Thiemann, Pennanen) o en alternativas a mónadas (Paju & Järvi).

---

*Reporte generado por 🔬 reference-validator — Loop 3 — 2026-04-10*
