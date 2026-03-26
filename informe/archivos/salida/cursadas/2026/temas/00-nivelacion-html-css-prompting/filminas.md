# Filminas — Tema 00: Nivelación HTML/CSS/Bootstrap 5
## IF009 Laboratorio de Programación y Lenguajes — UNTDF IDEI 2026

> **Nota:** Este documento es el guión de filminas complementario a las ya presentadas en clase (basadas en `HTML & CSS.pdf`). El docente puede usar estas filminas como repaso, seleccionar slides específicos o usarlos para el bloque de práctica.

---

### [F-01] Portada

**Título:** Nivelación HTML / CSS / Bootstrap 5

**Subtítulo:** Laboratorio de Programación y Lenguajes · Semana 1

**Pie:** UNTDF IDEI · 2026 · Prof. ______

---

### [F-02] ¿Qué vamos a construir?

**Título:** El proyecto de esta semana

```
[IMAGEN: Wireframe de un blog en 3 dispositivos]

  📱 Móvil          💻 Tablet          🖥️ Desktop
  ┌──────┐          ┌──────────┐       ┌────────────────┐
  │Navbar │          │  Navbar  │       │     Navbar     │
  ├──────┤          ├──────────┤       ├────────────────┤
  │ Card │          │Card│Card │       │Card │Card│Card │
  │      │          │    │     │       │     │    │     │
  │ Card │          │Card│Card │       ├─────┴────┴─────┤
  │      │          └──────────┘       │     Footer     │
  │Footer│                             └────────────────┘
  └──────┘
```

**Un blog personal con:**
- `index.html` — lista de posts (cards Bootstrap)
- `about.html` — sobre el autor
- `contact.html` — formulario de contacto con validación CSS
- `assets/styles.css` — estilos custom + media queries
- TP1: entrega vía **GitHub Classroom**

---

### [F-03] El Stack del Cuatrimestre

**Título:** ¿Por qué HTML/CSS ahora?

```
Semana 1-2  →  HTML + CSS + Bootstrap   ← HOY
Semana 3    →  Python 3.13 fundamentos
Semana 5    →  Django 5.1 (web framework)
Semana 7    →  Django Templates (↔ HTML ← acá se une)
Semana 11   →  Django Auth + Admin
Semana 15   →  REST APIs
```

**El HTML que aprenden hoy aparece de nuevo en Django Templates.**

> Las variables de Python `{{ nombre }}` y los bloques `{% block %}` son exactamente la estructura que ven hoy, pero con datos dinámicos.

---

### [F-04] Tu nuevo copiloto: GitHub Copilot

**Título:** IA como herramienta, no como sustituto

```
Buen prompt = Buen código

❌ "Haceme una web"
✅ "Crea un Navbar Bootstrap 5 con logo y 3 links:
    Inicio, Sobre mí, Contacto. Que sea responsive
    y colapse en dispositivos móviles."
```

**La regla del cursado:**
> Podés usar IA. **Debés entender lo que usás.**
> Cada TP requiere `PROMPTS.md` documentando el proceso.

**No alcanza con copiar y pegar — el docente puede preguntar sobre cualquier línea de código.**

---

### [F-05] PROMPTS.md — Formato

**Título:** Cómo documentar el uso de IA

```markdown
## Prompt 1 — Navbar Bootstrap

**Fecha:** 15/03/2026
**Herramienta:** GitHub Copilot

**Lo que pedí:**
> Crear un navbar bootstrap 5 responsive con 3 links

**Lo que recibí:**
[snippet del código]

**Lo que modifiqué:**
- Cambié el texto de los links a español
- Agregué aria-label al botón de toggle
- Agregué la clase ms-auto para alinear a la derecha

**Por qué lo modifiqué:**
Los links estaban en inglés y faltaba accesibilidad
```

**Mínimo requerido: 5 prompts completos con este formato**

---

### [F-06] ¿Qué es HTML?

**Título:** HyperText Markup Language

```
Marcado     → usa <etiquetas> para etiquetar contenido
Hipertexto  → vínculos (enlaces) entre contenidos y páginas
```

**Define la ESTRUCTURA de una página web:**

| HTML define... | Ejemplos |
|----------------|----------|
| Estructura | párrafos, encabezados, tablas, listas |
| Contenido | textos, imágenes, links, videos |
| **No** define | colores, fuentes, márgenes (eso es CSS) |

```html
<!DOCTYPE html>       <!-- declara HTML5 al navegador -->
<html lang="es">      <!-- raíz del documento, idioma español -->
<head>
    <meta charset="UTF-8">
    <title>Un título</title>    <!-- aparece en la pestaña -->
</head>
<body>
    <p>Un párrafo</p>           <!-- contenido visible -->
</body>
</html>
```

