# PROMPTS.md — TP1: Blog Personal HTML/CSS/Bootstrap
## [Tu nombre aquí] — IF009 Laboratorio de Programación y Lenguajes 2026
## UNTDF IDEI

> **Instrucciones:** Completá este archivo a medida que construís tu blog. Cada vez que uses GitHub Copilot, ChatGPT u otra IA para generar código, agregá una entrada con el formato indicado. Mínimo **5 prompts documentados**. Sin este archivo, el TP se devuelve sin calificar.

---

## ¿Cómo usar este archivo?

### La anatomía de un buen prompt

Un prompt efectivo tiene 4 componentes:

```
[CONTEXTO]         → Quién sos y para qué proyecto es
[TAREA]            → Qué querés generar exactamente
[RESTRICCIONES]    → Qué debe/no debe hacer, qué tecnología usar
[FORMATO DE SALIDA]→ Cómo querés que te lo entregue
```

**Ejemplo — Prompt malo:**
```
"haceme un navbar"
```

**Ejemplo — Prompt bueno:**
```
"Soy alumno de programación web. Necesito un Navbar de Bootstrap 5.3 responsive
con logo 'Mi Blog Personal' a la izquierda y 3 links a la derecha: Inicio
(href='index.html'), Sobre mí (href='about.html'), Contacto (href='contact.html').
Que colapse en menú hamburguesa en pantallas < 992px. Fondo oscuro (navbar-dark
bg-dark) con posición sticky-top. Dame solo el HTML del <nav> completo,
sin CSS adicional ni explicaciones."
```

---

## 📋 Workflow recomendado para el TP1

Seguí este orden para construir el blog. Con esta secuencia, en 3-4 sesiones de trabajo tenés el TP completo.

### Sesión 1 — Estructura base + Navbar (~60 min)
```
1. Clonar el repo de GitHub Classroom
2. Crear index.html con scaffold HTML5 (ver Prompt #1)
3. Agregar CDN de Bootstrap (ver Prompt #2)
4. Construir el Navbar (ver Prompt #3)
5. Commit: "feat: scaffold inicial con navbar Bootstrap"
```

### Sesión 2 — index.html completo (~60-90 min)
```
1. Construir el Hero banner
2. Grid de 3 cards de artículos (ver Prompt #4)
3. Card individual con imagen, badge, título, texto y botón (ver Prompt #5)
4. Footer con redes sociales (ver Prompt #6)
5. Commits por sección: "feat: hero section", "feat: grid de cards", "feat: footer"
```

### Sesión 3 — about.html + contact.html (~60 min)
```
1. Duplicar index.html → renombrar a about.html → limpiar el <main>
2. Construir sección de presentación personal
3. Duplicar about.html → renombrar a contact.html
4. Construir formulario de contacto (ver Prompt #7)
5. Commits: "feat: about page", "feat: contact form"
```

### Sesión 4 — CSS personalizado + revisión final (~45 min)
```
1. Crear assets/styles.css con variables CSS (ver Prompt #8)
2. Aplicar branding: navbar color, cards hover effect, botones custom
3. Verificar responsive en DevTools (F12 → ícono de móvil)
4. Validar con W3C Validator: validator.w3.org (ver Prompt #9)
5. Completar PROMPTS.md con todas las entradas
6. Commit final: "docs: completo PROMPTS.md y README"
7. Push → verificar en GitHub Classroom
```

---

## Prompts — Completar uno por cada componente

---

## Prompt #1 — Scaffold HTML5 base

**Fecha:** ____-__-__
**Herramienta:** [ ] GitHub Copilot Chat [ ] GitHub Copilot completions [ ] ChatGPT [ ] Otro: ______

**Prompt exacto que usaste:**
```
Soy alumno de primer año de programación web. Necesito el scaffold base de un documento 
HTML5 para una página llamada index.html de un blog personal. Debe incluir:
- <!DOCTYPE html> con lang="es"
- <head> con: charset UTF-8, viewport para mobile, meta description, title "Mi Blog Personal | Inicio"
- link al CSS de Bootstrap 5.3.3 via CDN (con el integrity correcto)
- link a mi CSS custom en assets/styles.css (después de Bootstrap)
- <body> vacío por ahora
- script de Bootstrap JS (bundle) antes de </body>
Dame el HTML completo y correcto. Sin comentarios de explicación en el código.
```

**Resultado:** _(describí en 1-2 líneas qué generó)_

**Modificaciones que hice:** _(qué cambiaste y por qué)_

**Qué aprendí:** _(una cosa concreta — puede ser técnica o sobre el uso de Copilot)_

---

## Prompt #2 — Navbar Bootstrap 5 responsive

**Fecha:** ____-__-__
**Herramienta:** [ ] GitHub Copilot Chat [ ] GitHub Copilot completions [ ] ChatGPT [ ] Otro: ______

**Prompt exacto que usaste:**
```
Necesito un Navbar de Bootstrap 5.3 responsive para mi blog personal. Características:
- Brand/logo a la izquierda con texto "[Tu Nombre] Blog" y un emoji 📝
- 3 links a la derecha: "Inicio" (href="index.html", active en esta página),
  "Sobre mí" (href="about.html"), "Contacto" (href="contact.html")
- Colapsa en menú hamburguesa en pantallas menores a lg (992px)
- Estilo: navbar-dark bg-dark, posición sticky-top
- El botón hamburguesa debe tener aria-label correcto para accesibilidad
Dame solo el <nav> completo con todas las clases Bootstrap correctas.
```

**Resultado:** _(describí)_

**Modificaciones que hice:**

**Qué aprendí:**

