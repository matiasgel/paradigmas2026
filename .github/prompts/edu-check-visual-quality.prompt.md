---
description: 'EDU: Evaluar calidad visual de slides con CLIP y análisis de layout'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Run: `cd {project-root} && python scripts/slide_quality_vision.py --topic {topic_id} --course {course_id}`
3. Display the visual quality report:
   - CLIP scores: image-text relevance per slide (✅ >0.25, ⚠️ 0.15-0.25, ❌ <0.15)
   - Layout grades: whitespace ratio, horizontal balance (A/B/C/F per slide)
4. If OpenCLIP is not installed, inform the user: `pip install open-clip-torch`
5. If thumbnails are missing, suggest running `capture_thumbnails.py` first.
