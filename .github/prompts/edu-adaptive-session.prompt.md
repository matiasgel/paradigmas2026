---
description: 'EDU: Iniciar sesión de aprendizaje adaptativo con un estudiante'
tools: ['read', 'write', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Ask for student ID and course ID.
3. Run `python scripts/adaptive_tutor.py --course {course_id} --student {student_id} summary` to show current state.
4. Run `python scripts/adaptive_tutor.py --course {course_id} --student {student_id} recommend` to get next concept.
5. Generate an explanation of the recommended concept.
6. After the student demonstrates understanding, update:
   `python scripts/adaptive_tutor.py --course {course_id} --student {student_id} update --concept {concept} --correct`
7. Repeat from step 3 for a continuous session.
8. For a web interface, suggest: `streamlit run app_adaptive.py`.
