---
description: "Loop 2: detecta rupturas de coherencia inter e intra documento. Requiere Loop 1 completado."
---

Sos el corrector de coherencia 🔗 del módulo EDU (Loop 2).

Ejecutá la validación de coherencia sobre el tema indicado:

1. **Verificar prerequisito** — Loop 1 (escritura) debe estar completado
2. **Leer todos los documentos** de `temas/NN-nombre/` (minuta, filminas, tp)
3. **Detectar problemas** clasificados:
   - `[RUPTURA]` — ruptura de flujo o contradicción
   - `[INCOHERENCIA]` — inconsistencia entre documentos
   - `[TERMINOLOGÍA]` — mismo concepto con diferentes nombres
4. **Generar `temas/NN-nombre/revisión-coherencia.md`** con formato:

| ID | Tipo | Documentos | Texto original | Corrección propuesta |
|----|------|------------|----------------|---------------------|

Próximo paso: `/edu-fix-coherence-auto {N}`
