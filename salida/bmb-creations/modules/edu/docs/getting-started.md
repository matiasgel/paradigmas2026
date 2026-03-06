# Primeros pasos — EDU: Academic Course Production Suite

Bienvenido al módulo EDU. Esta guía te lleva desde la instalación hasta tu primer tema listo para dar clase.

---

## ¿Qué hace este módulo?

EDU es el departamento de producción docente de tu cátedra. Cubre todo el ciclo:

1. **Ingesta** — cargás el programa oficial de la institución; EDU lo convierte en el contrato de tu cursada
2. **Plan** — construís el plan desde material existente o desde investigación académica
3. **Producción** — para cada tema: diseño → clase → TP, con la duración como constraint
4. **Calidad** — 3 loops automáticos (escritura → coherencia → referencias) + guardrail académico
5. **Testing** — el alumno simulado (con perfil empírico) lee el material antes que tus alumnos reales
6. **Cierre** — cada tema se cierra en Git; al final del año tenés la retrospectiva y el año siguiente arranca con memoria

---

## Instalación

```bash
bmad install edu
```

O copiá la carpeta `_edu/` a tu workspace y seguí los prompts de `module.yaml`.

---

## Primeros pasos — semana 1 del cuatrimestre

### Paso 1: Configurar la materia

```bash
/edu-start-course
```

Elena te hace 6 preguntas:
1. ¿Nombre de la materia?
2. ¿Universidad / institución?
3. ¿Perfil docente? (teorico, practico, socratico, flipped, investigador)
4. ¿Duración de clase? (60, 90, 120 min)
5. ¿LMS? (moodle / google-classroom / none)
6. ¿Idioma de comunicación?

### Paso 2: Cargar el programa institucional

```bash
/edu-load-official-plan programa.pdf
```

`plan-extractor` lee el PDF y extrae los tópicos obligatorios. Elena te los presenta para revisión.

```bash
/edu-confirm-official-plan
```

Desde acá, `plan-minimo.md` es **inmutable**. Es el contrato de la cursada.

### Paso 3: Construir el plan

**Si tenés material del año anterior:**
```bash
/edu-build-course-from-materials ./material-2025/
```

**Si empezás desde cero:**
```bash
/edu-research-plan
```

Elena propone el plan; vos ajustás y confirmás.

### Paso 4: Ciclo de un tema

```bash
/edu-design-topic 1          # Marcos diseña con la duración como constraint
/edu-create-class 1          # Roberto genera minuta + filminas
/edu-create-tp 1             # Valeria genera el TP trazable a la clase
```

### Paso 5: Loops de calidad

```bash
/edu-validate-writing 1
/edu-fix-writing-auto 1      # Correcciones automáticas (generan commits Git)
/edu-validate-coherence 1
/edu-fix-coherence-auto 1
/edu-validate-references 1
/edu-validate-scope 1
/edu-validate-density 1
```

### Paso 6: Testing pedagógico

```bash
/edu-test-topic 1 all        # Todos los perfiles configurados
```

El alumno simulado señala confusiones antes de que lleguen a tus alumnos reales.

### Paso 7: Cerrar el tema

```bash
/edu-close-topic 1
```

Solo disponible cuando todos los loops están resueltos. Genera un merge en Git.

---

## Navegación y ayuda

```bash
/edu-help                    # Estado actual + próximo paso recomendado
/edu-help ciclo-tema         # Ayuda contextual para la fase de ciclo de tema
/edu-help /edu-validate-writing   # Descripción detallada de un comando
/edu-status 3                # Estado del tema 3
```

---

## Siguientes pasos

- [Referencia de agentes](agents.md) — conocé a tu equipo
- [Referencia de workflows](workflows.md) — qué podés hacer
- [Ejemplos prácticos](examples.md) — casos de uso reales
