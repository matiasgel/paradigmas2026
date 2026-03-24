# Workflow: Create TP Quiz

**Module:** edu
**Phase:** 3 — Producción de Temas
**Owner Agent:** tp-designer (Valeria)
**Trigger:** Step 5.5-B del topic-cycle (tipo `quiz-moodle` o `quiz-google`) o `/edu-create-autograde-repo` con tipo quiz

---

## Overview

Genera los artefactos de quiz a partir de `tp.md`.
En Moodle hay que separar dos capas distintas:

1. **Banco de preguntas**: se importa con GIFT a una categoría del question bank.
2. **Actividad Quiz**: se configura dentro de Moodle con sus propios ajustes de tiempo, intentos, navegación, revisión y feedback.

Por lo tanto, este workflow **no pretende serializar toda la actividad Quiz dentro del archivo GIFT**, porque Moodle no funciona así. En su lugar genera:

| Plataforma | Output | Propósito |
|-----------|--------|-----------|
| Moodle | `tp-quiz.gift` + `tp-quiz-moodle-config.md` | Banco de preguntas GIFT UTF-8 + guía exacta para crear/configurar la actividad Quiz en Moodle 5 |
| Google Classroom / Forms | `tp-quiz-forms.md` + `tp-quiz-forms-script.js` | Estructura del quiz + Apps Script para Google Forms |

Referencias normativas usadas en este workflow:
- MoodleDocs 5.1 `GIFT format`
- MoodleDocs 5.1 `Import questions`
- MoodleDocs 5.1 `Question banks`
- MoodleDocs 5.1 `Quiz activity`
- MoodleDocs 5.1 `Quiz settings`

---

## Preconditions

- `_edu/active-topic.yaml` debe existir.
- `{topic_folder}/tp.md` debe existir.
- `{topic_folder}/topic.yaml` debe existir y contener `tp_type`.
- El `tp.md` debe contener consignas de evaluación estructurables como quiz.
- Si alguna precondition falla → informar y STOP.

---

## Step 0: Initialize

1. Load `{project-root}/_edu/config.yaml` → store all fields.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}`.
3. Load `{project-root}/{topic_folder}/topic.yaml` → store all fields.
4. Load `{project-root}/{topic_folder}/tp.md`.
5. Determinar plataforma destino desde `tp_type`.
6. Detectar preguntas candidatas a quiz y clasificarlas por tipo real:
  - multiple choice de respuesta única
  - multiple choice de respuesta múltiple
  - verdadero/falso
  - short answer solo si el docente lo pidió explícitamente
7. Si el TP no está estructurado en un formato evaluable → informar qué falta y STOP.

---

## Step 1: Elicitar configuración pedagógica y operativa

Preguntar al docente y esperar respuesta:

1. **Título visible del cuestionario**
  Sugerido: `TP {topic_number} — {topic_name}`
2. **Categoría del banco de preguntas**
  Sugerido: `TP/{topic_number}-{topic_name_slug}`
3. **Modo de evaluación**
  Opciones sugeridas: práctica formativa / parcial corto / autoevaluación
4. **Cantidad de intentos permitidos en Moodle**
5. **Método de calificación si hay múltiples intentos**
  Opciones Moodle: `highest`, `average`, `first`, `last`
6. **Tiempo límite de la actividad Quiz**
  En minutos, `0` = sin límite
7. **Navegación**
  `free` o `sequential`
8. **Comportamiento de preguntas**
  Sugerido: `deferred feedback` para examen tradicional, `interactive with multiple tries` para práctica guiada
9. **Shuffle de opciones dentro de cada pregunta**
  sí / no
10. **Mostrar right answers y feedback al alumno**
  Definir por franja de revisión: inmediatamente, mientras siga abierto, después del cierre
11. **Puntaje por pregunta**
  uniforme o específico por consigna
12. **Si habrá feedback específico por alternativa**
  sí / no

Mostrar resumen y pedir confirmación.

---

## Step 2: Validar las preguntas antes de exportar

Para cada pregunta candidata, verificar:

- Tiene trazabilidad explícita a `tp.md` y a la cobertura de `minuta.md`.
- El enunciado es autosuficiente fuera del contexto del TP.
- Si es multiple choice simple:
  - exactamente 1 correcta
  - al menos 3 distractores plausibles
- Si es multiple choice múltiple:
  - los pesos parciales suman como máximo `100%`
  - las incorrectas tienen peso `0` o negativo si se quiere evitar marcar todo
- Si incluye símbolos GIFT reservados `~ = # { } :`, deben escaparse con `\`.
- Si requiere formato enriquecido, usar `[html]` o `[markdown]` de manera consistente.
- Debe haber una línea en blanco entre preguntas en el archivo final.

