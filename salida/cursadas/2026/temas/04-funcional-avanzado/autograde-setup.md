# Guía de Publicación — GitHub Classroom Autograding
## Tema 04: Aspectos Avanzados de Programación Funcional

> **Este archivo es solo para el docente.** NO sube al repo template ni es visible para los alumnos.

---

## Paso 1: Crear el Template Repo en GitHub

1. Ir a github.com → New repository
2. Nombre: `tp04-funcional-avanzado-template`
3. Visibilidad: **Private** (recomendado)
4. Subir el contenido de `autograde-repo/`:
   ```bash
   cd salida/cursadas/2026/temas/04-funcional-avanzado/autograde-repo
   git init
   git add .
   git commit -m "Initial template — TP04 Funcional Avanzado"
   git remote add origin https://github.com/<tu-org>/tp04-funcional-avanzado-template.git
   git push -u origin main
   ```
5. En Settings del repo → marcar ✅ **"Template repository"**

## Paso 2: Crear el Assignment en GitHub Classroom

1. Ir a classroom.github.com → tu aula → **New Assignment**
2. Tipo: **Individual**
3. Título: "TP 04 — Aspectos Avanzados de Programación Funcional"
4. Template repository: buscar `tp04-funcional-avanzado-template`
5. Fecha límite: configurar según el cursado
6. Autograding: el `classroom.yml` en el template se activa automáticamente con cada push del alumno
   - Opcionalmente, ir a "Grading and feedback" para revisar o ajustar tests vía la UI
   - Para usar presets UI: seleccionar "Add autograding test" → los tests del `autograding.json` sirven como guía
7. Copiar el **Assignment Link** y compartirlo con los alumnos

## Paso 3: Monitoreo

- Panel de classroom.github.com → ver progreso por alumno en tiempo real
- Los tests corren automáticamente en cada push (y manualmente si se configura `workflow_dispatch`)
- Ver logs individuales: Assignments → alumno → ícono de checklist → GitHub Actions logs
- Descargar CSV con puntajes: botón "Download" en la página del assignment

## Requisitos del runner (ubuntu-latest)

El workflow instala automáticamente:
- **Node.js 20** + npm (para TypeScript/Vitest)
- **Java 21 Temurin** + Leiningen (para Clojure)
- Dependencias: `npm install` y `lein deps`

No se requiere configuración adicional.

## Trazabilidad de tests → consignas

| Test | Consigna tp.md | Filminas | Lenguaje | Puntos |
|------|----------------|----------|----------|--------|
| ej01 | Ejercicio 1 — Pipeline filter/map/reduce | F-06,07,08 | TypeScript | 3 |
| ej02 | Ejercicio 2 — Composición pipe/compose | F-09 | TypeScript | 5 |
| ej03 | Ejercicio 3 — Inmutabilidad | F-05,10 | TypeScript | 3 |
| ej04 | Ejercicio 4 — Pipeline ->> | F-12 | Clojure | 3 |
| ej05 | Ejercicio 5 — Secuencias perezosas | F-11 | Clojure | 5 |
| ej06 | Ejercicio 6 — Colecciones persistentes | F-13 | Clojure | 3 |
| ej07 | Ejercicio 7 — ADT tipo suma | F-14 | TypeScript | 5 |
| ej08 | Ejercicio 8 — Result\<T,E\> | F-15,16 | TypeScript | 6 |
| ej09 | Ejercicio 9 — Maybe/Option | F-17 | TypeScript | 5 |
| ej10 | Ejercicio 10 — Errores como datos | F-18 | Clojure | 5 |
| ej11 | Ejercicio 11 — Transducer básico | F-19,20 | Clojure | 5 |
| ej12 | Ejercicio 12 — Transducer vs pipeline | F-21 | Clojure | 5 |
| ej13 | Ejercicio 13 — API genérica funcional | F-22 | TypeScript | 7 |
| ej14 | Ejercicio 14 — HOF | F-23 | TypeScript | 5 |
| ej15 | Ejercicio 15 — core.async canales | F-26,27 | Clojure | 6 |
| ej16 | Ejercicio 16 — STM transacciones | F-28 | Clojure | 6 |
| ej17 | Ejercicio 17 — async/await | F-30,31 | TypeScript | 5 |
| ej18 | Ejercicio 18 — Separar efectos puros | F-32 | TypeScript | 5 |
| ej19 | Ejercicio 19 — Integrador TypeScript | F-35,36 | TypeScript | 6 |
| ej20 | Ejercicio 20 — Integrador Clojure | F-37 | Clojure | 7 |
| | | | **Total** | **100** |
