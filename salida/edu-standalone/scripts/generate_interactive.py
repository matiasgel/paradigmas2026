#!/usr/bin/env python3
"""
generate_interactive.py — Generador de HTML interactivo desde spec (S7.1)

Genera simulaciones HTML autocontenidas (HTML + CSS + JS en un solo archivo)
para conceptos que se benefician de interactividad visual.

Tipos soportados (v1):
  - sorting-visualizer: comparación de algoritmos de sorting
  - tree-explorer: visualización de BST/AVL
  - stack-simulator: simulación de stack push/pop/peek
  - fsm-simulator: autómata finito interactivo
  - memory-layout: visualización stack/heap/data
  - custom: template vacío

Uso:
    python scripts/generate_interactive.py --spec interactivos/spec.json --topic 05-sorting --course leng-2026

Exit codes:
    0 — generado (o feature desactivada)
    1 — error de entrada
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from pipeline_common import find_project_root, load_json, load_yaml


SUPPORTED_TYPES = {
    "sorting-visualizer", "tree-explorer", "stack-simulator",
    "fsm-simulator", "memory-layout", "custom",
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: system-ui, sans-serif; background: #1a1a2e; color: #eee; 
       display: flex; flex-direction: column; align-items: center; padding: 20px; min-height: 100vh; }}
h1 {{ margin-bottom: 10px; font-size: 1.5rem; }}
.concept {{ color: #aaa; margin-bottom: 20px; font-size: 0.9rem; }}
.canvas-area {{ background: #16213e; border-radius: 12px; padding: 20px; 
                width: 100%; max-width: 800px; min-height: 400px; position: relative; }}
.controls {{ margin-top: 15px; display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; }}
button {{ background: #0f3460; color: #eee; border: none; padding: 8px 16px; border-radius: 6px;
          cursor: pointer; font-size: 0.9rem; }}
button:hover {{ background: #1a4a8a; }}
button:focus {{ outline: 2px solid #e94560; outline-offset: 2px; }}
.info {{ margin-top: 15px; color: #aaa; font-size: 0.85rem; text-align: center; }}
canvas {{ display: block; margin: 0 auto; background: #0f3460; border-radius: 8px; }}
</style>
</head>
<body>
<h1>{title}</h1>
<p class="concept">{concept}</p>
<div class="canvas-area" role="application" aria-label="{title}">
  <canvas id="sim" width="760" height="360" tabindex="0" 
          aria-label="Simulación interactiva de {concept}"></canvas>
</div>
<div class="controls" role="toolbar" aria-label="Controles de simulación">
  {controls}
</div>
<p class="info">Tipo: {sim_type} · Bloom: {bloom_level} · Teclado: Tab + Enter</p>
<script>
{script}
</script>
</body>
</html>"""


def generate_sorting_visualizer(spec: dict) -> tuple[str, str]:
    """Genera controles y script para sorting visualizer."""
    controls = """
<button onclick="reset()" aria-label="Reiniciar">🔄 Reset</button>
<button onclick="step()" aria-label="Paso">⏭ Paso</button>
<button onclick="play()" aria-label="Reproducir">▶ Play</button>
<select id="algo" aria-label="Algoritmo">
  <option value="bubble">Bubble Sort</option>
  <option value="selection">Selection Sort</option>
  <option value="insertion">Insertion Sort</option>
</select>"""

    script = """
const c = document.getElementById('sim');
const ctx = c.getContext('2d');
let arr = [], i = 0, j = 0, sorted = false, timer = null;

function reset() {
  clearInterval(timer);
  arr = Array.from({length: 20}, () => Math.floor(Math.random() * 300) + 30);
  i = 0; j = 0; sorted = false;
  draw();
}

function draw() {
  ctx.clearRect(0, 0, c.width, c.height);
  const w = c.width / arr.length;
  arr.forEach((v, idx) => {
    ctx.fillStyle = idx === j ? '#e94560' : idx === i ? '#ffd700' : '#4ea8de';
    ctx.fillRect(idx * w + 2, c.height - v, w - 4, v);
  });
}

function step() {
  if (sorted) return;
  const algo = document.getElementById('algo').value;
  if (algo === 'bubble') {
    if (j < arr.length - i - 1) {
      if (arr[j] > arr[j+1]) [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
      j++;
    } else { i++; j = 0; }
    if (i >= arr.length - 1) sorted = true;
  } else if (algo === 'selection') {
    if (i < arr.length) {
      let min = i;
      for (let k = i+1; k < arr.length; k++) if (arr[k] < arr[min]) min = k;
      [arr[i], arr[min]] = [arr[min], arr[i]];
      j = min; i++;
    } else sorted = true;
  } else {
    if (i < arr.length) {
      let key = arr[i], k = i - 1;
      while (k >= 0 && arr[k] > key) { arr[k+1] = arr[k]; k--; }
      arr[k+1] = key; j = i; i++;
    } else sorted = true;
  }
  draw();
}

function play() { clearInterval(timer); timer = setInterval(step, 100); }
reset();
c.addEventListener('keydown', e => { if (e.key === ' ') step(); });
"""
    return controls, script


