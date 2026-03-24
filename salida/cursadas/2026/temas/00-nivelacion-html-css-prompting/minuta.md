# Minuta — Tema 00: Nivelación HTML/CSS/Bootstrap 5/Prompting
## Semana 1 — IF009 Laboratorio de Programación y Lenguajes — UNTDF IDEI 2026

**Fecha:** Semana 1  
**Duración:** 180 min (teoría) + 180 min (práctica)  
**Estado:** ✅ Clase iniciada — filminas ya presentadas, TP1 y TP2 ya entregados  
**Docente:** (nombre del docente)  
**Plataforma TP:** GitHub Classroom con Codespaces + Copilot habilitados

---

## Resumen Ejecutivo

Primera semana de cursada. Se presentó la materia, se introdujo el uso de IA (GitHub Copilot) como herramienta de trabajo, y se niveló a los alumnos en HTML5/CSS3/Bootstrap 5. La clase ya fue iniciada usando las filminas del archivo `HTML & CSS.pdf`. Se entregaron TP1 (Blog personal) y TP2 (Python autograding) para las próximas semanas.

---

## Bloque Teórico — Contenidos Desarrollados

### T0 — Presentación de la materia (15 min)
- Presentación del docente y ayudantes
- Modalidad de la cursada: 3h teoría + 3h práctica semanales
- Herramientas del cursado: VS Code + GitHub Copilot + GitHub Classroom
- Stack tecnológico del cuatrimestre: Python 3.13 → Django 5.1 → PostgreSQL
- Evaluación: 4 TPs + 2 Aplicaciones. Todo via GitHub Classroom con autograding
- **Política de IA**: GitHub Copilot habilitado en todos los proyectos. PROMPTS.md obligatorio en cada entrega (documentar qué se le pidió a la IA y qué se modificó)

### T1 — Prompting & IA como copiloto (30 min)
- **¿Qué es GitHub Copilot?** Autocompletado inteligente entrenado en código público
- **Anatomía de un buen prompt:**
  - Contexto: "Soy estudiante de programación web"
  - Tarea específica: "Necesito un Navbar de Bootstrap 5 con logo y 3 links"
  - Restricciones: "Debe ser responsive, collapsar en móvil"
  - Formato de salida: "Dame solo el HTML, sin CSS adicional"
- **Demo en vivo**: Se mostró Copilot completando HTML en VS Code
- **Anti-pattern**: Copiar sin entender. La IA es un copiloto, no el piloto
- **PROMPTS.md**: Cada entrega debe incluir este archivo con registro de prompts usados

### T2 — HTML5: estructura y semántica (45 min)

#### Estructura básica de un documento HTML5
```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi Blog Personal</title>
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <!-- contenido -->
</body>
</html>
```

**Puntos clave:**
- `<!DOCTYPE html>` declara HTML5 (sin versión)
- `lang="es"` es obligatorio para accesibilidad
- El `viewport` meta habilita diseño responsive en móviles
- Un solo `<h1>` por página (SEO + accesibilidad)

#### Elementos semánticos (vs `<div>` genérico)

| Elemento | Uso |
|----------|-----|
| `<header>` | Cabecera de página o sección |
| `<nav>` | Menú de navegación |
| `<main>` | Contenido principal (uno por página) |
| `<section>` | Sección temática con título |
| `<article>` | Contenido independiente (post, noticia) |
| `<aside>` | Contenido lateral/complementario |
| `<footer>` | Pie de página |

**Por qué importa la semántica:**
- Lectores de pantalla (accesibilidad)
- Mejor indexación en buscadores (SEO)
- Código más mantenible y legible

#### Ejemplo estructura blog
```html
<body>
  <header>
    <nav><!-- Navbar Bootstrap --></nav>
  </header>
  <main>
    <section id="posts">
      <article class="card"><!-- Post 1 --></article>
      <article class="card"><!-- Post 2 --></article>
    </section>
  </main>
  <footer><!-- Pie de página --></footer>
</body>
```

