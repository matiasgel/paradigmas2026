# TP N° 2 — Pruebas Unitarias

**Laboratorio de Programación y Lenguajes (IF009)**  
Universidad Nacional de Tierra del Fuego — Instituto IDEI  
Ciclo Lectivo 2026 — 1er Cuatrimestre

---

## Objetivo

Implementar 20 ejercicios de Python aplicando pruebas unitarias con `unittest`. Los tests se ejecutan automáticamente al hacer `push` mediante GitHub Actions (autograding).

---

## Consignas

Los 20 ejercicios están descritos en el enunciado del TP (disponible en el aula virtual). Cada ejercicio tiene:

- Un archivo de implementación: `src/ejNN.py`
- Un archivo de tests: `tests/test_ejNN.py` (ya incluido en el repo)

### Bloques

| Bloque | Ejercicios | Tema |
|--------|-----------|------|
| A | 01–05 | Aserciones básicas |
| B | 06–10 | Excepciones y validaciones |
| C | 11–15 | Fixtures y clases bajo test |
| D | 16–18 | Mock, Patch y aislamiento |
| E | 19–20 | TDD avanzado e integración |

---

## Estructura del repositorio

```
tp-02-pruebas-unitarias/
├── src/
│   ├── ej01.py ... ej20.py     ← implementá aquí
├── tests/
│   ├── test_ej01.py ... test_ej20.py  ← NO modificar
├── README.md
└── .github/
    ├── classroom/
    │   └── autograding.json
    └── workflows/
        └── classroom.yml       ← autograding al hacer push
```

> **⚠️ No modificar** los archivos en `tests/` ni `.github/`.

---

## Cómo ejecutar los tests localmente

### Opción A — GitHub Codespaces (recomendado)

1. Abrí el repo en Codespaces (botón verde "Code" → "Open in Codespaces")
2. El entorno ya tiene Python 3.12 instalado
3. Ejecutá todos los tests: `python -m unittest discover -v`
4. Ejecutá un ejercicio específico: `python -m unittest tests.test_ej01 -v`

### Opción B — Local

```bash
# Clonar el repo
git clone <url-del-repo>
cd <nombre-del-repo>

# Ejecutar todos los tests
python -m unittest discover -v

# Ejecutar un ejercicio específico
python -m unittest tests.test_ej05 -v
```

**Requisito:** Python 3.12+

---

## Cómo entregar

1. Implementá las funciones/clases en `src/ejNN.py`
2. Verificá que los tests pasen localmente
3. Hacé `git add`, `git commit`, `git push`
4. Verificá en la pestaña **Actions** de GitHub que el workflow de autograding pase

**Tu nota se calcula automáticamente** según la cantidad de ejercicios que pasen todos sus tests.

---

## Escala de calificación

| Tests que pasan | Nota |
|----------------|------|
| 20/20 | 10 |
| 18–19 | 9 |
| 16–17 | 8 |
| 14–15 | 7 |
| 12–13 | 6 |
| 10–11 | 5 |
| 8–9 | 4 |
| < 8 | Rehacer |
