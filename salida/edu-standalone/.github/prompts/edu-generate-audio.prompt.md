---
description: 'EDU: Generar audio TTS por filmina para clases asíncronas'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. If `tts_enabled` is false, inform the user how to enable it and exit.
3. Run: `cd {project-root} && python scripts/generate_tts.py --topic {topic_id} --course {course_id}`
4. If the configured provider is a paid service (gcloud-tts, elevenlabs), the script will ask for confirmation before proceeding.
5. Display the audio manifest summary: number of files generated, total duration, provider used.
6. The audio files are in `{topic_folder}/audio/filmina-{N}.mp3`.
