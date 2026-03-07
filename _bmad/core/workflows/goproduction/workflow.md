---
name: goproduction
description: Deploy edu-standalone to the 'production' git branch. Preserves all runtime outputs across deploy cycles.
standalone_source: '{project-root}/salida/edu-standalone'
target_branch: 'production'
---

# Go to Production

**Goal:** Desplegar la última versión de `salida/edu-standalone/` a la rama `production` de git para pruebas reales. Cada deploy pisa los archivos del módulo pero **nunca toca** los outputs generados durante el testing.

---

## REGLAS CRÍTICAS — SIN EXCEPCIONES

- 🛡️ **NUNCA** eliminar en rama production: `_edu-memory/`, `salida/cursadas/`
- 🛡️ **NUNCA** sobreescribir `_edu/config.yaml` si ya existe en production
- 🛡️ **NUNCA** usar `--force` en git
- ✅ **SIEMPRE** mostrar preview antes de ejecutar
- ✅ **SIEMPRE** pedir confirmación explícita
- ✅ Comunicar en `{communication_language}`

---

## SECUENCIA DE EJECUCIÓN

### 1. Pre-flight: Estado actual

Ejecutar y mostrar resultados al usuario:

```bash
cd {project-root}
CURRENT_BRANCH=$(git branch --show-current)
GIT_DIRTY=$(git status --porcelain | wc -l | tr -d ' ')

echo "=== GIT STATE ==="
echo "Rama actual:            $CURRENT_BRANCH"
echo "Archivos sin commitear: $GIT_DIRTY"

if git show-ref --verify --quiet refs/heads/production; then
  echo "Rama 'production':      EXISTE"
  echo "Último commit:          $(git log production --oneline -1)"
else
  echo "Rama 'production':      NO EXISTE → será creada desde $CURRENT_BRANCH"
fi

echo ""
echo "=== FUENTE (edu-standalone) ==="
echo "Agentes _edu:      $(ls salida/edu-standalone/_edu/agents/ 2>/dev/null | wc -l)"
echo "Workflows _edu:    $(ls salida/edu-standalone/_edu/workflows/ 2>/dev/null | wc -l)"
echo "Agent files .github: $(ls salida/edu-standalone/.github/agents/edu-*.agent.md 2>/dev/null | wc -l)"
echo "Prompt files .github: $(ls salida/edu-standalone/.github/prompts/edu-*.prompt.md 2>/dev/null | wc -l)"

echo ""
echo "=== PRODUCCIÓN A PRESERVAR (en rama production) ==="
if git show-ref --verify --quiet refs/heads/production; then
  git show production:_edu/config.yaml > /dev/null 2>&1 \
    && echo "  ✅ _edu/config.yaml EXISTS — será preservada" \
    || echo "  ℹ️  _edu/config.yaml no existe (se copiará del standalone)"
  git ls-tree production _edu-memory > /dev/null 2>&1 \
    && echo "  ✅ _edu-memory/ EXISTS — será preservada" \
    || echo "  ℹ️  _edu-memory/ no existe aún (se crea en runtime)"
  git ls-tree production salida/cursadas > /dev/null 2>&1 \
    && echo "  ✅ salida/cursadas/ EXISTS — será preservada" \
    || echo "  ℹ️  salida/cursadas/ no existe aún (se crea al usar el módulo)"
else
  echo "  ℹ️  (primer deploy — la rama no existe todavía)"
fi
```

### 2. Presentar plan de deploy

Mostrar la siguiente tabla al usuario:

**🚀 Go to Production — Plan de deploy a rama `production`:**

| Acción | Qué | Fuente |
|--------|-----|--------|
| SINCRONIZAR | `.github/` completo en production | rama de trabajo actual |
| REEMPLAZAR | `_edu/agents/` en production | `salida/edu-standalone/_edu/agents/` |
| REEMPLAZAR | `_edu/workflows/` en production | `salida/edu-standalone/_edu/workflows/` |
| REEMPLAZAR | `_edu/module-help.csv` en production | `salida/edu-standalone/_edu/module-help.csv` |
| REEMPLAZAR | `.github/agents/edu-*.agent.md` en production | `salida/edu-standalone/.github/agents/` |
| REEMPLAZAR | `.github/prompts/edu-*.prompt.md` en production | `salida/edu-standalone/.github/prompts/` |
| ACTUALIZAR | Bloque EDU en `.github/copilot-instructions.md` | `salida/edu-standalone/.github/copilot-instructions.md` |
| ⏭️ PRESERVAR | `_edu/config.yaml` | si ya existe en production |
| 🛡️ PRESERVAR | `_edu-memory/` | siempre |
| 🛡️ PRESERVAR | `salida/cursadas/` | siempre |