Si alguna pregunta falla, listar el problema y corregir antes de exportar.

---

## Step 2.5: Pre-validación de preguntas (tarea obligatoria antes de exportar)

> **Esta etapa es obligatoria.** Ninguna pregunta puede escribirse al archivo GIFT sin pasar esta validación.

Load `{project-root}/_edu/tasks/gift-validator.md` y aplicar **todas las reglas** sobre las
preguntas generadas en memoria (todavía no escritas a disco).

### Verificaciones obligatorias por pregunta

Para **cada pregunta candidata**, verificar en este orden:

1. **[A3] Tiene título** `::titulo::` presente y no vacío [A4].
2. **[A5] Llaves balanceadas** — el bloque `{ ... }` abre y cierra correctamente.
3. **[A8] Enunciado no vacío** — hay texto entre el título y el `{`.
4. **[A6] MC simple — exactamente 1 `=`** y al menos 1 `~` (sin pesos).
5. **[B1/B3] MC múltiple** — si usa `%N%`:
   - No mezclar con `=`.
   - Cada peso debe estar en la lista de valores válidos de Moodle.
   - Suma de pesos positivos ≤ 100%.
6. **[A9] T/F** — respuesta exactamente `{TRUE}`, `{FALSE}`, `{T}` o `{F}`.
7. **[A7] Caracteres reservados** — `~ = # { } :` como texto literal van escapados con `\`.
8. **[C5] Títulos únicos** — no repetir el mismo `::titulo::` en preguntas distintas.

**Para el archivo completo:**
- **[A2] Línea en blanco** entre cada par de preguntas consecutivas.
- **[C4] $CATEGORY:** formato correcto si presente.

### Resultado

Si hay **errores críticos (A*, B*):**
- Corregir en memoria ANTES de escribir al archivo.
- Si la corrección requiere decisión pedagógica (ej. A6: no hay correcta definida), reportar al docente y esperar instrucción. No proceder hasta resolver.

Si hay solo **advertencias (C*):**
- Mostrar al docente, preguntar si desea corregir o continuar.

Si todo OK → proceder a Step 3A.

**Formato del reporte de validación:**
```
## Validación GIFT — pre-exportación
✅ N pregunta(s) válidas
❌ M error(es) crítico(s) — corrigiendo antes de exportar...
⚠️  K advertencia(s) — consultar con docente

Detalle de errores:
[Q01 ::titulo:: ] A6 — Falta respuesta correcta (=). Sugerencia: marcar "..." como correcta.
[Q03 ::titulo:: ] B1 — Peso %33% inválido. Corrección automática: %33.33333%.
```

---

## Step 3A: Generar banco de preguntas Moodle en `tp-quiz.gift`

### Regla crítica

`tp-quiz.gift` representa **preguntas**, no la actividad Quiz completa.
Los parámetros como tiempo límite, intentos, review options, navegación, grade category y contraseña se documentan en `tp-quiz-moodle-config.md` para ser cargados luego en la actividad Quiz de Moodle.

### Formato base

```gift
// TP {topic_number}: {topic_name}
// Importar en Moodle 5: Banco de preguntas > Importar > Formato GIFT
// Encoding obligatorio: UTF-8 sin BOM

$CATEGORY: TP/{topic_number}-{topic_name_slug}

::TP{topic_number}-Q01::[markdown]{enunciado_pregunta_1} {
={opcion_correcta_1}#{feedback_correcto_1}
~{distractor_1_1}#{feedback_incorrecto_1a}
~{distractor_1_2}#{feedback_incorrecto_1b}
~{distractor_1_3}#{feedback_incorrecto_1c}
#### {feedback_general_1}
}

