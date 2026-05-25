# Retrospectiva Sprint 4 — E4: Niveles de densidad

**Sprint:** 4
**Epic:** E4 — Niveles de densidad
**Fecha:** 2026-05-23
**Stories completadas:** 4.1, 4.2, 4.3 (3/3)

---

## Qué salió bien

- **Cero duplicación:** Los modificadores de densidad se implementaron una sola vez en `tasks/density-levels.md` y se referencian desde los agentes. No hay lógica duplicada.
- **Taxonomía Bloom alineada:** La tabla N1/N2/N3 está alineada con los niveles de Bloom (Recordar→Comprender→Aplicar→Analizar→Evaluar). Coherencia pedagógica.
- **nivel_minimo en schema:** El campo opcional en `conceptos-clave` permite que el pipeline seleccione automáticamente qué conceptos incluir según el nivel, sin intervención del docente.
- **Coherencia filminas/guía:** Ambos agentes leen el mismo `nivel` del state file → mismo nivel de profundidad sin configuración adicional.

## Decisiones de diseño notables

- **Nivel 2 como default:** Si `--nivel` no se especifica → nivel 2 (Estándar). Evita contenido extremadamente básico o extremadamente denso sin intención explícita.
- **nivel_minimo no requerido:** El campo es `nullable: true, default: 1`, lo que significa que la mayoría de conceptos son para todos los niveles y solo los avanzados se marcan explícitamente.

## Qué se mejoraría

- El mecanismo de `nivel_minimo` en la generación de filminas de class-writer podría ser más explícito: el agent debe filtrar los conceptos del topic-extract.md por nivel_minimo ≤ nivel actual.

## Deuda técnica

- Ninguna crítica.
