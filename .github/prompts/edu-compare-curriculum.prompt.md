---
description: 'EDU: Comparar currícula local contra universidades internacionales y ACM/IEEE CC2023'
tools: ['read', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Read `plan-minimo.md` for the active course (course_id from config).
3. Compare the local program topics against:
   - ACM/IEEE CC2023 Knowledge Areas and Knowledge Units
   - MIT OCW public syllabi (courses 6.xxx)
   - Other publicly accessible CS syllabi
4. Generate a comparison report at `{course_output_folder}/comparacion-curricular.md` with:
   - Coverage matrix: topic × source
   - Gaps prioritized by academic relevance
   - Strengths of the local program
   - Emerging trends in CS education (2024-2026)
5. Remind the teacher that this is informational — plan-minimo is NOT modified.
