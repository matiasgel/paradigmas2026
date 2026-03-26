# Arquitectura: Memoria Colectiva + Multi-Clase

**Fecha:** 2026-03-25
**Autor:** architect (Winston)
**Status:** APROBADO — ready to implement

---

## Problema 1: Memoria Colectiva

### Situación actual

`_edu-memory/` es un directorio de archivos Markdown planos:
- `calibracion-simulador/` — datos del simulador de alumnos
- `notas-para-{año}.md` — handover notes del cierre de curso
- Sin indexación, sin búsqueda, sin trazabilidad de errores

Los agentes no tienen forma eficiente de:
- Consultar errores pasados (ej: "¿qué errores de coherencia se repitieron en temas anteriores?")
- Acceder a decisiones pedagógicas de años anteriores
- Detectar patrones cross-topic (ej: "en 3 temas distintos Sofía tuvo que marcar PENDIENTE los mismos PDFs")
- Reutilizar correcciones que un usuario ya hizo a outputs de agentes

### Decisión de diseño: SQLite FTS5 + JSON

**¿Por qué NO ChromaDB / LanceDB / vector DB externa?**
- Requieren dependencias pesadas (`sentence-transformers`, `torch`, `chromadb`)
- El volumen de datos de EDU es pequeño (decenas de documentos, no millones)
- Los agentes de Copilot ya tienen capacidad semántica nativa — no necesitan embeddings propios
- Agregar un servicio externo a mantener viola el principio de simplicidad de EDU

**¿Por qué NO MCP Memory Server (`@modelcontextprotocol/server-memory`)?**
- Requiere Node.js (no disponible en el entorno)
- Es key-value básico, no tiene búsqueda full-text ni categorías

**Solución elegida: SQLite con FTS5 (Full-Text Search)**
- **Zero dependencias** — Python 3.10+ trae `sqlite3` con FTS5 compilado
- **Búsqueda full-text** — consultas tipo `"coherencia error filminas"` sin embeddings
- **Categorías estructuradas** — columnas para tipo, clase, año, tema, agente
- **Cross-clase y cross-año** — queries filtradas por `course_id` y/o `course_year`
- **Un solo archivo** — `_edu-memory/memory.db` (en `.gitignore`, portable)

### Schema de la base

```sql
CREATE TABLE IF NOT EXISTS memory_entries (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id   TEXT NOT NULL,          -- "leng-2026", "para-2026"
    course_year TEXT NOT NULL,          -- "2026"
    topic_num   TEXT,                   -- "01", "02", NULL si es global
    category    TEXT NOT NULL,          -- enum: ver abajo
    agent       TEXT,                   -- "class-writer", "study-guide-writer", NULL
    summary     TEXT NOT NULL,          -- resumen corto (1-2 líneas)
    detail      TEXT,                   -- detalle largo, Markdown
    source_file TEXT,                   -- ruta al artefacto origen (relativa)
    created_at  TEXT DEFAULT (datetime('now')),
    resolved    INTEGER DEFAULT 0       -- 0=abierto, 1=resuelto
);

CREATE VIRTUAL TABLE IF NOT EXISTS memory_fts USING fts5(
    summary, detail, category, agent, course_id,
    content='memory_entries',
    content_rowid='id'
);

-- Triggers para mantener FTS sincronizado
CREATE TRIGGER IF NOT EXISTS memory_ai AFTER INSERT ON memory_entries BEGIN
    INSERT INTO memory_fts(rowid, summary, detail, category, agent, course_id)
    VALUES (new.id, new.summary, new.detail, new.category, new.agent, new.course_id);
END;

CREATE TRIGGER IF NOT EXISTS memory_ad AFTER DELETE ON memory_entries BEGIN
    INSERT INTO memory_fts(memory_fts, rowid, summary, detail, category, agent, course_id)
    VALUES ('delete', old.id, old.summary, old.detail, old.category, old.agent, old.course_id);
END;
```

### Categorías canónicas

| Categoría | Qué guarda | Ejemplo |
|---|---|---|
| `agent-error` | Error corregido por el usuario en output de un agente | "Roberto generó 45 filminas para clase de 90 min — se corrigió a 22" |
| `agent-correction` | Corrección factual aplicada al output | "El ejemplo de polimorfismo usaba herencia múltiple — el docente lo cambió a interfaces" |
| `quality-finding` | Hallazgo de los loops de calidad | "Loop 2 detectó incoherencia entre minuta F-05 y filmina F-05 en 3 temas" |
| `pedagogy-insight` | Decisión pedagógica del docente | "Evitar recursión en tema 01 — moverla a tema 04 por feedback de alumnos" |
| `student-feedback` | Feedback real de alumnos (encuestas, calibración) | "Alumnos de 2025 dijeron que el tema 03 era muy denso — reducir a 2 conceptos/filmina" |
| `cross-topic` | Coherencia inter-tópico | "Nomenclatura: siempre 'interfaz' (no 'interface') en todos los temas" |
| `retrospective` | Lecciones del cierre de cursado | "2025: el 80% de los temas necesitó 2+ ciclos de calidad por errores de coherencia" |
| `tool-issue` | Problema técnico del pipeline/scripts | "parse_filminas.py falla con tablas > 5 columnas — se resolvió en commit abc123" |

