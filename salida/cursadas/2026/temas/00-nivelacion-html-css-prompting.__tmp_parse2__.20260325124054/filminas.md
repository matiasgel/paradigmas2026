# Filminas â€” Tema 00: NivelaciÃ³n HTML/CSS/Bootstrap 5
## IF009 Laboratorio de ProgramaciÃ³n y Lenguajes â€” UNTDF IDEI 2026

> **Nota:** Este documento es el guiÃ³n de filminas complementario a las ya presentadas en clase (basadas en `HTML & CSS.pdf`). El docente puede usar estas filminas como repaso, seleccionar slides especÃ­ficos o usarlos para el bloque de prÃ¡ctica.

---

### [F-01] Portada

**TÃ­tulo:** NivelaciÃ³n HTML / CSS / Bootstrap 5

**SubtÃ­tulo:** Laboratorio de ProgramaciÃ³n y Lenguajes Â· Semana 1

**Pie:** UNTDF IDEI Â· 2026 Â· Prof. ______

---

### [F-02] Â¿QuÃ© vamos a construir?

**TÃ­tulo:** El proyecto de esta semana

```
[IMAGEN: Wireframe de un blog en 3 dispositivos]

  ðŸ“± MÃ³vil          ðŸ’» Tablet          ðŸ–¥ï¸ Desktop
  â”Œâ”€â”€â”€â”€â”€â”€â”          â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”       â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
  â”‚Navbar â”‚          â”‚  Navbar  â”‚       â”‚     Navbar     â”‚
  â”œâ”€â”€â”€â”€â”€â”€â”¤          â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤       â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
  â”‚ Card â”‚          â”‚Cardâ”‚Card â”‚       â”‚Card â”‚Cardâ”‚Card â”‚
  â”‚      â”‚          â”‚    â”‚     â”‚       â”‚     â”‚    â”‚     â”‚
  â”‚ Card â”‚          â”‚Cardâ”‚Card â”‚       â”œâ”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”¤
  â”‚      â”‚          â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜       â”‚     Footer     â”‚
  â”‚Footerâ”‚                             â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
  â””â”€â”€â”€â”€â”€â”€â”˜
```

**Un blog personal con:**
- `index.html` â€” lista de posts (cards Bootstrap)
- `about.html` â€” sobre el autor
- `contact.html` â€” formulario de contacto con validaciÃ³n CSS
- `assets/styles.css` â€” estilos custom + media queries
- TP1: entrega vÃ­a **GitHub Classroom**

---

### [F-03] El Stack del Cuatrimestre

**TÃ­tulo:** Â¿Por quÃ© HTML/CSS ahora?

```
Semana 1-2  â†’  HTML + CSS + Bootstrap   â† HOY
Semana 3    â†’  Python 3.13 fundamentos
Semana 5    â†’  Django 5.1 (web framework)
Semana 7    â†’  Django Templates (â†” HTML â† acÃ¡ se une)
Semana 11   â†’  Django Auth + Admin
Semana 15   â†’  REST APIs
```

**El HTML que aprenden hoy aparece de nuevo en Django Templates.**

> Las variables de Python `{{ nombre }}` y los bloques `{% block %}` son exactamente la estructura que ven hoy, pero con datos dinÃ¡micos.

---

### [F-04] Tu nuevo copiloto: GitHub Copilot

**TÃ­tulo:** IA como herramienta, no como sustituto

```
Buen prompt = Buen cÃ³digo

âŒ "Haceme una web"
âœ… "Crea un Navbar Bootstrap 5 con logo y 3 links:
    Inicio, Sobre mÃ­, Contacto. Que sea responsive
    y colapse en dispositivos mÃ³viles."
```

**La regla del cursado:**
> PodÃ©s usar IA. **DebÃ©s entender lo que usÃ¡s.**
> Cada TP requiere `PROMPTS.md` documentando el proceso.

**No alcanza con copiar y pegar â€” el docente puede preguntar sobre cualquier lÃ­nea de cÃ³digo.**

---

### [F-05] PROMPTS.md â€” Formato

**TÃ­tulo:** CÃ³mo documentar el uso de IA

```markdown
## Prompt 1 â€” Navbar Bootstrap

**Fecha:** 15/03/2026
**Herramienta:** GitHub Copilot

**Lo que pedÃ­:**
> Crear un navbar bootstrap 5 responsive con 3 links

**Lo que recibÃ­:**
[snippet del cÃ³digo]

**Lo que modifiquÃ©:**
- CambiÃ© el texto de los links a espaÃ±ol
- AgreguÃ© aria-label al botÃ³n de toggle
- AgreguÃ© la clase ms-auto para alinear a la derecha

**Por quÃ© lo modifiquÃ©:**
Los links estaban en inglÃ©s y faltaba accesibilidad
```

