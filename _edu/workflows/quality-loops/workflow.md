# Workflow: Quality Loops

**Module:** edu
**Phase:** 3 — Producción de Temas
**Agents:** writing-validator, writing-fixer, coherence-fixer, reference-validator, academic-guardrail

---

## Overview

Cadena secuencial de 4 loops de calidad que se ejecutan DESPUÉS de crear la clase, la guía de estudio y el TP.

## Document Scope

Todos los loops aplican al conjunto completo de documentos del tema:
- `diseno.md` — diseño del tema
- `minuta.md` — clase del docente
- `filminas.md` — presentación de clase
- `guia-estudio.md` — guía de estudio del alumno (**incluida en todos los loops**)
- `guiaprofesor.md` — guía de revisión docente (**incluir si existe**)
- `tp.md` — trabajo práctico

Si `guia-estudio.md` no existe aún, omitirla de los loops y notificar al docente: "⚠️ guia-estudio.md no encontrado — los loops se aplican a los demás documentos. Generá la guía con /edu-create-study-guide para incluirla."

Si `guiaprofesor.md` no existe, omitirla silenciosamente. No es bloqueante, pero si existe debe mantenerse alineada con el resto del tema.

## Loop Sequence

### Loop 1a: Validate Writing
- **Agent:** writing-validator
- **Input:** All topic documents (diseno.md, minuta.md, filminas.md, **guia-estudio.md**, **guiaprofesor.md si existe**, tp.md)
- **Output:** `writing-report.md` with classified issues [CRITICAL], [ERROR], [IMPROVEMENT]
- **Note for guia-estudio.md:** Validate also that student-facing language is clear and accessible (not professor-internal jargon)
- **Note for guiaprofesor.md:** Validate consistency between teacher guidance, deadlines, links, and the approved design.

### Loop 1b: Fix Writing
- **Agent:** writing-fixer
- **Auto-fix:** [CRITICAL] and [ERROR]
- **Confirm:** [IMPROVEMENT] requires professor approval
- **Output:** Git commits: `[writing-fixer] {ID}: {description}`

#### Auto-fix de referencias pendientes (sin confirmación)
Antes de procesar el report, el writing-fixer ejecuta el siguiente sub-paso:

1. Buscar en todos los documentos del tema marcadores de la forma:
   ```
   <!-- PENDIENTE: revisar manualmente {archivo}.txt -->
   ```
2. Para cada marcador encontrado, verificar si existe `{material_folder}/txt/{archivo}.txt`
3. Si **existe** → leer el `.txt`, extraer el fragmento relevante al contexto inmediato del marcador (párrafo o sección donde aparece), reemplazar el marcador por el contenido extraído y hacer commit automático:
   ```
   [writing-fixer] REF-AUTO: integrado contenido de {archivo}.txt en {documento}
   ```
4. Si **no existe** → dejar el marcador intacto y reportarlo como `[ERROR]` en el writing-report para que el docente lo resuelva manualmente
5. Este sub-paso se ejecuta **antes** del resto del auto-fix y **no requiere confirmación del docente**

### Loop 2a: Validate Coherence
- **Agent:** coherence-fixer (detect mode)
- **Prerequisite:** Loop 1 completed
- **Input:** All topic documents (including **guia-estudio.md** and **guiaprofesor.md si existe**)
- **Special check for guia-estudio.md:** Verify that all filmina references (e.g. "Ver Filmina 3") match actual filminas.md section numbers; verify all topic cross-references are accurate
- **Special check for guiaprofesor.md:** Verify that teacher checklists, classroom logistics, and resource paths match the actual repository state.
- **Output:** `coherence-report.md`

### Loop 2b: Fix Coherence
- **Agent:** coherence-fixer (fix mode)
- **Output:** Git commits: `[coherence-fixer] {ID}: {description}`

### Loop 3: Validate References
- **Agent:** reference-validator
- **Sources:** CrossRef, Semantic Scholar, arXiv, OpenLibrary
- **Input:** All topic documents (including **guia-estudio.md** and **guiaprofesor.md si existe** — their references sections are primary validation targets)
- **Output:** `references-report.md`
- **Manual:** Professor decides on flagged references

### Guardrail: Scope & Density
- **Agent:** academic-guardrail
- **Prerequisite:** Loops 1-3 completed
- **Checks:** Informal language, scope deviation, cognitive density
- **Input:** All topic documents (including **guia-estudio.md** and **guiaprofesor.md si existe**)
- **Special density profile for guia-estudio.md:** Apply `student-guide` cognitive density thresholds (more lenient than minuta — study guides are intentionally more verbose for clarity)
- **Special density profile for guiaprofesor.md:** Apply `teacher-guide` thresholds — high information density is acceptable if logistics and decisions remain scannable.
- **Output:** `scope-report.md`, `density-report.md`
- **Auto-fix:** Only if `academic_guardrail_enabled: true`

