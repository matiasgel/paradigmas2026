# Guía de Publicación — Autograde Repo TP N° 2

> ⚠️ **Este archivo es SOLO para el docente.** No debe subirse al repo template ni ser visible para los alumnos.

---

## Trazabilidad consignas ↔ tests

| Ejercicio | Archivo implementación | Archivo test | Puntos | Consigna |
|-----------|----------------------|--------------|--------|---------|
| 01 | `src/ej01.py` | `tests/test_ej01.py` | 5 | `es_par` — aserciones básicas |
| 02 | `src/ej02.py` | `tests/test_ej02.py` | 5 | `invertir_cadena` |
| 03 | `src/ej03.py` | `tests/test_ej03.py` | 5 | `maximo_de_tres` |
| 04 | `src/ej04.py` | `tests/test_ej04.py` | 5 | `contar_vocales` |
| 05 | `src/ej05.py` | `tests/test_ej05.py` | 5 | `es_palindromo` |
| 06 | `src/ej06.py` | `tests/test_ej06.py` | 5 | `dividir` + `assertRaises` |
| 07 | `src/ej07.py` | `tests/test_ej07.py` | 5 | `validar_edad` — múltiples rangos |
| 08 | `src/ej08.py` | `tests/test_ej08.py` | 5 | `Pila` con excepciones propias |
| 09 | `src/ej09.py` | `tests/test_ej09.py` | 5 | `calcular_descuento` — boundary testing |
| 10 | `src/ej10.py` | `tests/test_ej10.py` | 5 | `validar_contrasenia` |
| 11 | `src/ej11.py` | `tests/test_ej11.py` | 5 | `Contador` con `setUp` (TDD) |
| 12 | `src/ej12.py` | `tests/test_ej12.py` | 5 | `ListaOrdenada` con fixtures |
| 13 | `src/ej13.py` | `tests/test_ej13.py` | 5 | `CuentaBancaria` (TDD) |
| 14 | `src/ej14.py` | `tests/test_ej14.py` | 5 | `ConversorTemperatura` + `assertAlmostEqual` |
| 15 | `src/ej15.py` | `tests/test_ej15.py` | 5 | `Agenda` — integrador módulo |
| 16 | `src/ej16.py` | `tests/test_ej16.py` | 5 | Mock de archivos con `patch` |
| 17 | `src/ej17.py` | `tests/test_ej17.py` | 5 | Mock servicio externo con `MagicMock` |
| 18 | `src/ej18.py` | `tests/test_ej18.py` | 5 | `Notificador` con `@patch` |
| 19 | `src/ej19.py` | `tests/test_ej19.py` | 5 | `Calculadora` con `subTest` (TDD) |
| 20 | `src/ej20.py` | `tests/test_ej20.py` | 5 | `GestorTareas` — integrador final |
| **Total** | | | **100** | |

---

## Pasos para publicar en GitHub Classroom

### 1. Crear el repo template en GitHub

1. Ir a [github.com/new](https://github.com/new)
2. Nombre sugerido: `tp-02-pruebas-unitarias-template`
3. Marcar como **privado**
4. Subir el contenido de `autograde-repo/`:
   ```bash
   cd autograde-repo/
   git init
   git add .
   git commit -m "Initial template"
   git remote add origin https://github.com/<org>/tp-02-pruebas-unitarias-template.git
   git push -u origin main
   ```
5. En Settings del repo → marcar **"Template repository"**

### 2. Crear el Assignment en GitHub Classroom

1. Ir a [classroom.github.com](https://classroom.github.com)
2. Seleccionar la clase IF009-2026
3. Clic en **"New Assignment"**
4. Configurar:
   - **Title:** TP N° 2 — Pruebas Unitarias
   - **Deadline:** Semana 6
   - **Repository visibility:** Private
   - **Template repository:** `tp-02-pruebas-unitarias-template`
5. En **Grading and feedback → Add autograding tests**:
   - Usar los presets de `autograding.json` como referencia
   - O dejar que el `classroom.yml` maneje el autograding (recomendado)
6. Copiar el link del assignment y publicar en el aula virtual

### 3. Verificar el autograding

1. Aceptar la asignación con una cuenta de prueba
2. Hacer un `push` con las soluciones implementadas
3. Verificar que todos los pasos del workflow pasen en la pestaña **Actions**
4. Confirmar que la nota aparece en el dashboard de GitHub Classroom
