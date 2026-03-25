# Guía de Estudio — Tema 00: Nivelación HTML / CSS / Bootstrap 5
## IF009 — Laboratorio de Programación y Lenguajes
### UNTDF IDEI · 2026 · Semana 1

> **Para el alumno:** Esta guía está pensada para que puedas estudiar y reprasar los temas de la primera clase de forma autónoma. La idea es que la uses **entre clase y clase**, no durante la clase. Si podés estudiarlo solo, lo hicimos bien.

---

## Índice

1. [Introducción: ¿por qué este tema?](#1-introducción-por-qué-este-tema)
2. [Objetivos de aprendizaje](#2-objetivos-de-aprendizaje)
3. [Conceptos previos necesarios](#3-conceptos-previos-necesarios)
4. [Desarrollo teórico](#4-desarrollo-teórico)
   - 4.1 [HTML5 — Estructura y semántica (Filminas 06–13)](#41-html5--estructura-y-semántica)
   - 4.2 [CSS3 — Estilos y layout (Filminas 14–22)](#42-css3--estilos-y-layout)
   - 4.3 [Bootstrap 5 — Framework responsive (Filminas 23–33)](#43-bootstrap-5--framework-responsive)
   - 4.4 [Prompting con IA asistida (Filminas 04–05)](#44-prompting-con-ia-asistida)
   - 4.5 [Git y GitHub Classroom (Filminas 34–36)](#45-git-y-github-classroom)
5. [Ejemplos trabajados](#5-ejemplos-trabajados)
6. [Puntos clave y resumen](#6-puntos-clave-y-resumen)
7. [Autoevaluación](#7-autoevaluación)
8. [Glosario](#8-glosario)
9. [Referencias y lecturas recomendadas](#9-referencias-y-lecturas-recomendadas)

---

## 1. Introducción: ¿por qué este tema?

Este módulo cero **no es HTML por HTML**: es la base tecnológica que necesitás para entender cómo funciona una aplicación web completa con Python y Django.

En las próximas semanas vas a crear vistas con Django que generen HTML dinámicamente. Si no entendés la estructura de ese HTML, vas a estar copiando código sin saber por qué funciona. Este tema cambia eso.

**¿Qué lugar ocupa en la materia?**

```
Semana 1:  HTML/CSS/Bootstrap 5  ← estás aquí
Semana 2:  Python 3.13 fundamentos
Semana 3:  Python orientado a objetos
Semana 4-6: Django — Modelos, Vistas, Templates ← usa lo que aprendiste aquí
Semana 7+:  Proyecto integrador con HTML + Django + PostgreSQL
```

El TP1 que entregás esta semana va a vivir casi idéntico dentro de las vistas Django que construyas en la semana 6. Es inversión, no desvío.

---

## 2. Objetivos de aprendizaje

Al finalizar este tema vas a poder:

| # | Objetivo | Evidencia en el TP1 |
|---|----------|---------------------|
| 1 | **Construir páginas HTML5 semánticas** usando las etiquetas correctas | `index.html`, `about.html`, `contact.html` sin errores W3C |
| 2 | **Estilizar con CSS3** aplicando box model, selectores, flexbox y media queries | `assets/styles.css` con variables CSS y responsive |
| 3 | **Implementar layout responsive con Bootstrap 5** usando grid, Navbar, Cards y Forms | Blog con 3 columnas en desktop, 1 en mobile |
| 4 | **Usar IA asistida (Copilot)** para acelerar HTML/CSS y documentar en PROMPTS.md | `PROMPTS.md` con mínimo 5 prompts documentados |
| 5 | **Gestionar trabajo con Git** con commits semánticos y descriptivos | ≥5 commits en el repo de GitHub Classroom |

---

## 3. Conceptos previos necesarios

Para aprovechar esta guía necesitás tener:

- ✅ **Cuenta de GitHub** — si no la tenés, creá una en [github.com](https://github.com) con tu email universitario
- ✅ **VS Code instalado** con la extensión **GitHub Copilot** activada
- ✅ **Nociones básicas de programación** — variables, tipos de datos, condicionales (no hace falta saber Python todavía)
- ✅ **Git instalado** — verificá con `git --version` en la terminal. Si dice `command not found`, instalalo desde [git-scm.com](https://git-scm.com)

> Si no tenés instalado alguno de estos, el README del repositorio de la materia explica el setup completo paso a paso.

---

## 4. Desarrollo teórico

---

### 4.1 HTML5 — Estructura y semántica

> **Ver Filminas 06–13**

#### ¿Qué es HTML?

**HTML** (HyperText Markup Language) es el lenguaje que define la **estructura y el contenido** de una página web. No es un lenguaje de programación — no tiene variables, no hace cálculos. Es un lenguaje de **marcado**: usás etiquetas (tags) para decirle al navegador qué significa cada pedazo de contenido.

> **Definición formal:** HTML es un lenguaje de marcado estándar para crear documentos hipertexto. La versión actual, HTML5, fue estandarizada por el W3C en 2014 y es la base de la web moderna.

La anatomía básica de un documento HTML5:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Mi blog personal">
    <title>El título de la pestaña</title>
    <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
    <!-- Todo lo que el usuario ve va aquí -->
    <h1>Hola mundo</h1>
</body>
</html>
```

**¿Por qué cada línea importa?**

| Línea | Para qué sirve | ¿Obligatorio? |
|-------|---------------|---------------|
| `<!DOCTYPE html>` | Le dice al navegador que esto es HTML5 | ✅ Siempre |
| `lang="es"` | Accesibilidad y SEO — lectores de pantalla hablan idioma correcto | ✅ Siempre |
| `charset="UTF-8"` | Soporta acentos y ñ correctamente | ✅ Siempre |
| `viewport` | Evita que el celular muestre el sitio como versión de escritorio | ✅ Siempre |
| `description` | Texto que aparece en los resultados de Google | Recomendado |

#### Elementos y etiquetas

Un **elemento HTML** tiene esta forma:

```
<p>Un párrafo de texto</p>
 ↑                    ↑
 Tag de apertura      Tag de cierre
```

Algunas etiquetas no se cierran (son **void elements**):

```html
<img src="foto.jpg" alt="descripción de la foto">
<br>
<input type="text" name="nombre">
<link rel="stylesheet" href="styles.css">
```

> **Regla de oro:** Toda etiqueta que abrís, la cerrás. Excepto las void elements.

#### El árbol DOM

Cuando el navegador lee tu HTML, construye un árbol en memoria llamado **DOM** (Document Object Model). Cada etiqueta es un **nodo** en ese árbol.

```
document
└── html
    ├── head
    │   ├── meta charset
    │   ├── meta viewport
    │   └── title
    └── body
        ├── header
        │   └── nav
        ├── main
        │   └── section
        │       ├── article
        │       └── article
        └── footer
```

**¿Por qué te importa el DOM?** Porque CSS y JavaScript operan sobre el DOM. Cuando escribís `nav { color: white }` en CSS, estás apuntando al nodo `nav` del árbol.

Podés ver el DOM en vivo: abrí cualquier página web, presioná **F12** → pestaña **Elements**.

#### HTML5 Semántico — La gran diferencia

HTML4 y versiones anteriores tenían un problema: todo era `<div>`. El código resultaba ambiguo — un `<div id="header">` para el programador era lo mismo que `<div id="main">`: no había información sobre el **significado** del contenido.

HTML5 introdujo **etiquetas semánticas** que comunican el rol del contenido:

```html
<!-- ❌ Antes (HTML4 / "divitis") — sin significado estructural -->
<div id="header">
    <div id="nav">Menú</div>
</div>
<div id="main">
    <div class="article">Post 1</div>
</div>
<div id="footer">Pie</div>

<!-- ✅ Ahora (HTML5 semántico) — cada etiqueta dice qué es -->
<header>
    <nav>Menú</nav>
</header>
<main>
    <article>Post 1</article>
</main>
<footer>Pie</footer>
```

Las etiquetas semánticas principales:

| Etiqueta | Significado | Cuándo usarla |
|----------|-------------|---------------|
| `<header>` | Cabecera de la página o sección | Una vez, al inicio del body |
| `<nav>` | Navegación principal | Menú de links |
| `<main>` | Contenido principal del documento | Una vez por página |
| `<section>` | Sección temática con título | Agrupar contenido relacionado |
| `<article>` | Contenido independiente y reutilizable | Posts de blog, noticias |
| `<aside>` | Contenido relacionado pero secundario | Sidebar, anuncios, bio |
| `<footer>` | Pie de página o sección | Al final del body |
| `<figure>` | Contenido ilustrativo (imagen + leyenda) | Fotos con caption |
| `<figcaption>` | Leyenda del `<figure>` | Dentro de `<figure>` |

> **Regla de oro para el TP1:** Si podés usar una etiqueta semántica, usala. Si un `<div>` no tiene rol semántico (solo es un contenedor de layout), aceptable.

#### Formularios HTML5

Los formularios son fundamentales para el `contact.html`:

```html
<form action="#" method="post" novalidate>
    <div class="mb-3">
        <label for="nombre" class="form-label fw-semibold">Nombre completo</label>
        <input type="text" class="form-control" id="nombre" name="nombre"
               placeholder="Tu nombre" required minlength="3">
    </div>

    <div class="mb-3">
        <label for="email" class="form-label fw-semibold">Email</label>
        <input type="email" class="form-control" id="email" name="email"
               placeholder="nombre@ejemplo.com" required>
    </div>

    <div class="mb-3">
        <label for="mensaje" class="form-label fw-semibold">Mensaje</label>
        <textarea class="form-control" id="mensaje" name="mensaje"
                  rows="4" required minlength="10"></textarea>
    </div>

    <button type="submit" class="btn btn-primary">Enviar</button>
</form>
```

**Atributos clave de formularios:**

| Atributo | Para qué sirve |
|----------|---------------|
| `type="email"` | Valida formato de email automáticamente |
| `type="tel"` | Muestra teclado numérico en móvil |
| `required` | Campo obligatorio (HTML5 nativo) |
| `minlength="3"` | Mínimo de caracteres |
| `placeholder` | Texto de ejemplo gris dentro del campo |
| `label for="id"` | Asocia el label al input (accesibilidad) |
| `novalidate` | Desactiva validación del navegador para usar CSS propio |

#### Validación W3C

Antes de hacer el commit final del TP1, **validá tu HTML** en:
👉 [https://validator.w3.org](https://validator.w3.org)

Cargá el archivo local con **File Upload**. El validador muestra errores y warnings. Un TP1 con errores W3C tiene puntos descontados.

Errores frecuentes:
- Falta `alt` en `<img>` → accesibilidad
- `<button>` dentro de `<a>` o viceversa → inválido
- IDs duplicados → el mismo `id` no puede aparecer dos veces
- `<h1>` usado más de una vez por página

---

### 4.2 CSS3 — Estilos y layout

> **Ver Filminas 14–22**

#### ¿Qué es CSS?

**CSS** (Cascading Style Sheets) controla la **presentación visual** de un documento HTML. Si HTML es el esqueleto, CSS es la ropa y la decoración.

CSS opera sobre el DOM: seleccionás nodos del árbol DOM y les aplicás estilos.

```css
/* Sintaxis básica de CSS */
selector {
    propiedad: valor;
    otra-propiedad: otro-valor;
}

/* Ejemplo real */
h1 {
    color: #2c3e50;
    font-size: 2rem;
    margin-bottom: 1rem;
}
```

#### Selectores CSS

| Tipo | Sintaxis | Cuándo usarlo |
|------|----------|---------------|
| Elemento | `p { }` | Aplicar a todos los `<p>` |
| Clase | `.card-titulo { }` | Grupo de elementos con el mismo estilo |
| ID | `#navbar { }` | Un elemento único en la página |
| Descendiente | `nav a { }` | Todos los `<a>` dentro de `<nav>` |
| Hijo directo | `ul > li { }` | Solo `<li>` directos de `<ul>` |
| Pseudo-clase | `a:hover { }` | Estado del elemento |
| Pseudo-clase | `input:valid { }` | Input con contenido válido |

> **Regla de buenas prácticas:** Preferí clases (`.mi-clase`) sobre IDs (`#mi-id`) para estilos. Los IDs son para JavaScript. Los IDs tienen mayor especificidad y pueden causar conflictos difíciles de depurar.

#### Box Model

Cada elemento HTML es una caja rectangular. El **Box Model** describe las capas de esa caja:

```
┌─────────────────────────────────────┐
│             MARGIN (espacio exterior) │
│  ┌───────────────────────────────┐  │
│  │         BORDER                │  │
│  │  ┌─────────────────────────┐  │  │
│  │  │       PADDING           │  │  │
│  │  │  ┌───────────────────┐  │  │  │
│  │  │  │     CONTENT       │  │  │  │
│  │  │  │   (width x height)│  │  │  │
│  │  │  └───────────────────┘  │  │  │
│  │  └─────────────────────────┘  │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

```css
.caja {
    width: 300px;
    height: 200px;
    padding: 20px;        /* espacio interno */
    border: 2px solid #333;
    margin: 16px;         /* espacio externo */
    box-sizing: border-box; /* SIEMPRE incluir esto */
}
```

> **`box-sizing: border-box`** es crítico: hace que `width` incluya padding y border. Sin esto, una caja de `width: 300px` con `padding: 20px` termina midiendo 340px en realidad, rompiendo layouts.

**Tip práctico:** Al inicio de tu `styles.css`, siempre incluí:
```css
*, *::before, *::after {
    box-sizing: border-box;
}
```

#### Variables CSS (Custom Properties)

Las variables CSS permiten definir valores reutilizables:

```css
/* Definición en el elemento raíz */
:root {
    --color-primario: #2c3e50;
    --color-acento: #3498db;
    --color-fondo: #f8f9fa;
    --fuente-base: 'Segoe UI', Tahoma, sans-serif;
    --radio-borde: 8px;
    --sombra: 0 2px 8px rgba(0,0,0,0.1);
}

/* Uso en cualquier parte del archivo */
h1 {
    color: var(--color-primario);
    font-family: var(--fuente-base);
}

.card {
    border-radius: var(--radio-borde);
    box-shadow: var(--sombra);
    background-color: var(--color-fondo);
}

.btn-custom {
    background-color: var(--color-acento);
}
```

**¿Por qué usar variables CSS?**
- Cambiás el color de todo el sitio cambiando una sola línea
- El código es más legible (`var(--color-primario)` vs `#2c3e50`)
- Pueden modificarse desde JavaScript para temas dinámicos

#### Flexbox

Flexbox resuelve el problema de alinear elementos en una fila o columna:

```css
/* Contenedor flex */
.contenedor {
    display: flex;
    flex-direction: row;        /* fila (default) o column */
    justify-content: center;    /* alineación horizontal */
    align-items: center;        /* alineación vertical */
    flex-wrap: wrap;            /* permite que los items pasen a la siguiente línea */
    gap: 1rem;                  /* espacio entre items */
}
```

**Valores de `justify-content`:**

| Valor | Efecto |
|-------|--------|
| `flex-start` | Items al inicio (izquierda) |
| `flex-end` | Items al final (derecha) |
| `center` | Items centrados |
| `space-between` | Primer item al inicio, último al final, resto distribuidos |
| `space-around` | Espacio igual alrededor de cada item |
| `space-evenly` | Espacio exactamente igual entre todos |

**Caso frecuente en el TP1 — cards de igual altura:**
```css
.row-cards {
    display: flex;
    flex-wrap: wrap;
    align-items: stretch; /* todas las cards miden lo mismo verticalmente */
}

.card {
    display: flex;
    flex-direction: column;
}

.card-body {
    flex-grow: 1; /* el body ocupa todo el espacio disponible */
}

.card-footer {
    margin-top: auto; /* el footer siempre queda abajo */
}
```

#### Media Queries

Las media queries aplican estilos según el tamaño de la pantalla:

```css
/* Mobile first: escribís los estilos para móvil por defecto */
.container {
    padding: 1rem;
}

/* Tablet y arriba */
@media (min-width: 768px) {
    .container {
        padding: 2rem;
    }
}

/* Desktop y arriba */
@media (min-width: 992px) {
    .container {
        padding: 3rem;
        max-width: 1200px;
        margin: 0 auto;
    }
}
```

> **Mobile-first** significa que los estilos base son para pantalla chica, y usás `min-width` para agregar complejidad a medida que la pantalla crece. Es el enfoque correcto porque hay más usuarios en móvil que en desktop.

#### Transiciones y Hover

```css
/* Transición en botones al hacer hover */
.btn-custom {
    background-color: var(--color-acento);
    color: white;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: var(--radio-borde);
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
}

.btn-custom:hover {
    background-color: #2980b9;  /* tono más oscuro */
    transform: translateY(-2px); /* sube levemente */
}

/* Feedback visual en inputs */
input:focus {
    outline: none;
    border-color: var(--color-acento);
    box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.25);
}

input:valid { border-color: #28a745; }
input:invalid:not(:placeholder-shown) { border-color: #dc3545; }
```

---

### 4.3 Bootstrap 5 — Framework responsive

> **Ver Filminas 23–33**

#### ¿Qué es Bootstrap?

**Bootstrap** es el framework CSS más usado del mundo. Ofrece un sistema de grilla responsive, componentes visuales (Navbar, Cards, Forms, Botones, Alertas) y utilidades de espaciado, color y tipografía — todo listo para usar con clases CSS predefinidas.

**Ventaja principal:** En lugar de escribir Flexbox desde cero para cada layout responsive, Bootstrap lo hace con clases como `col-md-4`.

#### Incluir Bootstrap via CDN

```html
<!-- En el <head> — CSS de Bootstrap -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous">

<!-- Antes de </body> — JavaScript de Bootstrap (necesario para Navbar hamburgesa, modales, etc.) -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc4s9bIOgUxi8T/jzmwg3V1MRkh7B3T5mT1yKNYV1AT"
        crossorigin="anonymous"></script>
```

> **El `integrity`** es un hash SHA para verificar que el archivo no fue modificado en camino. Siempre copialo exactamente de la documentación oficial de Bootstrap.

#### Sistema de Grilla (Grid)

El grid de Bootstrap divide el ancho disponible en **12 columnas**. Las clases `col-{breakpoint}-{n}` indican cuántas columnas ocupa un elemento en cada tamaño de pantalla.

**Breakpoints de Bootstrap 5:**

| Prefijo | Breakpoint | Pantalla | Container máx. |
|---------|-----------|----------|----------------|
| *(sin prefijo)* | xs | < 576px | 100% |
| `sm` | Small | ≥ 576px | 540px |
| `md` | Medium | ≥ 768px | 720px |
| `lg` | Large | ≥ 992px | 960px |
| `xl` | Extra large | ≥ 1200px | 1140px |
| `xxl` | XX large | ≥ 1400px | 1320px |

**Estructura básica:**
```html
<div class="container">        <!-- centra y limita el ancho -->
    <div class="row">          <!-- fila flex con 12 columnas -->
        <div class="col-md-4">  <!-- 4/12 = 1/3 del ancho desde tableta -->
            Columna 1
        </div>
        <div class="col-md-4">
            Columna 2
        </div>
        <div class="col-md-4">
            Columna 3
        </div>
    </div>
</div>
```

En móvil (`< 768px`), las tres columnas se apilan verticalmente (100% de ancho cada una). En tableta y desktop, son tres columnas de igual ancho.

**Grid para las cards del blog (index.html):**
```html
<div class="container my-5">
    <h2 class="mb-4">Últimos artículos</h2>
    <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 g-4">
        <!-- row-cols-1: 1 card por fila en móvil -->
        <!-- row-cols-sm-2: 2 cards por fila en tableta -->
        <!-- row-cols-lg-3: 3 cards por fila en desktop -->
        <!-- g-4: gutter (espacio entre cards) de 1.5rem -->

        <div class="col">
            <div class="card h-100">...</div>
            <!-- h-100: la card ocupa toda la altura de la fila -->
        </div>
        <div class="col">
            <div class="card h-100">...</div>
        </div>
        <div class="col">
            <div class="card h-100">...</div>
        </div>
    </div>
</div>
```

#### Espaciado — Clases `m` y `p`

Bootstrap tiene clases utilitarias para margin y padding que siguen la convención `{propiedad}{lado}-{escala}`:

| Propiedad | `m` = margin | `p` = padding |
|-----------|-------------|--------------|
| Lado | `t`=top, `b`=bottom, `s`=start(left), `e`=end(right), `x`=horizontal, `y`=vertical, (vacío)=todos |
| Escala | `0`=0, `1`=0.25rem, `2`=0.5rem, `3`=1rem, `4`=1.5rem, `5`=3rem, `auto` |

Ejemplos:
```html
<div class="mt-3 mb-5 px-4">
    <!-- margin-top: 1rem; margin-bottom: 3rem; padding-left/right: 1.5rem -->
</div>

<h1 class="mb-4">Título</h1>          <!-- margin bottom 1.5rem -->
<p class="my-2 text-muted">Texto</p>  <!-- margin vertical 0.5rem + color gris -->
```

#### Navbar Bootstrap 5

El Navbar de Bootstrap es responsive por defecto: colapsa en un ícono hamburgesa en pantallas chicas.

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
    <div class="container">

        <!-- Logo / Brand -->
        <a class="navbar-brand fw-bold" href="index.html">
            📝 Mi Blog
        </a>

        <!-- Botón hamburguesa (visible solo en móvil) -->
        <button class="navbar-toggler" type="button"
                data-bs-toggle="collapse"
                data-bs-target="#navbarNav"
                aria-controls="navbarNav"
                aria-expanded="false"
                aria-label="Abrir menú">
            <span class="navbar-toggler-icon"></span>
        </button>

        <!-- Links de navegación -->
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <!-- ms-auto: empuja los links a la derecha -->
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="index.html">Inicio</a>
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

**Puntos críticos del Navbar:**
- El `data-bs-target="#navbarNav"` debe coincidir con el `id="navbarNav"` del `<div class="collapse">`. Si no coinciden, la hamburgesa no funciona.
- `sticky-top` hace que la barra quede pegada arriba al hacer scroll.
- `ms-auto` en `<ul>` empuja los links a la derecha (margin-start: auto en flex).

#### Cards Bootstrap 5

```html
<div class="card h-100">
    <!-- Imagen arriba -->
    <img src="assets/images/post1.jpg" class="card-img-top" alt="Descripción de la imagen del post">

    <!-- Cuerpo de la card -->
    <div class="card-body d-flex flex-column">
        <span class="badge bg-secondary mb-2">HTML/CSS</span>  <!-- categoría -->
        <h5 class="card-title">Título del artículo</h5>
        <p class="card-text text-muted small">Resumen del artículo. Máximo 2-3 líneas...</p>

        <!-- mt-auto empuja el botón siempre al fondo de la card -->
        <a href="#" class="btn btn-outline-primary mt-auto">Leer más →</a>
    </div>

    <!-- Pie de la card -->
    <div class="card-footer text-muted small">
        <span>📅 25 de marzo, 2026</span>
    </div>
</div>
```

**Para que todas las cards tengan la misma altura:**
- Usá `h-100` en el `<div class="card">` — el card ocupa 100% de la fila del grid
- Usá `d-flex flex-column` en `.card-body` — hace que el body sea un contenedor flex vertical
- Usá `mt-auto` en el último elemento — lo empuja siempre al fondo

#### Forms con Bootstrap 5

```html
<form novalidate>
    <div class="mb-3">
        <label for="nombre" class="form-label fw-semibold">Nombre</label>
        <input type="text" class="form-control" id="nombre"
               placeholder="Tu nombre completo" required>
        <div class="invalid-feedback">El nombre es obligatorio.</div>
        <div class="valid-feedback">¡Perfecto!</div>
    </div>

    <div class="mb-3">
        <label for="emailInput" class="form-label fw-semibold">Email</label>
        <input type="email" class="form-control" id="emailInput"
               placeholder="nombre@dominio.com" required>
        <div class="invalid-feedback">Ingresá un email válido.</div>
    </div>

    <div class="mb-3">
        <label for="mensajeArea" class="form-label fw-semibold">Mensaje</label>
        <textarea class="form-control" id="mensajeArea" rows="4" required></textarea>
    </div>

    <button type="submit" class="btn btn-primary w-100">Enviar mensaje</button>
</form>
```

**Feedback CSS para el formulario (en `styles.css`):**
```css
/* El feedback visual requiere que el input tenga was-validated o is-invalid en el form */
.form-control:valid {
    border-color: #28a745;
    background-image: url("data:image/svg+xml,..."); /* ícono verde */
}

.form-control:invalid:not(:placeholder-shown) {
    border-color: #dc3545;
}
```

---

### 4.4 Prompting con IA asistida

> **Ver Filminas 04–05**

#### La anatomía de un buen prompt

Un prompt efectivo tiene **4 componentes**:

```
[CONTEXTO] + [TAREA ESPECÍFICA] + [RESTRICCIONES] + [FORMATO DE SALIDA]
```

**Ejemplo — Prompt malo:**
```
"haceme un navbar"
```
Resultado: código genérico que probablemente no sirva para tu proyecto.

**Ejemplo — Prompt bueno:**
```
"Soy alumno de primer año de programación web. Necesito un Navbar de Bootstrap 5.3
responsive con:
- Logo/brand a la izquierda con texto 'Mi Blog Personal' y un emoji 📝
- 3 links a la derecha: Inicio (href='index.html'), Sobre mí (href='about.html'), Contacto (href='contact.html')
- Que colapse en menú hamburguesa en pantallas menores a lg (992px)
- Fondo oscuro (navbar-dark bg-dark) con posición sticky-top
Dame solo el HTML del <nav>, sin CSS adicional ni explicaciones extra."
```
Resultado: código exactamente el que necesitás.

**Los 4 componentes en el ejemplo:**
- **Contexto:** "Soy alumno de primer año de programación web"
- **Tarea:** "Navbar de Bootstrap 5.3 responsive con logo y 3 links"
- **Restricciones:** "colapse en hamburgesa", "fondo oscuro", "sticky-top"
- **Formato:** "solo el HTML del nav, sin CSS ni explicaciones"

#### PROMPTS.md — Por qué es obligatorio

El `PROMPTS.md` no es burocracia. Es evidencia de que:
1. Entendés lo que escribiste (si no podés documentarlo, no lo entendés)
2. Fuiste el autor — usaste la IA como herramienta, no como reemplazo
3. Podés defender el código en una consulta

**Formato oficial del PROMPTS.md:**

```markdown
# PROMPTS.md — TP{N} {Nombre del TP}
## {Tu Nombre} — IF009 Laboratorio de Programación y Lenguajes 2026

---

## Prompt #{N} — {Descripción breve de qué construiste}

**Fecha:** YYYY-MM-DD
**Herramienta:** GitHub Copilot Chat / GitHub Copilot completions / ChatGPT
**Contexto del prompt:**
{Contexto que le diste a la IA — quién sos, para qué es el proyecto}

**Prompt exacto:**
```
{El texto exacto que copiaste en la IA}
```

**Resultado obtenido:**
{Qué generó la IA — describir en 1-2 líneas}

**Modificaciones que hice:**
{Qué cambiaste respecto al output original y por qué}

**Qué aprendí:**
{Una cosa concreta que aprendiste de este intercambio}

---
```

> **Mínimo 5 prompts documentados en el TP1.** Uno por cada componente principal: navbar, grid de cards, card individual, formulario de contacto, y CSS custom.

---

### 4.5 Git y GitHub Classroom

> **Ver Filminas 34–36**

#### Flujo básico con GitHub Classroom

```bash
# 1. Aceptar la asignación → GitHub te crea un repo
#    Link del TP1: classroom.github.com/a/RI8vnIt_
#    Esto te crea: github.com/Laboratorio-de-Programacion-Y-lenguajes-2026/tp1-blog-TuUsuario

# 2. Clonar el repo en tu máquina
git clone https://github.com/Laboratorio-de-Programacion-Y-lenguajes-2026/tp1-blog-TuUsuario

# 3. Entrar al directorio
cd tp1-blog-TuUsuario

# 4. Crear la estructura de archivos
mkdir assets
mkdir assets/images

# 5. Flujo de trabajo diario
git status                  # ver qué cambió
git add index.html          # agregar archivo específico
git add .                   # agregar todo
git commit -m "feat: agrego navbar Bootstrap"
git push                    # subir al repo
```

#### Commits semánticos — Formato correcto

El formato **Conventional Commits** es el estándar en la industria:

```
tipo: descripción en minúsculas y tiempo presente
```

**Tipos principales:**

| Tipo | Cuándo usarlo |
|------|--------------|
| `feat:` | Agregás una nueva funcionalidad |
| `fix:` | Corregís un bug o un error visual |
| `style:` | Cambios de CSS / apariencia (sin cambios funcionales) |
| `refactor:` | Reorganizás código sin cambiar su comportamiento |
| `docs:` | Actualizás README, PROMPTS.md, comentarios |
| `chore:` | Tareas de mantenimiento (agregar imágenes, favicon, etc.) |

**Ejemplos buenos vs. malos:**

```bash
# ❌ Malos — no dicen nada útil
git commit -m "cambios"
git commit -m "arreglé cosas"
git commit -m "subi"

# ✅ Buenos — claros y descriptivos
git commit -m "feat: agrego navbar Bootstrap con menú responsive"
git commit -m "feat: implemento grid de 3 cards en index.html"
git commit -m "style: aplico variables CSS y paleta de colores custom"
git commit -m "feat: construyo formulario de contacto con validación HTML5"
git commit -m "docs: completo PROMPTS.md con 6 prompts documentados"
git commit -m "fix: corrijo error W3C en atributo alt faltante"
```

---

## 5. Ejemplos trabajados

### Ejemplo 1 — Scaffold completo de `index.html`

Este es el punto de partida para tu blog. Construilo en este orden, commit por commit.

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Blog personal de programación web">
    <title>Mi Blog Personal | Inicio</title>
    <link rel="icon" type="image/png" href="assets/images/favicon.png">
    <!-- Bootstrap CSS via CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
          crossorigin="anonymous">
    <!-- CSS personalizado (siempre después de Bootstrap) -->
    <link rel="stylesheet" href="assets/styles.css">
</head>
<body>

    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
        <div class="container">
            <a class="navbar-brand fw-bold" href="index.html">📝 Mi Blog</a>
            <button class="navbar-toggler" type="button"
                    data-bs-toggle="collapse" data-bs-target="#navbarNav"
                    aria-controls="navbarNav" aria-expanded="false"
                    aria-label="Abrir menú de navegación">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="index.html">Inicio</a>
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

    <!-- Hero -->
    <header class="hero-section text-center py-5">
        <div class="container">
            <h1 class="display-4 fw-bold">Mi Blog Personal</h1>
            <p class="lead text-muted mb-4">Apuntes, proyectos y aprendizajes de programación web</p>
            <a href="contact.html" class="btn btn-primary btn-lg">Contactame</a>
        </div>
    </header>

    <!-- Artículos -->
    <main class="container my-5">
        <h2 class="mb-4">Últimos artículos</h2>
        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 g-4">

            <div class="col">
                <div class="card h-100">
                    <img src="assets/images/post1.jpg" class="card-img-top" alt="Imagen del post sobre HTML5">
                    <div class="card-body d-flex flex-column">
                        <span class="badge bg-secondary mb-2">HTML/CSS</span>
                        <h5 class="card-title">Mi primer sitio web</h5>
                        <p class="card-text text-muted">Aprendí a construir páginas semánticas con HTML5 y a estilizar con CSS3...</p>
                        <a href="#" class="btn btn-outline-primary mt-auto">Leer más →</a>
                    </div>
                    <div class="card-footer text-muted small">📅 25 ene 2026</div>
                </div>
            </div>

            <!-- Repetir para post 2 y post 3 -->

        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-4 mt-5">
        <div class="container">
            <p class="mb-1">© 2026 Mi Blog Personal — Laboratorio de Programación y Lenguajes</p>
            <p class="mb-0 small text-muted">
                <a href="#" class="text-muted me-3">GitHub</a>
                <a href="#" class="text-muted me-3">LinkedIn</a>
            </p>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-YvpcrYf0tY3lHB60NNkmXc4s9bIOgUxi8T/jzmwg3V1MRkh7B3T5mT1yKNYV1AT"
            crossorigin="anonymous"></script>
</body>
</html>
```

### Ejemplo 2 — CSS personalizado (`assets/styles.css`)

```css
/* ============================================================
   styles.css — Estilos custom de Mi Blog Personal
   Siempre va DESPUÉS de Bootstrap en el <head>
   Para sobreescribir Bootstrap usá mayor especificidad
   ============================================================ */

/* Reset y Box Model */
*, *::before, *::after {
    box-sizing: border-box;
}

/* Variables CSS — Definir la paleta completa aquí */
:root {
    --color-primario:    #2c3e50;
    --color-acento:      #3498db;
    --color-acento-dark: #2980b9;
    --color-fondo:       #f8f9fa;
    --color-texto:       #343a40;
    --fuente-base: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    --radio-borde: 8px;
    --sombra-card: 0 2px 12px rgba(0,0,0,0.08);
    --transicion: 0.25s ease;
}

/* Base */
body {
    font-family: var(--fuente-base);
    color: var(--color-texto);
    background-color: var(--color-fondo);
}

/* Hero */
.hero-section {
    background: linear-gradient(135deg, var(--color-primario) 0%, #34495e 100%);
    color: white;
    padding: 5rem 0;
}

.hero-section .text-muted {
    color: rgba(255,255,255,0.7) !important;
}

/* Cards */
.card {
    border: none;
    border-radius: var(--radio-borde);
    box-shadow: var(--sombra-card);
    transition: transform var(--transicion), box-shadow var(--transicion);
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}

/* Botones custom */
.btn-primary {
    background-color: var(--color-acento);
    border-color: var(--color-acento);
}

.btn-primary:hover {
    background-color: var(--color-acento-dark);
    border-color: var(--color-acento-dark);
}

/* Footer */
footer {
    border-top: 3px solid var(--color-acento);
}

footer a:hover {
    color: var(--color-acento) !important;
    text-decoration: none;
}

/* Media Queries */
@media (max-width: 576px) {
    .hero-section {
        padding: 3rem 0;
    }

    .hero-section h1 {
        font-size: 1.75rem;
    }
}
```

### Ejemplo 3 — Estructura de carpetas del TP1

```
tp1-blog-TuUsuario/            ← raíz del repositorio
├── index.html                 ← página principal con listado de posts
├── about.html                 ← página "Sobre mí"
├── contact.html               ← formulario de contacto
├── assets/
│   ├── styles.css             ← CSS personalizado
│   └── images/
│       ├── favicon.png        ← ícono de la pestaña (32x32 px)
│       ├── avatar.jpg         ← tu foto para about.html
│       ├── post1.jpg          ← imagen para la card del artículo 1
│       ├── post2.jpg          ← imagen para la card del artículo 2
│       └── post3.jpg          ← imagen para la card del artículo 3
├── PROMPTS.md                 ← obligatorio — documentación de prompts
└── README.md                  ← instrucciones del proyecto
```

---

## 6. Puntos clave y resumen

### HTML5
- `<!DOCTYPE html>` + `lang="es"` + `charset="UTF-8"` + `viewport` → siempre, en todas las páginas
- Semántica sobre divitis: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<footer>`
- Formularios: `required`, `type="email"`, `type="tel"`, `label for=`
- Validar con W3C Validator antes del commit final

### CSS3
- `box-sizing: border-box` → `*, *::before, *::after`
- Variables CSS en `:root` → usa siempre `var(--nombre)`
- Flexbox: `display: flex`, `justify-content`, `align-items`, `flex-wrap`, `gap`
- Mobile-first: estilos base para móvil, `@media (min-width: ...)` para ampliar
- `:hover` + `transition` para interactividad sin JavaScript

### Bootstrap 5
- CDN: link en `<head>` + script antes de `</body>`
- Grid: `container > row > col-{breakpoint}-{n}` — 12 columnas totales
- `h-100` + `d-flex flex-column` + `mt-auto` → cards de altura uniforme
- Navbar: `data-bs-target` debe coincidir con `id` del div de colapso
- Espaciado: `m{t|b|s|e|x|y}-{0-5}` / `p{t|b|s|e|x|y}-{0-5}`

### Prompting
- 4 componentes: Contexto + Tarea + Restricciones + Formato
- PROMPTS.md obligatorio con mínimo 5 entradas
- La IA es copiloto, no piloto — entendés y podés modificar todo lo que entregás

### Git
- `git add .` → `git commit -m "tipo: descripción"` → `git push`
- Tipos: `feat:`, `fix:`, `style:`, `docs:`, `chore:`
- Mínimo 5 commits semánticos para el TP1

---

## 7. Autoevaluación

Respondé estas preguntas sin mirar la guía. Si podés contestarlas todas, estás listo para el TP1.

1. **Escribí de memoria** la estructura del `<head>` de un documento HTML5 correcto. ¿Cuáles son los meta tags obligatorios y por qué?

2. **Diferencia semántica:** ¿Cuándo usarías `<article>` vs `<section>`? Dá un ejemplo concreto de cada uno en el contexto del blog.

3. **Box Model:** Si un elemento tiene `width: 200px`, `padding: 20px` y `border: 2px solid` — ¿cuánto mide en realidad sin `box-sizing: border-box`? ¿Y con él?

4. **Grid Bootstrap:** Escribí el HTML para hacer que 4 cards sean 1 columna en móvil, 2 en tablet y 4 en desktop. ¿Qué clase usarías?

5. **Navbar bug:** Un compañero dice que la hamburguesa no funciona. El código tiene `data-bs-target="#menu-principal"` pero el div tiene `id="navMenu"`. ¿Cuál es el bug?

6. **Prompt:** Escribí un prompt completo para pedirle a Copilot que genere el footer del blog. Incluí los 4 componentes.

7. **Git:** Estás trabajando en el formulario de contacto. Completaste el HTML. Escribí el comando de commit correcto.

8. **Variables CSS:** ¿Qué ventaja tiene `color: var(--color-acento)` sobre `color: #3498db` en un archivo CSS?

---

## 8. Glosario

| Término | Definición |
|---------|-----------|
| **HTML** | HyperText Markup Language — lenguaje de marcado para estructurar contenido web |
| **CSS** | Cascading Style Sheets — lenguaje para definir la presentación visual de documentos HTML |
| **Bootstrap** | Framework CSS open-source para diseño responsive y componentes visuales |
| **DOM** | Document Object Model — representación en árbol del documento HTML en memoria del navegador |
| **Breakpoint** | Punto de quiebre de ancho de pantalla donde cambia el layout responsive |
| **Flexbox** | Modelo de layout CSS que permite distribuir y alinear elementos en una dirección |
| **Grid** | Sistema de 12 columnas de Bootstrap para hacer layouts responsive sin escribir CSS |
| **Semántica** | Uso de etiquetas HTML según su significado, no solo para diseño visual |
| **CDN** | Content Delivery Network — red de servidores que entrega archivos estáticos (Bootstrap, jQuery, etc.) |
| **Void element** | Elemento HTML sin contenido ni tag de cierre: `<img>`, `<input>`, `<br>`, `<link>` |
| **Box Model** | Modelo de caja CSS: content + padding + border + margin |
| **Variable CSS** | Valor CSS reutilizable definido con `--nombre-variable` y usado con `var(--nombre-variable)` |
| **Media Query** | Regla CSS que aplica estilos según características del dispositivo (ancho, orientación) |
| **Mobile-first** | Estrategia de diseño que escribe estilos para pantalla chica por defecto y agrega complejidad para pantallas grandes |
| **Gutter** | Espacio entre columnas en el grid de Bootstrap (clases `g-*`, `gx-*`, `gy-*`) |
| **Sticky** | Posición CSS/Bootstrap que hace que un elemento se pegue al borde al hacer scroll |
| **PROMPTS.md** | Archivo de documentación obligatorio en cada TP — registra los prompts de IA usados |
| **Commit semántico** | Commit con formato `tipo: descripción` que comunica claramente el propósito del cambio |
| **W3C Validator** | Servicio de validación de HTML en línea: validator.w3.org |
| **Copilot** | Herramienta de GitHub que autocompleta código usando IA |

---

## 9. Referencias y lecturas recomendadas

### Documentación oficial (fuente primaria)
- **MDN Web Docs — HTML:** https://developer.mozilla.org/es/docs/Web/HTML
- **MDN Web Docs — CSS:** https://developer.mozilla.org/es/docs/Web/CSS
- **Bootstrap 5.3 Docs:** https://getbootstrap.com/docs/5.3/

### Herramientas de práctica
- **W3Schools HTML:** https://www.w3schools.com/html/ — ejercicios interactivos
- **W3Schools CSS:** https://www.w3schools.com/css/ — referencia rápida
- **Flexbox Froggy:** https://flexboxfroggy.com/#es — aprende Flexbox jugando
- **Grid Garden:** https://cssgridgarden.com/ — aprende CSS Grid jugando
- **W3C Validator:** https://validator.w3.org/ — validar tu HTML antes de entregar

### Material del curso
- **Filminas Tema 00:** `filminas.md` en el repositorio
- **Minuta de clase:** `minuta.md` con la guía docente
- **TP1 consigna oficial:** `material/tema 01/TP 1.pdf`
- **Material HTML/CSS:** `material/tema 01/HTML & CSS.pdf`

### Lecturas adicionales opcionales
- **CSS-Tricks — A Complete Guide to Flexbox:** https://css-tricks.com/snippets/css/a-guide-to-flexbox/
- **Bootstrap — About (filosofía del framework):** https://getbootstrap.com/docs/5.3/about/overview/
- **Conventional Commits:** https://www.conventionalcommits.org/es/v1.0.0/

---

*Guía de estudio elaborada por el módulo EDU · IF009 Laboratorio de Programación y Lenguajes 2026 · UNTDF IDEI*
