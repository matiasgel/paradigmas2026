# Guía de Publicación — GitHub Classroom Autograding
## TP 03: Programación Funcional TypeScript + Clojure

> ⚠️ Este archivo es SOLO para el docente. NO subir a GitHub junto con el template.

---

## Estructura generada

```
autograde-repo/          ← este directorio es el repo template que sube a GitHub
├── .github/
│   ├── classroom/autograding.json   ← referencia para UI de Classroom
│   └── workflows/classroom.yml      ← fuente de verdad para el autograding
├── .gitignore
├── README.md
├── typescript/
│   ├── src/index.ts                 ← 25 stubs TypeScript
│   ├── tests/g1/ … g5/             ← 25 archivos de test Jest
│   ├── package.json
│   ├── tsconfig.json
│   └── jest.config.ts
└── clojure/
    ├── src/ejercicios/core.clj      ← 25 stubs Clojure
    ├── test/ejercicios/grupo*_test.clj  ← 5 archivos de test
    └── project.clj
```

---

## Paso 1: Crear el Template Repo en GitHub

```bash
# 1. Ir a github.com → New repository
#    Organización: UNTDF-LabProg
#    Nombre: tp-funcional-template
#    Visibilidad: Private (recomendado)
#    NO inicializar con README

# 2. Subir el contenido de autograde-repo/
cd salida/cursadas/2026/temas/03-intro-funcional-ts/autograde-repo

git init
git add -A
git commit -m "feat: template inicial TP03 funcional TypeScript + Clojure"
git remote add origin https://github.com/UNTDF-LabProg/tp-funcional-template.git
git branch -M main
git push -u origin main
```

### 3. Marcar como Template Repository

1. Ir a `github.com/UNTDF-LabProg/tp-funcional-template`
2. **Settings** → General → sección "Template repository" → marcar ✅
3. Guardar

---

## Paso 2: Crear el Assignment en GitHub Classroom

1. Ir a [classroom.github.com](https://classroom.github.com) → tu aula:
   **Paradigmas y Lenguajes de Programación 2026**
   (https://classroom.github.com/classrooms/260723469-paradigmas-y-lenguajes-de-programacion-2026)

2. Clic en **New Assignment**

3. Completar:
   - **Title:** `TP 03 — Programación Funcional TypeScript + Clojure`
   - **Type:** Individual
   - **Deadline:** (configurar fecha = 1 semana desde hoy)
   - **Template repository:** buscar `tp-funcional-template` (de la org `UNTDF-LabProg`)
   - **Visibility del repo del alumno:** Private (recomendado)

4. **Autograding:**
   El `classroom.yml` en el template se activa automáticamente con cada push.
   Si querés revisar los tests desde la UI de Classroom en vez de confiar solo en el workflow:
   - Ir a "Grading and feedback" → "Add autograding tests"
   - Los tests del `autograding.json` sirven como referencia para configurar los presets a mano

5. Clic en **Create Assignment** → copiar el link de invitación

6. Compartir el link con los alumnos (Moodle / Google Classroom / Slack)

---

## Paso 3: Verificar que el Autograding funciona

1. Aceptar el assignment con una cuenta de prueba (o tu cuenta personal)
2. Clonar el repo generado
3. Hacer un push cualquiera (sin implementar nada)
4. Verificar en la pestaña **Actions** que el workflow `Autograding Tests` corrió y que:
   - Todos los pasos TS-G1 … CLJ-G5 aparecen como ❌ (tests fallan = comportamiento esperado con stubs)
   - El reporter aparece al final

---

## Distribución de Puntos (referencia rápida)

| Step ID | Grupo | Pts |
|---------|-------|-----|
| `ts-g1` | TS-G1 Funciones Puras (TS-01–05) | 10 |
| `ts-g2` | TS-G2 Inmutabilidad (TS-06–10) | 10 |
| `ts-g3` | TS-G3 map/filter/reduce (TS-11–18) | 16 |
| `ts-g4` | TS-G4 Composición y HOF (TS-19–22) | 8 |
| `ts-g5` | TS-G5 Contraste (TS-23–25) | 6 |
| `clj-g1` | CLJ-G1 Básicas (CLJ-01–05) | 10 |
| `clj-g2` | CLJ-G2 map/filter/reduce (CLJ-06–11) | 12 |
| `clj-g3` | CLJ-G3 HOF (CLJ-12–16) | 10 |
| `clj-g4` | CLJ-G4 Recursión (CLJ-17–20) | 8 |
| `clj-g5` | CLJ-G5 Colecciones (CLJ-21–25) | 10 |
| **Total** | | **100** |

---

## Notas operativas

- **Las restricciones de estilo TypeScript** (no `let`, no loops) NO se verifican automáticamente — son por honor. Si un alumno pasa todos los tests pero usa `let` en todos lados, los tests igual pasan. Inspección manual si hay sospechas.
- **Timeout de cada step:** 5 minutos. Suficiente para tests simples. Si algún alumno tiene recursión infinita, el step expira y vale 0.
- **Clojure JVM warmup:** los primeros 2-3 minutos del job son setup de dependencies. El timeout por step (5 min) es independiente del setup.
- **Node.js 22 + TypeScript 5.4 + Clojure 1.12 + Leiningen** — versiones fijadas en `classroom.yml`.
- **Reintentos:** si el workflow falla por razones de infraestructura (rate limit de GitHub), el alumno puede rehacer un push o el docente puede re-run el workflow desde Actions.

---

*Generado por Aux. Valeria (tp-designer) — EDU Academic Course Production Suite*
*Tema 03 — Paradigmas y Lenguajes de Programación 2026 — UNTDF/IDEI — 2026-04-01*