---

### [F-07] HTML: Elementos y Tags

**Título:** La anatomía de un elemento HTML

```
         tag de apertura    contenido    tag de cierre
              ↓                 ↓              ↓
         <p>               Un párrafo         </p>

Elemento completo: <p>Un párrafo</p>
```

**Elementos sin tag de cierre (auto-closing):**
```html
<img src="foto.jpg" alt="descripción">
<input type="text" placeholder="Tu nombre">
<br>
<hr>
```

**Tags más usados:**

| Tag | Para qué | Ejemplo |
|-----|----------|---------|
| `<h1>`–`<h6>` | Encabezados | `<h1>Título principal</h1>` |
| `<p>` | Párrafo | `<p>Texto...</p>` |
| `<a>` | Enlace | `<a href="about.html">Sobre mí</a>` |
| `<img>` | Imagen | `<img src="foto.jpg" alt="Foto">` |
| `<ul>` / `<li>` | Lista no ordenada | `<ul><li>Ítem</li></ul>` |
| `<div>` | Contenedor bloque genérico | `<div class="card">...</div>` |
| `<span>` | Contenedor inline genérico | `<span class="badge">Nuevo</span>` |

---

### [F-08] HTML: Atributos esenciales

**Título:** Los atributos dan información extra al elemento

```
               atributo    valor
                  ↓          ↓
<a href="about.html" class="nav-link" id="link-about">
   Sobre mí
</a>
```

**Atributos globales (van en cualquier elemento):**

| Atributo | Función | Ejemplo |
|----------|---------|--------|
| `id` | Identificador único en la página | `id="navbar"` |
| `class` | Clase(s) CSS (puede repetirse) | `class="card shadow-sm"` |
| `style` | CSS inline (evitar en producción) | `style="color: red"` |

**Atributos específicos por tag:**

| Tag | Atributo | Para qué |
|-----|----------|----------|
| `<a>` | `href` | URL de destino |
| `<img>` | `src`, `alt` | Fuente e imagen alternativa |
| `<input>` | `type`, `placeholder`, `required` | Tipo, hint, obligatoriedad |
| `<form>` | `action`, `method` | Destino y método HTTP |
| `<link>` | `rel`, `href` | Tipo de recurso y ruta |

> **El atributo `alt` en imágenes es OBLIGATORIO** para accesibilidad y SEO.

---

### [F-09] HTML: El árbol DOM

**Título:** Cómo HTML forma una estructura de árbol

```
document
└── html
    ├── head
    │   ├── meta (charset)
    │   ├── meta (viewport)
    │   ├── title
    │   └── link (stylesheet)
    └── body
        ├── header
        │   └── nav
        │       ├── a.navbar-brand  ← hijo de nav
        │       └── ul.navbar-nav
        │           ├── li.nav-item ← hermanos entre sí
        │           └── li.nav-item
        ├── main
        │   └── section
        │       └── div.row
        │           ├── article.col-md-4 ← hermanos
        │           ├── article.col-md-4
        │           └── article.col-md-4
        └── footer
```

**Conceptos clave:**
- **parent** → el elemento que contiene a otro (`nav` es parent de `ul`)
- **child/hijo** → elemento dentro de otro (`ul` es child de `nav`)
- **siblings/hermanos** → elementos al mismo nivel (`li` son hermanos entre sí)

---

### [F-10] HTML5: Semántica vs Divitis

**Título:** El problema del `<div>` genérico

```
❌ HTML sin semántica (divitis)     ✅ HTML semántico
──────────────────────────         ──────────────────────
<div id="header">                  <header>
  <div id="menu">...</div>           <nav>...</nav>
</div>                             </header>
<div id="content">                 <main>
  <div class="post">...</div>        <article>...</article>
</div>                             </main>
<div id="footer">...</div>         <footer>...</footer>
```

**¿Por qué importa?**
- 👁️ **Lectores de pantalla** entienden la estructura → accesibilidad real
- 🔍 **SEO**: Google/Bing indexan mejor el contenido semántico
- 👨‍💻 **Mantenibilidad**: código que se puede leer 6 meses después

---

### [F-11] HTML5: Elementos semánticos

**Título:** El vocabulario de la estructura web

