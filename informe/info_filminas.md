# Informe tecnico sobre generacion de filminas

Fecha: 2026-03-25
Repositorio analizado: paradigmas2026
Objetivo: dejar un paquete autocontenido para que otro modelo pueda entender, auditar y mejorar el pipeline de generacion/publicacion de filminas sin depender del repo original.

## 1. Alcance del relevamiento

Este informe cubre:

- la evolucion del pipeline de filminas y Google Slides;
- los scripts y contratos usados realmente para el tema 00 y el tema 01;
- los cambios posteriores incorporados a partir de errores y correcciones;
- la evidencia concreta disponible en Git y en los artefactos del repo;
- los archivos ya usados y los archivos que probablemente haya que usar en la siguiente iteracion.

El paquete autocontenido quedo armado en `informe/archivos/` y conserva rutas relativas del repo para facilitar lectura automatica.

## 2. Resumen ejecutivo

Hallazgos principales:

1. El pipeline tecnico de filminas se consolida entre el 16 y el 19 de marzo de 2026. Primero aparece `scripts/slides_pipeline.py` como publicador tecnico y despues se agregan validacion, captura de thumbnails, parseo v2, reparacion iterativa y tests de contrato.
2. El tema 00 (`00-nivelacion-html-css-prompting`) fue el banco de pruebas real. Quedo evidencia de multiples rondas de correccion visual en `slides/thumbnails/`, `slides/thumbnails-fixed/`, `slides/thumbnails-fixed-v2/` y `slides/thumbnails-fixed-v3/`.
3. El tema 01 (`01-diseno-agil-python`) ya usa el flujo mas maduro: `filminas.md` -> `plan-draft-*.yaml` -> `plan-filminas-*.yaml` -> `assets-manifest.yaml` + `publish-context.yaml` -> publicacion.
4. El cambio mas importante de arquitectura es el pasaje a `filminas/v2`: el parser ya no infiere tipos de slide. Si falta `@tipo:`, el slide queda `pending` y debe resolverse antes de publicar.
5. La principal leccion operativa posterior es el endurecimiento de prompts visuales para Gemini: no nombrar conceptos tecnicos, describir solo geometria visual. Esto esta documentado como correccion anti-Bug 3.
6. Hay una divergencia importante entre documentacion y runtime: `slides-plan-schema.yaml` declara un modelo de plan unico por tema, pero la implementacion actual todavia usa tres artefactos separados (`plan-filminas`, `assets-manifest`, `publish-context`). Cualquier mejora futura debe decidir si converger documentacion hacia runtime o runtime hacia contrato.

## 3. Flujo real reconstruido

Flujo vigente reconstruido desde scripts, prompts y artefactos:

1. Diseno visual del cursado
   Archivo base: `_edu/slides-config.yaml`.
   Fuente conceptual: `_edu/agents/slides-designer.md` y `.github/prompts/edu-slides-designer.prompt.md`.
   Rol: define template de Google Slides, paleta, tipografia, layout canonico por tipo de slide y reglas de render Markdown.

2. Autoria de filminas
   Archivo fuente por tema: `{tema}/filminas.md`.
   Contrato humano/canonico: `_edu/templates/filminas-template.md` y `_edu/templates/filminas-schema.yaml`.

3. Parseo a borrador tecnico
   Script: `scripts/parse_filminas.py`.
   Salida: `slides/plan-draft-{tema}.yaml`.
   Regla central: sin `@tipo:` explicito no hay inferencia; el slide queda `pending`.

4. Complecion semantica del plan
   Actor: agente o correccion humana.
   Resultado: `slides/plan-filminas-{tema}.yaml`.

5. Validacion y reparacion
   Scripts: `scripts/validate_plan.py` y `scripts/repair_plan.py`.
   Objetivo: validar tipos, layout, prompts de imagen, presupuesto de imagenes y estado no-DRAFT.

6. Generacion de assets y publicacion
   Script principal: `scripts/slides_pipeline.py`.
   Salidas observadas en runtime actual:
   - `slides/plan-filminas-{tema}.yaml`
   - `slides/assets-manifest.yaml`
   - `slides/publish-context.yaml`
   - `slides/assets/` cuando existen assets locales
   - `slides/slides-url.txt` cuando la publicacion se completa

7. Auditoria visual posterior
   Script auxiliar: `scripts/capture_thumbnails.py`.
   Uso probado en tema 00 para comparar versiones visuales y detectar problemas de layout o imagen.

## 4. Linea de tiempo de cambios relevantes

Cronologia condensada de los commits mas importantes para filminas:

| Fecha | Commit | Cambio relevante |
|------|--------|------------------|
| 2026-03-10 | `bfbcb72` | Se despliegan prompts y agentes de slides al repo operativo. |
| 2026-03-16 | `d68fc86` | Aparecen `scripts/slides_pipeline.py`, `scripts/goproduction.py`, `requirements.txt` y `scripts/requirements.txt`. Nace el pipeline tecnico. |
| 2026-03-17 | `e8b80dd` | Se actualizan `README.md`, `scripts/slides_pipeline.py`, `scripts/test_slides_contract.py` y agentes de slides. |
| 2026-03-18 | `de09fbd` | Se incorporan wrappers `.github/agents/*slides*` y ajustes de prompts/README/pipeline. |
| 2026-03-19 | `9a074a4` | Se agregan `scripts/validate_plan.py` y `scripts/capture_thumbnails.py`; se endurece el circuito de validacion/QA visual. |
| 2026-03-19 | `468d664` | Se agregan `scripts/parse_filminas.py`, `scripts/repair_plan.py` y mejoras de contrato/test. Se formaliza el flujo v2 con `pending`. |
| 2026-03-24 | `827fc07` | Se crea el tema 00 con `diseno.md`, `minuta.md`, `filminas.md` y `topic.yaml`. |
| 2026-03-25 | `a29e3de` | Nace el tema 01: `diseno.md` y `topic.yaml`. |
| 2026-03-25 | `7ee3ab5` | Se actualizan `slides-config`, `filminas-template`, `filminas-schema`, `slides-plan-schema` y la guia de prompts de imagen. |
| 2026-03-25 | `9da952b` | Se agregan `slides-pipeline.json`, wrappers standalone y los artefactos concretos de tema 00 y tema 01. |

Para trazabilidad completa quedaron dos volcados en bruto:

- `archivos/git/git-log-filminas.txt`
- `archivos/git/git-log-filminas-name-only.txt`

## 5. Tema 00 como banco de pruebas

El tema 00 es la mejor evidencia de aprendizaje operativo del pipeline.

Evidencia copiada:

- carpeta completa `archivos/salida/cursadas/2026/temas/00-nivelacion-html-css-prompting/`
- reportes de calidad curricular y de escritura;
- `slides/plan-draft-00-...yaml`, `slides/plan-filminas-00-...yaml`, `slides/assets-manifest.yaml`, `slides/publish-context.yaml`;
- cuatro generaciones de thumbnails: `thumbnails`, `thumbnails-fixed`, `thumbnails-fixed-v2`, `thumbnails-fixed-v3`.

Lo que muestra ese tema:

1. El pipeline ya publicaba y capturaba slides el 25-03.
2. Hubo por lo menos tres rondas de correccion visual posteriores a la publicacion inicial.
3. Los prompts de imagen y las decisiones de layout fueron corregidos con evidencia visual, no solo textual.
4. El tema 00 fue el lugar donde maduro la regla anti-texto en imagenes Gemini y donde se incorporaron tipos nuevos como `concepto-mixto` y `tabla-mixta`.

Datos observables del plan final de tema 00:

- `total_slides: 39`
- `images_planned: 12`
- `status: READY_FOR_VALIDATION`
- `publish-context.generated_at: 2026-03-25T12:54:00`

## 6. Tema 01 como primer caso maduro

El tema 01 es el primer caso donde se ve el flujo casi completo y mas limpio.

Artefactos clave copiados:

- `archivos/salida/cursadas/2026/temas/01-diseno-agil-python/filminas.md`
- `archivos/salida/cursadas/2026/temas/01-diseno-agil-python/diseno.md`
- `archivos/salida/cursadas/2026/temas/01-diseno-agil-python/minuta.md`
- `archivos/salida/cursadas/2026/temas/01-diseno-agil-python/minuta-por-filmina.md`
- `archivos/salida/cursadas/2026/temas/01-diseno-agil-python/guia-estudio.md`
- `archivos/salida/cursadas/2026/temas/01-diseno-agil-python/guiaprofesor.md`
- `archivos/salida/cursadas/2026/temas/01-diseno-agil-python/slides/plan-draft-01-diseno-agil-python.yaml`
- `archivos/salida/cursadas/2026/temas/01-diseno-agil-python/slides/plan-filminas-01-diseno-agil-python.yaml`
- `archivos/salida/cursadas/2026/temas/01-diseno-agil-python/slides/assets-manifest.yaml`
- `archivos/salida/cursadas/2026/temas/01-diseno-agil-python/slides/publish-context.yaml`

Reconstruccion del flujo de tema 01:

