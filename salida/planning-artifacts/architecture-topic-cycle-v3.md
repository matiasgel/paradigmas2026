---
stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8]
workflowType: architecture
status: complete
completedAt: '2026-05-23'
project_name: paradigmas2026
inputDocuments:
  - salida/planning-artifacts/prd.md
  - salida/planning-artifacts/product-brief-edu-pipeline-v3.md
  - _edu/workflows/topic-cycle/workflow.md
  - _edu/agents/class-writer.md
  - salida/edu-standalone/_edu/config.yaml
---

# Arquitectura — topic-cycle-v3

**Proyecto:** paradigmas2026  
**Arquitecto:** Winston (BMAD Architect) — fast mode  
**Fecha:** 2026-05-23  
**Estado:** COMPLETO  
**PRD base:** `salida/planning-artifacts/prd.md`

---

## 0. Resumen Ejecutivo

`topic-cycle-v3` es un nuevo workflow de producción de temas que opera en paralelo y sin interferencia con `topic-cycle` (v2). Implementa un pipeline atómico de siete operaciones discretas con dos checkpoints explícitos de aprobación docente, grounding bibliográfico obligatorio vía ChromaDB, y densidad de contenido como parámetro de primera clase.

La innovación arquitectural central es el **artefacto intermedio `topic-extract.md`**: un contrato de conocimiento persisitido en disco que desacopla la extracción bibliográfica de la generación de material. Los agentes downstream consumen este contrato directamente desde el sistema de archivos, eliminando el re-procesamiento de ChromaDB y garantizando coherencia terminológica entre todos los artefactos del tema.

**Tipo de sistema:** AI Agent Pipeline — orquestación de agentes LLM con artefactos intermedios persisitidos  
**Contexto:** Brownfield — coexistencia obligatoria con 24 agentes y 16+ workflows en producción activa  
**Principio rector:** Aditivo/opt-in — zero modificaciones a componentes existentes

---

## 1. Análisis de Contexto

### 1.1 Sistema Existente (v2)

El sistema actual (`topic-cycle`) opera con el siguiente pipeline:

```
active-topic.yaml → topic-designer (Marcos) → diseno.md
diseno.md → class-writer (Roberto) → filminas.md + minuta.md
filminas.md + minuta.md → study-guide-writer (Sofía) → guia-estudio.md
guia-estudio.md → class-writer (Roberto) → guiaprofesor.md
```

**Problema estructural v2:** Cada agente trabaja con la información que tiene en contexto + PDFs locales del tema. No hay grounding sistemático contra el corpus bibliográfico en ChromaDB, ni coherencia curricular activa, ni niveles de densidad parametrizables.

### 1.2 Fallos Estructurales que Resuelve v3

| Fallo | Síntoma | Solución v3 |
|---|---|---|
| Sin checkpoints intermedios | Timeouts fuerzan reinicio desde cero | Estado persisitido; reanudación por paso |
| Generación sin bibliografía | Terminología inconsistente con lecturas | ChromaDB como Paso 1a/1b obligatorio |
| Profundidad uniforme | Material no se adapta al momento de la cursada | Parámetro `--nivel` 1/2/3 |
| Sin coherencia curricular | Conceptos repetidos o asumidos sin base | Paso 0 con consulta al registro de cursada |
| No reutilización de material previo | Trabajo histórico descartado | `--base filminas-año-anterior.md` opcional |

### 1.3 Alcance del Cambio

**Artefactos NUEVOS (no modifican nada existente):**
- Workflow `_edu/workflows/topic-cycle-v3/workflow.md`
- Agente `_edu/agents/topic-designer-v3.md` (variante de topic-designer)
- Esquema `_edu/schemas/topic-extract-schema.yaml`
- Artefacto `{topic_folder}/topic-extract.md` (nuevo por tema)
- Estado de pipeline `{topic_folder}/.pipeline-v3-state.yaml`

**Agentes MODIFICADOS (retrocompatibles):**
- `_edu/agents/class-writer.md` — nueva sección condicional para consumir `topic-extract.md` cuando esté presente
- `_edu/agents/study-guide-writer.md` — idem
- `_edu/agents/create-teacher-guide.md` — idem (actualmente es un workflow; se externaliza como agente)

