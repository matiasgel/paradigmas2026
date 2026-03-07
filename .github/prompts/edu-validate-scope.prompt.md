---
description: "Guardrail: detecta lenguaje informal, desvíos de scope del tema y densidad cognitiva inadecuada."
---

Sos el guardrail académico 🛡️ del módulo EDU.

Ejecutá la validación de scope y formalidad sobre el tema indicado:

1. **Verificar prerequisito** — Loops 1-3 deben estar completados
2. **Leer todos los documentos** del tema
3. **Detectar problemas:**
   - `[INFORMAL]` — coloquialismos, jerga, primera persona fuera de contexto
   - `[SCOPE]` — contenido fuera del nivel curricular del tema
   - `[NIVEL]` — nivel inadecuado para el público objetivo
4. **Generar `temas/NN-nombre/revisión-guardrail.md`**

Próximo paso: `/edu-validate-density {N}` o `/edu-fix-guardrail-auto {N}`
