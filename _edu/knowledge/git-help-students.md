# Guía de Errores Comunes de Git para Alumnos

> Este documento es la base de conocimiento del auto-responder de GitHub Actions.
> Se instala automáticamente en los repos de GitHub Classroom.

---

## 1. Archivos binarios >1MB

**Síntoma:** Push lento o rechazado. GitHub muestra "Large files detected".

**Causa:** Subiste un archivo compilado (.exe, .jar, .o), un PDF grande, o un ZIP.

**Solución:**
```bash
# Agregar al .gitignore
echo "*.exe" >> .gitignore
echo "*.jar" >> .gitignore
echo "*.zip" >> .gitignore

# Remover del historial (si ya lo commiteaste)
git rm --cached archivo_grande.exe
git commit -m "fix: remover binario del tracking"
git push
```

---

## 2. Push directo a `main`

**Síntoma:** El CI falla porque se esperaba un Pull Request.

**Causa:** Hiciste push directamente a la rama `main` en lugar de usar una branch.

**Solución:**
```bash
# Crear una branch nueva
git checkout -b feature/mi-cambio

# Si ya hiciste el commit en main, moverlo
git checkout main
git reset --soft HEAD~1
git checkout -b feature/mi-cambio
git commit -m "feat: agregar mi cambio"
git push -u origin feature/mi-cambio
# Luego abrir Pull Request en GitHub
```

---

## 3. Build failure (test CI)

**Síntoma:** Los tests automáticos fallan ❌ en el PR.

**Causa:** Tu código no compila o los tests unitarios no pasan.

**Solución:**
1. Leer el log del CI (pestaña "Actions" en GitHub)
2. Correr los tests localmente antes de pushear:
   ```bash
   # Python
   python -m pytest
   # Java
   mvn test
   # Node
   npm test
   ```
3. Fixear los errores y pushear de nuevo al mismo branch

---

## 4. Commit messages vacíos o genéricos

**Síntoma:** El historial de git tiene mensajes como "update", "fix", "asdf", "changes".

**Causa:** No estás describiendo qué hiciste en cada commit.

**Solución:** Usar mensajes descriptivos con el formato:
```
tipo: descripción breve

Ejemplos:
feat: agregar función de ordenamiento burbuja
fix: corregir error de índice en búsqueda binaria
docs: agregar comentarios al módulo de grafos
test: agregar test para caso límite de lista vacía
```

---

## 5. Archivos de IDE

**Síntoma:** Aparecen carpetas `.idea/`, `.vscode/`, archivos `.iml` en el repo.

**Causa:** Tu IDE genera archivos de configuración que son personales, no del proyecto.

**Solución:**
```bash
# Agregar al .gitignore
echo ".idea/" >> .gitignore
echo ".vscode/" >> .gitignore
echo "*.iml" >> .gitignore
echo ".DS_Store" >> .gitignore

# Remover del tracking
git rm -r --cached .idea/ 2>/dev/null
git rm -r --cached .vscode/ 2>/dev/null
git commit -m "fix: remover archivos de IDE del tracking"
```

---

## 6. node_modules/ o .venv/ en el repo

**Síntoma:** El repo pesa decenas de MB. `git status` muestra miles de archivos.

**Causa:** Commiteaste la carpeta de dependencias.

**Solución:**
```bash
# NUNCA commitear dependencias
echo "node_modules/" >> .gitignore
echo ".venv/" >> .gitignore
echo "__pycache__/" >> .gitignore

# Remover del tracking sin borrar de disco
git rm -r --cached node_modules/ 2>/dev/null
git rm -r --cached .venv/ 2>/dev/null
git commit -m "fix: remover dependencias del tracking"
git push
```

**Recuerda:** Las dependencias se instalan con `npm install` o `pip install -r requirements.txt`.

---

## 7. Conflictos de merge no resueltos

**Síntoma:** Archivos con marcadores `<<<<<<<`, `=======`, `>>>>>>>`.

**Causa:** Git no pudo fusionar automáticamente dos versiones del mismo archivo.

**Solución:**
1. Abrir el archivo con conflictos
2. Buscar los marcadores:
   ```
   <<<<<<< HEAD
   tu versión
   =======
   versión del compañero
   >>>>>>> branch-name
   ```
3. Elegir qué versión mantener (o combinar ambas)
4. Borrar los marcadores
5. Guardar, commitear y pushear:
   ```bash
   git add archivo_conflictivo.py
   git commit -m "fix: resolver conflicto de merge en archivo_conflictivo.py"
   git push
   ```

---

## Recursos adicionales

- [Git Handbook (GitHub)](https://docs.github.com/es/get-started/using-git)
- [Oh Shit, Git!?!](https://ohshitgit.com/es)
- [Learn Git Branching (interactivo)](https://learngitbranching.js.org/?locale=es_AR)
