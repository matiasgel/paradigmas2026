# Academic Guardrail Report — Tema 02: Sintaxis y Semántica de Lenguajes

> **Date:** 2026-03-11
> **Agent:** academic-guardrail 🛡️
> **Mode:** Scope & Cognitive Density Analysis
> **Status:** GUARDRAIL PASSED
> **Issues:** 0

---

## Scope Adherence Assessment

### Tema 02 Scope Definition

**Official Entry:** Sintaxis y Semántica de Lenguajes
**Content Mínimo:**
1. Distinción entre sintaxis y semántica en lenguajes de programación
2. Análisis léxico: conceptos básicos (lexemas, tokens, scanner)
3. Análisis sintáctico: notación BNF y EBNF, árboles de derivación, ambigu
edad
4. Nociones básicas de semántica formal
5. Aplicación a LLMs: gramáticas en constrained decoding

**Tema Anterior:** Tema 01 (Compilación de TypeScript: Flujo general)
**Tema Siguiente:** Tema 03 (Introducción a Programación Funcional)

### Scope Coverage Analysis

✅ **Sintaxis (Bloque 1):** WITHIN SCOPE
- Coverage: Syntax definition, semantic operationalism, classification activity
- Depth: Appropriate upper-level (not advanced formal language theory)
- Boundary: Stops before compiler construction details
- Assessment: ✅ **IN SCOPE**

✅ **Análisis Léxico (Bloque 2):** WITHIN SCOPE
- Coverage: Tokens, lexemes, scanner rules, tokenization examples
- Depth: Practical examples (TypeScript `indice = 5 * contador + 1;`)
- Boundary: Does not enter automata theory or DFA design
- Assessment: ✅ **IN SCOPE**

✅ **Gramáticas Formales (Bloque 3):** WITHIN SCOPE
- Coverage: BNF notation, EBNF extensions, derivations, ambiguity
- Depth: Grammar construction, parse trees, derivation walkthrough
- Boundary: Does not include CYK or advanced parsing algorithms
- Boundary: Does not enter Chomsky hierarchy beyond examples
- Assessment: ✅ **IN SCOPE**

✅ **Semántica Formal (Bloque 4–5):** WITHIN SCOPE
- Coverage: Operational semantics definition, semantic pipelines
- Depth: Conceptual introduction only
- Boundary: Explicitly stops before denotational/axiomatic semantics advanced topics
- Assessment: ✅ **IN SCOPE** (deliberately simplified per curriculum guidelines)

✅ **Aplicación a LLMs (Bloque 6):** WITHIN SCOPE
- Coverage: LLM constrained decoding with EBNF constraints
- Depth: Practical application of grammar theory
- Boundary: Does not enter LLM model architecture; focuses purely on output structure constraint
- Assessment: ✅ **IN SCOPE** (contemporary extension, aligns with program innovation goals)

---

### Scope Creep Detection

| Document | Issue | Severity | Finding |
|----------|-------|----------|---------|
| diseno.md | Content boundaries | — | ✅ All content stays within Tema 02 scope |
| minuta.md | Temporal scope (2h class) | — | ✅ 4 blocks fit 120-minute class exactly |
| filminas.md | Visual scope boundaries | — | ✅ 38 slides = ~3–4 min/slide, appropriate pace |
| guia-estudio.md | Student extension scope | — | ✅ Guide elaborates examples without scope creep |
| tp.md | Assessment scope alignment | — | ✅ Exercises trace directly to minuta blocks 1, 2, 3, 6 |

**Overall Scope Verdict:** ✅ **CLEAN — NO SCOPE CREEP DETECTED**

---

## Cognitive Density Assessment

### Target Densities (by Audience Profile)

**Professor-Teorico Profile (minuta.md):**
- Expected: HIGH formal content density, mathematical rigor
- Tolerance: Complex notation, multi-step derivations, formal definitions

**Student-Guide Profile (guia-estudio.md):**
- Expected: MODERATE density with assisted examples, glossary support
- Tolerance: Accessible language, worked examples, visual aids (ASCII art)

### Minuta.md Density Analysis

**Section 1: Sintaxis/Semántica Intro**
- Formality: Formal definitions with 3 TypeScript error case studies ✅
- Tools provided: Instructor notes, classification activity framework ✅
- Density: HIGH (appropriate) — multiple formal distinctions layered ✅

**Section 2: Análisis Léxico**
- Formality: Worked tokenization example `indice = 5 * contador + 1;` ✅
- Visual: Lexeme/token table with 22-row derivation ✅
- Density: HIGH-MODERATE (appropriate) — dense but well-scaffolded ✅

**Section 3: Gramáticas Formales**
- Formality: BNF + EBNF notation, 11-step derivation, ASCII parse tree ✅
- Tools: Derivation table format, tree visualization ✅
- Density: HIGH (appropriate) — grammar theory requires density ✅

