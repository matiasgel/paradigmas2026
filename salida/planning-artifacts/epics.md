---
stepsCompleted: [1, 2, 3, 4]
workflowType: epics-and-stories
status: complete
completedAt: '2026-05-23'
inputDocuments:
  - salida/planning-artifacts/prd.md
  - salida/planning-artifacts/architecture-topic-cycle-v3.md
---

# Epics y Stories — topic-cycle-v3

**Proyecto:** paradigmas2026  
**Fecha:** 2026-05-23  
**PRD base:** prd.md | **Arquitectura base:** architecture-topic-cycle-v3.md  
**Contexto:** Brownfield — cursada 2026 activa; principio aditivo/opt-in obligatorio; cero regresiones.

---

## Inventario de Requisitos

### Requisitos Funcionales (FRs)

| ID | Área | Descripción resumida |
|---|---|---|
| FR01 | Invocación | Invocar topic-cycle-v3 con tópico, libro principal (override opcional) y nivel 1/2/3 |
| FR02 | Invocación | Usar libro de config.yaml como libro principal por defecto |
| FR03 | Invocación | Informar libro seleccionado y nivel al inicio de cada ejecución |
| FR04 | Invocación | Aceptar filminas del año anterior como parámetro opcional `--base` |
| FR05 | Coherencia | Consultar registro de temas dados en cursada 2026 antes de extracción |
| FR06 | Coherencia | Reportar superposiciones con temas previos y esperar confirmación docente |
| FR07 | Coherencia | Docente ajusta estrategia de tratamiento de superposiciones antes de continuar |
| FR08 | Bibliografía | Extraer de ChromaDB vía chroma-mcp como paso obligatorio no salteable |
| FR09 | Bibliografía | Enriquecer con libros secundarios cuando libro principal no cubre suficientemente |
| FR10 | Bibliografía | Web research de tendencias académicas recientes (Paso 1c) |
| FR11 | Bibliografía | Marcar libros > 5 años como "a verificar" si hay tendencias contradictorias |
| FR12 | Artefacto | Generar topic-extract.md con secciones: fuentes, conceptos-clave, ejemplos-bibliograficos, tendencias, superposiciones-detectadas |
| FR13 | Checkpoints | Persistir topic-extract.md y esperar aprobación explícita (Checkpoint 1) |
| FR14 | Checkpoints | Docente puede editar topic-extract.md antes de aprobar Checkpoint 1 |
| FR15 | Checkpoints | Generar plan de generación y esperar aprobación (Checkpoint 2) |
| FR16 | Checkpoints | Docente puede reordenar, agregar o eliminar filminas del plan |
| FR17 | Generación | Generar filminas en 3 niveles de densidad diferenciados |
| FR18 | Generación | Guía de estudio consume topic-extract.md desde disco sin re-invocar ChromaDB |
| FR19 | Generación | Guía docente consume topic-extract.md y filminas generadas |
| FR20 | Generación | Output compatible con slides_pipeline.py — schema filminas invariante |
| FR21 | Renovación | Comparar filminas previas con topic-extract.md nuevo (conservar/actualizar/eliminar/nueva) |
| FR22 | Renovación | Reportar análisis de renovación al docente antes de generar |
| FR23 | Renovación | Priorizar reúso/adaptación de filminas existentes sobre generación desde cero |
| FR24 | Compatibilidad | Workflow topic-cycle original funciona sin cambios |
| FR25 | Compatibilidad | topic-cycle-v3 activable por flag en config.yaml o invocación explícita |
| FR26 | Compatibilidad | Artefactos v3 conviven en mismo directorio sin conflictos con v2 |

### Requisitos No Funcionales (NFRs)

| ID | Categoría | Descripción resumida |
|---|---|---|
| NFR01 | Confiabilidad | Estado del pipeline persisitido en disco tras cada paso; reanudación sin reprocesar pasos anteriores |
| NFR02 | Confiabilidad | Fail-fast con diagnóstico explícito si chroma-mcp no disponible al inicio del Paso 1a |
| NFR03 | Confiabilidad | Checkpoints persisitidos ante interrupción de sesión — docente no pierde trabajo de revisión |
| NFR04 | Bibliografía | Toda cita incluye libro, autor y sección/página verificable; sin referencia completa → "referencia incompleta" |
| NFR05 | Bibliografía | Plan de generación (Paso 2) bloqueado si topic-extract.md no tiene al menos 1 fuente con página verificada |
| NFR06 | Compatibilidad | Agentes refactorizados producen output en los mismos formatos que sus versiones anteriores |
| NFR07 | Compatibilidad | Sin dependencias nuevas (chroma-mcp ya está configurado en producción) |
| NFR08 | Performance | Tiempo de generación total ≤ 150% de topic-cycle v2 (checkpoints son tiempo docente, no sistema) |
| NFR09 | Mantenibilidad | Esquema de topic-extract.md documentado formalmente; cualquier cambio requiere actualización de todos los consumidores |
| NFR10 | Mantenibilidad | topic-cycle-v3 implementado como archivo independiente; no modifica archivos de topic-cycle |

### Requisitos Técnicos de Arquitectura (impactan stories)

| Req. técnico | Fuente | Impacto en stories |
|---|---|---|
| `.pipeline-v3-state.yaml` en `{topic_folder}/` con campos: `pasos_completados`, `checkpoint_1_aprobado`, `checkpoint_2_aprobado`, `nivel`, `libro_principal` | AD-01 | E1 — stories de pipeline state |
| Activación v3 condicional: SOLO si existe `topic-extract.md` Y `checkpoint_2_aprobado: true` | AD-02 | E6 — stories de agentes downstream |
| `chroma_query_documents(collection="edu_knowledge", where={"type":"material"})` | §9 arq. | E2 — story Paso 1a |
| Backup automático antes de sobrescribir: `filminas-v2-backup-YYYYMMDD.md` | AD-05, §13 | E6 — story de backup |
| Schema formal con reglas de validación: ≥1 fuente con página, ≥3 conceptos-clave | §4 arq. | E2 — story de generación topic-extract |
| Niveles propagados desde estado — agentes NO aceptan nivel como parámetro de prompt | §7.5 arq. | E4 — story de propagación de nivel |

---

## Lista de Epics

| Epic | Título | Stories | FRs cubiertos | NFRs cubiertos |
|---|---|---|---|---|
| **E1** | Pipeline base v3 | 5 | FR01, FR03, FR13, FR14, FR15, FR16, FR24, FR25, FR26 | NFR01, NFR03, NFR10 |
| **E2** | Bibliographic-first | 5 | FR02, FR08, FR09, FR10, FR11, FR12 | NFR02, NFR04, NFR05, NFR07, NFR09 |
| **E3** | Coherencia curricular | 3 | FR05, FR06, FR07 | NFR01 (parcial) |
| **E4** | Niveles de densidad | 3 | FR01 (parcial), FR17 | NFR08 |
| **E5** | Renovación de año anterior | 3 | FR04, FR21, FR22, FR23 | — |
| **E6** | Agentes downstream | 4 | FR18, FR19, FR20, FR24, FR26 | NFR06, NFR07 |
| **Total** | | **23 stories** | **26 FRs** | **10 NFRs** |

