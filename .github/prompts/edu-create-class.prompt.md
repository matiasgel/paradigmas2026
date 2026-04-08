---
description: 'EDU Fase 3: Crear clase — genera minuta.md y filminas.md en el directorio del tema'
agent: 'edu-agent-class-writer'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables.
   If not found → "Primero iniciá un tema con /edu-design-topic" → STOP.
3. Load `{project-root}/{topic_folder}/topic.yaml` and store all fields as session variables.
4. Check if `{project-root}/_edu/templates/class-template.md` exists.
   If yes → load it and pass it to Roberto as the structural constraint for minuta.md y filminas.md.
5. Check if `{project-root}/_edu/templates/filminas-template.md` and `{project-root}/_edu/templates/filminas-schema.yaml` exist.
   If yes → load both and pass to Roberto as the canonical filminas authoring contract.
   Also load `{project-root}/_edu/schemas/schema-registry.json` for the canonical type enum — Roberto must use ONLY types from `canonical_types` when assigning `@tipo:` directives.
6. If `{project-root}/{topic_folder}/minuta.md` or `{project-root}/{topic_folder}/filminas.md` already exist, load them and pass them to Roberto as baseline a mejorar, no como artefactos a ignorar.
7. If extracted source material exists under `{project-root}/material/{topic_number}-*/txt/`, load the available `.txt` files and pass them to Roberto as factual reference for improvements.
8. Require that every slide with `@imagen: background|content` includes either `@prompt-imagen:` or an `@asset:` directive with a non-empty `prompt="..."` tied to the topic of that slide.
9. Require that any extra material Roberto creates for the class (`minuta.md`, transiciones, notas docentes, ejemplos, bloques introductorios) remains coherent with `filminas.md`: misma secuencia conceptual, mismos ejemplos centrales, misma terminología y mismas decisiones pedagógicas.
10. Load and follow the workflow at `{project-root}/_edu/workflows/topic-cycle/workflow.md`.
11. Purpose: Generate `{topic_folder}/minuta.md` and `{topic_folder}/filminas.md`.
   Content proportional to `class_duration` from topic.yaml. Requires approved diseno.md.

