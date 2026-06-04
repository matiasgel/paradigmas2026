# Task: GIFT Validator

**Module:** edu
**Type:** reusable-task
**Owner:** tp-designer (Valeria)
**Version:** 1.0.0 — basado en MoodleDocs 5.1 GIFT format + moodle-quiz-moodle5.md

---

## Propósito

Validar un archivo GIFT antes de su importación en Moodle para detectar errores que
bloquean la importación o generan preguntas corruptas. Este task puede invocarse:

- Desde `create-tp-quiz/workflow.md` (Paso 2.5, antes de exportar).
- Standalone desde `/edu-validate-gift`.
- Manualmente por Valeria cuando el docente pide revisar un GIFT existente.

---

## Input

- Ruta del archivo a validar: `{gift_file_path}` (por defecto: `{topic_folder}/tp-quiz.gift`)
- O contenido del GIFT pegado directamente en el chat.

---

## Reglas de validación

### GRUPO A — Errores críticos (bloquean importación o corrompen preguntas)

| ID | Regla | Descripción |
|----|-------|-------------|
| A1 | UTF-8 sin BOM | Advertir si hay indicios de BOM (primeros bytes EF BB BF). El BOM puede corromper la primer pregunta o el primer `$CATEGORY:`. |
| A2 | Línea en blanco entre preguntas | Debe haber al menos una línea vacía entre el cierre `}` de una pregunta y el inicio de la siguiente. Error si no existe. |
| A3 | Título presente | Toda pregunta debe tener `::titulo::` antes del enunciado. Sin título Moodle no puede importar correctamente. |
| A4 | Título no vacío | `::::` (título vacío) no está permitido. |
| A5 | Llaves balanceadas | Cada `{` de bloque de respuestas debe tener su `}` de cierre en la misma pregunta. |
| A6 | MC simple — exactamente 1 correcta | Para preguntas sin pesos (`%`), debe haber exactamente un `=` y al menos un `~`. Si hay 0 `=` o más de 1 `=` en MC, es error. |
| A7 | Caracteres reservados sin escapar | Los caracteres `~ = # { } :` usados como texto literal deben ir precedidos de `\`. Detectar patrones sospechosos donde aparezcan sin contexto de sintaxis. |
| A8 | Pregunta vacía | El enunciado entre `::titulo::` y `{` no puede estar vacío. |
| A9 | True/False malformado | Las respuestas T/F deben ser exactamente `{TRUE}`, `{FALSE}`, `{T}` o `{F}`. Otros valores son error. |

### GRUPO B — Errores de pesos percentuales (generan preguntas con calificación incorrecta)

| ID | Regla | Descripción |
|----|-------|-------------|
| B1 | Pesos válidos de Moodle | Moodle solo acepta los porcentajes de su lista interna. Si el porcentaje no está en la lista, Moodle puede fallar la importación o redondear silenciosamente. |
| B2 | Suma de pesos positivos ≤ 100% | En MC múltiple, la suma de todos los `%N%` positivos no debe superar 100. |
| B3 | No mezclar `=` y `%N%` | Una pregunta no puede tener al mismo tiempo `=` (MC simple) y `~%N%` (MC múltiple). Moodle entra en estado indefinido. |

**Lista de porcentajes válidos de Moodle (positivos y negativos):**
```
100, 90, 83.33333, 80, 75, 70, 66.66667, 60, 50, 40, 33.33333, 30, 25, 20,
16.66667, 14.28571, 12.5, 11.11111, 10, 5, 0
y sus negativos: -5, -10, -11.11111, -12.5, -14.28571, -16.66667, -20, -25,
-30, -33.33333, -40, -50, -60, -66.66667, -70, -75, -80, -83.33333, -90, -100
```
> Nota sobre tercios: usar `33.33333` (7 dígitos), no `33.33` ni `33`. Para dos tercios: `66.66667`.

### GRUPO C — Advertencias (pueden causar problemas pedagógicos o de UX)

| ID | Regla | Descripción |
|----|-------|-------------|
| C1 | MC simple sin distractores suficientes | Menos de 3 `~` en MC es técnicamente válido pero debilita la pregunta. Advertir. |
| C2 | Inconsistencia de formato de texto | Mezclar `[html]` y `[markdown]` en el mismo archivo sin motivo claro. Advertir. |
| C3 | Feedback sin valor pedagógico aparente | Feedback presente pero idéntico en varias preguntas consecutivas. Advertir. |
| C4 | $CATEGORY malformado | `$CATEGORY:` sin ruta después, o con espacios antes del `:`. Advertir. |
| C5 | Titulo duplicado | Dos preguntas con el mismo `::titulo::`. Moodle puede sobreescribir. Advertir. |
| C6 | Pregunta sin feedback en quiz formativo | Si el quiz es formativo y la pregunta no tiene `#` ni `####`, advertir que el alumno no recibirá orientación. |
| C7 | `[markdown]` ausente en pregunta con código | Si el enunciado contiene `<pre>`, `<code>`, o patrones de código (backtick, `function`, `class`, `:-`) pero NO tiene `[markdown]` --> advertencia. |
| C8 | Cierre HTML incorrecto | Si el enunciado contiene `</pre></code>` (orden incorrecto) --> advertencia. El correcto es `</code></pre>`. |
| C9 | Feedback truncado | Si el texto de feedback termina mid-word (sin punto, ?, !) --> advertencia. |

### GRUPO D -- Errores de encoding (bloquean importación con error PostgreSQL)

| ID | Regla | Descripción |
|----|-------|-------------|
| D1 | Em dash / en dash Unicode | Presencia de U+2014 (--) o U+2013 (-) en cualquier campo. PostgreSQL en el servidor Moodle puede rechazar con `ERROR: secuencia de bytes no válida para codificación UTF8: 0xe2 0x80`. Reemplazar por `--`. |
| D2 | Caracteres Unicode no-ASCII fuera del rango latin-1 | Presencia de superíndices (U+2070-U+2079), flechas (U+2192 ->), operador menos matemático (U+2212), puntos suspensivos (U+2026), comillas tipográficas (U+201C U+201D U+2018 U+2019). Reemplazar por equivalentes ASCII: `^N`, `->`, `-`, `...`, `"`. |
| D3 | BOM UTF-8 | Primeros bytes `EF BB BF`. Eliminar. |

### GRUPO E -- Errores de WAF/ModSecurity (bloquean processattempt.php con HTTP 403 Forbidden)

| ID | Regla | Descripción |
|----|-------|-------------|
| E1 | `console.log(` en bloque de código | Apache/ModSecurity en servidores Moodle bloquea el POST de `processattempt.php` cuando el cuerpo contiene `console.log(`. El texto de cada pregunta se incluye como campo oculto en el form de respuesta. Reemplazar por la expresión sola con comentario: `expr  // ¿qué retorna?`. |
| E2 | Otras llamadas JS peligrosas | `alert(`, `document.write(`, `eval(`, `innerHTML` en bloques de código activan las mismas reglas XSS del WAF. Mismo tratamiento que E1. |
| E3 | Métodos string/array OWASP CRS PL2 | `toUpperCase(`, `toLowerCase(` (regla 941200), `Math.abs(`, `Math.sqrt(`, `Math.random(`, `Math.floor(` y otros `Math.*` (regla 941210), `toFixed(`, `reduce(` (reglas custom frecuentes). Reemplazos seguros: `.trim()`, `.toPrecision()`, literales numéricos `3.14159`, bucles `for...of`. Afectan tanto bloques de código como texto de opciones y feedback. |

---

## Algoritmo de validación

```
PARA CADA pregunta en el archivo:
  1. Extraer bloque: desde ::titulo:: hasta cierre de }
  2. Detectar tipo: MC-simple | MC-múltiple | T/F | short-answer | numerical | essay | description
  3. Aplicar reglas del GRUPO A correspondientes al tipo
  4. Si tipo es MC-múltiple: aplicar reglas del GRUPO B
  5. Aplicar reglas del GRUPO C como advertencias
  6. Si BOM detectado al inicio del archivo: reportar A1 / D3 inmediatamente

EXTRA (sobre el archivo completo, no por pregunta):
  7. Escanear todo el contenido en busca de caracteres D1/D2 (Unicode no-ASCII problemático)
  8. Escanear bloques <pre><code> y texto de opciones/feedback en busca de patrones E1/E2/E3 (llamadas JS que activan WAF)

CONSOLIDAR resultados:
  - Errores críticos (A*, B*, D*, E*): listar con número de pregunta y descripción exacta del problema
  - Advertencias (C*): listar separadas
  - Preguntas OK: indicar cantidad

REPORTAR en formato:
  ✅ N pregunta(s) válidas
  ❌ M error(es) crítico(s) --> NO exportar hasta corregir
  ⚠️  K advertencia(s) --> revisar antes de publicar
```

---

## Formato de reporte

```
## Resultado de validación GIFT
**Archivo:** {gift_file_path}
**Fecha:** {fecha}

### Resumen
- ✅ Preguntas válidas: N
- ❌ Errores críticos: M (el archivo NO debe importarse hasta corregirlos)
- ⚠️  Advertencias: K

### Errores críticos
| # | Pregunta | ID regla | Descripción del problema | Corrección sugerida |
|---|----------|----------|--------------------------|---------------------|
| 1 | ::titulo-q01:: | A6 | No hay respuesta correcta (falta `=`) | Agregar `=` antes de la opción correcta |
| 2 | ::titulo-q03:: | B1 | Peso `%33%` inválido en Moodle | Cambiar a `%33.33333%` |
...

### Advertencias
| # | Pregunta | ID regla | Descripción |
|---|----------|----------|-------------|
...

### Correcciones aplicadas
(Si el docente autoriza, listar los fixes automáticos aplicados al archivo)
```

---

## Modo autofix

Si el usuario solicita `autofix: sí`, el validador puede corregir automáticamente:

- **Pesos redondeados** --> reemplazar por el valor más cercano de la lista Moodle.
  Regla: si la diferencia es < 0.01, corregir automáticamente; si es mayor, reportar y pedir confirmación.
- **BOM** --> eliminar del archivo si se puede editar.
- **Líneas en blanco faltantes** --> agregar entre preguntas automáticamente.
- **Em/en dashes (D1)** --> reemplazar `--` y `-` por `--` automáticamente.
- **Otros Unicode D2** --> reemplazar superíndices, flechas Unicode, elipsis y operador menos matemático por equivalentes ASCII.
- **Llamadas WAF E1/E2** --> comentar el wrapper: `console.log(expr)` --> `expr  // ¿qué retorna?`.
- **Métodos WAF E3** --> sustituir por equivalente seguro: `toUpperCase()` --> `trim()`, `Math.PI` --> `3.14159`, `reduce(...)` --> bucle `for...of`, `toFixed(N)` --> `toPrecision(N+2)`.

Los fixes se reportan en la sección "Correcciones aplicadas".

**NO autofix automático para:**
- Agregar/quitar respuestas correctas (A6) --> decisión pedagógica del docente.
- Escapar caracteres (A7) --> requiere interpretación semántica.
- Títulos vacíos o duplicados --> requiere contexto del docente.

---

## Invocación desde create-tp-quiz/workflow.md

Cuando este task es llamado desde el workflow:

1. Recibir el contenido generado en Step 3A (todavía en memoria, antes de escribir a disco).
2. Ejecutar validación completa.
3. Si hay errores críticos (A*, B*): **NO generar el archivo**. Mostrar el reporte y volver a Step 3A para corregir.
4. Si solo hay advertencias (C*): mostrar el reporte, preguntar al docente si desea continuar o corregir.
5. Si todo OK: confirmar y proceder a escribir `tp-quiz.gift`.

---

## Referencias normativas

- MoodleDocs 5.1 — `GIFT format`
- MoodleDocs 5.1 — `Import questions`
- `{project-root}/docs/moodle-quiz-moodle5.md`
- `{project-root}/docs/Formato GIFT - MoodleDocs.html`
- `{project-root}/docs/Formato GIFT con medios - MoodleDocs.html`
