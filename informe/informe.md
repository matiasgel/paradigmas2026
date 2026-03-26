# Paquete autocontenido para analizar y mejorar filminas

Este directorio resume y empaqueta la evidencia relevante del pipeline de filminas.

## Archivos principales

- `info_filminas.md`: informe tecnico completo con hallazgos, linea de tiempo y recomendaciones.
- `archivos/`: copia autocontenida de scripts, contratos, prompts, configuracion y temas usados como evidencia.

## Como leer este paquete

Orden recomendado:

1. `info_filminas.md`
2. `archivos/_edu/templates/filminas-schema.yaml`
3. `archivos/scripts/parse_filminas.py`
4. `archivos/scripts/validate_plan.py`
5. `archivos/scripts/slides_pipeline.py`
6. `archivos/salida/cursadas/2026/temas/00-nivelacion-html-css-prompting/`
7. `archivos/salida/cursadas/2026/temas/01-diseno-agil-python/`
8. `archivos/git/git-log-filminas-name-only.txt`
9. `archivos/git/git-log-filminas.txt`

## Que incluye `archivos/`

- scripts usados y scripts modificados del pipeline;
- configuracion de slides y contratos canonicos;
- prompts/agentes relacionados con publicacion de filminas;
- artefactos completos de tema 00 y tema 01;
- snapshot parcial del tema 03 visible en el editor, como referencia de lo que queda por migrar;
- trazas Git en bruto para una auditoria mas fina.

## Nota importante

El tema 03 no estaba persistido en disco al momento del relevamiento. Por eso se guardo como snapshot parcial de contexto del editor en:

- `archivos/salida/cursadas/2026/temas/03-intro-funcional-ts/filminas.editor-context.partial.md`

El detalle y el motivo estan explicados en `info_filminas.md`.