### 3. Confirmación

**"¿Deployar a rama `production`? [S] Sí [N] Cancelar"**

- 🛑 HALT y esperar input del usuario
- IF N → "Deploy cancelado. No se realizaron cambios." — fin del workflow
- IF S → continuar al paso 4

### 4. Ejecutar deploy

#### 4.0 — Setup worktree

```bash
cd {project-root}
CURRENT_BRANCH=$(git branch --show-current)
WORKTREE_PATH="/tmp/edu-production-deploy"

# Limpiar worktree anterior si quedó colgado
git worktree remove "$WORKTREE_PATH" --force 2>/dev/null || true
rm -rf "$WORKTREE_PATH" 2>/dev/null || true

# Crear worktree apuntando a production (o crearla desde HEAD)
if git show-ref --verify --quiet refs/heads/production; then
  git worktree add "$WORKTREE_PATH" production
  echo "✅ Worktree abierto en $WORKTREE_PATH (rama production existente)"
else
  git worktree add -b production "$WORKTREE_PATH" HEAD
  echo "✅ Rama 'production' CREADA desde $CURRENT_BRANCH — worktree en $WORKTREE_PATH"
fi
```

#### 4.0.5 — Sync `.github/` desde rama de trabajo (excepto agents/)

```bash
cd "$WORKTREE_PATH"
# Sync todo .github/ EXCEPTO agents/ (los agentes los pone el standalone en 4.5)
git checkout $CURRENT_BRANCH -- .github/prompts/
git checkout $CURRENT_BRANCH -- .github/workflows/
git checkout $CURRENT_BRANCH -- .github/copilot-instructions.md 2>/dev/null || true
# Limpiar agentes BMAD que pudieran haber quedado de deploys anteriores
rm -f "$WORKTREE_PATH/.github/agents/bmad-"*.agent.md
echo "✅ .github/ sincronizado desde $CURRENT_BRANCH (agents/ excluido — solo edu-*)"
```

#### 4.1 — Deploy `_edu/agents/`

```bash
rm -rf "$WORKTREE_PATH/_edu/agents"
mkdir -p "$WORKTREE_PATH/_edu"
cp -r salida/edu-standalone/_edu/agents "$WORKTREE_PATH/_edu/agents"
echo "✅ _edu/agents/ → $(ls $WORKTREE_PATH/_edu/agents/ | wc -l) archivos"
```

#### 4.2 — Deploy `_edu/workflows/`

```bash
rm -rf "$WORKTREE_PATH/_edu/workflows"
cp -r salida/edu-standalone/_edu/workflows "$WORKTREE_PATH/_edu/workflows"
echo "✅ _edu/workflows/ → $(ls $WORKTREE_PATH/_edu/workflows/ | wc -l) carpetas"
```

#### 4.3 — Deploy `_edu/module-help.csv`

```bash
cp salida/edu-standalone/_edu/module-help.csv "$WORKTREE_PATH/_edu/module-help.csv"
echo "✅ _edu/module-help.csv actualizado"
```

#### 4.4 — Deploy `_edu/config.yaml` (solo primer deploy)

```bash
if [ ! -f "$WORKTREE_PATH/_edu/config.yaml" ]; then
  cp salida/edu-standalone/_edu/config.yaml "$WORKTREE_PATH/_edu/config.yaml"
  echo "✅ _edu/config.yaml copiado del standalone (primer deploy)"
else
  echo "⏭️  _edu/config.yaml PRESERVADO — ya estaba configurado"
fi
```

#### 4.5 — Deploy `.github/agents/edu-*`

```bash
mkdir -p "$WORKTREE_PATH/.github/agents"
rm -f "$WORKTREE_PATH/.github/agents/edu-"*.md
cp salida/edu-standalone/.github/agents/edu-*.agent.md "$WORKTREE_PATH/.github/agents/"
echo "✅ .github/agents/ edu-* → $(ls $WORKTREE_PATH/.github/agents/edu-*.agent.md | wc -l) archivos"
```

