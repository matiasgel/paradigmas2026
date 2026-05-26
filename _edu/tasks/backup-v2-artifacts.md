# Task: Backup de artefactos v2 antes de sobrescribir
# Usado por: class-writer (v3), study-guide-writer (v3), create-teacher-guide (v3)
# Activación: solo en modo v3 (topic-extract.md EXISTS AND checkpoint_2_aprobado: true)

---

## Propósito

Garantizar que los artefactos producidos por el pipeline v2 se preservan como backup antes de que el pipeline v3 los sobrescriba. Esto implementa AD-05 (Política de coexistencia de artefactos) de la arquitectura.

---

## Protocolo de backup (ejecutar antes de cada sobrescritura v3)

### Verificación previa al backup

```
PARA CADA artefacto en [filminas.md, minuta.md, guia-estudio.md, guiaprofesor.md]:
  SI el artefacto existe en {topic_folder}/:
    1. Verificar si ya existe {artefacto}-v2-backup.md
    2. SI ya existe el backup: NO volver a crear (idempotente)
    3. SI no existe: copiar {artefacto} → {artefacto}-v2-backup.md
    4. Informar al docente: "✅ Backup creado: {topic_folder}/{artefacto}-v2-backup.md"
```

### Tabla de mappings

| Artefacto v2 | Backup v3 | Notas |
|---|---|---|
| `filminas.md` | `filminas-v2-backup.md` | Filminas generadas por pipeline v2 |
| `minuta.md` | `minuta-v2-backup.md` | Minuta generada por pipeline v2 |
| `guia-estudio.md` | `guia-estudio-v2-backup.md` | Guía de estudio generada por pipeline v2 |
| `guiaprofesor.md` | `guiaprofesor-v2-backup.md` | Guía docente generada por pipeline v2 |
| `diseno.md` | NO aplica | No es generado por v3 |
| `topic-extract.md` | NO aplica | Nuevo en v3, sin equivalente v2 |
| `.pipeline-v3-state.yaml` | NO aplica | Nuevo en v3, sin equivalente v2 |

---

## Implementación en cada agente

### class-writer (Roberto) — v3

Antes de escribir `filminas.md` y `minuta.md`:
```
# Backup protocol
if exists("{topic_folder}/filminas.md") and not exists("{topic_folder}/filminas-v2-backup.md"):
    copy "{topic_folder}/filminas.md" → "{topic_folder}/filminas-v2-backup.md"
    inform: "✅ Backup: filminas-v2-backup.md creado"

if exists("{topic_folder}/minuta.md") and not exists("{topic_folder}/minuta-v2-backup.md"):
    copy "{topic_folder}/minuta.md" → "{topic_folder}/minuta-v2-backup.md"
    inform: "✅ Backup: minuta-v2-backup.md creado"
```

### study-guide-writer (Sofía) — v3

Antes de escribir `guia-estudio.md`:
```
if exists("{topic_folder}/guia-estudio.md") and not exists("{topic_folder}/guia-estudio-v2-backup.md"):
    copy "{topic_folder}/guia-estudio.md" → "{topic_folder}/guia-estudio-v2-backup.md"
    inform: "✅ Backup: guia-estudio-v2-backup.md creado"
```

### create-teacher-guide (Roberto) — v3

Antes de escribir `guiaprofesor.md`:
```
if exists("{topic_folder}/guiaprofesor.md") and not exists("{topic_folder}/guiaprofesor-v2-backup.md"):
    copy "{topic_folder}/guiaprofesor.md" → "{topic_folder}/guiaprofesor-v2-backup.md"
    inform: "✅ Backup: guiaprofesor-v2-backup.md creado"
```

---

## Restauración manual (si es necesario)

Si el docente quiere volver a los artefactos v2:
```
mv {topic_folder}/filminas-v2-backup.md {topic_folder}/filminas.md
mv {topic_folder}/minuta-v2-backup.md {topic_folder}/minuta.md
mv {topic_folder}/guia-estudio-v2-backup.md {topic_folder}/guia-estudio.md
mv {topic_folder}/guiaprofesor-v2-backup.md {topic_folder}/guiaprofesor.md
```

---

## Idempotencia

- El protocolo de backup es idempotente: si el backup ya existe, NO se reemplaza.
- Esto protege el backup original de v2 incluso si se ejecuta el pipeline v3 múltiples veces sobre el mismo tema.
