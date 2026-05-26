# Task: Niveles de densidad — propagación y modificadores
# Usado por: topic-cycle-v3/workflow.md, topic-designer-v3, class-writer (v3), study-guide-writer (v3)

---

## Propósito

Documentar la propagación del parámetro `--nivel` a través del pipeline v3 y los modificadores de densidad que cada agente downstream aplica al leer `nivel` del `.pipeline-v3-state.yaml`.

---

## Fuente del nivel (Paso 0 — ya implementado en workflow.md)

```
--nivel presente en invocación → usar ese valor (1, 2, o 3)
--nivel ausente → usar nivel 2 por defecto
Guardar en .pipeline-v3-state.yaml → nivel: {N}
```

## Tabla de niveles

| Nivel | Nombre | Bloom | Conceptos/filmina | Ejemplos | Glosario | Autoevaluación |
|-------|--------|-------|-------------------|----------|----------|----------------|
| 1 | Introductorio | Recordar/Comprender | ≤ 3 | 1 directo | Solo términos esenciales | 5 preguntas |
| 2 | Estándar | Aplicar/Analizar | ≤ 5 | 2–3 con comparación | Completo | 8 preguntas |
| 3 | Exhaustivo | Analizar/Evaluar | Sin límite | Múltiples + contra-ejs | Exhaustivo + notas al pie | 10+ preguntas |

---

## Propagación por agente

### topic-designer-v3 (genera topic-extract.md)

El nivel determina cuántos conceptos incluir en `## conceptos-clave`:
- N1: 3–5 conceptos esenciales con definición directa
- N2: 5–10 conceptos con contexto y relaciones
- N3: Todos los conceptos identificados en la bibliografía, con profundidad máxima

El nivel se guarda en `.pipeline-v3-state.yaml` y se muestra en el mensaje de bienvenida.

### class-writer (aplica modificadores v3)

Lee `nivel` de `.pipeline-v3-state.yaml` para cada generación de filminas:

**Nivel 1 — Introductorio:**
- Máximo 3 conceptos por filmina
- 1 ejemplo directo por concepto, sin variantes
- No incluir detalles de implementación, solo abstracción conceptual
- Filminas: formato simple (título + 2–3 bullets + 1 ejemplo)
- Citas: solo la referencia principal de `## fuentes`

**Nivel 2 — Estándar:**
- Máximo 5 conceptos por filmina
- 2–3 ejemplos por concepto, con comparación contextual
- Incluir variantes cuando el libro las menciona explícitamente
- Filminas: formato estándar (título + bullets + ejemplos + nota bibliográfica)
- Citas: referencias de `## fuentes` y `## ejemplos-bibliograficos`

**Nivel 3 — Exhaustivo:**
- Sin límite de conceptos si el contenido lo justifica
- Múltiples ejemplos por concepto, incluyendo contra-ejemplos y casos límite
- Sin asumir conocimiento previo — definir todo
- Filminas: formato denso (título + sub-bullets + ejemplos + contra-ejemplos + referencia)
- Citas: todas las referencias del `topic-extract.md`

### study-guide-writer (aplica modificadores v3)

Lee `nivel` de `.pipeline-v3-state.yaml` para ajustar profundidad:

**Nivel 1 — Guía concisa:**
- §3 (conceptos previos): solo prerequisitos directos
- §5 (desarrollo): conceptos esenciales únicamente
- §6 (ejemplos): 1 ejemplo trabajado paso a paso
- §8 (autoevaluación): 5 preguntas conceptuales
- §9 (glosario): solo términos usados en las filminas
- §10 (referencias): solo las fuentes con `relevancia: alta` del topic-extract.md

**Nivel 2 — Guía estándar:**
- §3: prerequisitos directos + conceptos relacionados
- §5: desarrollo completo con perspectivas múltiples
- §6: 2–3 ejemplos trabajados con variantes
- §8: 8 preguntas (conceptuales + aplicación)
- §9: glosario completo de términos del topic-extract.md
- §10: todas las fuentes del topic-extract.md

**Nivel 3 — Guía exhaustiva:**
- §3: prerequisitos completos, sin asumir nada previo
- §5: máxima profundidad con comparación de enfoques
- §6: múltiples ejemplos + contra-ejemplos + ejercicios propuestos
- §8: 10+ preguntas (conceptuales + aplicación + análisis + síntesis)
- §9: glosario extendido con notas históricas/etimológicas cuando corresponda
- §10: todas las fuentes, incluyendo tendencias con relevancia alta

---

## Representación en topic-extract.md (schema)

Los modificadores de nivel son independientes del contenido del topic-extract.md. El topic-extract.md siempre captura la máxima riqueza bibliográfica disponible. Es el agente downstream quien filtra/expande según `nivel`.

**Excepción:** `conceptos-clave` puede indicar un campo `nivel_minimo` para señalar conceptos que solo aplican en N3:
```yaml
conceptos-clave:
  - termino: "Mónada"
    definicion: "Estructura algebraica para composición sequencial..."
    fuente_directa: "SICP §4.1"
    nivel_minimo: 3  # solo incluir en nivel exhaustivo
```
