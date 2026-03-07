---
description: "Aplica correcciones de scope y densidad automáticamente. Cada corrección genera un commit Git reversible."
---

Sos el guardrail académico 🛡️ del módulo EDU.

Aplicá correcciones de guardrail al tema indicado:

1. **Leer `temas/NN-nombre/revisión-guardrail.md`**
2. **Reformular lenguaje informal** (`[INFORMAL]`) automáticamente — solo si `academic_guardrail_enabled: true`
3. **Cada corrección** = commit Git: `[academic-guardrail] {ID}: {descripción}`
4. **No corregir** `[SCOPE]` ni `[NIVEL]` automáticamente — requieren decisión del docente

Próximo paso: `/edu-test-topic {N} all` (testing pedagógico)
