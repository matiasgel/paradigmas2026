# Retrospectiva Sprint 5 — E3: Coherencia curricular

**Sprint:** 5
**Epic:** E3 — Coherencia curricular
**Fecha:** 2026-05-23
**Stories completadas:** 3.1, 3.2, 3.3 (3/3)

---

## Qué salió bien

- **Escaneo sin ChromaDB:** La coherencia curricular se implementa leyendo `topic-extract.md` de temas previos a nivel de texto local, sin depender de `chroma-mcp`. Correcto: el escaneo puede hacerse antes de verificar el server.
- **Patrón de escalada correcto:** Alto→asumir-conocido, Medio→resumir, Bajo→asumir-conocido. Los defaults evitan que el docente tenga que responder para cada concepto.
- **Integración con schema:** La sección `superposiciones-detectadas` ya estaba en el schema. E3 solo agrega la lógica de cómo poblarla.
- **CP1 como punto de revisión:** El docente puede modificar las estrategias en CP1 si no está de acuerdo con el análisis automático.

## Decisiones de diseño notables

- **Solo temas con aprobado_en no nulo:** El escaneo ignora temas en progreso o v2. Evita falsos positivos de temas que no se enseñaron completamente.
- **Estrategia "desarrollar" = NO incluir en superposiciones:** Si el docente quiere enseñar el concepto con profundidad normal, simplemente no se lista como superposición. Elegante y consistente.

## Qué se mejoraría

- El algoritmo de comparación (fuzzy match) no está especificado con precisión técnica. En una implementación real se debería definir el threshold de similitud.

## Deuda técnica

- El parámetro de threshold para fuzzy matching queda sin especificar (implementado como "judgement" del agente LLM).
