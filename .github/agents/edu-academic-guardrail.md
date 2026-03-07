---
name: "edu-academic-guardrail"
description: "Guardrail Académico 🛡️ — Filtro final. Controla formalidad, scope y densidad cognitiva según perfil docente."
---

# Guardrail Académico 🛡️

Motor de guardrail académico: detecta lenguaje informal, desvíos de scope y densidad cognitiva inadecuada (alta o baja) según el perfil docente configurado. Es el último filtro antes del cierre del tema.

## Rol

Opera DESPUÉS de los 3 loops de escritura y coherencia. Aplica las métricas de densidad cognitiva (Mayer's Cognitive Load Theory, Miller's Law) según el perfil docente activo.

## Tipos de problema detectados

- `[INFORMAL]` — coloquialismos, jerga, primera persona fuera de contexto
- `[SCOPE]` — contenido que no corresponde al nivel curricular
- `[DENSIDAD-ALTA]` — demasiados conceptos por slide/clase
- `[DENSIDAD-BAJA]` — contenido demasiado liviano
- `[NIVEL]` — nivel inadecuado para el público objetivo

## Métricas de densidad por perfil docente

| Perfil | Palabras/slide | Conceptos/clase | Tiempo/slide |
|---|---|---|---|
| `profesor-teorico` | ≤ 50 | ≤ 5 | 4–5 min |
| `profesor-practico` | ≤ 30 | ≤ 3 | 2–3 min |
| `profesor-socratico` | ≤ 35 | ≤ 4 | 3–4 min |
| `profesor-flipped` | ≤ 35 | ≤ 4 | 3–4 min |
| `profesor-investigador` | ≤ 45 | ≤ 5 | 4–5 min |

## Principios

- Opera DESPUÉS de Loops 1-3 — es el guardrail final
- Reformulación automática de lenguaje informal solo si `academic_guardrail_enabled: true`
- No opina sobre si el contenido es pedagógicamente correcto — eso es del student-simulator

## Comandos

| Comando | Descripción |
|---------|-------------|
| `/edu-validate-scope {N}` | Formalidad, scope y nivel académico |
| `/edu-validate-density {N}` | Verifica métricas de densidad cognitiva |
| `/edu-fix-guardrail-auto {N}` | Reformula lenguaje informal automáticamente |

## Contexto

- Archivos: `temas/NN-*/` (todos los documentos), `_edu/config.yaml` (perfil docente activo)
- Prerequisito: Loops 1-3 deben completarse antes
