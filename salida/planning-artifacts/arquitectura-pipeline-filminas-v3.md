# Arquitectura Pipeline EDU Filminas v3
## Desacoplamiento Máximo: Schemas Inmutables + Scripts Inmutables + Configs JSON Deterministas

**Proyecto:** Paradigmas y Lenguajes de Programación 2026  
**Arquitecto:** Winston (BMAD Architect)  
**Fecha:** 25 de marzo de 2026  
**Estado:** IMPLEMENTADO  
**Base:** Análisis del informe técnico (`informe/info_filminas.md`) + arquitectura v2 + evidencia de temas 00 y 01

---

## 1. Diagnóstico — Problemas Residuales de v2

La arquitectura v2 resolvió los bugs críticos (inferencia de tipos, prompts con vocabulario técnico, budget hardcodeado) pero dejó **divergencias estructurales** que impiden determinismo total:

| Problema | Evidencia | Impacto |
|---|---|---|
| **Divergencia contrato/runtime** | `slides-plan-schema.yaml` dice UN archivo, pero el agente genera 3 (`plan-filminas`, `assets-manifest`, `publish-context`) | El validador verifica un contrato; el runtime usa otro. |
| **Schema descriptivo, no ejecutable** | Los `.yaml` de schema son documentación, no JSON Schema validable programáticamente | No hay validación automática contra schema. |
| **Duplicación de verdad** | `LAYOUT_MAP` y `IMAGE_STRATEGY` existen como dicts Python Y en `slides-config.yaml` Y en `slides-pipeline.json` | Drift inevitable entre fuentes. |
| **Plan YAML con estructura dual** | Plan actual usa `background_image` + `content_image` separados, schema dice `image` unificado | Agentes no saben cuál formato usar. |
| **Formato YAML no versionado** | Plan no declara `$schema_version`, imposible saber contra qué contrato fue generado | No hay trazabilidad de versión. |
| **Agentes con libertad residual** | Diego puede armar layouts creativos que divergen de la tabla canónica | Resultado no determinista. |

---

## 2. Principios de Arquitectura v3

### P1 — Schema Registry como Única Fuente de Verdad
Un solo archivo (`_edu/schemas/schema-registry.json`) declara TODOS los schemas, versiones, rutas, enums canónicos, y el mapeo determinista tipo→layout. Los scripts leen de ahí. Los agentes leen de ahí. No hay otra fuente.

### P2 — JSON Schema Ejecutable
Los schemas son JSON Schema Draft 2020-12 reales, validables con `jsonschema` en Python. No son documentación descriptiva. El validador carga el schema y valida el plan programáticamente.

### P3 — Determinismo Total: type → layout → image_layer
El mapeo `type_layout_map` en el schema registry define de forma INMUTABLE qué layout y qué `image_layer` corresponde a cada tipo. El agente NO elige layouts — los COPIA del mapeo según el tipo asignado. El JSON Schema valida esto con constraints `if/then/const`.

### P4 — Plan en JSON, No YAML
El plan pasa a ser `plan-filminas-{tema}.json`. JSON es más estricto que YAML (sin ambigüedad de tipos, sin aliases, sin !!tags), validable con JSON Schema nativo, y parseable sin librerías extras.

### P5 — Eliminación de Artefactos Redundantes
Se elimina `assets-manifest.yaml` y `publish-context.yaml`. Toda la información está en `plan-filminas-{tema}.json`. El campo `meta` contiene lo que era `publish-context`. Los campos `table_assets` y `image` contienen lo que era `assets-manifest`.

### P6 — Scripts Sin Constantes Propias
Los scripts no definen `LAYOUT_MAP`, `IMAGE_STRATEGY`, ni ninguna constante de diseño. Todo se lee del schema registry y del design system config al inicio de la ejecución.

### P7 — Trazabilidad por Diseño
Cada plan JSON declara `$schema_version`, y en `meta` las rutas exactas al design system, pipeline runtime y schema registry que se usaron para generarlo. Esto permite regeneración exacta.

---

## 3. Arquitectura de Datos — Tres Capas

