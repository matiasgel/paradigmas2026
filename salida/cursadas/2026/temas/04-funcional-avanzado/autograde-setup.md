# Autograde Setup — TP04 Funcional Avanzado

## Datos del repositorio template

| Campo | Valor |
|---|---|
| **Nombre** | `tp04-funcional-avanzado-template` |
| **Ejercicios** | 18 (11 TypeScript + 7 Clojure) |
| **Puntos totales** | 100 |
| **Framework TS** | vitest |
| **Framework Clj** | lein test (clojure.test) |
| **Runner** | `ubuntu-latest` con Node.js 20 + Java 21 Temurin + Leiningen |

## Pasos para publicar en GitHub Classroom

### 1. Crear repositorio template

```bash
# Desde la carpeta autograde-repo/
cd autograde-repo
git init
git add -A
git commit -m "initial: tp04 funcional avanzado template"
git remote add origin https://github.com/UNTDF-IDEI/tp04-funcional-avanzado-template.git
git push -u origin main
```

En **Settings → General**, marcar **Template repository**.

### 2. Crear assignment en GitHub Classroom

1. Ir a [classroom.github.com](https://classroom.github.com) → Tu clase
2. **New assignment** → Individual
3. **Title**: `TP04 — Programación Funcional Avanzada`
4. **Template repository**: `UNTDF-IDEI/tp04-funcional-avanzado-template`
5. **Visibility**: Private
6. **Grant admin access to students**: No
7. **Enable feedback pull request**: Sí

### 3. Configurar autograding desde la UI

El archivo `.github/classroom/autograding.json` ya tiene la configuración. Al importar el template, Classroom debería reconocer los 18 tests automáticamente. Si no:

- Ir al assignment → **Test settings**
- Agregar manualmente cada test con los datos del JSON

### 4. Verificar el workflow

El archivo `.github/workflows/classroom.yml` ejecuta los 18 ejercicios como steps independientes usando `classroom-resources/autograding-command-grader@v1`. Cada step tiene:

- `test-name`: nombre descriptivo
- `command`: comando de ejecución específico
- `timeout`: 10 minutos
- `max-score`: puntos de ese ejercicio

El último step `autograding-grading-reporter@v1` genera el badge de nota.

## Distribución de puntos

| Ej | Tema | Lang | Pts |
|----|------|------|-----|
| 01 | Pipeline filter/map/reduce | TS | 5 |
| 02 | Composición pipe/compose | TS | 6 |
| 03 | Inmutabilidad con spread | TS | 4 |
| 04 | Pipeline con ->> | Clj | 5 |
| 05 | flatMap y reduce | TS | 5 |
| 06 | Partial application | TS | 6 |
| 07 | Partial en Clojure | Clj | 5 |
| 08 | Currying | TS | 6 |
| 09 | Validadores currying | Clj | 5 |
| 10 | Result y validación | TS | 7 |
| 11 | Middleware como HOF | TS | 6 |
| 12 | Recursión de cola | Clj | 6 |
| 13 | Recursión de cola | TS | 5 |
| 14 | Memoization | TS | 5 |
| 15 | Lazy sequences | Clj | 5 |
| 16 | DSL data-driven | Clj | 5 |
| 17 | Integrador | TS | 7 |
| 18 | Integrador | Clj | 7 |
| | | **Total** | **100** |

## Requisitos del runner

El workflow instala automáticamente:
- **Node.js 20** (para TypeScript/vitest)
- **Java 21 Temurin** (para Clojure)
- **Leiningen** (se descarga desde GitHub en el step)

No se necesitan secrets adicionales ni configuración extra.