**Artefactos INVARIANTES:**
- `_edu/workflows/topic-cycle/workflow.md` — sin cambios
- `scripts/slides_pipeline.py` — sin cambios
- Schema de filminas (`_edu/schemas/schema-registry.json`) — sin cambios
- Todos los demás agentes — sin cambios

---

## 2. Stack Tecnológico

Este sistema no involucra código nuevo de aplicación. El stack es la plataforma de agentes LLM existente:

| Componente | Tecnología | Versión/Config |
|---|---|---|
| Runtime de agentes | VS Code + GitHub Copilot Chat | Configurado en `.vscode/` |
| Knowledge base | ChromaDB (persistent) | `chroma-mcp` vía `.vscode/mcp.json` |
| Colección activa | `edu_knowledge` | cosine similarity |
| Tipos de documentos | `material` (libros), `tool`, `reference` | filtro `where: {"type": "material"}` |
| Formato de artefactos | Markdown | UTF-8, sin encoding especial |
| Persistencia de estado | YAML (archivos en disco) | Compatible con `active-topic.yaml` existente |
| Pipeline de publicación | `slides_pipeline.py` | Python — sin cambios |

**Dependencias nuevas:** ninguna. `chroma-mcp` ya está configurado en producción.

---

## 3. Decisiones Arquitecturales

### AD-01: Pipeline State Machine con persistencia por paso

**Decisión:** El estado del pipeline se persiste en `{topic_folder}/.pipeline-v3-state.yaml` al completar cada paso. Si la sesión es interrumpida, el workflow lee este archivo al inicio y reanuda desde el último paso completado.

**Estructura del estado:**
```yaml
# .pipeline-v3-state.yaml
topic: "Programación Funcional"
libro_principal: "SICP"
nivel: 2
base_filminas_previas: null  # o path relativo
pasos_completados: ["paso-0", "paso-1a", "paso-1b", "paso-1c"]
checkpoint_1_aprobado: false
checkpoint_2_aprobado: false
iniciado_en: "2026-05-23T14:30:00"
ultimo_paso_en: "2026-05-23T14:45:00"
```

**Alternativa rechazada:** Guardar estado en memoria de sesión del agente — se pierde ante cualquier reinicio.  
**Rationale:** El requisito NFR01 exige reanudación sin reprocesar pasos anteriores. Persistencia en disco es la única opción confiable.

---

### AD-02: topic-extract.md como contrato de interfaz entre agentes

**Decisión:** `topic-extract.md` es el único artefacto de handoff entre `topic-designer-v3` y los agentes downstream. Los agentes `class-writer`, `study-guide-writer` y `create-teacher-guide` lo leen desde disco como input primario cuando existe. No re-invocan ChromaDB.

**Rationale:**
- Desacopla extracción de generación — si la generación falla, la extracción no se repite
- Permite edición humana entre pasos (checkpoint 1)
- Garantiza que todos los agentes downstream usan exactamente el mismo corpus de conocimiento
- Habilita versionado y comparación entre años

**Regla de activación:** Los agentes downstream usan `topic-extract.md` si existe en `{topic_folder}/`. Si no existe (invocación vía `topic-cycle` original), usan el comportamiento v2 sin cambios.

---

### AD-03: ChromaDB como paso no-salteable (fail-fast)

**Decisión:** Si `chroma-mcp` no responde al inicio del Paso 1a, el pipeline detiene la ejecución con error explícito. No degrada silenciosamente a generación sin grounding.

**Mensaje de error estándar:**
```
ERROR [paso-1a]: chroma-mcp no disponible.
Diagnóstico: verificar que el MCP server está activo en .vscode/mcp.json
Comando de diagnóstico: [instrucción específica]
El pipeline NO continúa sin grounding bibliográfico verificado.
```

**Rationale:** NFR02. Un sistema que genera sin grounding pero parece haberlo hecho es más peligroso que uno que falla explícitamente. El docente debe saber cuando el material no está anclado.

---

### AD-04: Niveles de densidad como modificador del prompt de generación

**Decisión:** El nivel de densidad (1, 2, 3) se propaga como variable de sesión y modifica los prompts de generación en los Pasos 3, 4 y 5. No hay post-procesamiento de expansión/compresión.

**Mapa taxonómico:**
| Nivel | Nombre | Bloom | Duración implícita | Descripción operacional |
|---|---|---|---|---|
| 1 | Introductorio | Recordar / Comprender | Primera exposición | Conceptos clave y ejemplo directo; sin detalles de implementación |
| 2 | Estándar | Aplicar / Analizar | Desarrollo completo | Contexto completo, múltiples perspectivas, comparaciones |
| 3 | Exhaustivo | Analizar / Evaluar | Repaso autónomo | Sin asumir conocimiento previo; contra-ejemplos, variantes, casos límite |

