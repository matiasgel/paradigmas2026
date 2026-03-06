stepsCompleted: [1, 2, 3, 4]
inputDocuments: ["/home/matiasgel/desarrollo/paradigmas2026/material/lab.pdf", "/home/matiasgel/desarrollo/paradigmas2026/material/para.pdf"]
session_topic: 'Módulo BMAD educativo para preparación de clases universitarias (genérico)'
session_goals: 'Definir agentes, workflows y la estructura para producir guiones, slides, tps y planificaciones para cualquier materia universitaria. Con validación de referencias y guardrails de formalidad universitaria.'
selected_approach: 'progressive-flow'
techniques_used: ['Role Playing', 'Constraint Mapping', 'Decision Tree Mapping', 'Concept Blending']
ideas_generated: []
context_file: ''
---

# Brainstorming Session Results

**Facilitator:** Matiasgel
**Date:** 2026-03-05

## Session Overview

**Topic:** Módulo BMAD educativo para preparación de clases universitarias (genérico, cualquier materia)
**Goals:** Definir agentes, workflows y la estructura para producir guiones, slides, tps y planificaciones.

### Context Guidance

El módulo está diseñado para preparar **cualquier materia universitaria**, independientemente de la disciplina, año curricular o institución. Los PDFs y nombres de materias que aparecen en este documento (`lab.pdf`, `para.pdf`, "Laboratorio de programación y lenguajes", "Lenguajes y paradigmas de programación") son **ejemplos ilustrativos** usados durante el brainstorming — no forman parte del diseño del módulo.

El módulo debe contemplar los insumos académicos más frecuentes en cualquier cátedra: programas de materia en PDF, clases de Google Slides exportadas a PDF, libros en PDF, archivos `pptx` y apuntes docentes en formatos mixtos.

### Perfil del docente usuario

- Maneja Git con fluidez: commits, branches, merge, revert
- Usa GitHub Copilot activamente como herramienta de trabajo
- Lee y edita Markdown sin dificultad
- Comprende el modelo mental de slash commands y agentes de AI
- **No requiere modo tutorial básico** — sí se beneficia de orientación de flujo tipo `bmad-help`

### Session Setup

Enfoque seleccionado: Flujo de Técnica Progresivo. Iniciaremos explorando el ecosistema de manera amplia para luego reducir el foco hasta obtener soluciones viables.

## Exploración expansiva

### Nuevas familias de insumos a soportar

- Programas de materia en PDF
- Filminas exportadas desde Google Slides a PDF
- Presentaciones en `pptx`
- Libros y capítulos en PDF
- Apuntes docentes heterogéneos en formatos mezclados

### Ideas iniciales de agentes y comandos

- Agente que clasifica automáticamente el tipo de documento de entrada antes de procesarlo
- Agente `pdf-to-md` orientado a programas de materia, con extracción de unidades, objetivos y bibliografía
- Agente `slides-pdf-to-md` que reconstruye una secuencia de diapositivas en Markdown
- Agente `pptx-to-md` que transforma presentaciones editables en slides reutilizables en texto
- Agente `book-chapter-summarizer` para convertir capítulos de libros en resúmenes de clase
- Agente `reading-guide-generator` que produce guías de lectura con preguntas para estudiantes
- Agente `topic-researcher` que investiga en web y agrega material complementario actualizado
- Agente `class-script-generator` que toma programa + bibliografía + slides y arma un guion docente
- Agente `tp-generator` que toma una unidad y produce una guía práctica con consignas escalonadas
- Agente `curriculum-diff` que compara el plan actual con una propuesta nueva de contenidos
- Agente `weekly-planner` que reparte temas, materiales y actividades a lo largo de la cursada
- Agente `source-merger` que fusiona programa, libro, slides y notas en un documento maestro para una clase

### Tensiones y oportunidades detectadas

- El módulo debe distinguir entre documentos estructurales del curso y materiales operativos de una clase
- La salida principal debe ser Markdown limpio y reutilizable, no solo extracción cruda
- Conviene separar conversión de formato de interpretación pedagógica
- Los flujos deberían permitir iteración: programa → clase → slides → TP → ajuste del plan

## Reconocimiento de patrones

### Hallazgo principal

La definición más importante del módulo es que debe soportar **dos modos de trabajo complementarios**:

1. **Implementar una cursada con material existente**
2. **Generar una cursada nueva buscando y construyendo material**

Este hallazgo ordena casi todo el diseño.

### Patrón estructural emergente

El módulo no debería organizarse solo por tipo de documento, sino por **estrategia de construcción de cursada**:

- **Modo brownfield académico:** parte de programas, libros, slides, PDFs y PPTX ya existentes
- **Modo greenfield académico:** parte de un tema, objetivos de aprendizaje o plan deseado, y sale a investigar, seleccionar y construir material nuevo

### Capacidades comunes a ambos modos

- Normalizar fuentes heterogéneas a Markdown
- Analizar estructura temática y secuencia conceptual
- Diseñar clases, guiones, slides y trabajos prácticos
- Mantener coherencia entre clases, unidades y planificación general
- Permitir iteración y revisión docente

### Capacidades específicas por modo

#### Modo 1: Cursada con material existente

- Ingestar y clasificar archivos (`pdf`, `pptx`, slides exportadas, libros)
- Extraer estructura, bibliografía, unidades y actividades existentes
- Reutilizar y refactorizar material a formatos docentes consistentes
- Detectar huecos, solapamientos y desactualizaciones en el material disponible

#### Modo 2: Cursada nueva basada en investigación

- Investigar temas, bibliografía, tendencias y recursos web
- Armar mapa conceptual y secuencia de contenidos desde cero
- Proponer bibliografía, ejemplos, ejercicios y trabajos prácticos
- Construir una cursada inicial que luego pueda refinarse iterativamente

### Decisión de diseño derivada

Conviene que el módulo tenga dos workflows de entrada muy claros:

- **`build-course-from-materials`**
- **`build-course-from-research`**

Y luego ambos converjan en una zona común de producción documental:

- guiones de clase
- slides en Markdown
- guías de TP
- planificaciones
- propuestas de cambio curricular

### Implicancia para los agentes

Los agentes se ordenan mejor en tres capas:

1. **Ingesta e investigación**
2. **Análisis y diseño pedagógico**
3. **Producción documental**

