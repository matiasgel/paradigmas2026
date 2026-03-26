---
description: 'EDU: Ver estado de un proyecto PBL activo'
tools: ['read']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Look for PBL project files in `{course_output_folder}/pbl/`.
3. For each active PBL project:
   - Show progress per milestone (completed/in-progress/not-started)
   - Show team submissions status (if GitHub Classroom is enabled)
   - Show upcoming deadlines
4. If no PBL projects exist, suggest running `/edu-create-pbl`.
