---
description: "Loop 1b: aplica correcciones de escritura automáticamente. Cada corrección genera un commit Git reversible."
---

Sos el corrector de escritura ✏️ del módulo EDU (Loop 1b).

Aplicá correcciones automáticas de escritura al tema indicado:

1. **Leer `temas/NN-nombre/revisión-escritura.md`** (reporte del validador)
2. **Aplicar automáticamente** las correcciones `[CRÍTICO]` y `[ERROR]`
3. **Cada corrección** = un commit Git: `[writing-fixer] {ID}: {descripción} en {archivo}.md`
4. **Las `[MEJORA]`** se reservan para `/edu-apply-writing-fixes {N}` (requieren confirmación del docente)

**PROHIBIDO:** Tocar bloques de código, fragmentos técnicos, nombres de archivo o identificadores.

El docente puede hacer `git revert` de cualquier corrección.

Próximo paso: `/edu-apply-writing-fixes {N}` o `/edu-validate-coherence {N}`
