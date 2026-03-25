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

> **🎓 Guía docente — T0 (15 min)**
>
> **Apertura sugerida:** *"Bienvenidos. Esta cursada es distinta: van a trabajar como lo haría un desarrollador junior real. Git desde el día uno, IA desde el día uno, código real desde el día uno."*
>
> **Demo de apertura (2 min):** Abrir VS Code con la extensión GitHub Copilot activa. Mostrá que el ícono del copiloto está en la barra de estado inferior. Crear un archivo `hola.html`, escribir `<!`, esperar la sugerencia de Copilot y aceptarla con **Tab**. Decir: *"Así trabajan hoy los devs."*
>
> **Mostrar en pantalla:** La estructura del cuatrimestre (SLIDE 03) — señalar que todo el stack va sumándose semana a semana. Hacer énfasis en que TP0 ya debería estar entregado.
>
> **Política de IA — punto importante:** Aclarar desde el principio que usar Copilot/ChatGPT **no es trampa**, pero que el `PROMPTS.md` es obligatorio en cada entrega. Sin `PROMPTS.md`, el TP se devuelve sin calificar. Mostrar el formato del archivo en SLIDE 05.
>
> **Errores frecuentes en este bloque:**
> - Estudiantes creen que "usar IA es trampa" → Reforzar con analogía: *"Un carpintero usa sierra eléctrica, no manual. La IA es tu sierra eléctrica."*
> - Preguntan si pueden usar ChatGPT en lugar de Copilot → Sí, pero el `PROMPTS.md` es obligatorio en ambos casos.
>
> **Slides de referencia:** SLIDE 01 (portada), SLIDE 03 (stack cuatrimestre), SLIDE 04 (GitHub Copilot), SLIDE 05 (PROMPTS.md)

- Presentación del docente y ayudantes
- Modalidad de la cursada: 3h teoría + 3h práctica semanales
- Herramientas del cursado: VS Code + GitHub Copilot + GitHub Classroom
- Stack tecnológico del cuatrimestre: Python 3.13 → Django 5.1 → PostgreSQL
- Evaluación: 4 TPs + 2 Aplicaciones. Todo via GitHub Classroom con autograding
- **Política de IA**: GitHub Copilot habilitado en todos los proyectos. PROMPTS.md obligatorio en cada entrega (documentar qué se le pidió a la IA y qué se modificó)

### T1 — Prompting & IA como copiloto (30 min)

> **🎓 Guía docente — T1 (30 min)**
>
> **Apertura sugerida:** *"Un prompt malo te da código basura que no entendés. Un prompt bueno te da código que podés leer, modificar y defender. Hoy aprendemos la diferencia."*
>
> **Pregunta disparadora para la clase:** *"¿Cuántos de ustedes ya usaron ChatGPT para código? ¿Siempre funcionó bien? ¿Cuándo no funcionó, por qué creen que falló?"* — Esperar 2-3 respuestas antes de avanzar.
>
> **Demo en vivo — Prompt malo vs. bueno (5 min):**
> Abrí el chat de Copilot en VS Code y mostrá ambos prompts en vivo:
> ```
> ❌ MALO:  "haceme un navbar"
> ✅ BUENO: "Necesito un Navbar de Bootstrap 5 responsive con logo a la izquierda
>           ('Mi Blog') y 3 links a la derecha: Inicio, Sobre mí, Contacto.
>           Que colapse en hamburguesa en móvil. Solo el HTML, sin CSS adicional."
> ```
> Mostrar la diferencia de output. Comentar: *"El segundo prompt tiene contexto, tarea específica, restricciones y formato de salida. Esos cuatro elementos son la anatomía de un buen prompt."*
>
> **Mostrar PROMPTS.md en vivo — ejemplo completo:**
> Crear el archivo `PROMPTS.md` vacío y completarlo en vivo:
> ```markdown
> ## PROMPTS.md — TP1 Blog Personal
>
> ### Prompt 1 — Navbar Bootstrap
> **Fecha:** 2026-03-25
> **Herramienta:** GitHub Copilot Chat
> **Contexto:** Alumno de programación web, primer proyecto HTML/CSS
> **Pedido:** Navbar Bootstrap 5 responsive con logo y 3 enlaces (Inicio, Sobre mí, Contacto)
> **Resultado:** Usé el código sugerido. Cambié el color del fondo a `bg-dark navbar-dark`
> **Qué aprendí:** El ID del botón colapso debe coincidir con el ID del div que se expande
> ```
> Decir: *"Cada entrega necesita al menos 5 prompts documentados así. Es lo que demuestra que entendieron lo que la IA generó."*
>
> **Errores frecuentes:**
> - Copiar el output de Copilot sin leerlo → Decir: *"Si no podés explicar qué hace cada línea, no lo incluyas en tu entrega. Te lo voy a preguntar en la defensa."*
> - No saber qué escribir en `PROMPTS.md` → Mostrar el ejemplo de arriba siempre que haya dudas.
>
> **Slides de referencia:** SLIDE 04 (Copilot), SLIDE 05 (PROMPTS.md formato)

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

