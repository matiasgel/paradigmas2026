import unicodedata
import textwrap
from pathlib import Path

md_path = Path(r"c:\Users\matia\paradigmas2026\salida\cursadas\2026\temas\01-diseno-agil-python\guia-estudio.md")
ps_path = md_path.with_suffix('.ps')
pdf_path = md_path.with_name('guia-estudio-ps.pdf')

raw = md_path.read_text(encoding='utf-8')


def asciify(text: str) -> str:
    normalized = unicodedata.normalize('NFKD', text)
    return ''.join(ch for ch in normalized if ord(ch) < 128)


def clean_markdown_inline(text: str) -> str:
    text = text.replace('**', '')
    text = text.replace('*', '')
    text = text.replace('`', '')
    text = text.replace('_', '')
    return text


def ps_escape(text: str) -> str:
    return text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')

lines = []
in_code = False
for raw_line in raw.splitlines():
    line = raw_line.rstrip('\r')
    if line.startswith('```'):
        if in_code:
            in_code = False
            lines.append('')
        else:
            in_code = True
            lines.append('')
        continue
    if in_code:
        lines.append('    ' + line)
        continue
    if line.startswith('# '):
        lines.append(clean_markdown_inline(line[2:]).upper())
        lines.append('')
        continue
    if line.startswith('## '):
        lines.append(clean_markdown_inline(line[3:]))
        lines.append('')
        continue
    if line.startswith('### '):
        lines.append(clean_markdown_inline(line[4:]))
        lines.append('')
        continue
    if line.startswith('#### '):
        lines.append(clean_markdown_inline(line[5:]))
        continue
    if line.startswith('>'):
        content = clean_markdown_inline(line.lstrip('> ').strip())
        lines.append('NOTE: ' + content)
        lines.append('')
        continue
    if line.startswith('|'):
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        lines.append(' | '.join(cells))
        continue
    if line.startswith(('- ', '* ', '+ ')):
        lines.append('• ' + clean_markdown_inline(line[2:].strip()))
        continue
    if not line.strip():
        lines.append('')
        continue
    lines.append(clean_markdown_inline(line))

wrapped = []
for line in lines:
    ascii_line = asciify(line)
    if not ascii_line:
        wrapped.append('')
        continue
    if ascii_line.startswith('    '):
        wrapped.append(ascii_line)
        continue
    wrapped.extend(textwrap.wrap(ascii_line, width=90) or [''])

ps_lines = []
ps_lines.append('%!PS-Adobe-3.0')
ps_lines.append('%%Pages: (atend)')
ps_lines.append('%%PageOrder: Ascend')
ps_lines.append('%%BoundingBox: 0 0 595 842')
ps_lines.append('%%EndComments')
page_num = 1
line_height = 12
x = 40
page_top = 820
current_y = page_top
ps_lines.append(f'%%Page: {page_num} {page_num}')
ps_lines.append('/Courier findfont 10 scalefont setfont')

for line in wrapped:
    if current_y < 60:
        ps_lines.append('showpage')
        page_num += 1
        ps_lines.append(f'%%Page: {page_num} {page_num}')
        ps_lines.append('/Courier findfont 10 scalefont setfont')
        current_y = page_top
    if not line:
        current_y -= line_height
        continue
    escaped = ps_escape(line)
    ps_lines.append(f'{x} {current_y} moveto ({escaped}) show')
    current_y -= line_height

ps_lines.append('showpage')
ps_lines.append('%%EOF')

ps_path.write_text('\n'.join(ps_lines), encoding='ascii', errors='ignore')
print(f'Wrote PS: {ps_path}')
print(f'Lines: {len(wrapped)}')
