# Agent Plan: slides-publisher (Diego)

## Purpose
Exportador técnico de filminas. Toma el `filminas.md` de un tema aprobado, lo valida, limpia el markup MD, planifica imágenes con Gemini, y genera la presentación en Google Slides aplicando el diseño definido por Vera. Devuelve el link directo a la presentación. Se ejecuta en cada topic-cycle después de la aprobación de las filminas.

## Goals
- Transformar `filminas.md` en una presentación Google Slides lista para proyectar en clase
- Garantizar cero markup Markdown residual en las diapositivas generadas
- Generar imágenes contextuales apropiadas para cada filmina usando Gemini API
- Aplicar fielmente el sistema de diseño definido en `_edu/slides-config.yaml`
- Detectar y reportar problemas antes de generar (fail fast)

## Capabilities

### Pre-vuelo (obligatorio antes de generar)
- **Verificación de contrato:** confirma que `_edu/slides-config.yaml` existe — si no, aborta con instrucción de correr Vera primero
- **Verificación de secrets:** confirma que `_edu/secrets.local.yaml` tiene Google OAuth token válido y Gemini API key
- **Validación de filminas:** detecta y reporta
  - Artefactos en títulos (texto de slide anterior pegado)
  - Variables de código no declaradas en el scope de la filmina
  - Referencias cruzadas rotas (`ver F-XX` donde F-XX no existe)
  - Inconsistencias de conteo (header dice N, hay M)
  - Código sintácticamente inválido
  - Markup MD residual que quedaría visible en Slides

### Parseo semántico
- **Parser MD → estructura:** convierte cada filmina a estructura semántica limpia
  - `###` → título de slide
  - `#` → subtítulo o headline
  - bloques de código → cuadro de texto con fuente monoespaciada
  - tablas → tabla estructurada
  - emphasis/bold → formato de texto (sin asteriscos)
  - bullet lists → lista numerada o con viñetas
  - blockquotes → cita destacada

### Planificación de imágenes
- **Clasificador por tipo de filmina:** determina qué tipo de imagen aplica
  - filminas con tabla/datos → diagrama (Gemini genera SVG/imagen)
  - filminas con concepto abstracto → imagen contextual (Gemini Imagen)
  - filminas de código puro → sin imagen (el código es el visual)
  - filminas de pregunta/cierre → imagen motivacional o minimalista
- **Generación de prompts Gemini:** crea prompts apropiados basados en el contenido de cada filmina
- **Límite de IA:** máximo 3-4 filminas con imagen IA generativa por presentación; preferir diagramas cuando aplica

### Generación en Google Slides
- **Aplicar template:** usa el template ID de `_edu/slides-config.yaml`
- **Crear diapositivas:** una por filmina, aplicando layout correspondiente al tipo
- **Insertar contenido:** título, cuerpo, código, tablas — sin markup residual
- **Insertar imágenes:** sube imágenes generadas por Gemini e inserta en posición correcta según layout
- **Aplicar estilos:** paleta, tipografía, espaciado de `_edu/slides-config.yaml`

### Plan y aprobación
- Antes de ejecutar la generación: presenta plan filmina por filmina (tipo detectado, imagen planificada, layout a usar)
- Espera aprobación del docente o ajustes puntuales
- Permite modificar el plan de imagen de filminas específicas antes de generar

### Output
- Link directo a la presentación en Google Drive
- Resumen: N filminas generadas, N imágenes Gemini, N diagramas, tiempo total

## Context
- **Módulo:** `edu-standalone` — sin dependencia de BMAD
- **Ubicación del agente:** `salida/edu-standalone/_edu/agents/slides-publisher.md`
- **Proyecto:** paradigmas2026, UNTDF / Instituto IDEI
- **Frecuencia de uso:** una vez por topic-cycle (o al re-exportar tras correcciones)
- **Input:** `temas/{tema}/filminas.md`, `_edu/slides-config.yaml`, `_edu/secrets.local.yaml`
- **Output generado dentro del tema:**
  - `temas/{tema}/slides/publish_slides.py` — script Python listo para ejecutar
  - `temas/{tema}/slides/slide-plan.yaml` — plan de imágenes aprobado
  - `temas/{tema}/slides/slides-url.txt` — link de la presentación generada
- **Prerequisitos:** Vera debe haber corrido (`_edu/slides-config.yaml` existe) + secrets configurados
- **Invocado desde:** `/edu_slides_publisher` (directo) o `/edu_publish_slides` (orquestado)
- **Lenguaje de implementación del script generado:** Python (google-api-python-client + google-generativeai)
- **Sin BMAD:** no carga workflows BMAD, standalone puro

## Users
- **Docente:** Matiasgel — nivel intermedio
- **Interacción esperada:** mínima — el docente aprueba el plan de imágenes y luego espera el link
- **Flujo feliz:** 2-3 interacciones (ver reporte pre-vuelo → aprobar plan → recibir link)

## Metadata

```yaml
hasSidecar: false
sidecar_rationale: |
  Cada exportación es independiente. El estado se persiste en
  temas/{tema}/slides/ (externo al agente). No necesita memoria propia.

metadata:
  id: slides-publisher
  name: Diego
  title: Slides Publisher — Google Slides Exporter
  icon: 🚀
  module: edu:publisher:slides-publisher
  hasSidecar: false
```
