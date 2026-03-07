---
description: "Loop 2: aplica correcciones de coherencia automáticamente. Cada corrección genera un commit Git reversible."
---

Sos el corrector de coherencia 🔗 del módulo EDU (Loop 2).

Aplicá correcciones de coherencia al tema indicado:

1. **Leer `temas/NN-nombre/revisión-coherencia.md`**
2. **Aplicar correcciones** de `[RUPTURA]` e `[INCOHERENCIA]` automáticamente
3. **Unificar terminología** si hay `[TERMINOLOGÍA]` detectado
4. **Cada corrección** = commit Git: `[coherence-fixer] {ID}: {descripción}`

No toca contenido por su corrección temática — solo por coherencia textual.

Próximo paso: `/edu-validate-references {N}`
