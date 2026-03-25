# Ejemplos prácticos — EDU

---

## Caso 1: Adrián — Jefe de Cátedra, semana 1

Adrián lleva 5 años dictando Electrónica Digital. Tiene material del año pasado y quiere producir el cursado nuevo aprovechando lo que ya existe.

### Lunes — Setup inicial

```chat
Adrián: /edu-start-course

Elena: Bienvenido. Voy a hacerte 6 preguntas para configurar la materia.
   1. ¿Nombre de la materia?
Adrián: Electrónica Digital
Elena: 2. ¿Universidad / institución?
Adrián: UTN FRSF
Elena: 3. ¿Perfil docente? (teorico, practico, socratico, flipped, investigador)
Adrián: practico
Elena: 4. ¿Duración de clase estándar? (60, 90, 120 min)
Adrián: 90
Elena: 5. ¿LMS que usás? (moodle / google-classroom / none)
Adrián: moodle
Elena: 6. ¿Idioma de comunicación?
Adrián: español

Elena: Configuración guardada. El plan mínimo todavía no está cargado.
       Siguiente paso: /edu-load-official-plan programa.pdf
```

### Lunes — Cargar programa oficial

```chat
Adrián: /edu-load-official-plan programa-2026.pdf

Elena: [plan-extractor leyendo...]
       Encontré 12 tópicos obligatorios:
       ✅ T1 Sistemas Numéricos
       ✅ T2 Álgebra de Boole
       ✅ T3 Circuitos Combinacionales
       ...
       ✅ T12 Memorias Programables

       ¿Confirmás este programa? Una vez confirmado, plan-minimo.md será inmutable.
       [CONFIRMAR / AJUSTAR]

Adrián: CONFIRMAR

Elena: plan-minimo.md guardado. ¡Este es el contrato de tu cursada 2026!
       Siguiente paso: /edu-build-course-from-materials ./material-2025/
```

### Martes — Construir plan desde material existente

```chat
Adrián: /edu-build-course-from-materials ./material-2025/

Elena: [material-ingester procesando 47 archivos...]
       Procesé: 12 PDFs, 8 PPTX, 3 DOCX, 1 tabla de ejercicios.

       [Marcos diseñando la estructura del plan...]

       Plan borrador listo:
       - T1 Sistemas Numéricos (2 semanas, material: 3 archivos)
       - T2 Álgebra de Boole (1 semana, material: 2 archivos)
       ...
       Cobertura del plan mínimo: 12/12 tópicos ✅

       ¿Aprobás el plan borrador? [APROBAR / AJUSTAR]

Adrián: APROBAR

Elena: Plan 2026 activo. Empezamos con el Tema 1.
```

### Miércoles — Ciclo Tema 1

```chat
Adrián: /edu-design-topic 1

Marcos: Diseñando Tema 1: Sistemas Numéricos
        Duración: 90 min (config activa)
        
        Estructura propuesta:
        ┌─────────────────────────────────────────────────────┐
        │ Tema 1 — Sistemas Numéricos (90 min)                │
        │                                                     │
        │ Parte 1 (25 min): Representación en distintas bases │
        │ Parte 2 (30 min): Conversión entre bases            │
        │ Parte 3 (25 min): Complemento a 2                   │
        │ Ejercicios integrados (10 min)                      │
        └─────────────────────────────────────────────────────┘
        
        ¿Ajustás algo? [/edu-adjust-design 1 instrucciones]
        ¿Aprobás? [/edu-approve-design 1]

Adrián: /edu-approve-design 1

Adrián: /edu-create-class 1

Roberto: Generando minuta.md y filminas.md para T1...
         ✅ temas/01-sistemas-numericos/minuta.md (1.800 palabras)
         ✅ temas/01-sistemas-numericos/filminas.md (12 slides)

Adrián: /edu-create-tp 1

Valeria: Generando TP1 trazable a la minuta...
         ✅ temas/01-sistemas-numericos/tp.md (5 ejercicios)
```

### Jueves — Calidad