#### 4.6 — Deploy `.github/prompts/edu-*`

```bash
mkdir -p "$WORKTREE_PATH/.github/prompts"
rm -f "$WORKTREE_PATH/.github/prompts/edu-"*.prompt.md
cp salida/edu-standalone/.github/prompts/edu-*.prompt.md "$WORKTREE_PATH/.github/prompts/"
echo "✅ .github/prompts/ edu-* → $(ls $WORKTREE_PATH/.github/prompts/edu-*.prompt.md | wc -l) archivos"
```

#### 4.7 — Actualizar bloque EDU en `copilot-instructions.md`

```bash
if [ -f "$WORKTREE_PATH/.github/copilot-instructions.md" ]; then
  sed -i '/<!-- EDU:START -->/,/<!-- EDU:END -->/d' "$WORKTREE_PATH/.github/copilot-instructions.md"
fi
echo "" >> "$WORKTREE_PATH/.github/copilot-instructions.md"
cat salida/edu-standalone/.github/copilot-instructions.md >> "$WORKTREE_PATH/.github/copilot-instructions.md"
echo "✅ copilot-instructions.md — bloque EDU actualizado"
```

#### 4.8 — Commit a rama `production`

```bash
cd "$WORKTREE_PATH"
git add -A
DEPLOY_DATE=$(date +"%Y-%m-%d %H:%M")
git commit -m "deploy: edu-standalone → production [$DEPLOY_DATE]" --allow-empty
echo "✅ Commit realizado:"
git log --oneline -1
```

#### 4.9 — Cleanup worktree

```bash
cd {project-root}
git worktree remove "$WORKTREE_PATH"
echo "✅ Worktree eliminado — seguís en rama: $(git branch --show-current)"
```

### 5. Reporte final

Ejecutar y mostrar:

```bash
cd {project-root}
echo "=== DEPLOY COMPLETADO ==="
echo "  Rama: production"
echo "  Últimos commits:"
git log production --oneline -3
echo ""
echo "=== PRODUCCIÓN PRESERVADA ==="
git show production:_edu-memory/ > /dev/null 2>&1 \
  && echo "  ✅ _edu-memory/" \
  || echo "  ℹ️  _edu-memory/ (se creará al usar el módulo)"
git show production:salida/cursadas/ > /dev/null 2>&1 \
  && echo "  ✅ salida/cursadas/" \
  || echo "  ℹ️  salida/cursadas/ (se creará al usar el módulo)"
git show production:_edu/config.yaml > /dev/null 2>&1 \
  && echo "  ✅ _edu/config.yaml preservada"
```

Mostrar al usuario:

"**✅ Deploy completado en rama `production`. Hacé `git checkout production` para probar.**"

"**Ciclo de mejora:** editá en `salida/edu-standalone/` → `/goproduction` → `git checkout production` → probá → `git checkout main` → repetí."

---

## Ciclo de mejora continua

```
salida/edu-standalone/     ← fuente de verdad (editar aquí, en main/develop)
        │
        │  /goproduction   (usa git worktree — no cambia tu rama actual)
        ▼
  rama: production          ← instancia de prueba (git checkout production)
  ├── _edu/agents/          ← REEMPLAZADO en cada deploy
  ├── _edu/workflows/       ← REEMPLAZADO en cada deploy
  ├── _edu/module-help.csv  ← REEMPLAZADO en cada deploy
  ├── _edu/config.yaml      ← PRESERVADO después del primer deploy
  ├── _edu-memory/          ← NUNCA TOCADO (acumula entre deploys)
  └── salida/cursadas/      ← NUNCA TOCADO (producción real)
```

---

## Success Metrics

✅ Rama `production` existe con el último commit de deploy
✅ `_edu/agents/`, `_edu/workflows/`, `_edu/module-help.csv` actualizados
✅ `.github/agents/edu-*` y `.github/prompts/edu-*` actualizados
✅ Bloque EDU en `copilot-instructions.md` reemplazado
✅ `_edu/config.yaml`, `_edu-memory/`, `salida/cursadas/` PRESERVADOS
✅ La rama de trabajo actual no fue modificada
✅ `_edu-memory/`, `salida/cursadas/`, `material/` sin modificar
