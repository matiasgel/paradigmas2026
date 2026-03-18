<!-- markdownlint-disable MD001 MD025 MD041 -->

# Filminas de prueba del Tema 04

## PORTADA

---

### [F-00] Portada

# Tema 04 · Pruebas de filminas

Contrato canónico para generación, plan y publicación

Clase técnica de prueba · 90 minutos

---

## BLOQUE 1 — Contrato único

---

### [F-01] El problema real

# Cada fase interpreta distinto la misma filmina

- El escritor piensa en Markdown humano.
- El generador de plan intenta inferir semántica.
- El publicador necesita una estructura inequívoca.
- Si cada fase adivina, aparecen incoherencias y errores.

---

### [F-02] La regla base

# Una slide debe ser inequívoca para humano y máquina

## Convención mínima

- `### [F-XX]` identifica la slide.
- El primer `#` de la slide es el subtítulo visible.
- Los `##` internos pasan a ser secciones del cuerpo.
- Listas, código y tablas usan Markdown estándar.

---

## BLOQUE 2 — Ambigüedad controlada

---

### [F-03] Cuando el contenido no alcanza

@tipo: diagrama
@imagen: content
@asset: kind=diagram position=right-half prompt="flujo entre autor, plan y publicador"

# Las directivas eliminan ambigüedad visual

## Casos típicos

- Un bloque ASCII puede ser código o diagrama.
- Una tabla puede necesitar contexto arriba.
- Una slide conceptual puede requerir imagen lateral o no.

---

### [F-04] Flujo del pipeline

@tipo: diagrama
@imagen: content
@asset: kind=diagram position=right-half prompt="filminas markdown a plan yaml a google slides"

# Un contrato único reduce errores acumulados

- `filminas.md` define contenido y hints.
- El plan YAML preserva semántica y assets.
- El publicador renderiza sin re-interpretar desde cero.

---

## BLOQUE 3 — Casos difíciles

---

### [F-05] Código largo

@tipo: codigo

# El código debe adaptarse al espacio disponible

## Criterio de publicación

- Si no entra, la tipografía baja.
- Si sigue siendo denso, se encuadra dentro de un cuadro interno.

```ts
type SlideDirective = {
  type?: "codigo" | "tabla" | "diagrama";
  layout?: "codigo" | "tabla" | "concepto-abstracto";
  image?: "background" | "content" | "none";
  asset?: { kind: string; position: string; prompt: string };
};

const buildPlanSlide = (sourceId: string, directive: SlideDirective, blocks: string[]) => ({
  id: sourceId,
  directive,
  blocks,
  valid: blocks.length > 0 && (directive.image ?? "none") !== "background",
});
```

---

### [F-06] Tabla con contexto

@tipo: tabla

# La tabla no debe aparecer sola

## Antes de leer la tabla

- La primera columna describe el artefacto.
- La segunda muestra quién lo consume.
- La tercera explica qué riesgo evita.

| Artefacto | Consumidor | Riesgo que evita |
| --------- | ---------- | ---------------- |
| `filminas.md` | autor humano | ambigüedad de contenido |
| `filminas-schema.yaml` | parser y publicador | interpretación inconsistente |
| `plan-filminas.yaml` | assets + Slides | pérdida de semántica |

---

### [F-07] Heading interno dentro del cuerpo

# Los headings Markdown también son parte del contrato

## Qué debe pasar

- El parser no debe descartarlos.
- El plan no debe convertirlos en texto plano indiferenciado.
- Slides debe mostrarlos como jerarquía real, no como markup literal.

## Qué no debe pasar

- No deben desaparecer.
- No deben verse `##` en pantalla.

---

## BLOQUE 4 — Cierre

---

### [F-08] Cierre

@tipo: cierre

# El contrato vive fuera de cada tema

- La plantilla humana guía al autor.
- El esquema YAML guía al parser.
- El publicador valida antes de generar.
- Así los errores aparecen temprano y no en el proyector.
