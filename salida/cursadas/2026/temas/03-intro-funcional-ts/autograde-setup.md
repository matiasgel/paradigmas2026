# Configuración del Repo Autograde

Este archivo contiene instrucciones para publicar el repositorio en GitHub Classroom y habilitar el autograding.

## Pasos sugeridos

1. Crear un nuevo repositorio en GitHub (o usar GitHub Classroom) usando **esta plantilla**.
2. En la sección de Actions, verificar que el workflow `CI` se ejecute correctamente.
3. Verificar que `npm test` pase en el pipeline.

## Estructura del repositorio
- `src/` — código entregable.
- `__tests__/` — pruebas automáticas.
- `.github/workflows/ci.yml` — pipeline de evaluación.

## Cómo corregir
- Si el estudiante no implementa `esFuncionPura` o `aplicarMap`, el pipeline fallará.
- Para agregar nuevas preguntas, añadir tests en `__tests__/`.