**MÃ­nimo requerido: 5 prompts completos con este formato**

---

### [F-06] Â¿QuÃ© es HTML?

**TÃ­tulo:** HyperText Markup Language

```
Marcado     â†’ usa <etiquetas> para etiquetar contenido
Hipertexto  â†’ vÃ­nculos (enlaces) entre contenidos y pÃ¡ginas
```

**Define la ESTRUCTURA de una pÃ¡gina web:**

| HTML define... | Ejemplos |
|----------------|----------|
| Estructura | pÃ¡rrafos, encabezados, tablas, listas |
| Contenido | textos, imÃ¡genes, links, videos |
| **No** define | colores, fuentes, mÃ¡rgenes (eso es CSS) |

```html
<!DOCTYPE html>       <!-- declara HTML5 al navegador -->
<html lang="es">      <!-- raÃ­z del documento, idioma espaÃ±ol -->
<head>
    <meta charset="UTF-8">
    <title>Un tÃ­tulo</title>    <!-- aparece en la pestaÃ±a -->
</head>
<body>
    <p>Un pÃ¡rrafo</p>           <!-- contenido visible -->
</body>
</html>
```

---

### [F-07] HTML: Elementos y Tags

**TÃ­tulo:** La anatomÃ­a de un elemento HTML

```
         tag de apertura    contenido    tag de cierre
              â†“                 â†“              â†“
         <p>               Un pÃ¡rrafo         </p>

Elemento completo: <p>Un pÃ¡rrafo</p>
```

**Elementos sin tag de cierre (auto-closing):**
```html
<img src="foto.jpg" alt="descripciÃ³n">
<input type="text" placeholder="Tu nombre">
<br>
<hr>
```

**Tags mÃ¡s usados:**

| Tag | Para quÃ© | Ejemplo |
|-----|----------|---------|
| `<h1>`â€“`<h6>` | Encabezados | `<h1>TÃ­tulo principal</h1>` |
| `<p>` | PÃ¡rrafo | `<p>Texto...</p>` |
| `<a>` | Enlace | `<a href="about.html">Sobre mÃ­</a>` |
| `<img>` | Imagen | `<img src="foto.jpg" alt="Foto">` |
| `<ul>` / `<li>` | Lista no ordenada | `<ul><li>Ãtem</li></ul>` |
| `<div>` | Contenedor bloque genÃ©rico | `<div class="card">...</div>` |
| `<span>` | Contenedor inline genÃ©rico | `<span class="badge">Nuevo</span>` |

---

### [F-08] HTML: Atributos esenciales

**TÃ­tulo:** Los atributos dan informaciÃ³n extra al elemento

```
               atributo    valor
                  â†“          â†“
<a href="about.html" class="nav-link" id="link-about">
   Sobre mÃ­
</a>
```

**Atributos globales (van en cualquier elemento):**

| Atributo | FunciÃ³n | Ejemplo |
|----------|---------|--------|
| `id` | Identificador Ãºnico en la pÃ¡gina | `id="navbar"` |
| `class` | Clase(s) CSS (puede repetirse) | `class="card shadow-sm"` |
| `style` | CSS inline (evitar en producciÃ³n) | `style="color: red"` |

**Atributos especÃ­ficos por tag:**

| Tag | Atributo | Para quÃ© |
|-----|----------|----------|
| `<a>` | `href` | URL de destino |
| `<img>` | `src`, `alt` | Fuente e imagen alternativa |
| `<input>` | `type`, `placeholder`, `required` | Tipo, hint, obligatoriedad |
| `<form>` | `action`, `method` | Destino y mÃ©todo HTTP |
| `<link>` | `rel`, `href` | Tipo de recurso y ruta |

> **El atributo `alt` en imÃ¡genes es OBLIGATORIO** para accesibilidad y SEO.

---

### [F-09] HTML: El Ã¡rbol DOM

**TÃ­tulo:** CÃ³mo HTML forma una estructura de Ã¡rbol