---

## Epic 1: Pipeline base v3

**Objetivo:** Crear el workflow `topic-cycle-v3` con estructura de 7 pasos, mecanismo de persistencia de estado y dos checkpoints de aprobación docente. Este epic establece el andamiaje completo sobre el cual los demás epics construyen.

**Artefactos producidos:**
- `_edu/workflows/topic-cycle-v3/workflow.md`
- `_edu/agents/topic-designer-v3.md`
- Mecanismo `.pipeline-v3-state.yaml` (inicialización, lectura, actualización)
- Checkpoint 1 y Checkpoint 2 con formato estandarizado

**Criterio de completitud del epic:** Un docente puede invocar `@topic-cycle-v3 [tópico]`, ver el mensaje de inicio con libro/nivel, y el workflow persiste el estado entre pasos. Los checkpoints bloquean la ejecución esperando "ok".

---

### Story 1.1: Crear workflow topic-cycle-v3 con estructura de 7 pasos

**Como docente, quiero** un nuevo archivo de workflow `topic-cycle-v3` con los 7 pasos del pipeline documentados, el formato de invocación canónico y la instrucción de no modificar el workflow v2 existente, **para poder** invocar el pipeline v3 sin riesgo de afectar el sistema en producción.

**FRs cubiertos:** FR01, FR03, FR24, FR25  
**NFR cubiertos:** NFR10

**Criterios de aceptación:**

*Dado que* no existe `_edu/workflows/topic-cycle-v3/workflow.md`,  
*cuando* se crea el archivo,  
*entonces* el archivo existe en la ruta exacta `_edu/workflows/topic-cycle-v3/workflow.md` y el archivo `_edu/workflows/topic-cycle/workflow.md` permanece sin modificaciones.

*Dado que* el workflow es invocado con `@topic-cycle-v3 Programación Funcional --libro SICP --nivel 2`,  
*cuando* el agente topic-designer-v3 inicia la ejecución,  
*entonces* el primer output visible al docente informa explícitamente: tópico, libro principal seleccionado (SICP) y nivel activo (2).

*Dado que* el workflow es invocado sin `--libro`,  
*cuando* el agente lee la configuración,  
*entonces* usa `libro_principal` de `salida/edu-standalone/_edu/config.yaml` como valor por defecto e informa al docente qué libro fue seleccionado automáticamente.

*Dado que* el workflow es invocado sin `--nivel`,  
*cuando* el agente inicializa el estado,  
*entonces* usa nivel 2 como valor por defecto y lo informa al inicio.

**Detalles técnicos de implementación:**
- El archivo workflow.md documenta el formato de invocación canónico: `@topic-cycle-v3 [tópico] [--libro LIBRO] [--nivel N] [--base RUTA]`
- La sección de inicio del workflow incluye el bloque de "mensaje de bienvenida" con libro, nivel, y tópico
- El workflow referencia explícitamente que `topic-cycle/workflow.md` permanece invariante (principio brownfield)
- Estructura del workflow: Paso 0 → Paso 1a → Paso 1b → Paso 1c → CP1 → Paso 2 → CP2 → Paso 3 → Paso 4 → Paso 5

---

### Story 1.2: Crear agente topic-designer-v3

**Como docente, quiero** un agente `topic-designer-v3.md` distinto del agente `topic-designer.md` existente, con la persona extendida de Marcos v3 y las instrucciones para ejecutar los Pasos 0 a 1c más la generación de `topic-extract.md`, **para poder** ejecutar el pipeline v3 sin modificar el agente de producción actual.

**FRs cubiertos:** FR01, FR24  
**NFR cubiertos:** NFR10

**Criterios de aceptación:**

*Dado que* existe `_edu/agents/topic-designer.md` en producción,  
*cuando* se crea `_edu/agents/topic-designer-v3.md`,  
*entonces* el archivo `_edu/agents/topic-designer.md` permanece sin ninguna modificación, y el nuevo agente existe en la ruta `_edu/agents/topic-designer-v3.md`.

*Dado que* el agente topic-designer-v3 es invocado,  
*cuando* presenta su identidad al docente,  
*entonces* se identifica como "Marcos v3" con responsabilidades explícitas: Pasos 0–1c, generación de `topic-extract.md`, y presentación de Checkpoints 1 y 2.

*Dado que* el agente topic-designer-v3 recibe el estado del pipeline con `pasos_completados: ["paso-1a", "paso-1b"]`,  
*cuando* lee `.pipeline-v3-state.yaml` al inicio de la sesión,  
*entonces* informa al docente que retoma desde el Paso 1c y no re-ejecuta los pasos anteriores.

**Detalles técnicos de implementación:**
- El agente hereda la persona de Marcos pero tiene un menú ampliado con los 7 pasos v3
- Incluye instrucciones explícitas para leer `.pipeline-v3-state.yaml` al inicio
- Referencia el esquema `_edu/schemas/topic-extract-schema.yaml` para la generación
- Incluye los contratos de salida: antes de ceder control a class-writer, el estado debe tener `checkpoint_1_aprobado: true` Y `checkpoint_2_aprobado: true`

---

### Story 1.3: Implementar persistencia de estado del pipeline

**Como docente, quiero** que el pipeline persista su estado en `.pipeline-v3-state.yaml` tras completar cada paso y lo lea al inicio de cada sesión para reanudar sin reprocesar, **para poder** interrumpir la sesión en cualquier momento sin perder el trabajo realizado.

**FRs cubiertos:** FR26 (convivencia de artefactos)  
**NFR cubiertos:** NFR01, NFR03

**Criterios de aceptación:**

*Dado que* el pipeline está en el Paso 0,  
*cuando* el docente invoca por primera vez `@topic-cycle-v3 [tópico]`,  
*entonces* el agente crea `{topic_folder}/.pipeline-v3-state.yaml` con campos: `topic`, `libro_principal`, `nivel`, `base_filminas_previas`, `pasos_completados: []`, `checkpoint_1_aprobado: false`, `checkpoint_2_aprobado: false`, `iniciado_en` (timestamp ISO), `ultimo_paso_en`.

*Dado que* el Paso 1a completó exitosamente,  
*cuando* el agente persiste el estado,  
*entonces* `pasos_completados` incluye `"paso-1a"` y `ultimo_paso_en` tiene el timestamp actualizado.

*Dado que* el pipeline fue interrumpido con `pasos_completados: ["paso-0", "paso-1a", "paso-1b"]`,  
*cuando* el docente reinvoca el workflow en una nueva sesión,  
*entonces* el agente lee el estado, informa "Reanudando desde Paso 1c", y ejecuta únicamente desde ese paso sin repetir 0, 1a, 1b.

*Dado que* el Checkpoint 1 fue aprobado y la sesión fue interrumpida,  
*cuando* el docente reinicia el workflow,  
*entonces* `checkpoint_1_aprobado: true` se preserva en el archivo y el pipeline no vuelve a pedir aprobación del topic-extract.md.

