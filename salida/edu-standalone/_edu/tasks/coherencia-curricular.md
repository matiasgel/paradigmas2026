# Task: Coherencia curricular — escaneo de temas previos
# Ejecutado por: topic-designer-v3 (topic-cycle-v3/workflow.md Paso 0, ítem 6)
# Activación: SIEMPRE en Paso 0 (no condicionado a v3/v2 — es parte del pipeline v3)

---

## Propósito

Implementa la coherencia curricular del curso detectando solapamiento de conceptos entre el tópico actual y temas previamente impartidos. El resultado se informa al docente antes de iniciar la extracción bibliográfica, permitiendo acordar una estrategia de tratamiento para los conceptos solapados.

---

## Paso 1: Escaneo del registro de temas

```
# Obtener la lista de temas previos
topics_folder = config.yaml → topics_folder
temas_previos = []

PARA CADA carpeta en {topics_folder}/:
  SI la carpeta tiene un archivo topic-extract.md:
    SI topic-extract.md frontmatter.aprobado_en NO es null:  # solo temas aprobados
      SI carpeta != {topic_folder}:  # excluir el tema actual
        leer topic-extract.md → extraer:
          - frontmatter.tema
          - frontmatter.libro_principal
          - ## conceptos-clave (lista de terminos)
        agregar a temas_previos
```

**Nota de eficiencia:** Solo escanear temas con `topic-extract.md` aprobado. Si la carpeta existe pero no tiene `topic-extract.md` (pipeline v2 puro), ignorarla silenciosamente.

---

## Paso 2: Detección de solapamiento

Para cada concepto en el tópico actual (se obtiene del query ChromaDB que se ejecutará en Paso 1a), comparar contra los `## conceptos-clave` de cada tema previo:

**Algoritmo de comparación:**
```
solapamientos = []
PARA CADA tema_previo en temas_previos:
  PARA CADA concepto_previo en tema_previo.conceptos:
    SI concepto_previo aparece en la query del tópico actual (fuzzy match o exact):
      solapamientos.agregar({
        tema_previo: tema_previo.nombre,
        concepto: concepto_previo,
        nivel: "por determinar"
      })
```

**Clasificación de nivel de solapamiento:**
- `alto`: El concepto es central en AMBOS temas (nivel_bloom en los dos es "recordar" o "comprender")
- `medio`: El concepto aparece pero con distinto enfoque (bloom diferente entre temas)
- `bajo`: El concepto es mencionado de paso en el tema previo (relevancia marginal)

---

## Paso 3: Reporte de coherencia curricular

Si se detectaron solapamientos (cualquier nivel), presentar al docente:

```
📚 Reporte de Coherencia Curricular
=====================================

Tema actual: {tema}
Temas analizados: {N} temas previos con topic-extract.md aprobado

⚠️ Solapamientos detectados:

| Concepto | Tema previo | Nivel solapamiento |
|----------|-------------|---------------------|
| {concepto_1} | {tema_previo_1} | Alto |
| {concepto_2} | {tema_previo_2} | Medio |
| ...

📝 Para cada solapamiento, indicar estrategia:
  [A] asumir-conocido — El concepto ya fue cubierto; referenciar sin re-enseñar
  [R] resumir — Recordatorio breve (1 filmina de repaso)
  [D] desarrollar — Enseñar en profundidad igual (conceptos que requieren refuerzo)

Ingresá las estrategias para cada concepto solapado (o presioná Enter para aplicar la estrategia por defecto según nivel):
  - Alto: asumir-conocido
  - Medio: resumir
  - Bajo: asumir-conocido
```

---

## Paso 4: Captura de estrategias

Registrar las estrategias acordadas con el docente como lista de `superposiciones-detectadas` en el contexto de sesión `{superposiciones_previas}`.

Este contexto se incorpora al `topic-extract.md` en la sección `## superposiciones-detectadas` (schema ya definido).

---

## Estrategias de tratamiento (enum normalizado)

| Estrategia | Código en schema | Comportamiento en class-writer |
|-----------|-----------------|--------------------------------|
| `asumir-conocido` | "asumir-conocido" | Mencionar el concepto pero no dedicar filmina. Solo citarlo si aparece como prerequisito. |
| `resumir` | "resumir" | Incluir 1 filmina de repaso (sin profundizar). Agregar nota "[Repaso de {tema_previo}]" |
| `referenciar` | "referenciar" | Solo mencionarlo con referencia: "Ver Tema {N} para profundización" |

**Nota:** La estrategia `"desarrollar"` del reporte de usuario se mapea a NO incluir en `superposiciones-detectadas` (el concepto se trata con profundidad normal).

---

## Integración con topic-extract.md

Las superposiciones detectadas y sus estrategias se incluyen en:

```markdown
## superposiciones-detectadas

- tema_previo: "03-paradigma-imperativo"
  conceptos_solapados: "variables, asignación, estado mutable"
  nivel_solapamiento: alto
  estrategia: asumir-conocido

- tema_previo: "02-introduccion-paradigmas"
  conceptos_solapados: "abstraccion"
  nivel_solapamiento: medio
  estrategia: resumir
```

---

## Integración con Checkpoint 1 (CP1)

En CP1, el docente verifica `## superposiciones-detectadas` como parte de la revisión del `topic-extract.md`. Las estrategias pueden modificarse en CP1.

---

## Caso especial: Primer tema del curso

Si `temas_previos` está vacío (ningún tema tiene `topic-extract.md` aprobado), omitir el reporte de coherencia y continuar sin mostrar la tabla. Guardar `superposiciones_previas: []` en el contexto.

---

## Caso especial: chroma-mcp no disponible aún

El escaneo de coherencia se hace a nivel de texto local (leyendo los `topic-extract.md` ya existentes), sin usar ChromaDB. No depende de `chroma-mcp`.
