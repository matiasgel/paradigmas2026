
description: 'EDU: Estado del tema — muestra estado de producción de un tema específico'
agent: 'agent'
tools: ['read', 'search']
---

1. Load {project-root}/_edu/config.yaml and store ALL fields as session variables
2. Ask the user which topic number to check (or detect automatically by scanning temas/ folder).
3. Read all artifacts for that topic (diseno.md, minuta.md, filminas.md, tp.md, quality reports, slides-url.txt).
4. Report the production status: design, class, TP, quality loops, testing, slides.
5. Recommend the next step based on what is missing.


