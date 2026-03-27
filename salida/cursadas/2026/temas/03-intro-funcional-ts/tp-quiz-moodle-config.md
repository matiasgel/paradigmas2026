# Configuración Moodle 5 — Quiz TP 03

## Banco de preguntas

| Campo | Valor |
|-------|-------|
| **Archivo** | `tp-quiz.gift` |
| **Encoding** | UTF-8 sin BOM |
| **Categoría raíz** | `TP/03-intro-funcional-ts` |
| **Subcategorías** | 7: A-historia, B-modelo, C-funciones-puras, D-inmutabilidad, E-transparencia, F-map-filter-reduce, G-clojure |
| **Preguntas totales** | 60 |
| **Formato de importación** | GIFT |
| **En importación** | Activar `Get category from file` para respetar `$CATEGORY:` |

---

## Actividad Quiz

| Setting | Valor | Notas |
|---------|-------|-------|
| **Nombre** | TP 03 — Introducción a Programación Funcional con TypeScript | |
| **Descripción** | Quiz evaluativo — 60 preguntas MC sobre paradigma funcional, TypeScript y Clojure | Mostrar en página del curso |
| **Intentos permitidos** | 1 | Evaluación sumativa |
| **Método de calificación** | Highest grade | Con 1 intento, no aplica diferencia |
| **Tiempo límite** | 90 minutos | ~1.5 min/pregunta |
| **Navegación** | Free | El alumno puede ir y volver entre preguntas |
| **Comportamiento** | Deferred feedback | Sin pistas durante el intento — feedback al final |
| **Shuffle dentro de preguntas** | Sí | Las opciones se mezclan en cada intento |
| **Shuffle de preguntas** | Sí | El orden de preguntas varía entre alumnos |
| **Puntaje por pregunta** | 1.00 | Uniforme |
| **Puntaje máximo** | 60.00 | |
| **Calificación para aprobar** | 36.00 | 60% del total (ajustar según criterio) |

---

## Review Options sugeridas

| Momento | Intento | Si es correcto | Puntos | Feedback específico | Feedback general | Respuesta correcta |
|---------|---------|----------------|--------|--------------------|-----------------|--------------------|
| **Inmediatamente después** | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Mientras el quiz está abierto** | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Después del cierre** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

> **Nota:** Mostrar las respuestas correctas solo después del cierre previene que los primeros alumnos compartan las respuestas con los que aún no rindieron.

---

## Procedimiento de importación en Moodle 5

### Paso 1 — Importar las preguntas al banco

1. Ir al curso → **More** → **Question banks** (o **Banco de preguntas**)
2. Clic en **Import** (o **Importar**)
3. Formato: **GIFT format**
4. Encoding: **UTF-8** (verificar que esté seleccionado)
5. Tildar **Get category from file** para crear las subcategorías automáticamente
6. Seleccionar o arrastrar el archivo `tp-quiz.gift`
7. Clic en **Import**
8. Verificar que se importaron las **60 preguntas** y las **7 categorías**
9. Verificar que todas las preguntas están en estado **Ready** (no Draft)

### Paso 2 — Crear la actividad Quiz

1. En el curso, activar **Modo edición**
2. **Agregar actividad** → **Quiz** (cuestionario)
3. Configurar los settings según la tabla anterior:
   - General: nombre, descripción
   - Timing: tiempo límite 90 min
   - Grade: intentos 1, método highest, calificación máxima 60
   - Layout: navegación free
   - Question behaviour: deferred feedback, shuffle sí
   - Review options: según tabla anterior
4. **Guardar y mostrar**

### Paso 3 — Agregar preguntas al Quiz

1. En la página del quiz → **Edit quiz** (o **Editar cuestionario**)
2. Clic en **Add** → **from question bank** (o **del banco de preguntas**)
3. Seleccionar la categoría `TP/03-intro-funcional-ts` (con "incluir subcategorías")
4. Seleccionar las 60 preguntas
5. Clic en **Add selected questions to the quiz**
6. Verificar que el puntaje máximo sea **60.00**
7. Opcionalmente, agregar saltos de página cada 10 preguntas para mejorar la UX

---

## Notas importantes

- **Moodle separa banco de preguntas de actividad Quiz.** El GIFT importa preguntas al banco; la actividad Quiz se configura por separado con sus propios settings.
- **Las preguntas Draft no se pueden agregar al quiz.** Si alguna pregunta quedó Draft después de la importación, cambiarla a Ready antes de agregarla.
- **Las preguntas del course question bank pueden reutilizarse** entre múltiples quizzes del mismo curso. Las del quiz question bank son privadas de ese quiz.
- **El encoding debe ser UTF-8** (no ANSI ni Latin-1). El archivo fue generado en UTF-8 sin BOM.
- **Shuffle de opciones:** Moodle mezcla las opciones de cada pregunta en cada intento. Esto reduce la copia entre alumnos.
- **El feedback específico por alternativa** se muestra después del intento según las Review Options configuradas. Cada opción incorrecta explica por qué es incorrecta.
- **El feedback general (####)** aparece en 15 de las 60 preguntas, proporcionando explicaciones extendidas para las preguntas más complejas.

---

## Distribución de preguntas por categoría

| Categoría | Preguntas | Contenido |
|-----------|-----------|-----------|
| A — Historia y fundamentos | Q01–Q10 (10) | Entscheidungsproblem, Church, Turing, Tesis C-T, lenguajes |
| B — Modelo funcional | Q11–Q18 (8) | Cómputo por reescritura, β-reducción, paralelización |
| C — Funciones puras | Q19–Q30 (12) | Definición, identificación, efectos colaterales, testing |
| D — Inmutabilidad | Q31–Q38 (8) | const, as const, spread, Clojure, structural sharing |
| E — Transparencia referencial | Q39–Q44 (6) | Definición, sustitución, optimizaciones, relación pilares |
| F — map/filter/reduce | Q45–Q56 (12) | Evaluación, trazas, pipe, composición, restricciones |
| G — Clojure | Q57–Q60 (4) | Sintaxis, funciones, ->> macro, comparativa TS |

---

*Documento generado por Aux. Valeria (tp-designer) — EDU Academic Course Production Suite*
*Tema 03 — Paradigmas y Lenguajes de Programación 2026     —, 2026-03-27*
