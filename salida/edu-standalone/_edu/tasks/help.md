
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

Todo comando se muestra con prefijo `/edu_` (ej: `/edu_design_topic`).

Formato por ítem:
```
**Nombre (CODE)**
`/edu_comando`
Agente: 🎓 Nombre del agente
Descripción breve.
```

## CONJUNTO DE COMANDOS ACTIVOS (27)

Comentará solo los comandos relevantes al estado detectado.
Nunca mostrar todos los 27 a la vez — presentar los 3-5 más relevantes según el contexto.

### Anytime
- `edu_help`, `edu_status`, `edu_check_coverage`, `edu_manage_profiles`, `edu_update_context`

### Phase 1
- `edu_start_course` — Fase 1 completa (configura + carga plan + congela)

### Phase 2
- `edu_build_course_from_materials`, `edu_research_plan`, `edu_propose_curriculum_change`

### Phase 3 — ciclo de tema
- `edu_topic` — punto de entrada recomendado (detecta estado y guía)
- `edu_design_topic` — diseñar o ajustar (antes de aprobar)
- `edu_approve_design` — aprobar diseño
- `edu_create_class` — crear minuta + filminas
- `edu_create_tp` — crear TP
- `edu_quality_validate` — validar calidad (todos los loops)
- `edu_quality_fix` — corregir calidad (todos los fixes)
- `edu_test_topic` — testing pedagógico
- `edu_debate_topic` — panel multi-agente
- `edu_compare_survey_simulator` — calibrar simulador
- `edu_close_topic` — cerrar tema
- `edu_reopen_topic` — reabrir tema
- `edu_adaptive_replan` — replanificar

### Phase 3 — slides (opcional)
- `edu_setup_apis` — configurar APIs (una vez)
- `edu_slides_designer` — diseño visual (una vez por cursada)
- `edu_publish_slides` — publicar filminas en Google Slides
- `edu_slides_publisher` — re-exportar sin rediseñar

### Phase 4
- `edu_close_course`, `edu_start_new_year`

## DETECCIÓN DEL ESTADO

1. **Cargar catálogo** — Leer `{project-root}/_edu/module-help.csv`
2. **Resolver rutas** — Leer `{project-root}/_edu/config.yaml` para obtener `{course_output_folder}`, `{memory_folder}`, `{user_name}`, `{communication_language}`
3. **Detectar fase activa** — Buscar artefactos clave:
   - `plan-minimo.md` existe → phase-1 completada
   - `plan-borrador.md` existe → phase-2 en curso o completada
   - `temas/*/diseno.md` existe → phase-3 en curso
   - `retrospectiva.md` existe → phase-4 en curso o completada
4. **Detectar tema activo** — si hay `temas/NN-*/` sin `git-merge`, ese es el tema en producción
5. **Si no hay artefactos** → sugerir comenzar por `/edu_start_course`

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
4. **Presentar recomendaciones** — máximo 5 comandos, ordenados por relevancia:
   - Si hay tema activo: `edu_topic` como primera recomendación
   - Si no hay tema: siguiente paso del flujo general
   - Incluir siempre `edu_help` y `edu_status` si el docente parece desorientado
5. **Formato de respuesta:**
   ```
   📍 Estado actual: [fase] — [descripción]
   
   ⭐ Próximo paso recomendado:
   /edu_COMANDO — descripción
   
   Otros comandos disponibles:
   /edu_X — descripción
   /edu_Y — descripción
   ```

1. **Cargar catálogo** — Leer `{project-root}/_edu/module-help.csv`
2. **Resolver rutas** — Leer `{project-root}/_edu/config.yaml` para obtener `{course_output_folder}`, `{memory_folder}`, `{user_name}`, `{communication_language}`
3. **Detectar fase activa** — Buscar artefactos clave:
   - `plan-minimo.md` existe → phase-1 completada
   - `plan-borrador.md` existe → phase-2 en curso o completada
   - `temas/*/diseno.md` existe → phase-3 en curso
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
