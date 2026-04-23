# Workflow: Exportar repo EDU a GitHub

**Module:** edu
**Phase:** anytime
**Owner Agent:** course-planner, agent

---

## Propósito

Exportar el módulo `edu-standalone` completo como un repositorio GitHub independiente listo para un curso nuevo. El repo debe contener la última versión de agentes, scripts, workflows, templates y configuraciones del módulo EDU.

## ¿Qué hace?

1. Consulta si el repo existe en GitHub.
2. Crea el repo si no existe.
3. Copia todo el contenido de `salida/edu-standalone` a un repositorio nuevo.
4. Inicializa Git, commitea y empuja la rama `main` al repositorio GitHub.
5. Reporta la URL del repo creado.

## Uso

```
python scripts/export_repo.py --repo judiciales2026ush --visibility public --description "Curso Judiciales 2026 USh"
```

## Requisitos

- GitHub CLI (`gh`) autenticado con el usuario correcto.
- Permisos `repo` en GitHub.
- Acceso de escritura al directorio actual.

## Output

- `https://github.com/{usuario}/{repo}`

## Nota

Este workflow produce un repo independiente con el contenido de `edu-standalone` como raíz. Es ideal para usar como base de un curso nuevo y mantener el historial del módulo EDU separado del repo original.