| Elemento | Descripción | Ejemplo de uso |
|----------|-------------|----------------|
| `<header>` | Cabecera de página/sección | Logo + Navbar |
| `<nav>` | Bloque de navegación | Menú principal |
| `<main>` | Contenido principal (1 por página) | La sección de posts |
| `<section>` | Sección temática | "Mis últimos posts" |
| `<article>` | Contenido independiente y reutilizable | Un post del blog |
| `<aside>` | Contenido complementario lateral | Sidebar con categorías |
| `<footer>` | Pie de página/sección | Copyright, redes sociales |
| `<figure>` | Imagen con descripción | Ilustración de un post |
| `<figcaption>` | Leyenda de una `<figure>` | "Foto tomada en Ushuaia" |

**Regla:** Solo un `<main>` por página. `<header>` y `<footer>` pueden repetirse dentro de `<article>` o `<section>`.

---

### [F-12] HTML5: Anatomía del documento completo

**Título:** Estructura base lista para usar

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <!-- Codificación obligatoria -->
  <meta charset="UTF-8">

  <!-- OBLIGATORIO para Bootstrap responsive -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- SEO básico -->
  <meta name="description" content="Blog personal — UNTDF 2026">
  <meta name="author" content="Tu Nombre">

  <title>Mi Blog Personal</title>

  <!-- Favicon -->
  <link rel="icon" type="image/x-icon" href="assets/images/favicon.ico">

  <!-- Bootstrap CSS (primero) -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        rel="stylesheet">

  <!-- CSS custom (después de Bootstrap para poder sobreescribir) -->
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>

  <!-- contenido aquí -->

  <!-- Bootstrap JS al final del body -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js">
  </script>
</body>
</html>
```

---

### [F-13] Estructura del Blog (HTML completo)

**Título:** Arquitectura del proyecto TP1

```html
<body>
  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <!-- Bootstrap Navbar responsive -->
    </nav>
  </header>

  <main class="container mt-4">
    <section id="posts">
      <h2 class="mb-4">Mis últimos posts</h2>
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <article class="col">
          <div class="card h-100 shadow-sm">
            <!-- Card Bootstrap completa -->
          </div>
        </article>
        <!-- más articles/cards -->
      </div>
    </section>
  </main>

  <footer class="bg-dark text-light mt-5 py-3">
    <div class="container text-center">
      <p class="mb-0">© 2026 Mi Blog · UNTDF · Laboratorio de Lenguajes</p>
    </div>
  </footer>
</body>
```

**`row-cols-1 row-cols-md-3`** = 1 columna en móvil, 3 columnas en desktop

---

### [F-14] ¿Qué es CSS?

**Título:** Cascading Style Sheets

**CSS controla TODO lo visual de la página:**

| Controla | Ejemplos |
|----------|---------|
| Color | `color: #333; background-color: #f8f9fa;` |
| Tipografía | `font-size: 1.2rem; font-weight: bold;` |
| Espaciado | `margin: 16px; padding: 8px 16px;` |
| Disposición | `display: flex; grid-template-columns: ...` |
| Responsive | `@media (min-width: 768px) { ... }` |
| Animaciones | `transition: all 0.3s ease;` |

**Regla CSS = Selector + Declaraciones:**

```css
           selector
              ↓
h1 { color: #CC9900; font-size: 2rem; }
     ────────────────────────────────
           declaraciones
           (propiedad: valor;)
```

> **"Cascading"** = cuando múltiples reglas aplican al mismo elemento, gana la más específica.

---

### [F-15] CSS: Selectores

**Título:** Cómo apuntar a los elementos

```css
/* 1. Selector de ELEMENTO — aplica a todos los h1 */
h1 { color: #333; }

/* 2. Selector de CLASE — aplica a todo lo que tenga class="card" */
.card { border-radius: 8px; }

/* 3. Selector de ID — aplica solo al elemento con id="navbar" */
#navbar { background-color: white; }

/* 4. Selector DESCENDIENTE — solo p dentro de article */
article p { line-height: 1.7; }

/* 5. Selector de HIJO DIRECTO */
nav > ul { list-style: none; }

/* 6. Selector de ATRIBUTO */
input[type="email"] { border-color: #0d6efd; }

/* 7. Pseudo-clase */
a:hover { color: #0d6efd; text-decoration: underline; }
button:focus { outline: 2px solid #0d6efd; }
```

**Especificidad (quién gana cuando hay conflicto):**
```
!important > inline style > #id > .class > element
    ∞              1000       100     10       1
```

---

### [F-16] CSS: Unidades y Colores

**Título:** Números en CSS — cuál usar cuándo

**Unidades de medida:**

| Unidad | Tipo | Cuándo usar |
|--------|------|-------------|
| `px` | Absoluta | Bordes, sombras, valores fijos precisos |
| `rem` | Relativa a root `<html>` | Font sizes (accesibilidad) |
| `em` | Relativa al padre | Padding/margin proporcional al texto |
| `%` | Relativa al padre | Anchos fluidos de contenedores |
| `vw` / `vh` | Relativa al viewport | Secciones hero full-screen |

