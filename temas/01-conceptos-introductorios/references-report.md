# References Report — Tema 01: Conceptos Introductorios + Intro a TypeScript

> **Agente:** reference-validator 🔬
> **Fecha:** 2026-03-10
> **Prerequisito:** Loops 1 y 2 completados
> **Fuentes consultadas:** conocimiento de entrenamiento (libros académicos consolidados) + análisis de consistencia interna de citaciones
> **⚠️ Nota:** El agente no tiene acceso en tiempo real a CrossRef, Semantic Scholar, arXiv ni OpenLibrary en esta ejecución. Las referencias que requieren verificación externa están marcadas con [VERIFICAR].
> **Estado:** 3 referencias válidas con alta confianza · 1 referencia [VERIFICAR MANUALMENTE]

---

## Inventario de referencias por documento

| Referencia | Documentos que la citan | Tipo |
|-----------|------------------------|------|
| Sebesta (2018), 12th ed. | diseno, minuta, filminas (F-04), guia-estudio, tp | Libro de texto |
| Louden & Lambert, 3rd ed. | diseno, minuta, filminas (F-08, F-11, F-18), guia-estudio, tp | Libro de texto |
| Gabbrielli & Martini, 2nd ed. | diseno, minuta, filminas (F-14, F-16), guia-estudio, tp | Libro de texto |
| Schmidt & Runfola (2025) arXiv:2511.17696 | diseno, minuta, filminas (F-21, F-22, F-26), guia-estudio, tp | Preprint arXiv |

---

## Validación detallada

### REF-01 — Sebesta (2018)

**Referencia completa citada:**
> Sebesta, Robert W. *Concepts of Programming Languages*, 12th ed. Pearson, 2018.

**Estado:** ✅ **VÁLIDA — alta confianza**

**Análisis:**
- La existencia del libro es confirmable: Robert W. Sebesta publicó múltiples ediciones de "Concepts of Programming Languages" con Pearson. Las ediciones del libro van hasta la 12ª. La 11ª edición es de 2015 y la 12ª alrededor de 2018 — consistente con la cita.
- El capítulo 1 de Sebesta cubre criterios de evaluación de lenguajes (legibilidad, escribibilidad, confiabilidad, costo, portabilidad, eficiencia) — consistente con el uso en los documentos.
- La filmina F-04 cita "Sebesta (2018)" con 6 criterios. Sebesta Cap. 1 §1.3 efectivamente lista estos criterios. ✓
- **Incongruencia menor (no es error de referencia):** La filmina F-04 lista 6 criterios; diseno.md lista 7 (incluyendo "Entorno de programación"). Sebesta menciona criterios adicionales en ediciones más modernas — el docente seleccionó 6 para la clase. Esto ya fue documentado como IMP-01 en writing-report.md.

**Acción requerida:** Ninguna.

---

### REF-02 — Louden & Lambert (3rd ed.)

**Referencia completa citada:**
> Louden, Kenneth C. & Lambert, Kenneth A. *Programming Languages: Principles and Practice*, 3rd ed. Course Technology / Cengage Learning, 2011.

**Estado:** ✅ **VÁLIDA — alta confianza**

**Análisis:**
- La 3ª edición de Louden & Lambert existe y fue publicada por Course Technology (Cengage Learning) en 2011. ✓
- El capítulo 1 incluye discusión sobre:
  - Historia y evolución de los LP — citado en Bloque 1 ✓
  - La arquitectura de Von Neumann y el paradigma imperativo ✓
  - El "cuello de botella de Von Neumann" (Von Neumann bottleneck) ✓
  - La jerarquía de niveles de abstracción (figuras en Cap. 1) ✓
  - Funciones de orden superior (`map` y `reduce`) ✓

**Observación sobre Figures 1.4 y 1.5:** Los documentos citan "Louden & Lambert, Cap. 1 — Fig. 1.4 y 1.5" para la "escalera de abstracciones". Los números de figura **no son verificables sin acceso físico al libro**. Se recomienda que el docente confirme los números exactos contra su ejemplar.

**Acción requerida:** ⚠️ [VERIFICAR] Confirmar que las Figs. 1.4 y 1.5 de Louden & Lambert Cap. 1 corresponden efectivamente a la "escalera de abstracciones" mencionada en filminas y guía.

