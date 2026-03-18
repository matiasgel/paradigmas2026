# Minuta — Tema 04: Pruebas de Filminas

## Objetivo docente

Usar una clase artificial y corta para validar que el flujo `filminas.md -> plan YAML -> publicación` preserve estructura semántica y no dependa de inferencias frágiles.

## Recorrido sugerido

### Bloque 1 — Contrato canónico

- Explicar por qué las filminas no pueden depender de heurísticas ambiguas.
- Mostrar la diferencia entre título de slide, subtítulo visible y cuerpo.
- Recordar que `### [F-XX]` identifica la slide, mientras que el primer `#` define el subtítulo.

### Bloque 2 — Casos que suelen romperse

- Listas que quedan como texto plano.
- Código que desborda el cuadro.
- Tablas sin contexto previo.
- Diagramas cuya intención visual no está declarada.

### Bloque 3 — Directivas explícitas

- Introducir `@tipo`, `@layout`, `@imagen` y `@asset`.
- Explicar que se usan sólo cuando el contenido no alcanza para desambiguar.

### Bloque 4 — Cierre

- El contrato debe poder ser leído por un humano, por un modelo simple y por el pipeline.
- Si una slide necesita adivinación, el problema está en el origen y no en el publicador.