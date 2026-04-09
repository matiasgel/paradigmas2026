# Bloom's Taxonomy & Assessment Design — Anderson 2001, Haladyna 2024

**Fuentes:**
- Anderson, L.W. & Krathwohl, D.R. (2001). *A Taxonomy for Learning, Teaching, and Assessing*, Pearson
- Haladyna, T.M., Rodriguez, M.C. & Stevens, T.M. (2024). *Developing and Validating Test Items* (4th ed.), Routledge
- NBME Item Writing Guide (2024 update)
- Rudolph, J., Tan, S. & Tan, S. (2023). *ChatGPT: Bullshit Spewer or the End of Traditional Assessments?*, JALT, 6(1)
- Prather, J. et al. (2023). *The Robots Are Coming*, SIGCSE '23
**Relevancia Sprint:** S2.2

## Taxonomía Revisada de Bloom (2001) — Vigente

### 6 Niveles Cognitivos (de menor a mayor)

| Nivel | Nombre | Verbos típicos | Ejemplo CS |
|-------|--------|----------------|------------|
| 1 | **Recordar** | listar, definir, identificar | "¿Qué es un puntero?" |
| 2 | **Comprender** | explicar, parafrasear, clasificar | "Explica la diferencia entre stack y heap" |
| 3 | **Aplicar** | implementar, ejecutar, usar | "Escribí una función que..." |
| 4 | **Analizar** | comparar, depurar, diferenciar | "¿Por qué este código da segfault?" |
| 5 | **Evaluar** | justificar, criticar, juzgar | "¿Es mejor usar ArrayList o LinkedList aquí?" |
| 6 | **Crear** | diseñar, construir, formular | "Diseñá un sistema de cache con LRU" |

### Distribución Recomendada para Parciales CS (universidad)

| Nivel | Porcentaje sugerido | Justificación |
|-------|--------------------|-|
| Recordar | 10-20% | Necesario pero no suficiente |
| Comprender | 20-30% | Base para niveles superiores |
| Aplicar | 25-35% | Core de materias de programación |
| Analizar | 15-20% | Diferencia alumnos competentes de excelentes |
| Evaluar | 5-10% | Solo para ítems difíciles / bonus |
| Crear | 0-5% | Reservar para proyectos finales |

## Haladyna et al. (2024, 4th Edition) — Novedades

### AI-Generated Items (sección nueva)
- LLMs pueden generar ítems de MC pero requieren revisión humana para:
  - Verificar que los distractores sean plausibles pero incorrectos
  - Asegurar que la clave (respuesta correcta) sea inequívocamente correcta
  - Eliminar patrones que LLMs puedan "adivinar" (longest option is correct, etc.)

### AI-Resistant Assessment Design (sección nueva)
- Ítems que LLMs no pueden resolver fácilmente:
  - Análisis de código con errores sutiles (off-by-one, race conditions)
  - Código incompleto que requiere contexto del curso
  - Preguntas que referencian material específico de la clase (no googleable)
  - Oral defense post-escrita

### Calibración de Dificultad
- Ítems MC bien escritos: 60-80% de acierto (dificultad media)
- Distractores deben atraer al menos 5% de respuestas cada uno
- Test bien calibrado: distribución normal con media 65-75%

### Reglas de Item Writing (vigentes)
1. Un solo concepto por ítem
2. Stem en positivo (evitar "cuál NO es...")
3. Opciones de longitud similar
4. Sin "todas las anteriores" / "ninguna de las anteriores"
5. Distractores plausibles basados en errores comunes reales
6. Sin pistas gramaticales (artículo que delata género/número)

## NBME Guide (2024) — Gold Standard MC

### Formato Recomendado
```
::Nombre del ítem::
Contexto/viñeta clínica (o técnica en CS)
{pregunta lead-in}

A. Distractor 1 (error común: confundir X con Y)
B. Distractor 2 (error común: aplicar mal regla Z)
=C. Clave correcta
D. Distractor 3 (error común: olvidar caso base)
```

### Adaptación a GIFT (Moodle)
```
::Punteros - Nivel Analizar::
Dado el siguiente fragmento de código C\:
```int *p \= NULL; *p \= 42;```
¿Qué ocurre al ejecutar este código?{
~Imprime 42 en pantalla#Error: confunde asignación con printf
~Crea una variable con valor 42#Error: ignora que p es NULL
=Produce un segmentation fault#Correcto: dereferencia de puntero NULL causa SIGSEGV
~Error de compilación#Error: el código compila, el error es en runtime
}
```

## AI-Proofing Exams (Rudolph 2023, Prather 2023)

### Estrategias para CS
1. **Análisis de código existente** (Bloom nivel 4+): "¿Por qué este código no compila?"
2. **Tracing manual**: "¿Cuál es el output de este programa con input X?"
3. **Debugging con contexto**: dar código que funciona pero ineficientemente
4. **Referencia a material de clase**: "Según lo visto en las filminas de Tema 3..."
5. **Componente presencial**: live coding defense post-TP
6. **Variantes por alumno**: parámetros distintos para misma estructura de problema