```
┌─────────────────────────────────────────────────────────────┐
│  CAPA 1 — SCHEMAS INMUTABLES (JSON Schema)                 │
│                                                             │
│  _edu/schemas/schema-registry.json      ← Manifiesto       │
│  _edu/schemas/filmina-slide.schema.json ← Por slide        │
│  _edu/schemas/plan-filminas.schema.json ← Plan completo    │
│  _edu/schemas/design-system.schema.json ← Sistema diseño   │
│  _edu/schemas/pipeline-runtime.schema.json ← Geometría     │
│                                                             │
│  REGLA: Solo cambian con bump de versión planificado.       │
│  Contienen constraints if/then que validan determinismo     │
│  tipo→layout→image_layer.                                   │
└─────────────────────────────┬───────────────────────────────┘
                              │ leen
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  CAPA 2 — SCRIPTS INMUTABLES (Python)                      │
│                                                             │
│  scripts/parse_filminas.py     ← filminas.md → DRAFT JSON  │
│  scripts/validate_plan.py     ← Valida plan vs JSON Schema │
│  scripts/repair_plan.py       ← Loop validación+corrección │
│  scripts/slides_pipeline.py   ← Genera assets + publica    │
│  scripts/capture_thumbnails.py ← QA visual                 │
│                                                             │
│  REGLA: Sin constantes de diseño. Sin inferencia.           │
│  Solo leen configs + ejecutan APIs.                         │
└─────────────────────────────┬───────────────────────────────┘
                              │ generan
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  CAPA 3 — CONFIGS GENERADOS POR AGENTES (JSON)             │
│                                                             │
│  {tema}/slides/plan-filminas-{tema}.json  ← Plan completo  │
│  {tema}/slides/plan-draft-{tema}.json     ← DRAFT (parser) │
│  {tema}/slides/assets/F-XX-*.png          ← Assets gen.    │
│  {tema}/slides/slides-url.txt             ← URL publicada  │
│                                                             │
│  _edu/slides-config.yaml  ← Design system (Vera, una vez)  │
│  _edu/slides-pipeline.json ← Pipeline runtime (arquitecto) │
│                                                             │
│  REGLA: Deben cumplir los schemas de Capa 1.                │
│  Son trazables y regenerables desde filminas.md + schemas.  │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Flow Completo v3

```
filminas.md (fuente del contenido — escrita por humano/agente)
    │
    ▼
[SCRIPT: parse_filminas.py]
    │  Lee filminas-schema del registry
    │  Parsea Markdown → JSON DRAFT
    │  Slides sin @tipo: quedan type: "pending"
    │  Genera: plan-draft-{tema}.json
    │
    ▼
[AGENTE: slides-publisher (Diego)]
    │  1. Lee schema-registry.json PRIMERO
    │  2. Lee type_layout_map del registry
    │  3. Para cada slide DRAFT:
    │     a. Asigna type explícito del enum canónico
    │     b. COPIA layout de type_layout_map[type] — sin inventar
    │     c. COPIA image.layer de type_layout_map[type].image_layer
    │     d. Si image.layer != "none": escribe prompt visual puro
    │  4. Calcula summary (conteos, distribución)
    │  5. Genera: plan-filminas-{tema}.json
    │
    ▼
[SCRIPT: validate_plan.py]
    │  Carga plan-filminas.schema.json
    │  Carga filmina-slide.schema.json
    │  Valida con jsonschema (programático)
    │  Validaciones cruzadas adicionales:
    │  - type↔layout coherencia (ya en schema con if/then)
    │  - image.layer↔prompt no vacío
    │  - summary.images_planned ≤ 12
    │  - summary.total_slides == len(slides)
    │  - IDs secuenciales sin saltos
    │
    ├─ PASA → continúa
    └─ FALLA → errores estructurados por slide y campo
         │
         ▼
    [SCRIPT: repair_plan.py]
         │  Máx 3 reintentos
         │  Devuelve errores al agente
         │  Agente corrige SOLO campos reportados
         │
         └─ Si supera max → STOP, revisión humana
    │
    ▼
[SCRIPT: slides_pipeline.py] (INMUTABLE — solo ejecuta)
    │  Lee plan-filminas-{tema}.json
    │  Lee design system config
    │  Lee pipeline runtime config
    │  Fase 1: genera imágenes con Gemini
    │  Fase 2: renderiza tablas como PNG
    │  Fase 3: sube assets a Drive
    │  Fase 4: crea presentación en Google Slides
    │  Actualiza plan JSON con drive_ids
    │
    ▼
[SCRIPT: capture_thumbnails.py]
    │  Descarga thumbnails por API
    │  El docente inspecciona visualmente
    │
    ▼
