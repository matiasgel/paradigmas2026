# Snapshot parcial de `filminas.md` visto en el editor

Estado del relevamiento: el archivo no estaba persistido en disco al momento de copiar evidencia, pero si existia un buffer visible en el editor. Se guarda aqui el contenido parcial observable para futura migracion al contrato `filminas/v2`.

Advertencias:

- Es un snapshot parcial, no una copia completa garantizada.
- El contenido visible no sigue el contrato `### [F-XX]` del parser v2; usa `### [1]`, `### [2]`, etc.
- Los prompts visibles usan lenguaje conceptual y no el lenguaje visual puro endurecido despues del tema 00/01.

## Contenido parcial observado

```md
# Filminas — Tema 03: Introduccion a Programacion Funcional con TypeScript

> **Estado:** GENERADA
> **Agente:** Dr. Roberto (class-writer)
> **Fecha:** 2026-03-23
> **Duracion total:** 120 minutos · 8 bloques · 29 filminas (F-00 portada + F-01 a F-28)
> **Formato:** Markdown estructurado para exportar a presentacion
> **Input:** `temas/03-intro-funcional-ts/diseno.md` (aprobado)

---

## PORTADA

---

### [1]

# Introduccion a Programacion Funcional con TypeScript

**Paradigmas y Lenguajes de Programacion 2026**
Universidad Nacional de Tierra del Fuego — IDEI

Semana 2 · Clase 1 de 1 · 120 minutos

*Lenguaje principal: TypeScript (estilo puro) · Contraste: Clojure*

@imagen: background
@prompt-imagen: prompt="Dark abstract background with lambda symbol (λ) in minimalist white lines, computational mathematics aesthetic, university lecture style"

---

## BLOQUE 0 — Recap y punto de partida (5 min)

---

### [2]

# ¿Donde estamos?

**En T01 vimos el mapa de los paradigmas:**

| Paradigma | Raiz formal | Unidad |
|-----------|-------------|--------|
| Imperativo | Maquina de Turing | Instruccion + estado |
| Orientado a Objetos | Imperativo + encapsulamiento | Objeto / mensaje |
| **Funcional** | **λ-calculo (Church, 1936)** | **Funcion** |
| Logico | Logica simbolica | Relacion / hecho |

> *"Hoy nos adentramos en el funcional. Y empezamos con una pregunta rara:"*

**¿Que tiene de especial un lenguaje donde ninguna variable cambia de valor?**

---

## BLOQUE 0.5 — Historia y Raices Formales (15 min)

---

### [3]

# El problema que lo origino todo

## El *Entscheidungsproblem* — Hilbert, 1928

> *"¿Existe un algoritmo mecanico que, dado cualquier enunciado matematico, determine en tiempo finito si es verdadero o falso?"*

**Por que importaba:**
- Era la pregunta central del programa formalista de Hilbert
- Para responderla habia que definir primero: ¿que es un **algoritmo mecanico**?
- Esa definicion dio origen a dos modelos de computo que cambiaron la historia

@imagen: content
@prompt-imagen: prompt="Portrait of David Hilbert with a chalkboard showing mathematical formulas, academic early 20th century style, black and white"

---

### [4]

# La respuesta de Turing: la maquina con cinta (1936)
```

## Recomendacion de uso

Antes de intentar publicar este tema con el pipeline actual, conviene:

1. normalizar encabezados a `### [F-XX]`;
2. agregar `@tipo:` explicito en cada slide;
3. reescribir prompts de imagen con lenguaje visual puro;
4. ejecutar `parse_filminas.py` y revisar el `plan-draft` resultante.