Estas tres capas se materializan en el flujo iterativo de la Etapa 2, descripto en detalle en la sección **Planificación de acción**.

## Desarrollo de ideas

> **Nota sobre nomenclatura:** Los nombres de agentes y comandos que aparecen en esta sección son nombres provisorios del brainstorming divergente. Los nombres definitivos adoptados en el diseño final son los de la tabla de agentes y comandos de la sección **Planificación de acción**. Por ejemplo: `class-script-generator` → `class-writer`; `tp-generator` → `tp-designer`; `slides-pdf-to-md` + `pptx-to-md` → `material-ingester`.

### Arquitectura inicial del módulo

#### Fase 1: Descubrimiento / Ingesta

- `ingest-syllabus` — importa y estructura programas de materia
- `ingest-slides-pdf` — convierte clases exportadas desde Google Slides a Markdown reutilizable
- `ingest-pptx` — extrae contenido, jerarquía y notas desde presentaciones `pptx`
- `ingest-book` — resume y estructura capítulos o fragmentos de libros
- `research-topic` — busca material externo cuando no existe base documental suficiente

#### Fase 2: Análisis pedagógico

- `analyze-course-structure` — detecta unidades, secuencia y cobertura temática
- `analyze-existing-materials` — identifica redundancias, vacíos y material faltante
- `build-topic-map` — arma mapa conceptual y relaciones entre temas
- `align-objectives` — vincula contenidos con objetivos, actividades y evaluaciones

#### Fase 3: Producción de cursada

- `create-class-script` — genera guion docente por clase o por unidad
- `create-slides-md` — produce slides en Markdown a partir del guion o material fuente
- `create-tp-guide` — crea guía de trabajo práctico con consignas y criterios
- `create-course-plan` — arma planificación semanal o por unidades
- `propose-curriculum-change` — redacta cambios al plan de estudio a partir del análisis

### Dos modos de entrada al módulo

> **Nota de implementación:** Estos dos modos se materializan en el mismo comando `/edu-start-course`, que pregunta al docente la modalidad al inicio. Los flujos convergen completamente a partir de la Etapa 1 (diseño del plan de estudio).

#### Camino A: cursada con material existente

- Comando de entrada: `/edu-start-course` → seleccionar modalidad `desde-materiales`
- Equivalente conceptual en diseño: `build-course-from-materials`

Flujo sugerido:

1. Ingestar programas y materiales existentes
2. Analizar cobertura y calidad del material
3. Generar o reconstruir guiones, slides y TPs
4. Producir planificación consolidada

#### Camino B: cursada nueva desde investigación

- Comando de entrada: `/edu-start-course` → seleccionar modalidad `desde-investigacion`
- Equivalente conceptual en diseño: `build-course-from-research`

Flujo sugerido:

1. Investigar temas, bibliografía y recursos web
2. Construir mapa conceptual de la materia
3. Diseñar secuencia de clases y trabajos prácticos
4. Generar materiales iniciales de la cursada

### Convergencia final

Ambos caminos terminan en los mismos artefactos de salida, usando los nombres definitivos del módulo:

- `minuta.md` — guion de clase
- `filminas.md` — slides en Markdown
- `tp.md` — guía de trabajo práctico
- `curso-plan-general.md` — planificación consolidada
- `curriculum-change-proposal.md` — propuesta de cambios al plan de estudio

## Planificación de acción

### Flujo completo del módulo (refinado)

#### Punto de entrada: configuración del docente

El módulo arranca con una configuración mínima:

- nombre de la materia
- **año de la cursada** — determina la carpeta de salida `salida/{materia}/{año}/`
- duración de cada clase (en minutos) — configurable por comando
- modalidad de construcción: desde material existente o desde investigación
- **plan mínimo institucional** — obligatorio, dado por la universidad (importado desde PDF o cargado manualmente)

> **Primer año vs. años siguientes:** Si ya existe una cursada del año anterior para esta materia, usar `/edu-start-new-year {materia} {año}` en vez de `/edu-start-course`. Ese comando lee la retrospectiva del año anterior y preconfigura el plan de estudio como punto de partida.

> **Invariante del módulo:** El plan mínimo universitario es inmutable durante la cursada. El docente decide cómo distribuir los tópicos entre temas y cuánto peso darle a cada uno, pero **todos los tópicos del plan deben estar cubiertos** antes de poder cerrar la cursada.

#### Etapa 0 — Carga del plan mínimo institucional

- El docente provee el programa oficial de la materia (PDF de la universidad — cualquier materia, cualquier institución)
- El agente `plan-extractor` lo procesa y produce `plan-minimo.md`: lista estructurada de **todos los tópicos obligatorios** con sus unidades y descriptores
- El docente revisa y confirma el `plan-minimo.md` — este documento es la fuente de verdad de cobertura durante toda la cursada
- Salida: `plan-minimo.md` (inmutable una vez confirmado)

```
/edu-load-official-plan {ruta-pdf}    ← extrae tópicos del PDF institucional
/edu-confirm-official-plan            ← docente confirma; el plan queda bloqueado
```

#### Etapa 1 — Diseño del plan de estudio docente

- Sobre la base del plan mínimo confirmado, el módulo genera o recibe un plan de cursada docente
- Si no hay plan previo, arranca desde los tópicos del plan mínimo
- Si hay material existente, lo usa como base y verifica cobertura contra `plan-minimo.md`
- Se realiza un brainstorming académico: el agente navega solo en sitios de libros, papers y repositorios académicos (arXiv, Google Scholar, ACM, IEEE, etc.) para detectar temas nuevos, tendencias y actualizaciones relevantes
- El resultado es un `plan-de-estudio.md` revisable por el docente
- El módulo verifica inmediatamente que el `plan-de-estudio.md` cubra el 100% de los tópicos de `plan-minimo.md` y advierte si alguno queda sin asignar
- Salida: `plan-de-estudio.md` + `cobertura-inicial.md` (matriz de tópicos vs temas)

#### Etapa 2 — Ciclo iterativo por tema (loop)

Para cada tema del plan de estudio, se ejecuta el siguiente ciclo:

**Paso 2a — Diseño del tema**

- Se define qué entra en el tema: conceptos clave, objetivos de aprendizaje, bibliografía
- El docente **asigna explícitamente qué tópicos del plan mínimo** cubre este tema (puede ser uno o varios)
- El agente `plan-coverage-checker` marca esos tópicos como `asignados` en la matriz de cobertura
- Se establece cuántas semanas/clases cubre ese tema
- Salida: `tema-NN-diseño.md` (incluye sección `## Tópicos del plan mínimo cubiertos`)
- El módulo actualiza `cobertura-actual.md` automáticamente al cerrar el diseño

