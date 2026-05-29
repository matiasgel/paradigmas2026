# Configuración Moodle 5 — Quiz TP 09

**Temas cubiertos:** 09.1 Variables, Binding y Ámbito + 09.2 Aliases, Closures, GC, Gradual Typing e Inmutabilidad FP  
**Generado:** 2026-05-28 — Agente Valeria (tp-designer)  
**Archivo GIFT:** `tp-quiz.gift`

---

## Banco de preguntas

- **Archivo:** `tp-quiz.gift`
- **Categoría:** `TP/09-variables-binding-closures`
- **En importación:** activar `Get category from file` para respetar el `$CATEGORY:` definido en el archivo
- **Encoding:** UTF-8 sin BOM (obligatorio)
- **Total de preguntas:** 30

### Preguntas por bloque

| Rango | Bloque | Cantidad |
|-------|--------|----------|
| Q01–Q15 | 09.1 — Variables, Binding y Ámbito | 15 |
| Q16–Q30 | 09.2 — Aliases, Closures, GC, Gradual Typing, FP | 15 |

### Tipos de preguntas

| Tipo | Cantidad |
|------|----------|
| Multiple choice (respuesta única) | 30 |
| Con fragmento de código | ~10 |
| Teóricas conceptuales | ~20 |

### Lenguajes presentes en las preguntas con código

- TypeScript (principal): Q02, Q07, Q09, Q12, Q14, Q17, Q18, Q21, Q22, Q23, Q28, Q29, Q30
- JavaScript (comparación con TS): Q12, Q15, Q22
- Python (comparación/closures/GC): Q24, Q26, Q30
- Haskell (FP puro): Q29
- Go (breve mención en contexto): implícito en Q19

---

## Configuración sugerida de la actividad Quiz en Moodle 5

| Parámetro | Valor sugerido | Justificación |
|-----------|---------------|---------------|
| **Nombre** | `TP 09 — Variables, Binding, Closures y GC` | Título visible para el alumno |
| **Intentos permitidos** | `1` para evaluación sumativa; `3` para práctica formativa | Ajustar según uso |
| **Método de calificación** | `Highest` (si hay múltiples intentos) | Beneficia al alumno |
| **Tiempo límite** | `40 minutos` | ~80 seg/pregunta; ajustable |
| **Cuando se acaba el tiempo** | `Open attempts are submitted automatically` | Estándar |
| **Navegación** | `Free` | El alumno puede revisitar preguntas |
| **Comportamiento de preguntas** | `Deferred feedback` | Para examen. Usar `Interactive with multiple tries` para práctica. |
| **Shuffle opciones dentro de pregunta** | `Sí` | Dificulta memorización del orden |
| **Shuffle preguntas** | Opcional | Activar si se quiere variabilidad entre alumnos |

---

## Review Options sugeridas

| Franja | Mostrar | Ocultar |
|--------|---------|---------|
| Immediately after attempt | Puntaje | Right answer, feedback, respuesta marcada |
| While quiz is still open | Puntaje, respuesta marcada | Right answer, feedback general |
| After the quiz is closed | Todo | — |

---

## Puntaje

- **Puntaje por pregunta:** uniforme (1 punto c/u)
- **Total:** 30 puntos
- **Nota sugerida de aprobación:** 60% (18/30)
- **Grade category en Moodle:** asignar a la categoría del TP 09 en el gradebook

---

## Procedimiento de importación paso a paso

1. En el curso Moodle → `More` → `Question banks`
2. Seleccionar (o crear) la question bank del curso
3. `Import` → `GIFT format`
4. Subir `tp-quiz.gift` (UTF-8 sin BOM)
5. Activar `Get category from file` → Moodle creará automáticamente `TP/09-variables-binding-closures`
6. Confirmar importación — verificar que las 30 preguntas aparezcan en estado `Ready`
7. Volver al curso → `Add an activity` → `Quiz`
8. Configurar settings según tabla anterior
9. `Edit quiz` → `Add` → `from question bank`
10. Seleccionar la categoría `TP/09-variables-binding-closures`
11. Agregar las 30 preguntas al quiz
12. Configurar puntaje por pregunta y guardar

---

## Notas importantes

- Los parámetros de tiempo, intentos, review options y navegación **no viajan dentro del GIFT**; deben configurarse manualmente en la actividad Quiz.
- Las preguntas importadas quedan en el **course question bank**; son reutilizables en otros quizzes del mismo curso.
- Las preguntas con código usan `[markdown]` y `<pre><code>...</code></pre>` — verificar que el tema Moodle renderice markdown correctamente (activar en `Site administration → Additional HTML`).
- Si alguna pregunta aparece como `Draft` en vez de `Ready`, editarla y guardar para activarla.
- Los caracteres reservados GIFT (`~ = # { } :`) en los enunciados de código están escapados con `\` según la especificación.

---

## Cobertura de objetivos de aprendizaje

| Objetivo | Preguntas |
|----------|-----------|
| OA1 (09.1) — Variable como 5-tupla | Q01, Q02 |
| OA2 (09.1) — 6 momentos de binding | Q03, Q04 |
| OA3 (09.1) — Categorías de variables | Q08, Q09 |
| OA4 (09.1) — Ámbito estático vs. dinámico | Q10, Q11, Q13 |
| OA5 (09.1) — Dimensiones ortogonales del tipado | Q05, Q06, Q07, Q15 |
| OA6 (09.1) — Hoisting y scope en TypeScript | Q12, Q14 |
| OA1 (09.2) — Aliases | Q16, Q17, Q18, Q19 |
| OA2 (09.2) — Closures y binding | Q20, Q21, Q22, Q23 |
| OA3 (09.2) — Garbage collection | Q24, Q25, Q26 |
| OA4 (09.2) — Gradual typing | Q27, Q28 |
| OA5 (09.2) — Inmutabilidad FP | Q29, Q30 |