**Detalles técnicos de implementación:**
- El agente topic-designer-v3 tiene instrucciones explícitas de leer el state file como primera acción
- La escritura del state file usa el formato YAML documentado en AD-01 de la arquitectura
- `.pipeline-v3-state.yaml` usa prefijo `.` (archivo oculto en Unix), conviviendo en `{topic_folder}/` sin colisionar con artefactos v2

---

### Story 1.4: Implementar Checkpoint 1 — aprobación de topic-extract.md

**Como docente, quiero** que el pipeline se detenga después de generar `topic-extract.md` y espere mi aprobación explícita con posibilidad de editar el archivo directamente, **para poder** validar el grounding bibliográfico antes de que se genere cualquier material de clase.

**FRs cubiertos:** FR13, FR14  
**NFR cubiertos:** NFR03

**Criterios de aceptación:**

*Dado que* el Paso 1c completó y `topic-extract.md` fue generado,  
*cuando* el pipeline alcanza el Checkpoint 1,  
*entonces* muestra el bloque visual estandarizado:
```
╔═══════════════════════════════════════════════════════════╗
║  CHECKPOINT 1 — Aprobación de topic-extract.md            ║
║  Revisá: [{topic_folder}/topic-extract.md]                ║
║  Verificá: fuentes, conceptos-clave, ejemplos.            ║
║  Podés editar el archivo directamente.                    ║
║  Respondé "ok" para continuar, o indicá correcciones.    ║
╚═══════════════════════════════════════════════════════════╝
```

*Dado que* el docente responde "ok" al Checkpoint 1,  
*cuando* el agente persiste el estado,  
*entonces* `.pipeline-v3-state.yaml` tiene `checkpoint_1_aprobado: true` y el pipeline continúa al Paso 2.

*Dado que* el docente edita `topic-extract.md` y luego responde "ok",  
*cuando* el agente recibe la aprobación,  
*entonces* persiste `checkpoint_1_aprobado: true` con el archivo editado por el docente, sin revertir los cambios manuales.

*Dado que* el docente indica una corrección (ej. "agregá más ejemplos de closures"),  
*cuando* el agente recibe la corrección,  
*entonces* actualiza `topic-extract.md` según la instrucción y vuelve a presentar el Checkpoint 1 — no continúa sin aprobación explícita.

---

### Story 1.5: Implementar Checkpoint 2 — aprobación del plan de generación

**Como docente, quiero** revisar y modificar el plan de filminas (lista ordenada con nivel de densidad) antes de que comience la generación del material, **para poder** controlar la estructura pedagógica del tema antes del costoso proceso de generación.

**FRs cubiertos:** FR15, FR16  
**NFR cubiertos:** NFR03

**Criterios de aceptación:**

*Dado que* el Checkpoint 1 fue aprobado,  
*cuando* el agente ejecuta el Paso 2 (plan de generación),  
*entonces* produce una lista numerada de filminas con: número, título descriptivo, conceptos cubiertos, nivel de densidad aplicado; y presenta el Checkpoint 2 con el bloque visual estandarizado.

*Dado que* el plan tiene 12 filminas propuestas,  
*cuando* el docente responde "mové la filmina 5 al final",  
*entonces* el agente actualiza el plan reordenando y presenta el plan modificado antes de pedir confirmación final.

*Dado que* el docente responde "ok" al Checkpoint 2 (sin modificaciones),  
*cuando* el agente persiste el estado,  
*entonces* `.pipeline-v3-state.yaml` tiene `checkpoint_2_aprobado: true` y el pipeline continúa al Paso 3.

*Dado que* el docente responde "eliminá la filmina 3 y agregá una sobre tail recursion",  
*cuando* el agente actualiza el plan,  
*entonces* el plan final contiene exactamente las filminas especificadas por el docente y el agente no comienza Paso 3 hasta recibir confirmación explícita del plan modificado.

---

## Epic 2: Bibliographic-first

**Objetivo:** Implementar el grounding bibliográfico obligatorio vía ChromaDB como corazón del pipeline v3: esquema formal de `topic-extract.md`, Pasos 1a/1b/1c, y generación del artefacto completo con validaciones.

**Artefactos producidos:**
- `_edu/schemas/topic-extract-schema.yaml`
- Secciones de Pasos 1a, 1b, 1c en `topic-designer-v3.md`
- Secciones de generación y validación de `topic-extract.md` en `topic-designer-v3.md`

**Criterio de completitud del epic:** El agente topic-designer-v3 genera un `topic-extract.md` con todas las secciones del esquema, al menos una fuente con página verificada, y falla explícitamente si chroma-mcp no está disponible.

---

### Story 2.1: Crear esquema formal topic-extract-schema.yaml

**Como docente, quiero** un schema YAML documentado que defina exactamente la estructura de `topic-extract.md` — secciones, campos, tipos y reglas de validación — **para poder** confiar en que todos los agentes consumidores del artefacto lo interpretan de forma predecible.

**FRs cubiertos:** FR12  
**NFR cubiertos:** NFR09

**Criterios de aceptación:**

*Dado que* no existe `_edu/schemas/topic-extract-schema.yaml`,  
*cuando* se crea el archivo,  
*entonces* el schema documenta las 5 secciones obligatorias: `fuentes`, `conceptos-clave`, `ejemplos-bibliograficos`, `tendencias`, `superposiciones-detectadas`, con todos los campos, tipos y si son obligatorios u opcionales.

*Dado que* el schema está creado,  
*cuando* se revisa la sección `fuentes`,  
*entonces* especifica los campos: `libro`, `autor`, `seccion`, `pagina` (null permitido → marcar "referencia incompleta"), `relevancia` (alta|media), `fragmento` — todos documentados con tipo y obligatoriedad.

*Dado que* el schema está creado,  
*cuando* se revisan las reglas de validación,  
*entonces* el schema documenta explícitamente: (a) `fuentes` debe tener ≥1 ítem con `pagina` no nulo, (b) `conceptos-clave` debe tener ≥3 ítems, (c) `superposiciones-detectadas` puede estar vacío.

*Dado que* el schema está creado,  
*cuando* se revisa el frontmatter del esquema de `topic-extract.md`,  
*entonces* documenta los campos obligatorios del header YAML: `tema`, `libro_principal`, `nivel`, `generado_en`, `aprobado_en` (null hasta CP1), `version`.

**Detalles técnicos de implementación:**
- El archivo es un YAML con comentarios descriptivos extensos (fuente de verdad para todos los agentes)
- Incluye un ejemplo completo de `topic-extract.md` válido con datos ficticios para referencia
- Documenta el formato canónico de cita: `[Autor, Libro §Sección, p. N]`

---

### Story 2.2: Implementar Paso 1a — extracción ChromaDB libro principal con fail-fast

**Como docente, quiero** que el sistema consulte ChromaDB con el libro principal como primer paso del pipeline y falle explícitamente si chroma-mcp no está disponible, **para poder** tener certeza de que cualquier material generado está anclado a la bibliografía verificada de la materia.