Presentación publicada y verificada
```

---

## 5. Cambios Concretos vs v2

### 5.1 Nuevo: Schema Registry (`_edu/schemas/schema-registry.json`)
- Manifiesto central con versiones, rutas, enums canónicos
- `type_layout_map` como la ÚNICA tabla tipo→layout→image_layer
- Reglas de prompts de imagen
- Convenciones de archivos (formato JSON, nombres, rutas)

### 5.2 Nuevo: JSON Schemas ejecutables
- `filmina-slide.schema.json` — constraints `if/then/const` que hacen IMPOSIBLE que un agente asigne un layout incorrecto para un tipo dado
- `plan-filminas.schema.json` — estructura completa con `$schema_version`, `summary`, `$ref` a slide schema
- `design-system.schema.json` — valida `slides-config.yaml` programáticamente
- `pipeline-runtime.schema.json` — valida `slides-pipeline.json`

### 5.3 Consolidación de artefactos
| v2 (3 archivos) | v3 (1 archivo) |
|---|---|
| `plan-filminas-{tema}.yaml` | `plan-filminas-{tema}.json` |
| `assets-manifest.yaml` | → integrado en `slides[].image` y `slides[].table_assets` |
| `publish-context.yaml` | → integrado en `meta` |

### 5.4 Unificación de formato de imagen
| v2 (dual) | v3 (unificado) |
|---|---|
| `background_image.strategy` | `image.layer` |
| `background_image.prompt` | `image.prompt` |
| `content_image.strategy` | (eliminado — ya lo dice `image.layer`) |
| `content_image.prompt` | (eliminado — solo `image.prompt`) |

### 5.5 Script sin constantes propias
El `slides_pipeline.py` actual define `LAYOUT_MAP` y `IMAGE_STRATEGY` como dicts Python. En v3:
- Se leen de `schema-registry.json` → `type_layout_map` al inicio
- El script no tiene ninguna constante de diseño hardcodeada
- Los cambios de layout se hacen en EL SCHEMA, no en el script

### 5.6 Validación programática
El `validate_plan.py` actual valida con lógica Python ad hoc. En v3:
- Paso 1: `jsonschema.validate(plan, plan_schema)` — valida estructura + determinismo
- Paso 2: validaciones semánticas cruzadas adicionales en Python (conteos, secuencia de IDs)

---

## 6. Contrato de Responsabilidades

| Componente | Responsabilidad | NO hace |
|---|---|---|
| **Schema Registry** | Define enums, mapeos, reglas | No ejecuta nada |
| **JSON Schemas** | Validan estructura y determinismo | No corrigen errores |
| **parse_filminas.py** | Parsea Markdown → DRAFT JSON | No asigna tipos ni prompts |
| **validate_plan.py** | Valida plan contra schemas | No corrige el plan |
| **repair_plan.py** | Orquesta loop validación→corrección | No edita el plan directamente |
| **slides_pipeline.py** | Genera assets + publica | No infiere tipos/layouts/prompts |
| **capture_thumbnails.py** | QA visual | No modifica la presentación |
| **Vera (slides-designer)** | Genera design system config | No genera planes por tema |
| **Diego (slides-publisher)** | Genera plan JSON por tema | No modifica scripts ni schemas |

---

## 7. Ejemplo de Plan JSON v3 (fragmento)

```json
{
  "$schema_version": "plan-filminas/v3",
  "meta": {
    "topic_id": "01-diseno-agil-python",
    "title": "Módulo I — Diseño Ágil + Python",
    "source": "filminas.md",
    "generated_at": "2026-03-25T17:37:27Z",
    "template_id": "1mGncfOizGbRHXNo5xqi9wfqePnlnGKbZUtlvTysYMsI",
    "topics_folder": "salida/cursadas/2026/temas",
    "topic_folder": "salida/cursadas/2026/temas/01-diseno-agil-python",
    "design_system_path": "_edu/slides-config.yaml",
    "pipeline_runtime_path": "_edu/slides-pipeline.json",
    "schema_registry_path": "_edu/schemas/schema-registry.json"
  },
  "summary": {
    "total_slides": 85,
    "images_planned": 12,
    "tables_planned": 15,
    "code_slides": 20,
    "status": "READY_FOR_VALIDATION",
    "pending_types": 0,
    "pending_prompts": 0,
    "type_distribution": {
      "portada": 1,
      "concepto-abstracto": 25,
      "concepto-mixto": 8,
      "codigo": 20,
      "tabla": 10,
      "tabla-comparativa": 5,
      "tabla-mixta": 2,
      "diagrama": 5,
      "socratica": 4,
      "demo": 3,
      "cierre": 1,
      "timeline": 1
    }
  },
  "slides": [
    {
      "id": "F-00",
      "type": "portada",
      "title": "Portada Módulo I",
      "subtitle": "Módulo I — Diseño Ágil + Python",
      "body_blocks": [
        {"type": "text", "content": "Laboratorio de Programación y Lenguajes 2026"}
      ],
      "code_blocks": [],
      "tables": [],
      "layout": {
        "title": "full-title",
        "body": "center-bottom",
        "image": "background",
        "code": "none",
        "table": "none"
      },
      "image": {
        "layer": "background",
        "prompt": "Large bold horizontal plain rectangle bordo #8B0000 at center. Below it, a thin dark gray horizontal line. Four small identical flat icons arranged in a row near the bottom: small gear circle, small branching tree, small document icon with folded corner, small checkmark badge. White background. Flat minimal design. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.",
        "local_asset": "",
        "drive_id": null
      },
      "table_assets": []
    },
    {
      "id": "F-01",
      "type": "codigo",
      "title": "Hola Mundo en Python",
      "subtitle": "Primer programa",
      "body_blocks": [
        {"type": "text", "content": "El clásico punto de partida"}
      ],
      "code_blocks": [
        {"lang": "python", "content": "print('Hola Mundo')"}
      ],
      "tables": [],
      "layout": {
        "title": "full-title",
        "body": "subtitle-only",
        "image": "none",
        "code": "full-bottom",
        "table": "none"
      },
      "image": {
        "layer": "none",
        "prompt": "",
        "local_asset": "",
        "drive_id": null
      },
      "table_assets": []
    }
  ]
}
```

---

## 8. Plan de Migración

### Fase 1: Schemas (COMPLETADO en esta sesión)
- [x] `_edu/schemas/schema-registry.json`
- [x] `_edu/schemas/filmina-slide.schema.json`
- [x] `_edu/schemas/plan-filminas.schema.json`
- [x] `_edu/schemas/design-system.schema.json`
- [x] `_edu/schemas/pipeline-runtime.schema.json`

### Fase 2: Actualización de Agentes
- [x] `slides-publisher.md` actualizado para leer schema-registry PRIMERO
- [x] `slides-designer.md` actualizado para referenciar design-system.schema.json
- [x] Prompts `.prompt.md` actualizados

### Fase 3: Actualización de Scripts (COMPLETADO)
- [x] `validate_plan.py` → carga JSON Schema y valida con `jsonschema` (v3) + legacy ad hoc (v2)
- [x] `parse_filminas.py` → genera DRAFT en JSON v3 con `image` unificado, lee del schema registry
- [x] `slides_pipeline.py` → lee `type_layout_map` del schema registry, elimina LAYOUT_MAP/IMAGE_STRATEGY hardcodeados (usa fallback), soporta planes JSON
- [x] `repair_plan.py` → soporta planes JSON y YAML, normalización dual
- [x] `slides_pipeline.py` → lee `image.layer`/`image.prompt` unificado con fallback a `background_image`/`content_image`

### Fase 4: Backward Compatibility (COMPLETADO)
- [x] Converter script `convert_plan_v2_to_v3.py` para planes existentes YAML→JSON
- [x] Detección automática de formato en todos los scripts (JSON priorizado sobre YAML)
- [x] Mensajes de deprecación para planes YAML v2

### Fase 5: Revisión Adversarial y Limpieza (COMPLETADO)
- [x] Revisión adversarial BMAD del código y artefactos v3
- [x] Fix: LAYOUT_MAP fallback `portada.title` sincronizado con schema-registry (`center-middle` → `full-title`)
- [x] Fix: Docstring de `slides_pipeline.py` actualizado para v3 (eliminada referencia a assets-manifest/publish-context)
- [x] Eliminados archivos muertos: `_edu/templates/filmina-slide-schema.yaml`, `_edu/templates/slides-plan-schema.yaml`
- [x] Conservado: `_edu/templates/filminas-schema.yaml` (reglas de parseo Markdown, no plan output)
- [x] Actualizado README.md con sección v3 schemas
- [x] Actualizado `edu-test-pipeline.prompt.md` (YAML → JSON)
- [x] Verificación de sintaxis Python de los 5 scripts: OK

---

## 9. Riesgos y Mitigaciones

| Riesgo | Mitigación |
|---|---|
| Scripts actuales rompen con formato JSON | Migración gradual con flag `--format json|yaml` |
| Agentes no leen el schema registry | Schema registry referenciado en copilot-instructions.md como OBLIGATORIO |
| JSON Schema no cubre todas las validaciones cruzadas | Capa 2 en Python para reglas semánticas (conteos, secuencia IDs) |
| Temas existentes en formato YAML | Converter script + backward compat transitoria |
| Plan muy grande para contexto de agente (85+ slides) | El agente puede generar por bloques pero el JSON final debe ser uno solo |

---

## 10. Comparativa v2 → v3

| Aspecto | v2 | v3 |
|---|---|---|
| Schema | YAML descriptivo | JSON Schema ejecutable |
| Validación | Python ad hoc | `jsonschema` programático + Python semántico |
| Plan | YAML, 3 archivos | JSON, 1 archivo |
| Imagen | `background_image` + `content_image` | `image` unificado |
| Determinismo tipo→layout | Documentado pero no enforced | Enforced con `if/then/const` en schema |
| Fuente de verdad de tipos | 3 lugares (Python + YAML + JSON) | 1 lugar (schema-registry.json) |
| Trazabilidad | Sin versión de schema en plan | `$schema_version` + rutas de configs en meta |
| Regenerabilidad | Parcial (faltan refs a configs) | Total (meta tiene todas las refs) |
