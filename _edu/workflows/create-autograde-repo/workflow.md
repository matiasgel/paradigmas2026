# Workflow: Create Autograde Repo

**Module:** edu
**Phase:** 3 — Producción de Temas
**Owner Agent:** classroom-designer (Rodrigo)
**Trigger:** `/edu-create-autograde-repo` or Step 5.5 of topic-cycle

---

## Overview

Genera la estructura completa de un **repo plantilla para GitHub Classroom** con autograding
configurado por consigna. Cada test del `autograding.json` tiene trazabilidad directa al `tp.md`.

El output es un directorio `{topic_folder}/autograde-repo/` listo para subir como template repo
a GitHub y configurar como assignment en GitHub Classroom.

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
6. **Tiempo máximo de ejecución por test** (sugerido: 10 segundos)

Mostrar resumen de configuración y pedir confirmación antes de generar.

---

### Step 2: Generar Estructura del Repo

Crear el directorio `{topic_folder}/autograde-repo/` con la siguiente estructura:

```
autograde-repo/
├── .github/
│   ├── classroom/
│   │   └── autograding.json          ← config oficial de GitHub Classroom
│   └── workflows/
│       └── classroom.yml             ← GitHub Actions para autograding
├── src/
│   └── (starter code según lenguaje) ← scaffolding mínimo, SIN solución
├── tests/
│   └── (un archivo de test por consigna)
├── README.md                          ← instrucciones para el alumno
└── autograde-setup.md                ← guía de publicación para el docente (NO va al repo público)
```

**Reglas de generación:**

- `src/`: Solo scaffolding mínimo. Firmas de funciones/clases vacías o con `pass`/`throw new NotImplementedException()`.
  - Python: `src/__init__.py`, `src/solucion.py` (o nombre derivado del tema)
  - Java: `src/main/java/tp/Solucion.java`
  - C: `src/solucion.c`, `src/solucion.h`
- `tests/`: Un archivo por consigna (`test_ej1.py`, `test_ej2.py`, etc.).
  - Cada archivo tiene al menos 2 casos de test: caso borde + caso normal.
  - Los tests son funcionales pero NO revelan la solución completa.
- `README.md`: En español. Secciones: Objetivo / Consignas / Cómo ejecutar los tests localmente / Cómo entregar.
- `autograding.json`: Un objeto de test por consigna. Puntos configurados según Step 1.
- `classroom.yml`: Usa `education/autograding@v1` (acción oficial).

---

### Step 3: Generar `autograding.json`

Formato oficial GitHub Classroom:

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
      "timeout": <timeout_segundos>,
      "points": <puntos_consigna>
    }
  ]
}
```

**Trazabilidad obligatoria:** El campo `"name"` de cada test DEBE incluir el número de consigna
tal como aparece en `tp.md`. Documentar la trazabilidad como comentario en `autograde-setup.md`.

---

### Step 4: Generar `classroom.yml`

```yaml
name: GitHub Classroom Autograding

on:
  push:
    branches: ['*']
  pull_request:
    branches: ['*']

permissions:
  checks: write
  actions: read
  contents: read

jobs:
  autograding:
    name: Autograding
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup (lenguaje específico)
        # <agregar setup específico: pip install, mvn, gcc, npm, etc.>
      - name: Autograding
        uses: education/autograding@v1
        env:
          FORCE_COLOR: 1
```

Adaptar el step "Setup" al lenguaje elegido en Step 1.

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
6. Autograding: seleccionar ✅ "Add autograding"
   - GitHub detecta automáticamente el `autograding.json` del template
7. Copiar el **Assignment Link** y compartirlo con los alumnos

## Paso 3: Monitoreo
- Panel de classroom.github.com → ver progreso por alumno en tiempo real
- Los tests corren automáticamente en cada push del alumno
- Puntos se calculan automáticamente según `autograding.json`

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
  .github/classroom/autograding.json  → {N} tests configurados ({total} puntos)
  .github/workflows/classroom.yml     → GitHub Actions autograding
  src/                                → Starter code ({lenguaje})
  tests/                              → {N} archivos de test
  README.md                           → Instrucciones para alumnos
  autograde-setup.md                  → Guía de publicación (solo para docente)

Próximos pasos:
1. Revisá los tests en tests/ y ajustalos si necesario
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
| `autograde-repo/autograde-setup.md` | Guía de publicación (solo docente) |
