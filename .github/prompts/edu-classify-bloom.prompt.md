---
description: 'EDU: Clasificar preguntas de TP/examen por nivel de Bloom con ML'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Run: `cd {project-root} && python scripts/bloom_classifier.py --course {course_id} --exam {exam_name}`
   - Alternative: `--file preguntas.txt` for a plain text file with one question per line.
3. Display the classification table with Bloom level, confidence, and method (ML vs keyword-fallback).
4. Show the distribution chart across Bloom levels.
5. If the model is not fine-tuned, suggest running `python scripts/train_bloom_model.py`.
