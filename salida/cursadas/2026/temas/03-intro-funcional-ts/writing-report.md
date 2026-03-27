# Writing Report — Tema 03
## Introducción a Programación Funcional con TypeScript
**Ejecutado:** 2026-03-27 | **Agentes:** writing-validator, writing-fixer, coherence-fixer, reference-validator, academic-guardrail

---

## Loop 1 — Validación y Corrección de Escritura

### Errores encontrados y corregidos

| ID | Tipo | Documento | Texto original | Corrección aplicada |
|----|------|-----------|---------------|---------------------|
| WV-01 | [ERROR] | `guia-estudio.md` L88 | `### 1.2 Linea de tiempo` | `### 1.2 Línea de tiempo` |
| WV-02 | [CRÍTICO] | `tp-quiz.gift` Q56 | `se evatan los loops` | `se evitan los loops` |

**2 correcciones automáticas aplicadas. 0 mejoras pendientes de confirmación.**

**Nota crítica tp-quiz.gift:** Archivo modificado con máximo cuidado. Solo se corrigió la pregunta del enunciado (línea de texto visible al alumno). El estructura GIFT (escapes `\:`, `\=`, `\{`, `\}`, categorías, pesos) permanece intacta.

---

## Loop 2 — Coherencia Inter e Intra Documento

### Verificación de terminología

| Término | Ocurrencias | Estado |
|---------|-------------|--------|
| `β-reducción` | 6 en guía + 3 en quiz | ✓ Consistente |
| `λ-cálculo` | 8 en guía + 4 en quiz | ✓ Consistente |
| `Máquina de Turing` | 5 en guía + 4 en quiz | ✓ Consistente |
| `funciones de orden superior` | 4 en guía + 2 en quiz | ✓ Consistente |
| `transparencia referencial` | 6 en guía + 6 en quiz | ✓ Consistente |
| `inmutabilidad` | 10 en guía + 8 en quiz | ✓ Consistente |

### Trazabilidad OA → Quiz

| OA | Nivel Bloom | Categoría Quiz | Preguntas | Estado |
|----|-------------|----------------|-----------|--------|
| OA-7 | Comprender | A — Historia | Q01–Q10 | ✓ |
| OA-1 | Comprender | B — Modelo funcional | Q11–Q18 | ✓ |
| OA-2, OA-3 | Comprender / Aplicar | C — Funciones puras | Q19–Q30 | ✓ |
| OA-2, OA-5 | Comprender / Analizar | D — Inmutabilidad | Q31–Q38 | ✓ |
| OA-2, OA-5 | Comprender / Analizar | E — Transparencia referencial | Q39–Q44 | ✓ |
| OA-3, OA-4 | Aplicar | F — map / filter / reduce | Q45–Q56 | ✓ |
| OA-6 | Analizar | G — Clojure | Q57–Q60 | ✓ |

**Sin inconsistencias entre guía, quiz y minuta.**

---

## Loop 3 — Validación de Referencias

| # | Referencia | Tipo | Verificación |
|---|-----------|------|-------------|
| 1 | Gabbrielli & Martini (2023). *Programming Languages: Principles and Paradigms* 2ª ed. Springer. Cap. 11. | Textbook | ✓ Presente en `/ingesta/` |
| 2 | Sebesta, R. W. (2019). *Concepts of Programming Languages* 12ª ed. Pearson. Cap. 15. | Textbook | ✓ Presente en `/ingesta/` |
| 3 | Louden & Lambert (2011). *Programming Languages: Principles and Practice* 3ª ed. Course Technology. | Textbook | ✓ Presente en `/ingesta/` |
| 4 | Apunte de cátedra UNTDF (2025). *Introducción a la Programación Funcional*. IDEI. | Material interno | ✓ Fuente de cátedra |

**Sin fuentes prohibidas (Wikipedia, blogs). Sin referencias a verificar por DOI (libros de texto).**

---

## Guardrail Académico

| Criterio | Evaluación |
|----------|-----------|
| Registro formal | ✓ Sostenido en todo el documento |
| Densidad cognitiva | ✓ Adecuada para 4° año Lic. Sistemas |
| Bloom coverage | ✓ Niveles 1 (Recordar) a 5 (Evaluar) cubiertos |
| Marcadores pendientes | ✓ Ninguno (`<!-- PENDIENTE: -->`) |
| Fuentes prohibidas | ✓ Ninguna |
| Formalidad de quiz | ✓ 60 preguntas con feedback explicativo |

---

## Resumen Final

- **Estado:** ✅ Aprobado — listo para exportar a PDF
- **Correcciones aplicadas:** 2 (1 en guía, 1 en quiz)
- **Archivos modificados:** `guia-estudio.md`, `tp-quiz.gift`
- **Integridad del quiz GIFT:** ✓ Sin alteraciones a estructura Moodle
