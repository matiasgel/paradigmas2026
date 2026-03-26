# WCAG 2.2 & 3.0 — Accesibilidad Web

**Fuente principal:** W3C (2023). *Web Content Accessibility Guidelines (WCAG) 2.2*, W3C Recommendation.
**Fuentes complementarias:**
- W3C (2024-2026). *WCAG 3.0 (Silver)*, Working Draft
- EN 301 549 v3.2.1 (2021). Estándar europeo de accesibilidad ICT
- Seale, J. (2022). *Improving Accessible Digital Practices in Higher Education* (2nd ed.), Springer
- Rello, L. (2023). *Designing for Dyslexia in Digital Environments*, Universal Access in the Information Society
**Relevancia Sprint:** S1.1

## WCAG 2.2 — Criterios Relevantes para Slides

### 1.4.3 — Contraste (Nivel AA)
- Texto normal: ratio mínimo **4.5:1**
- Texto grande (≥18pt o ≥14pt bold): ratio mínimo **3:1**
- **Fórmula de luminancia relativa:**
  ```
  L = 0.2126 * R_lin + 0.7152 * G_lin + 0.0722 * B_lin
  donde R_lin = (R/255)^2.2 (aproximación gamma)
  Ratio = (L1 + 0.05) / (L2 + 0.05) donde L1 > L2
  ```

### 1.4.6 — Contraste Mejorado (Nivel AAA)
- Texto normal: ratio mínimo **7:1**
- Texto grande: ratio mínimo **4.5:1**
- **Recomendado para proyección a distancia (>4m)**

### 1.4.11 — Contraste de Elementos No-Textuales (Nivel AA)
- Componentes UI y gráficos: ratio mínimo **3:1**
- Aplica a bordes de tablas, flechas de diagramas, iconos

### 1.1.1 — Texto Alternativo (Nivel A)
- Toda imagen no decorativa DEBE tener alt_text descriptivo
- Imágenes decorativas: alt="" (vacío explícito)
- **Implementación EDU:** Verificar campo `alt_text` en plan JSON

### 1.4.12 — Espaciado de Texto (Nivel AA)
- Line height ≥ 1.5x font size
- Paragraph spacing ≥ 2x font size
- Letter spacing ≥ 0.12x font size
- Word spacing ≥ 0.16x font size

## WCAG 3.0 (Silver) — Cambios Importantes

### Scoring Continuo (reemplaza A/AA/AAA)
- Bronze, Silver, Gold en vez de niveles binarios
- Scoring numérico por guideline
- Permite compliance parcial con score

### Nuevos Criterios Relevantes para EDU
- Contenido generado por AI: debe cumplir mismos estándares
- Presentaciones dinámicas: criterios específicos para slides
- Adaptabilidad por contexto (distancia, iluminación, dispositivo)

## Distancia de Proyección — Cálculos para Aula

### Tabla de Tamaño Mínimo por Distancia

| Distancia (m) | Font mínimo (pt) | Ratio contraste recomendado |
|----------------|-------------------|-----------------------------|
| 3 | 18 | 4.5:1 (AA) |
| 4 | 20 | 4.5:1 (AA) |
| 6 | 24 | 7:1 (AAA recomendado) |
| 8 | 28 | 7:1 (AAA obligatorio) |
| 10 | 32 | 7:1 (AAA obligatorio) |

**Fórmula:** font_pt_min = distancia_m * 3.5 + 7 (aproximación lineal para legibilidad en proyección)

### Modo Remoto (Pantalla Compartida)
- Resolución efectiva: ~720p-1080p
- Font mínimo: 18pt sans-serif
- Máximo 5 bullets por slide
- Área útil: 60% central horizontal (Duarte 2022)

## Tipografía para Dislexia (Rello 2023)
- OpenDyslexic: mejora modesta (5-8% velocidad lectora)
- **Más impactante:** espaciado interlineal amplio (18% mejora)
- **Más impactante:** contraste alto + font sans-serif estándar
- Recomendación: no usar fuentes especializadas, mejor optimizar spacing y contraste