**FRs cubiertos:** FR02, FR08  
**NFR cubiertos:** NFR02, NFR07

**Criterios de aceptación:**

*Dado que* chroma-mcp no está disponible (MCP server inactivo),  
*cuando* el Paso 1a intenta ejecutar la query,  
*entonces* el pipeline detiene la ejecución con el mensaje estándar:
```
ERROR [paso-1a]: chroma-mcp no disponible.
Diagnóstico: verificar que el MCP server está activo en .vscode/mcp.json
El pipeline NO continúa sin grounding bibliográfico verificado.
```
y NO degrada silenciosamente a generación sin grounding.

*Dado que* chroma-mcp está disponible y el libro principal es "SICP",  
*cuando* el Paso 1a ejecuta la query,  
*entonces* usa `chroma_query_documents(collection_name="edu_knowledge", query_texts=[subtemas del tópico], n_results=10, where={"type": "material", "libro": libro_principal})`.

*Dado que* el filtro por `libro_principal` no devuelve resultados (libro no indexado con ese nombre exacto),  
*cuando* el Paso 1a intenta la query filtrada,  
*entonces* reintenta con `where={"type": "material"}` sin filtro de libro, filtra por relevancia en el resultado, e informa al docente que usó el corpus completo sin filtrar por libro específico.

*Dado que* la colección `edu_knowledge` tiene count == 0,  
*cuando* se verifica la disponibilidad con `chroma_get_collection_info`,  
*entonces* muestra: "Colección edu_knowledge vacía. Ejecutá: python salida/edu-standalone/scripts/knowledge_base.py ingest --include-material" y detiene el pipeline.

*Dado que* el Paso 1a completó exitosamente,  
*cuando* el agente persiste el estado,  
*entonces* `pasos_completados` incluye `"paso-1a"` y los resultados de la query están disponibles para la generación de topic-extract.md.

---

### Story 2.3: Implementar Paso 1b — enriquecimiento con libros secundarios

**Como docente, quiero** que el sistema consulte libros secundarios del corpus para subtemas con baja cobertura del libro principal, **para poder** obtener un topic-extract.md más completo cuando el libro principal no cubre todos los ángulos del tópico.

**FRs cubiertos:** FR09  
**NFR cubiertos:** NFR07

**Criterios de aceptación:**

*Dado que* el Paso 1a completó y hay subtemas con relevancia "baja" en los resultados,  
*cuando* el Paso 1b ejecuta sus queries,  
*entonces* para cada subtema con cobertura baja usa `chroma_query_documents(collection_name="edu_knowledge", query_texts=[subtema], n_results=5, where={"type": "material"})` sin filtro de libro.

*Dado que* el Paso 1b encuentra resultados en libros secundarios,  
*cuando* construye las fuentes del topic-extract.md,  
*entonces* los resultados de libros secundarios se agregan con `relevancia: "media"` y con el campo `libro` del libro secundario correspondiente.

*Dado que* chroma-mcp falla durante el Paso 1b (pero funcionó en 1a),  
*cuando* el Paso 1b encuentra el error,  
*entonces* el pipeline continúa con una advertencia visible: "⚠️ Paso 1b: enriquecimiento con libros secundarios no disponible. Continuando con cobertura del libro principal únicamente." — el Paso 1b no es bloqueante.

*Dado que* todos los subtemas tienen cobertura suficiente del libro principal (relevancia alta),  
*cuando* el Paso 1b evalúa si ejecutar queries,  
*entonces* lo omite e informa: "Paso 1b: cobertura suficiente del libro principal. No se requieren libros secundarios."

---

### Story 2.4: Implementar Paso 1c — web research de tendencias académicas

**Como docente, quiero** que el pipeline busque tendencias académicas recientes sobre el tópico y detecte posibles desactualizaciones en la bibliografía asignada, **para poder** enriquecer el material con perspectivas actuales y alertar sobre contenido bibliográfico potencialmente desactualizado.

**FRs cubiertos:** FR10, FR11  
**NFR cubiertos:** NFR07

**Criterios de aceptación:**

*Dado que* el Paso 1b completó,  
*cuando* el Paso 1c ejecuta web research,  
*entonces* busca tendencias académicas recientes del tópico (últimos 3-5 años) e identifica al menos 1-3 tendencias relevantes.

*Dado que* una tendencia académica contradice o supera contenido de un libro con > 5 años de antigüedad,  
*cuando* el agente construye la sección `tendencias` del topic-extract.md,  
*entonces* el ítem de tendencia tiene `conflicto_con_bibliografía: "sí"` y `nota` describiendo qué sección del libro podría estar desactualizada, y la fuente bibliográfica correspondiente en `fuentes` se marca con "⚠️ a verificar".

*Dado que* el web research falla (sin acceso a internet o herramienta no disponible),  
*cuando* el Paso 1c encuentra el error,  
*entonces* el pipeline continúa con advertencia: "⚠️ Paso 1c: web research no disponible. La sección `tendencias` estará vacía." — el Paso 1c no es bloqueante.

*Dado que* el Paso 1c completó,  
*cuando* se persiste el estado,  
*entonces* `pasos_completados` incluye `"paso-1c"`.

---

### Story 2.5: Implementar generación completa de topic-extract.md con validaciones

**Como docente, quiero** que el agente genere un `topic-extract.md` completo según el esquema formal, con validaciones automáticas de obligatoriedad y marcado de referencias incompletas, **para poder** revisar un artefacto bien estructurado y confiable en el Checkpoint 1.

**FRs cubiertos:** FR12, FR13, FR14  
**NFR cubiertos:** NFR04, NFR05

**Criterios de aceptación:**

*Dado que* los Pasos 1a, 1b, 1c completaron,  
*cuando* el agente genera `topic-extract.md`,  
*entonces* el archivo contiene las 5 secciones obligatorias (fuentes, conceptos-clave, ejemplos-bibliograficos, tendencias, superposiciones-detectadas) y el frontmatter YAML con todos los campos requeridos del esquema.

*Dado que* una fuente bibliográfica no tiene número de página disponible en el fragmento de ChromaDB,  
*cuando* el agente construye el ítem de fuente,  
*entonces* el campo `pagina` es `null` y el ítem se marca con el texto `⚠️ referencia incompleta` visible en el archivo.

*Dado que* `topic-extract.md` fue generado con todas las fuentes sin `pagina` verificable (todos null),  
*cuando* el docente aprueba CP1 y el pipeline intenta avanzar al Paso 2,  
*entonces* el pipeline bloquea el avance e informa: "NFR05: No se puede generar el plan sin al menos una fuente con página verificada. Editá topic-extract.md agregando al menos una referencia completa."

*Dado que* `topic-extract.md` tiene menos de 3 ítems en `conceptos-clave`,  
*cuando* el agente valida el artefacto antes de presentar CP1,  
*entonces* el agente corrige automáticamente el artefacto agregando conceptos faltantes basados en los resultados de ChromaDB, antes de presentarlo al docente.