def generate_stack_simulator(spec: dict) -> tuple[str, str]:
    """Genera controles y script para stack simulator."""
    controls = """
<button onclick="push_val()" aria-label="Push">⬆ Push</button>
<button onclick="pop_val()" aria-label="Pop">⬇ Pop</button>
<button onclick="peek_val()" aria-label="Peek">👁 Peek</button>
<button onclick="reset()" aria-label="Reset">🔄 Reset</button>"""

    script = """
const c = document.getElementById('sim');
const ctx = c.getContext('2d');
let stack = [], msg = '';

function draw() {
  ctx.clearRect(0, 0, c.width, c.height);
  ctx.strokeStyle = '#4ea8de'; ctx.lineWidth = 2;
  const bx = 280, by = 20, bw = 200, bh = 320;
  ctx.strokeRect(bx, by, bw, bh);
  ctx.fillStyle = '#aaa'; ctx.font = '14px system-ui';
  ctx.fillText('Stack', bx + 75, by - 5);
  
  stack.forEach((v, i) => {
    const y = by + bh - (i + 1) * 35;
    ctx.fillStyle = i === stack.length - 1 ? '#e94560' : '#4ea8de';
    ctx.fillRect(bx + 5, y, bw - 10, 30);
    ctx.fillStyle = '#fff'; ctx.font = '16px monospace';
    ctx.fillText(String(v), bx + 85, y + 20);
  });
  
  if (msg) { ctx.fillStyle = '#ffd700'; ctx.font = '16px system-ui'; ctx.fillText(msg, 20, 350); }
}

function push_val() {
  if (stack.length >= 9) { msg = 'Stack Overflow!'; draw(); return; }
  const v = Math.floor(Math.random() * 99) + 1;
  stack.push(v); msg = 'push(' + v + ')'; draw();
}
function pop_val() {
  if (!stack.length) { msg = 'Stack Underflow!'; draw(); return; }
  const v = stack.pop(); msg = 'pop() → ' + v; draw();
}
function peek_val() {
  msg = stack.length ? 'peek() → ' + stack[stack.length-1] : 'Stack vacío';
  draw();
}
function reset() { stack = []; msg = ''; draw(); }
reset();
"""
    return controls, script


def generate_generic(spec: dict) -> tuple[str, str]:
    """Genera un template genérico para tipos no específicos."""
    controls = '<button onclick="draw()" aria-label="Ejecutar">▶ Ejecutar</button>'
    script = """
const c = document.getElementById('sim');
const ctx = c.getContext('2d');
function draw() {
  ctx.clearRect(0, 0, c.width, c.height);
  ctx.fillStyle = '#4ea8de'; ctx.font = '20px system-ui';
  ctx.fillText('Simulación de """ + spec.get("type", "custom") + """', 200, 180);
  ctx.fillStyle = '#aaa'; ctx.font = '14px system-ui';
  ctx.fillText('Personalizar en el HTML generado', 230, 220);
}
draw();
"""
    return controls, script


TYPE_GENERATORS = {
    "sorting-visualizer": generate_sorting_visualizer,
    "stack-simulator": generate_stack_simulator,
}


def generate_html(spec: dict) -> str:
    """Genera el HTML completo a partir de una spec."""
    sim_type = spec.get("type", "custom")
    generator = TYPE_GENERATORS.get(sim_type, generate_generic)
    controls, script = generator(spec)

    return HTML_TEMPLATE.format(
        title=spec.get("title", "Simulación EDU"),
        concept=spec.get("concept", ""),
        sim_type=sim_type,
        bloom_level=spec.get("bloom_level", "apply"),
        controls=controls,
        script=script,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generador de HTML interactivo")
    parser.add_argument("--spec", required=True, help="Ruta a la spec JSON")
    parser.add_argument("--topic", required=True, help="ID del tema")
    parser.add_argument("--course", required=True, help="ID del curso")
    args = parser.parse_args()

    root = find_project_root(Path(__file__).parent)
    config = load_yaml(root / "_edu" / "config.yaml")

    if not config.get("interactive_scenes_enabled", False):
        print("ℹ️  Simulaciones interactivas desactivadas (interactive_scenes_enabled: false)")
        return 0

    spec_path = Path(args.spec)
    if not spec_path.is_absolute():
        spec_path = root / "salida" / "cursadas" / args.course / "temas" / args.topic / spec_path

    if not spec_path.exists():
        print(f"❌ Spec no encontrada: {spec_path}")
        return 1

    spec = load_json(spec_path)
    sim_type = spec.get("type", "custom")
    if sim_type not in SUPPORTED_TYPES:
        print(f"❌ Tipo no soportado: {sim_type}. Válidos: {', '.join(sorted(SUPPORTED_TYPES))}")
        return 1

    html = generate_html(spec)

    # Verificar tamaño
    max_kb = config.get("interactive_max_size_kb", 500)
    size_kb = len(html.encode("utf-8")) / 1024
    if size_kb > max_kb:
        print(f"⚠️  HTML generado ({size_kb:.0f}KB) excede el límite ({max_kb}KB)")

    topic_folder = root / "salida" / "cursadas" / args.course / "temas" / args.topic
    output_dir = topic_folder / "interactivos"
    output_dir.mkdir(parents=True, exist_ok=True)

    name = spec.get("title", sim_type).lower().replace(" ", "-")
    output_path = output_dir / f"simulacion-{name}.html"
    output_path.write_text(html, encoding="utf-8")
    print(f"✅ Simulación generada: {output_path} ({size_kb:.0f}KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
