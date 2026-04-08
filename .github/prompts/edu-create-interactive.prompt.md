---
description: 'EDU: Generar simulación HTML interactiva para un concepto'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. If `interactive_scenes_enabled` is false, inform the user how to enable it and exit.
3. Ask the user for the simulation type (sorting-visualizer, tree-explorer, stack-simulator, fsm-simulator, memory-layout, custom) and the concept to simulate.
4. Create an `interactive-spec.json` file in the topic's `interactivos/` folder with the spec.
5. Run: `cd {project-root} && python scripts/generate_interactive.py --spec {spec_path} --topic {topic_id} --course {course_id}`
6. Verify the generated HTML is self-contained (<500KB, opens with file://).
7. Suggest adding `<!-- interactive: simulacion-{name}.html -->` in `filminas.md` to link the simulation.