```
document
â””â”€â”€ html
    â”œâ”€â”€ head
    â”‚   â”œâ”€â”€ meta (charset)
    â”‚   â”œâ”€â”€ meta (viewport)
    â”‚   â”œâ”€â”€ title
    â”‚   â””â”€â”€ link (stylesheet)
    â””â”€â”€ body
        â”œâ”€â”€ header
        â”‚   â””â”€â”€ nav
        â”‚       â”œâ”€â”€ a.navbar-brand  â† hijo de nav
        â”‚       â””â”€â”€ ul.navbar-nav
        â”‚           â”œâ”€â”€ li.nav-item â† hermanos entre sÃ­
        â”‚           â””â”€â”€ li.nav-item
        â”œâ”€â”€ main
        â”‚   â””â”€â”€ section
        â”‚       â””â”€â”€ div.row
        â”‚           â”œâ”€â”€ article.col-md-4 â† hermanos
        â”‚           â”œâ”€â”€ article.col-md-4
        â”‚           â””â”€â”€ article.col-md-4
        â””â”€â”€ footer
```

**Conceptos clave:**
- **parent** â†’ el elemento que contiene a otro (`nav` es parent de `ul`)
- **child/hijo** â†’ elemento dentro de otro (`ul` es child de `nav`)
- **siblings/hermanos** â†’ elementos al mismo nivel (`li` son hermanos entre sÃ­)

---

### [F-10] HTML5: SemÃ¡ntica vs Divitis

**TÃ­tulo:** El problema del `<div>` genÃ©rico

```
âŒ HTML sin semÃ¡ntica (divitis)     âœ… HTML semÃ¡ntico
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€         â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
<div id="header">                  <header>
  <div id="menu">...</div>           <nav>...</nav>
</div>                             </header>
<div id="content">                 <main>
  <div class="post">...</div>        <article>...</article>
</div>                             </main>
<div id="footer">...</div>         <footer>...</footer>
```

**Â¿Por quÃ© importa?**
- ðŸ‘ï¸ **Lectores de pantalla** entienden la estructura â†’ accesibilidad real
- ðŸ” **SEO**: Google/Bing indexan mejor el contenido semÃ¡ntico
- ðŸ‘¨â€ðŸ’» **Mantenibilidad**: cÃ³digo que se puede leer 6 meses despuÃ©s

---

### [F-11] HTML5: Elementos semÃ¡nticos

**TÃ­tulo:** El vocabulario de la estructura web

| Elemento | DescripciÃ³n | Ejemplo de uso |
|----------|-------------|----------------|
| `<header>` | Cabecera de pÃ¡gina/secciÃ³n | Logo + Navbar |
| `<nav>` | Bloque de navegaciÃ³n | MenÃº principal |
| `<main>` | Contenido principal (1 por pÃ¡gina) | La secciÃ³n de posts |
| `<section>` | SecciÃ³n temÃ¡tica | "Mis Ãºltimos posts" |
| `<article>` | Contenido independiente y reutilizable | Un post del blog |
| `<aside>` | Contenido complementario lateral | Sidebar con categorÃ­as |
| `<footer>` | Pie de pÃ¡gina/secciÃ³n | Copyright, redes sociales |
| `<figure>` | Imagen con descripciÃ³n | IlustraciÃ³n de un post |
| `<figcaption>` | Leyenda de una `<figure>` | "Foto tomada en Ushuaia" |

**Regla:** Solo un `<main>` por pÃ¡gina. `<header>` y `<footer>` pueden repetirse dentro de `<article>` o `<section>`.

---

### [F-12] HTML5: AnatomÃ­a del documento completo

**TÃ­tulo:** Estructura base lista para usar

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <!-- CodificaciÃ³n obligatoria -->
  <meta charset="UTF-8">

  <!-- OBLIGATORIO para Bootstrap responsive -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- SEO bÃ¡sico -->
  <meta name="description" content="Blog personal â€” UNTDF 2026">
  <meta name="author" content="Tu Nombre">

  <title>Mi Blog Personal</title>

  <!-- Favicon -->
  <link rel="icon" type="image/x-icon" href="assets/images/favicon.ico">

  <!-- Bootstrap CSS (primero) -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        rel="stylesheet">

  <!-- CSS custom (despuÃ©s de Bootstrap para poder sobreescribir) -->
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>

  <!-- contenido aquÃ­ -->

  <!-- Bootstrap JS al final del body -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js">
  </script>
