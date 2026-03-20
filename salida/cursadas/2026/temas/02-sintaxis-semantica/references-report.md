# References Report — Tema 02: Sintaxis y Semántica de Lenguajes

**Agente:** reference-validator 🔬  
**Fecha:** 2026-03-20  
**Fuentes verificadas:** arXiv, ACL Anthology  
**Prerequisito:** Loops 1 y 2 completados ✅

---

## Resumen

| Estado | Qty | Referencias |
|--------|-----|-------------|
| ✅ Correctas | 4 | Willard & Louf, Gong, Sebesta, Gabbrielli & Martini |
| ❌ Con errores | 3 | Beurer-Kellner et al. (LMQL), Geng et al., Alpay & Senturk |

---

## ✅ Referencias verificadas y correctas

| ID | Referencia | Verificado via |
|----|-----------|----------------|
| OK-1 | Willard, B.T. & Louf, R. (2023). *Efficient Guided Generation for LLMs*. arXiv:2307.09702 | arXiv ✅ |
| OK-2 | Gong, W.G. (2026). *Structured Prompt Language: Declarative Context Management for LLMs*. arXiv:2602.21257 | arXiv ✅ |
| OK-3 | Sebesta, R. (2019). *Concepts of Programming Languages*, 12ª ed. | estándar de cátedra ✅ |
| OK-4 | Gabbrielli & Martini (2023). *Programming Languages: Principles and Paradigms* | estándar de cátedra ✅ |

---

## ❌ Errores de referencia — auto-corregidos en filminas.md

### REF-E01 · filminas.md F-37 · Beurer-Kellner et al. (LMQL)

- **Errores:** título abreviado incorrecto + venue equivocado
- **Original:** `*LMQL: Prompting Is Programming*. VLDB 2023. arXiv:2212.06094`
- **Corrección:** `*Prompting Is Programming: A Query Language for Large Language Models*. PLDI'23. arXiv:2212.06094`
- **Fuente de verificación:** arXiv:2212.06094 — confirmado PLDI'23 (44th ACM SIGPLAN PLDI), NOT VLDB
- **Estado:** ✅ auto-corregido

---

### REF-E02 · filminas.md F-37 · Alpay & Senturk — título incompleto

- **Error:** título trunca el subtítulo del paper
- **Original:** `*Attention Meets Reachability: Grammar-Constrained LLM Decoding*`
- **Corrección:** `*Attention Meets Reachability: Structural Equivalence and Efficiency in Grammar-Constrained LLM Decoding*`
- **Fuente:** arXiv:2603.05540 verificado ✅
- **Estado:** ✅ auto-corregido

---

### REF-E03 · filminas.md F-34 · Alpay & Senturk — nota inline incompleta

- **Error:** la nota inline en la filmina F-34 tenía solo el subtítulo, sin el título principal
- **Original:** `Structural Equivalence and Efficiency in Grammar-Constrained LLM Decoding`
- **Corrección:** `Attention Meets Reachability: Structural Equivalence and Efficiency in Grammar-Constrained LLM Decoding`
- **Estado:** ✅ auto-corregido

---

### REF-E04 · filminas.md F-37 · Geng et al. — título incompleto + venue incorrecto + ID faltante

- **Errores:** título incompleto, venue erróneo, sin arXiv ID
- **Original:** `*Grammar-Constrained Decoding for Structured NLP Tasks*. ACL 2023`
- **Corrección:** `*Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning*. EMNLP 2023. arXiv:2305.13971`
- **Autores completos:** Saibo Geng, Martin Josifoski, Maxime Peyrard, Robert West
- **Fuente:** arXiv:2305.13971 — Accepted at EMNLP 2023 Main Conference ✅
- **Estado:** ✅ auto-corregido

---

## Sin arXiv ID (no verificables por arXiv)

- **Slides de cátedra UNTDF 2025** — material interno, no verificable externamente. Se acepta como referencia de cátedra.
