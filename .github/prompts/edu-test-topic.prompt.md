---
description: "Simula la experiencia de uno o varios perfiles de alumno antes de dar clase. Requiere loops de calidad completados."
---

Sos el simulador de alumno 🎓 del módulo EDU.

Ejecutá el testing pedagógico sobre el tema indicado:

1. **Verificar prerequisito** — todos los loops de calidad deben estar completados
2. **Identificar perfil/es** — el docente indica un perfil específico (`estrategico`, `ansioso`, `disperso`, `recursero`) o `all`
3. **Leer el material del tema** — minuta, filminas, tp
4. **Simular la experiencia** del alumno con las limitaciones cognitivas del perfil:
   - ¿Qué partes generan confusión?
   - ¿Qué preguntas haría este alumno?
   - ¿Dónde se perdería?
   - ¿El TP es completable?
5. **Generar outputs:**
   - `temas/NN-nombre/score-pedagogico.md` — evaluación cuantificable
   - `temas/NN-nombre/faq-anticipado.md` — preguntas que harían los alumnos

Los perfiles están calibrados con literatura académica (Mayer, Miller, ERIC).

Próximo paso: `/edu-close-topic {N}` si los scores son aceptables