> **🎓 Guía docente — T2 (45 min)**
>
> **Apertura sugerida:** *"HTML no es programación. Es estructura. Es como el esqueleto de un edificio: define dónde va cada habitación, pero todavía no lo decora. Eso lo hace CSS después."*
>
> **Secuencia de demo en vivo recomendada (20 min):**
>
> **Paso 1 — Crear el documento base (5 min):**
> Abrir VS Code. Crear `index.html` vacío. Escribir `!` y presionar **Enter** (Emmet). Señalar cada parte del scaffold generado:
> - `<!DOCTYPE html>` → declara HTML5, sin número de versión
> - `lang="es"` → **obligatorio** para accesibilidad y SEO (lectores de pantalla)
> - `<meta name="viewport">` → sin esto el blog se ve enorme en el celular
> - El `<link rel="stylesheet">` va en el **HEAD**, nunca en el body
>
> **Paso 2 — Árbol DOM en DevTools (5 min):**
> Agregar un `<h1>`, un `<p>` y un `<a>`. Abrir en el navegador. Presionar **F12** → pestaña **Elements**. Expandir el árbol. Decir: *"Esto es el DOM. Cada etiqueta es un nodo. CSS y JavaScript operan sobre estos nodos."*
>
> **Paso 3 — Semántica vs. divitis (10 min):**
> Mostrar en el proyector dos versiones del mismo layout:
> ```html
> <!-- ❌ Divitis -->
> <div id="header">
>   <div id="nav">Menú</div>
> </div>
> <div id="main">Contenido</div>
> <div id="footer">Pie</div>
>
> <!-- ✅ Semántico -->
> <header>
>   <nav>Menú</nav>
> </header>
> <main>Contenido</main>
> <footer>Pie</footer>
> ```
> Preguntar: *"¿Qué diferencia visual hay?"* → Ninguna. *"¿Y para un lector de pantalla? ¿Para Google?"* → Todo.
>
> **Código mínimo a construir en vivo:**
> ```html
> <!DOCTYPE html>
> <html lang="es">
> <head>
>   <meta charset="UTF-8">
>   <meta name="viewport" content="width=device-width, initial-scale=1.0">
>   <title>Blog — Paradigmas 2026</title>
>   <link rel="stylesheet" href="assets/styles.css">
> </head>
> <body>
>   <header>
>     <nav><!-- Navbar Bootstrap aquí --></nav>
>   </header>
>   <main>
>     <section id="posts">
>       <article><!-- Post 1 --></article>
>       <article><!-- Post 2 --></article>
>     </section>
>   </main>
>   <footer>
>     <p>© 2026 Mi Blog</p>
>   </footer>
> </body>
> </html>
> ```
> Notar en voz alta: `href="assets/styles.css"` — **no** `css/styles.css`. El TP pide la carpeta `assets/`.
>
> **Errores frecuentes a anticipar:**
> - Olvidar `<meta name="viewport">` → mostrarlo en DevTools con toggle mobile: el texto se ve microscópico
> - Poner el `<link>` del CSS dentro del `<body>` → FOUC (flash of unstyled content)
> - Múltiples `<h1>` por página → penalización SEO; en el TP se espera un solo `<h1>`
> - Usar `<div>` para todo (divitis) → mostrar en el árbol DOM lo ilegible que queda
>
> **Tip de cierre del bloque:** *"Antes de agregar Bootstrap, el HTML semántico tiene que estar bien. Bootstrap no arregla HTML mal estructurado."*
>
> **Slides de referencia:** SLIDES 06-13

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