**Colores:**

```css
/* Las 3 notaciones equivalentes para el mismo color */
h1 { color: rgb(220, 53, 69); }    /* RGB: 0-255 por canal */
h1 { color: #dc3545; }             /* Hexadecimal: 00-FF por canal */
h1 { color: crimson; }             /* Literal (limitado, evitar) */

/* Con transparencia (alpha) */
.overlay { background: rgba(0, 0, 0, 0.5); }   /* 50% opaco */
.card-hover { background: #0d6efd20; }          /* hex + alpha */
```

> **Buena práctica:** Usar variables CSS para los colores del proyecto → un solo lugar para cambiar toda la paleta.

---

### [F-17] CSS Box Model

**Título:** Todo elemento es una caja

```
┌─────────────────────────────────────┐
│  MARGIN (espacio externo)            │
│  ┌───────────────────────────────┐  │
│  │  BORDER (borde visible)        │  │
│  │  ┌─────────────────────────┐  │  │
│  │  │  PADDING (espacio intern │  │  │
│  │  │  ┌───────────────────┐  │  │  │
│  │  │  │  CONTENT          │  │  │  │
│  │  │  └───────────────────┘  │  │  │
│  │  └─────────────────────────┘  │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

```css
/* SIEMPRE incluir esto — evita sorpresas de ancho */
*, *::before, *::after { box-sizing: border-box; }

.card-post {
  width: 300px;       /* ancho del contenido */
  padding: 20px;      /* espacio interno */
  border: 1px solid #dee2e6;
  border-radius: 8px;
  margin-bottom: 24px; /* espacio externo abajo */
}
```

> Con `box-sizing: border-box`, el `padding` y `border` **se incluyen** dentro del `width` declarado.

---

### [F-18] CSS: Variables (Custom Properties)

**Título:** Define una vez, usa en todo el proyecto

```css
/* Declarar variables en :root → disponibles en todo el CSS */
:root {
  /* Paleta de colores */
  --color-primario:   #0d6efd;
  --color-secundario: #6c757d;
  --color-fondo:      #f8f9fa;
  --color-texto:      #212529;

  /* Tipografía */
  --fuente-principal: 'Segoe UI', system-ui, sans-serif;
  --size-base:        1rem;      /* 16px en la mayoría de browsers */

  /* Espaciado */
  --espacio-sm:  8px;
  --espacio-md:  16px;
  --espacio-lg:  32px;

  /* Bordes */
  --border-radius: 8px;
}

/* Usar las variables con var() */
body {
  font-family: var(--fuente-principal);
  color: var(--color-texto);
  background-color: var(--color-fondo);
}

.btn-custom {
  background-color: var(--color-primario);
  padding: var(--espacio-sm) var(--espacio-md);
  border-radius: var(--border-radius);
}
```

**Ventaja:** Cambiar el color primario en **una sola línea** actualiza todo el sitio.

---

### [F-19] CSS Flexbox

**Título:** Layout flexible en una dimensión

```css
/* Flex container */
.posts-row {
  display: flex;      /* activa flexbox */
  flex-wrap: wrap;    /* salto de línea automático */
  gap: 24px;          /* espacio entre items */
  justify-content: flex-start;
}

/* Flex items */
.post-card {
  flex: 1 1 280px;    /* grow shrink basis */
  min-width: 280px;
  max-width: 400px;
}
```

**Flexbox vs Bootstrap Grid:**
- **Flexbox** → CSS puro, control total
- **Bootstrap Grid** → clases predefinidas, más rápido

**Para el TP1: usá Bootstrap Grid + Flexbox en `styles.css`**

---

### [F-20] CSS Media Queries (Mobile-First)

**Título:** Responsive Design — Mobile First

```css
/* BASE: estilos para móvil (< 768px) */
.posts-grid {
  display: flex;
  flex-direction: column;  /* apilado */
  padding: 16px;
}

/* TABLET: 768px y arriba */
@media (min-width: 768px) {
  .posts-grid {
    flex-direction: row;
    flex-wrap: wrap;
  }
}

