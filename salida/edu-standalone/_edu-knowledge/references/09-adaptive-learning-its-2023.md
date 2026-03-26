# Adaptive Learning & ITS — VanLehn, ALEKS, Du, Mollick (2023)

**Fuentes:**
- Aleven, V. et al. (2023). *Intelligent Tutoring Systems: Then and Now*, International Handbook of the Learning Sciences (3rd ed.), Routledge
- VanLehn, K. (2023). *Can AI Tutors Match Human Tutors? An Updated Analysis*, Educational Psychology Review
- ALEKS/McGraw-Hill (2023). Estudio longitudinal 180k alumnos
- Du, X. et al. (2023). *Leveraging LLMs for Automated Adaptive Learning*, AIED '23
- Mollick, E. & Mollick, L. (2023). *Using AI to Implement Effective Teaching Strategies*, SSRN
- Bloom, B.S. (1984). *The 2 Sigma Problem* (clásico vigente)
**Relevancia Sprint:** S5.2

## The 2 Sigma Problem (Bloom 1984, post-LLM)
- Tutoring 1:1 produce **2 sigma** de mejora vs. instrucción grupal
- Pregunta original: ¿cómo escalar tutoring 1:1?
- **Pregunta post-LLM:** ¿puede GenAI cerrar el gap de 2 sigma?

### Respuesta Parcial (Mollick 2023)
- Sí, cuando LLM se usa como **tutor socrático** (hace preguntas, no da respuestas)
- No, cuando LLM se usa como **generador de respuestas** (el alumno no piensa)
- **Implementación EDU:** el student-simulator ya usa modo socrático. Las rutas adaptativas deben incluir prompts de reflexión, no solo contenido resumido

## ITS Meta-Análisis Actualizado (Aleven 2023)
- Effect size de Intelligent Tutoring Systems: **d=0.66**
- Comparable a tutoring humano grupal (d=0.70)
- Los ITS más efectivos combinan:
  1. Knowledge tracing (saber qué sabe el alumno)
  2. Feedback explicativo (no solo correcto/incorrecto)
  3. Adaptación de dificultad (zona de desarrollo próximo)

## AI Tutoring con LLMs (VanLehn 2023)
- Con LLMs GPT-4 class: d=0.70 en estudios controlados
- Arizona State University + Carnegie Learning, n=12,000
- El gap con tutoring humano 1:1 se acorta
- **Limitación:** sin knowledge model persistente del alumno
- **Implementación EDU:** memory.db + analytics = knowledge model persistente local

## ALEKS (McGraw-Hill 2023)
- Reemplaza a Knewton (adquirida por Wiley 2019, discontinuada)
- Estudio longitudinal: **180k alumnos STEM**
- Mejora completion rates: **14-22%**
- Basado en Knowledge Space Theory (Falmagne & Doignon)
- Modelo de prerequisitos: cada concepto tiene dependencias explícitas

### Lecciones para EDU
- Prerequisite tree explícito por tema es viable y efectivo
- No necesita ML complejo — un grafo dirigido de dependencias funciona
- El quiz diagnóstico pre-tema es la pieza clave

## LLMs para Adaptive Learning (Du 2023)
- Primer estudio que usa LLMs para generar learning paths adaptativos en tiempo real
- El LLM recibe:
  - Perfil del alumno (fuerte/débil en qué)
  - Contenido disponible (filminas, guías, ejercicios)
  - Resultados diagnósticos
- Output: secuencia personalizada de materiales

### Implementación para EDU (S5.2)
```
IF score_diagnostico >= 80%:
    ruta = "avanzada"  → skip intro, ejercicios nivel 4-5 Bloom
ELIF score_diagnostico >= 50%:
    ruta = "estandar"  → ruta completa
ELSE:
    ruta = "refuerzo"  → material de temas prerequisito + ruta extendida
```

## Prerequisite Trees para CS
- Estructura: grafo dirigido acíclico (DAG)
- Ejemplo:
  ```
  variables → tipos → punteros → memoria_virtual
  funciones → recursión → backtracking
  tipos → structs → OOP
  ```
- Se define en `diseno.md` de cada tema:
  ```yaml
  prerequisites:
    - topic: "02-tipos"
      concepts: ["variables", "tipado estático"]
    - topic: "01-intro"
      concepts: ["compilación", "enlazado"]
  ```
- adaptive_path.py lee el DAG y verifica dominio de prerequisites