**Parámetro de invocación:** `--nivel N` en la invocación del workflow (o `nivel` en el estado del pipeline).

---

### AD-05: Política de coexistencia de artefactos

**Decisión:** Los artefactos de v3 usan el mismo directorio `{topic_folder}/` pero con nombres que no colisionan con v2.

| Artefacto v2 | Artefacto v3 | Colisión |
|---|---|---|
| `filminas.md` | `filminas.md` | ⚠️ Mismo nombre — v3 sobrescribe si el docente aprueba |
| `minuta.md` | `minuta.md` | ⚠️ Mismo nombre — mismo comportamiento |
| `guia-estudio.md` | `guia-estudio.md` | ⚠️ Mismo nombre |
| `guiaprofesor.md` | `guiaprofesor.md` | ⚠️ Mismo nombre |
| `diseno.md` | NO existe en v3 | ✅ Sin colisión |
| *(no existe)* | `topic-extract.md` | ✅ Nuevo |
| *(no existe)* | `.pipeline-v3-state.yaml` | ✅ Nuevo |

**Regla de seguridad:** v3 solo sobrescribe `filminas.md`, `minuta.md` etc. después del checkpoint 2 aprobado explícitamente. Antes de sobrescribir, el agente ofrece hacer backup renombrando a `filminas-v2-backup.md`.

---

### AD-06: topic-designer-v3 como variante del topic-designer existente

**Decisión:** En lugar de modificar el agente `topic-designer` existente, se crea `topic-designer-v3.md` como agente independiente. Comparte la persona de Marcos pero tiene menú y comportamiento extendido.

**Rationale:** Evita riesgo de regresión en el agente v2 que está siendo usado activamente. Los dos agentes coexisten. Cuando v3 sea el estándar, se puede deprecar v2 en una iteración futura.

---

### AD-07: Renovación de material previo como análisis comparativo

**Decisión:** Cuando se provee `--base filminas-anteriores.md`, el workflow ejecuta un análisis comparativo entre el `topic-extract.md` nuevo (ya aprobado en checkpoint 1) y el material previo. El resultado es un reporte de renovación que el docente aprueba antes de la generación.

**Categorías del análisis:**
- `conservar`: filmina válida sin cambios (contenido alineado con topic-extract.md actual)
- `actualizar`: filmina con terminología o contexto desactualizado
- `eliminar`: filmina con superposición curricular detectada en Paso 0
- `nueva`: filmina requerida por topic-extract.md que no existe en el material previo

---

## 4. Esquema de topic-extract.md

Este es el contrato de interfaz central del sistema. Todo agente downstream lo parsea con este esquema.

```markdown
---
tema: "Programación Funcional"
libro_principal: "SICP"
nivel: 2
generado_en: "2026-05-23T15:00:00"
aprobado_en: "2026-05-23T15:05:00"  # null hasta checkpoint 1
version: "1"
---

# topic-extract — [Nombre del Tema]

## fuentes
Lista de referencias bibliográficas extraídas de ChromaDB.
Formato obligatorio por ítem:
- libro: "[Título]"
  autor: "[Autor(es)]"
  seccion: "[Capítulo/Sección]"
  pagina: "[N o rango N-M]"   # null si no disponible → marcar "referencia incompleta"
  relevancia: "[alta|media]"
  fragmento: "[Cita textual breve o paráfrasis]"

## conceptos-clave
Lista de conceptos centrales del tema.
Formato obligatorio por ítem:
- concepto: "[Nombre]"
  definicion: "[1-2 oraciones]"
  fuente_seccion: "[libro §sección]"  # referencia a fuentes arriba
  nivel_bloom: "[recordar|comprender|aplicar|analizar|evaluar]"

## ejemplos-bibliograficos
Ejemplos concretos extraídos directamente de los libros fuente.
Formato obligatorio por ítem:
- titulo: "[Nombre descriptivo del ejemplo]"
  descripcion: "[Qué ilustra]"
  codigo_o_texto: |
    [Contenido del ejemplo — código, pseudocódigo o párrafo]
  fuente_libro: "[libro]"
  fuente_pagina: "[página]"

## tendencias
Investigación académica reciente (Paso 1c — web research).
Formato obligatorio por ítem:
- tendencia: "[Descripción]"
  relevancia: "[alta|media|baja]"
  conflicto_con_bibliografía: "[sí|no]"
  nota: "[Si conflicto=sí: qué sección del libro podría estar desactualizada]"
  fuente_url: "[URL si disponible]"

## superposiciones-detectadas
Temas previos de la cursada con solapamiento de conceptos.
Formato obligatorio por ítem:
- tema_previo: "[NN-nombre-tema]"
  conceptos_solapados: "[Lista de conceptos]"
  nivel_solapamiento: "[alto|medio|bajo]"
  estrategia: "[asumir-conocido|resumir|referenciar]"  # definida en checkpoint 0
```

