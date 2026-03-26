# Guía de Prompts de Imagen para Filminas EDU
## Template de "Lenguaje Visual Puro" para Gemini Imagen

**Propósito:** Esta guía es para el agente `slides-designer` (Vera) y para el docente al corregir prompts manualmente en el plan JSON.

---

## Regla de oro

**Gemini Imagen agrega texto cuando el prompt nombra conceptos técnicos.**

Si escribís "diagrama con fases del compilador", Gemini genera una imagen con etiquetas como "COMPILER", "PARSER", "LEXER" — transliteradas al inglés y con errores ortográficos.

**Solución:** Describir SOLO la geometría visual. Nunca nombrar lo que los elementos representan.

---

## Template canónico

```
[Elemento principal]: [forma geométrica] [color] [posición].
[Elemento secundario]: [forma geométrica] [color] [posición relativa a elemento anterior].
[Tercero si lo hay]: [ídem].
[Conectores o relaciones posicionales]: [tipo de conector] entre ellos.
[Estilo]: flat design, [paleta: bordo #8B0000 y gris #1A1A1A], fondo blanco.
Sin texto, sin letras, sin etiquetas, sin código, sin números.
Alta resolución.
```

---

## Vocabulario visual permitido

### Formas geométricas
- rectangle, square, circle, triangle, hexagon, diamond
- cylinder, cube, star, oval, blob (forma orgánica)
- branching tree (árbol bifurcado)

### Conectores
- thin arrow, bold arrow, curved line, dashed line, downward arrow
- horizontal sequence, vertical column, radiate outward

### Posiciones
- top-left, center, bottom-right, arranged in a row/column
- stacked vertically, side by side, surrounding a central element

### Íconos abstractos seguros (sin texto)
- checkmark (tilde), gear (engranaje), magnifying glass, document icon (folded corner)
- human silhouette, monitor icon, book icon, microchip icon

---

## Ejemplos probados ✅

### Para slides de proceso/pipeline
```
Two vertical parallel columns. Each column has four plain gray and bordo rectangles 
connected by downward arrows. Left column ends at a document icon with a folded top 
corner. Right column ends at a microchip icon. White background. Flat minimal design.
No text, no code symbols. Alta resolución. Sin texto, sin letras.
```

### Para slides de comparación (dos opciones)
```
Justice scales flat icon. Left bowl contains orderly stacked horizontal rectangles.
Right bowl contains randomly scattered small squares. Bordo and dark gray tones.
White background. Zero text. Alta resolución. Sin texto, sin letras.
```

### Para slides de mapa conceptual (nodo central + ramas)
```
One large bordo filled circle in the center. Six thin straight lines radiate outward.
At the end of each line, one small flat icon: magnifying glass, gear, downward branching 
tree, two-by-two grid, cube, horizontal tube. White background.
No labels, no words, nothing written anywhere. Alta resolución. Sin texto, sin letras.
```

### Para slides de tres etapas en secuencia
```
Three flat icons in a horizontal sequence on white background separated by thin arrows.
First: irregular blob shape. Second: symmetrical triangular branching tree.
Third: bold checkmark symbol. Flat design, bordo and dark gray palette. Nothing written.
Alta resolución. Sin texto, sin letras.
```

### Para slides conceptuales abstractas (dos capas)
```
Two flat squares stacked vertically. Top square dark red. Bottom square light gray.
Three thin curved lines connecting them in the center. White background.
Pure geometric abstract composition. Alta resolución. Sin texto, sin letras.
```

---

## Ejemplos que FALLAN ❌

| Prompt problemático | Resultado | Por qué falla |
|---|---|---|
| "diagrama de capas: compilador, ejecución" | Genera etiquetas "Compiler Layer", "Execution Base" | Nombra conceptos técnicos |
| "infografía ambigüedad → gramática formal → validación" | "AMBINICITY", "FORMACL GRAMMAR" | Palabra "infografía" + conceptos nombrados |
| "mapa conceptual: lexer, parser, gramática, pipeline" | "Parser", "Lexicon", "Grammaris" | Lista de conceptos técnicos |
| "balanza: programa correcto vs programa erróneo" | Texto en los platos | Nombra lo que representan los elementos |

---

## Proceso de corrección cuando hay texto en una imagen

1. Identificar el slide problemático en los thumbnails capturados
2. Abrir `slides/plan-filminas-{tema}.json`  
3. Localizar el slide por `id`
4. Reescribir `image.prompt` siguiendo este template
5. Poner `image.drive_id: null` para forzar regeneración
6. Eliminar `slides/assets/F-XX-*.png` si existe localmente
7. Ejecutar: `python scripts/slides_pipeline.py <tema> --assets-only`
8. Ejecutar: `python scripts/slides_pipeline.py <tema> --publish-only`
9. Ejecutar: `python scripts/capture_thumbnails.py <nuevo_id> <carpeta>`
10. Verificar visualmente

---

*Documentado el 19 de marzo de 2026 — Lección aprendida del Tema 02, Bug 3.*