**Paso 2b — Material de clase**

- Se genera el contenido detallado de cada clase dentro del tema
- El agente respeta la duración de clase configurada por el docente
- Salidas:
  - `tema-NN-minuta.md` — guion completo de la clase, con secciones, tiempos estimados y notas para el docente
  - `tema-NN-filminas.md` — slides en Markdown estructuradas para exportar a un generador de presentaciones

**Paso 2c — Prácticas del tema**

- Se diseñan las guías de trabajos prácticos en base al contenido de las clases generadas
- Incluyen consignas, criterios de evaluación y referencias al material de la clase
- Salida: `tema-NN-tp.md`

**Paso 2d — Validación de cobertura del tema**

- Antes de cerrar, el agente `plan-coverage-checker` verifica que el contenido de `minuta.md` y `filminas.md` efectivamente trate los tópicos del plan mínimo asignados en `diseño.md`
- Si algún tópico asignado no aparece desarrollado en el material generado, se marca `[TÓPICO SIN DESARROLLO]` y bloquea el cierre
- El docente puede: corregir el material generado, desasignar el tópico a otro tema, o aceptar la cobertura parcial con justificación explícita
- El resultado se registra en `cobertura-actual.md`

**Paso 2e — Cierre del tema**

- El tema se cierra y todos sus archivos quedan organizados bajo una carpeta con título y numeración
- Estructura de carpeta: `temas/NN-nombre-del-tema/`
- Archivos dentro:
  - `diseño.md` — contenido del tema, objetivos y tópicos del plan mínimo asignados
  - `minuta.md` — guion completo de la clase con tiempos estimados
  - `filminas.md` — slides en Markdown para exportar a generador de presentaciones
  - `tp.md` — guía de trabajos prácticos alineada al contenido de la clase
  - `cobertura-tema.md` — tópicos del plan mínimo cubiertos en este tema y nivel de desarrollo
  - `referencias-estado.md` — reporte final del loop de validación de referencias
  - `revisión-escritura.md` — errores de escritura y gramática detectados y corregidos por ronda
  - `correcciones-escritura-historial.md` — resumen de cambios aplicados por `writing-fixer` *(si no se usa Git-native; con Git, este archivo es opcional — el `git log` de la branch contiene el historial completo)*
  - `revisión-coherencia.md` — rupturas, inconsistencias y correcciones de coherencia por ronda
  - `correcciones-coherencia-historial.md` — resumen de cambios aplicados por `coherence-fixer` *(opcional con Git-native — ver nota anterior)*
  - `revisión-guardrail.md` — resultado del guardrail de scope, formalidad y nivel académico

#### Etapa 3 — Documento integrador y verificación final de cobertura

Antes de cerrar la cursada, el módulo ejecuta la verificación final obligatoria:

```
/edu-check-coverage               ← verifica que el 100% del plan mínimo esté cubierto
```

Este comando produce `cobertura-final.md`: matriz completa de tópicos del plan mínimo vs. temas de la cursada, con estado de cada tópico:

| Tópico plan mínimo | Tema/s que lo cubren | Estado |
|---|---|---|
| [Tópico A del programa oficial] | 02-nombre-tema | `✓ cubierto` |
| [Tópico B del programa oficial] | 03-nombre-tema | `✓ cubierto` |
| [Tópico C del programa oficial] | — | `✗ sin cubrir` |

**El cierre de cursada queda bloqueado si algún tópico está en estado `✗ sin cubrir`.**

El docente puede resolverlo de tres maneras:
- Asignarlo a un tema existente y regenerar el material
- Crear un tema nuevo específico para ese tópico
- Justificar su omisión explícitamente (queda registrado en el informe)

Al terminar todos los temas se genera la planificación consolidada:

- `curso-plan-general.md` — mapa completo de la cursada con semanas, temas y referencias a cada carpeta
- `cobertura-final.md` — matriz de verificación de cobertura del plan mínimo institucional
- `curriculum-change-proposal.md` — comparación con el plan original y propuestas de cambio documentadas

---

### Estructura de salida del módulo

La cursada se organiza bajo `salida/{nombre-materia}/{año}/`. Cada año es una instancia independiente pero puede partir del año anterior como base.

```
salida/
  nombre-materia/                     ← una carpeta por materia
    2025/                             ← año anterior (solo lectura una vez cerrado)
      plan-minimo.md
      plan-de-estudio.md
      cobertura-final.md
      curso-plan-general.md
      curriculum-change-proposal.md
      retrospectiva-anual.md          ← qué funcionó, qué no, qué cambiar
      temas/
        01-primer-tema/
          ...
    2026/                             ← año actual en progreso
      plan-minimo.md                  ← tópicos obligatorios del programa universitario
      plan-de-estudio.md              ← plan docente (puede derivar del año anterior)
      cobertura-actual.md             ← matriz de cobertura actualizada en tiempo real
      cobertura-final.md              ← verificación final al cerrar cursada
      curso-plan-general.md
      curriculum-change-proposal.md
      comparacion-vs-anio-anterior.md ← diff automático entre 2025 y 2026
      temas/
        01-primer-tema/
          diseño.md                   ← incluye tópicos del plan mínimo asignados
          minuta.md
          filminas.md
          tp.md
          cobertura-tema.md
          referencias-estado.md
          revisión-escritura.md
          correcciones-escritura-historial.md  ← opcional con Git-native
          revisión-coherencia.md
          correcciones-coherencia-historial.md ← opcional con Git-native
          revisión-guardrail.md
        02-segundo-tema/
          ...
```

---

### Continuidad entre años

#### Concepto central

Una cursada no empieza de cero cada año. El módulo permite **iniciar el año nuevo partiendo del año anterior** como base, con un flujo de mejora incremental.

#### Flujo de apertura de nuevo año

```
/edu-start-new-year {materia} {año}        ← crea la carpeta del nuevo año
```

Este comando:

1. Lee el `curso-plan-general.md` y `cobertura-final.md` del año anterior
2. Copia el `plan-minimo.md` como punto de partida (el docente puede actualizarlo si cambió el programa oficial)
3. Genera un `plan-de-estudio.md` borrador basado en el año anterior
4. Genera automáticamente `comparacion-vs-anio-anterior.md`: diff entre el plan anterior y el nuevo borrador
5. Lista los temas del año anterior disponibles para reutilizar, adaptar o descartar

#### Modos de reutilización por tema

Para cada tema del año anterior, el docente puede elegir:

| Modo | Comando | Acción |
|---|---|---|
| Reutilizar sin cambios | `/edu-copy-topic {tema} {año-origen}` | Copia el tema al año nuevo sin modificaciones |
| Adaptar | `/edu-adapt-topic {tema} {año-origen}` | Copia y abre el ciclo de mejora (loops de validación) |
| Reescribir desde cero | `/edu-design-topic {N}` | Ignora el año anterior, diseño nuevo |
| Descartar | — | No se incluye en el nuevo año |

#### Retrospectiva anual

Al cerrar una cursada con `/edu-close-course`, el módulo genera `retrospectiva-anual.md`:

- Temas que generaron más correcciones de escritura/coherencia (indicador de dificultad de producción)
- Referencias rechazadas o no verificadas con mayor frecuencia
- Tópicos del plan mínimo que requirieron múltiples iteraciones para cubrirse
- Notas libres del docente sobre qué mejorar el próximo año

Este archivo es leído automáticamente en `/edu-start-new-year` para informar el borrador del nuevo plan.

#### Comando de cierre de cursada

```
/edu-close-course {materia} {año}          ← cierra la cursada y genera retrospectiva
```

Bloquea la carpeta del año como solo lectura (las branches mergeadas a `main` quedan protegidas) y genera la retrospectiva. A partir de ahí el año es referencia histórica.

---

### Memoria global y perfiles de profesores

#### Problema

El módulo, tal como está diseñado, es stateless por cursada. No recuerda:
- Qué decisiones de diseño tomó el docente en años anteriores y por qué
- Qué estilos de clase funcionaron mejor
- Qué perfiles de alumnos tiene cada materia
- Qué patrones de error son recurrentes en el material generado

#### Propuesta: memoria global del módulo

Una carpeta `_edu-memory/` a nivel de workspace (análoga a `_bmad/_memory/`) que persiste entre materias y años:

```
_edu-memory/
  global-preferences.md              ← preferencias globales del docente (estilo, tono, formato)
  perfiles-alumnos/
    {nombre-materia}-perfil.md        ← perfil del alumno típico de cada materia
  patrones-recurrentes.md            ← errores y correcciones que aparecen siempre
  historial-decisiones.md            ← por qué se tomaron ciertas decisiones de diseño
  perfiles-profesores/               ← si hay más de un docente usando el módulo
    perfil-{nombre}.md
```

#### Perfiles de profesores universitarios

Si el módulo es usado por múltiples docentes (o un docente quiere simular perspectivas distintas para mejorar el material), se pueden definir **perfiles de profesor** que informan el tono, nivel de profundidad y estilo de los documentos generados:

| Perfil | Características |
|---|---|
| `profesor-teorico` | Prefiere rigor formal, definiciones precisas, ejemplos abstractos. Bibliografía clásica. |
| `profesor-practico` | Prioriza ejemplos concretos, ejercicios aplicados, casos reales. |
| `profesor-socratico` | Estructura el material como preguntas que guían al alumno a la respuesta. |
| `profesor-flipped` | Diseña para clase invertida: material de lectura previa + clase de ejercicio. |
| `profesor-investigador` | Incorpora papers recientes, estado del arte, conexión con investigación activa. |

Cada perfil ajusta cómo `class-writer`, `tp-designer` y `academic-guardrail` producen sus documentos.

**Comandos propuestos:**

```
/edu-set-professor-profile {perfil}        ← activa un perfil para la cursada actual
/edu-create-professor-profile {nombre}     ← el docente define su propio perfil personalizado
/edu-compare-profiles {tema} {perfil-A} {perfil-B}  ← genera el mismo tema con dos estilos distintos para comparar
```

#### Uso de la memoria global en el flujo

- Al iniciar cualquier cursada, el módulo lee `_edu-memory/global-preferences.md` y `perfiles-alumnos/{materia}-perfil.md`
- Al cerrar una cursada, actualiza `patrones-recurrentes.md` con los errores más frecuentes del año
- Al iniciar un nuevo año, lee `historial-decisiones.md` para no repetir decisiones ya descartadas
- El `academic-guardrail` usa el perfil del alumno de `_edu-memory` para calibrar el nivel académico esperado

#### Actualización del `copilot-instructions.md`

La memoria global también informa la generación de `.github/copilot-instructions.md`: el perfil del docente activo y el perfil del alumno de la materia se incorporan al contexto, haciendo que GitHub Copilot asista de forma coherente con el estilo docente elegido.

---

### Comandos clave del módulo