### API del script: `edu_memory.py`

```
# Agregar entrada
python scripts/edu_memory.py add --course leng-2026 --topic 01 --category agent-error \
  --agent class-writer --summary "Generó 45 filminas para 90 min" \
  --detail "Se corrigió a 22 filminas. Regla: máx 1 filmina por 4 min."

# Buscar (full-text)
python scripts/edu_memory.py search "coherencia filminas"

# Buscar filtrado
python scripts/edu_memory.py search "error" --course leng-2026 --category agent-error

# Listar por tema
python scripts/edu_memory.py list --course leng-2026 --topic 03

# Cross-año (todas las clases, todos los años)
python scripts/edu_memory.py search "recursión" --all

# Marcar como resuelto
python scripts/edu_memory.py resolve 42

# Exportar (para handover/retrospectiva)
python scripts/edu_memory.py export --course leng-2026 --format md
```

---

## Problema 2: Multi-Clase

### Situación actual

- `config.yaml` tiene `project_name: ""` (un solo valor)
- Los prompts no reciben argumentos — el tema se resuelve por `active-topic.yaml`
- No hay noción de `course_id` (materia+año como clave compuesta)
- Si un profesor da 2 materias (ej: "Lenguajes" y "Paradigmas"), necesita 2 workspaces completamente separados

### Decisión de diseño: `course_id` como clave compuesta

**Formato:** `{prefix}-{year}` (ej: `leng-2026`, `para-2026`)

**Dónde se define:**
- `_edu/config.yaml` → nuevo campo `course_id` (derivado de `course_prefix` + `course_year`)
- `_edu/config.yaml` → nuevo campo `course_prefix` (ej: `leng`, `para`)
- Los prompts reciben `course_id` como parámetro implícito (leído de config)

**Impacto en la estructura de carpetas:**
```
salida/cursadas/
  leng-2026/           ← antes era solo "2026"
    temas/
  para-2026/
    temas/
```

**`topics_folder`** se redefine:
```yaml
# Antes
course_output_folder: "{output_folder}/cursadas/{course_year}"

# Después
course_output_folder: "{output_folder}/cursadas/{course_id}"
```

### Prompts: argumentos implícitos (no explícitos)

Los prompts de Copilot no soportan argumentos posicionales tipo `/edu-create-class leng-2026 01-intro`. Lo que sí funciona:

1. El prompt lee `config.yaml` → obtiene `course_id` y `course_prefix`
2. El prompt lee `active-topic.yaml` → obtiene el tema activo
3. Si el usuario quiere cambiar de clase dentro del mismo workspace → edita `course_prefix` en `config.yaml` o usa `/edu-switch-course`

### Nuevo comando: `/edu-switch-course`

```
/edu-switch-course
```

Pregunta al docente qué materia activar, actualiza `config.yaml` con el nuevo `course_prefix` (manteniendo `course_year`), y recalcula todas las rutas derivadas.

---

## Integración: Memoria + Multi-Clase

La columna `course_id` en `memory_entries` es la clave. Cuando un agente consulta la memoria:

1. **Default:** filtra por `course_id` actual (ej: `leng-2026`)
2. **Cross-curso:** si se pide contexto de otra materia → busca por `course_id` distinto
3. **Cross-año:** `course_id = leng-2025` accede al año anterior de la misma materia
4. **Global:** `--all` busca sin filtro

### Flujo de escritura automática en la memoria

| Evento | Categoría | Quién escribe |
|---|---|---|
| /edu-quality detecta error | `quality-finding` | Loop de calidad (automático) |
| Usuario corrige output de agente | `agent-correction` | Agente que recibe la corrección |
| /edu-close-topic | `cross-topic` | Elena (hallazgos de coherencia) |
| /edu-close-course | `retrospective` | Elena (lecciones aprendidas) |
| /edu-compare-survey-simulator | `student-feedback` | Simulador (calibración) |
| Error en scripts | `tool-issue` | El script que falla |

### Flujo de lectura automática de la memoria

| Evento | Qué consulta |
|---|---|
| /edu-design-topic | Busca `pedagogy-insight` + `student-feedback` para el tema |
| /edu-create-class | Busca `agent-error` + `agent-correction` del class-writer |
| /edu-quality | Busca `quality-finding` para detectar errores recurrentes |
| /edu-start-new-year | Exporta toda la memoria del `course_id` anterior |

---

## Archivos a crear/modificar

### Crear
1. `scripts/edu_memory.py` — CLI + API Python para leer/escribir memoria
2. `.github/prompts/edu-switch-course.prompt.md` — switch de materia activa
3. `.github/prompts/edu-memory-search.prompt.md` — búsqueda en memoria colectiva

### Modificar
1. `_edu/config.yaml` — agregar `course_prefix`, `course_id`
2. `copilot-instructions.md` — documentar memoria y multi-clase
3. `topic-cycle/workflow.md` — lectura de memoria en Step 0
4. `close-course/workflow.md` — escritura de retrospectiva en memoria
5. `quality-loops/workflow.md` — escritura de findings en memoria
6. `new-year/workflow.md` — exportar memoria del año anterior
7. `README.md` — documentar memoria, multi-clase, nuevos comandos