</body>
</html>
```

---

### [F-13] Estructura del Blog (HTML completo)

**TÃ­tulo:** Arquitectura del proyecto TP1

```html
<body>
  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <!-- Bootstrap Navbar responsive -->
    </nav>
  </header>

  <main class="container mt-4">
    <section id="posts">
      <h2 class="mb-4">Mis Ãºltimos posts</h2>
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <article class="col">
          <div class="card h-100 shadow-sm">
            <!-- Card Bootstrap completa -->
          </div>
        </article>
        <!-- mÃ¡s articles/cards -->
      </div>
    </section>
  </main>

  <footer class="bg-dark text-light mt-5 py-3">
    <div class="container text-center">
      <p class="mb-0">Â© 2026 Mi Blog Â· UNTDF Â· Laboratorio de Lenguajes</p>
    </div>
  </footer>
</body>
```

**`row-cols-1 row-cols-md-3`** = 1 columna en mÃ³vil, 3 columnas en desktop

---

### [F-14] Â¿QuÃ© es CSS?

**TÃ­tulo:** Cascading Style Sheets

**CSS controla TODO lo visual de la pÃ¡gina:**

| Controla | Ejemplos |
|----------|---------|
| Color | `color: #333; background-color: #f8f9fa;` |
| TipografÃ­a | `font-size: 1.2rem; font-weight: bold;` |
| Espaciado | `margin: 16px; padding: 8px 16px;` |
| DisposiciÃ³n | `display: flex; grid-template-columns: ...` |
| Responsive | `@media (min-width: 768px) { ... }` |
| Animaciones | `transition: all 0.3s ease;` |

**Regla CSS = Selector + Declaraciones:**

```css
           selector
              â†“
h1 { color: #CC9900; font-size: 2rem; }
     â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
           declaraciones
           (propiedad: valor;)
```

> **"Cascading"** = cuando mÃºltiples reglas aplican al mismo elemento, gana la mÃ¡s especÃ­fica.

---

### [F-15] CSS: Selectores

**TÃ­tulo:** CÃ³mo apuntar a los elementos

```css
/* 1. Selector de ELEMENTO â€” aplica a todos los h1 */
h1 { color: #333; }

/* 2. Selector de CLASE â€” aplica a todo lo que tenga class="card" */
.card { border-radius: 8px; }

/* 3. Selector de ID â€” aplica solo al elemento con id="navbar" */
#navbar { background-color: white; }

/* 4. Selector DESCENDIENTE â€” solo p dentro de article */
article p { line-height: 1.7; }

/* 5. Selector de HIJO DIRECTO */
nav > ul { list-style: none; }

/* 6. Selector de ATRIBUTO */
input[type="email"] { border-color: #0d6efd; }

/* 7. Pseudo-clase */
a:hover { color: #0d6efd; text-decoration: underline; }
button:focus { outline: 2px solid #0d6efd; }
```

**Especificidad (quiÃ©n gana cuando hay conflicto):**
```
!important > inline style > #id > .class > element
    âˆž              1000       100     10       1
```

---

### [F-16] CSS: Unidades y Colores

**TÃ­tulo:** NÃºmeros en CSS â€” cuÃ¡l usar cuÃ¡ndo

**Unidades de medida:**

| Unidad | Tipo | CuÃ¡ndo usar |
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

> **Buena prÃ¡ctica:** Usar variables CSS para los colores del proyecto â†’ un solo lugar para cambiar toda la paleta.

---

### [F-17] CSS Box Model