| Comando | Fase | Acción |
|---|---|---|
| `/edu-load-official-plan {ruta-pdf}` | Configuración | Extrae tópicos obligatorios del PDF del programa universitario |
| `/edu-confirm-official-plan` | Configuración | Docente confirma el plan mínimo; queda bloqueado como referencia |
| `/edu-start-course` | Configuración | Inicia la cursada desde cero o importando un programa |
| `/edu-set-class-duration {minutos}` | Configuración | Configura la duración de cada clase |
| `/edu-research-plan` | Plan de estudios | Brainstorming académico web para armar o actualizar el plan |
| `/edu-check-coverage` | Cobertura | Muestra matriz de cobertura actual del plan mínimo vs. temas definidos |
| `/edu-design-topic {N}` | Ciclo por tema | Diseña el contenido del tema N y asigna tópicos del plan mínimo |
| `/edu-assign-topics {N} {IDs}` | Ciclo por tema | Asigna explícitamente tópicos del plan mínimo al tema N |
| `/edu-create-class {N}` | Ciclo por tema | Genera minuta y filminas del tema N |
| `/edu-create-tp {N}` | Ciclo por tema | Genera guía de prácticos del tema N |
| `/edu-validate-coverage {N}` | Validación tema | Verifica que el material generado desarrolle los tópicos asignados al tema N |
| `/edu-validate-writing {N}` | Loop escritura | Revisa ortografía, gramática, puntuación y estructura de párrafos en todos los documentos del tema N |
| `/edu-apply-writing-fixes {N}` | Loop escritura | El agente aplica automáticamente todas las correcciones sugeridas (el docente confirma) |
| `/edu-fix-writing {N} {ID}` | Loop escritura | Docente corrige manualmente un ítem de escritura específico; el agente reverifica esa sección |
| `/edu-ignore-writing {N} {ID}` | Loop escritura | Docente descarta una sugerencia [MEJORA] con justificación; queda registrado |
| `/edu-validate-references {N}` | Loop referencias | Muestra estado actualizado de todas las referencias del tema N |
| `/edu-fix-reference {N} {ID} "{texto}"` | Loop referencias | Docente reescribe una referencia; el sistema la reverifica |
| `/edu-suggest-alternative {N} {ID}` | Loop referencias | El agente busca una referencia alternativa verificada sobre el mismo tema |
| `/edu-accept-reference {N} {ID}` | Loop referencias | Docente aprueba manualmente una referencia no verificable automáticamente |
| `/edu-reject-reference {N} {ID}` | Loop referencias | Elimina una referencia del documento del tema N |
| `/edu-validate-scope {N}` | Guardrail | Formalidad, scope y nivel académico del tema N |
| `/edu-fix-guardrail-auto {N}` | Guardrail | El agente reformula automáticamente lenguaje informal a registro académico formal |
| `/edu-close-topic {N}` | Cierre tema | Cierra el tema y organiza su carpeta (bloqueado hasta resolver todos los loops) |
| `/edu-generate-course-plan` | Cierre cursada | Genera la planificación consolidada |
| `/edu-propose-curriculum-change` | Cierre cursada | Propone cambios al plan de estudio |
| `/edu-close-course {materia} {año}` | Cierre cursada | Cierra la cursada, protege la carpeta y genera retrospectiva anual |
| `/edu-start-new-year {materia} {año}` | Nuevo año | Crea la cursada del año nuevo partiendo del año anterior como base |
| `/edu-copy-topic {tema} {año-origen}` | Nuevo año | Copia un tema del año anterior sin modificaciones |
| `/edu-adapt-topic {tema} {año-origen}` | Nuevo año | Copia un tema del año anterior y abre el ciclo de mejora |
| `/edu-set-professor-profile {perfil}` | Configuración | Activa un perfil docente para la cursada actual |
| `/edu-create-professor-profile {nombre}` | Configuración | Define un perfil docente personalizado |
| `/edu-compare-profiles {tema} {A} {B}` | Configuración | Genera el mismo tema con dos perfiles distintos para comparar |
| `/edu-update-copilot-context` | Configuración | Regenera copilot-instructions.md con el estado actual de la cursada |
| `/edu-status {N}` | Navegación | Muestra el estado del tema N y el próximo paso recomendado |

---

### Agentes del módulo

| Agente | Rol | Operación principal |
|---|---|---|
| `course-planner` | Diseño del plan de estudio | Importar, analizar y generar plan de estudio |
| `academic-researcher` | Investigación web académica | Solo sitios de papers, libros y repositorios académicos |
| `topic-designer` | Diseño de cada tema | Definir contenidos, objetivos y semanas |
| `class-writer` | Generación de minuta y filminas | Respetar duración, producir minuta y slides |
| `tp-designer` | Generación de prácticos | Consignas alineadas al material de clase |
| `material-ingester` | Conversión de insumos | PDF, PPTX, slides exportadas → Markdown |
| `curriculum-reviewer` | Propuesta de cambios | Comparar plan actual vs. nuevo y documentar cambios |
| `plan-extractor` | Extracción del plan mínimo | Procesar PDF universitario y producir lista estructurada de tópicos obligatorios |
| `plan-coverage-checker` | Verificación de cobertura | Mantener y verificar la matriz de cobertura del plan mínimo en tiempo real |
| `reference-validator` | Validación de referencias | Verificar que toda cita, fuente y referencia sea real y trazable |
| `writing-validator` | Validación de escritura y gramática | Corregir ortografía, gramática, puntuación y estructura de párrafos en todos los documentos generados |
| `writing-fixer` | Corrección automática de escritura | Aplicar correcciones de escritura directamente en los archivos Markdown sin intervención del docente para errores críticos |
| `coherence-fixer` | Corrección de coherencia textual | Detectar y reparar rupturas de coherencia interna y entre documentos del mismo tema; unificar terminología |
| `academic-guardrail` | Control de contexto, formalidad y corrección | Detectar y corregir desvíos de formalidad, scope y coherencia universitaria; reformular lenguaje informal automáticamente |

---

## Capas de calidad y guardrails

### Problema central

Los modelos de lenguaje pueden generar:

- **Referencias y citas falsas** (autores inventados, DOIs que no existen, libros inexistentes)
- **Contenido fuera del scope del tema** (desvíos conceptuales o temáticos no planificados)
- **Lenguaje informal** incompatible con la formalidad académica universitaria
- **Afirmaciones imprecisas o sin respaldo** que parecen válidas pero no lo son
- **Mezcla de niveles de complejidad** inadecuada para el año/perfil del estudiante
- **Errores de escritura y gramática** (faltas ortográficas, puntuación incorrecta, concordancia de género/número, construcciones gramaticales ambiguas, párrafos mal estructurados) que afectan la credibilidad del material universitario

### Agente `reference-validator`

Responsabilidades:

- Revisar toda referencia generada por `academic-researcher` y `class-writer` antes de guardarla
- Verificar cada cita bibliográfica contra fuentes reales: cruzar título, autor, año con bases de datos académicas (CrossRef, OpenLibrary, Semantic Scholar)
- Marcar con `[NO VERIFICADO]` toda referencia que no pueda confirmarse como existente
- Producir una lista `referencias-no-verificadas.md` por tema, para que el docente las revise manualmente
- **Nunca elimina** una referencia no verificada; la señaliza y escala al docente

Protocolo de verificación:

1. Toda referencia generada pasa por el validador antes de incluirse en un documento final
2. Si la URL de un paper es accesible, se verifica título y abstract
3. Si es un libro, se cruza título + autor + ISBN/editorial con bases abiertas
4. Si es un paper sin URL, se busca el título exacto en Semantic Scholar o arXiv
5. Se reporta el nivel de confianza: `verificado` / `probable` / `no-verificado`

### Agente `writing-validator`

Responsabilidades:

- Revisar **todos** los documentos generados del tema: `diseño.md`, `minuta.md`, `filminas.md`, `tp.md`
- Detectar y clasificar errores en cuatro dimensiones:

  1. **Ortografía** — palabras mal escritas, acentuación incorrecta, uso incorrecto de mayúsculas
  2. **Gramática** — concordancia de género/número, uso correcto de tiempos verbales, construcciones sintácticas incorrectas
  3. **Puntuación** — comas, puntos, dos puntos, punto y coma mal usados o faltantes
  4. **Estructura de párrafos** — párrafos sin idea principal clara, oraciones excesivamente largas o ambiguas, conectores lógicos faltantes o incorrectos

- Producir `revisión-escritura.md` con cada error encontrado, su ubicación exacta (documento + línea/sección) y la corrección sugerida
- Clasificar cada error por severidad:
  - `[CRÍTICO]` — error que distorsiona el significado o hace ilegible el texto
  - `[ERROR]` — error claro que debe corregirse antes del cierre del tema
  - `[MEJORA]` — el texto es comprensible pero puede mejorar su claridad
- Proponer la corrección directa para cada hallazgo
- **El cierre del tema queda bloqueado** si quedan errores `[CRÍTICO]` o `[ERROR]` sin atender

Protocolo de revisión:

1. Cada documento pasa por `writing-validator` después de ser generado y antes de la validación de referencias
2. El agente `writing-fixer` puede aplicar correcciones automáticamente sin intervención del docente para errores `[CRÍTICO]` y `[ERROR]`; los `[MEJORA]` siempre requieren aprobación
3. Después de cada correción automática, `writing-validator` re-verifica solo las secciones modificadas
4. El loop continúa hasta que no queden errores `[CRÍTICO]` ni `[ERROR]`
5. El docente puede revisar un historial de todos los cambios aplicados por el agente en `correcciones-escritura-historial.md`

El formato del reporte `revisión-escritura.md`:

```markdown
# Revisión de escritura — Tema NN — Ronda X

| ID | Documento | Sección | Error | Severidad | Corrección sugerida |
|----|-----------|---------|-------|-----------|--------------------|
| E01 | minuta.md | Introducción | "los paradigma" → concordancia | [ERROR] | "los paradigmas" |
| E02 | filminas.md | Slide 3 | Punto final faltante | [MEJORA] | Agregar "." al final |
| E03 | tp.md | Consigna 2 | Oración de 80 palabras sin pausas | [ERROR] | Dividir en dos oraciones |

Errores críticos pendientes: 0
Errores pendientes de corrección: 2 (E01, E03)
Loop cerrado: NO
```

Comandos del loop de escritura:

- `/edu-validate-writing {N}` — detecta y clasifica todos los errores de escritura en los documentos del tema N
- `/edu-fix-writing-auto {N}` — el agente `writing-fixer` corrige automáticamente todos los `[CRÍTICO]` y `[ERROR]` sin intervención del docente y muestra resumen de cambios aplicados
- `/edu-apply-writing-fixes {N}` — el agente aplica correcciones `[MEJORA]` sugeridas con confirmación del docente antes de cada cambio
- `/edu-fix-writing {N} {ID}` — el docente corrige manualmente el ítem ID y el agente re-verifica esa sección
- `/edu-ignore-writing {N} {ID}` — el docente descarta una sugerencia `[MEJORA]` con justificación; queda registrado
- `/edu-writing-history {N}` — muestra el historial completo de correcciones aplicadas por el agente en el tema N

### Agente `writing-fixer`

Agente especializado en **ejecutar** correcciones de escritura, separado del `writing-validator` que solo detecta.

Capacidades:

- Recibe la lista de ítems del reporte de `writing-validator` y aplica cada corrección directamente en el archivo Markdown correspondiente
- Reescribe oraciones demasiado largas mantenéiendo el significado original
- Corrige concordancias, acentuación y puntuación de forma precisa y localizada (no reescribe todo el documento)
- Registra cada cambio en `correcciones-escritura-historial.md` con: documento, sección, texto original, texto corregido y tipo de corrección *(este archivo es opcional si el docente usa el flujo Git-native — en ese caso los commits del agente cumplen la misma función)*
- Nunca modifica el contenido temático ni las referencias — solo la forma de escritura
- Para errores `[CRÍTICO]` y `[ERROR]`: actúa automáticamente al recibir `/edu-fix-writing-auto {N}`
- Para errores `[MEJORA]`: presenta el cambio propuesto y espera confirmación del docente

### Agente `coherence-fixer`

Agente dedicado a detectar y reparar **problemas de coherencia textual** dentro de cada documento, y entre documentos del mismo tema.

Responsabilidades:

**Coherencia interna (dentro de un documento):**
- Detectar saltos abruptos entre ideas sin transición
- Identificar párrafos o secciones que no conectan lógicamente con el anterior
- Detectar contradicciones internas dentro del mismo documento
- Verificar que la progresión de conceptos siga una secuencia didáctica lógica (de general a específico, de simple a complejo)

**Coherencia entre documentos del mismo tema:**
- Verificar que `minuta.md` y `filminas.md` sean coherentes entre sí: las filminas deben ser la versión visual del guion, no una versión diferente del tema
- Verificar que `tp.md` solo refiera conceptos presentes en `minuta.md`
- Detectar terminología inconsistente: si un concepto se llama de una manera en la minuta debe llamarse igual en las filminas y el TP

**Capacidades de corrección automática:**
- Reescribir párrafos de transición para conectar ideas desconectadas
- Agregar frases conectoras lógicas ("A partir de esto...", "En consecuencia...", "Retomando el concepto anterior...")
- Unificar terminología inconsistente en todos los documentos del tema con un solo comando
- Reestructurar el orden de secciones si la secuencia didáctica no es óptima (con aprobación del docente)

**Clasificación de hallazgos:**
- `[RUPTURA]` — el texto pierde el hilo completamente; bloquea cierre
- `[INCOHERENCIA]` — ideas que se contradicen o no se conectan; bloquea cierre
- `[INCONSISTENCIA]` — mismo concepto nombrado de forma diferente en distintos documentos; bloquea cierre
- `[TRANSICIÓN]` — falta conector entre párrafos; no bloquea, el docente decide

**Salidas:**
- `revisión-coherencia.md` — reporte por ronda con hallazgos y correcciones sugeridas
- `correcciones-coherencia-historial.md` — historial de todos los cambios aplicados por el agente

