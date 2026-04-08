---
description: 'EDU: Inferir prerequisitos entre conceptos usando ML (active learning)'
tools: ['read', 'write', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Ensure the Knowledge Graph exists (run `/edu-build-kg` first if not).
3. If no CPL model exists, inform the teacher about training options:
   - Run `python scripts/train_prerequisite_model.py --dataset lecturebank` for seed training.
   - For custom data: `python scripts/train_prerequisite_model.py --dataset custom --csv annotations.csv`.
4. Run `python scripts/prerequisite_learner.py --course {course_id} predict` to generate suggestions.
5. For active learning: `python scripts/prerequisite_learner.py --course {course_id} annotate`.
6. Review the suggestions with the teacher before adding to the KG.