> **🎓 Guía docente — T3 (30 min)**
>
> **Apertura sugerida:** *"CSS es el estilista del blog. Pero tiene sus propias reglas de cascada y especificidad que al principio parecen magia negra. La clave para dominarlas es DevTools."*
>
> **Demo en vivo — Crear el CSS base (5 min):**
> Crear `assets/styles.css` (remarcar: en `assets/`, no en `css/`). Escribir primero las variables y el reset global:
> ```css
> /* 1. Variables CSS — todas las referencias de color/fuente pasan por acá */
> :root {
>   --color-primario: #0d6efd;
>   --color-texto:    #212529;
>   --fuente-base:    'Segoe UI', sans-serif;
> }
>
> /* 2. Reset global — PRIMERO que cualquier otra regla */
> *, *::before, *::after {
>   box-sizing: border-box;
>   margin: 0;
>   padding: 0;
> }
>
> body {
>   font-family: var(--fuente-base);
>   color: var(--color-texto);
> }
> ```
> Decir: *"El `box-sizing: border-box` hace que el `width` incluya el padding y el borde. Sin esto, calcular anchos se convierte en matemática frustrante."*
>
> **Demo DevTools — Box Model visual (5 min):**
> Seleccionar cualquier elemento en **F12 → Elements → Computed**. Mostrar el diagrama azul/verde/amarillo/naranja del box model. Cambiar el `padding` de un elemento directamente en DevTools y ver el cambio en tiempo real. Preguntar: *"¿Qué cambió? ¿El margin? ¿El border?"*
>
> **Demo Flexbox responsive (5 min):**
> ```css
> .posts-grid {
>   display: flex;
>   flex-wrap: wrap;  /* sin esto las cards se salen del viewport */
>   gap: 1.5rem;
> }
> .posts-grid .card {
>   flex: 1 1 280px;  /* crece, se achica, base mínima 280px */
> }
> ```
> Achicar la ventana del navegador en vivo. Los alumnos ven cómo las cards pasan de 3 columnas a 2, a 1. Decir: *"Eso es el flex-wrap trabajando. No escribimos ninguna media query para esto."*
>
> **Errores frecuentes a anticipar:**
> - Ruta incorrecta del CSS: `href="css/styles.css"` en lugar de `href="assets/styles.css"` → el CSS no carga
> - `box-sizing` no declarado → los anchos con padding se desborden
> - Olvidar `flex-wrap: wrap` → las cards se salen del viewport en pantallas pequeñas
> - Variables CSS sin declarar en `:root` → las referencias `var(--color-primario)` no se aplican
>
> **Tip:** *"DevTools es tu mejor amigo para CSS. Si un estilo no funciona, antes de tocar el código, revisá en DevTools si el selector está coincidiendo y si el valor se está aplicando."*
>
> **Slides de referencia:** SLIDES 14-22

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