---

## Prompt #3 — Grid de cards para artículos (index.html)

**Fecha:** ____-__-__
**Herramienta:** [ ] GitHub Copilot Chat [ ] GitHub Copilot completions [ ] ChatGPT [ ] Otro: ______

**Prompt exacto que usaste:**
```
Necesito una sección de artículos para el index.html de mi blog personal usando Bootstrap 5.3.
Requisitos:
- Un <h2> "Últimos artículos" con mb-4
- Row responsiva con row-cols-1 (móvil), row-cols-sm-2 (tablet), row-cols-lg-3 (desktop)
- Gutter g-4 entre cards
- 3 cards de artículos, cada una con:
  * Imagen arriba (card-img-top) con alt descriptivo
  * Badge de categoría (ej: "HTML/CSS", "Python", "Bootstrap")
  * Título del post (card-title)
  * Resumen de 2 líneas (card-text text-muted)
  * Botón "Leer más →" con btn-outline-primary, siempre al fondo de la card
  * Footer de card con la fecha del post
- Todas las cards deben tener la misma altura (usar h-100 + d-flex flex-column + mt-auto)
Dame solo el HTML de esta sección, dentro de un <main class="container my-5">.
```

**Resultado:** _(describí)_

**Modificaciones que hice:**

**Qué aprendí:**

---

## Prompt #4 — Formulario de contacto con validación (contact.html)

**Fecha:** ____-__-__
**Herramienta:** [ ] GitHub Copilot Chat [ ] GitHub Copilot completions [ ] ChatGPT [ ] Otro: ______

**Prompt exacto que usaste:**
```
Necesito el formulario de contacto para contact.html de mi blog. Usando Bootstrap 5.3.
Campos obligatorios:
- Nombre completo (type="text", required, minlength="3")
- Email (type="email", required)
- Teléfono (type="tel", opcional)
- Mensaje (textarea, required, minlength="10", rows="5")
- Botón "Enviar mensaje" (btn-primary, w-100)

Cada campo debe tener:
- <label> con for= correcto (accesibilidad)
- clase form-control
- div.invalid-feedback con mensaje de error descriptivo
- div.valid-feedback con mensaje de éxito

El <form> debe tener novalidate (para manejar validación con CSS).
Envolver todo en un <div class="col-md-8 mx-auto"> centrado.
Dame solo el HTML del formulario completo.
```

**Resultado:** _(describí)_

**Modificaciones que hice:**

**Qué aprendí:**

---

## Prompt #5 — CSS personalizado con variables y efectos hover

**Fecha:** ____-__-__
**Herramienta:** [ ] GitHub Copilot Chat [ ] GitHub Copilot completions [ ] ChatGPT [ ] Otro: ______

**Prompt exacto que usaste:**
```
Necesito el archivo assets/styles.css para mi blog personal que usa Bootstrap 5.3.
El CSS custom va después de Bootstrap y debe sobreescribir/extender sus estilos.

Incluir:
1. Reset de box-sizing: *, *::before, *::after { box-sizing: border-box }
2. Variables CSS en :root: --color-primario (azul oscuro), --color-acento (azul claro),
   --color-fondo (gris muy claro), --radio-borde (8px), --sombra-card, --transicion
3. Body con font-family Segoe UI/sans-serif
4. Sección hero: gradiente con --color-primario, text-center, padding generoso
5. Cards: sin border, border-radius con var, box-shadow con var, transición suave,
   efecto hover que levante la card (translateY) y aumente la sombra
6. Footer: borde superior de 3px con --color-acento
7. Media query para móvil: reducir padding del hero
8. Feedback visual para inputs: :valid con borde verde, :invalid:not(:placeholder-shown) con rojo

Quiero que use exclusivamente var(--nombre) sin repetir valores hardcodeados.
```

**Resultado:** _(describí)_

**Modificaciones que hice:**

**Qué aprendí:**

---

## Prompt #6 — [Tu componente aquí — agrego uno propio]

**Fecha:** ____-__-__
**Herramienta:** [ ] GitHub Copilot Chat [ ] GitHub Copilot completions [ ] ChatGPT [ ] Otro: ______

**Descripción del componente:** _(ej: "Footer con redes sociales", "Hero de about.html", "Badges de skills", etc.)_

**Prompt exacto que usaste:**
```
[Escribí aquí el prompt completo con los 4 componentes: contexto, tarea, restricciones, formato]
```

**Resultado:** _(describí)_

**Modificaciones que hice:**

**Qué aprendí:**

---

## Prompt #7 — [Tu componente aquí]

**Fecha:** ____-__-__
**Herramienta:** [ ] GitHub Copilot Chat [ ] GitHub Copilot completions [ ] ChatGPT [ ] Otro: ______

**Descripción del componente:**

**Prompt exacto que usaste:**
```
[Escribí aquí el prompt completo]
```

**Resultado:**

**Modificaciones que hice:**

**Qué aprendí:**

---

## Resumen de aprendizajes

> *Al finalizar el TP, completá esta sección. Es lo que te lleva 2 minutos y vale más que el código.*

**¿Qué fue lo más difícil del TP?**

**¿Qué parte te salió mejor que esperabas?**

**¿Qué mejorarías con más tiempo?**

**¿Qué aprendiste sobre el uso de IA que no sabías antes?**

---

## Registro de sesiones de trabajo

| Fecha | Tiempo | Qué hice | Commits |
|-------|--------|----------|---------|
| | | | |
| | | | |
| | | | |

---

*Formato PROMPTS.md · IF009 Laboratorio de Programación y Lenguajes 2026 · UNTDF IDEI*
