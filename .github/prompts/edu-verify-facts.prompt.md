---
description: 'EDU: Verificar hechos del contenido generado contra fuentes primarias (NLI)'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Run: `cd {project-root} && python scripts/fact_verifier.py --topic {topic_id} --course {course_id}`
3. Display the fact-check report:
   - ✅ ENTAILMENT: verified claims
   - ❌ CONTRADICTION: refuted claims — MUST be reviewed by the teacher
   - ⚠️ NEUTRAL: insufficient evidence
4. If any claim has verdict ❌, warn the user that these MUST be corrected before publishing.
5. The script exits with code 1 if contradictions are found (blocks CI pipelines).