Comandos del loop de coherencia:

- `/edu-validate-coherence {N}` — detecta problemas de coherencia interna y entre documentos del tema N
- `/edu-fix-coherence-auto {N}` — el agente corrige automáticamente `[RUPTURA]`, `[INCOHERENCIA]` e `[INCONSISTENCIA]`
- `/edu-fix-coherence {N} {ID}` — el docente acepta o ajusta una corrección de coherencia específica
- `/edu-unify-terminology {N}` — el agente unifica terminología inconsistente en todos los documentos del tema (con lista de cambios para confirmar)
- `/edu-coherence-history {N}` — muestra historial de correcciones de coherencia aplicadas en el tema N

### Agente `academic-guardrail`

Responsabilidades:

- Revisar cada documento producido contra tres ejes:

  1. **Formalidad lingüística** — detectar lenguaje coloquial, contracciones, términos imprecisos o expresiones informales
  2. **Coherencia de scope** — verificar que el contenido de la clase/minuta/filminas no se desvíe del tema diseñado en `diseño.md`
  3. **Nivel académico universitario** — verificar que el nivel de profundidad, la terminología y la estructura del contenido sea apropiada para la materia y el año curricular configurado

- **Además de reportar, el agente puede ejecutar correcciones** cuando el docente lo autoriza:
  - Reformular frases informales en registro académico formal sin cambiar el contenido
  - Ajustar el nivel de profundidad de una explicación si está por encima o por debajo del perfil del alumno
  - Agregar disclaimers académicos cuando el contenido roza afirmaciones sin respaldo

- Producir un `revisión-guardrail.md` con advertencias clasificadas por severidad:
  - `[CRÍTICO]` — debe corregirse antes de cerrar el tema
  - `[ADVERTENCIA]` — se recomienda revisión docente
  - `[SUGERENCIA]` — mejora opcional de calidad

Comandos del loop de guardrail:

- `/edu-validate-scope {N}` — ejecuta el guardrail completo sobre los documentos del tema N
- `/edu-fix-guardrail-auto {N}` — el agente corrige automáticamente todos los `[CRÍTICO]`: reformula lenguaje informal, ajusta nivel, inserta conectores académicos
- `/edu-fix-guardrail {N} {ID}` — el docente acepta o modifica una corrección de guardrail específica
- `/edu-guardrail-history {N}` — muestra historial de correcciones de guardrail aplicadas en el tema N

### Guardrails incorporados en cada agente

Cada agente del módulo tiene reglas de contexto que no puede violar:

| Agente | Guardrail principal |
|---|---|
| `academic-researcher` | Solo puede navegar dominios académicos: arXiv, ACM, IEEE, Springer, Google Scholar, OpenLibrary, Semantic Scholar. Nunca Wikipedia, Medium, blogs ni sitios sin afiliación académica |
| `class-writer` | El contenido de la minuta y las filminas no puede salir del scope definido en `diseño.md` de ese tema. Debe incluir siempre notas de tiempo estimado por sección |
| `tp-designer` | Las consignas deben ser trazables al contenido de `minuta.md`. No puede incluir ejercicios sobre temas no vistos en la clase |
| `course-planner` | El plan de estudio solo puede incluir temas coherentes con los objetivos de la materia y el perfil del plan de estudios de la carrera |
| `curriculum-reviewer` | Los cambios propuestos deben estar justificados con al menos una fuente académica verificada |

### Paso de validación agregado al ciclo iterativo

El ciclo por tema incluye un paso de validación **explícitamente iterativo** antes del cierre. El docente puede pasar por él tantas veces como sea necesario hasta que todas las referencias sean reales y estén correctamente escritas en su contexto:

```
/edu-design-topic {N}
/edu-create-class {N}
/edu-create-tp {N}

┌─── LOOP 1: ESCRITURA Y GRAMÁTICA ───────────────────────────────────────────────┐
│  /edu-validate-writing {N}           ← detecta errores de escritura
│  /edu-fix-writing-auto {N}            ← agente corrige [CRÍTICO] y [ERROR] directo
│  /edu-apply-writing-fixes {N}         ← agente propone correcciones [MEJORA] (docente confirma)
│  /edu-fix-writing {N} {ID}            ← docente corrige un ítem puntualmente
│  /edu-writing-history {N}             ← historial de cambios aplicados por el agente
└─────────────────────────────────────────────────────────────────────────────┘

┌─── LOOP 2: COHERENCIA Y TERMINOLOGÍA ─────────────────────────────────────────┐
│  /edu-validate-coherence {N}          ← detecta rupturas, contradicciones, inconsistencias
│  /edu-fix-coherence-auto {N}           ← agente repara [RUPTURA] e [INCOHERENCIA] directo
│  /edu-unify-terminology {N}            ← agente unifica terminología (docente confirma lista)
│  /edu-fix-coherence {N} {ID}           ← docente acepta/ajusta una corrección puntual
│  /edu-coherence-history {N}            ← historial de cambios aplicados por el agente
└─────────────────────────────────────────────────────────────────────────────┘

┌─── LOOP 3: REFERENCIAS ──────────────────────────────────────────────────────────┐
│  /edu-validate-references {N}         ← estado de cada referencia
│  /edu-fix-reference / suggest / accept / reject
└─────────────────────────────────────────────────────────────────────────────┘

/edu-validate-scope {N}                  ← guardrail de formalidad + nivel académico
/edu-fix-guardrail-auto {N}              ← agente corrige reformulando lenguaje formal automáticamente
/edu-close-topic {N}                     ← bloqueado hasta que no queden [CRÍTICO]/[ERROR]/[RUPTURA]/[INCOHERENCIA] en ningún loop
```

### Loop de validación de referencias en detalle

El agente `reference-validator` trabaja en rondas. Cada ronda produce un reporte actualizado. El docente decide qué hacer con cada ítem pendiente antes de la próxima ronda.

#### Estado de cada referencia

| Estado | Significado |
|---|---|
| `✓ verificado` | Confirmada en CrossRef / Semantic Scholar / OpenLibrary / arXiv |
| `~ probable` | Datos coherentes pero no pudo confirmarse con URL o DOI directo |
| `✗ no-verificado` | No encontrada en ninguna fuente. Requiere acción del docente |
| `⊘ rechazada` | El docente la eliminó del documento |
| `★ aceptada-manualmente` | El docente la verificó por su cuenta y la aprobó |

