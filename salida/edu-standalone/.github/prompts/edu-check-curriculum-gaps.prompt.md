---
description: 'EDU: Detectar gaps y redundancias curriculares comparando plan vs artefactos'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. If `topic_analysis_enabled` is false, inform the user how to enable it and exit.
3. Run: `cd {project-root} && python scripts/curriculum_topic_analyzer.py --course {course_id}`
4. Display the gaps report:
   - 🔴 GAP: topics in plan-minimo not covered in any artifact
   - 🟡 Partial GAP: topics in minutas but not in filminas
   - ⚠️ REDUNDANCY: topics appearing in >3 different themes
5. Show the coverage matrix and suggest which themes need attention.
