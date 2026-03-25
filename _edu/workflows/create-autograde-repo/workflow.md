# Workflow: Create Autograde Repo

**Module:** edu
**Phase:** 3 — Producción de Temas
**Owner Agent:** classroom-designer (Rodrigo)
**Trigger:** `/edu-create-autograde-repo` or Step 5.5 of topic-cycle

---

## Overview

Genera la estructura completa de un **repo plantilla para GitHub Classroom** con autograding
configurado por consigna. Cada test tiene trazabilidad directa al `tp.md`.

El output es un directorio `{topic_folder}/autograde-repo/` listo para subir como template repo
a GitHub y configurar como assignment en GitHub Classroom.

> **Acciones modernas (2024+):** El workflow usa las acciones oficiales del org `classroom-resources`:
> - `classroom-resources/autograding-command-grader@v1` — test por exit code
> - `classroom-resources/autograding-python-grader@v1` — test con pytest
> - `classroom-resources/autograding-io-grader@v1` — test input/output
> - `classroom-resources/autograding-grading-reporter@v1` — reporte final
>
> La acción `education/autograding@v1` es **obsoleta** y no debe usarse.

---

## Preconditions

- `_edu/active-topic.yaml` debe existir.
- `{topic_folder}/tp.md` debe existir (con consignas definidas).
- Si alguna precondition falla → informar y STOP.

---

## Steps

### Step 0: Initialize

1. Load `{project-root}/_edu/config.yaml` → store all fields.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}`.
3. Load `{project-root}/{topic_folder}/tp.md` → extraer consignas, puntos y descripción de cada una.
4. Informar: "Generando repo autograde para Tema {topic_number}: {topic_name}."

---

### Step 1: Elicitar Configuración del Repo

Preguntar al docente (en orden, esperar respuesta antes de continuar):

1. **Lenguaje de programación**: Python / Java / C / C++ / JavaScript / otro (escribir cual)
2. **Framework de tests** (sugerir el estándar para el lenguaje elegido):
   - Python → pytest
   - Java → JUnit 5
   - C/C++ → criterion o make check
   - JavaScript → jest
   - otro → especificar
3. **Puntos totales del assignment** (sugerido: 100)
4. **Distribución de puntos**:
   - Automática (proporcional a dificultad indicada en tp.md, si existe)
   - Manual (el docente especifica puntos por consigna)
5. **Nombre del repo** (sugerido: `tp{topic_number}-{topic_name}-template`, slug en kebab-case)
6. **Tiempo máximo de ejecución por test en minutos** (sugerido: 10 minutos; máximo: 360 minutos = 6 horas)

Mostrar resumen de configuración y pedir confirmación antes de generar.

---

### Step 2: Generar Estructura del Repo

Crear el directorio `{topic_folder}/autograde-repo/` con la siguiente estructura:

```
{topic_folder}/
├── autograde-setup.md                ← guía de publicación (SOLO para el docente, NO sube a GitHub)
└── autograde-repo/                   ← este directorio es el repo template que sube a GitHub
    ├── .github/
    │   ├── classroom/
    │   │   └── autograding.json      ← config oficial de GitHub Classroom
    │   └── workflows/
    │       └── classroom.yml         ← GitHub Actions para autograding
    ├── src/
    │   └── (starter code según lenguaje) ← scaffolding mínimo, SIN solución
    ├── tests/
    │   └── (un archivo de test por consigna)
    └── README.md                     ← instrucciones para el alumno