```chat
Adrián: /edu-fix-writing-auto 1
        /edu-fix-coherence-auto 1
        /edu-validate-references 1

Elena: Loops de calidad T1:
       📝 Escritura: 3 correcciones aplicadas (3 commits Git)
       🔗 Coherencia: 1 término unificado ("circuito lógico" → consistente)
       🔬 Referencias: 2 referencias verificadas. 1 señalizada (no tiene DOI):
          → "Tanenbaum, 2001" — sugerencia: /edu-suggest-alternative 1 REF01

Adrián: /edu-validate-scope 1
        /edu-validate-density 1

academic-guardrail: ✅ Scope OK (sin desvíos detectados)
                   ⚠️ Densidad: Slide 7 tiene 3 conceptos nuevos sin ejemplar
                     → Sugerencia: agregar ejercicio ilustrativo
                     
Adrián: /edu-fix-guardrail-auto 1

academic-guardrail: ✅ Corrección aplicada (commit: fix/guardrail-t01-slide7)
```

### Viernes — Testing pedagógico

```chat
Adrián: /edu-test-topic 1 all

student-simulator → perfil: disperso
"Profe, no entendí cuándo usar complemento a 2 en vez del otro método... además en el slide 7 dice 'conversión directa' pero antes dijiste algo diferente."

student-simulator → perfil: ansioso
"¿Tiene muchos ejercicios el TP? ¿Cuánto vale cada uno?"

student-simulator → perfil: estrategico
"¿Esto entra en el parcial? ¿Con qué otros temas se relaciona?"

test-runner: score-pedagogico.md actualizado
             Claridad conceptual: 7.2/10
             Coherencia interna: 8.5/10
             Ansiedad estimada: baja
             FAQ anticipado: 4 preguntas frecuentes detectadas

Adrián: Perfecto. Bajo el score de claridad. Voy a arreglar el slide 7.
        [hace ajuste manual]

Adrián: /edu-close-topic 1

Elena: ✅ Tema 1 cerrado.
       Git: branch tema/01-sistemas-numericos mergeada.
       Cobertura del plan mínimo: T1 ✅ (1/12)
```

---

## Caso 2: Laura — Auxiliar nueva, primer cuatrimestre

Laura es nueva en la cátedra. Adrián le pasó el workspace con el cursado ya armado. Ella tiene que producir el Tema 5.

```chat
Laura: /edu-help

Elena: Hola Laura. El cursado está en T4-completado / T5-en-progreso.
       Próximo paso recomendado: /edu-create-class 5
       
       ¿Querés el resumen del Tema 5 primero? /edu-status 5

Laura: /edu-status 5

Elena: Tema 5 — Circuitos Secuenciales
       Diseño: ✅ aprobado por Marcos (duración: 90 min)
       Clase: ⏳ pendiente
       TP: ⏳ pendiente
       Calidad: ⏳ pendiente

Laura: /edu-create-class 5

Roberto: [Generando con el perfil docente activo: "practico"]
         ✅ temas/05-circuitos-secuenciales/minuta.md
         ✅ temas/05-circuitos-secuenciales/filminas.md
```

---

## Tips y FAQs

### "¿Qué pasa si el plan mínimo tiene un error?"

`plan-minimo.md` es inmutable por diseño — es el contrato con la institución. Si hay un error en el PDF original, debés cargar un PDF corregido y ejecutar `/edu-load-official-plan` nuevamente (te pedirá confirmación antes de reemplazar).

### "¿Puedo ajustar la duración de un tema específico?"

Sí, antes de diseñar el tema:
```bash
/edu-set-topic-duration 3 120   # Tema 3 tendrá 120 min
```

### "¿Cómo vuelvo atrás una corrección automática?"

Cada corrección automática genera un commit Git individual. Para revertir:
```bash
git revert <commit-hash>
```
O usá la vista de commits de tu IDE.

### "¿El simulador de alumno aprende?"

El simulador tiene dos memorias:
- **Session-scoped:** perfil activo de sesión, se descarta al cerrar
- **Long-term:** calibración acumulada de todas las sesiones (en `_edu-memory/calibracion-simulador/`), nunca se descarta

Para alimentar el long-term con datos reales de tus alumnos:
```bash
/edu-compare-survey-simulator 3   # después de tomar encuesta en T3
```

### Easter eggs

- Si escribís **"estoy en pánico"** a Elena, te responde con el estado exacto del cursado, el próximo paso más importante, y un café virtual ☕
- `academic-guardrail` cita a Bloom cuando rechaza algo: *"Según la taxonomía de Bloom, este nivel requiere..."*
- Bib. Carlos tiene fobia a Wikipedia: si le pedís que cite Wikipedia responde *"Wikipedia no figura en mi lista de fuentes aceptadas. ¿Querés que busque en Semantic Scholar?"*
- Si el score pedagógico supera 9.0/10 en dos temas consecutivos, Elena dice: *"Tu cátedra está en modo excelencia. 🏆"*