*Dado que* el topic-extract.md fue generado y validado,  
*cuando* el agente lo persiste en `{topic_folder}/topic-extract.md`,  
*entonces* el frontmatter tiene `aprobado_en: null` (se actualiza recién en CP1) y `generado_en` tiene el timestamp de generación.

---

## Epic 3: Coherencia curricular

**Objetivo:** Implementar el Paso 0 del pipeline — consulta al registro de temas dados en la cursada 2026, detección de superposiciones conceptuales, reporte al docente y captura de estrategia de tratamiento antes de la extracción bibliográfica.

**Artefactos producidos:**
- Sección Paso 0 en `topic-designer-v3.md`
- Formato del reporte de coherencia curricular
- Persistencia de estrategia de tratamiento en el estado del pipeline

**Criterio de completitud del epic:** El agente topic-designer-v3 escanea temas previos completados, genera un reporte de superposiciones formateado, y captura la estrategia del docente antes de continuar al Paso 1a.

---

### Story 3.1: Implementar Paso 0 — escaneo del registro de temas dados

**Como docente, quiero** que el pipeline escanee automáticamente los temas ya dados en la cursada 2026 y extraiga los conceptos cubiertos, **para poder** detectar superposiciones antes de generar nuevo material.

**FRs cubiertos:** FR05  
**NFR cubiertos:** NFR01 (parcial)

**Criterios de aceptación:**

*Dado que* existe `{topics_folder}/` con múltiples subcarpetas de temas,  
*cuando* el Paso 0 ejecuta el escaneo,  
*entonces* lee el `topic.yaml` de cada subcarpeta y considera "tema dado" a los que tienen `status: completado` (excluyendo el tema actual de `active-topic.yaml`).

*Dado que* un tema dado tiene `diseno.md` disponible,  
*cuando* el Paso 0 extrae conceptos,  
*entonces* usa `diseno.md` como fuente de conceptos cubiertos en ese tema.

*Dado que* ningún tema previo tiene `status: completado` (primer tema del ciclo),  
*cuando* el Paso 0 completa el escaneo,  
*entonces* el pipeline continúa sin checkpoint intermedio e informa: "Paso 0: No se encontraron temas previos completados. Sin superposiciones a reportar."

*Dado que* el directorio de temas no existe o está vacío,  
*cuando* el Paso 0 intenta el escaneo,  
*entonces* continúa con advertencia visible y `superposiciones-detectadas` queda vacío en topic-extract.md.

---

### Story 3.2: Implementar reporte de coherencia curricular con formato estándar

**Como docente, quiero** recibir un reporte formateado con las superposiciones detectadas (tema previo, conceptos solapados, nivel de solapamiento) antes de continuar el pipeline, **para poder** decidir conscientemente cómo tratar cada superposición en el nuevo material.

**FRs cubiertos:** FR06  
**NFR cubiertos:** —

**Criterios de aceptación:**

*Dado que* el escaneo del Paso 0 encontró superposiciones,  
*cuando* el agente presenta el reporte al docente,  
*entonces* usa el formato de tabla documentado en §10.2 de la arquitectura, con columnas: "Tema previo", "Conceptos solapados", "Nivel de solapamiento" (alto/medio/bajo), "Estrategia sugerida".

*Dado que* el reporte fue presentado,  
*cuando* el agente espera respuesta del docente,  
*entonces* el pipeline se detiene (blocking) hasta recibir confirmación de la estrategia para cada superposición, antes de continuar al Paso 1a.

*Dado que* el docente necesita ver el reporte completo antes de decidir,  
*cuando* hay más de 5 superposiciones,  
*entonces* el reporte lista todas y pide al docente que confirme la estrategia globalmente ("mismo tratamiento para todas") o ítem por ítem.

---

### Story 3.3: Capturar estrategia de superposición y propagarla al topic-extract.md

**Como docente, quiero** que la estrategia que defino para cada superposición (asumir-conocido, resumir, referenciar) quede registrada en el estado del pipeline y se propague al topic-extract.md, **para poder** que la generación de material respete exactamente las decisiones curriculares que tomé.

**FRs cubiertos:** FR07  
**NFR cubiertos:** NFR01 (parcial)

**Criterios de aceptación:**

*Dado que* el docente confirma la estrategia para las superposiciones detectadas,  
*cuando* el agente procesa la respuesta,  
*entonces* el estado del pipeline registra las estrategias y `pasos_completados` incluye `"paso-0"`.

*Dado que* las estrategias fueron capturadas,  
*cuando* el agente genera `topic-extract.md` (post Pasos 1a-1c),  
*entonces* la sección `superposiciones-detectadas` contiene cada superposición con el campo `estrategia` exactamente como fue definida por el docente (no como fue sugerida por el sistema).

*Dado que* la estrategia es "asumir-conocido" para un concepto,  
*cuando* el agente genera el `topic-extract.md`,  
*entonces* el concepto solapado aparece en `superposiciones-detectadas` con `estrategia: "asumir-conocido"` y este dato está disponible para que class-writer lo considere al generar las filminas.

---

## Epic 4: Niveles de densidad

**Objetivo:** Implementar el sistema de 3 niveles de densidad como parámetro de primera clase: lectura desde estado del pipeline, modificadores de prompt para class-writer, y correlación de nivel en study-guide-writer.

**Artefactos producidos:**
- Sección de procesamiento de `--nivel` en `topic-designer-v3.md`
- Modificadores de densidad en sección v3 de `class-writer.md`
- Modificadores de nivel en sección v3 de `study-guide-writer.md`

**Criterio de completitud del epic:** El mismo tópico generado con nivel 1 vs nivel 3 produce filminas visiblemente distintas en extensión, profundidad y cantidad de ejemplos (ratio ≥ 2x en palabras).

---

### Story 4.1: Implementar parámetro --nivel y propagación al estado del pipeline

**Como docente, quiero** especificar el nivel de densidad al invocar el workflow (o usar nivel 2 por defecto) y que ese nivel se propague automáticamente a todos los pasos de generación desde el estado persisitido, **para poder** controlar la profundidad del material con un único parámetro sin tener que indicarlo en cada agente.

**FRs cubiertos:** FR01 (parcial), FR17 (prerequisito)  
**NFR cubiertos:** NFR08

**Criterios de aceptación:**

*Dado que* la invocación incluye `--nivel 3`,  
*cuando* el agente inicializa `.pipeline-v3-state.yaml`,  
*entonces* el campo `nivel: 3` queda persisitido en el archivo de estado.

*Dado que* la invocación no incluye `--nivel`,  
*cuando* el agente inicializa el estado,  
*entonces* el campo `nivel: 2` queda persisitido como valor por defecto.

*Dado que* el estado del pipeline tiene `nivel: 1`,  
*cuando* class-writer y study-guide-writer leen el nivel al inicio de sus respectivos pasos,  
*entonces* leen `nivel` del archivo `.pipeline-v3-state.yaml` del topic_folder, NO del prompt ni de ningún parámetro del agente — garantizando consistencia entre todos los pasos de generación.

---

### Story 4.2: Implementar modificadores de densidad en class-writer (niveles 1, 2 y 3)

