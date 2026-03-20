# Configuración Moodle 5 — Quiz TP 02: Sintaxis y Semántica

> **Agente:** Aux. Valeria 📝 (tp-designer)
> **Fecha:** 2026-03-20
> **Archivo de preguntas:** `tp-quiz.gift`

---

## Banco de preguntas

| Campo | Valor |
|-------|-------|
| **Archivo** | `tp-quiz.gift` |
| **Categoría sugerida** | `TP/02-sintaxis-semantica` |
| **Formato de importación** | GIFT |
| **Encoding obligatorio** | UTF-8 **sin BOM** |
| **Total de preguntas** | 40 preguntas de opción múltiple |
| **Activar al importar** | `Get category from file` (para respetar la directiva `$CATEGORY:` del GIFT) |

---

## Actividad Quiz — Configuración

| Campo Moodle | Valor sugerido | Notas |
|---|---|---|
| **Nombre** | `TP 02 — Sintaxis y Semántica: BNF, EBNF y Análisis` | Visible para los alumnos |
| **Descripción** | `Quiz de práctica sobre BNF, EBNF, derivaciones y análisis de gramáticas formales. 40 preguntas de opción múltiple.` | Mostrar en la página del curso |
| **Intentos permitidos** | `3` | Formativo — permite mejorar |
| **Método de calificación** | `highest` | Se registra la mejor nota |
| **Tiempo límite** | `60 minutos` | Suficiente para práctica formativa |
| **Navegación** | `free` | El alumno puede ir y volver |
| **Comportamiento de preguntas** | `interactive with multiple tries` | Feedback inmediato — modo práctica |
| **Shuffle de preguntas** | Sí | Aleatorizar orden entre intentos |
| **Shuffle de opciones** | Sí | Aleatorizar opciones dentro de cada pregunta |
| **Puntaje total** | 40 puntos (1 punto por pregunta uniforme) | |
| **Calificación de aprobación** | 28/40 (70%) | Ajustar según criterio de la cátedra |

---

## Review options (revisión por franja)

| Franja | Respuesta correcta | Feedback específico | Feedback general | Puntaje |
|--------|-------------|---------------------|-----------------|---------|
| **Inmediatamente después** | No | Sí | Sí | Sí |
| **Mientras el quiz está abierto** | No | Sí | Sí | Sí |
| **Después del cierre del quiz** | Sí | Sí | Sí | Sí |

---

## Procedimiento de carga en Moodle 5

### Paso 1: Importar el banco de preguntas

1. Ingresar al curso en Moodle 5.
2. Ir a **More** (o **Más**) → **Question banks** (o **Banco de preguntas**).
3. En el banco de preguntas, hacer clic en **Import** (Importar).
4. Seleccionar el formato **GIFT**.
5. Seleccionar el archivo `tp-quiz.gift`.
6. **Importante:** Tildar la opción `Get category from file` para que las preguntas queden en la categoría `TP/02-sintaxis-semantica` como define el archivo.
7. Verificar que el encoding sea **UTF-8**.
8. Hacer clic en **Import** y confirmar.
9. Revisar el resumen de importación: deben quedar **40 preguntas** en estado `Ready`.

> ⚠️ **Si alguna pregunta queda en estado `Draft`:** Editarla individualmente y cambiar el estado a `Ready`. Las preguntas en Draft no pueden agregarse al quiz.

### Paso 2: Crear la actividad Quiz

1. Ir al curso → **Turn editing on**.
2. En la sección correspondiente al Tema 02, hacer clic en **Add an activity or resource**.
3. Seleccionar **Quiz**.
4. Completar los campos según la sección **Actividad Quiz — Configuración** de este documento.
5. En la sección **Review options**, configurar según la tabla de revisión.
6. Hacer clic en **Save and display**.

### Paso 3: Agregar preguntas al quiz

1. En la página del quiz recién creado, hacer clic en **Edit quiz**.
2. Hacer clic en **Add** → **From question bank**.
3. Seleccionar la categoría `TP/02-sintaxis-semantica`.
4. Seleccionar **todas las preguntas** (40).
5. Hacer clic en **Add selected questions to the quiz**.
6. Verificar que el puntaje máximo sea **40**.

### Paso 4: Verificación final

- [ ] 40 preguntas agregadas al quiz.
- [ ] Puntaje total: 40 puntos.
- [ ] Tiempo límite configurado: 60 minutos.
- [ ] Shuffle activado para preguntas y opciones.
- [ ] Calificación de aprobación configurada.
- [ ] Hacer un **preview** del quiz como estudiante para verificar la visualización.

---

## Notas importantes

### Separación quiz / banco de preguntas

Moodle crea la actividad Quiz en dos pasos:
1. **Settings**: nombre, tiempo, intentos, revisión, etc.
2. **Edit quiz**: agregar preguntas desde el banco.

Los parámetros de tiempo límite, intentos, contraseña, review options y navegación **no viajan dentro del archivo GIFT** — se configuran en la actividad Quiz de Moodle manualmente.

### Preguntas reutilizables

Las preguntas en el **course shared question bank** (`TP/02-sintaxis-semantica`) pueden reutilizarse en otros quizzes del mismo curso. Las preguntas agregadas directamente desde un quiz (sin pasar por el banco compartido) son privadas de ese quiz.

### Ponderación negativa (opcional)

El archivo GIFT no incluye ponderación negativa (penalización por respuesta incorrecta). Si el docente desea agregar penalización:
- En "Behaviour", configurar `Apply penalty` en la sección de revisión.
- El valor de penalización por defecto de Moodle es 1/n (donde n es el número de opciones).

### Comportamiento con `interactive with multiple tries`

Con este comportamiento, el alumno puede intentar cada pregunta varias veces durante el intento:
- 1er intento correcto: 100% del puntaje.
- 2do intento correcto: descuento configurado (sugerido: 33%).
- 3er intento correcto: descuento mayor (sugerido: 66%).

Alternativa más estricta: usar `Deferred feedback` si el quiz se usa como parcial.

---

## Distribución de preguntas por sección

| Sección | Preguntas | Contenido |
|---------|-----------|-----------|
| A — Análisis Léxico | Q01–Q05 | Tokens, lexemas, función del lexer |
| B — Sintaxis vs. Semántica | Q06–Q10 | Clasificación de errores |
| C — BNF Conceptos | Q11–Q17 | Terminales, no-terminales, tupla gramatical |
| D — BNF Derivaciones | Q18–Q24 | Derivaciones paso a paso, árboles |
| E — Ambigüedad | Q25–Q28 | Detección y resolución de ambigüedad |
| F — EBNF | Q29–Q36 | Metasímbolos, equivalencia con BNF |
| G — Aplicaciones | Q37–Q40 | Python, tsc, constrained decoding |
