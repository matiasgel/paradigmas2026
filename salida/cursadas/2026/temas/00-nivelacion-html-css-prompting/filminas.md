# Filminas — Tema 00: Nivelación HTML/CSS/Bootstrap 5
## IF009 Laboratorio de Programación y Lenguajes — UNTDF IDEI 2026

> **Nota:** Este documento es el guión de filminas complementario a las ya presentadas en clase (basadas en `HTML & CSS.pdf`). El docente puede usar estas filminas como repaso, seleccionar slides específicos o usarlos para el bloque de práctica.

---

## SLIDE 01 — Portada

**Título:** Nivelación HTML / CSS / Bootstrap 5

**Subtítulo:** Laboratorio de Programación y Lenguajes · Semana 1

**Pie:** UNTDF IDEI · 2026 · Prof. ______

---

## SLIDE 02 — ¿Qué vamos a construir?

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
- `index.html` — lista de posts
- `about.html` — sobre el autor
- `contact.html` — formulario de contacto
- TP1: entrega via **GitHub Classroom**

---

## SLIDE 03 — El Stack del Cuatrimestre

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

---

## SLIDE 04 — Tu nuevo copiloto: GitHub Copilot

**Título:** IA como herramienta, no como sustituto

```
Buen prompt = Buen código

❌ "Haceme una web"
✅ "Crea un Navbar Bootstrap 5 con logo y 3 links:
    Inicio, Sobre mí, Contacto. Que sea responsive
    y colapse en dispositivos móviles."
```

**La regla del cursado:**
> Podés usar IA. Debés entender lo que usás.  
> Cada TP requiere `PROMPTS.md` documentando el proceso.

---

## SLIDE 05 — PROMPTS.md — Formato

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

---

## SLIDE 06 — HTML5: Anatomía de un documento

**Título:** Estructura básica obligatoria

```html
<!DOCTYPE html>                    <!-- Declara HTML5 -->
<html lang="es">                   <!-- Idioma (accesibilidad) -->
<head>
  <meta charset="UTF-8">           <!-- Codificación de caracteres -->
  <meta name="viewport"            <!-- RESPONSIVE en móvil -->
        content="width=device-width, 
                 initial-scale=1.0">
  <title>Mi Blog Personal</title>  <!-- Aparece en la pestaña -->
  <link rel="stylesheet" 
        href="css/styles.css">     <!-- Estilos externos -->
</head>
<body>
  <!-- Todo el contenido visible va aquí -->
</body>
</html>
```

**⚠️ El `viewport` meta es OBLIGATORIO para Bootstrap**

---

## SLIDE 07 — HTML5: Semántica vs Divitis

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
- 👁️ **Lectores de pantalla** entienden la estructura
- 🔍 **SEO**: Google/Bing indexan mejor
- 👨‍💻 **Mantenibilidad**: código más legible

---

## SLIDE 08 — Elementos semánticos de HTML5

**Título:** El vocabulario de la estructura web

| Elemento | Descripción | Ejemplo de uso |
|----------|-------------|----------------|
| `<header>` | Cabecera de página/sección | Logo + Navbar |
| `<nav>` | Bloque de navegación | Menú principal |
| `<main>` | Contenido principal | El blog en sí |
| `<section>` | Sección temática | "Mis últimos posts" |
| `<article>` | Contenido independiente | Un post del blog |
| `<aside>` | Contenido lateral | Sidebar con tags |
| `<footer>` | Pie de página/sección | Copyright, redes |

**Regla:** Solo un `<main>` por página. `<header>` y `<footer>` pueden repetirse dentro de `<article>`.

---

## SLIDE 09 — Estructura del Blog

**Título:** Arquitectura del proyecto TP1

```html
<body>
  <header>
    <nav class="navbar navbar-expand-lg">
      <!-- Bootstrap Navbar -->
    </nav>
  </header>

  <main class="container mt-4">
    <section id="posts">
      <h2>Mis últimos posts</h2>
      <div class="row">
        <article class="col-md-4">
          <div class="card"><!-- Card Bootstrap --></div>
        </article>
        <!-- más articles/cards -->
      </div>
    </section>
  </main>

  <footer class="bg-dark text-light mt-5 py-3">
    <div class="container text-center">
      <p>© 2026 Mi Blog · UNTDF</p>
    </div>
  </footer>
</body>
```

