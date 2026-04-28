# Multimedia Learning — Fiorella & Mayer (2023)

**Fuente:** Fiorella, L. & Mayer, R.E. (2023). *The Cambridge Handbook of Multimedia Learning* (3rd ed.), Cambridge University Press.
**Tipo:** Meta-análisis de >700 estudios
**Relevancia Sprint:** S1.1, S1.2, S4.1, S4.2

## Principios Verificados con Effect Sizes

### 1. Principio de Contigüidad Espacial (d=1.10)
- Texto e imagen relacionados DEBEN estar próximos en la misma slide
- Replicado en 80+ estudios, robusto en presencial, remoto e híbrido
- **Implementación EDU:** Validar que elementos `body` e `image` estén en el mismo "half" de la slide (contigüidad horizontal), no separados por >50% del ancho

### 2. Principio de Señalización (d=0.41)
- Flechas, resaltado, color y encuadres mejoran retención
- Robusto en presencial y online
- **Implementación EDU:** Verificar que slides con `image_file` tengan al menos un elemento de señalización (título destacado, flecha, color distintivo)

### 3. Principio de Coherencia (d=0.86)
- Eliminar elementos decorativos irrelevantes mejora aprendizaje significativamente
- Incluye: clipart decorativo, música de fondo, animaciones innecesarias, texto ornamental
- **Implementación EDU:** Flag `forbidden: ["decorative_clipart", "full_paragraph"]` en layout-rules.schema.json

### 4. Principio de Redundancia (d=0.72 negativo)
- NO duplicar texto oral como texto en pantalla
- Efecto negativo: el alumno lee el texto en vez de escuchar la explicación
- **Implementación EDU:** Limitar palabras por body (max 30 para concepto-abstracto). El body complementa al speech del profesor, no lo replica

### 5. Principio de Generatividad (d=0.56) — NUEVO en 3ra edición
- Pedir al alumno que complete, genere o prediga contenido mejora aprendizaje profundo
- Self-explanation prompts, fill-in-the-blank, predict-the-outcome
- **Implementación EDU:** Tipo de slide `socratica` debe incluir prompt de generación, no solo pregunta de elección

### 6. Principio de Segmentación (d=0.79)
- Material complejo presentado en segmentos manejables > presentación continua
- Permitir pausa entre segmentos en video/slides
- **Implementación EDU:** Máximo 3 slides teóricas consecutivas sin "attention reset"

### 7. Principio de Pre-entrenamiento (d=0.46)
- Enseñar terminología y conceptos clave ANTES de la explicación principal
- **Implementación EDU:** Slide tipo `glosario` o bloque introductorio con definiciones

### 8. Principio de Modalidad (d=0.72)
- Gráficos + narración oral > gráficos + texto en pantalla
- En contexto de slides: la imagen domina, el texto es mínimo, el profesor habla
- **Implementación EDU:** Ratio imagen/texto alto en slides de concepto-abstracto y diagrama

## Extensiones 2023 vs. Ediciones Anteriores
- Validación en contextos remotos/híbridos (Zoom, Teams, Meet)
- Eficacia en pantallas pequeñas (mobile-first education post-COVID)
- Interacción con GenAI: los principios aplican igual cuando el contenido es generado por AI

## Citas Complementarias
- Mayer, R.E., Fiorella, L. & Stull, A. (2020). *Five Ways to Increase the Effectiveness of Instructional Video*, ETR&D, 68, pp. 837-852
- Alley, M. & Neeley, K.A. (2005→2023). Assertion-Evidence framework: título-oración + visual > bullet-point. d=0.72 comprensión, d=0.84 retención a 2 semanas
- Kasneci, E. et al. (2023). *ChatGPT for Good?*, Learning and Individual Differences. Marco GenAI + diseño instruccional