**TÃ­tulo:** Todo elemento es una caja

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  MARGIN (espacio externo)            â”‚
â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”‚
â”‚  â”‚  BORDER (borde visible)        â”‚  â”‚
â”‚  â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”‚  â”‚
â”‚  â”‚  â”‚  PADDING (espacio intern â”‚  â”‚  â”‚
â”‚  â”‚  â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”‚  â”‚  â”‚
â”‚  â”‚  â”‚  â”‚  CONTENT          â”‚  â”‚  â”‚  â”‚
â”‚  â”‚  â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â”‚  â”‚  â”‚
â”‚  â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â”‚  â”‚
â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

```css
/* SIEMPRE incluir esto â€” evita sorpresas de ancho */
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

**TÃ­tulo:** Define una vez, usa en todo el proyecto

```css
/* Declarar variables en :root â†’ disponibles en todo el CSS */
:root {
  /* Paleta de colores */
  --color-primario:   #0d6efd;
  --color-secundario: #6c757d;
  --color-fondo:      #f8f9fa;
  --color-texto:      #212529;

  /* TipografÃ­a */
  --fuente-principal: 'Segoe UI', system-ui, sans-serif;
  --size-base:        1rem;      /* 16px en la mayorÃ­a de browsers */

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

**Ventaja:** Cambiar el color primario en **una sola lÃ­nea** actualiza todo el sitio.

---

### [F-19] CSS Flexbox

**TÃ­tulo:** Layout flexible en una dimensiÃ³n

```css
/* Flex container */
.posts-row {
  display: flex;      /* activa flexbox */
  flex-wrap: wrap;    /* salto de lÃ­nea automÃ¡tico */
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
- **Flexbox** â†’ CSS puro, control total
- **Bootstrap Grid** â†’ clases predefinidas, mÃ¡s rÃ¡pido

**Para el TP1: usÃ¡ Bootstrap Grid + Flexbox en `styles.css`**

---

### [F-20] CSS Media Queries (Mobile-First)

**TÃ­tulo:** Responsive Design â€” Mobile First

```css
/* BASE: estilos para mÃ³vil (< 768px) */
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

**Mobile-first = menos cÃ³digo = mejor rendimiento**

---

### [F-21] CSS: DevTools del Navegador

**TÃ­tulo:** Tu mejor herramienta de debug

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  F12  â†’  Abre DevTools                               â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚  Elements (Inspector)                                â”‚
â”‚  â”œâ”€â”€ Seleccionar elemento con ðŸ–±ï¸ â†’ ver su HTML        â”‚
â”‚  â”œâ”€â”€ Panel Styles â†’ ver quÃ© CSS aplica y de dÃ³nde    â”‚
â”‚  â”œâ”€â”€ Editar CSS en vivo (sin guardar el archivo)     â”‚
â”‚  â””â”€â”€ Ver Box Model visual (margin/border/padding)    â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚  Responsive Design Mode  (Ctrl+Shift+M)              â”‚
â”‚  â”œâ”€â”€ Simular iPhone / Android / iPad                 â”‚
â”‚  â””â”€â”€ Arrastrar para probar cualquier ancho           â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚  Console                                             â”‚
â”‚  â””â”€â”€ Ver errores de JavaScript y de recursos        â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

**Flujo de trabajo recomendado:**
1. DiseÃ±ar en DevTools (cambios instantÃ¡neos, sin guardar)
2. Copiar el CSS que funciona al archivo `assets/styles.css`
3. Verificar en mÃ³vil con Responsive Design Mode antes de hacer commit

---

### [F-22] CSS: Transiciones y Hover Effects

**TÃ­tulo:** Animaciones sutiles con CSS puro

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
  background-color: #0b5ed7;   /* mÃ¡s oscuro */
  transform: translateY(-2px); /* sube 2px */
}

.btn-custom:active {
  transform: translateY(0);    /* vuelve al lugar al hacer clic */
}

/* Links de navegaciÃ³n */
.nav-link {
  transition: color 0.15s ease;
}
.nav-link:hover { color: var(--color-primario) !important; }

/* Cards con efecto de elevaciÃ³n */
.card {
  transition: box-shadow 0.2s ease, transform 0.2s ease;
}
.card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  transform: translateY(-4px);
}
```

---

### [F-23] Bootstrap: Â¿QuÃ© es y por quÃ© usarlo?

**TÃ­tulo:** El framework CSS mÃ¡s usado del mundo

```
Sin Bootstrap                    Con Bootstrap
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€            â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
Escribir 200 lÃ­neas CSS         Agregar 2 clases al HTML
para hacer una grilla

Inventar el Navbar               <nav class="navbar
 responsive desde cero             navbar-expand-lg">

Debugguear diferencias            Funciona igual en
entre Chrome/Safari/Firefox       todos los browsers

Media queries manuales           row-cols-1 row-cols-md-3
```

**Bootstrap provee:**
- **Sistema de grilla** de 12 columnas responsive con 6 breakpoints
- **Componentes** listos: Navbar, Card, Form, Button, Modal, Alertâ€¦
- **Utilidades** CSS: mÃ¡rgenes, padding, colores, flex, displayâ€¦
- **JavaScript** integrado para componentes interactivos

**VersiÃ³n del cursado: Bootstrap 5.3.3** (Ãºltima estable, sin jQuery)

---

### [F-24] Bootstrap 5: CDN Setup

**TÃ­tulo:** Incluir Bootstrap en 3 lÃ­neas

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi Blog</title>
  
  <!-- â‘  Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" 
        rel="stylesheet">
  
  <!-- â‘¡ Tu CSS custom (DESPUÃ‰S de Bootstrap) -->
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>

  <!-- ... contenido ... -->

  <!-- â‘¢ Bootstrap JS (con Popper incluido) -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js">
  </script>
</body>
</html>
```

