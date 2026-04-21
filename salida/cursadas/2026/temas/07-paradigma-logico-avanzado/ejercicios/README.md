# Ejercicios Prolog — Clase 2+3: Paradigma Lógico Avanzado
**Paradigmas y Lenguajes de Programación 2026 — UNTdF**

> **28 ejercicios** sobre unificación, backtracking, corte, negación, aritmética, listas, recursión con acumulador, meta-predicados y aplicaciones (grafos, CSP, N-reinas).

---

## Temas cubiertos (alineados con la clase 2+3)

| Bloque de clase | Ejercicios |
|-----------------|-----------|
| Unificación (`=`, `==`, `=..`) | 1, 2, 3 |
| Backtracking, `findall`, `setof` | 4, 5, 6, 22, 26 |
| Aritmética (`is/2`, operadores) | 7, 8, 19, 22, 27 |
| Corte (`!`, verde y rojo), if-then-else | 9, 10, 11 |
| Negación por falla (`\+`) | 12 |
| Listas (`member`, `append`, `length` manuales) | 13, 14, 15, 16 |
| Recursión con acumulador | 17, 18, 19, 20 |
| Meta-predicados + filtros | 21, 22, 26 |
| Grafos (backtracking recursivo) | 23, 24 |
| Aplicaciones: CSP, N-reinas | 25, 28 |
| Integrador final | 27 |

**Peso total:** 111 puntos → normalizado a 10 por GitHub Classroom.

---

## Instalación de SWI-Prolog

### Windows
1. Descargar desde https://www.swi-prolog.org/download/stable → *Windows 64-bit installer (.exe)*
2. Marcar **"Add SWI-Prolog to PATH"** durante la instalación.
3. Verificar: `swipl --version` (debe mostrar `SWI-Prolog version 9.x.x`).

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install swi-prolog
swipl --version
```

### macOS
```bash
brew install swi-prolog
```

### Sin instalar: SWISH online
https://swish.swi-prolog.org/ — pegar el contenido de `ejercicios-clase2-3.pl` y probar consultas.

---

## Flujo de trabajo

### 1. Clonar tu fork (GitHub Classroom creará uno automático al aceptar la tarea)

```bash
git clone <URL-de-tu-repo>
cd <nombre-del-repo>
```

### 2. Editar `ejercicios-clase2-3.pl`

Buscá los `% COMPLETAR` y reemplazá con tu solución. Cada bloque tiene:
- **Enunciado** en comentarios.
- **Ejemplos de uso** con resultado esperado.
- **Pistas** cuando el ejercicio es avanzado.

### 3. Probar localmente

Desde la terminal integrada:

```bash
# Cargar el archivo en el intérprete y probar consultas
swipl -l ejercicios-clase2-3.pl

?- factorial(5, F).      % F = 120
?- reversa([1,2,3], R).  % R = [3,2,1]
?- halt.
```

### 4. Correr el test suite completo

```bash
swipl -l tests/test_ejercicios.pl
```

Salida esperada (cuando todo está bien):
```
% PL-Unit: ej01_iguales .. done
...
% 28 tests passed
```

### 5. Correr un solo grupo

```bash
swipl -q -t 'run_tests(ej08_factorial),halt(0)' -l tests/test_ejercicios.pl
```

### 6. Commit + push → autograding automático

```bash
git add .
git commit -m "resuelvo ejercicios 1-5"
git push
```

GitHub Actions corre los 28 tests y publica el puntaje en la pestaña **Actions** del repo.

---

## Configuración de VS Code (recomendado)

### Extensión VSC-Prolog

1. `Ctrl+Shift+X` → buscar `VSC-Prolog` (autor: Arthur Wang).
2. Instalar.

### Ruta del ejecutable

Abrir `settings.json` (`Ctrl+Shift+P` → *Open User Settings JSON*) y agregar:

**Windows:**
```json
{ "prolog.executablePath": "C:\\Program Files\\swipl\\bin\\swipl.exe" }
```

**Linux / macOS:**
```json
{ "prolog.executablePath": "/usr/bin/swipl" }
```

### Atajo útil

`F5` sobre un archivo `.pl` abre el intérprete con el archivo cargado.

---

## Consejos de depuración

| Problema | Solución |
|----------|----------|
| `arguments are not sufficiently instantiated` | Usaste `is/2` con variables libres → liga las variables antes. |
| Bucle infinito | El caso recursivo está antes del caso base → invertí el orden. |
| `undefined procedure` | Faltó cargar con `consult/1` o el predicado está mal escrito. |
| Tests pasan local, falla CI | Verificá que usás SWI-Prolog puro (no extensiones no portables). |

### Trazador paso a paso
```prolog
?- trace.
?- factorial(5, F).
% enter, call, exit visibles en cada paso

?- notrace.
```

---

## Estructura del repo

```
.
├── ejercicios-clase2-3.pl     # archivo a completar (28 ejercicios)
├── tests/
│   └── test_ejercicios.pl      # test suite PLUnit (NO modificar)
├── .github/
│   ├── classroom/
│   │   └── autograding.json    # definición de tests (NO modificar)
│   └── workflows/
│       └── classroom.yml       # CI autograding (NO modificar)
└── README.md                   # este archivo
```

---

## Entrega

- **Fecha límite:** ver consigna en GitHub Classroom.
- **Modalidad:** individual o en pares (declarar en commit).
- **Evaluación:** automática (CI) + revisión humana del docente para ejercicios de diseño.
- **No está permitido** modificar `tests/` ni `.github/`.

### Criterios de nota (sobre el autograding automático)

| Porcentaje de tests | Nota |
|--------------------:|------|
| 95–100% | 10 |
| 85–94%  | 9 |
| 75–84%  | 8 |
| 65–74%  | 7 |
| 55–64%  | 6 |
| 40–54%  | 4 (recuperatorio) |
| < 40%   | rehacer |

---

## Recursos

- **Guía de estudio del tema:** entregada por el docente (PDF).
- **Filminas de la clase:** Google Slides (link en el aula).
- **SWI-Prolog Reference Manual:** https://www.swi-prolog.org/pldoc/refman/
- **Learn Prolog Now!** (capítulos 1–7): https://lpn.swi-prolog.org/

**Docente:** Matías Gel — Paradigmas y Lenguajes de Programación 2026 — UNTdF
