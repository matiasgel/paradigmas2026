# Score Pedagógico — Tema 07: Paradigma Lógico — Clase 2+3

**Tema evaluado:** 07 — Paradigma Lógico Avanzado (Prolog, clase doble 240 min)
**Fecha de simulación:** 2026-04-21
**Modo:** Batch — 4 perfiles (estratégico, ansioso, disperso, recursero)
**Dual perspective:** clase (minuta + filminas) + autónomo (guía de estudio)
**Literatura base:** Sweller & Chen (2023), Olipas (2022), Mahatanankoon & Wolf (2021), Hoq et al. (2025), Mayer (Multimedia Learning 2023)

---

## Resumen Ejecutivo

| Perfil | En clase | Guía autónoma | TP estimado | **Score global** |
|--------|---------:|--------------:|------------:|-----------------:|
| Estratégico | **82** | **89** | 85–92 | **85** |
| Ansioso | **58** | **74** | 55–68 | **65** |
| Disperso | **42** | **51** | 38–52 | **46** |
| Recursero | **60** | **66** | 60–72 | **63** |
| **Cohort promedio** | **60** | **70** | — | **65** |

> **Lectura:** La clase cumple con objetivos para el estratégico. La guía de estudio compensa bien al ansioso (+16 pts). **Disperso queda expuesto** en bloques densos (B9, B11). Recursero aprueba ejercicios mecánicos pero falla en 3.3 (por qué el orden importa) y en acumuladores integradores.

---

## Scores por Bloque (promedio cohort)

| Bloque | Min | Contenido | Score | Riesgo |
|--------|----:|-----------|------:|:------:|
| B0 | 10 | Repaso | 88 | 🟢 |
| B1 | 25 | Unificación | 74 | 🟡 |
| B2 | 25 | Resolución SLD | 66 | 🟡 |
| B3 | 25 | Backtracking | 58 | 🔴 |
| B4 | 20 | Corte | **52** | 🔴 |
| B5 | 15 | Negación por falla | 61 | 🟡 |
| B6 | 20 | Ejercicio | 70 | 🟢 |
| B7 | 20 | Aritmética | 68 | 🟡 |
| B8 | 25 | Listas | 63 | 🟡 |
| B9 | 25 | Recursión c/ acumulador | **54** | 🔴 |
| B10 | 20 | Meta-predicados | 62 | 🟡 |
| B11 | 15 | Aplicaciones (CSP + 4-reinas) | **45** | 🔴 |
| B12 | 5 | Prolog 2026 | 72 | 🟡 |
| B13 | 5 | Cierre | 80 | 🟢 |

**Bloques en rojo (< 60):** B3 Backtracking, B4 Corte, B9 Recursión con acumulador, B11 Aplicaciones.

---

## Análisis por Perfil

### 🎯 Estratégico — "Lucía" (83 pts)
- **Fortalezas:** unificación, SLD, listas manuales.
- **Puntos bajos:** B4 (corte rojo vs verde — dice *"entiendo cuándo usarlo pero no por qué uno es peor"*), B11 (CSP con 4-reinas sin tiempo para internalizar).
- **Misconception probable:** `dif/2` es *"solo una versión más nueva de `\=`"* — no capta el concepto de restricción diferida hasta trabajar el ejercicio integrador.
- **Requiere:** explicación explícita de *"declarativo puro vs corte rojo"* con contraejemplo.

### 😰 Ansioso — "Tomás" (65 pts)
- **Score clase 58:** sobrecarga cognitiva en B3+B4 (50 min consecutivos de backtracking + corte sin respiro). Cita: *"¿El `!` corta siempre? ¿También cuando vuelve? No entiendo..."*
- **Score guía 74:** la guía baja el ritmo y Tomás remonta. El ejemplo completo del árbol SLD (3.2.2) es salvador.
- **Bloquea en:** occurs-check, `=..`, meta-predicados (`findall` vs `bagof` vs `setof` — tabla comparativa ayuda mucho).
- **Riesgo alto:** el TP ej24 (rutas en grafo) lo abandona si no ve la traza en pizarrón.
- **Requiere:** caja de pánico *"si estás perdido, leé solo X antes de seguir"* al inicio de cada bloque rojo.

### 🤯 Disperso — "Sofía" (46 pts)
- **Score clase 42:** perdida desde min 85 (fin de B3). No distingue *goal*, *cláusula*, *resolvente*.
- **Misconception persistente:** *"el `!` es como `return` en Python"* — no lo corrige nadie en clase.
- **Abandono estimado:** durante B4 (corte). Score 0 en B9, B11.
- **Score guía 51:** recupera en B1-B2 si lee la guía, pero B9 y B11 siguen siendo opacos.
- **TP:** aprueba ej01–ej12 (básicos). Falla ej17+ (acumulador), ej23–25 (grafos+CSP). Entrega 40% funcional.
- **Requiere:** mapa mental *visual* al inicio de B3 y B9, demo de *"¿cuándo backtrackea?"* con animación lenta.

