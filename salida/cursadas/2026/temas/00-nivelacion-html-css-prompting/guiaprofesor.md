# Guía del Profesor — Tema 00: Nivelación HTML/CSS/Bootstrap 5
## IF009 — Laboratorio de Programación y Lenguajes
### UNTDF IDEI · 2026 · Semana 1

> **Para el docente:** Este documento es tu centro de mando para la semana 1. Está pensado para ser autosuficiente: podés revisar el tema sin abrir ningún otro archivo. Incluye el plan de clase, extractos técnicos clave, anticipación de dudas frecuentes y ruta a todos los recursos.

---

## Mapa de Recursos del Tema

| Artefacto | Archivo | Para quién | Función |
|-----------|---------|-----------|---------|
| Filminas | `filminas.md` (39 slides) | Docente → pantalla | Soporte visual de clase |
| Minuta | `minuta.md` | Docente | Guión con demos y guías por bloque |
| Esta guía del profesor | `guiaprofesor.md` | Docente | Visión global + extractos técnicos |
| Guía de estudio | `guia-estudio.md` | **Alumno** | Estudio autónomo post-clase |
| Workflow de prompts | `PROMPTS.md` | **Alumno** | Plantilla y ejemplos para el TP1 |
| Diseño pedagógico | `diseno.md` | Docente / coordinación | Alcance, objetivos, cronograma |
| Configuración del tema | `topic.yaml` | Sistema EDU | Metadata, TPs, links Classroom |

---

## Plan de Clase — Vista Rápida

### Bloque Teórico (180 min)

```
 T0 ─── 15 min ─── Presentación de la materia + política IA
 T1 ─── 30 min ─── Prompting & GitHub Copilot
 T2 ─── 45 min ─── HTML5: estructura y semántica
 T3 ─── 40 min ─── CSS3: box model + flexbox
 T4 ─── 30 min ─── Preview TP1 + setup GitHub Classroom
 T5 ─── 10 min ─── Cierre, preguntas, resumen semana 1  (T4+T5 ajustable)
 
 SLIDES: 01-13 (teoría), 37-39 (cierre)
```

### Bloque Práctico (180 min)

```
 P1 ─── 45 min ─── Bootstrap Grid: CDN + container/row/col + breakpoints
 P2 ─── 45 min ─── Bootstrap Navbar + Cards + Forms
 P3 ─── 30 min ─── Live coding: index.html completo + W3C Validator
 P4 ─── 30 min ─── GitHub Classroom: clonar, primer commit, push
 P5 ─── 30 min ─── Trabajo autónomo asistido (dudas individuales)  (ajustable)
 
 SLIDES: 23-39
```

---

## Cronograma Detallado

### T0 — Presentación de la materia (15 min)
**Slides:** 01, 03, 04, 05

**Contenido a cubrir:**
- Presentación del docente y ayudantes (2 min)
- Modalidad: 3h teoría + 3h práctica, todo via GitHub Classroom
- Stack del cuatrimestre: HTML/CSS → Python → Django → PostgreSQL (SLIDE 03)
- Evaluación: 4 TPs + 2 Aplicaciones + autograding en algunos TPs
- **Política de IA** (SLIDE 04/05): Copilot habilitado + PROMPTS.md obligatorio
- Demo de apertura: crear `hola.html` en VS Code, Copilot autocompleta con Tab

**Mensaje clave:** *"Usan IA como herramienta profesional. El PROMPTS.md es la evidencia de que lo usaron de forma reflexiva."*

---

### T1 — Prompting & GitHub Copilot (30 min)
**Slides:** 04, 05

**Contenido a cubrir:**
- ¿Qué es Copilot? Autocompletado inteligente, no magia
- Anatomía de un buen prompt: contexto + tarea + restricciones + formato
- Demo: prompt malo vs. bueno para navbar (mostrar diferencia de output en vivo)
- Crear PROMPTS.md en vivo con formato completo
- Anti-pattern: copiar sin entender

**Demo en vivo (code a mostrar):**
```
❌ prompt malo:  "haceme un navbar"

✅ prompt bueno: "Soy alumno de primer año de programación web. Necesito un
  Navbar de Bootstrap 5.3 responsive con logo 'Mi Blog' a la izquierda
  y 3 links a la derecha: Inicio, Sobre mí, Contacto.
  Que colapse en hamburguesa en pantalla < 992px (navbar-expand-lg).
  Fondo oscuro (navbar-dark bg-dark) con sticky-top.
  Solo el HTML del <nav>, sin CSS adicional."
```