> **🎓 Guía docente — P1 (45 min)**
>
> **Apertura sugerida:** *"Bootstrap es CSS pre-escrito y probado por miles de desarrolladores durante años. No lo estamos construyendo desde cero. Lo estamos usando como herramienta profesional, igual que cualquier librería."*
>
> **Demo en vivo — Incluir CDN y primera grid (15 min):**
>
> **Paso 1:** Abrir el `index.html` existente. Agregar en `<head>`, **después** del CSS custom:
> ```html
> <!-- Bootstrap CSS — va ANTES del styles.css custom -->
> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
> <!-- CSS custom —viene DESPUÉS para que pueda sobreescribir Bootstrap -->
> <link rel="stylesheet" href="assets/styles.css">
> ```
> Refrescar el navegador. Señalar el cambio de fuente y espaciado. Decir: *"Con solo una línea ya tenemos el sistema de diseño de Bootstrap activo."*
>
> **Paso 2:** Agregar antes de `</body>`:
> ```html
> <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
> ```
> Decir: *"Sin este script, el dropdown y el navbar hamburguesa no van a funcionar. Es el único JS que necesitan hoy."*
>
> **Paso 3 — Primera grid de 3 cards:**
> ```html
> <div class="container py-4">
>   <div class="row g-4">
>     <div class="col-12 col-md-4">
>       <div class="card">
>         <div class="card-body">
>           <h5 class="card-title">Post 1</h5>
>           <p class="card-text">Descripción breve del primer post.</p>
>           <a href="#" class="btn btn-primary">Leer más</a>
>         </div>
>       </div>
>     </div>
>     <!-- Repetir ×2 -->
>   </div>
> </div>
> ```
> Achicar la ventana: en móvil → 1 columna. En tablet/desktop → 3 columnas. Mostrar los 6 breakpoints de SLIDE 26.
>
> **Demo del gutter `g-*` (2 min):**
> Cambiar `g-4` por `g-0` y por `g-5` en vivo. Los alumnos ven inmediatamente el efecto del espaciado entre columnas.
>
> **Errores frecuentes a anticipar:**
> - CSS custom **antes** del Bootstrap CSS → Bootstrap pisa los estilos custom. El orden correcto: Bootstrap primero, custom después
> - Olvidar el JS de Bootstrap → el navbar hamburguesa no abre en móvil
> - `<div class="row">` sin un `container` padre → el layout se desborda hacia los bordes
> - `col-4` sin breakpoint → siempre 4 columnas, incluso en pantallas de 320px
>
> **Slides de referencia:** SLIDES 23-27

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

> **🎓 Guía docente — P2 (45 min)**
>
> **Apertura sugerida:** *"Ahora la parte más visible del blog: el navbar que el usuario ve en todas las páginas, las cards donde van los posts, y el formulario de contacto."*
>
> **Demo Navbar (10 min):**
> Pegar el código de Navbar del bloque técnico en el `index.html`. Luego:
> 1. Abrir en pantalla completa → el navbar se muestra completo con los links
> 2. Reducir a ~375px (DevTools → toggle device toolbar) → aparece el botón hamburguesa
> 3. Hacer click en el hamburguesa → se despliega el menú con animación
> Preguntar: *"¿Por qué funciona esto sin que yo haya escrito una sola línea de JavaScript?"* → El Bootstrap JS que pusimos antes. El `data-bs-toggle` y `data-bs-target` son atributos especiales que Boostrap JS interpreta.
>
> **Punto crítico a remarcar:**
> ```html
> <!-- El id del botón y el div DEBEN coincidir -->
> data-bs-target="#navbarNav"  ←→  id="navbarNav"
> ```
> Mostrar qué pasa cuando no coinciden: el toggle no funciona. Este es el error número uno.
>
> **Demo Cards con altura uniforme (5 min):**
> Agregar tres cards con texto de diferente longitud. Sin `h-100`, las cards tienen alturas distintas. Agregar `h-100` a la clase de la card:
> ```html
> <div class="card h-100">
> ```
> Las tres cards igualan la altura de la más alta. Explicar: *"`h-100` es height 100% del contenedor flex. El row de Bootstrap ya es flex."*
>
> **Demo Forms con validación HTML5 (10 min):**
> Crear `contact.html` con el formulario del bloque técnico. Mostrar en DevTools:
> - Completar el campo email con un texto inválido → borde rojo (`:invalid`)
> - Completar con un email válido → borde verde (`:valid`)
> - El mensaje `.invalid-feedback` aparece solo con JavaScript de Bootstrap (agregar clase `was-validated` al form)
>
> **Errores frecuentes a anticipar:**
> - `data-bs-target="#navbarNav"` no coincide con `id="navbarNav"` → navbar no abre
> - Olvidar `navbar-expand-lg` → el navbar nunca se expande, siempre muestra hamburguesa
> - `card-img-top` sin atributo `alt` → error en W3C Validator
> - `<form>` sin `action` y `method` → funciona visualmente pero es importante para cuando conecten el backend
>
> **Tip:** *"Para el navbar, siempre copien de la documentación oficial de Bootstrap (getbootstrap.com/docs/5.3/components/navbar/), no de Stack Overflow. La doc tiene el código más actualizado."*
>
> **Slides de referencia:** SLIDES 28-33

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

