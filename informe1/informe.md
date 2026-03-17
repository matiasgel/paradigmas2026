# Informe de publicación de slides — Tema 01

**Fecha:** 17/03/2026

## 1) Objetivo
Generar y publicar en Google Slides las filminas correspondientes al **Tema 01: Conceptos Introductorios + Intro a TypeScript**, manteniendo `filminas.md` inmutable.

## 2) Archivos usados en el proceso (copiados a `informe1/`)
- `scripts/slides_pipeline.py` (pipeline de publicación)
- `_edu/secrets.local.yaml` (credenciales Google + Gemini API)
- `_edu/slides-config.yaml` (configuración visual y template)
- `salida/cursadas/2026/temas/01-conceptos-introductorios/filminas.md` (fuente de las slides)
- `salida/cursadas/2026/temas/01-conceptos-introductorios/slides/plan-filminas-01-conceptos-introductorios.yaml` (plan generado por el pipeline)

## 3) Pasos ejecutados
1. Verificar que existieran:
   - `_edu/secrets.local.yaml`
   - `_edu/slides-config.yaml`
   - `filminas.md` en el tema activo

2. Instalar dependencias Python en el entorno virtual (`.venv`) mediante:
   ```bash
   pip install -r scripts/requirements.txt
   ```

3. Ejecutar la publicación con:
   ```bash
   python scripts/slides_pipeline.py salida/cursadas/2026/temas/01-conceptos-introductorios
   ```

4. Ajustar el parser de `filminas.md` para aceptar numeración `### [N]` (sin prefijo `F-`) y no alterar el archivo original.

5. Ajustar el posicionamiento y color del título en la slide para que se vea más visible (más arriba + rojo institucional).

## 4) Resultados
- Se generaron **47 slides** a partir de `filminas.md`.
- Se creó la presentación en Google Slides:
  https://docs.google.com/presentation/d/1qhkyWzSvcM5CHMQn1S7schaBD5rCfcIMM1BxPovCwdg/edit

## 5) Notas adicionales
- El archivo `filminas.md` no fue modificado en el proceso: el parser del pipeline fue adaptado para aceptar el formato existente.
- Todos los archivos relevantes al proceso fueron copiados a `informe1/` para auditoría y reproducibilidad.