1. Se crea `diseno.md` y `topic.yaml` en `a29e3de`.
2. `filminas.md` se redacta con contrato v2, ya usando `@tipo:` y prompts visuales puros.
3. `scripts/parse_filminas.py` genera `plan-draft-01-diseno-agil-python.yaml`.
   Evidencia: `generated_at: 2026-03-25T14:34:15` y `status: DRAFT`.
4. El borrador todavia mostraba `pending_prompts: 20`, o sea, la etapa humana/agente seguia siendo necesaria.
5. Luego se resuelve `plan-filminas-01-diseno-agil-python.yaml`.
   Evidencia: `generated_at: 2026-03-25T17:37:27Z`, `status: READY_FOR_VALIDATION`, `pending_types: 0`, `pending_prompts: 0`, `known_types: 85`.
6. El mismo momento temporal aparece en `publish-context.yaml`, lo que indica que el plan final y el contexto de publicacion quedaron sincronizados.
7. `assets-manifest.yaml` enumera los assets a generar/subir para la presentacion final.

Datos importantes de tema 01:

- `total_slides: 85`
- `images_planned: 12`
- hay `drive_id` persistidos dentro del plan final;
- ya se observa mezcla madura de `background_image`, `content_image` y `table_assets`.

Conclusion operativa sobre tema 01:

Tema 01 no fue solo una redaccion de `filminas.md`; fue una ejecucion real del pipeline moderno, con contrato v2, artefactos tecnicos separados y persistencia de IDs de Drive dentro del plan.

## 7. Scripts y archivos usados directamente

### 7.1 Scripts nucleares

- `archivos/scripts/slides_pipeline.py`
  Publicador tecnico. Valida artefactos, genera imagenes/tablas, sube assets a Drive y crea la presentacion en Google Slides.

- `archivos/scripts/parse_filminas.py`
  Convierte `filminas.md` a `plan-draft`. Introduce la regla `pending` y obliga a resolver semantica antes de publicar.

- `archivos/scripts/validate_plan.py`
  Validador estructural del plan final.

- `archivos/scripts/repair_plan.py`
  Orquestador de iteraciones agente -> validacion -> correccion.

- `archivos/scripts/capture_thumbnails.py`
  QA visual posterior a publicacion. Muy importante para el aprendizaje observado en tema 00.

- `archivos/scripts/test_slides_contract.py`
  Tests de regresion del contrato. Verifica metadata de schema, `pending` sin `@tipo:` y errores rapidos ante directivas invalidas.

### 7.2 Scripts perifericos pero relevantes

- `archivos/scripts/goproduction.py`
  No genera filminas, pero explica como el pipeline y los prompts llegan a ramas operativas (`production`, `lenguajes`, `lenguajes2026`). Es relevante para entender por que muchos cambios aparecen como commits de deploy.

- `archivos/salida/edu-standalone/scripts/parse_filminas.py`
- `archivos/salida/edu-standalone/scripts/slides_pipeline.py`

Esos dos wrappers muestran que el repo mantiene una variante desplegable en `salida/edu-standalone/`.

### 7.3 Contratos y configuracion

- `archivos/_edu/slides-config.yaml`
- `archivos/_edu/slides-pipeline.json`
- `archivos/_edu/templates/filminas-template.md`
- `archivos/_edu/templates/filminas-schema.yaml`
- `archivos/_edu/templates/slides-plan-schema.yaml`
- `archivos/_edu/templates/prompt-imagen-guide.md`
- `archivos/_edu/config.yaml`

Estos archivos son los contratos que otro modelo debe leer antes de proponer mejoras.

### 7.4 Agentes y prompts que explican la intencion del sistema

- `archivos/_edu/agents/slides-designer.md`
- `archivos/_edu/agents/slides-publisher.md`
- `archivos/.github/agents/edu-agent-slides-designer.agent.md`
- `archivos/.github/agents/edu-agent-slides-publisher.agent.md`
- `archivos/.github/prompts/edu-slides-designer.prompt.md`
- `archivos/.github/prompts/edu-slides-publisher.prompt.md`
- `archivos/.github/prompts/edu-publish-slides.prompt.md`

Estos archivos son utiles porque explican la separacion de responsabilidades entre Vera (sistema de diseno) y Diego (planeamiento semantico + publish).

## 8. Cambios posteriores mas importantes

Cambios posteriores a la primera idea de pipeline que importan para cualquier mejora futura:

1. `filminas/v2` y tipos explicitos
   El parser deja de inferir tipo de slide. Esto evita falsos positivos y fuerza control semantico explicito.

