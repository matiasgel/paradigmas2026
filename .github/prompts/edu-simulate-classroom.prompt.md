---
description: 'EDU: Simular clase completa con perfiles de alumnos interactuando (debate grupal)'
tools: ['read', 'write']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Read `{project-root}/_edu/templates/student-profiles-schwanke.yaml` for the 4 student archetypes.
3. Read `filminas.md` and `minuta.md` for the topic to simulate.
4. Simulate a full class with the 4 profiles interacting:
   - **Inquisitive Mind** (TI): asks "what if..." and "how does this relate to..."
   - **Deep Thinker** (ID): connects to papers, proposes alternatives
   - **Note Taker** (EC): "is this on the exam?", "can you repeat?"
   - **Distracted Student** (CM): requires re-engagement, loses thread
5. Generate turn-based dialogue: teacher → student → teacher → group debate → ...
6. Output: `{topic_folder}/simulacion/transcripcion-debate.md` + `metricas-simulacion.md`
7. Metrics include: Bloom coverage per profile, unresolved questions, engagement level per profile.
8. Register the simulation result in `memory.db` as category `simulation-result`.
