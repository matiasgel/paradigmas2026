# Diseño del Tema 04 — Pruebas de Filminas

## Estado

- Aprobado para pruebas técnicas del pipeline de filminas.
- Objetivo principal: validar el contrato canónico de `filminas.md` y el render de Slides.

## Propósito del tema

Este tema no está pensado como contenido final de cursada. Sirve para probar, en un solo recorrido, los casos que más suelen romper la publicación:

- título y subtítulo,
- listas simples,
- headings internos del cuerpo,
- diagramas con directivas explícitas,
- código largo,
- tablas con contexto,
- cierre de clase.

## Restricción de duración

- Duración de clase objetivo: 90 minutos.
- Cantidad de filminas objetivo: entre 8 y 12.
- Densidad: baja a media, priorizando claridad sobre profundidad.

## Resultado esperado

- `minuta.md` breve, trazable a las filminas.
- `filminas.md` compatible con `_edu/templates/filminas-template.md` y `_edu/templates/filminas-schema.yaml`.
- El pipeline `slides_pipeline.py --plan-only` debe ejecutarse sin errores estructurales.

## Cobertura mínima de pruebas

1. Portada con título claro.
2. Slide conceptual con bullets.
3. Slide con heading interno `##`.
4. Slide con directiva `@tipo: diagrama`.
5. Slide con `@asset` para hint visual.
6. Slide con código suficientemente largo como para exigir ajuste tipográfico.
7. Slide con tabla y explicación previa.
8. Slide final de cierre.