#### Acciones disponibles por referencia

- `/edu-fix-reference {N} {ID} "{nueva referencia}"` — el docente reescribe la referencia manualmente con datos correctos; el sistema la reverifica
- `/edu-suggest-alternative {N} {ID}` — el agente busca activamente en fuentes académicas una referencia alternativa verificada sobre el mismo tema/concepto
- `/edu-accept-reference {N} {ID}` — el docente confirma que la referencia es real aunque el sistema no pudo verificarla automáticamente (queda marcada `★ aceptada-manualmente`)
- `/edu-reject-reference {N} {ID}` — elimina la referencia del documento y la marca como `⊘ rechazada`
- `/edu-validate-references {N}` — re-ejecuta la validación completa sobre el estado actual del tema y muestra el nuevo reporte

#### Condición de cierre del loop

El loop de referencias queda resuelto cuando **no existe ningún ítem en estado `✗ no-verificado`**. Puede quedar ítems `~ probable` o `★ aceptada-manualmente` — son responsabilidad del docente y quedan registrados en el reporte final.

#### Reporte de estado por ronda

Cada vez que corre `/edu-validate-references {N}`, el sistema imprime y actualiza `tema-NN/referencias-estado.md`:

```markdown
# Estado de referencias — Tema NN — Ronda X

| ID | Referencia | Estado | Fuente de verificación |
|----|-----------|--------|------------------------|
| R01 | Aho, A. et al. (2006). Compilers... | ✓ verificado | CrossRef DOI:10.xxx |
| R02 | García, L. (2023). Tipos en Haskell... | ✗ no-verificado | No encontrada en ninguna fuente |
| R03 | Pierce, B. (2002). Types and... | ✓ verificado | OpenLibrary ISBN:978-0-262-16209-8 |
| R04 | Martínez, P. (2021). Lambda calculus... | ~ probable | Título encontrado, sin DOI confirmado |

Referencias pendientes de acción: 1 (R02)
Loop cerrado: NO
```

#### Escritura en contexto

Además de verificar la existencia, el agente controla que cada referencia esté escrita correctamente **en el contexto donde se usa**:

- Si es una cita en la minuta: debe incluir autor, año y estar en el formato bibliográfico de la cátedra
- Si es una referencia en filminas: debe ser concisa, trazable y apropiada para el slide donde aparece
- Si es bibliografía en el TP: debe incluir todos los datos necesarios para que el alumno la encuentre

El agente señala con `[FORMATO INCORRECTO]` toda referencia correctamente verificada pero mal escrita en su contexto, para que el docente la corrija o use `/edu-fix-reference`.

---

## Derivaciones del debate multi-agente (party mode — 2026-03-06)

### Hallazgos críticos incorporados al diseño

#### 1. Guardrails faltantes en 9 de 14 agentes

La tabla de guardrails por agente solo cubría 5 agentes. Los 9 restantes (`plan-extractor`, `plan-coverage-checker`, `reference-validator`, `writing-validator`, `writing-fixer`, `coherence-fixer`, `academic-guardrail`, `topic-designer`, `material-ingester`) necesitan guardrails explícitos. En particular:

- `writing-fixer` no debe tocar bloques de código, fragmentos técnicos ni nombres de archivos
- `material-ingester` no debe interpretar contenido, solo convertir formato
- `plan-extractor` no debe inferir tópicos no presentes en el PDF — solo extraer lo que está

#### 2. Protocolo de precedencia entre agentes de calidad

Los agentes de calidad deben ejecutarse en orden secuencial fijo para evitar conflictos sobre los mismos archivos:

```
Loop 1: writing-validator → writing-fixer
         ↓
Loop 2: coherence-fixer
         ↓
Loop 3: reference-validator
         ↓
Guardrail: academic-guardrail
```

Cada agente toma como input el output del anterior, no el archivo original. No se permite ejecución en paralelo de agentes que modifiquen los mismos documentos.

#### 3. Integración Git-native — estrategia de branching por tema

Dado el perfil Git del docente, el módulo adopta una estrategia Git-native:

- Cada tema trabaja en una branch propia: `tema/NN-nombre-del-tema`
- Cada corrección automática de un agente se registra como un **commit con mensaje estandarizado**:
  - `[writing-fixer] E01: concordancia corregida en minuta.md`
  - `[coherence-fixer] C02: terminología unificada en filminas.md y tp.md`
- El cierre del tema (`/edu-close-topic`) hace el **merge a `main`** solo cuando todos los loops están resueltos
- El bloqueo de cierre se convierte en un bloqueo de merge — natural para el flujo Git
- El docente puede hacer `git revert` de cualquier corrección automática si no la acepta

**Beneficio:** los archivos `correcciones-escritura-historial.md` y `correcciones-coherencia-historial.md` pueden eliminarse o reducirse — el `git log` de la branch es el historial de cambios del agente

**Temas en paralelo resueltos:** con branches por tema, el docente puede trabajar en `tema/01` y `tema/02` simultáneamente sin conflicto. La serialización ocurre solo en el merge.

#### 4. Generación de `copilot-instructions.md` por materia

Como parte de `/edu-start-course`, el módulo genera o actualiza `.github/copilot-instructions.md` con el contexto de la cursada actual:

- Nombre de la materia y perfil del alumno
- Resumen del plan mínimo institucional
- Estilo académico esperado (formalidad, nivel de profundidad)
- Vocabulario técnico específico de la materia
- Estado actual de la cursada (temas completados, en progreso)

**Resultado:** GitHub Copilot se convierte en un colaborador informado de la cursada. Cuando el docente edita cualquier archivo del módulo, Copilot tiene contexto real de la materia para asistir con coherencia.

**Comando propuesto:**
```
/edu-update-copilot-context    ← regenera copilot-instructions.md con el estado actual de la cursada
```

#### 5. Orientación de flujo (modo asistido)

En lugar de un modo tutorial básico, el módulo incorpora orientación de estado al estilo `bmad-help`:

- Después de cada comando ejecutado, el sistema muestra el próximo paso recomendado
- Ejemplo: _"Loop 1 cerrado sin errores. Próximo paso: `/edu-validate-coherence {N}`"
- El docente puede ignorar la sugerencia y correr cualquier comando manualmente

**Comando propuesto:**
```
/edu-status {N}    ← muestra el estado completo del tema N y el próximo paso recomendado
```

