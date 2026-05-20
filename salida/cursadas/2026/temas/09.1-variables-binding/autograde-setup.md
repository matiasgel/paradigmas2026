# Guía de configuración — TP 09.1 en GitHub Classroom

**Solo para docentes — no publicar en el repositorio template**

---

## 1. Publicar el template en GitHub

### 1a. Crear el repositorio template

1. Ir a [github.com/new](https://github.com/new) con la cuenta de la organización `paradigmas-y-lenguajes-de-programacion-2026`.
2. Nombre sugerido: `tp09-1-variables-binding-template`
3. Visibilidad: **Public** (requerido para GitHub Classroom gratuito).
4. **No** inicializar con README — se va a subir el contenido desde local.

### 1b. Subir el contenido del autograde-repo

Desde la carpeta `autograde-repo/` de este tema:

```bash
cd salida/cursadas/2026/temas/09.1-variables-binding/autograde-repo

git init
git add -A
git commit -m "chore: TP 09.1 template inicial — Variables, Binding y Ambito"
git branch -M main
git remote add origin https://github.com/paradigmas-y-lenguajes-de-programacion-2026/tp09-1-variables-binding-template.git
git push -u origin main
```

### 1c. Marcar como template

En GitHub → Settings del repositorio → activar **"Template repository"**.

---

## 2. Crear la asignación en GitHub Classroom

1. Ir a: [classroom.github.com/classrooms/260723469-paradigmas-y-lenguajes-de-programacion-2026](https://classroom.github.com/classrooms/260723469-paradigmas-y-lenguajes-de-programacion-2026)
2. Click en **"New assignment"** → **"Individual assignment"**.

### Configuración recomendada

| Campo | Valor |
|-------|-------|
| Title | `TP 09.1 — Variables, Binding y Ámbito` |
| Deadline | Fecha de cierre (agregar aquí) |
| Repository prefix | `tp09-1-variables-binding-` |
| Visibility | Private |
| Template repository | `tp09-1-variables-binding-template` |
| Add a supported editor | VS Code (opcional) |

### Autograding

En la sección **Grading and feedback**:

1. Click **"Add autograding test"** → **"Run command"** para cada ejercicio:

| Test name | Setup command | Run command | Timeout | Points |
|-----------|--------------|-------------|---------|--------|
| Ej01 — L-value y 5-tupla | `npm install` | `npx vitest run tests/ej01.test.ts` | 10 min | 20 |
| Ej02 — Binding de tipos | `npm install` | `npx vitest run tests/ej02.test.ts` | 10 min | 20 |
| Ej03 — Binding de almacenamiento | `npm install` | `npx vitest run tests/ej03.test.ts` | 10 min | 25 |
| Ej04 — Ámbito estático | `npm install` | `npx vitest run tests/ej04.test.ts` | 10 min | 20 |
| Ej05 — Errores de binding | `npm install` | `npx vitest run tests/ej05.test.ts` | 10 min | 15 |

> **Alternativa**: si el classroom.yml ya está en el repo, GitHub Classroom detecta los tests automáticamente desde `.github/classroom/autograding.json`. En ese caso, solo hacer click en "Enable autograding from .github/classroom/autograding.json".

3. Click **"Create assignment"**.

---

## 3. Compartir el link a los alumnos

Una vez creada la asignación, GitHub Classroom genera un link de invitación:
```
https://classroom.github.com/a/<código-de-asignación>
```

Publicar ese link en el aula virtual (Moodle / SIGA / Canal de Teams).

---

## 4. Monitorear entregas

En GitHub Classroom → nombre de la asignación → ver la tabla con todos los alumnos,
estado del último push y puntaje de autograding.

---

## 5. Notas de corrección manual

Los tests de autograding verifican la funcionalidad. Adicionalmente revisar:

- **Ej01**: la implementación de `swap` usa una variable temporal (no desestructuración), para que el alumno vea explícitamente el L-value temporal. No penalizar si usa desestructuración, pero preguntar en oral.
- **Ej03**: verificar que `factorial` es efectivamente recursiva (no iterativa). El test no lo distingue, pero el objetivo pedagógico es OA3 sobre stack-dynamic.
- **Ej05**: verificar que las funciones `buggy*` NO fueron modificadas (son parte del enunciado).

---

## Estructura del autograde-repo

```
autograde-repo/
├── .github/
│   ├── classroom/
│   │   └── autograding.json        ← config de autograding
│   └── workflows/
│       └── classroom.yml           ← GitHub Actions workflow
├── src/
│   ├── ej01.ts   ← L-value, R-value, 5-tupla       (20 pts)
│   ├── ej02.ts   ← Binding de tipos                (20 pts)
│   ├── ej03.ts   ← Binding de almacenamiento       (25 pts)
│   ├── ej04.ts   ← Ámbito estático                 (20 pts)
│   └── ej05.ts   ← Errores de binding              (15 pts)
├── tests/
│   ├── ej01.test.ts
│   ├── ej02.test.ts
│   ├── ej03.test.ts
│   ├── ej04.test.ts
│   └── ej05.test.ts
├── package.json
├── tsconfig.json
├── vitest.config.ts
└── README.md
```
