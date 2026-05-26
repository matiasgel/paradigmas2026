import json, sys, re
from pathlib import Path

plan = json.load(open('salida/cursadas/2026/temas/10-tipos-de-datos/slides/plan-filminas-10-tipos-de-datos.json', encoding='utf-8'))
registry = json.load(open('_edu/schemas/schema-registry.json', encoding='utf-8'))

errors = []
slides = plan.get('slides', [])
summary = plan.get('summary', {})
type_layout_map = registry.get('type_layout_map', {})

images_count = sum(1 for s in slides if s.get('image',{}).get('layer','none') != 'none')
max_images = 12
if images_count > max_images:
    errors.append(f'BUDGET: {images_count} imagenes planificadas (max={max_images})')

pending = sum(1 for s in slides if s.get('image',{}).get('layer','none') != 'none' and not s.get('image',{}).get('prompt','').strip())
if pending > 0:
    bad = [s['id'] for s in slides if s.get('image',{}).get('layer','none') != 'none' and not s.get('image',{}).get('prompt','').strip()]
    errors.append(f'PROMPTS: {pending} prompts vacios: {bad}')

for slide in slides:
    sid = slide.get('id','?')
    stype = slide.get('type','')
    if stype not in type_layout_map:
        continue
    exp = type_layout_map[stype]
    for zone in ('title','body','image','code','table'):
        ev = exp.get('layout',{}).get(zone)
        av = slide.get('layout',{}).get(zone)
        if ev and av and ev != av:
            errors.append(f'DETERMINISMO [{sid}]: layout.{zone}={av!r} != {ev!r}')
    exp_layer = exp.get('image_layer','none')
    act_layer = slide.get('image',{}).get('layer','none')
    if exp_layer != act_layer:
        errors.append(f'DETERMINISMO [{sid}]: image.layer={act_layer!r} != {exp_layer!r}')

seen = set()
for s in slides:
    sid = s.get('id','?')
    if not re.match(r'^F-[0-9]{2,3}$', sid):
        errors.append(f'ID [{sid}]: formato invalido')
    if sid in seen:
        errors.append(f'DUPLICADO: {sid}')
    seen.add(sid)

real_dist = {}
for s in slides:
    t = s.get('type','')
    real_dist[t] = real_dist.get(t,0) + 1
if summary.get('type_distribution',{}) != real_dist:
    errors.append(f'SUMMARY: type_distribution incorrecta. Real: {real_dist}')

if summary.get('total_slides') != len(slides):
    errors.append(f'SUMMARY: total_slides={summary.get("total_slides")} != {len(slides)}')

for s in slides:
    sid = s.get('id','?')
    n_tables = len(s.get('tables',[]))
    n_assets = len(s.get('table_assets',[]))
    if n_tables != n_assets:
        errors.append(f'TABLE_ASSETS [{sid}]: {n_tables} tablas != {n_assets} assets')

n_code = sum(1 for s in slides if s.get('code_blocks'))
if summary.get('code_slides') != n_code:
    errors.append(f'SUMMARY: code_slides={summary.get("code_slides")} != real {n_code}')

n_tables_total = sum(len(s.get('tables',[])) for s in slides)
if summary.get('tables_planned') != n_tables_total:
    errors.append(f'SUMMARY: tables_planned={summary.get("tables_planned")} != real {n_tables_total}')

if errors:
    print(f'\nVALIDACION - {len(errors)} error(es):')
    for i, e in enumerate(errors, 1):
        print(f'  {i:2d}. {e}')
    sys.exit(1)
else:
    print('\nVALIDACION EXITOSA')
    print(f'   Slides: {len(slides)} | Imagenes: {images_count} | Tablas: {n_tables_total} | Codigo: {n_code}')
    sys.exit(0)