**âš ï¸ Tu CSS va DESPUÃ‰S de Bootstrap para poder sobreescribir estilos**

> **CDN** = Content Delivery Network â†’ el archivo viene del servidor de Bootstrap, el browser lo cachea y no lo descarga de nuevo.

---

### [F-25] Bootstrap: Sistema de Espaciado

**TÃ­tulo:** Las utilidades m y p â€” margin y padding

```
m = margin (externo)       p = padding (interno)

DirecciÃ³n:
  t = top       b = bottom
  s = start (izquierda)   e = end (derecha)
  x = horizontal (s + e)  y = vertical (t + b)
  (sin letra) = los 4 lados

TamaÃ±o:  0  1  2  3  4  5   auto
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

**TÃ­tulo:** Los 6 puntos de quiebre responsive

| Nombre | Prefijo clase | Desde | Container mÃ¡x |
|--------|--------------|-------|--------------|
| Extra small (mÃ³vil) | `col-` | < 576px | 100% |
| Small | `col-sm-` | â‰¥ 576px | 540px |
| Medium (tablet) | `col-md-` | â‰¥ 768px | 720px |
| Large | `col-lg-` | â‰¥ 992px | 960px |
| Extra large | `col-xl-` | â‰¥ 1200px | 1140px |
| XX large | `col-xxl-` | â‰¥ 1400px | 1320px |

```html
<!-- Comportamiento en cada breakpoint -->
<div class="col-12 col-sm-6 col-md-4 col-lg-3">
  â†‘ mÃ³vil   â†‘ tablet  â†‘ desktop â†‘ full-hd
  100%       50%        33%       25%
</div>
```

**Para el blog usamos principalmente `col-md-*`:**
```html
<!-- 1 columna en mÃ³vil â†’ 3 en desktop -->
<div class="row row-cols-1 row-cols-md-3 g-4">
  <div class="col"><div class="card">...</div></div>
  <div class="col"><div class="card">...</div></div>
  <div class="col"><div class="card">...</div></div>
</div>
```

---

### [F-27] Bootstrap Grid (12 columnas)

**TÃ­tulo:** El sistema de grillas

```
                    12 columnas
â”Œâ”€â”€â”¬â”€â”€â”¬â”€â”€â”¬â”€â”€â”¬â”€â”€â”¬â”€â”€â”¬â”€â”€â”¬â”€â”€â”¬â”€â”€â”¬â”€â”€â”¬â”€â”€â”¬â”€â”€â”
â”‚  col-4  â”‚  col-4  â”‚  col-4  â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜

â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”
â”‚    col-8     â”‚ col-4 â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”˜

â”Œâ”€â”€â”¬â”€â”€â”¬â”€â”€â”¬â”€â”€â”¬â”€â”€â”¬â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚col-2â”‚col-2â”‚    col-8               â”‚
â””â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
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

**TÃ­tulo:** NavegaciÃ³n responsive

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container">
    <!-- Logo / Brand -->
    <a class="navbar-brand fw-bold" href="index.html">Mi Blog</a>
    
    <!-- BotÃ³n hamburguesa (solo mÃ³vil) -->
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
          <a class="nav-link" href="about.html">Sobre mÃ­</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="contact.html">Contacto</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

**Claves:** `navbar-expand-lg` = colapsa en < 992px Â· `ms-auto` = links a la derecha Â· `sticky-top` = Navbar fijo al hacer scroll

---

### [F-29] Bootstrap Cards

**TÃ­tulo:** Componente Card para posts del blog

```html
<div class="card h-100 shadow-sm">
  <!-- Imagen superior -->
  <img src="img/post1.jpg" class="card-img-top" 
       alt="Imagen del post 1">
  
  <!-- Cuerpo de la card -->
  <div class="card-body">
    <h5 class="card-title">TÃ­tulo del Post</h5>
    <p class="card-text text-muted">
      DescripciÃ³n breve del contenido...
    </p>
    <a href="post1.html" class="btn btn-primary btn-sm">
      Leer mÃ¡s
    </a>
  </div>
  
  <!-- Pie de card -->
  <div class="card-footer">
    <small class="text-muted">Publicado el 15/03/2026</small>
  </div>
</div>
```

