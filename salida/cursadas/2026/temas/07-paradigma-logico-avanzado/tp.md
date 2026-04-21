# Trabajo Práctico — Tema 07: Paradigma Lógico Avanzado (Clase 2+3)

**Materia:** Paradigmas y Lenguajes de Programación 2026
**Docente:** Matías Gel
**Tipo de entrega:** **Repositorio Git con autograding** (GitHub Classroom)
**Fecha de entrega:** 2 semanas desde el día de la clase
**Modalidad:** individual o en pares
**Aceptación:** [GitHub Classroom — Paradigmas 2026](https://classroom.github.com/classrooms/260723469-paradigmas-y-lenguajes-de-programacion-2026)

---

## Cómo aceptar la tarea

1. Ingresar al link de GitHub Classroom de la materia.
2. Aceptar la tarea **"TP Tema 07 — Prolog Avanzado"**.
3. Classroom crea automáticamente un repositorio privado con el scaffold.
4. Clonar el repositorio en local:
   ```bash
   git clone <URL-de-tu-repo>
   cd <nombre-del-repo>
   ```
5. Leer el `README.md` del repo con las instrucciones completas de instalación y uso de SWI-Prolog.

---

## Objetivos

Integrar y aplicar los conceptos de la **clase 2+3 del módulo Prolog**:

- Unificación (`=`, `==`, `=..`)
- Backtracking y motores de búsqueda SLD
- Corte verde y rojo (`!`), if-then-else
- Negación por falla (`\+`)
- Aritmética Prolog (`is/2`, comparadores)
- Listas: `member`, `append`, `length` — implementación manual
- Recursión con acumulador (last-call optimization)
- Meta-predicados (`findall`, `setof`, `bagof`)
- Aplicaciones: grafos, CSP, N-reinas

---

## Estructura del trabajo

**28 ejercicios** en el archivo `ejercicios-clase2-3.pl`:

| Rango | Temas | Dificultad |
|-------|-------|-----------|
| 1–3   | Unificación | Básica |
| 4–6   | Backtracking + meta-predicados | Intermedia |
| 7–8   | Aritmética | Intermedia |
| 9–11  | Corte e if-then-else | Intermedia |
| 12    | Negación por falla | Básica |
| 13–16 | Listas (member, append, length, last) | Intermedia |
| 17–19 | Recursión con acumulador | Intermedia-avanzada |
| 20–22 | Integración meta-predicados | Intermedia |
| 23–24 | Grafos recursivos | Avanzada |
| 25    | CSP (mapa de colores) | Avanzada |
| 26–27 | Integradores | Avanzada |
| 28    | **Desafío: 4-reinas** | Experta |

**Total de puntos de autograding: 111** (normalizado a 10 por Classroom).

---

## Flujo de trabajo

1. Abrir `ejercicios-clase2-3.pl` en VS Code.
2. Buscar los `% COMPLETAR` y escribir tu solución.
3. Probar localmente:
   ```bash
   swipl -l ejercicios-clase2-3.pl
   ?- factorial(5, F).       % F = 120
   ```
4. Correr el test suite completo:
   ```bash
   swipl -q -g 'run_tests' -t halt -l tests/test_ejercicios.pl
   ```
5. Commit + push:
   ```bash
   git add .
   git commit -m "resueltos ejercicios 1-10"
   git push
   ```
6. GitHub Actions corre automáticamente los 28 tests y publica resultados.

---

## Criterios de evaluación (automáticos)

| Porcentaje de tests que pasan | Nota |
|:-----------------------------:|:----:|
| 95–100% | **10** |
| 85–94%  | 9 |
| 75–84%  | 8 |
| 65–74%  | 7 |
| 55–64%  | 6 |
| 40–54%  | 4 (recuperatorio oral) |
| < 40%   | rehacer |

**Bonus (+1 punto):** código bien comentado con explicación del razonamiento en los ejercicios 24 (ruta), 25 (CSP) y 28 (4-reinas). Se evalúa manualmente tras el cierre.

**Restricciones:**
- No se permite modificar `tests/` ni `.github/`.
- No se permiten librerías externas salvo `library(lists)` (ya importada).
- Los ejercicios 13, 14, 15 **deben** implementarse **sin** usar `member/2`, `append/3`, `length/2` incorporados.

---

## Recursos

- **Guía de estudio del tema (PDF):** entregada junto con este TP.
- **Filminas de la clase:** https://docs.google.com/presentation/d/1Uu9WdtDPY_pQrYYvMqKsBwh5J38pOshTEXOfVvRvr5k/edit
- **SWI-Prolog Reference Manual:** https://www.swi-prolog.org/pldoc/refman/
- **SWISH (online):** https://swish.swi-prolog.org/
- **Learn Prolog Now!** (capítulos 4–7 recomendados): https://lpn.swi-prolog.org/

---

## Consultas

- **Canal del aula en Google Classroom** para consultas generales.
- **Office hours del docente:** según cronograma de la materia.
- **Issues del repo de cada alumno:** el docente revisa periódicamente y deja feedback.
