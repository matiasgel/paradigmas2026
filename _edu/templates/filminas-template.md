# Plantilla canónica de filminas EDU

Usar esta plantilla para que `filminas.md`, el plan JSON y la publicación a Slides hablen el mismo idioma.

## Reglas mínimas

1. Cada slide empieza con `### [F-XX] Título corto`.
2. El primer `#` dentro de la slide es el subtítulo visible.
3. Los `##`, `###`, etc. dentro de la slide son encabezados del cuerpo.
4. Las listas usan Markdown estándar.
5. El código usa fences con lenguaje.
6. Las tablas usan tablas Markdown.
7. Si la intención visual no se deduce bien del contenido, agregar directivas simples.

## Directivas opcionales

- `@tipo: portada|concepto-abstracto|codigo|tabla|tabla-comparativa|diagrama|socratica|demo|cierre|timeline`
- `@layout: portada|concepto-abstracto|codigo|tabla|tabla-comparativa|diagrama|socratica|demo|cierre|timeline`
- `@imagen: background|content|none`
- `@prompt-imagen: descripción visual específica del tópico de la filmina`
- `@asset: kind=diagram position=right-half prompt="texto breve para imagen o grafico"`

Si una slide activa `@imagen: background|content`, debe incluir `@prompt-imagen:` o un `@asset:` con `prompt="..."`.

## Esqueleto sugerido

```md
## PORTADA

---

### [F-00] Portada

# Título de la clase

Subtítulo institucional o de contexto

---

## BLOQUE 1 — Nombre del bloque

---

### [F-01] Título corto de la slide

# Idea principal visible

- Punto clave 1
- Punto clave 2

---

### [F-02] Slide con diagrama

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama del flujo entre parser, árbol sintáctico y validación semántica
@asset: kind=diagram position=right-half prompt="diagrama simple del flujo"

# Explicación del concepto

## Qué mirar

- Elemento A
- Elemento B

---

### [F-03] Slide con código

@tipo: codigo

# Ejemplo mínimo

## Idea del ejemplo

- Explicar primero qué se quiere mostrar

```ts
const saludo = (nombre: string) => `Hola ${nombre}`;
console.log(saludo("Ada"));
```

---

### [F-04] Slide con tabla

@tipo: tabla

# Comparación breve

## Cómo leer la tabla

- Fila por concepto
- Columna por criterio

| Concepto | Ventaja | Riesgo |
|----------|---------|--------|
| A | Claro | Limitado |
| B | Flexible | Más complejo |
```

## Criterio editorial

- Una slide debe ser inequívoca para un humano y para el pipeline.
- Si una slide necesita “adivinarse”, faltan subtítulo o directivas.
- Si un gráfico es importante, declarar la intención con `@asset` y/o `@prompt-imagen`.
- Si ya existían filminas previas del tema, reutilizar lo rescatable y mejorar con el material fuente dado.