**`flex-grow-1`** en el texto + **`mt-auto`** en el botÃ³n = el botÃ³n siempre al fondo sin importar el largo del texto.

---

### [F-30] Bootstrap Cards: Variantes

**TÃ­tulo:** Cards con estilos visuales adicionales

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
    <p class="card-text text-success">TP entregado con Ã©xito.</p>
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

**TÃ­tulo:** Formulario de contacto accesible

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
    <label for="telefono" class="form-label">TelÃ©fono <small class="text-muted">(opcional)</small></label>
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

**TÃ­tulo:** Las clases utilitarias mÃ¡s usadas en el blog

**Display y Flexbox:**
```html
<div class="d-flex justify-content-between align-items-center">
<div class="d-grid gap-2">           <!-- botones full-width -->
<div class="d-none d-md-block">      <!-- oculto en mÃ³vil -->
```

**Texto:**
```html
<p class="text-muted">Texto gris secundario</p>
<p class="text-primary fw-bold">Azul en negrita</p>
<p class="text-center fs-5">Centrado, tamaÃ±o 5</p>
<p class="text-truncate" style="max-width: 200px;">Texto largoâ€¦</p>
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

### [F-33] ValidaciÃ³n con CSS :valid/:invalid

**TÃ­tulo:** Feedback visual de formulario con CSS puro

```css
/* styles.css */

/* Campo vÃ¡lido â†’ borde verde */
.form-control:valid:not(:placeholder-shown) {
  border-color: #198754;
  box-shadow: 0 0 0 0.25rem rgba(25, 135, 84, 0.25);
}

/* Campo invÃ¡lido â†’ borde rojo */
.form-control:invalid:not(:placeholder-shown) {
  border-color: #dc3545;
  box-shadow: 0 0 0 0.25rem rgba(220, 53, 69, 0.25);
}
```

**ExplicaciÃ³n:**
- `:valid` â†’ cuando el valor cumple las restricciones HTML5
- `:invalid` â†’ cuando no cumple (email mal formado, required vacÃ­o)
- `:not(:placeholder-shown)` â†’ no mostrar errores hasta que el usuario empiece a escribir

| Pseudo-clase | CuÃ¡ndo activa |
|--------------|---------------|
| `:valid` | El valor cumple las restricciones HTML5 (`required`, `type="email"`, `minlength`) |
| `:invalid` | No cumple las restricciones |
| `:not(:placeholder-shown)` | El usuario ya escribiÃ³ algo (campo no vacÃ­o) |

---

### [F-34] Git: Flujo de trabajo con Classroom

**TÃ­tulo:** Del link al commit â€” paso a paso

```
1. ACEPTAR el TP
   â†’ Ir a classroom.github.com/a/RI8vnIt_
   â†’ "Accept this assignment"
   â†’ GitHub crea: github.com/lab-lenguajes-2026/tp1-blog-TuUsuario

2. CLONAR el repo
   $ git clone https://github.com/lab-lenguajes-2026/tp1-blog-TuUsuario.git
   $ cd tp1-blog-TuUsuario

3. CREAR la estructura
   â†’ Crear index.html, about.html, contact.html, assets/styles.css

4. CICLO de trabajo (repetir para cada funcionalidad)
   $ git add index.html
   $ git commit -m "feat: agregar navbar Bootstrap 5 responsive"
   $ git push

5. VERIFICAR en GitHub.com que el archivo estÃ¡ actualizado
```

**Mensajes de commit recomendados:**
```
feat: estructura base HTML + Bootstrap CDN
feat: navbar responsive con hamburguesa
feat: grid de 3 cards en index.html
feat: formulario de contacto con validaciÃ³n
style: CSS custom â€” variables, :valid/:invalid, transiciones
docs: agregar README y PROMPTS.md con 5 prompts
```

---

### [F-35] Estructura de archivos del TP1

**TÃ­tulo:** OrganizaciÃ³n del proyecto

```
mi-blog/
â”œâ”€â”€ index.html          â† Lista de posts (cards)
â”œâ”€â”€ about.html          â† Sobre el autor
â”œâ”€â”€ contact.html        â† Formulario de contacto
â”œâ”€â”€ assets/
â”‚   â”œâ”€â”€ styles.css      â† Estilos custom
â”‚   â””â”€â”€ images/
â”‚       â”œâ”€â”€ favicon.ico
â”‚       â”œâ”€â”€ avatar.jpg
â”‚       â””â”€â”€ post1.jpg
â”œâ”€â”€ README.md           â† Instrucciones del proyecto
â””â”€â”€ PROMPTS.md          â† OBLIGATORIO: registro de IA
```

**En Git (GitHub Classroom):**
```
feat: agregar estructura base HTML + Bootstrap
style: aplicar estilos custom en styles.css
feat: navbar responsive con Bootstrap 5
feat: grid de cards para lista de posts
feat: formulario de contacto con validaciÃ³n
docs: documentar prompts de Copilot en PROMPTS.md
```

---

### [F-36] Checklist TP1

**TÃ­tulo:** Â¿Estoy listo para entregar?

```
ARCHIVOS
  â˜ index.html â€” Navbar + grid de cards (â‰¥3 posts)
  â˜ about.html â€” InformaciÃ³n del autor
  â˜ contact.html â€” Formulario con Bootstrap + campo telÃ©fono
  â˜ assets/styles.css â€” Estilos custom + media queries
  â˜ assets/images/ â€” favicon.ico + imÃ¡genes del blog
  â˜ README.md â€” Instrucciones del proyecto
  â˜ PROMPTS.md â€” â‰¥5 prompts documentados

