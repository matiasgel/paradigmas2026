# Retrospectiva Sprint 3 — E6: Agentes downstream

**Sprint:** 3
**Epic:** E6 — Agentes downstream
**Fecha:** 2026-05-23
**Stories completadas:** 6.1, 6.2, 6.3, 6.4 (4/4)

---

## Qué salió bien

- **Patrón brownfield verificado:** Agregar la sección v3 DESPUÉS del tag `</agent>` resultó en la estrategia más segura. El XML original queda intacto y la lógica v3 es puro Markdown separado con `---`.
- **Condicional doble obligatorio:** El patrón "topic-extract.md EXISTS AND checkpoint_2_aprobado: true" es correcto. Una condición sola no sería suficiente (podrían existir topic-extract.md sin aprobar).
- **Task file de backup centralizado:** `tasks/backup-v2-artifacts.md` documenta el protocolo idempotente de backup en un único lugar. Cada agente referencia el mismo protocolo.
- **create-teacher-guide es workflow, no agente:** Se detectó correctamente que el archivo es un workflow. La lógica v3 fue añadida al workflow.md correctamente.

## Decisiones de diseño notables

- **Idempotencia del backup:** Si el backup ya existe → no reemplazarlo. Esto protege la versión original v2 aunque se ejecute el pipeline v3 múltiples veces.
- **Nivel de densidad en downstream agents:** Se implementó la lectura de `nivel` desde `.pipeline-v3-state.yaml` en todos los agentes, no solo en el workflow.

## Qué se mejoraría

- La sección v3 de `create-teacher-guide/workflow.md` es menos detallada que la de los agentes. En una siguiente iteración podría incluir el pseudocódigo de verificación explícito.

## Deuda técnica

- La lógica de lectura de `filminas-base-acciones.yaml` en class-writer.md se documenta en S5.3 pero no está explícitamente en la sección v3 del agente. Podría completarse en una iteración futura.
