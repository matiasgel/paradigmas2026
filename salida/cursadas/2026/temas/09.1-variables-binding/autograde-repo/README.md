# TP 09.1 — Variables, Binding y Ámbito

**Paradigmas y Lenguajes de Programación 2026 — UNTDF**

Aceptá la asignación en GitHub Classroom y cloná tu repositorio para empezar.

## Cómo trabajar

```bash
git clone <url-de-tu-repo>
cd <nombre-del-repo>
npm install
```

## Ejecutar tests

```bash
npx vitest run             # todos los tests
npx vitest run tests/ej01.test.ts   # ejercicio específico
```

## Entregar

```bash
git add .
git commit -m "feat: resolver ej01 swap"
git push
```

Los tests se ejecutan automáticamente en GitHub Actions con cada `push`.
Verificá el check ✅ en la pestaña **Actions** de tu repositorio.

## Estructura

```
src/          ← Implementar aquí (ej01.ts a ej05.ts)
tests/        ← NO modificar (tests de autograding)
```

## Puntos

| Ejercicio | Tema | Pts |
|-----------|------|-----|
| Ej01 | L-value, R-value y la 5-tupla | 20 |
| Ej02 | Binding de tipos: dimensiones ortogonales | 20 |
| Ej03 | Binding de almacenamiento: closures y recursión | 25 |
| Ej04 | Ámbito estático y algoritmo de resolución | 20 |
| Ej05 | Detectar y corregir errores de binding y ámbito | 15 |
| **Total** | | **100** |
