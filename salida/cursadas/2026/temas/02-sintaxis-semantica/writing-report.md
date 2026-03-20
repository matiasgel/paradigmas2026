# Writing Report — Tema 02: Sintaxis y Semántica de Lenguajes

**Agente:** writing-validator 🔎  
**Fecha:** 2026-03-20  
**Documentos revisados:** diseno.md, minuta.md, filminas.md, guia-estudio.md, tp.md  
**Marcadores PENDIENTE:** ninguno encontrado  

---

## Resumen

| Categoría | Cantidad |
|-----------|----------|
| [CRÍTICO] | 0 |
| [ERROR]   | 3 |
| [MEJORA]  | 1 |

---

## [ERROR] — Errores claros (auto-fix aplicado)

### WR-E01 · filminas.md · línea 733

- **Documento:** filminas.md
- **Ubicación:** F-32, título de sección
- **Texto original:** `## Ejemplo práctico — guiar estructura con prompt bando`
- **Tipo de error:** ortográfico — palabra incorrecta ("bando" en lugar de "blando")
- **Corrección:** `## Ejemplo práctico — guiar estructura con prompt blando`
- **Estado:** ✅ auto-corregido

---

### WR-E02 · minuta.md · línea 155

- **Documento:** minuta.md
- **Ubicación:** Bloque 2, diálogo del docente sobre F-10 (lexemas y tokens)
- **Texto original:** `Un mismo token (\`identificador\`) puede tens miles de lexemas distintos.`
- **Tipo de error:** tipográfico — verbo incompleto ("tens" en lugar de "tener")
- **Corrección:** `Un mismo token (\`identificador\`) puede tener miles de lexemas distintos.`
- **Estado:** ✅ auto-corregido

---

### WR-E03 · guia-estudio.md · línea 624

- **Documento:** guia-estudio.md
- **Ubicación:** Sección 5, Ejemplo 2 — título del ejemplo
- **Texto original:** `` ### Ejemplo 2: Derivación completa de `A := B* (A + C)` ``
- **Tipo de error:** tipográfico — espacio faltante alrededor del operador `*`; `B*` puede leerse como anotación de repetición (regex/EBNF) en lugar de multiplicación
- **Corrección:** `` ### Ejemplo 2: Derivación completa de `A := B * (A + C)` ``
- **Estado:** ✅ auto-corregido

---

## [MEJORA] — Sugerencias (requieren aprobación del docente)

### WR-M01 · diseno.md · línea 10

- **Documento:** diseno.md
- **Ubicación:** Historial de ajustes (metadata)
- **Texto:** `B6 reenmarcado como síntesis`
- **Observación:** "reenmarcado" es una forma no estándar. La forma canónica sería "reencuadrado" o "reformulado como síntesis".
- **Sugerencia:** `B6 reformulado como síntesis`
- **Estado:** ⏳ pendiente de aprobación del docente

---

## Notas para Loop 2 (coherencia)

- filminas.md, cabecera (línea 14): estado del input dice "pendiente de aprobación" aunque diseno.md figura como APROBADO → inconsistencia de estado a resolver en Loop 2.