> **🎓 Guía docente — P3 (30 min)**
>
> **Propósito:** Este bloque integra todo lo visto. El docente construye el `index.html` completo del blog en vivo, de principio a fin, con Copilot como copiloto.
>
> **Mostrar la estructura de carpetas ANTES de empezar (2 min):**
> ```
> mi-blog/
> ├── index.html          ← página principal con el grid de posts
> ├── about.html          ← página "Sobre mí"
> ├── contact.html        ← página con formulario
> ├── assets/
> │   ├── styles.css      ← estilos custom (NO en css/)
> │   └── images/
> │       ├── favicon.ico
> │       └── post1.jpg
> ├── README.md
> └── PROMPTS.md          ← OBLIGATORIO
> ```
> Decir: *"Esta es la estructura exacta que va a revisar el autograder. Si el archivo está en otro lado, el test falla."*
>
> **Secuencia de construcción en vivo:**
>
> **(5 min) — Header + Navbar:**
> Armar el `<header>` con el Navbar Bootstrap. Copilot puede sugerir el navbar completo si escribís el primer `<nav class="navbar`. Aceptar con Tab, revisar en voz alta cada parte.
>
> **(10 min) — Main con grid de 3 cards:**
> Escribir la primera card manualmente. Luego usar Copilot para sugerir las dos siguientes:
> *"Copilot vio el patrón. Le pedimos que lo repita. Eso es pair programming con IA."*
>
> **(5 min) — CSS custom con variables:**
> En `assets/styles.css`, agregar un hover effect sobre las cards:
> ```css
> .card {
>   transition: transform 0.2s ease, box-shadow 0.2s ease;
> }
> .card:hover {
>   transform: translateY(-4px);
>   box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
> }
> ```
> Demostrar el efecto en el navegador. Señalar los valores de `transition` de SLIDE 22.
>
> **(5 min) — Footer:**
> ```html
> <footer class="bg-dark text-light py-4 mt-5">
>   <div class="container text-center">
>     <p class="mb-0">© 2026 Mi Blog — Paradigmas de Programación IDEI-UNTDF</p>
>   </div>
> </footer>
> ```
>
> **(3 min) — Validar con W3C Validator:**
> Abrir https://validator.w3.org/ → opción "Validate by Direct Input" → pegar el HTML completo → **0 errores**. Decir: *"Este es el estándar del TP. Si el validador da errores, el checklist no está completo."*
>
> **Errores frecuentes durante la demo:**
> - Ruta `href="css/styles.css"` en lugar de `href="assets/styles.css"` → el CSS no carga; mostrar el error en consola del DevTools
> - `favicon.ico` faltante → W3C no lo detecta, pero el checklist del TP lo pide
>
> **Slides de referencia:** SLIDES 34-36 (Git workflow, estructura TP1, checklist)

Se realizó un live coding construyendo la página `index.html` completa del TP1:
1. Estructura HTML5 semántica con `<header>`, `<main>`, `<footer>`
2. Navbar Bootstrap con toggle para móvil
3. Grid de 3 cards con Bootstrap
4. Footer con información de contacto

### P4 — Setup GitHub Classroom (20 min)