**Reglas de validación del esquema:**
- `fuentes` debe tener al menos 1 ítem con `pagina` no nulo (NFR05)
- Ítems con `pagina: null` se marcan automáticamente con `⚠️ referencia incompleta` (NFR04)
- `conceptos-clave` debe tener al menos 3 ítems
- `superposiciones-detectadas` puede estar vacío (si no hay solapamientos)

---

## 5. Pipeline — Máquina de Estados

### Diagrama de flujo

```
INICIO (invocación workflow)
    │
    ├─ Leer .pipeline-v3-state.yaml
    │   └─ Si existe: reanudar desde último paso completado
    │   └─ Si no: iniciar desde Paso 0
    │
    ▼
PASO 0: Coherencia curricular
    │   Consultar registro de temas dados en 2026
    │   Reportar superposiciones al docente
    │   Esperar estrategia de tratamiento
    │   └─ Persisitir en estado: paso-0 completado
    │
    ▼
PASO 1a: Extracción ChromaDB — libro principal
    │   chroma_query_documents(collection="edu_knowledge", where={"type":"material","libro":libro_principal})
    │   └─ Si falla: ERROR y STOP (AD-03)
    │   └─ Persisitir en estado: paso-1a completado
    │
    ▼
PASO 1b: Enriquecimiento ChromaDB — libros secundarios
    │   chroma_query_documents por subtemas no suficientemente cubiertos en 1a
    │   └─ Persisitir en estado: paso-1b completado
    │
    ▼
PASO 1c: Web research — tendencias académicas
    │   Buscar tendencias recientes del tópico
    │   Identificar conflictos con bibliografía > 5 años
    │   └─ Persisitir en estado: paso-1c completado
    │
    ▼
GENERAR topic-extract.md (según esquema §4)
    │   Secciones: fuentes, conceptos-clave, ejemplos-bibliograficos, tendencias, superposiciones-detectadas
    │   Validar que al menos 1 fuente tiene página verificada
    │
    ▼
╔══════════════════════════════════════╗
║  CHECKPOINT 1 — Aprobación docente   ║
║  "Revisá topic-extract.md.           ║
║   Podés editarlo directamente.       ║
║   Aprobás para continuar?"           ║
╚══════════════════════════════════════╝
    │   └─ Persisitir en estado: checkpoint_1_aprobado: true
    │
    ▼
PASO 2: Plan de generación
    │   Lista ordenada de filminas con nivel de densidad
    │   Si --base previas: ejecutar análisis comparativo (AD-07)
    │
    ▼
╔══════════════════════════════════════╗
║  CHECKPOINT 2 — Aprobación del plan  ║
║  "Revisá el plan. Podés reordenar,   ║
║   agregar o eliminar filminas.       ║
║   Aprobás para generar?"             ║
╚══════════════════════════════════════╝
    │   └─ Persisitir en estado: checkpoint_2_aprobado: true
    │
    ▼
PASO 3: Generación de filminas (class-writer con topic-extract.md)
    │   Nivel 1/2/3 según parámetro
    │   Output: filminas.md, minuta.md (backup de v2 si existe)
    │
    ▼
PASO 4: Guía de estudio (study-guide-writer con topic-extract.md)
    │   Output: guia-estudio.md
    │
    ▼
PASO 5: Guía docente (create-teacher-guide con topic-extract.md)
    │   Output: guiaprofesor.md
    │
    ▼
COMPLETADO
    └─ Actualizar .pipeline-v3-state.yaml: status: complete
```

### Tabla de transiciones de estado