/* DESKTOP: 992px y arriba */
@media (min-width: 992px) {
  .posts-grid .card {
    width: calc(33.33% - 16px);
  }
}
```

**Mobile-first = menos código = mejor rendimiento**

---

### [F-21] CSS: DevTools del Navegador

**Título:** Tu mejor herramienta de debug

```
┌─────────────────────────────────────────────────────┐
│  F12  →  Abre DevTools                               │
├─────────────────────────────────────────────────────┤
│  Elements (Inspector)                                │
│  ├── Seleccionar elemento con 🖱️ → ver su HTML        │
│  ├── Panel Styles → ver qué CSS aplica y de dónde    │
│  ├── Editar CSS en vivo (sin guardar el archivo)     │
│  └── Ver Box Model visual (margin/border/padding)    │
├─────────────────────────────────────────────────────┤
│  Responsive Design Mode  (Ctrl+Shift+M)              │
│  ├── Simular iPhone / Android / iPad                 │
│  └── Arrastrar para probar cualquier ancho           │
├─────────────────────────────────────────────────────┤
│  Console                                             │
│  └── Ver errores de JavaScript y de recursos        │
└─────────────────────────────────────────────────────┘
```

**Flujo de trabajo recomendado:**
1. Diseñar en DevTools (cambios instantáneos, sin guardar)
2. Copiar el CSS que funciona al archivo `assets/styles.css`
3. Verificar en móvil con Responsive Design Mode antes de hacer commit

---

### [F-22] CSS: Transiciones y Hover Effects

**Título:** Animaciones sutiles con CSS puro

```css
.btn-custom {
  background-color: var(--color-primario);
  color: white;
  padding: 8px 20px;
  border: none;
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: background-color 0.2s ease, transform 0.1s ease;
}

.btn-custom:hover {
  background-color: #0b5ed7;   /* más oscuro */
  transform: translateY(-2px); /* sube 2px */
}

.btn-custom:active {
  transform: translateY(0);    /* vuelve al lugar al hacer clic */
}

/* Links de navegación */
.nav-link {
  transition: color 0.15s ease;
}
.nav-link:hover { color: var(--color-primario) !important; }

/* Cards con efecto de elevación */
.card {
  transition: box-shadow 0.2s ease, transform 0.2s ease;
}
.card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  transform: translateY(-4px);
}
```

---

### [F-23] Bootstrap: ¿Qué es y por qué usarlo?

**Título:** El framework CSS más usado del mundo

```
Sin Bootstrap                    Con Bootstrap
────────────────────            ──────────────────────────
Escribir 200 líneas CSS         Agregar 2 clases al HTML
para hacer una grilla

Inventar el Navbar               <nav class="navbar
 responsive desde cero             navbar-expand-lg">

Debugguear diferencias            Funciona igual en
entre Chrome/Safari/Firefox       todos los browsers

Media queries manuales           row-cols-1 row-cols-md-3
```

**Bootstrap provee:**
- **Sistema de grilla** de 12 columnas responsive con 6 breakpoints
- **Componentes** listos: Navbar, Card, Form, Button, Modal, Alert…
- **Utilidades** CSS: márgenes, padding, colores, flex, display…
- **JavaScript** integrado para componentes interactivos

**Versión del cursado: Bootstrap 5.3.3** (última estable, sin jQuery)

---

### [F-24] Bootstrap 5: CDN Setup

**Título:** Incluir Bootstrap en 3 líneas

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi Blog</title>
  
  <!-- ① Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" 
        rel="stylesheet">
  
  <!-- ② Tu CSS custom (DESPUÉS de Bootstrap) -->
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>

  <!-- ... contenido ... -->

  <!-- ③ Bootstrap JS (con Popper incluido) -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js">
  </script>
</body>
</html>
```

**⚠️ Tu CSS va DESPUÉS de Bootstrap para poder sobreescribir estilos**

> **CDN** = Content Delivery Network → el archivo viene del servidor de Bootstrap, el browser lo cachea y no lo descarga de nuevo.

---

### [F-25] Bootstrap: Sistema de Espaciado

**Título:** Las utilidades m y p — margin y padding

```
m = margin (externo)       p = padding (interno)

Dirección:
  t = top       b = bottom
  s = start (izquierda)   e = end (derecha)
  x = horizontal (s + e)  y = vertical (t + b)
  (sin letra) = los 4 lados

Tamaño:  0  1  2  3  4  5   auto
         0  4  8  16 24 48  auto   px (default)
```

```html
<!-- Ejemplos reales del proyecto -->
<div class="container mt-4">           <!-- margin-top: 24px -->
  <h2 class="mb-4">Posts</h2>         <!-- margin-bottom: 24px -->

  <div class="card p-3 mb-3">         <!-- padding: 16px, margin-bottom: 16px -->
    <p class="px-2 py-0 mb-0">Texto</p>
  </div>

  <footer class="mt-5 py-3">          <!-- margin-top: 48px, padding-y: 16px -->
  </footer>
</div>
```

---

### [F-26] Bootstrap: Breakpoints