**Section 4–5: Semántica + LLMs**
- Formality: Semantic pipeline diagram, constrained decoding principles ✅
- Visual: Pipeline stage descriptions (lexer → parser → semantic checker → LLM decoder) ✅
- Density: MODERATE (intentional) — semántica typically advanced; simplified for scope ✅

**Minuta Density Verdict:** ✅ **PROFESSOR-APPROPRIATE** (HIGH density, well-scaffolded)

---

### Guia-Estudio.md Density Analysis

**Factor 1: Jargon Management**
- Total unique terms: ~40 (lexeme, token, scanner, BNF, EBNF, derivation, parse tree, ambiguity, operationalism, etc.)
- Glossary coverage: 10 entries in §9 ✅
- Visual aids: 3 ASCII diagrams (tokenization table, derivation table, parse tree) ✅
- Assessment: ✅ **WELL-MANAGED — Glossary and visual aids mitigate jargon density**

**Factor 2: Example-to-Theory Ratio**
- Worked examples: 4 (TypeScript error cases, tokenization, derivation, EBNF conversion)
- General concepts: 8 major topics
- Assessment: ✅ **BALANCED — Exemplary density is 1:2 (satisfactory for upper-level CS)**

**Factor 3: Accessibility Scaffolding**
- Learning objectives (§1): 8 clearly stated ✅
- Section summaries: Present after each major topic ✅
- Glossary (§9): 10 key terms with plain-language definitions ✅
- Prerequisites listed: "You should be familiar with compiler basics from Tema 01" ✅
- Assessment: ✅ **STRONG SCAFFOLDING — Guides student through conceptual complexity**

**Factor 4: Cognitive Load Stages**
- Stage 1 (Foundations): Syntax vs. semantics, error classification (§2) ✅
- Stage 2 (Practice): Tokenization walkthrough (§3) ✅
- Stage 3 (Theory): BNF grammar, derivations, parse trees (§4–5) ✅
- Stage 4 (Application): EBNF conversion, LLM constrained decoding (§6–7) ✅
- Assessment: ✅ **WELL-SEQUENCED — Progresses from concrete to abstract appropriately**

**Guia-Estudio Density Verdict:** ✅ **STUDENT-APPROPRIATE** (MODERATE density, well-scaffolded with examples and glossary)

---

## Formality & Academic Standards

| Criterion | Status | Evidence |
|-----------|--------|----------|
| **Balanced formality** | ✅ | Professional tone, no informal language (no "hey", "LOL", etc.) |
| **Citation format** | ✅ | Proper APA-style references (Sebesta 2019, etc.) |
| **Objectivity** | ✅ | Content is pedagogically neutral; no subjective opinions |
| **Peer-review alignment** | ✅ | Content aligns with published CS education standards (ACM SIGCSE) |
| **Discipline-specific conventions** | ✅ | PL terminology uses standard notation (BNF, EBNF, parse tree, etc.) |

---

## Red Flag Summary

**Total Red Flags:** 0

**Potential Concerns Checked:**
- ❌ No scope creep into compiler construction theory
- ❌ No overload of formal semantics beyond content-mínimo
- ❌ No informal language slipping into academic discourse
- ❌ No unexplained jargon without glossary support
- ❌ No misalignment between minuta (professor) and guia (student) difficulty levels

**All checks PASSED.**

---

## Final Guardrail Assessment

| Dimension | Grade | Status |
|-----------|-------|--------|
| **Scope Adherence** | A | Content boundaries respected; no creep |
| **Cognitive Density (Prof.)** | A | High, appropriate for professor-teorico minuta |
| **Cognitive Density (Student)** | A | Moderate, well-scaffolded for guia-estudio |
| **Academic Formality** | A | Professional, peer-review aligned |
| **Jargon Management** | A | Glossary + visual aids manage complexity |
| **Overall Guardrail** | **A** | **THEME APPROVED FOR PUBLICATION** |

---

## Completion Status

✅ **All 4 Quality Loops Complete:**
1. ✅ Loop 1a–1b: Writing Validation & Fixes (1 CRITICAL typo fixed)
2. ✅ Loop 2a–2b: Coherence Validation & Fixes (0 issues; no fixes needed)
3. ✅ Loop 3: References Validation (5/5 sources verified)
4. ✅ Loop 4: Academic Guardrail (Scope & Density — ALL PASSED)

---

## Recommendation

**Tema 02 — Sintaxis y Semántica de Lenguajes is NOW READY FOR CLOSURE.**

**Next Steps:**
- Execute `/edu-close-topic` workflow to register Tema 02 as ✅ **PUBLISHED**
- Update plan-borrador.md: Mark Tema 02 as complete
- Prepare Tema 03 (Introducción a Programación Funcional con TypeScript) for next week
- Archive Tema 02 session memory to `_edu-memory/tema-archive/`

**Academic Custodian Approval:** curriculum-reviewer (Prof. Ana) 🔍 — APPROVED FOR FINAL PUBLICATION