| Paso | Precondición | Acción principal | MCP/Tool | Fallo → |
|---|---|---|---|---|
| Paso 0 | estado inicializado | Consultar registro de temas | read_file (registro) | warn + continuar |
| Paso 1a | paso-0 en estado | Query ChromaDB libro principal | `chroma_query_documents` | **STOP** con diagnóstico |
| Paso 1b | paso-1a en estado | Query ChromaDB libros secundarios | `chroma_query_documents` | warn + continuar |
| Paso 1c | paso-1b en estado | Web research tendencias | `fetch_webpage` | warn + continuar |
| CP1 | topic-extract.md generado | Esperar aprobación docente | — | Esperar (blocking) |
| Paso 2 | CP1 aprobado | Generar plan filminas | — | Re-intentar |
| CP2 | plan generado | Esperar aprobación docente | — | Esperar (blocking) |
| Paso 3 | CP2 aprobado | Generar filminas + minuta | class-writer | Re-intentar desde CP2 |
| Paso 4 | Paso 3 completado | Generar guía de estudio | study-guide-writer | Re-intentar desde Paso 4 |
| Paso 5 | Paso 4 completado | Generar guía docente | create-teacher-guide | Re-intentar desde Paso 5 |

**Política de fallos:**
- Pasos 1b y 1c: no bloqueantes — el pipeline continúa con advertencia visible
- Paso 1a y ChromaDB en general: **bloqueante** (AD-03)
- Checkpoints: bloqueantes por diseño — esperan input docente
- Pasos 3/4/5: re-intentables desde el paso fallido; topic-extract.md ya está aprobado

---

## 6. Contratos de Agentes

### 6.1 topic-designer-v3 (Marcos v3)

**Responsabilidad:** Ejecutar Pasos 0–1c y generar `topic-extract.md`. Presentar checkpoints 1 y 2.

**Inputs:**
- `_edu/config.yaml` (libro_principal default, topics_folder, etc.)
- `_edu/active-topic.yaml` (topic_folder, topic_number, topic_name)
- `chroma-mcp` (acceso a ChromaDB)
- Parámetros de invocación: `--nivel`, `--libro`, `--base` (opcionales)

**Outputs:**
- `{topic_folder}/topic-extract.md` (esquema §4)
- `{topic_folder}/.pipeline-v3-state.yaml`

**Contrato de salida:** Antes de ceder control a class-writer-v3, el estado debe tener `checkpoint_1_aprobado: true` y `checkpoint_2_aprobado: true`.

---

### 6.2 class-writer (Roberto) — comportamiento condicional v3

**Comportamiento v2 (sin cambios):** Si `{topic_folder}/topic-extract.md` NO existe → comportamiento actual completo.

**Comportamiento v3 (nuevo):** Si `{topic_folder}/topic-extract.md` EXISTE Y `.pipeline-v3-state.yaml` tiene `checkpoint_2_aprobado: true`:
- Leer `topic-extract.md` como fuente de conceptos, ejemplos y terminología
- Generar filminas con el nivel indicado en el estado del pipeline
- Aplicar los modificadores de densidad del nivel (ver §3 AD-04)
- No re-consultar ChromaDB

**Modificadores de densidad por nivel:**
- Nivel 1: cada filmina tiene ≤ 3 conceptos, 1 ejemplo directo, sin variantes
- Nivel 2: cada filmina tiene ≤ 5 conceptos, 2-3 ejemplos, comparación contextual
- Nivel 3: cada filmina tiene todos los conceptos necesarios, múltiples ejemplos, contra-ejemplos, sin asumir conocimiento previo

---

### 6.3 study-guide-writer (Sofía) — comportamiento condicional v3

**Comportamiento v2 (sin cambios):** Si `topic-extract.md` NO existe → usa PDFs locales y filminas como v2.

**Comportamiento v3 (nuevo):** Si `topic-extract.md` EXISTE:
- Usar `topic-extract.md` como fuente bibliográfica primaria (ya verificada por docente)
- Las referencias de la guía citan libro/sección/página desde `fuentes` del topic-extract
- Nivel de profundidad de la guía correlacionado con el nivel del pipeline

---

### 6.4 create-teacher-guide — comportamiento condicional v3

**Comportamiento v2 (sin cambios):** Si `topic-extract.md` NO existe → comportamiento actual.