---

### REF-03 — Gabbrielli & Martini (2nd ed.)

**Referencia completa citada:**
> Gabbrielli, Maurizio & Martini, Simone. *Programming Languages: Principles and Paradigms*, 2nd ed. Springer, 2010.

**Estado:** ✅ **VÁLIDA — alta confianza**

**Análisis:**
- La 2ª edición de Gabbrielli & Martini existe, publicada por Springer en 2010 (Undergraduate Topics in Computer Science). ✓
- El capítulo 1 de este libro es precisamente sobre **máquinas abstractas** — el concepto central citado en los documentos ("Todo lenguaje define una máquina abstracta $M_L$"). ✓
- Las dos formas de implementación (interpretación pura vs. compilación pura) y el concepto de lenguaje intermedio están en Cap. 1.

**Observación:** La fórmula matemática $M_L$ usada en guia-estudio.md es consistente con la notación del libro. ✓

**Acción requerida:** Ninguna.

---

### REF-04 — Schmidt & Runfola (2025), arXiv:2511.17696

**Referencia completa citada:**
> Schmidt, Eric & Runfola, Dan. *Liberating Logic in the Age of AI*. arXiv:2511.17696, 2025.

**Estado:** ⚠️ **[VERIFICAR MANUALMENTE]**

**Análisis:**
- El ID arXiv `2511.17696` sigue el formato `YYMM.NNNNN`, correspondiendo a **noviembre de 2025** — fecha que está **fuera del período de entrenamiento del agente** para verificación directa.
- El título "Liberating Logic in the Age of AI" y los autores "Schmidt & Runfola" **no pueden ser verificados** con certeza desde el conocimiento de entrenamiento.
- Las citas específicas son:
  - `§2`: cambio de rol del programador (porcentajes de tareas: 70%→20% codificación, etc.)
  - `Fig. 8`: el "loop trust but verify"
  - `Fig. 12`: jerarquía AI Literacy → AI Fluency → AI Mastery
  - `Fig. 14`: "sweet spot" entre autonomía y dependencia de IA
  - Cita textual: *"Natural language has become the new compiler, and developer's focus is migrating from syntax and semantics to strategy"*
- La cita textual es internamente consistente con el resto del documento y temáticamente plausible para la era de IA generativa.
- Si el paper existe en arXiv, está accesible gratuitamente en `https://arxiv.org/abs/2511.17696`.

**Acción requerida:** 🔴 **VERIFICACIÓN MANUAL OBLIGATORIA por el docente.**
1. Acceder a `https://arxiv.org/abs/2511.17696`
2. Confirmar: título, autores, año.
3. Verificar que la cita textual existe en §2
4. Verificar que las Figs. 8, 12 y 14 corresponden a los conceptos citados.
5. Si el paper no existe o los datos son incorrectos: **reemplazar o eliminar la referencia** antes de la clase y actualizar las filminas F-21 a F-26 y la sección 5 de la guía de estudio.

---

## Resumen de acciones requeridas por el docente

| ID | Urgencia | Acción |
|----|----------|--------|
| REF-02-fig | Baja | Confirmar que Figs. 1.4 y 1.5 de Louden & Lambert corresponden a la escalera de abstracciones |
| REF-04 | **Alta** | Verificar existencia y contenido de arXiv:2511.17696 (Schmidt & Runfola 2025) antes de la clase |

---

## Verificaciones internas que NO requieren acción

| Check | Estado |
|-------|--------|
| Consistencia interna de citas entre documentos | ✅ Todas las citas son consistentes entre sí |
| Sebesta Cap. 1 como fuente de criterios de evaluación | ✅ Correcto |
| Louden & Lambert Cap. 1 como fuente de Von Neumann bottleneck | ✅ Correcto |
| Gabbrielli & Martini Cap. 1 como fuente de máquinas abstractas | ✅ Correcto |
| Formato de cita arXiv (YYMM.NNNNN) | ✅ Formato válido |
| Ejemplo de código TypeScript vs. cita Louden (map/reduce = funciones de orden superior) | ✅ Correcto |