**Título:** Los 6 puntos de quiebre responsive

| Nombre | Prefijo clase | Desde | Container máx |
|--------|--------------|-------|--------------|
| Extra small (móvil) | `col-` | < 576px | 100% |
| Small | `col-sm-` | ≥ 576px | 540px |
| Medium (tablet) | `col-md-` | ≥ 768px | 720px |
| Large | `col-lg-` | ≥ 992px | 960px |
| Extra large | `col-xl-` | ≥ 1200px | 1140px |
| XX large | `col-xxl-` | ≥ 1400px | 1320px |

```html
<!-- Comportamiento en cada breakpoint -->
<div class="col-12 col-sm-6 col-md-4 col-lg-3">
  ↑ móvil   ↑ tablet  ↑ desktop ↑ full-hd
  100%       50%        33%       25%
</div>
```

**Para el blog usamos principalmente `col-md-*`:**
```html
<!-- 1 columna en móvil → 3 en desktop -->
<div class="row row-cols-1 row-cols-md-3 g-4">
  <div class="col"><div class="card">...</div></div>
  <div class="col"><div class="card">...</div></div>
  <div class="col"><div class="card">...</div></div>
</div>
```

---

### [F-27] Bootstrap Grid (12 columnas)

**Título:** El sistema de grillas

```
                    12 columnas
┌──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┐
│  col-4  │  col-4  │  col-4  │
└─────────┴─────────┴─────────┘

┌──────────────┬───────┐
│    col-8     │ col-4 │
└──────────────┴───────┘

┌──┬──┬──┬──┬──┬──┬──────────────────┐
│col-2│col-2│    col-8               │
└─────┴─────┴────────────────────────┘
```

```html
<!-- 3 columnas iguales -->
<div class="container">
  <div class="row g-3">  <!-- g-3 = gap entre columnas -->
    <div class="col-12 col-md-4">Columna 1</div>
    <div class="col-12 col-md-4">Columna 2</div>
    <div class="col-12 col-md-4">Columna 3</div>
  </div>
</div>
```

---

### [F-28] Bootstrap Navbar

**Título:** Navegación responsive

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container">
    <!-- Logo / Brand -->
    <a class="navbar-brand fw-bold" href="index.html">Mi Blog</a>
    
    <!-- Botón hamburguesa (solo móvil) -->
    <button class="navbar-toggler" type="button" 
            data-bs-toggle="collapse" 
            data-bs-target="#navMenu"
            aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    
    <!-- Links -->
    <div class="collapse navbar-collapse" id="navMenu">
      <ul class="navbar-nav ms-auto">  <!-- ms-auto = derecha -->
        <li class="nav-item">
          <a class="nav-link active" href="index.html">Inicio</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="about.html">Sobre mí</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="contact.html">Contacto</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

**Claves:** `navbar-expand-lg` = colapsa en < 992px · `ms-auto` = links a la derecha · `sticky-top` = Navbar fijo al hacer scroll

---

### [F-29] Bootstrap Cards

**Título:** Componente Card para posts del blog

```html
<div class="card h-100 shadow-sm">
  <!-- Imagen superior -->
  <img src="img/post1.jpg" class="card-img-top" 
       alt="Imagen del post 1">
  
  <!-- Cuerpo de la card -->
  <div class="card-body">
    <h5 class="card-title">Título del Post</h5>
    <p class="card-text text-muted">
      Descripción breve del contenido...
    </p>
    <a href="post1.html" class="btn btn-primary btn-sm">
      Leer más
    </a>
  </div>
  
  <!-- Pie de card -->
  <div class="card-footer">
    <small class="text-muted">Publicado el 15/03/2026</small>
  </div>
</div>
```

**`flex-grow-1`** en el texto + **`mt-auto`** en el botón = el botón siempre al fondo sin importar el largo del texto.

---

### [F-30] Bootstrap Cards: Variantes

**Título:** Cards con estilos visuales adicionales

```html
<!-- Card con color de fondo (text-bg-{color}) -->
<div class="card text-bg-primary mb-3" style="max-width: 18rem;">
  <div class="card-header">Destacado</div>
  <div class="card-body">
    <h5 class="card-title">Post especial</h5>
    <p class="card-text">Nota importante del blog.</p>
  </div>
</div>

<!-- Card con solo borde de color -->
<div class="card border-success mb-3">
  <div class="card-header text-success">Completado</div>
  <div class="card-body">
    <p class="card-text text-success">TP entregado con éxito.</p>
  </div>
</div>

<!-- Grid de cards con row-cols -->
<div class="row row-cols-1 row-cols-md-3 g-4">
  <div class="col">
    <div class="card h-100">...</div>
  </div>
  <!-- se repite para cada card -->
</div>
```