**Comportamiento v3 (nuevo):** Si `topic-extract.md` EXISTE:
- Incluir sección "Fundamentos bibliográficos" derivada de `topic-extract.md § fuentes`
- Incluir sección "Conceptos con profundidad variable" mostrando qué cambiaría en cada nivel
- Citar explícitamente las tendencias académicas del Paso 1c

---

## 7. Patrones de Implementación y Consistencia

### 7.1 Naming conventions para artefactos v3

| Concepto | Nombre de archivo | Comentario |
|---|---|---|
| Extracción bibliográfica | `topic-extract.md` | Snake-case con guión |
| Estado del pipeline | `.pipeline-v3-state.yaml` | Prefijo punto (oculto en Unix) |
| Backup de artefactos v2 | `{nombre}-v2-backup.md` | Sufijo `-v2-backup` |
| Nuevo workflow | `topic-cycle-v3/workflow.md` | Sufijo `-v3` |
| Nuevo agente | `topic-designer-v3.md` | Sufijo `-v3` |

### 7.2 Formato de referencias bibliográficas

Toda cita en `topic-extract.md` y en artefactos generados con v3 usa este formato unificado:

```
[Autor, Libro §Sección, p. N]
```

Ejemplo: `[Abelson & Sussman, SICP §1.3, p. 58]`

Si la página no está disponible: `[Autor, Libro §Sección, p. ⚠️ referencia incompleta]`

### 7.3 Invocación del workflow

Formato canónico:
```
@topic-cycle-v3 [tópico] [--libro LIBRO] [--nivel N] [--base RUTA_FILMINAS_PREVIAS]
```

Ejemplos:
```
@topic-cycle-v3 Programación Funcional
@topic-cycle-v3 Programación Funcional --libro SICP --nivel 2
@topic-cycle-v3 Programación Funcional --nivel 3
@topic-cycle-v3 Paradigma OO --nivel 2 --base temas/04-oo/filminas.md
```

### 7.4 Mensajes de checkpoint

Los checkpoints usan un formato estandarizado para que el docente siempre reconozca el patrón:

```
╔═══════════════════════════════════════════════════════════╗
║  CHECKPOINT [N] — [Nombre]                                ║
║  Revisá: [{ruta del artefacto}]                           ║
║  [Descripción breve de qué revisar]                       ║
║  Respondé "ok" para continuar, o indicá correcciones.    ║
╚═══════════════════════════════════════════════════════════╝
```

### 7.5 Propagación del nivel de densidad

El nivel se lee del estado del pipeline (`{topic_folder}/.pipeline-v3-state.yaml`) al inicio de cada paso de generación. Los agentes NO aceptan el nivel como parámetro de prompt — siempre lo leen del estado persisitido para garantizar consistencia entre Pasos 3, 4 y 5.

---

## 8. Estructura de Directorios

### 8.1 Artefactos nuevos por tema (v3)

```
{topic_folder}/                          # ej: salida/cursadas/2026/temas/08-funcional/
├── topic-extract.md                     # NUEVO — contrato bibliográfico (schema §4)
├── .pipeline-v3-state.yaml             # NUEVO — estado del pipeline (oculto)
├── filminas.md                         # EXISTENTE — sobrescrito por v3 (backup automático)
├── filminas-v2-backup.md               # NUEVO — backup automático si v2 existía
├── minuta.md                           # EXISTENTE — sobrescrito por v3
├── minuta-v2-backup.md                 # NUEVO — backup automático si v2 existía
├── guia-estudio.md                     # EXISTENTE — sobrescrito por v3
├── guiaprofesor.md                     # EXISTENTE — sobrescrito por v3
├── diseno.md                           # SOLO en v2 — v3 no lo genera ni modifica
└── topic.yaml                          # EXISTENTE — sin cambios
```

### 8.2 Nuevos archivos de agentes/workflows

```
_edu/
├── agents/
│   └── topic-designer-v3.md            # NUEVO — variante v3 de topic-designer
├── workflows/
│   ├── topic-cycle/
│   │   └── workflow.md                 # SIN CAMBIOS
│   └── topic-cycle-v3/                 # NUEVO
│       └── workflow.md
└── schemas/
    └── topic-extract-schema.yaml       # NUEVO — schema formal del contrato
```

### 8.3 Modificaciones a agentes existentes (mínimas)

Los agentes `class-writer.md`, `study-guide-writer.md`, `create-teacher-guide.md` reciben una única sección adicional en su `<context>` y una regla condicional:

