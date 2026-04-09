# Slide Composition & Visual Design — Duarte, Scheiter, Pernice (2019-2023)

**Fuentes:**
- Duarte, N. (2019). *DataStory* + (2022). *Illuminate*. Actualizan slide:ology (2008)
- Scheiter, K. & Eitel, A. (2023). *Visual Design of Multimedia Learning Materials*, Educational Psychology Review
- Pernice, K. & Nielsen, J. (2023). *How People Read on Screens: New Research*, Nielsen Norman Group
**Relevancia Sprint:** S1.2, S4.1

## Densidad Visual Óptima (Scheiter & Eitel 2023)

### Meta-análisis Post-COVID
- **Ideal: 35-55% de área ocupada** (ajustado a la baja desde 40-60% de Duarte 2008)
- Razón: fatiga de pantalla post-COVID → más whitespace necesario
- Aplica a proyección presencial y pantalla compartida

### Escala de Densidad para EDU

| Densidad | Score | Descripción |
|----------|-------|-------------|
| <25% | C | Demasiado vacía — no aprovecha el espacio |
| 25-35% | B | Aceptable, ligeramente subutilizada |
| 35-55% | A | Óptima |
| 55-70% | B | Aceptable, ligeramente densa |
| >70% | F | Sobrecargada — reducir contenido |

## Patrones de Atención (Pernice & Nielsen 2023)

### Patrón Z — Proyección de Aula
- Ojos van: arriba-izquierda → arriba-derecha → centro → abajo-izquierda → abajo-derecha
- **Zona de máxima atención:** cuadrante superior-izquierdo (35% de fijaciones)
- **Zona de atención muerta:** cuadrante inferior-derecho (10% de fijaciones)
- **Implementación EDU:** título y concepto clave en arriba-izquierda, detalle/fuente en abajo-derecha

### Patrón Layer-Cake — Pantallas Móviles (NUEVO)
- En mobile (>50% del consumo educativo post-COVID): dominan headers horizontales
- Los alumnos escanean headers y deciden si leer el contenido debajo
- **Implementación EDU:** para guías de estudio (mobile-friendly), no para filminas

### Patrón F — Pantalla de Computadora
- Primer barrido horizontal arriba
- Segundo barrido horizontal al medio
- Barrido vertical izquierdo
- **Implementación EDU:** relevante para slides compartidas por pantalla (modo remoto)

## Regla de Tercios (Duarte, vigente)
- Dividir la slide en 9 zonas (3×3)
- Intersecciones de las líneas = puntos de mayor impacto visual
- Elementos clave (título, imagen principal) en intersecciones

## Áreas de Atención por Modo de Entrega (Duarte 2022)

| Modo | Área de atención activa | Recomendación |
|------|------------------------|---------------|
| Presencial (proyección) | 75% central | Márgenes 12.5% cada lado |
| Remoto (pantalla compartida) | 60% central horizontal | Márgenes 20% cada lado |
| Mobile | 90% horizontal, 40% vertical superior | Contenido en mitad superior |

## Márgenes Seguros para EDU

### Safe Margin = 5% del borde
- Ningún elemento textual a menos del 5% de cualquier borde
- Evita corte en:
  - Proyección (overscan de proyectores: 3-5%)
  - PDF (márgenes de impresión)
  - Pantalla compartida (barras de herramientas de Zoom/Meet)

### Cálculo en EMU (English Metric Units)
```
Slide estándar: 9144000 × 5143500 EMU (10" × 5.625")
Margen 5%:
  x_min = 457200 EMU (0.5")
  x_max = 8686800 EMU (9.5")
  y_min = 257175 EMU (0.28")
  y_max = 4886325 EMU (5.34")
```

## Superposición de Elementos
- Detectar colisiones de bounding boxes
- Cada elemento tiene: (x, y, width, height) en EMU
- Colisión si: NOT (A.right < B.left OR A.left > B.right OR A.bottom < B.top OR A.top > B.bottom)
- **Implementación EDU:** iterate par a par sobre elementos del plan JSON, reportar solapamientos

## Assertion-Evidence Design (Alley 2005→2023)
- **Título:** oración declarativa completa ("La memoria virtual mapea direcciones lógicas a físicas"), NO frase nominal ("Memoria Virtual")
- **Body:** evidencia visual (diagrama, gráfico, imagen) que soporta la afirmación del título
- **Effect size:** d=0.72 comprensión, d=0.84 retención a 2 semanas
- Validado en >30 universidades, incluyendo contextos remotos/híbridos (2023 update)
- **Implementación EDU:** validar que `title` contenga verbo conjugado (assertion), no solo sustantivo (frase nominal)