**Errores frecuentes:**
- *"¿Puedo usar ChatGPT en lugar de Copilot?"* → Sí, el PROMPTS.md es igual
- *"¿Usar IA es trampa?"* → Analogía de la sierra eléctrica

---

### T2 — HTML5: estructura y semántica (45 min)
**Slides:** 06-13

**Secuencia recomendada:**

**1. Crear el documento base (10 min)**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Blog</title>
</head>
<body>
    <h1>Hola</h1>
</body>
</html>
```
Señalar cada línea y su propósito. El `lang="es"` importa para accesibilidad.

**2. Árbol DOM en DevTools (5 min)**
Abrir en navegador → F12 → Elements. Expandir el árbol. Agregar un `<p>` y ver el nodo aparecer.

**3. Semántica vs. Divitis (15 min)**
Mostrar en pantalla la diferencia (SLIDE 10-11). Construir la estructura semántica en vivo:
```html
<header>
    <nav>
        <a href="index.html">Inicio</a>
    </nav>
</header>
<main>
    <section>
        <article><h2>Post 1</h2><p>Resumen...</p></article>
        <article><h2>Post 2</h2><p>Resumen...</p></article>
    </section>
</main>
<footer>
    <p>© 2026 Mi Blog</p>
</footer>
```

**4. Formularios HTML5 (15 min)**
Crear el formulario de contacto básico con validación nativa.

**Errores frecuentes:**
- No cerrar etiquetas → el navegador es permisivo pero el W3C Validator no
- Usar `<br>` en lugar de etiquetas semánticas → código de los 90s
- `<div id="header">` en lugar de `<header>` → hábito viejo

---

### T3 — CSS3: Box Model + Flexbox (40 min)
**Slides:** 14-22

**Secuencia recomendada:**

**1. Hoja de estilos base (10 min)**
```css
:root {
    --color-primario: #2c3e50;
    --color-acento: #3498db;
}

*, *::before, *::after {
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', sans-serif;
    color: var(--color-primario);
}
```
Explicar `box-sizing: border-box` con la analogía de la caja — el `padding` va para adentro.

**2. BoxModel en DevTools (5 min)**
Seleccionar un elemento → pestaña Computed → mostrar las capas del box model visualmente.

**3. Flexbox en vivo (10 min)**
Crear un `<div class="nav-links">` con 3 links. Aplicar:
```css
.nav-links { display: flex; gap: 1rem; }
```
Mostrar qué cambia cada valor de `justify-content`.

**4. Media Queries (5 min)**
Agregar `@media (max-width: 576px)` y mostrar en DevTools cómo simular un iPhone.

**Errores frecuentes:**
- Usar `margin: auto` en lugar de `display: flex; justify-content: center` → funciona pero no entienden por qué
- Confundir `margin` y `padding` → margin es entre elementos, padding es espacio interno

---

### T4 — Preview TP1 + GitHub Classroom (30 min)
**Slides:** 34-36, revisitar 02

**Contenido:**
- Mostrar el wireframe del blog terminado (SLIDE 02)
- Estructura de carpetas obligatoria del TP1 (SLIDE 35)
- Checklist de entrega (SLIDE 36)
- Abrir el link del TP1 en el navegador: `classroom.github.com/a/RI8vnIt_`
- Mostrar cómo aceptar la asignación → GitHub crea el repo automáticamente

---

### P1 — Bootstrap Grid (45 min)
**Slides:** 23-27

**Secuencia de construcción:**
```
1. Pegar CDN link + script en el <head> y <body>
2. Verificar en DevTools que Bootstrap está cargado (agregar btn btn-primary → cambia)
3. Crear container > row > 3 × col-md-4
4. Mostrar breakpoints con DevTools: arrastrar el tamaño
5. Cambiar a row-cols-1 row-cols-sm-2 row-cols-lg-3 g-4
6. Demo gutter: g-1 vs g-3 vs g-5 en tiempo real
```

**Concepto clave a dejar claro:**
`col-md-4` = "a partir de 768px ocupa 4 de 12 columnas. En pantallas menores, ocupa el 100%."

---

### P2 — Navbar + Cards + Forms (45 min)
**Slides:** 28-33

**Secuencia:**
```
1. Navbar: pegar estructura base → mostrar hamburguesa en mobile → 
   demo bug: cambiar el id del div y ver que deja de funcionar