```xml
<!-- Adición en <context> de cada agente downstream -->
<context-v3>
  Si existe {topic_folder}/topic-extract.md Y .pipeline-v3-state.yaml tiene
  checkpoint_2_aprobado: true → consumir topic-extract.md como fuente primaria.
  Ver reglas de comportamiento v3 en la sección correspondiente de este agente.
</context-v3>
```

---

## 9. Integración ChromaDB — Especificaciones

### 9.1 Queries del Paso 1a (libro principal)

```python
# Query semántica por subtemas del tópico
chroma_query_documents(
    collection_name="edu_knowledge",
    query_texts=["[tópico] [subtema_1]", "[tópico] [subtema_2]", ...],
    n_results=10,
    where={"type": "material", "libro": libro_principal}
)
```

Si `libro_principal` no está disponible como filtro exacto, usar solo `{"type": "material"}` y filtrar por relevancia en el resultado.

### 9.2 Queries del Paso 1b (libros secundarios)

Para subtemas con cobertura baja del libro principal (relevancia `baja` en resultados de 1a):

```python
chroma_query_documents(
    collection_name="edu_knowledge",
    query_texts=["[subtema con cobertura baja]"],
    n_results=5,
    where={"type": "material"}  # sin filtro de libro
)
```

### 9.3 Validación de disponibilidad

Al inicio del Paso 1a, verificar que la colección tiene documentos:

```python
chroma_get_collection_info(collection_name="edu_knowledge")
# Si count == 0 → ERROR con instrucción de ingesta:
# "Ejecutá: python salida/edu-standalone/scripts/knowledge_base.py ingest --include-material"
```

---

## 10. Registro de Temas Dados (Coherencia Curricular)

### 10.1 Fuente del registro

El Paso 0 consulta el registro de temas dados en la cursada activa. Las fuentes en orden de preferencia:

1. `{topics_folder}/*/topic.yaml` — campo `status: completado` indica tema dado
2. `_edu/active-topic.yaml` — tema actual (excluir de superposiciones)
3. Cualquier `{topic_folder}/diseno.md` existente — extrae conceptos cubiertos

### 10.2 Formato del reporte de coherencia

```markdown
## Reporte de Coherencia Curricular — [Nombre del Tema]

**Temas previos analizados:** [N]
**Superposiciones encontradas:** [M]

| Tema previo | Conceptos solapados | Solapamiento | Estrategia sugerida |
|---|---|---|---|
| 05-recursion | Funciones de orden superior, Lambda | Alto | asumir-conocido |
| 03-funciones | Closures básicos | Medio | resumir |

**Acción requerida:** Confirmá la estrategia para cada solapamiento antes de continuar.
```

---

## 11. Matriz de Compatibilidad

| Componente | v2 funcionando | v3 coexistiendo | Regresión posible |
|---|---|---|---|
| `topic-cycle/workflow.md` | ✅ Sin cambios | ✅ Archivos separados | ❌ No |
| `topic-designer.md` | ✅ Sin cambios | ✅ v3 es archivo nuevo | ❌ No |
| `class-writer.md` | ✅ Comportamiento base intacto | ✅ Lógica condicional nueva | ⚠️ Solo si topic-extract existe |
| `study-guide-writer.md` | ✅ Comportamiento base intacto | ✅ Lógica condicional nueva | ⚠️ Solo si topic-extract existe |
| `create-teacher-guide.md` | ✅ Comportamiento base intacto | ✅ Lógica condicional nueva | ⚠️ Solo si topic-extract existe |
| `slides_pipeline.py` | ✅ Sin cambios | ✅ Schema filminas invariante | ❌ No |
| `schema-registry.json` | ✅ Sin cambios | ✅ Schema filminas invariante | ❌ No |
| Temas ya generados (2026) | ✅ Accesibles | ✅ Sin topic-extract → v2 path | ❌ No |

**Invariante de compatibilidad:** La presencia de `topic-extract.md` en el directorio de un tema activa el comportamiento v3 en los agentes downstream. Su ausencia garantiza el comportamiento v2 exacto.

---

## 12. Validación de Requisitos

### Cobertura de FRs

