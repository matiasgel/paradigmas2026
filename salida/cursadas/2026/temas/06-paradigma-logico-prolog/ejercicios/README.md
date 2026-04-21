# Ejercicios Prolog — Clase 1: Paradigma Lógico
**Paradigmas y Lenguajes de Programación 2026 — UNTdF**

---

## Instalación de SWI-Prolog

### Windows

1. Descargar el instalador desde: https://www.swi-prolog.org/download/stable  
   Elegir **Windows 64-bit installer (.exe)**

2. Ejecutar el instalador. Durante la instalación:
   - Dejar marcada la opción **"Add SWI-Prolog to PATH"**
   - Instalar en la ruta por defecto (`C:\Program Files\swipl\`)

3. Verificar la instalación abriendo una terminal (PowerShell o CMD):
   ```
   swipl --version
   ```
   Debe mostrar algo como: `SWI-Prolog version 9.x.x`

---

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install swi-prolog
```

Verificar:
```bash
swipl --version
```

**Para otras distros:**
- Fedora/RHEL: `sudo dnf install pl`
- Arch: `sudo pacman -S swi-prolog`
- O compilar desde fuente: https://www.swi-prolog.org/build/unix.html

---

## Configuración en Visual Studio Code

### 1. Instalar la extensión VSC-Prolog

1. Abrir VS Code
2. Ir a **Extensiones** (`Ctrl+Shift+X`)
3. Buscar: `VSC-Prolog`
4. Instalar la extensión de **Arthur Wang** (identificador: `arthurwang.vsc-prolog`)

### 2. Configurar la ruta de SWI-Prolog

Abrir la configuración de VS Code (`Ctrl+,`) y buscar `prolog.executablePath`.

**Windows** — agregar en `settings.json`:
```json
{
  "prolog.executablePath": "C:\\Program Files\\swipl\\bin\\swipl.exe"
}
```

**Linux** — agregar en `settings.json`:
```json
{
  "prolog.executablePath": "/usr/bin/swipl"
}
```

Para abrir `settings.json` directamente: `Ctrl+Shift+P` → `Open User Settings (JSON)`

### 3. Verificar que funciona

1. Abrir el archivo `ejercicios-clase1.pl` en VS Code
2. Debería aparecer coloreo de sintaxis (azul para predicados, verde para comentarios)
3. Errores de sintaxis se marcan con línea roja debajo

---

## Uso: correr ejercicios en VS Code

### Opción A — Terminal integrada (recomendada)

1. Abrir terminal en VS Code: `Ctrl+ñ` (o `Ctrl+`` ` ``)
2. Navegar a la carpeta del archivo:
   ```bash
   cd ruta/al/archivo
   ```
3. Iniciar SWI-Prolog con el archivo cargado:
   ```bash
   swipl -l ejercicios-clase1.pl
   ```
4. Se abre el intérprete `?-`. Escribir consultas:
   ```prolog
   ?- madre(ana, X).
   ?- abuelo(jorge, laura).
   ?- findall(X, hermano(carlos, X), L).
   ```
5. Para salir: `halt.` o `Ctrl+D`

### Opción B — Run on Save (extensión VSC-Prolog)

La extensión puede ejecutar el archivo automáticamente al guardarlo.  
Activar en `settings.json`:
```json
{
  "prolog.linter.run": "onSave"
}
```

### Opción C — Sin instalación (SWISH online)

Si no podés instalar SWI-Prolog, usá el entorno online:  
🔗 https://swish.swi-prolog.org/

1. Abrir SWISH en el navegador
2. Copiar el contenido de `ejercicios-clase1.pl` en el panel izquierdo
3. Escribir consultas en el panel derecho
4. Presionar **Enter** para ejecutar

---

## Flujo de trabajo recomendado

```
1. Abrir ejercicios-clase1.pl en VS Code
2. Leer el enunciado del ejercicio (comentario %---)
3. Completar la regla donde dice "% completar aquí"
4. Guardar el archivo (Ctrl+S)
5. En la terminal: swipl -l ejercicios-clase1.pl
6. Probar las consultas de verificación del ejercicio
7. Usar ; para pedir más soluciones cuando aparece una respuesta
```

---

## Comandos útiles del intérprete

| Comando | Acción |
|---------|--------|
| `?- halt.` | Salir del intérprete |
| `?- consult('archivo.pl').` | Cargar un archivo |
| `?- listing(predicado/aridad).` | Ver la definición de un predicado |
| `?- trace.` | Activar el trazador paso a paso |
| `?- notrace.` | Desactivar el trazador |
| `Ctrl+C` → `a` | Interrumpir una consulta colgada |

### Ejemplo de uso de trace (Ejercicio 11):
```prolog
?- trace.
?- abuelo(jorge, laura).
% Prolog muestra cada paso de la resolución
```

---

## Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `ERROR: Unknown procedure` | El predicado no está definido | Verificar que el archivo está cargado con `consult` |
| `ERROR: Syntax error` | Falta `.` al final de un hecho/regla | Agregar `.` al final de cada cláusula |
| `false` en lugar de `true` | Prolog no encuentra prueba | Verificar nombre y aridad del predicado |
| Bucle infinito (no termina) | Recursión sin caso base primero | Ver Ejercicio 19 — el orden importa |
| `swipl: command not found` | SWI-Prolog no está en el PATH | Reinstalar marcando "Add to PATH" |