HTML
  â˜ Estructura semÃ¡ntica (header/main/footer)
  â˜ Bootstrap incluido via CDN
  â˜ Viewport meta en todos los HTMLs
  â˜ W3C Validator: sin errores âœ“

CSS
  â˜ Variables CSS (â‰¥2: --color-primario, --font-principal...)
  â˜ Media queries mobile (<768px) y desktop (â‰¥768px)
  â˜ :valid/:invalid en el formulario
  â˜ Transiciones en hover de botones/links

GIT
  â˜ â‰¥ 5 commits con mensajes descriptivos
  â˜ Pushes al repositorio de Classroom
```

---

### [F-37] Recursos y documentaciÃ³n

**TÃ­tulo:** Donde buscar ayuda

| Recurso | Para quÃ© |
|---------|----------|
| MDN HTML | Referencia oficial de etiquetas y semÃ¡ntica |
| MDN CSS | Referencia oficial de propiedades y selectores |
| Bootstrap 5 Docs | Clases y componentes de Bootstrap |
| W3C Validator | Verificar que el HTML estÃ¡ bien |
| MDN Web Docs | DocumentaciÃ³n detallada tÃ©cnica |
| GitHub Copilot | Generar cÃ³digo con prompts |

**Horarios de consulta:** (completar con el docente)

**Campus virtual:** (completar con link)

**En clase:** podÃ©s abrir issues en tu repo de Classroom para marcar dudas.

---

### [F-38] TPs activos â€” Links y entregas

**TÃ­tulo:** TPs de las primeras semanas

| TP | Tema | Entrega | Link de Classroom |
|----|------|---------|-------------------|
| **TP1** | Blog Personal HTML/CSS/Bootstrap | **31/3 Â· 23hs** | classroom.github.com/a/RI8vnIt_ |
| **TP2** | IntroducciÃ³n a Python | **31/3 Â· 23hs** | classroom.github.com/a/X4xiTEDQ |
| **TP3** | Tests Unitarios con pytest | **7/4 Â· 23hs** | classroom.github.com/a/jLxPRyso |

> Para aceptar cada TP: accedÃ© al link â†’ "Accept this assignment" â†’ te crea un repo personal

**TP4 prÃ³ximamente:**
- Django ORM Â· Entrega 14/4 Â· 23hs Â· classroom.github.com/a/mZttlvBE

---

### [F-39] PrÃ³xima clase

**TÃ­tulo:** Semana 2 â€” Python 3.13

```
Semana 1 âœ… HTML + CSS + Bootstrap (HOY)
Semana 2    Python 3.13 â€” Fundamentos

QuÃ© viene:
â€¢ Variables y tipos de datos
â€¢ Control de flujo (if/for/while)
â€¢ Funciones y mÃ³dulos
â€¢ Git branches + pull requests

TPs que siguen corriendo:
â€¢ TP1 (Blog HTML)  â†’ 31/3 23hs Â· classroom.github.com/a/RI8vnIt_
â€¢ TP2 (Python)     â†’ 31/3 23hs Â· classroom.github.com/a/X4xiTEDQ
â€¢ TP3 (pytest)     â†’  7/4 23hs Â· classroom.github.com/a/jLxPRyso
```

**Tip:** Avanzar con el TP1 mientras el material de hoy estÃ¡ fresco â€” al menos completar la estructura base y el Navbar.