### 🔁 Recursero — "Diego" (63 pts)
- **Zona de confort:** patrones `member`, `append`, `length` — los memoriza de clase 1.
- **Falla:** *"¿por qué el orden cláusula base → recursivo importa?"* (3.2.3) — dice *"porque sí, es la regla"*, no entiende la consecuencia.
- **Misconception crítica:** en acumuladores piensa *"es una variable global"*, no capta la semántica de *"parámetro de estado que decrece"*.
- **Alerta TP:** ej17 (`suma_lista` c/ acumulador) lo **aprueba sin comprender** copiando el patrón.
- **Integradores ej26/27/28:** filtro — si entiende acumulador, aprueba 28 (4-reinas); si no, bloquea.
- **Requiere:** pregunta detectora en vivo: *"Pedí al recursero que cuente de 1 a N usando acumulador. Probable respuesta: usa decrementar en vez de incrementar y se pierde."*

---

## Riesgos de Clase (ordenados)

| # | Riesgo | Perfiles afectados | Intervención sugerida |
|--:|--------|-------------------|-----------------------|
| 1 | **B3+B4 consecutivos (50 min) sin ejercicio** | disperso, ansioso | Insertar pausa socrática en min 80 — *"¿dónde backtrackea Prolog ahora?"* |
| 2 | **B9 recursión c/ acumulador — concepto abstracto en 25 min** | disperso, recursero | Analogía física: *"mochila que va cargando el resultado"* + dibujar traza en pizarrón para `factorial/2 → factorial/3` |
| 3 | **B11 aplicaciones: CSP + 4-reinas en 15 min** | todos | Recortar a 1 solo ejemplo (colorear mapa) → 4-reinas queda como ejercicio del TP |
| 4 | **Corte rojo sin contraejemplo** | estratégico, recursero | F-063: agregar contraejemplo con **misma consulta, resultados distintos** |
| 5 | **Occurs-check: SWI lo desactiva** | ansioso | F-021: caja *"no te asustes — 99% de los programas no lo necesitan"* |
| 6 | **`dif/2` vs `\+` con variables** | estratégico | Tabla comparativa lado a lado con el **mismo caso** |
| 7 | **`findall/bagof/setof`: misma consulta, salidas distintas** | ansioso, recursero | F-134: una misma consulta con los 3 operadores mostrando las 3 salidas |

---

## Zona de Recuperación de la Guía

| Bloque | Clase | Guía | Δ |
|--------|------:|-----:|---:|
| B1 Unificación | 74 | 87 | +13 |
| B2 SLD | 66 | 82 | +16 |
| B3 Backtracking | 58 | 74 | +16 |
| B9 Recursión | 54 | 68 | +14 |

La guía **cumple función compensatoria crítica**. Debe comunicarse explícitamente en clase (*"esta sección está desarrollada a fondo en la guía de estudio — foto del link en pantalla"*).

---

## Comparación vs Temas Previos

| Tema | Score cohort | Cobertura | Nota |
|------|-------------:|----------:|------|
| Tema 03 (Funcional I) | 71 | 95% | Base sólida |
| Tema 04 (Funcional avanzado) | 64 | 88% | Concurrencia fue punto bajo |
| **Tema 07 (Lógico avanzado)** | **65** | **91%** | **Backtracking y acumuladores son los riesgos** |

Tendencia: temas avanzados estabilizan en cohort ~65. Consistent con Sweller & Chen (2023) — carga cognitiva de contenido *abstracto* (SLD, acumulador) requiere segmentación adicional.

---

## Correcciones Recomendadas (priorizadas)

### [C1] Guía de estudio — Agregar caja "mapa mental" al inicio de §3.3 (Backtracking)
- **Impacto:** +6 pts dispersos
- **Forma:** diagrama ASCII del ciclo *goal → unifica → consume → falla → trail → choice point*

### [C2] Guía de estudio — §3.4 Corte — Añadir tabla "verde vs rojo" con contraejemplo
- **Impacto:** +8 pts estratégicos, +4 recursero
- **Forma:** tabla de 3 filas + código que cambia de semántica al cambiar el corte

### [C3] Filminas F-021 — Caja de calma para occurs-check
- **Impacto:** –ansiedad perfil ansioso
- **Forma:** block "para la práctica: no te preocupes — SWI lo desactiva por default"

### [C4] Filminas F-063 — Corte rojo: contraejemplo ejecutable
- **Impacto:** +6 pts cohort en B4
- **Forma:** mismo predicado con/sin corte rojo, mostrar que la semántica declarativa se rompe

### [C5] Filminas F-134 — `findall/bagof/setof` lado a lado
- **Impacto:** +8 pts en B10
- **Forma:** una misma consulta, 3 salidas distintas, anotadas

### [C6] Guía de estudio — §3.9 Acumuladores — Analogía física "mochila"
- **Impacto:** +10 pts disperso, +6 recursero
- **Forma:** párrafo + esquema visual antes del código

### [C7] Minuta — Pausa socrática en min 80
- **Impacto:** –fatiga cohort
- **Forma:** 2 min de pregunta abierta *"¿dónde backtrackea Prolog ahora?"*

---

## Próximos Pasos

1. Aplicar correcciones C1–C7 en los artefactos correspondientes.
2. Regenerar plan de filminas JSON a partir de `filminas.md` actualizado.
3. Re-publicar slides.
4. Ciclo visual: fotos → ajustes → re-publicación hasta consistencia.
5. Calibrar scores post-clase real con encuesta (campo `historial` del YAML).

---

*Generado por simulación batch de 4 perfiles — base: literatura ERIC/ACM + calibración acumulada de temas 03 y 04.*