#### Formularios HTML5
```html
<form action="/contacto" method="POST">
  <label for="nombre">Nombre:</label>
  <input type="text" id="nombre" name="nombre" required>
  
  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required>
  
  <label for="mensaje">Mensaje:</label>
  <textarea id="mensaje" name="mensaje" rows="5"></textarea>
  
  <button type="submit">Enviar</button>
</form>
```

**Input types importantes:**
- `text`, `email`, `password`, `number`, `date`, `tel`, `url`
- `required`, `minlength`, `maxlength`, `pattern` (validación HTML5 nativa)

### T3 — CSS3: Box Model y Flexbox (30 min)

#### El Box Model
Todo elemento HTML es una caja con:
- **Content**: el contenido real
- **Padding**: espacio interno entre contenido y borde
- **Border**: el borde (ancho, estilo, color)
- **Margin**: espacio externo entre elementos

```css
/* Buena práctica: border-box */
*, *::before, *::after {
  box-sizing: border-box;
}

.card {
  width: 300px;     /* ancho total incluyendo padding y border */
  padding: 16px;    /* espacio interno */
  border: 1px solid #dee2e6;
  margin-bottom: 20px;
}
```

#### CSS Flexbox
Para layouts de una dimensión (fila o columna):

```css
/* Flex container */
.posts-grid {
  display: flex;
  flex-wrap: wrap;      /* permite que los items salten de línea */
  gap: 20px;            /* espacio entre items */
  justify-content: flex-start;  /* alineación horizontal */
  align-items: stretch;          /* alineación vertical */
}

/* Flex items */
.posts-grid .card {
  flex: 1 1 300px;  /* grow shrink basis */
}
```

#### Media Queries (responsive design)
```css
/* Mobile-first: estilos base para móvil */
.posts-grid {
  display: flex;
  flex-direction: column;  /* apilado en móvil */
}

/* Tablets */
@media (min-width: 768px) {
  .posts-grid {
    flex-direction: row;
    flex-wrap: wrap;
  }
}

/* Desktop */
@media (min-width: 992px) {
  .posts-grid .card {
    width: calc(33.33% - 20px);
  }
}
```

#### Pseudo-clases para validación de formularios
```css
input:valid {
  border-color: #198754;  /* verde Bootstrap success */
}

input:invalid {
  border-color: #dc3545;  /* rojo Bootstrap danger */
}
```

---

## Bloque Práctico — Laboratorio

### P1 — Bootstrap 5: CDN y Grid System (45 min)

#### Incluir Bootstrap 5 via CDN
```html
<!-- En <head> -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" 
      rel="stylesheet">

<!-- Antes de </body> -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js">
</script>
```

#### Grid System — 12 columnas
El grid de Bootstrap funciona con 3 elementos:
1. **Container**: centra el contenido y define máximo ancho
2. **Row**: fila que contiene columnas
3. **Col**: columna que ocupa N/12 del ancho

```html
<div class="container">
  <div class="row">
    <!-- 3 columnas iguales en pantallas medianas o mayores -->
    <!-- En móvil: apilar (1 columna completa cada una) -->
    <div class="col-12 col-md-4">
      <div class="card">Post 1</div>
    </div>
    <div class="col-12 col-md-4">
      <div class="card">Post 2</div>
    </div>
    <div class="col-12 col-md-4">
      <div class="card">Post 3</div>
    </div>
  </div>
</div>
```

**Breakpoints Bootstrap 5:**
- `col-` → xs (0px y más)
- `col-sm-` → small (576px+)
- `col-md-` → medium (768px+)  ← más usado
- `col-lg-` → large (992px+)
- `col-xl-` → extra large (1200px+)

### P2 — Bootstrap: Navbar + Cards + Forms (45 min)

#### Navbar Responsive
```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container">
    <!-- Brand / Logo -->
    <a class="navbar-brand" href="index.html">Mi Blog</a>
    
    <!-- Botón hamburguesa para móvil -->
    <button class="navbar-toggler" type="button" 
            data-bs-toggle="collapse" 
            data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    
    <!-- Links de navegación -->
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
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

#### Card de Bootstrap
```html
<div class="card mb-4">
  <img src="img/post1.jpg" class="card-img-top" alt="Imagen del post">
  <div class="card-body">
    <h5 class="card-title">Título del Post</h5>
    <p class="card-text text-muted">
      Descripción breve del contenido del post...
    </p>
    <a href="#" class="btn btn-primary">Leer más</a>
  </div>
  <div class="card-footer text-muted">
    <small>Publicado el 15 de marzo de 2026</small>
  </div>