**Colores disponibles:** `primary` `secondary` `success` `danger` `warning` `info` `light` `dark`

---

### [F-31] Bootstrap Forms

**Título:** Formulario de contacto accesible

```html
<form>
  <div class="mb-3">
    <label for="nombre" class="form-label">Nombre</label>
    <input type="text" class="form-control" 
           id="nombre" name="nombre" 
           placeholder="Tu nombre completo"
           required>
  </div>
  
  <div class="mb-3">
    <label for="email" class="form-label">Email</label>
    <input type="email" class="form-control" 
           id="email" name="email"
           placeholder="tu@email.com"
           required>
  </div>
  
  <div class="mb-3">
    <label for="telefono" class="form-label">Teléfono <small class="text-muted">(opcional)</small></label>
    <input type="tel" class="form-control" 
           id="telefono" name="telefono"
           placeholder="+54 9 2901 000000">
  </div>
  
  <div class="mb-3">
    <label for="mensaje" class="form-label">Mensaje</label>
    <textarea class="form-control" id="mensaje" 
              name="mensaje" rows="5"
              minlength="10" required></textarea>
  </div>
  
  <div class="d-grid">
    <button type="submit" class="btn btn-primary btn-lg">
      Enviar mensaje
    </button>
  </div>
</form>
```

---

### [F-32] Bootstrap: Utilidades esenciales

**Título:** Las clases utilitarias más usadas en el blog

**Display y Flexbox:**
```html
<div class="d-flex justify-content-between align-items-center">
<div class="d-grid gap-2">           <!-- botones full-width -->
<div class="d-none d-md-block">      <!-- oculto en móvil -->
```

**Texto:**
```html
<p class="text-muted">Texto gris secundario</p>
<p class="text-primary fw-bold">Azul en negrita</p>
<p class="text-center fs-5">Centrado, tamaño 5</p>
<p class="text-truncate" style="max-width: 200px;">Texto largo…</p>
```

**Fondos, Bordes y Sombras:**
```html
<div class="bg-light border rounded-3 p-3">
<div class="bg-dark text-light rounded p-4">
<div class="shadow-sm">   <!-- sombra sutil (cards) -->
<div class="shadow-lg">   <!-- sombra grande (modals) -->
```

**Width / Height:**
```html
<div class="w-100">      <!-- width: 100% -->
<div class="h-100">      <!-- height: 100% (cards igual alto) -->
<img class="img-fluid">  <!-- max-width: 100%, responsive -->
```

---

### [F-33] Validación con CSS :valid/:invalid

**Título:** Feedback visual de formulario con CSS puro

```css
/* styles.css */

/* Campo válido → borde verde */
.form-control:valid:not(:placeholder-shown) {
  border-color: #198754;
  box-shadow: 0 0 0 0.25rem rgba(25, 135, 84, 0.25);
}

/* Campo inválido → borde rojo */
.form-control:invalid:not(:placeholder-shown) {
  border-color: #dc3545;
  box-shadow: 0 0 0 0.25rem rgba(220, 53, 69, 0.25);
}
```

**Explicación:**
- `:valid` → cuando el valor cumple las restricciones HTML5
- `:invalid` → cuando no cumple (email mal formado, required vacío)
- `:not(:placeholder-shown)` → no mostrar errores hasta que el usuario empiece a escribir

| Pseudo-clase | Cuándo activa |
|--------------|---------------|
| `:valid` | El valor cumple las restricciones HTML5 (`required`, `type="email"`, `minlength`) |
| `:invalid` | No cumple las restricciones |
| `:not(:placeholder-shown)` | El usuario ya escribió algo (campo no vacío) |

---

### [F-34] Git: Flujo de trabajo con Classroom

**Título:** Del link al commit — paso a paso

```
1. ACEPTAR el TP
   → Ir a classroom.github.com/a/RI8vnIt_
   → "Accept this assignment"
   → GitHub crea: github.com/lab-lenguajes-2026/tp1-blog-TuUsuario

2. CLONAR el repo
   $ git clone https://github.com/lab-lenguajes-2026/tp1-blog-TuUsuario.git
   $ cd tp1-blog-TuUsuario

3. CREAR la estructura
   → Crear index.html, about.html, contact.html, assets/styles.css

4. CICLO de trabajo (repetir para cada funcionalidad)
   $ git add index.html
   $ git commit -m "feat: agregar navbar Bootstrap 5 responsive"
   $ git push

5. VERIFICAR en GitHub.com que el archivo está actualizado
```

