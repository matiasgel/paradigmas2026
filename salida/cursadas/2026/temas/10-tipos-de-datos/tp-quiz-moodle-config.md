# Configuración Moodle 5 — Quiz TP 10: Tipos de Datos y Sistemas de Tipos

> Generado por Valeria (tp-designer) — 2026-06-03  
> Nivel: 4to año universitario  
> Referencia: `tp-quiz.gift` (30 preguntas)

---

## Banco de preguntas

| Campo | Valor |
|-------|-------|
| Archivo a importar | `tp-quiz.gift` |
| Formato | GIFT — encoding **UTF-8 sin BOM** |
| Categoría destino | `TP/10-tipos-de-datos` |
| Opción de importación | Tildar **"Get category from file"** para respetar `$CATEGORY:` |

### Procedimiento de importación

1. Curso → **More** → **Question banks** → seleccionar el banco del curso.
2. Clic en **Import** → Format: **GIFT format**.
3. Seleccionar `tp-quiz.gift`.
4. Tildar **"Get category from file"** (respeta el `$CATEGORY: TP/10-tipos-de-datos` del archivo).
5. Clic **Import**. Verificar que 30 preguntas queden en estado **Ready** (no Draft).
6. Si alguna pregunta queda en **Draft**, revisarla en el editor antes de agregar al quiz.

---

## Actividad Quiz — Configuración recomendada

| Campo Moodle | Valor sugerido | Notas |
|-------------|---------------|-------|
| **Nombre** | `TP 10 — Tipos de Datos y Sistemas de Tipos` | Visible para el alumno |
| **Descripción** | `Quiz teórico-práctico. Cubre tipos primitivos, compuestos, punteros, null safety y sistemas de tipos (Módulo VII).` | Texto corto, informativo |
| **Intentos permitidos** | `1` | Evaluación parcial. Cambiar a `3` si es formativo. |
| **Método de calificación** | `Highest grade` | Si se permiten múltiples intentos. |
| **Tiempo límite** | `60 minutos` | Aprox. 2 min por pregunta para nivel universitario 4to año. |
| **When time expires** | `Open attempts are submitted automatically` | Evita que queden intentos abiertos. |
| **Navegación** | `Free** | Los alumnos pueden ir y volver entre preguntas. Cambiar a `Sequential` si se quiere evitar que revisen preguntas anteriores. |
| **Comportamiento de preguntas** | `Deferred feedback` | No muestra si es correcto durante el intento. Apropiado para examen. Para práctica guiada usar `Interactive with multiple tries`. |
| **Shuffle dentro de preguntas** | `Sí` | Aleatoriza el orden de las opciones dentro de cada pregunta. |
| **Shuffle de preguntas** | `Sí` | Aleatoriza el orden de las 30 preguntas. Reduce copia entre alumnos. |

---

## Puntaje

| Campo | Valor |
|-------|-------|
| **Calificación máxima** | `100` |
| **Puntaje por pregunta** | `3.33` (uniforme, aproximado) o fijar a `3` y calificación máxima `90` para números enteros. |
| **Penalización por intento fallido** | `0` (deferred feedback — no aplica penalización por intento dentro de una pregunta). |

> **Nota:** Con 30 preguntas a 3.33 puntos cada una ≈ 100 puntos. Alternativamente, usar 30 preguntas × 3 puntos \= 90 puntos como máximo y escalar en la grade book del curso.

---

## Review options (opciones de revisión para el alumno)

Configurar las tres franjas en Moodle:

| Qué muestra | Inmediatamente después | Mientras está abierto | Después del cierre |
|-------------|----------------------|-----------------------|-------------------|
| El intento | ✅ | ✅ | ✅ |
| Si es correcto | ❌ | ❌ | ✅ |
| Puntos | ✅ | ✅ | ✅ |
| Feedback específico (por opción) | ❌ | ❌ | ✅ |
| Feedback general (`####`) | ❌ | ❌ | ✅ |
| Respuesta correcta | ❌ | ❌ | ✅ |

> **Razón:** Durante el período de evaluación (mientras está abierto) el alumno solo ve su puntaje total, no las respuestas correctas. Después del cierre del quiz, puede ver todas las correcciones con feedback para aprender de los errores.

---

## Agregar preguntas al quiz

1. Crear la actividad Quiz con la configuración anterior.
2. En la actividad: **Edit quiz** → **Add** → **From question bank**.
3. Seleccionar la categoría `TP/10-tipos-de-datos`.
4. Seleccionar las 30 preguntas → **Add selected questions to the quiz**.
5. Verificar que el orden es aleatorio (shuffle activado).
6. **Save** y verificar la vista previa con una pregunta.

---

## Distribución de preguntas por bloque

| Bloque | Preguntas | Temas cubiertos |
|--------|-----------|----------------|
| Bloque 1 — Primitivos y Ordinales | Q01–Q07 | Definición de tipo, `number`/IEEE 754, `bigint`, `boolean`/`char`, enums, equivalencia estructural, subrangos |
| Bloque 2 — Agregación y Colecciones | Q08–Q14 | Strings, taxonomía de arrays, row-major, jagged, `Map` vs `Record`, shallow copy, discriminated unions |
| Bloque 3 — Punteros, Null Safety, Recursivos | Q15–Q20 | Dangling pointer, GC/reference counting, referencias vs. punteros, tipos recursivos, operadores `?.`/`??`, null safety opt-in |
| Bloque 4 — Sistemas de Tipos y Polimorfismo | Q21–Q28 | Strong typing, type erasure, sobrecarga ad-hoc, generics con constraints, subtipo/LSP, branded types, varianza, LSP |
| Bloque 5 — Síntesis | Q29–Q30 | Límites del type erasure, tradeoffs Result type vs. excepciones |

---

## Notas importantes para el docente

- **Las preguntas son solo el banco.** La actividad Quiz con tiempo límite, intentos, navegación y review options se configura manualmente en Moodle siguiendo esta guía.
- **Estado Ready obligatorio.** Las preguntas en estado Draft no pueden agregarse al quiz. Verificar después de la importación.
- **Preguntas con código.** Todas las preguntas que contienen código usan `[markdown]` y `<pre><code>...</code></pre>`. Verificar que Moodle renderice correctamente el markdown en la vista previa antes de publicar.
- **Course vs. Quiz question bank.** Si se importa al course question bank, las preguntas pueden reutilizarse en otros quizzes. Si se importa directamente al quiz question bank, son privadas de este quiz. Se recomienda importar al **course question bank** para reutilización futura.
- **Contraseña opcional.** Para exámenes presenciales, configurar una contraseña en la sección **Extra restrictions on attempts** y comunicarla en el momento del examen.
- **Safe Exam Browser opcional.** Para mayor control, configurar SEB en la sección **Browser security**.