```

> ⚠️ `autograde-setup.md` se genera en `{topic_folder}/` (fuera de `autograde-repo/`) para que nunca sea subido al template repo ni sea visible para los alumnos.

**Reglas de generación:**

- `src/`: Solo scaffolding mínimo. Firmas de funciones/clases vacías o con `pass`/`throw new NotImplementedException()`.
  - Python: `src/__init__.py`, `src/solucion.py` (o nombre derivado del tema)
  - Java: `src/main/java/tp/Solucion.java`
  - C: `src/solucion.c`, `src/solucion.h`
- `tests/`: Un archivo por consigna (`test_ej1.py`, `test_ej2.py`, etc.).
  - Cada archivo tiene al menos 2 casos de test: caso borde + caso normal.
  - Los tests son funcionales pero NO revelan la solución completa.
- `README.md`: En español. Secciones: Objetivo / Consignas / Cómo ejecutar los tests localmente / Cómo entregar.
- `classroom.yml`: Usa las acciones modernas de `classroom-resources/*@v1` — un step por consigna + reporter final.
- `autograding.json` (referencia): Solo se genera como hoja de ruta para configurar los presets en la UI de GitHub Classroom si el docente prefiere ese flujo. El `classroom.yml` es la fuente de verdad para el repo template.

---

### Step 3: Generar `autograding.json` (referencia para UI de GitHub Classroom)

Este archivo describe los tests en el formato que GitHub Classroom espera cuando se configuran
los tests vía la **UI de Classroom** (presets). Es opcional si se usa el `classroom.yml` custom.
Útil como referencia para el docente y como documentación de la trazabilidad.

Formato oficial GitHub Classroom (timeout en **minutos**):

```json
{
  "tests": [
    {
      "name": "Ejercicio N — <descripción breve>",
      "setup": "<comando de instalación de dependencias si aplica>",
      "run": "<comando que ejecuta los tests de ese ejercicio>",
      "input": "",
      "output": "",
      "comparison": "included",
      "timeout": <timeout_minutos>,
      "points": <puntos_consigna>
    }
  ]
}
```

Valores válidos para `comparison`: `included` (output aparece en algún lugar), `exact` (idéntico), `regex` (expresión regular).

**Trazabilidad obligatoria:** El campo `"name"` de cada test DEBE incluir el número de consigna
tal como aparece en `tp.md`. Documentar la trazabilidad en `autograde-setup.md`.

---

### Step 4: Generar `classroom.yml`

Estructura moderna (2024+): **un step por consigna** usando las acciones de `classroom-resources`,
más un step final de `autograding-grading-reporter` que sincroniza los resultados con GitHub Classroom.

```yaml
name: Autograding Tests

on:
  - push
  - workflow_dispatch

permissions:
  actions: read
  contents: read

jobs:
  autograding:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      # ── Un step por consigna ───────────────────────────────────────────────
      # PYTHON: usa autograding-python-grader (corre pytest automáticamente)
      - name: Ejercicio 1 — <descripción>
        id: ej1
        uses: classroom-resources/autograding-python-grader@v1
        with:
          max-score: <puntos_ej1>
          setup-command: 'pip install -r requirements.txt'
          test-path: 'tests/test_ej1.py'  # archivo específico del ejercicio — evita correr todos los tests
          timeout: '10'          # minutos (máx 360)

      # COMMAND: usa autograding-command-grader (evalúa exit code)
      - name: Ejercicio 2 — <descripción>
        id: ej2
        uses: classroom-resources/autograding-command-grader@v1
        with:
          test-name: 'Ejercicio 2'
          setup-command: '<setup si aplica>'
          command: '<comando de test>'
          timeout: '10'          # minutos (máx 360)
          max-score: <puntos_ej2>

      # IO: usa autograding-io-grader (stdin/stdout comparison)
      # - name: Ejercicio 3 — <descripción>
      #   id: ej3
      #   uses: classroom-resources/autograding-io-grader@v1
      #   with:
      #     test-name: 'Ejercicio 3'
      #     command: '<comando ejecutable>'
      #     input: '<stdin>'
      #     expected-output: '<stdout esperado>'
      #     comparison-method: 'included'  # included | exact | regex
      #     timeout: '10'
      #     max-score: <puntos_ej3>

      # ── Reporter (siempre al final) ────────────────────────────────────────
      - name: Autograding Reporter
        uses: classroom-resources/autograding-grading-reporter@v1
        env:
          EJ1_RESULTS: "${{steps.ej1.outputs.result}}"
          EJ2_RESULTS: "${{steps.ej2.outputs.result}}"
          # EJ3_RESULTS: "${{steps.ej3.outputs.result}}"
        with:
          runners: ej1,ej2  # lista separada por coma, must match los step ids
```

**Reglas de generación del `classroom.yml`:**
- Adaptar el tipo de grader según el lenguaje y tipo de test de cada consigna
- El `id` de cada step determina el nombre de la env var en el reporter (`{ID_UPPERCASE}_RESULTS`)
- El `runners:` del reporter debe listar todos los ids en el mismo orden
- Timeout siempre en **minutos** — default 10, máximo 360 (6 horas)
- NO usar `education/autograding@v1` — es obsoleto
- Adaptar `setup-command` al lenguaje: Python→`pip install`, Java→`mvn install`, Node→`npm install`, C→`make`

---

### Step 5: Generar `README.md` del Repo (para alumnos)

Contenido:

```markdown
# TP {topic_number}: {topic_name}

## Objetivo
<resumen del tp.md — en lenguaje accesible para el alumno>

## Consignas
<listado de consignas del tp.md, enumeradas>

## Setup local
<instrucciones para instalar dependencias y ejecutar tests en la computadora del alumno>

## Cómo ejecutar los tests localmente
<comando exacto, según lenguaje/framework>

## Cómo entregar
1. Aceptá el assignment desde el link que te mandó tu docente.
2. GitHub va a crear un repo personal en tu cuenta.
3. Clonά tu repo: `git clone <url-de-tu-repo>`
4. Implementá la solución en `src/`.
5. Hacé commit y push. GitHub Classroom ejecuta los tests automáticamente.
6. Verificá que el check ✅ aparece en tu repo antes de la fecha límite.
```

---

### Step 6: Generar `autograde-setup.md` (guía para el docente)

Este archivo **no va al repo público** — es una guía paso a paso para que el docente publique
el assignment en GitHub Classroom. Incluir:

```markdown
# Guía de Publicación — GitHub Classroom Autograding
## Tema {topic_number}: {topic_name}

## Paso 1: Crear el Template Repo en GitHub
1. Ir a github.com → New repository
2. Nombre: `{repo_name}-template`
3. Visibilidad: **Private** (recomendado) o Public
4. Subir el contenido de esta carpeta (`autograde-repo/`):
   ```
   cd {topic_folder}/autograde-repo
   git init
   git add .
   git commit -m "Initial template"
   git remote add origin https://github.com/{tu-org}/{repo_name}-template.git
   git push -u origin main
   ```
5. En Settings del repo → marcar ✅ "Template repository"

## Paso 2: Crear el Assignment en GitHub Classroom
1. Ir a classroom.github.com → tu aula → New Assignment
2. Tipo: **Individual** (o Group si aplica)
3. Título: "TP {topic_number} — {topic_name}"
4. Template repository: buscar `{repo_name}-template`
5. Fecha límite: configurar según el cursado
6. Autograding: el `classroom.yml` en el template se activa automáticamente con cada push del alumno.
   - Opcionalmente, ir a "Grading and feedback" para revisar o ajustar tests via UI
   - Para usar presets UI en vez de `classroom.yml`: seleccionar "Add autograding test" → elegir preset
     (los tests del `autograding.json` de referencia sirven como guía)
7. Copiar el **Assignment Link** y compartirlo con los alumnos

## Paso 3: Monitoreo
- Panel de classroom.github.com → ver progreso por alumno en tiempo real
- Los tests corren automáticamente en cada push del alumno (y manualmente si se configura `workflow_dispatch`)
- Ver logs individuales: Assignments → alumno → ícono de checklist → GitHub Actions logs
- Descargar CSV con puntajes: botón "Download" en la página del assignment

## Trazabilidad de tests → consignas
| Test | Consigna tp.md | Puntos |
|------|----------------|--------|
<tabla completada automáticamente por Rodrigo>
```

---

### Step 7: Output Summary

Mostrar al docente:

```
✅ Repo Autograde generado en: {topic_folder}/autograde-repo/

Archivos creados:
  autograde-repo/.github/classroom/autograding.json  → {N} tests configurados ({total} puntos)
  autograde-repo/.github/workflows/classroom.yml     → GitHub Actions autograding
  autograde-repo/src/                               → Starter code ({lenguaje})
  autograde-repo/tests/                             → {N} archivos de test
  autograde-repo/README.md                          → Instrucciones para alumnos
  autograde-setup.md                                → Guía de publicación (solo docente — NO sube a GitHub)

Próximos pasos:
1. Revisá los tests en autograde-repo/tests/ y ajustalos si necesario
2. Seguí las instrucciones en autograde-setup.md para publicar en GitHub Classroom
3. Compartí el Assignment Link con tus alumnos
```

Preguntar: "¿Querés ajustar algún test o configuración antes de publicar?"

---

## Output Files

| Archivo | Descripción |
|---------|-------------|
| `autograde-repo/.github/classroom/autograding.json` | Config de tests de GitHub Classroom |
| `autograde-repo/.github/workflows/classroom.yml` | GitHub Actions workflow |
| `autograde-repo/src/*` | Starter code sin solución |
| `autograde-repo/tests/*` | Un archivo de test por consigna |
| `autograde-repo/README.md` | Instrucciones para alumnos |
| `autograde-setup.md` | Guía de publicación (en `{topic_folder}/`, fuera del repo — NO sube a GitHub) |