**Mensajes de commit recomendados:**
```
feat: estructura base HTML + Bootstrap CDN
feat: navbar responsive con hamburguesa
feat: grid de 3 cards en index.html
feat: formulario de contacto con validación
style: CSS custom — variables, :valid/:invalid, transiciones
docs: agregar README y PROMPTS.md con 5 prompts
```

---

### [F-35] Estructura de archivos del TP1

**Título:** Organización del proyecto

```
mi-blog/
├── index.html          ← Lista de posts (cards)
├── about.html          ← Sobre el autor
├── contact.html        ← Formulario de contacto
├── assets/
│   ├── styles.css      ← Estilos custom
│   └── images/
│       ├── favicon.ico
│       ├── avatar.jpg
│       └── post1.jpg
├── README.md           ← Instrucciones del proyecto
└── PROMPTS.md          ← OBLIGATORIO: registro de IA
```

**En Git (GitHub Classroom):**
```
feat: agregar estructura base HTML + Bootstrap
style: aplicar estilos custom en styles.css
feat: navbar responsive con Bootstrap 5
feat: grid de cards para lista de posts
feat: formulario de contacto con validación
docs: documentar prompts de Copilot en PROMPTS.md
```

---

### [F-36] Checklist TP1

**Título:** ¿Estoy listo para entregar?

```
ARCHIVOS
  ☐ index.html — Navbar + grid de cards (≥3 posts)
  ☐ about.html — Información del autor
  ☐ contact.html — Formulario con Bootstrap + campo teléfono
  ☐ assets/styles.css — Estilos custom + media queries
  ☐ assets/images/ — favicon.ico + imágenes del blog
  ☐ README.md — Instrucciones del proyecto
  ☐ PROMPTS.md — ≥5 prompts documentados

HTML
  ☐ Estructura semántica (header/main/footer)
  ☐ Bootstrap incluido via CDN
  ☐ Viewport meta en todos los HTMLs
  ☐ W3C Validator: sin errores ✓

CSS
  ☐ Variables CSS (≥2: --color-primario, --font-principal...)
  ☐ Media queries mobile (<768px) y desktop (≥768px)
  ☐ :valid/:invalid en el formulario
  ☐ Transiciones en hover de botones/links

GIT
  ☐ ≥ 5 commits con mensajes descriptivos
  ☐ Pushes al repositorio de Classroom
```

---

### [F-37] Recursos y documentación

**Título:** Donde buscar ayuda

| Recurso | Para qué |
|---------|----------|
| MDN HTML | Referencia oficial de etiquetas y semántica |
| MDN CSS | Referencia oficial de propiedades y selectores |
| Bootstrap 5 Docs | Clases y componentes de Bootstrap |
| W3C Validator | Verificar que el HTML está bien |
| MDN Web Docs | Documentación detallada técnica |
| GitHub Copilot | Generar código con prompts |

**Horarios de consulta:** (completar con el docente)

**Campus virtual:** (completar con link)

**En clase:** podés abrir issues en tu repo de Classroom para marcar dudas.

---

### [F-38] TPs activos — Links y entregas

**Título:** TPs de las primeras semanas

| TP | Tema | Entrega | Link de Classroom |
|----|------|---------|-------------------|
| **TP1** | Blog Personal HTML/CSS/Bootstrap | **31/3 · 23hs** | classroom.github.com/a/RI8vnIt_ |
| **TP2** | Introducción a Python | **31/3 · 23hs** | classroom.github.com/a/X4xiTEDQ |
| **TP3** | Tests Unitarios con pytest | **7/4 · 23hs** | classroom.github.com/a/jLxPRyso |

> Para aceptar cada TP: accedé al link → "Accept this assignment" → te crea un repo personal

**TP4 próximamente:**
- Django ORM · Entrega 14/4 · 23hs · classroom.github.com/a/mZttlvBE

---

### [F-39] Próxima clase

**Título:** Semana 2 — Python 3.13

```
Semana 1 ✅ HTML + CSS + Bootstrap (HOY)
Semana 2    Python 3.13 — Fundamentos

Qué viene:
• Variables y tipos de datos
• Control de flujo (if/for/while)
• Funciones y módulos
• Git branches + pull requests

TPs que siguen corriendo:
• TP1 (Blog HTML)  → 31/3 23hs · classroom.github.com/a/RI8vnIt_
• TP2 (Python)     → 31/3 23hs · classroom.github.com/a/X4xiTEDQ
• TP3 (pytest)     →  7/4 23hs · classroom.github.com/a/jLxPRyso
```

**Tip:** Avanzar con el TP1 mientras el material de hoy está fresco — al menos completar la estructura base y el Navbar.