---

## SLIDE 10 — CSS Box Model

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
/* Buena práctica: incluir siempre */
* { box-sizing: border-box; }

.card {
  padding: 16px;
  margin-bottom: 24px;
  border: 1px solid #dee2e6;
  border-radius: 8px;
}
```

---

## SLIDE 11 — CSS Flexbox

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

## SLIDE 12 — CSS Media Queries (Mobile-First)

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

## SLIDE 13 — Bootstrap 5: CDN Setup

**Título:** Incluir Bootstrap en 2 líneas

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

---

## SLIDE 14 — Bootstrap Grid (12 columnas)

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

## SLIDE 15 — Bootstrap Navbar

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

**`ms-auto`** = margin-start auto = empuja los links a la derecha

---

## SLIDE 16 — Bootstrap Cards

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

**`h-100`** = height: 100% → todas las cards de la fila tienen igual altura

---

## SLIDE 17 — Bootstrap Forms

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
    <label for="mensaje" class="form-label">Mensaje</label>
    <textarea class="form-control" id="mensaje" 
              name="mensaje" rows="5" required></textarea>
  </div>
  
  <div class="d-grid">
    <button type="submit" class="btn btn-primary">
      Enviar mensaje
    </button>
  </div>
</form>
```

---

## SLIDE 18 — Validación con CSS :valid/:invalid

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

---

## SLIDE 19 — Estructura de archivos del TP1

**Título:** Organización del proyecto

```
mi-blog/
├── index.html          ← Lista de posts (cards)
├── about.html          ← Sobre el autor
├── contact.html        ← Formulario de contacto
├── css/
│   └── styles.css      ← Estilos custom
├── img/
│   ├── post1.jpg
│   ├── post2.jpg
│   └── avatar.jpg
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

## SLIDE 20 — Checklist TP1

**Título:** ¿Estoy listo para entregar?

```
ARCHIVOS
  ☐ index.html — Navbar + grid de cards (≥3 posts)
  ☐ about.html — Información del autor
  ☐ contact.html — Formulario con Bootstrap
  ☐ css/styles.css — Estilos custom + media queries
  ☐ PROMPTS.md — ≥5 prompts documentados

HTML
  ☐ Estructura semántica (header/main/footer)
  ☐ Bootstrap incluido via CDN
  ☐ Viewport meta en todos los HTMLs
  ☐ W3C Validator: sin errores ✓

CSS
  ☐ Variables CSS (≥2)
  ☐ Al menos 1 media query
  ☐ :valid/:invalid en el formulario

GIT
  ☐ ≥ 5 commits con mensajes descriptivos
  ☐ Pushes al repositorio de Classroom
```

---

## SLIDE 21 — Recursos y soporte

**Título:** Donde buscar ayuda

| Recurso | Para qué |
|---------|----------|
| W3Schools HTML | Referencia rápida de etiquetas |
| W3Schools CSS | Propiedades CSS con ejemplos |
| Bootstrap 5 Docs | Clases y componentes de Bootstrap |
| W3C Validator | Verificar que el HTML está bien |
| MDN Web Docs | Documentación detallada técnica |
| GitHub Copilot | Generar código con prompts |

**Horarios de consulta:** (completar con el docente)

**Campus virtual:** (completar con link)

---

## SLIDE 22 — Próxima clase

**Título:** Semana 2 — Python 3.13

```
Semana 1 ✅ HTML + CSS + Bootstrap
Semana 2    Python 3.13 — Fundamentos

Qué viene:
• Variables y tipos de datos
• Control de flujo (if/for/while)
• Funciones
• Módulos y packages
• Introducción a Git branches

Antes de la próxima clase:
• Avanzar con TP1 (entrega semana 3)
• Completar TP2 Python (entrega semana 2)
  → classroom.github.com/a/X4xiTEDQ
```
