# Workflow: Auto-Topic — Producción Automática de Tema

## Objetivo
Producir todo el material de un tema con un solo comando, invocando agentes en secuencia con gates de calidad.

## Prerequisitos
- Plan mínimo aprobado
- Diseño del tema completado (o se genera en Paso 2)
- config.yaml con curso activo

## Pasos

### Paso 1 — Inicialización
1. Leer `topic.yaml` + `active-topic.yaml`
2. Consultar `memory.db` para errores previos del mismo tema
3. Crear `.pipeline-state.json` con `current_step: init`

### Paso 2 — Diseño (Agent: Marcos)
1. Invocar diseño del tema
2. Guardar checkpoint: `design-complete`

### Paso 3 — GATE: Aprobación del Diseño
1. **OBLIGATORIO**: El docente revisa y aprueba
2. Sin aprobación, el flujo se detiene aquí
3. Estado: `waiting-human`

### Paso 4 — Contenido (Agent: Roberto)
1. Generar `minuta.md` + `filminas.md`
2. Guardar checkpoint: `content-complete`

### Paso 5 — Quality Loop
1. coherencia-validator automático
2. guardrail académico
3. Si falla: pausar para corrección

### Paso 6 — Pipeline
1. `parse_filminas.py` → `validate_plan.py` → `slides_pipeline.py`
2. Guardar checkpoint: `slides-pipeline-complete`

### Paso 7 — TP (Agent: Valeria, si aplica)
1. Generar TP trazable a la minuta
2. Guardar checkpoint: `tp-complete`

### Paso 8 — Simulación (si S7.4 activo)
1. Simulación pedagógica con perfiles
2. Guardar checkpoint: `simulation-complete`

### Paso 9 — Resumen Final
1. Compilar métricas de calidad
2. Docente decide si publicar
3. Estado: `complete`

## Reanudación
`/edu-resume-topic` lee `.pipeline-state.json` y retoma desde el último paso exitoso.
