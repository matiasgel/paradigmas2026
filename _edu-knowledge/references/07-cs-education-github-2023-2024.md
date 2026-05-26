# CS Education & GitHub in Education — SIGCSE, Feliciano, Zagalsky, Denny (2023-2024)

**Fuentes:**
- Feliciano, J. et al. (2023). *Student and Instructor Experiences Using GitHub Classroom: A Systematic Literature Review*, ACM Computing Surveys, 55(13s)
- Zagalsky, A. et al. (2023). *The Evolution of GitHub in Education*, IEEE Software, 40(3)
- Denny, P. et al. (2024). *Computing Education in the Era of Generative AI*, CACM, 67(2)
- Fiksdal, J. & Riedesel, C. (2023). *Common Git Mistakes in CS Education*, SIGCSE '23
- Glassman, E.L. & Kim, J. (2023). *Scaling Personalized Feedback with LLMs*, L@S '23
- ACM/IEEE-CS/AAAI (2023). *Computer Science Curricula 2023 (CS2023)*
- Lishinski, A. et al. (2023). *Multi-Institutional CS Curricula Alignment with CS2023*, SIGCSE '24
**Relevancia Sprint:** S3.1, S3.2, S6.1

## GitHub Classroom — Pain Points (Feliciano 2023)

### Review Sistemático de 78 Estudios
1. **Pain #1 (67%):** "Too many manual steps" para crear assignments
2. **Pain #2 (54%):** "Lack of analytics integration" — grades están aislados
3. **Pain #3 (43%):** "Student onboarding friction" — alumnos no saben Git
4. **Pain #4 (31%):** "Autograding limitations" — CI/CD complejo de configurar

### Recomendaciones Implementadas en EDU
- S3.1 ataca Pain #1: un solo comando publica TP → Assignment → invite link
- S5.1 ataca Pain #2: importar grades de Classroom API → analytics unificado
- S3.2 ataca Pain #3: auto-responder para errores comunes de Git
- Existente: `classroom-designer` ya genera autograde-repo con CI

## 7 Errores Git Más Comunes de Alumnos (Fiksdal 2023)

### Estudio: n=4,500 alumnos, múltiples universidades
Estos 7 errores representan el **82%** de todas las consultas Git:

| # | Error | Frecuencia | Detección | Respuesta sugerida |
|---|-------|------------|-----------|-------------------|
| 1 | **Merge conflicts** no resueltos | 23% | Marcadores `<<<<<<<` en archivos | Tutorial paso a paso de resolución |
| 2 | **Force push** que borra trabajo | 15% | `push --force` en logs | Explicar rebase vs. force push |
| 3 | **Binarios commiteados** (.exe, .jar, .zip) | 14% | Archivos >1MB o extensiones específicas | Sugerir .gitignore template |
| 4 | **Detached HEAD** | 10% | `HEAD detached at` en status | Explicar checkout -b + merge |
| 5 | **Wrong branch** (push a main) | 9% | Push directo a main sin PR | Sugerir branch protection + workflow |
| 6 | **No .gitignore** (node_modules, .venv) | 7% | Presencia de carpetas generadas | Sugerir .gitignore por lenguaje |
| 7 | **Commit messages vacíos/genéricos** | 4% | Messages como "asdf", "update", "." | Template de conventional commits |

### Implementación en student-helper-action.yml (S3.2)
- Cada detección → PR comment automático con solución
- Mensajes en español (configurable vía git-help-students.md)
- No bloquea el push — solo informa y sugiere

## GenAI en CS Education (Denny 2024, Glassman 2023)

### LLM-Generated Feedback (Glassman 2023)
- Estudio MIT+Harvard, n=1,200
- Feedback generado por LLM + contexto del error = **tan efectivo como feedback humano** para errores comunes
- Para errores poco comunes/novedosos, humano sigue siendo superior
- **Implementación EDU:** la base de conocimiento git-help-students.md puede ser enriquecida con LLM-generated responses para errores específicos

### Computing Education Post-GenAI (Denny 2024)
- Los TPs de programación deben evolucionar:
  - De "escribí código desde cero" a "analizá/depurá/optimizá este código"
  - Debugging y tracing son más AI-resistant que producción
  - Code review como skill evaluable
- **Implementación EDU:** tp-designer (Valeria) debe priorizar ítems Bloom nivel 4+ para TPs tipo repo

## CS2023 — Curricula (ACM/IEEE/AAAI)

### Novedades vs. CC2013
- **17 knowledge areas** (vs. 14 en CC2013)
- AI/ML como knowledge area OBLIGATORIA
- Ética de AI como cross-cutting concern
- Competency model (no solo content model)

### Alineación Real (Lishinski 2023)
- Primer estudio empírico: programas reales se alinean ~62% con CS2023
- Gaps más comunes: AI/Ethics, Security, Parallelism
- **Implementación EDU (S6.1):** curriculum-comparator puede medir este % para el programa del usuario

## GitHub en Educación (Zagalsky 2023)
- >250k docentes usan GitHub en educación (2023)
- Transición de tool de industria a plataforma educativa
- GitHub Classroom CLI (GA 2024): `gh classroom assignment create|list`, `clone student-repos`, `grades export`
- GitHub Actions for Education (2024): templates oficiales CI/CD para repos educativos