**Como docente, quiero** que class-writer genere filminas con características distintas según el nivel de densidad leído del estado del pipeline — nivel 1 introductorio, nivel 2 estándar, nivel 3 exhaustivo — **para poder** obtener material pedagógicamente diferenciado para distintos momentos del curso sin post-procesamiento.

**FRs cubiertos:** FR17, FR20  
**NFR cubiertos:** NFR06, NFR08

**Criterios de aceptación:**

*Dado que* el estado tiene `nivel: 1` y `checkpoint_2_aprobado: true`,  
*cuando* class-writer genera cada filmina en comportamiento v3,  
*entonces* cada filmina tiene ≤3 conceptos, 1 ejemplo directo, sin variantes ni detalles de implementación, y el nivel Bloom implícito es Recordar/Comprender.

*Dado que* el estado tiene `nivel: 2` y `checkpoint_2_aprobado: true`,  
*cuando* class-writer genera cada filmina en comportamiento v3,  
*entonces* cada filmina tiene ≤5 conceptos, 2-3 ejemplos con comparación contextual, y el nivel Bloom implícito es Aplicar/Analizar.

*Dado que* el estado tiene `nivel: 3` y `checkpoint_2_aprobado: true`,  
*cuando* class-writer genera cada filmina en comportamiento v3,  
*entonces* cada filmina tiene todos los conceptos necesarios, múltiples ejemplos, contra-ejemplos y variantes, sin asumir conocimiento previo, y el nivel Bloom implícito es Analizar/Evaluar.

*Dado que* class-writer genera en nivel 3 y luego en nivel 1 para el mismo tópico,  
*cuando* se compara el total de palabras de ambos outputs,  
*entonces* el output de nivel 3 tiene al menos el doble de palabras que el output de nivel 1 (ratio ≥ 2x — NFR medible post-implementación).

*Dado que* class-writer genera en comportamiento v3,  
*cuando* produce `filminas.md`,  
*entonces* el schema y estructura de `filminas.md` son idénticos al output de class-writer en comportamiento v2 — la diferencia es solo en contenido, no en formato.

---

### Story 4.3: Implementar propagación de nivel en study-guide-writer

**Como docente, quiero** que study-guide-writer correlacione la profundidad de la guía de estudio con el nivel del pipeline, **para poder** que el material de apoyo sea consistente con la profundidad de las filminas generadas.

**FRs cubiertos:** FR18 (parcial)  
**NFR cubiertos:** NFR06, NFR08

**Criterios de aceptación:**

*Dado que* el estado tiene `nivel: 1` y study-guide-writer usa comportamiento v3,  
*cuando* genera la guía de estudio,  
*entonces* la guía tiene formato introductorio: definiciones cortas, 1-2 ejemplos por concepto, sin análisis comparativo.

*Dado que* el estado tiene `nivel: 3` y study-guide-writer usa comportamiento v3,  
*cuando* genera la guía de estudio,  
*entonces* la guía es exhaustiva: definiciones extendidas, múltiples ejemplos, variantes, referencias a páginas específicas de los libros, sección de "para profundizar".

*Dado que* study-guide-writer es invocado sin `topic-extract.md` presente (comportamiento v2),  
*cuando* genera la guía,  
*entonces* el comportamiento es exactamente el mismo que antes de esta story — cero regresión.

---

## Epic 5: Renovación de año anterior

**Objetivo:** Implementar el análisis comparativo de filminas previas contra el topic-extract.md nuevo, con categorización automática y priorización de reúso sobre generación desde cero.

**Artefactos producidos:**
- Sección de procesamiento de `--base` en `topic-designer-v3.md`
- Algoritmo de análisis comparativo (categorías: conservar/actualizar/eliminar/nueva)
- Reporte de renovación como artefacto presentado en Checkpoint 2

**Criterio de completitud del epic:** Dado un archivo de filminas previas y un topic-extract.md aprobado, el sistema categoriza cada filmina previa y genera un reporte que el docente aprueba antes de la generación.

---

### Story 5.1: Implementar procesamiento del parámetro --base

**Como docente, quiero** poder proveer filminas del año anterior al invocar el workflow con `--base RUTA`, y que el sistema lea ese archivo y lo mantenga disponible para el análisis comparativo post-Checkpoint 1, **para poder** iniciar el proceso de renovación de material histórico.

**FRs cubiertos:** FR04  
**NFR cubiertos:** —

**Criterios de aceptación:**

*Dado que* la invocación incluye `--base temas/08-funcional/filminas-2025.md`,  
*cuando* el agente inicializa el estado del pipeline,  
*entonces* `.pipeline-v3-state.yaml` tiene `base_filminas_previas: "temas/08-funcional/filminas-2025.md"`.

*Dado que* el archivo especificado en `--base` no existe,  
*cuando* el agente intenta leerlo,  
*entonces* informa: "⚠️ Archivo de base no encontrado: [ruta]. Continuando sin renovación de material previo." y el pipeline continúa normalmente sin análisis comparativo.

*Dado que* la invocación no incluye `--base`,  
*cuando* el agente inicializa el estado,  
*entonces* `base_filminas_previas: null` y el análisis comparativo de Paso 2 se omite completamente.

---

### Story 5.2: Implementar análisis comparativo filminas previas vs topic-extract.md

**Como docente, quiero** que el sistema compare cada filmina del año anterior contra el topic-extract.md aprobado y las categorice en conservar/actualizar/eliminar/nueva, **para poder** entender exactamente qué del material histórico sigue siendo válido antes de decidir la estrategia de generación.

**FRs cubiertos:** FR21  
**NFR cubiertos:** —

**Criterios de aceptación:**

*Dado que* el Checkpoint 1 fue aprobado y `base_filminas_previas` no es null,  
*cuando* el Paso 2 ejecuta el análisis comparativo,  
*entonces* evalúa cada filmina previa contra `topic-extract.md` y la categoriza como:
- `conservar`: contenido alineado con topic-extract.md actual sin cambios de terminología
- `actualizar`: contenido válido pero con terminología o contexto a modernizar según topic-extract.md
- `eliminar`: cubre conceptos marcados como "asumir-conocido" en superposiciones-detectadas
- `nueva`: filmina requerida por los conceptos-clave de topic-extract.md que no existe en el material previo

*Dado que* el análisis completó,  
*cuando* el agente construye el reporte,  
*entonces* el reporte indica el porcentaje de filminas en cada categoría y el total de filminas previas analizadas.

---

### Story 5.3: Implementar reporte de renovación y priorización en generación

**Como docente, quiero** ver el reporte de renovación como parte del Checkpoint 2 y que la generación posterior priorice conservar/adaptar filminas existentes sobre generar desde cero, **para poder** reutilizar el trabajo histórico y recibir un material final con continuidad respecto al año anterior.

**FRs cubiertos:** FR22, FR23  
**NFR cubiertos:** —

**Criterios de aceptación:**

*Dado que* el análisis comparativo completó,  
*cuando* el agente presenta el Checkpoint 2,  
*entonces* el plan de generación incluye el reporte de renovación con la tabla de categorización y el docente puede revisar ambos (plan + renovación) antes de aprobar.

