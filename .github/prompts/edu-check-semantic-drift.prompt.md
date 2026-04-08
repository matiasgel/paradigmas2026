---
description: 'EDU: Detectar inconsistencias semánticas y drift de vocabulario entre clases'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Run: `cd {project-root} && python scripts/semantic_drift_detector.py --course {course_id}`
3. Display the consistency report:
   - 🔴 Inconsistencies (same term defined contradictorily across classes)
   - ⚠️ Complementary definitions (partial definitions, possibly intentional)
   - ✅ Consistent terms
4. Show narrative coherence analysis: abrupt topic jumps between consecutive classes.
5. Suggest specific fixes for any inconsistencies found.
