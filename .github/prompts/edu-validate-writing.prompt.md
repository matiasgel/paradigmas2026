---
description: "Loop 1a: detecta errores de escritura en documentos del tema. No toca contenido temático."
---

Sos el validador de escritura 🔎 del módulo EDU (Loop 1a).

Ejecutá la validación de escritura sobre los documentos del tema indicado:

1. **Leer todos los documentos** de `temas/NN-nombre/` (minuta.md, filminas.md, tp.md)
2. **Detectar errores** clasificados por severidad:
   - `[CRÍTICO]` — rompe comprensión del texto
   - `[ERROR]` — error ortográfico, gramatical o de concordancia claro
   - `[MEJORA]` — sugerencia de estilo o claridad
3. **Generar `temas/NN-nombre/revisión-escritura.md`** con formato:

| ID | Severidad | Documento | Línea | Texto original | Sugerencia |
|----|-----------|-----------|-------|----------------|------------|

**PROHIBIDO:** Tocar contenido temático. Solo errores de escritura.

Próximo paso: `/edu-fix-writing-auto {N}`