2. Tipos nuevos `concepto-mixto` y `tabla-mixta`
   Se agregan para resolver slides donde antes se perdia codigo o tabla al mezclar formatos.

3. Prompt visual puro anti-Bug 3
   Se incorpora la guia `prompt-imagen-guide.md` con ejemplos correctos/incorrectos para evitar que Gemini escriba texto dentro de la imagen.

4. Validacion previa obligatoria
   `validate_plan.py` y `repair_plan.py` cortan el flujo antes de publicar si faltan prompts, layouts o tipos.

5. Runtime parametrizable
   `slides-pipeline.json` pasa a concentrar geometria, rendering y `slide_types` sobreescribibles por tema.

6. QA visual por thumbnails
   El tema 00 evidencia que la mejora real no fue solo textual; hubo un ciclo de captura y reinspeccion de thumbnails.

## 9. Inconsistencias, huecos y riesgos detectados

1. Divergencia contrato/runtime
   `slides-plan-schema.yaml` habla de un solo archivo de plan, pero el runtime actual sigue usando `assets-manifest.yaml` y `publish-context.yaml` como artefactos separados.

2. El deploy mete ruido en la historia
   Muchos commits relevantes aparecen como `deploy: edu-standalone -> lenguajes`. Para una futura mineria automatica de cambios hay que separar commits de producto de commits de despliegue.

3. Tema 03 todavia no esta migrado al contrato v2 en disco
   El contenido visible en el editor usa encabezados `### [1]`, `### [2]`, etc., no `### [F-01]`. Tambien conserva prompts con lenguaje conceptual (`lambda symbol`, `Hilbert`, etc.) que chocan con la regla visual pura introducida luego.

4. Los wrappers standalone no cubren todos los auxiliares
   Quedaron wrappers para `parse_filminas.py` y `slides_pipeline.py`, pero no se observo el mismo despliegue espejo para todos los scripts auxiliares de validacion/reparacion.

## 10. Archivos por usar en la siguiente iteracion

Archivos que probablemente entren en la proxima mejora/generacion:

- `archivos/salida/cursadas/2026/temas/03-intro-funcional-ts/filminas.editor-context.partial.md`
  Snapshot parcial del contenido visible en el editor. No existia persistido en disco al momento del relevamiento, por eso se guarda como referencia parcial. Sirve para comparar el estado actual del tema 03 contra el contrato v2.

- `archivos/_edu/slides-pipeline.json`
  Es el punto mas natural para mejoras de geometria y rendering sin romper semantica.

- `archivos/_edu/templates/filminas-schema.yaml`
  Es el punto correcto si se quiere endurecer el contrato de autoria.

- `archivos/scripts/parse_filminas.py`
  Es el punto correcto si se quiere mejorar el paso de `filminas.md` a `plan-draft`.

- `archivos/scripts/validate_plan.py`
  Es el punto correcto si se quiere cerrar huecos del contrato antes de publicar.

## 11. Recomendacion para otro LLM

Orden sugerido de lectura para mejorar el sistema sin romperlo:

1. `archivos/_edu/templates/filminas-schema.yaml`
2. `archivos/_edu/templates/filminas-template.md`
3. `archivos/_edu/slides-config.yaml`
4. `archivos/_edu/slides-pipeline.json`
5. `archivos/scripts/parse_filminas.py`
6. `archivos/scripts/validate_plan.py`
7. `archivos/scripts/repair_plan.py`
8. `archivos/scripts/slides_pipeline.py`
9. `archivos/salida/cursadas/2026/temas/00-nivelacion-html-css-prompting/`
10. `archivos/salida/cursadas/2026/temas/01-diseno-agil-python/`
11. `archivos/git/git-log-filminas-name-only.txt`
12. `archivos/git/git-log-filminas.txt`

Si hubiera que elegir una sola referencia empirica para aprender del comportamiento real del sistema:

- usar tema 00 para entender correcciones visuales y bugs;
- usar tema 01 para entender el flujo maduro y el contrato ya estabilizado.

## 12. Inventario resumido del paquete autocontenido

El paquete `informe/archivos/` contiene:

- scripts del pipeline;
- contratos y templates;
- prompts/agentes de slides;
- `README.md` y archivos de requirements;
- directorio completo del tema 00;
- directorio completo del tema 01;
- snapshot parcial del tema 03 visible en el editor;
- historial Git bruto filtrado a filminas.

Esto alcanza para que otro modelo:

- reconstruya la evolucion del pipeline;
- compare la intencion del contrato con la implementacion real;
- use tema 00 y tema 01 como dataset de evidencia;
- proponga mejoras sin depender del repo original.
