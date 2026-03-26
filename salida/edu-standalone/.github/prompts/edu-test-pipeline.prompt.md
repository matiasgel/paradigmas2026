---
description: "Ejecuta el test de integración completo del pipeline de filminas. Usa informe/filminas.md como fuente de referencia y genera un reporte con capturas de cada slide en reporte/test{fecha}/"
agent: 'agent'
tools: ['read', 'edit', 'search', 'execute']
---

Ejecutar el test de integración completo del pipeline de producción de filminas.

## Instrucciones

1. Verificar que existen los prerequisitos:
   - `_edu/secrets.local.yaml` (credenciales Google + Gemini API key)
   - `_edu/slides-config.yaml` (sistema de diseño)
   - `informe/filminas.md` (fuente de referencia para el test)
   - `salida/edu-standalone/scripts/test_pipeline.py` (test runner)

2. Mostrar opciones al usuario:
   ```
   🧪 Test Pipeline de Filminas

   Modos disponibles:
   [1] Test completo (plan + assets IA + publicar + capturas)    ~5-10 min
   [2] Solo plan     (parseo filminas.md → JSON, sin APIs)       ~5 seg
   [3] Sin imágenes  (plan + publish, sin Imagen 4.0)            ~2-3 min
   [4] Desde filminas.md alternativo (pedir ruta)
   ```

3. Según la opción elegida, ejecutar el comando correspondiente:
   - [1]: `python salida/edu-standalone/scripts/test_pipeline.py`
   - [2]: `python salida/edu-standalone/scripts/test_pipeline.py --plan-only`
   - [3]: `python salida/edu-standalone/scripts/test_pipeline.py --no-images`
   - [4]: `python salida/edu-standalone/scripts/test_pipeline.py --from {ruta}`

4. Una vez completado, reportar:
   - Ruta del directorio generado: `reporte/test{YYYYMMDD_HHMMSS}/`
   - Número de filminas procesadas
   - Número de capturas generadas
   - Errores encontrados (si los hay)
   - Link al `report.html` generado (abrir con Live Server o navegador)

5. Si hay errores, diagnosticar y sugerir correcciones.

## Artefactos generados

```
reporte/test{YYYYMMDD_HHMMSS}/
  filminas.md           — copia del filminas.md de entrada
  slides-config.yaml    — copia de la config usada
  plan.json             — plan JSON v3 generado (copia del tema-test/)
  assets/               — imágenes IA + tablas PNG locales
  filminas/             — capturas de Google Slides (filmina_01.png, ...)
  report.html           — informe visual con thumbnails y estado de fases
  test-meta.yaml        — metadatos del run (timings, errores)
  tema-test/            — carpeta de trabajo del pipeline
    slides/
      plan-filminas-tema-test.json
      assets/
```