*Dado que* el docente aprueba el Checkpoint 2 con filminas previas analizadas,  
*cuando* el Paso 3 genera las filminas,  
*entonces* las filminas categorizadas como `conservar` se incluyen sin regenerar (reúso directo), las `actualizar` se regeneran usando la filmina previa como base textual, y las `nueva` se generan desde topic-extract.md.

*Dado que* al menos el 40% de las filminas previas son categorizadas como `conservar`,  
*cuando* se completa la generación,  
*entonces* el resumen final del pipeline informa cuántas filminas fueron conservadas, actualizadas y generadas nuevas.

---

## Epic 6: Agentes downstream

**Objetivo:** Actualizar los 3 agentes downstream existentes (`class-writer`, `study-guide-writer`, `create-teacher-guide`) con lógica condicional v3: si `topic-extract.md` existe y el checkpoint 2 está aprobado, usar comportamiento v3; sino, comportamiento v2 exacto sin cambios.

**Artefactos producidos:**
- `_edu/agents/class-writer.md` — con nueva sección `<context-v3>` condicional
- `_edu/agents/study-guide-writer.md` — idem
- `_edu/agents/create-teacher-guide.md` — idem
- Mecanismo de backup automático de artefactos v2

**Criterio de completitud del epic:** Los 3 agentes detectan la presencia de `topic-extract.md` + `checkpoint_2_aprobado: true` y activan el comportamiento v3 de forma condicional. Sin esos archivos, el comportamiento v2 es exactamente el mismo de antes.

---

### Story 6.1: Agregar lógica condicional v3 a class-writer.md

**Como docente, quiero** que class-writer detecte automáticamente la presencia de `topic-extract.md` y `checkpoint_2_aprobado: true` para usar comportamiento v3 (filminas desde topic-extract), y que en ausencia de esos archivos funcione exactamente igual que siempre, **para poder** usar el mismo agente en flujos v2 y v3 sin intervención manual.

**FRs cubiertos:** FR20, FR24, FR26  
**NFR cubiertos:** NFR06

**Criterios de aceptación:**

*Dado que* `{topic_folder}/topic-extract.md` NO existe,  
*cuando* class-writer es invocado,  
*entonces* ejecuta el comportamiento v2 completo sin ninguna modificación — cero regresión.

*Dado que* `{topic_folder}/topic-extract.md` existe PERO `.pipeline-v3-state.yaml` tiene `checkpoint_2_aprobado: false` (o el archivo de estado no existe),  
*cuando* class-writer es invocado,  
*entonces* ejecuta el comportamiento v2 — la presencia de topic-extract.md sola no es suficiente para activar v3.

*Dado que* `topic-extract.md` existe Y `checkpoint_2_aprobado: true`,  
*cuando* class-writer es invocado en modo v3,  
*entonces* lee `topic-extract.md` como fuente primaria de conceptos, ejemplos y terminología; lee el nivel desde `.pipeline-v3-state.yaml`; y genera filminas con los modificadores de densidad correspondientes al nivel.

*Dado que* class-writer va a sobrescribir `filminas.md` existente (generado por v2),  
*cuando* class-writer detecta que el archivo ya existe,  
*entonces* crea backup `filminas-v2-backup-YYYYMMDD.md` (con fecha actual en el nombre) antes de escribir el nuevo `filminas.md`.

---

### Story 6.2: Agregar lógica condicional v3 a study-guide-writer.md

**Como docente, quiero** que study-guide-writer en comportamiento v3 genere la guía de estudio usando `topic-extract.md` como fuente bibliográfica primaria — con referencias libro/sección/página directamente del artefacto — sin re-invocar ChromaDB, **para poder** obtener una guía donde cada concepto sea trazable a la bibliografía verificada por el docente.

**FRs cubiertos:** FR18  
**NFR cubiertos:** NFR06, NFR07

**Criterios de aceptación:**

*Dado que* `topic-extract.md` NO existe,  
*cuando* study-guide-writer es invocado,  
*entonces* ejecuta el comportamiento v2 completo — cero regresión, usa PDFs locales y filminas como fuente.

*Dado que* `topic-extract.md` existe Y `checkpoint_2_aprobado: true`,  
*cuando* study-guide-writer genera la guía en modo v3,  
*entonces* NO invoca `chroma_query_documents` — usa exclusivamente `topic-extract.md` como fuente bibliográfica.

*Dado que* study-guide-writer genera en modo v3,  
*cuando* referencia un concepto en la guía,  
*entonces* la referencia usa el formato canónico `[Autor, Libro §Sección, p. N]` tomado directamente de la sección `fuentes` de `topic-extract.md`.

*Dado que* la guía de estudio fue generada en modo v3,  
*cuando* se compara su estructura con la guía generada en modo v2,  
*entonces* el formato del archivo de salida (`guia-estudio.md`) es idéntico — la diferencia es solo en la fuente de contenido y las referencias.

---

### Story 6.3: Agregar lógica condicional v3 a create-teacher-guide.md

**Como docente, quiero** que create-teacher-guide en comportamiento v3 incluya tres secciones adicionales derivadas de `topic-extract.md` — fundamentos bibliográficos, conceptos con densidad variable, y tendencias académicas — **para poder** tener una guía docente que facilite la preparación de clase con contexto bibliográfico explícito.

**FRs cubiertos:** FR19  
**NFR cubiertos:** NFR06

**Criterios de aceptación:**

*Dado que* `topic-extract.md` NO existe,  
*cuando* create-teacher-guide es invocado,  
*entonces* ejecuta el comportamiento v2 completo sin ninguna modificación — cero regresión.

*Dado que* `topic-extract.md` existe Y `checkpoint_2_aprobado: true`,  
*cuando* create-teacher-guide genera la guía docente en modo v3,  
*entonces* el output incluye una sección "Fundamentos bibliográficos" con la lista de fuentes de `topic-extract.md § fuentes` con libro, sección y página.

*Dado que* create-teacher-guide genera en modo v3,  
*cuando* incluye la sección de conceptos,  
*entonces* agrega una subsección "Conceptos con profundidad variable" que describe brevemente cómo cambiaría la presentación de cada concepto clave en Nivel 1, 2 y 3.

*Dado que* `topic-extract.md` tiene ítems en la sección `tendencias`,  
*cuando* create-teacher-guide genera en modo v3,  
*entonces* incluye una sección "Tendencias académicas recientes" con los ítems de tendencias y sus notas de posible desactualización bibliográfica.

---

### Story 6.4: Implementar mecanismo de backup de artefactos v2 en todos los agentes downstream

**Como docente, quiero** que cualquier artefacto v2 existente sea respaldado automáticamente con sufijo `-v2-backup-YYYYMMDD` antes de ser sobrescrito por una generación v3, **para poder** recuperar el material anterior si necesito comparar o revertir.

**FRs cubiertos:** FR26  
**NFR cubiertos:** NFR06

**Criterios de aceptación:**