</div>
```

#### Form con Bootstrap
```html
<form class="needs-validation" novalidate>
  <div class="mb-3">
    <label for="name" class="form-label">Nombre</label>
    <input type="text" class="form-control" id="name" required>
    <div class="invalid-feedback">Por favor ingresá tu nombre.</div>
  </div>
  
  <div class="mb-3">
    <label for="email" class="form-label">Email</label>
    <input type="email" class="form-control" id="email" required>
    <div class="invalid-feedback">Por favor ingresá un email válido.</div>
  </div>
  
  <div class="mb-3">
    <label for="message" class="form-label">Mensaje</label>
    <textarea class="form-control" id="message" rows="4" required></textarea>
  </div>
  
  <button type="submit" class="btn btn-primary">Enviar</button>
</form>
```

### P3 — Demo Live: Armar index.html del Blog (30 min)

Se realizó un live coding construyendo la página `index.html` completa del TP1:
1. Estructura HTML5 semántica con `<header>`, `<main>`, `<footer>`
2. Navbar Bootstrap con toggle para móvil
3. Grid de 3 cards con Bootstrap
4. Footer con información de contacto

### P4 — Setup GitHub Classroom (20 min)

- **Conceptos de Git revisados:**
  - `git init` / `git clone` (Classroom crea el repo)
  - `git add` → `git commit -m "mensaje"` → `git push`
  - Commits semánticos: `feat:`, `style:`, `fix:`, `docs:`
- **TP1**: Consigna entregada. Link de Classroom será enviado por correo.
- **TP2**: Link ya activo → `classroom.github.com/a/X4xiTEDQ`
- Los repos tienen **Codespaces habilitados** y **GitHub Copilot** disponible

---

## Preguntas y Observaciones de los Alumnos

- Consulta frecuente: diferencia entre `margin` y `padding` → se reforzó con visualización del box model
- Duda: cuándo usar `col-12 col-md-4` vs solo `col-md-4` → explicación de mobile-first
- Consulta sobre PROMPTS.md: se aclaró formato y ejemplos de contenido esperado

---

## Tareas Pendientes para los Alumnos

| Tarea | Fecha límite | Plataforma |
|-------|-------------|------------|
| TP1 — Blog personal HTML/CSS/Bootstrap | Semana 3 | GitHub Classroom (link a enviar) |
| TP2 — Python fundamentos autograding | Semana 2 | `classroom.github.com/a/X4xiTEDQ` |

**TP1 checklist de entrega:**
- [ ] `index.html` con Navbar y grid de cards (mínimo 3 posts)
- [ ] `about.html` con información personal
- [ ] `contact.html` con formulario funcional
- [ ] `css/styles.css` con estilos custom y media queries
- [ ] `PROMPTS.md` con al menos 5 prompts documentados
- [ ] ≥ 5 commits con mensajes descriptivos
- [ ] W3C Validator: sin errores en los 3 HTMLs

---

## Recursos Compartidos en Clase

- W3Schools HTML: https://www.w3schools.com/html/
- W3Schools CSS: https://www.w3schools.com/css/
- Bootstrap 5 Docs: https://getbootstrap.com/docs/5.3/
- Bootstrap Grid: https://getbootstrap.com/docs/5.3/layout/grid/
- Bootstrap Navbar: https://getbootstrap.com/docs/5.3/components/navbar/
- Bootstrap Cards: https://getbootstrap.com/docs/5.3/components/card/
- W3C Validator: https://validator.w3.org/
- Plantilla inicial del TP1: (se entregará con link de Classroom)

---

## Próxima Clase

**Semana 2 — Módulo I: Python 3.13 + Introducción a Git/GitHub**
- Instalación y configuración de Python 3.13
- Sintaxis básica: variables, tipos, operadores
- Control de flujo: if/elif/else, for, while
- Introducción a funciones y módulos
- Continuación Git: ramas, merge, pull requests
