# Scope & Density Report — Tema 02: Sintaxis y Semántica de Lenguajes

**Agente:** academic-guardrail 🛡️  
**Fecha:** 2026-03-20  
**Config:** `academic_guardrail_enabled: true` · Perfil docente: `profesor-teorico`  
**Prerequisito:** Loops 1, 2 y 3 completados ✅

---

## Resumen Ejecutivo

| Dimensión | Resultado | Issues |
|-----------|-----------|--------|
| Lenguaje informal | ⚠️ 1 anglicismo | Auto-corregido |
| Desviación de scope | ✅ Sin issues | — |
| Densidad cognitiva — minuta.md | ✅ Dentro del rango | `profesor-teorico` |
| Densidad cognitiva — filminas.md | ✅ Dentro del rango | Filminas, densidad baja esperada |
| Densidad cognitiva — guia-estudio.md | ✅ Dentro del rango | Perfil `student-guide` aplicado |
| Densidad cognitiva — tp.md | ✅ Dentro del rango | Formato quiz, densidad normal |

---

## Lenguaje Formal — Issues Detectados

### GR-L01 · guia-estudio.md · línea 649 · Anglicismo

- **Ubicación:** Sección 5 — Ejemplo 2 (derivación), cierre del example
- **Original:** `**Chequeo:** todos los símbolos son terminales. La derivación está completa.`
- **Tipo:** Anglicismo: "chequeo" (de *check*); en español académico formal corresponde "Verificación" o "Comprobación"
- **Corrección:** `**Verificación:** todos los símbolos son terminales. La derivación está completa.`
- **Estado:** ✅ auto-corregido

---

## Scope — Verificación

### Items OUT OF SCOPE — Respetados

| Item OUT OF SCOPE (diseno.md) | ¿Aparece en profundidad? | Estado |
|-------------------------------|--------------------------|--------|
| Scope rules, binding y entorno (→ Tema 09) | Solo mención breve en B5; tratamiento completo diferido ✅ | ✅ OK |
| Algoritmos de parsing (recursive-descent, LR) | Solo mención conceptual sin desarrollo de algoritmos ✅ | ✅ OK |
| Semántica operacional formal (formalismos SOS) | Solo panorámica de 3 enfoques; formalismos diferidos a Semántica Formal ✅ | ✅ OK |

### Items IN SCOPE — Cobertura verificada

| Item del Plan Mínimo | Cubierto en | Status |
|----------------------|-------------|--------|
| Sintaxis y semántica — nociones básicas | filminas B1, guia §4.1, minuta B1 | ✅ |
| Semántica estática (gramáticas de atributos) | filminas B5 F-25/F-26, guia §4.6 | ✅ |
| Semántica dinámica — tres enfoques | filminas B5 F-27, guia §4.6 | ✅ (sólo mención) |
| Conceptos de intérpretes y compiladores | filminas B6 F-29/F-31, guia §4.7 | ✅ |

---

## Densidad Cognitiva — Análisis por Documento

### minuta.md (perfil: `profesor-teorico`)

- **Nivel:** Adecuado para notas de conducción de clase
- **Patrones:** Instrucciones claras por filmina; alternancia entre explicación y preguntas; tiempos bien marcados
- **Observaciones:** Los bloques de tiempo son específicos y manejables; no se detecta sobrecarga conceptual por filmina

### filminas.md (perfil: presentación académica)

- **Nivel:** Adecuado para filminas — densidad intencionalmente baja; se evita texto largo
- **Patrones:** Predominan tablas, código y listas cortas; buena relación texto/blanco
- **Observaciones:** B5 (semántica) es el bloque con mayor densidad conceptual; está diseñado como síntesis (12 min) — aceptable

### guia-estudio.md (perfil: `student-guide`)

- **Nivel:** Apropiado para material de estudio autónomo
- **Patrones:** Uso de iconos 💡 para destacar estrategias de estudio; ejemplos trabajados paso a paso; ejercicios de autoevaluación separados del TP
- **Observaciones:** La guía es extensa (~830 líneas) pero el nivel de detalle es intencionalmente alto para un material de referencia del alumno. Los ejemplos derivados son largos pero didácticamente necesarios

### tp.md (perfil: evaluación formativa)

- **Nivel:** Adecuado para quiz Moodle de 40 preguntas
- **Patrones:** Instrucciones concisas; gramáticas de referencia bien especificadas; distribución de secciones clara
- **Observaciones:** El énfasis en BNF/EBNF (65% de preguntas) está alineado con los objetivos centrales del diseño

---

## Resultado Final

Todos los documentos del Tema 02 pasan la auditoría del guardrail con **1 corrección menor** (anglicismo auto-corregido).  
Los loops de calidad 1-3 + guardrail están completos. El tema está listo para publicación.
