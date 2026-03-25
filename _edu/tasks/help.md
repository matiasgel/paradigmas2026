
---
name: edu-help
description: 'Analiza el estado del cursado y recomienda el próximo paso. Usar cuando el docente pregunta qué hacer a continuación.'
---

# Task: EDU Help

## REGLAS DE RUTEO

- **`anytime`** — Disponible en cualquier fase del cursado
- **Fases numeradas** — `phase-1` → `phase-2` → `phase-3` → `phase-4` en orden
- **`required=true`** — Bloquea el avance a la siguiente fase si no está completo
- **Los artefactos revelan completitud** — Buscar en `{course_output_folder}` archivos que matcheen la columna `outputs`
- **Flujo del módulo**: Configuración → Plan → Producción de temas (ciclo) → Cierre

## MAPEO DE VARIABLES

- `{course_output_folder}` = ruta de salida del cursado (nomenclatura nueva)
- `{memory_folder}` = ruta de memoria persistente (nomenclatura nueva)

## REGLAS DE DISPLAY

Todo comando se muestra con prefijo `/edu-` (ej: `/edu-design-topic`).

Formato por ítem:
```
**Nombre (CODE)**
`/edu-comando`
Agente: 🎓 Nombre del agente
Descripción breve.
```

## CONJUNTO DE COMANDOS ACTIVOS (28)

Comentar solo los comandos relevantes al estado detectado.
Nunca mostrar todos los 28 a la vez — presentar los 3-5 más relevantes según el contexto.

### Anytime
- `edu-help`, `edu-status`, `edu-check-coverage`, `edu-student-profiles`, `edu-update-context`, `edu-edit-class-template`

### Phase 1
- `edu-start-course` — Fase 1 completa (configura + carga plan + congela)

### Phase 2
- `edu-build-course`, `edu-propose-curriculum-change`

### Phase 3 — ciclo de tema
- `edu-topic` — punto de entrada recomendado (detecta estado y guía)
- `edu-design-topic` — diseñar o ajustar (antes de aprobar)
- `edu-approve-design` — aprobar diseño
- `edu-create-class` — crear minuta + filminas
- `edu-create-tp` — crear TP
- `edu-create-autograde-repo` — regenerar output de TP (autograde, quiz)
- `edu-quality` — validar y/o corregir calidad (todos los loops)
- `edu-test-topic` — testing pedagógico
- `edu-debate-topic` — panel multi-agente
- `edu-compare-survey-simulator` — calibrar simulador
- `edu-adaptive-replan` — replanificar cronograma
- `edu-close-topic` — cerrar tema
- `edu-reopen-topic` — reabrir tema

### Phase 3 — slides (opcional)
- `edu-setup-apis` — configurar APIs (una vez)
- `edu-slides-designer` — diseño visual (una vez por cursada)
- `edu-publish-slides` — único punto de entrada para publicar filminas en Google Slides

### Phase 4
- `edu-close-course`, `edu-start-new-year`

## DETECCIÓN DEL ESTADO

1. **Cargar catálogo** — Leer `{project-root}/_edu/module-help.csv`
2. **Resolver rutas** — Leer `{project-root}/_edu/config.yaml` para obtener `{course_output_folder}`, `{memory_folder}`, `{user_name}`, `{communication_language}`
3. **Detectar fase activa** — Buscar artefactos clave:
   - `plan-minimo.md` existe → phase-1 completada
   - `plan-borrador.md` existe → phase-2 en curso o completada
   - `{topics_folder}/*/diseno.md` existe → phase-3 en curso (donde `{topics_folder}` se obtiene de `_edu/config.yaml`)
   - `retrospectiva.md` existe → phase-4 en curso o completada
4. **Detectar tema activo** — si hay `temas/NN-*/` sin `git-merge`, ese es el tema en producción
5. **Si no hay artefactos** → sugerir comenzar por phase-1

## ANÁLISIS DEL INPUT

Determinar qué se acaba de completar:
- Frase explícita del docente ("terminé el diseño", "cerré el tema 3")
- Artefactos encontrados en disco
- Contexto de la conversación actual
- Si no está claro → preguntar: "¿Qué fue lo último que completaste?"

## EJECUCIÓN

1. **Cargar catálogo** `{project-root}/_edu/module-help.csv`
2. **Resolver config** `{project-root}/_edu/config.yaml`
3. **Detectar estado** usando los criterios anteriores
4. **Presentar recomendaciones** ordenadas por fase+secuencia:
   - Primero ítems opcionales hasta llegar a uno requerido
   - Luego el próximo requerido (marcado claramente)
   - Mostrar máximo 4–5 ítems relevantes (no volcar todo el catálogo)

5. **Formato de salida** (en `{communication_language}`):

```
## 📚 EDU Help — Estado del cursado

**Fase detectada:** [phase-X o anytime]
**Tema activo:** [NN-nombre o "ninguno"]

### ✅ Completado recientemente
[ítem si se detecta]

### 🔜 Próximo paso recomendado
**Nombre (CODE)**
`/edu-comando`
Agente: Nombre
Descripción.

### 📋 Opciones disponibles
[lista de hasta 3 ítems relevantes opcionales]

### ⛔ Bloqueado hasta completar
[si hay required pendiente que bloquea avance]
```

6. **Orientación adicional:**
   - Comunicar siempre en `{communication_language}`
   - Cada workflow en una **ventana de contexto nueva**
   - Para dudas sobre un tema específico: `/edu-status`
   - Para ver cobertura del plan: `/edu-check-coverage`