> **🎓 Guía docente — P4 (20 min)**
>
> **Apertura sugerida:** *"El código que no está en Git no existe. Para un empleador, si no podés mostrar tu historial de commits, es como si no hubieras trabajado esos meses."*
>
> **Demo en vivo desde Codespaces (10 min):**
> 1. Proyectar: abrir `classroom.github.com/a/RI8vnIt_` en el navegador
> 2. Mostrar cómo se acepta la tarea → GitHub crea el repo individual automáticamente
> 3. Click en **"Open in Codespaces"** → VS Code se abre en el navegador, en el servidor de GitHub
> 4. Mostrar que Copilot ya está activo en el Codespace (ícono en la barra de estado)
> 5. Hacer una pequeña edición al `README.md` (cambiar el título)
> 6. En la terminal integrada, demostrar el flujo completo:
>    ```bash
>    git add README.md
>    git commit -m "docs: agregar descripción del proyecto"
>    git push
>    ```
> 7. Refrescar la pestaña del repo en GitHub → el commit aparece con el mensaje
> 8. Mostrar la pestaña **Actions** → el autograder ya está corriendo
>
> **Commits semánticos — mostrar en pantalla:**
> ```
> ✅ feat: agregar navbar bootstrap responsive
> ✅ style: ajustar colores primarios con variables CSS
> ✅ fix: corregir ruta de imagen rota en card de post
> ✅ docs: completar PROMPTS.md con 5 prompts documentados
> ✅ chore: agregar favicon.ico a assets/images/
>
> ❌ "cambios"
> ❌ "arreglé cosas"
> ❌ "final definitivo v3"
> ❌ "asd"
> ```
> Decir: *"En 6 meses, cuando vean el historial del proyecto, el commit 'arreglé cosas' no les dice nada. El commit 'fix: corregir ruta de imagen' les dice exactamente qué pasó."*
>
> **Checklist de entrega — leer con los alumnos (3 min):**
> Recorrer el checklist del TP1 en voz alta. Preguntar por cada ítem: *"¿Qué dudas tienen sobre este?"* Hacer énfasis en:
> - `PROMPTS.md` con **≥ 5 prompts** documentados
> - **≥ 5 commits** con mensajes semánticos
> - W3C Validator: **0 errores** en los 3 HTMLs
>
> **Errores frecuentes a anticipar:**
> - No hacer `git push` → el trabajo queda local, el autograder no lo ve, el TP aparece como no entregado
> - Commits sin descripción → Decir: *"El mensaje del commit es para future-you, no para mí."*
> - `git push` denegado → En Codespaces está configurado automáticamente; si trabajan local, necesitan autenticarse con `gh auth login`
>
> **Tip final:** *"Si el check en Actions está en verde, sus tests pasan. Si está en rojo, hay algo que arreglar antes de la fecha límite. Pueden hacer push cuantas veces quieran antes del cierre."*
>
> **Slides de referencia:** SLIDE 34 (Git flujo con Classroom), SLIDE 35 (estructura TP1), SLIDE 36 (checklist TP1)

- **Conceptos de Git revisados:**
  - `git init` / `git clone` (Classroom crea el repo)
  - `git add` → `git commit -m "mensaje"` → `git push`
  - Commits semánticos: `feat:`, `style:`, `fix:`, `docs:`
- **TP1**: Link activo → `classroom.github.com/a/RI8vnIt_`
- **TP2**: Link activo → `classroom.github.com/a/X4xiTEDQ`
- **TP3**: Tests unitarios pytest — Link activo → `classroom.github.com/a/jLxPRyso` (entrega 7/4)
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
| TP1 — Blog personal HTML/CSS/Bootstrap | Martes 31/3 · 23hs | `classroom.github.com/a/RI8vnIt_` |
| TP2 — Python fundamentos autograding | Martes 31/3 · 23hs | `classroom.github.com/a/X4xiTEDQ` |
| TP3 — Tests unitarios con pytest | Martes 7/4 · 23hs | `classroom.github.com/a/jLxPRyso` |

**TP1 checklist de entrega:**
- [ ] `index.html` con Navbar y grid de cards (mínimo 3 posts)
- [ ] `about.html` con información personal
- [ ] `contact.html` con formulario funcional
- [ ] `assets/styles.css` con estilos custom, variables CSS y media queries
- [ ] `assets/images/` con favicon.ico e imágenes del blog
- [ ] `README.md` con instrucciones del proyecto
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
- TP1 — Blog HTML/CSS: https://classroom.github.com/a/RI8vnIt_
- TP2 — Python: https://classroom.github.com/a/X4xiTEDQ
- TP3 — pytest: https://classroom.github.com/a/jLxPRyso

---

## Próxima Clase

**Semana 2 — Módulo I: Python 3.13 + Introducción a Git/GitHub**
- Instalación y configuración de Python 3.13
- Sintaxis básica: variables, tipos, operadores
- Control de flujo: if/elif/else, for, while
- Introducción a funciones y módulos
- Continuación Git: ramas, merge, pull requests
