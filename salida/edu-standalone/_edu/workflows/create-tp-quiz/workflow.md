# Workflow: Create TP Quiz

**Module:** edu
**Phase:** 3 — Producción de Temas
**Owner Agent:** tp-designer (Valeria)
**Trigger:** Step 5.5-B del topic-cycle (tipo `quiz-moodle` o `quiz-google`) o `/edu-create-autograde-repo` con tipo quiz

---

## Overview

Genera los archivos de quiz a partir del `tp.md` del tema.
Soporta dos plataformas de destino:

| Plataforma | Output | Formato |
|-----------|--------|---------|
| Moodle | `tp-quiz.gift` | GIFT (General Import Format Template) — importable directo en Moodle |
| Google Classroom / Forms | `tp-quiz-forms.md` + `tp-quiz-forms-script.js` | Markdown estructurado + Apps Script para crear el Form automáticamente |

---

## Preconditions

- `_edu/active-topic.yaml` debe existir.
- `{topic_folder}/tp.md` debe existir con preguntas de tipo multiple choice definidas.
- Si alguna precondition falla → informar y STOP.

---

## Steps

### Step 0: Initialize

1. Load `{project-root}/_edu/config.yaml` → store all fields.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}`.
3. Load `{project-root}/{topic_folder}/tp.md` → extraer preguntas, opciones y respuestas correctas.
4. Determinar plataforma destino (viene de topic.yaml `tp_type`: `quiz-moodle` o `quiz-google`).

---

### Step 1: Elicitar Configuración del Quiz

Preguntar al docente (esperar respuesta antes de continuar):

1. **Título del quiz** (sugerido: "TP {topic_number} — {topic_name}")
2. **Tiempo límite** (en minutos; sugerido: 30 minutos; 0 = sin límite)
3. **Intentos permitidos** (sugerido: 1)
4. **Puntaje por pregunta correcta** (sugerido: igual para todas; o el docente especifica por pregunta)
5. **Penalización por respuesta incorrecta** (sugerido: 0 — sin penalización)
6. **Mostrar respuestas correctas al alumno** después de completar: sí / no

Mostrar resumen y pedir confirmación antes de generar.

---

### Step 2: Verificar y Completar Preguntas del tp.md

Revisar que cada consigna del tp.md marcada como multiple choice tenga:
- Enunciado claro
- Exactamente 1 respuesta correcta marcada (o indicada)
- Al menos 3 opciones incorrectas (distractores)

Si alguna pregunta está incompleta → mostrar el listado y pedir que el docente las complete antes de continuar.

---

### Step 3A: Generar `tp-quiz.gift` (Moodle)

Formato GIFT — importable desde Moodle en: Banco de preguntas → Importar → Formato GIFT.

```
// TP {topic_number}: {topic_name}
// Importar en: Moodle → Banco de preguntas → Importar → Formato GIFT
// Encoding: UTF-8

$CATEGORY: TP{topic_number}-{topic_name_slug}

::Pregunta 1::[html]<p>{enunciado_pregunta_1}</p> {
  ={opcion_correcta_1}
  ~{distractor_1_1}
  ~{distractor_1_2}
  ~{distractor_1_3}
}

::Pregunta 2::[html]<p>{enunciado_pregunta_2}</p> {
  ={opcion_correcta_2}
  ~{distractor_2_1}
  ~{distractor_2_2}
  ~{distractor_2_3}
}
```

**Reglas GIFT:**
- Encoding obligatorio: UTF-8
- `=` prefija la respuesta correcta
- `~` prefija cada distractor
- `[html]` permite HTML en el enunciado (tildes, código, negrita)
- Para penalización: `~%XX%{distractor}` donde XX es porcentaje negativo (ej: `~%-25%{Incorrecta}`)
- Comentarios con `//`
- El campo `name_slug` es {topic_name} en minúsculas sin espacios ni tildes

**Trazabilidad:** Cada pregunta GIFT DEBE tener el número de consigna de tp.md en el título (`::Pregunta N - ...::`)

---

### Step 3B: Generar quiz para Google Classroom / Forms

Generar dos archivos:

#### `tp-quiz-forms.md` — estructura legible para el docente

```markdown
# Quiz: TP {topic_number} — {topic_name}
**Plataforma:** Google Forms (importar como quiz)
**Tiempo límite:** {tiempo_limite} min | **Intentos:** {intentos}

---

## Pregunta 1 — {descripción breve} *(Consigna {N} tp.md)*
{enunciado_completo}

- ( ) {opcion_A}
- (✓) {opcion_correcta}
- ( ) {opcion_B}
- ( ) {opcion_C}

**Puntos:** {puntos} | **Feedback correcto:** {feedback_si_aplica}

---
```

#### `tp-quiz-forms-script.js` — Apps Script para crear el Form automáticamente

```javascript
// Google Apps Script — Crear quiz automáticamente
// Instrucciones: script.google.com → Nuevo proyecto → Pegar este código → Ejecutar createQuiz()
// Requiere permisos de Google Forms.

function createQuiz() {
  const form = FormApp.create("TP {topic_number}: {topic_name}");
  form.setIsQuiz(true);
  form.setCollectEmail(true);       // requerido para identificar al alumno en el panel de respuestas
  form.setLimitOneResponsePerUser(true);
  {si tiempo_limite > 0: // Nota: Google Forms no tiene límite de tiempo nativo — usar timer externo}

  // Pregunta 1
  const q1 = form.addMultipleChoiceItem();
  q1.setTitle("{enunciado_pregunta_1}");
  q1.setChoices([
    q1.createChoice("{opcion_correcta_1}", true),
    q1.createChoice("{distractor_1_1}", false),
    q1.createChoice("{distractor_1_2}", false),
    q1.createChoice("{distractor_1_3}", false),
  ]);
  q1.setPoints({puntos_pregunta_1});

  // ... (una entrada por pregunta)

  Logger.log("Form URL: " + form.getPublishedUrl());
  Logger.log("Edit URL: " + form.getEditUrl());
}
```

---

### Step 4: Output Summary

Mostrar al docente según plataforma:

**Moodle:**
```
✅ Quiz Moodle generado en: {topic_folder}/tp-quiz.gift

Preguntas: {N} | Formato: GIFT | Encoding: UTF-8

Cómo importar:
1. Moodle → tu curso → Banco de preguntas → Importar
2. Formato: GIFT
3. Subir tp-quiz.gift (UTF-8)
4. Crear cuestionario → Agregar desde banco de preguntas
5. Configurar: tiempo={tiempo_limite}min, intentos={intentos}
```

**Google:**
```
✅ Quiz Google Forms generado en:
  {topic_folder}/tp-quiz-forms.md         ← estructura legible
  {topic_folder}/tp-quiz-forms-script.js  ← Apps Script para crear el Form

Cómo publicar:
1. Ir a script.google.com → Nuevo proyecto
2. Pegar el contenido de tp-quiz-forms-script.js
3. Ejecutar createQuiz()
4. Autorizar permisos de Google Forms
5. Copiar el Form URL del log y compartirlo en Google Classroom como assignment
```

---

## Output Files

| Archivo | Plataforma | Descripción |
|---------|-----------|-------------|
| `tp-quiz.gift` | Moodle | Quiz importable directo — formato GIFT UTF-8 |
| `tp-quiz-forms.md` | Google | Estructura legible del quiz |
| `tp-quiz-forms-script.js` | Google | Apps Script para crear el Google Form automáticamente |