::TP{topic_number}-Q02::[markdown]{enunciado_pregunta_2} {
~%-50%{distractor_2_1}
~%50%{correcta_parcial_2a}
~%50%{correcta_parcial_2b}
~%-50%{distractor_2_2}
#### {feedback_general_2}
}
```

### Reglas obligatorias para Moodle GIFT

- El archivo debe guardarse como `UTF-8` y preferentemente **sin BOM**.
- Debe haber al menos una línea en blanco entre preguntas.
- `::titulo::` debe estar presente en todas las preguntas.
- `=` marca respuesta correcta en multiple choice simple.
- `~` marca respuesta incorrecta o alternativa ponderada.
- `#` agrega feedback específico de esa alternativa.
- `####` agrega feedback general de la pregunta.
- `[html]`, `[markdown]`, `[moodle]` o `[plain]` pueden prefijar el texto de la pregunta.
- `$CATEGORY:` puede cambiar la categoría de destino dentro del archivo.
- Si se usan porcentajes, Moodle valida contra su lista de grades importables; si no coincide exacto, el import puede fallar o redondear según `Match grades`.
- Para dividir en tercios usar `33.33333`, no `33` ni `33.33`.
- Los caracteres reservados `~ = # { } :` deben escaparse con `\` cuando se usan como texto literal.

### Criterios de generación para el módulo EDU

- Preferir `multiple choice` de respuesta única como formato por defecto.
- Usar `multiple choice` de respuesta múltiple solo si la consigna realmente lo exige.
- Incluir feedback específico solo cuando agrega valor pedagógico real.
- Incluir `feedback general` breve cuando el quiz sea formativo.
- Trazabilidad obligatoria en el título de la pregunta:
  - formato sugerido: `::TP{topic_number}-C{consigna_numero}-{slug_corto}::`
- No generar categorías ambiguas; usar una ruta jerárquica estable.

---

## Step 3B: Generar `tp-quiz-moodle-config.md`

Generar una guía operativa para crear la actividad Quiz en Moodle 5 usando las preguntas importadas.

Contenido mínimo:

```markdown
# Configuración Moodle 5 — Quiz TP {topic_number}

## Banco de preguntas
- Archivo: `tp-quiz.gift`
- Categoría sugerida: `TP/{topic_number}-{topic_name_slug}`
- En importación: activar `Get category from file` si se quiere respetar `$CATEGORY:`

## Actividad Quiz
- Nombre: {quiz_title}
- Intentos permitidos: {attempts_allowed}
- Método de calificación: {grading_method}
- Tiempo límite: {time_limit}
- Navegación: {navigation_method}
- Comportamiento: {question_behaviour}
- Shuffle dentro de preguntas: {shuffle_answers}

## Review options sugeridas
- Immediately after: {review_immediate}
- Later while quiz is still open: {review_open}
- After the quiz is closed: {review_closed}

## Procedimiento
1. Curso > More > Question banks.
2. Import > GIFT.
3. Seleccionar `tp-quiz.gift`.
4. Si corresponde, tildar `Get category from file`.
5. Crear la actividad Quiz.
6. Configurar settings según esta guía.
7. Edit quiz > Add > from question bank.
8. Seleccionar la categoría importada.
```

Incluir además notas importantes:

- Moodle crea la actividad Quiz en dos pasos: primero settings, luego agregar preguntas.
- Los tiempos, intentos, contraseña, review options y navegación no viajan dentro del GIFT.
- Las preguntas `Draft` no se pueden agregar al quiz; deben quedar `Ready`.
- Las preguntas del course shared question bank pueden reutilizarse entre cursos; las del quiz question bank son privadas del quiz.

---

## Step 3C: Generar quiz para Google Forms

Generar dos archivos:

### `tp-quiz-forms.md`

Documento legible con:

- título
- objetivos del quiz
- preguntas
- opciones
- correcta marcada
- puntaje
- feedback si aplica
- nota explícita de que Google Forms no soporta tiempo límite nativo

### `tp-quiz-forms-script.js`

Script Apps Script con:

- `form.setIsQuiz(true)`
- `form.setCollectEmail(true)` cuando el docente quiera trazabilidad
- `form.setLimitOneResponsePerUser(true)` si corresponde
- una pregunta por `MultipleChoiceItem` o `CheckboxItem` según el caso
- `setPoints(...)`

---

## Step 4: Output Summary

### Moodle

```text
Quiz Moodle preparado en:
- {topic_folder}/tp-quiz.gift
- {topic_folder}/tp-quiz-moodle-config.md

Preguntas: {N}
Categoría: {question_category}
Formato de importación: GIFT UTF-8

Importante:
- El GIFT importa preguntas al banco.
- La actividad Quiz se configura aparte en Moodle 5.
```

### Google

```text
Quiz Google preparado en:
- {topic_folder}/tp-quiz-forms.md
- {topic_folder}/tp-quiz-forms-script.js
```

---

## Output Files

| Archivo | Plataforma | Descripción |
|---------|-----------|-------------|
| `tp-quiz.gift` | Moodle | Banco de preguntas importable en GIFT UTF-8 |
| `tp-quiz-moodle-config.md` | Moodle | Guía de configuración de la actividad Quiz en Moodle 5 |
| `tp-quiz-forms.md` | Google | Estructura legible del quiz |
| `tp-quiz-forms-script.js` | Google | Apps Script para crear el Google Form |
