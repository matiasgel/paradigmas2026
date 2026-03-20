# activate-env.ps1 — Activa el entorno local de herramientas EDU
# Uso: . .\activate-env.ps1
# (el punto inicial es importante para que las variables de PATH persistan en la sesión actual)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvScripts = Join-Path $root ".venv\Scripts"

# Activar el venv de Python
& "$venvScripts\Activate.ps1"

# Asegurar que pandoc y tectonic estén en PATH (ya están en .venv\Scripts\)
if (-not ($env:PATH -like "*$venvScripts*")) {
    $env:PATH = "$venvScripts;$env:PATH"
}

# Exportar ruta del pandoc de pypandoc_binary al PATH de pandoc
$pandocBin = & python -c "import pypandoc; import os; print(os.path.dirname(pypandoc.get_pandoc_path()))" 2>$null
if ($pandocBin -and -not ($env:PATH -like "*$pandocBin*")) {
    $env:PATH = "$pandocBin;$env:PATH"
}

Write-Host "✅ Entorno EDU activado"
Write-Host "   pandoc  : $(& pandoc --version 2>&1 | Select-Object -First 1)"
Write-Host "   tectonic: $(& tectonic --version 2>&1 | Select-Object -First 1)"
Write-Host "   python  : $(python --version)"
