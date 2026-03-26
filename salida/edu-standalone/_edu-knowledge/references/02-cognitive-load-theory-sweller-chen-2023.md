# Cognitive Load Theory — Sweller, Chen et al. (2011→2023)

**Fuente principal:** Chen, O., Castro-Alonso, J.C., Paas, F. & Sweller, J. (2023). *Extending Cognitive Load Theory to Incorporate Working Memory Resource Depletion*, Educational Psychology Review, 35, 7.
**Fuentes complementarias:**
- Sweller, J., Ayres, P. & Kalyuga, S. (2011→2019). *Cognitive Load Theory*, Springer
- Skulmowski, A. & Xu, K.M. (2022). *Understanding Cognitive Load in Digital and Online Learning*, Educational Psychology Review, 34, pp.1-28
**Tipo:** Teoría + Meta-análisis
**Relevancia Sprint:** S4.1, S4.2, S1.2

## Marco Teórico — Tres Tipos de Carga

### 1. Carga Intrínseca
- Determinada por la complejidad inherente del tema y la interactividad entre elementos
- Un concepto con 5 elementos que interactúan = más carga que 5 elementos independientes
- **No reducible por diseño** — depende del tema y del conocimiento previo del alumno
- **Implementación EDU:** Estimar interactividad de elementos por slide: conceptos que requieren relación = alta interactividad

### 2. Carga Extrínseca
- Causada por MAL diseño del material
- Incluye: navegación confusa, elementos decorativos, información redundante, layout caótico
- **REDUCIBLE por diseño** — objetivo principal de los validadores EDU
- **Implementación EDU:** Los validadores de accesibilidad, composición y layout cognitivo atacan directamente la carga extrínseca

### 3. Carga Germane
- Esfuerzo cognitivo dedicado a CONSTRUIR esquemas mentales
- Es el aprendizaje útil — no debe reducirse, debe maximizarse
- **Implementación EDU:** Slides socráticas y actividades generativas promueven carga germane

## Hallazgo 2023 — Depleción de Working Memory (NUEVO)
- **Working memory NO es un recurso estático** — se depleta con el uso sostenido
- Después de 20-30 min de procesamiento intensivo, la capacidad baja
- La depleción es acumulativa dentro de una sesión
- **Implicación para EDU:** No basta con que cada slide individualmente sea correcta. La SECUENCIA importa:
  - Bloques de alta carga deben alternarse con bloques de baja carga
  - "Attention resets" (slides socráticas, demos, pausas activas) permiten recuperación
  - **Regla S4.2:** máximo 3 slides teóricas consecutivas sin un attention reset

## Reglas Cuantitativas para EDU

| Métrica | Valor | Fuente |
|---------|-------|--------|
| Capacidad WM | 7±2 chunks (Miller, 1956, aún vigente) | Miller |
| Conceptos nuevos por 30 min | Máximo 6 | Chen & Sweller 2023 |
| Slides teóricas consecutivas | Máximo 3 sin attention reset | Inferido de depleción WM |
| Interactividad alta | Máximo 3 elementos interrelacionados por slide | Element interactivity theory |
| Curva de complejidad óptima | U invertida: medio → alto → medio → bajo (cierre) | Skulmowski 2022 |

## Atención y Mind-Wandering

### Bradbury (2016→2023) — Desmitificando los "10 minutos"
- El mito de que la atención dura 10-15 minutos NO tiene base empírica sólida
- Lo que importa es la VARIABILIDAD de actividad (cambio de formato cada 8-12 min)
- **Implementación EDU:** cognitive_budget.py debe medir variabilidad de formato, no solo duración

### Szpunar, Moulton & Schacter (2013)
- Interrupciones activas (preguntas, actividades) reducen mind-wandering un 40%
- Testing effect: preguntarse sobre el material durante la clase mejora retención
- **Implementación EDU:** Insertar slides socráticas cada 3-4 slides teóricas

## Citas Complementarias
- Kosslyn, S.M. (2007). *Clear and to the Point*. 8 principios cognitivos base — aún citados como fundamento