2. Cards con h-100: mostrar cards sin h-100 vs. con h-100 (diferencia enorme)
3. d-flex flex-column + mt-auto → botón siempre al fondo
4. Formulario: campos name/email/tel/mensaje + required + type correcto
```

**Bug intencional para mostrar:**
```html
<!-- Bug: data-bs-target="#menuNav" pero el div tiene id="navbarMenu" -->
<!-- La hamburguesa no hace nada → mensaje de error silencioso -->
```

---

### P3 — Live coding index.html completo (30 min)
**Slides:** 34-36

Construir desde cero:
1. Estructura HTML base (Emmet: `!` → Enter)
2. CDN links
3. Navbar (copiar de la demo anterior)
4. Hero section (`<header class="hero-section">`)
5. Grid de 3 cards de artículos
6. Footer
7. **W3C Validator al final** — mostrar cómo subir el archivo y leer el resultado

---

### P4 — GitHub Classroom (30 min)
**Slides:** 34-36

```bash
# Demo completa en terminal
git clone https://github.com/Laboratorio-de-Programacion-Y-lenguajes-2026/tp1-blog-[usuario]
cd tp1-blog-[usuario]
mkdir assets assets/images
# Crear index.html básico
git add index.html
git commit -m "feat: scaffold inicial index.html"
git push
```

Mostrar en GitHub.com que el push llegó.
Mostrar los criterios de autograding (si aplica) en la interfaz del Classroom.

---

## Extractos clave del material fuente

### De `material/tema 01/HTML & CSS.pdf`

> "HTML (HyperText Markup Language) nos permite definir la **estructura** de una página web. Estructura: párrafos, headings, tablas, listas. Contenido: textos, imágenes, links. **CSS** controla los estilos: color, tipografía, alineación, espaciado, fondos."

> "Árbol de HTML: cada etiqueta es un nodo. `<div>` puede tener hijos `<h1>` y `<span>` que son hermanos entre sí."

### De `material/tema 01/bootstrap5-grid.pdf`

> "Bootstrap grid usa contenedores, filas y columnas para layoutear y alinear contenido. Está construido con flexbox y es completamente responsive. **12 columnas** por fila, **6 breakpoints** responsive, gutters configurables."

> **Breakpoints:** xs < 576px, sm ≥ 576px, md ≥ 768px, lg ≥ 992px, xl ≥ 1200px, xxl ≥ 1400px

### De `material/tema 01/bootstrap5-navbar.pdf`

> "La Navbar colapsa en mobile: el botón hamburguesa tiene `data-bs-target` que **debe coincidir exactamente** con el `id` del `<div class='collapse'>`. Este es el error más frecuente."

### De `material/tema 01/bootstrap5-card.pdf`

> "Cards son contenedores de contenido flexibles y extensibles. Soportan headers, footers, colores de fondo, imágenes. Para igualar alturas: `d-flex flex-column` en `.card-body` + `mt-auto` en el último elemento."

---

## Anticipación de Dudas Frecuentes

| Duda | Respuesta sugerida |
|------|-------------------|
| "¿Puedo usar CSS en línea (`style="..."`)?" | Para el TP no — el CSS va en `assets/styles.css`. El CSS en línea rompe la separación de responsabilidades y hace el código imposible de mantener. |
| "¿Bootstrap reemplaza CSS?" | No. Bootstrap da el sistema de grilla y los componentes. Tu `styles.css` agrega el branding (colores, tipografía, efectos hover) que Bootstrap no sabe. |
| "El navbar no funciona en mobile" | Verificar que el `data-bs-target` del botón coincide con el `id` del div que colapsa. 9 de cada 10 veces es ese bug. |
| "¿Cuántos commits hago?" | Mínimo 5. Uno por componente: navbar, hero, grid-cards, form, CSS + 1 para PROMPTS.md. |
| "¿Las imágenes de los posts tienen que ser mías?" | No — pueden usar imágenes de Unsplash (unsplash.com) que son libres de derechos. Sí necesitan poner el `alt` descriptivo. |
| "¿Puedo usar otro framework que no sea Bootstrap?" | Para el TP1 no — el objetivo es que aprendan Bootstrap porque lo usaremos en Django Templates. Para proyectos propios, bienvenidos. |
| "¿Qué pasa si el W3C Validator muestra warnings?" | Los warnings no descuentan, los errores sí. Meta description faltante es warning; `<img>` sin `alt` es error. |

---

## Checklist del Docente — Antes de Clase

- [ ] VS Code abierto con extensión Copilot activa y visible
- [ ] Repositorio de demo creado (o reutilizado de la clase anterior)
- [ ] DevTools del navegador configurado en modo responsive
- [ ] Slides proyectables en `filminas.md` (o exportadas a PDF)
- [ ] Link del TP1 abierto en una pestaña: `classroom.github.com/a/RI8vnIt_`
- [ ] Link del TP2 abierto: `classroom.github.com/a/X4xiTEDQ`
- [ ] W3C Validator abierto: `validator.w3.org`
- [ ] Terminal abierta con `.venv` activado (para demos de Python en T3 si hay tiempo)

---

## Checklist del Docente — Después de Clase

- [ ] Verificar que hay submissions en GitHub Classroom (señal de que alumnos aceptaron el TP)
- [ ] Enviar link de recursos por el canal de comunicación (PROMPTS.md template, guia-estudio.md)
- [ ] Revisar si hubo dudas recurrentes para agregar a la guía docente
- [ ] Actualizar `topic.yaml` si cambió algún deadline o descripción de TP

---

## TPs Activos — Links y Deadlines

| TP | Nombre | Link Classroom | Deadline | Autograding |
|----|--------|---------------|----------|-------------|
| TP01 | Blog personal HTML/CSS/Bootstrap | classroom.github.com/a/RI8vnIt_ | `2026-03-31 23:00` | No (revisión manual W3C) |
| TP02 | Python Autograding — Fundamentos | classroom.github.com/a/X4xiTEDQ | `2026-03-31 23:00` | ✅ Sí |
| TP03 | Tests Unitarios con pytest | classroom.github.com/a/jLxPRyso | `2026-04-07 23:00` | ✅ Sí |

---

## Criterios de Evaluación del TP1

| Criterio | Descripción | Peso |
|----------|-------------|------|
| HTML válido (W3C) | Sin errores en las 3 páginas | 20% |
| Semántica HTML5 | Uso correcto de `<header>`, `<nav>`, `<main>`, `<article>`, `<footer>` | 15% |
| Bootstrap Grid | Layout responsive que funciona en mobile/tablet/desktop | 20% |
| Bootstrap Navbar | Hamburgesa funcional en mobile | 10% |
| Formulario | Validación HTML5 + feedback visual CSS | 15% |
| CSS personalizado | Variables CSS, hover effects, diseño propio | 10% |
| PROMPTS.md | Mínimo 5 prompts documentados en formato correcto | 10% |
| **Bonus** | Breadcrumbs, favicon, animaciones CSS, ARIA labels | +5% |

> **Devolución sin nota:** Entregar sin `PROMPTS.md`, o con menos de 5 commits. Se devuelve para completar.

---

## Rutas a Todos los Recursos

```
salida/cursadas/2026/temas/00-nivelacion-html-css-prompting/
├── diseno.md           ← Diseño pedagógico aprobado
├── filminas.md         ← 39 slides de clase
├── minuta.md           ← Guión docente con demos y errores frecuentes
├── guiaprofesor.md     ← Este documento
├── guia-estudio.md     ← Material para el alumno
├── PROMPTS.md          ← Plantilla de workflow de prompts para TP1
└── topic.yaml          ← Metadata, TPs, links

material/tema 01/
├── HTML & CSS.pdf                ← PDF fuente teórico
├── bootstrap5-grid.pdf           ← Referencia grid Bootstrap
├── bootstrap5-navbar.pdf         ← Referencia navbar Bootstrap
├── bootstrap5-card.pdf           ← Referencia cards Bootstrap
├── TP 1.pdf / tp1-consigna.pdf   ← Consigna oficial del TP1
├── TP 3.pdf / tp3-consigna.pdf   ← Consigna oficial del TP3
└── txt/                          ← Versiones texto de los PDF (para Copilot)
    ├── html-css.txt
    ├── bootstrap5-grid.txt
    ├── bootstrap5-navbar.txt
    ├── bootstrap5-card.txt
    ├── tp1.txt
    └── tp3.txt
```

---

*Guía del profesor elaborada por el módulo EDU · IF009 Laboratorio de Programación y Lenguajes 2026 · UNTDF IDEI*
