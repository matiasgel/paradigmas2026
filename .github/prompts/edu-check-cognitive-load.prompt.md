---
description: 'EDU: Analizar presupuesto cognitivo de una clase'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Run: `cd {project-root} && python scripts/cognitive_budget.py --topic {topic_id} --course {course_id}`
3. Display the cognitive load curve and key findings:
   - Where fatigue is expected to set in
   - Whether the intensity pattern follows an inverted U-curve
   - Specific slides that contribute most to overload
4. Suggest where to insert attention resets (socratic questions, demos, pauses).