*Dado que* `filminas.md` existe en `{topic_folder}/` antes de la generación v3,  
*cuando* class-writer genera en modo v3,  
*entonces* crea `filminas-v2-backup-YYYYMMDD.md` (con fecha en formato YYYYMMDD) antes de escribir el nuevo `filminas.md`.

*Dado que* `guia-estudio.md` existe antes de la generación v3,  
*cuando* study-guide-writer genera en modo v3,  
*entonces* crea `guia-estudio-v2-backup-YYYYMMDD.md` antes de escribir el nuevo archivo.

*Dado que* `guiaprofesor.md` existe antes de la generación v3,  
*cuando* create-teacher-guide genera en modo v3,  
*entonces* crea `guiaprofesor-v2-backup-YYYYMMDD.md` antes de escribir el nuevo archivo.

*Dado que* ya existe un backup previo con la misma fecha (doble ejecución en el mismo día),  
*cuando* el agente intenta crear el backup,  
*entonces* agrega sufijo `-2`, `-3`, etc. para evitar sobreescribir el backup anterior (ej. `filminas-v2-backup-20260523-2.md`).

*Dado que* `filminas.md` NO existe antes de la generación v3 (tema nuevo sin run v2 previo),  
*cuando* class-writer genera en modo v3,  
*entonces* escribe `filminas.md` directamente sin crear backup — no hay nada que respaldar.

---

## Mapa de Cobertura FR

| FR | Story(ies) que lo cubren |
|---|---|
| FR01 — Invocación con tópico/libro/nivel | 1.1, 4.1 |
| FR02 — Libro default de config.yaml | 1.1, 2.2 |
| FR03 — Informar libro y nivel al inicio | 1.1 |
| FR04 — Parámetro --base filminas previas | 5.1 |
| FR05 — Consultar registro temas dados | 3.1 |
| FR06 — Reportar superposiciones + esperar confirmación | 3.2 |
| FR07 — Capturar estrategia de tratamiento | 3.3 |
| FR08 — ChromaDB obligatorio, fail-fast | 2.2 |
| FR09 — Libros secundarios | 2.3 |
| FR10 — Web research tendencias | 2.4 |
| FR11 — Marcar libros > 5 años conflictivos | 2.4 |
| FR12 — topic-extract.md con secciones obligatorias | 2.1, 2.5 |
| FR13 — Persistir y esperar aprobación CP1 | 1.4, 2.5 |
| FR14 — Docente puede editar topic-extract.md | 1.4 |
| FR15 — Plan de generación con CP2 | 1.5 |
| FR16 — Docente puede editar plan (CP2) | 1.5 |
| FR17 — 3 niveles de densidad en filminas | 4.2 |
| FR18 — Guía de estudio sin re-invocar ChromaDB | 6.2, 4.3 |
| FR19 — Guía docente con topic-extract.md | 6.3 |
| FR20 — Compatibilidad slides_pipeline.py | 4.2, 6.1 |
| FR21 — Comparar filminas previas vs topic-extract.md | 5.2 |
| FR22 — Reporte análisis renovación al docente | 5.3 |
| FR23 — Priorizar reúso sobre generación nueva | 5.3 |
| FR24 — topic-cycle original sin cambios | 1.1, 6.1, 6.2, 6.3 |
| FR25 — topic-cycle-v3 activable por flag o invocación | 1.1 |
| FR26 — Artefactos v3 conviven sin conflictos con v2 | 1.3, 6.4 |

## Mapa de Cobertura NFR

| NFR | Story(ies) que lo cubren |
|---|---|
| NFR01 — Estado persisitido por paso; reanudación | 1.3 |
| NFR02 — Fail-fast con diagnóstico si chroma-mcp falla | 2.2 |
| NFR03 — Checkpoints persisitidos ante interrupción | 1.4, 1.5 |
| NFR04 — Citas con referencia verificable o "referencia incompleta" | 2.5 |
| NFR05 — Bloquear plan sin fuente verificada en topic-extract | 2.5 |
| NFR06 — Mismo formato de salida que v2 | 4.2, 6.1, 6.2, 6.3, 6.4 |
| NFR07 — Sin dependencias nuevas | 2.2, 2.3, 2.4 |
| NFR08 — Tiempo ≤ 150% de v2 | 4.1, 4.2, 4.3 |
| NFR09 — Schema documentado formalmente | 2.1 |
| NFR10 — Workflow independiente; no modifica topic-cycle | 1.1, 1.2 |

---

## Validación Final

### Cobertura FR: 26/26 ✅

Todos los requisitos funcionales están cubiertos por al menos una story. Los FRs más complejos (FR12, FR13) tienen cobertura distribuida entre stories de Epic 1 y Epic 2.

### Cobertura NFR: 10/10 ✅

Todos los requisitos no funcionales están cubiertos. NFR08 (performance ≤ 150%) es medible post-implementación; la arquitectura lo garantiza estructuralmente porque los checkpoints son tiempo del docente, no del sistema.

### Principio brownfield respetado ✅

- Cada story de Epic 6 incluye AC explícita de cero regresión: comportamiento v2 exacto cuando `topic-extract.md` no existe
- Story 1.1 y 1.2 incluyen AC de que los archivos v2 existentes permanecen sin modificaciones
- Story 6.4 garantiza backup antes de cualquier sobrescritura

### Orden de implementación sugerido

```
E1 (base pipeline) → E2 (bibliographic-first) → E3 (coherencia) 
  → E4 (densidad) → E6 (downstream) → E5 (renovación)
```

E1 y E2 son bloqueantes para todos los demás. E3, E4 y E6 pueden desarrollarse en paralelo una vez E1+E2 están completos. E5 depende de E2 (topic-extract.md aprobado) y puede hacerse al final.

### Decisiones de diseño tomadas autónomamente

1. **Story 6.4 separada del resto de E6:** El mecanismo de backup podría haberse incorporado en 6.1/6.2/6.3, pero se separó para poder verificarlo independientemente y porque cubre el FR26 de coexistencia de artefactos v2/v3 como concern transversal.

2. **Story 2.2 incluye validación de colección vacía:** El PRD habla de fail-fast si chroma-mcp no responde, pero la arquitectura §9.3 especifica también el caso de colección vacía. Se incorporó en la misma story por cohesión.

3. **Story 3.1 tiene comportamiento silencioso cuando no hay temas previos:** El PRD no especifica este caso borde, pero es necesario para el primer tema de una cursada. Se decidió continuar sin checkpoint adicional para no obstruir el flujo normal de inicio de cursada.

4. **Story 1.5 incluye edición del plan en Checkpoint 2:** El FR15 habla de "esperar aprobación" y el FR16 habla de "reordenar, agregar o eliminar". Se unificaron en una sola story porque el checkpoint es el contexto donde ocurre la edición — separarlos habría creado una story vacía de "solo esperar input".

---

*Epics y stories generadas con el workflow `bmad-create-epics-and-stories` (fast mode autónomo). Fecha: 2026-05-23.*  
*Próximo paso recomendado: crear stories individuales con `bmad-create-story` comenzando por Story 1.1, o ejecutar sprint planning con `bmad-sprint-planning`.*