| FR | Cubierto por | Decisión arquitectural |
|---|---|---|
| FR01 — Invocación con tópico/libro/nivel | Formato de invocación (§7.3) | AD-04 |
| FR02 — Libro default de config.yaml | `_edu/config.yaml` → `libro_principal` default | AD-06 |
| FR03 — Informar libro y nivel al inicio | workflow.md Paso 0 header | AD-01 |
| FR04 — Filminas año anterior como parámetro | `--base` en invocación | AD-07 |
| FR05–07 — Coherencia curricular | Paso 0 + reporte §10.2 | AD-01 |
| FR08 — ChromaDB obligatorio | Paso 1a fail-fast | AD-03 |
| FR09 — Libros secundarios | Paso 1b condicional | AD-01 |
| FR10 — Web research tendencias | Paso 1c | AD-01 |
| FR11 — Marcar libros > 5 años | Campo `conflicto_con_bibliografía` en tendencias | §4 schema |
| FR12 — topic-extract.md con secciones obligatorias | Schema §4 | AD-02 |
| FR13 — Persisitir y esperar aprobación CP1 | Checkpoint 1 en pipeline §5 | AD-01 |
| FR14 — Docente puede editar topic-extract.md | Checkpoint 1 espera edición | AD-01 |
| FR15–16 — Plan con CP2 y edición | Checkpoint 2 en pipeline §5 | AD-01 |
| FR17 — 3 niveles de densidad | §3 AD-04, §7.5 | AD-04 |
| FR18 — Guía de estudio sin re-invocar ChromaDB | Contrato agente §6.3 | AD-02 |
| FR19 — Guía docente con topic-extract.md | Contrato agente §6.4 | AD-02 |
| FR20 — Compatibilidad slides_pipeline.py | Schema filminas invariante | AD-05 |
| FR21–23 — Renovación material previo | Análisis comparativo §3 AD-07 | AD-07 |
| FR24–26 — Coexistencia v2/v3 | Matriz compatibilidad §11 | AD-05, AD-06 |

### Cobertura de NFRs

| NFR | Cubierto por | Verificación |
|---|---|---|
| NFR01 — Estado persisitido por paso | `.pipeline-v3-state.yaml` (AD-01) | Leer archivo al inicio de cada sesión |
| NFR02 — Fail-fast si chroma-mcp falla | AD-03 + mensaje estándar §3 | Error visible en consola de agente |
| NFR03 — CP persisitidos ante interrupción | Estado en disco con `checkpoint_N_aprobado` | Campo en .pipeline-v3-state.yaml |
| NFR04 — Citas con referencia verificable | Schema §4 con validación | Marcado automático "referencia incompleta" |
| NFR05 — Bloquear plan sin fuente verificada | Regla de validación en Paso 2 | Count de fuentes con página != null |
| NFR06 — Mismo formato de salida | Schema filminas invariante | AD-05 |
| NFR07 — Sin dependencias nuevas | Stack §2 — chroma-mcp ya instalado | — |
| NFR08 — Tiempo ≤ 150% de v2 | Checkpoints son tiempo docente (no sistema) | Medible post-implementación |
| NFR09 — Schema documentado formalmente | `_edu/schemas/topic-extract-schema.yaml` | §4 de este documento |
| NFR10 — Workflow independiente | `topic-cycle-v3/workflow.md` separado | AD-06 |

---

## 13. Riesgos Arquitecturales y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| ChromaDB devuelve fragmentos sin contexto suficiente | Media | Alto | Paso 1b enriquece con libros secundarios; docente revisa en CP1 |
| Docente edita topic-extract.md rompiendo el schema | Baja | Medio | topic-designer-v3 valida schema antes de CP1; si inválido, ofrece corrección |
| Pipeline interrumpido en estado inconsistente (CP1 aprobado pero topic-extract.md borrado) | Baja | Alto | Al reanudar, verificar existencia de artefactos previos; si falta, re-ejecutar desde el paso que generó el artefacto |
| class-writer detecta topic-extract.md de v3 sin checkpoint_2_aprobado y lo consume | Baja | Medio | Comportamiento v3 solo se activa si AMBAS condiciones se cumplen (§6.2) |
| Backup de v2 sobrescribe backup existente | Baja | Bajo | Al hacer backup, agregar timestamp: `filminas-v2-backup-YYYYMMDD.md` |

---

*Arquitectura generada con el workflow `bmad-create-architecture` (fast mode). Fecha: 2026-05-23.*  
*Próximo paso recomendado: crear epics y stories — `bmad-create-epics-and-stories` con este documento + prd.md como input.*
