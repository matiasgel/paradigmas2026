"""
generate_guide_pdf.py — Genera PDFs a partir de guías de estudio y profesor en Markdown.
Uso:
    python scripts/generate_guide_pdf.py <archivo.md> [salida.pdf]
    python scripts/generate_guide_pdf.py --tema 01-diseno-agil-python

Requisitos: fpdf2 >= 2.8, markdown >= 3.0
"""
import sys
import os
import re
import argparse
from pathlib import Path

# Add project root to path
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent

try:
    from fpdf import FPDF
except ImportError:
    print("ERROR: fpdf2 no instalado. Ejecutar: pip install fpdf2")
    sys.exit(1)

try:
    import markdown
    MD_AVAILABLE = True
except ImportError:
    MD_AVAILABLE = False


# ─── Conversión de caracteres Unicode → Latin-1 segura ────────────────────
UNICODE_MAP = {
    "\u2014": "--",   # em dash —
    "\u2013": "-",    # en dash –
    "\u00b7": ".",    # middle dot ·
    "\u2192": "->",   # →
    "\u2190": "<-",   # ←
    "\u2022": "*",    # bullet •
    "\u25e6": "-",    # white bullet ◦
    "\u25b8": ">",    # black right-pointing triangle ▸
    "\u2713": "OK",   # ✓
    "\u2714": "OK",   # ✔
    "\u2717": "X",    # ✗
    "\u2718": "X",    # ✘
    "\u2716": "X",    # ✖
    "\u2611": "[X]",  # ☑
    "\u2610": "[ ]",  # ☐
    "\u2705": "[OK]", # ✅
    "\u274c": "[X]",  # ❌
    "\u26a0": "[!]",  # ⚠️
    "\u00e9": "e",    # é → normalizar para seguridad (aunque es latin-1)
    "\u201c": '"',    # " left double quotation
    "\u201d": '"',    # " right double quotation
    "\u2018": "'",    # ' left single quotation
    "\u2019": "'",    # ' right single quotation
    "\u00b0": " deg", # °
    "\u03c0": "pi",   # π
    "\u221a": "sqrt", # √
    "\u2264": "<=",   # ≤
    "\u2265": ">=",   # ≥
    "\u00d7": "x",    # ×
    "\u00f7": "/",    # ÷
    "\u2026": "...",  # …
    "\u00ab": "<<",   # «
    "\u00bb": ">>",   # »
    "\uff5c": "|",    # ｜ fullwidth
    "\u23b3": "V",    # ⎳
    "\u25bc": "v",    # ▼
    "\u25ba": ">",    # ►
    "\ufb01": "fi",   # ﬁ ligature
    "\ufb02": "fl",   # ﬂ ligature
    "\u00a0": " ",    # non-breaking space
}


def s(text: str) -> str:
    """Sanitiza texto para compatibilidad Latin-1 con fpdf2 core fonts."""
    for ch, replacement in UNICODE_MAP.items():
        text = text.replace(ch, replacement)
    # Eliminar cualquier carácter fuera de Latin-1 restante
    return text.encode("latin-1", errors="replace").decode("latin-1")


# ─── Colores institucionales ───────────────────────────────────────────────
COLOR_BORDO   = (139, 0, 0)
COLOR_DARK    = (30, 30, 30)
COLOR_GRAY    = (100, 100, 100)
COLOR_LIGHT   = (240, 240, 240)
COLOR_WHITE   = (255, 255, 255)
COLOR_CODE_BG = (248, 248, 248)
COLOR_BLUE    = (0, 80, 160)


class GuiaPDF(FPDF):
    """PDF para Guías EDU — diseño institucional UNTDF."""

    def __init__(self, titulo_doc: str = "", docente: str = "Prof. Matias Gel"):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.titulo_doc = titulo_doc
        self.docente = docente
        self.set_auto_page_break(auto=True, margin=22)
        self.set_margins(left=20, top=20, right=20)
        self._in_code_block = False
        self._code_buffer = []
        self._current_h_level = 0

    def header(self):
        if self.page_no() == 1:
            return
        # Línea decorativa bordo
        self.set_fill_color(*COLOR_BORDO)
        self.rect(0, 0, 210, 5, "F")
        # Título cabecera
        self.set_font("Helvetica", "B", 7)
        self.set_text_color(*COLOR_WHITE)
        self.set_xy(20, 7)
        self.cell(0, 4, s(self.titulo_doc), align="L")
        self.set_xy(20, 7)
        self.cell(0, 4, s(f"Docente: {self.docente}"), align="R")
        self.ln(6)

    def footer(self):
        self.set_y(-15)
        self.set_fill_color(*COLOR_BORDO)
        self.rect(0, 282, 210, 5, "F")
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*COLOR_GRAY)
        self.cell(0, 5, s("IF009 - Laboratorio de Programacion y Lenguajes 2026 - UNTDF-IDEI"), align="C")
        self.set_xy(170, -15)
        self.set_font("Helvetica", "B", 8)
        self.cell(0, 5, f"Pág. {self.page_no()}", align="R")

    def cover_page(self, title: str, subtitle: str, university: str, details: list[str]):
        """Genera la portada del documento."""
        self.add_page()
        # Banda bordo superior
        self.set_fill_color(*COLOR_BORDO)
        self.rect(0, 0, 210, 45, "F")
        # Título principal
        self.set_font("Helvetica", "B", 22)
        self.set_text_color(*COLOR_WHITE)
        self.set_xy(20, 15)
        self.multi_cell(170, 10, s(title), align="C")
        # Subtítulo
        self.set_font("Helvetica", "", 11)
        self.set_xy(20, 36)
        self.multi_cell(170, 5, s(subtitle), align="C")

        # Línea separadora
        self.set_y(48)
        self.set_draw_color(*COLOR_BORDO)
        self.set_line_width(0.5)
        self.line(20, self.get_y(), 190, self.get_y())

        # Universidad
        self.ln(8)
        self.set_x(20)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(*COLOR_DARK)
        self.multi_cell(170, 7, s(university), align="C")

        # Detalles
        self.ln(5)
        for detail in details:
            self.set_x(20)
            self.set_font("Helvetica", "", 10)
            self.set_text_color(*COLOR_GRAY)
            self.multi_cell(170, 6, s(detail), align="C")

        # Box docente
        self.set_y(130)
        self.set_fill_color(*COLOR_LIGHT)
        self.rect(40, 125, 130, 22, "F")
        self.set_xy(40, 128)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*COLOR_GRAY)
        self.cell(130, 5, s("Docente"), align="C")
        self.set_xy(40, 133)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(*COLOR_DARK)
        self.cell(130, 8, s(self.docente), align="C")

        # Año académico
        self.set_y(200)
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(*COLOR_BORDO)
        self.cell(0, 10, "2026", align="C")

        # Franja bordo inferior
        self.set_fill_color(*COLOR_BORDO)
        self.rect(0, 275, 210, 22, "F")
        self.set_xy(0, 280)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*COLOR_WHITE)
        self.cell(210, 5, s("IF009 - Laboratorio de Programacion y Lenguajes - UNTDF - Instituto IDEI"), align="C")

    def h1(self, text: str):
        self.ln(6)
        self.set_fill_color(*COLOR_BORDO)
        self.rect(20, self.get_y(), 170, 9, "F")
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(*COLOR_WHITE)
        self.set_x(20)
        self.cell(170, 9, s(text), align="L", fill=False)
        self.ln(11)
        self.set_text_color(*COLOR_DARK)

    def h2(self, text: str):
        self.ln(4)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(*COLOR_BORDO)
        self.set_x(20)
        self.multi_cell(170, 6, s(text))
        self.set_draw_color(*COLOR_BORDO)
        self.set_line_width(0.3)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(3)
        self.set_text_color(*COLOR_DARK)

    def h3(self, text: str):
        self.ln(3)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*COLOR_DARK)
        self.set_x(20)
        self.cell(4, 5, "", fill=False)
        self.set_fill_color(*COLOR_BORDO)
        self.rect(20, self.get_y(), 2, 5, "F")
        self.set_x(24)
        self.multi_cell(166, 5, s(text))
        self.ln(1)

    def h4(self, text: str):
        self.ln(2)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*COLOR_GRAY)
        self.set_x(20)
        self.multi_cell(170, 5, s(f"> {text}"))
        self.ln(1)
        self.set_text_color(*COLOR_DARK)

    def body_text(self, text: str):
        if not text.strip():
            return
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*COLOR_DARK)
        self.set_x(20)
        self.multi_cell(170, 5, s(text))
        self.ln(1)

    def code_block(self, code: str, lang: str = ""):
        """Bloque de código monoespaciado con fondo."""
        lines = code.strip().split("\n")
        # Calcular altura estimada
        line_h = 4
        total_h = len(lines) * line_h + 6

        # Verificar que quepa en la página
        if self.get_y() + total_h > (297 - 22):
            self.add_page()

        y_start = self.get_y()
        # Fondo
        self.set_fill_color(*COLOR_CODE_BG)
        self.set_draw_color(200, 200, 200)
        self.set_line_width(0.2)
        self.rect(20, y_start, 170, total_h, "DF")

        # Label lenguaje
        if lang:
            self.set_font("Helvetica", "I", 6)
            self.set_text_color(*COLOR_GRAY)
            self.set_xy(185 - len(lang) * 2, y_start + 1)
            self.cell(0, 3, s(lang), align="R")

        # Código
        self.set_font("Courier", "", 7.5)
        self.set_text_color(50, 50, 120)
        self.set_xy(23, y_start + 3)
        for line in lines:
            if len(line) > 100:
                line = line[:97] + "..."
            self.set_x(23)
            self.cell(164, line_h, s(line), ln=True)

        self.set_y(y_start + total_h + 2)
        self.set_text_color(*COLOR_DARK)

    def blockquote(self, text: str):
        """Cita o nota destacada."""
        y = self.get_y()
        self.set_fill_color(*COLOR_BORDO)
        self.rect(20, y, 2, 8, "F")
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(60, 60, 90)
        self.set_xy(24, y)
        self.multi_cell(166, 5, s(text.strip()))
        self.ln(2)
        self.set_text_color(*COLOR_DARK)

    def bullet_item(self, text: str, level: int = 0):
        indent = 20 + level * 5
        width = 170 - level * 5
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*COLOR_DARK)
        bullet = "-" if level == 0 else " -"
        self.set_x(indent)
        self.cell(4, 5, bullet)
        self.set_x(indent + 4)
        self.multi_cell(width - 4, 5, s(text.strip()))

    def table_from_md(self, rows: list[list[str]], has_header: bool = True):
        """Renderiza tabla simple desde filas de texto."""
        if not rows:
            return
        col_count = max(len(r) for r in rows)
        if col_count == 0:
            return

        avail = 170
        col_w = avail / col_count
        line_h = 5

        for i, row in enumerate(rows):
            if i == 1 and has_header:
                continue  # saltar fila separadora ---
            is_header = (i == 0 and has_header)

            y = self.get_y()
            if y + line_h > (297 - 22):
                self.add_page()
                y = self.get_y()

            self.set_x(20)
            for j, cell_text in enumerate(row):
                cell_text = cell_text.strip()
                if is_header:
                    self.set_fill_color(*COLOR_BORDO)
                    self.set_text_color(*COLOR_WHITE)
                    self.set_font("Helvetica", "B", 8)
                    fill = True
                elif i % 2 == 0:
                    self.set_fill_color(*COLOR_LIGHT)
                    self.set_text_color(*COLOR_DARK)
                    self.set_font("Helvetica", "", 8)
                    fill = True
                else:
                    self.set_fill_color(*COLOR_WHITE)
                    self.set_text_color(*COLOR_DARK)
                    self.set_font("Helvetica", "", 8)
                    fill = True

                self.set_draw_color(200, 200, 200)
                self.set_line_width(0.1)
                # Truncar texto largo
                if len(cell_text) > int(col_w * 1.5):
                    cell_text = cell_text[:int(col_w * 1.5) - 3] + "..."
                x_pos = 20 + j * col_w
                self.set_xy(x_pos, y)
                self.cell(col_w, line_h, s(cell_text), border=1, fill=fill)
            self.ln(line_h)

        self.set_text_color(*COLOR_DARK)
        self.ln(2)


# ─── Parser de Markdown ────────────────────────────────────────────────────

def parse_md_to_pdf(pdf: GuiaPDF, content: str):
    """Parsea el contenido Markdown y lo renderiza en el PDF."""
    lines = content.split("\n")
    i = 0
    in_code_block = False
    code_lang = ""
    code_lines = []
    in_table = False
    table_rows = []
    in_blockquote = False
    bq_text = ""

    while i < len(lines):
        line = lines[i]

        # ── Bloques de código ─────────────────────────────────────────────
        if line.startswith("```"):
            if not in_code_block:
                in_code_block = True
                code_lang = line[3:].strip()
                code_lines = []
            else:
                in_code_block = False
                pdf.code_block("\n".join(code_lines), code_lang)
                code_lines = []
                code_lang = ""
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # ── Tablas Markdown ───────────────────────────────────────────────
        if line.startswith("|"):
            # Inicio o continuación de tabla
            if not in_table:
                in_table = True
                table_rows = []
            cells = [c for c in line.split("|") if c != ""]
            table_rows.append(cells)
            i += 1
            continue
        else:
            if in_table:
                # Verificar si la fila 2 es separadora
                if len(table_rows) >= 2:
                    sep = table_rows[1]
                    if all(re.match(r'^[-:\s]+$', c.strip()) for c in sep):
                        pdf.table_from_md(table_rows, has_header=True)
                    else:
                        pdf.table_from_md(table_rows, has_header=False)
                elif table_rows:
                    pdf.table_from_md(table_rows, has_header=False)
                in_table = False
                table_rows = []

        # ── Blockquotes ───────────────────────────────────────────────────
        if line.startswith(">"):
            bq_content = line[1:].strip()
            # Limpiar marcadores MD de la cita
            bq_content = re.sub(r'\*\*(.+?)\*\*', r'\1', bq_content)
            bq_content = re.sub(r'\*(.+?)\*', r'\1', bq_content)
            bq_content = re.sub(r'`(.+?)`', r'\1', bq_content)
            if bq_content:  # no vacía
                pdf.blockquote(bq_content)
            i += 1
            continue

        # ── Línea horizontal ──────────────────────────────────────────────
        if re.match(r'^[-─]{3,}$', line.strip()):
            pdf.set_draw_color(200, 200, 200)
            pdf.set_line_width(0.2)
            pdf.line(20, pdf.get_y(), 190, pdf.get_y())
            pdf.ln(3)
            i += 1
            continue

        # ── Headings ──────────────────────────────────────────────────────
        if line.startswith("#### "):
            text = clean_inline(line[5:])
            pdf.h4(text)
            i += 1
            continue
        if line.startswith("### "):
            text = clean_inline(line[4:])
            pdf.h3(text)
            i += 1
            continue
        if line.startswith("## "):
            text = clean_inline(line[3:])
            pdf.h2(text)
            i += 1
            continue
        if line.startswith("# "):
            text = clean_inline(line[2:])
            pdf.h1(text)
            i += 1
            continue

        # ── Listas ────────────────────────────────────────────────────────
        m_bullet = re.match(r'^(\s*)([-*+]|\d+\.) (.+)$', line)
        if m_bullet:
            indent_str, bullet_char, text = m_bullet.groups()
            level = len(indent_str) // 2
            text = clean_inline(text)
            pdf.bullet_item(text, level)
            i += 1
            continue

        # ── Checkbox de lista de tareas ───────────────────────────────────
        m_check = re.match(r'^(\s*)[-*] \[([ xX])\] (.+)$', line)
        if m_check:
            indent_str, checked, text = m_check.groups()
            level = len(indent_str) // 2
            mark = "☑" if checked.lower() == "x" else "☐"
            text = clean_inline(f"{mark} {text}")
            pdf.bullet_item(text, level)
            i += 1
            continue

        # ── Línea vacía ───────────────────────────────────────────────────
        if not line.strip():
            pdf.ln(2)
            i += 1
            continue

        # ── Texto de párrafo normal ────────────────────────────────────────
        # Juntar líneas consecutivas del mismo párrafo
        para_lines = [line]
        j = i + 1
        while j < len(lines):
            next_line = lines[j]
            if (not next_line.strip() or
                    next_line.startswith("#") or
                    next_line.startswith(">") or
                    next_line.startswith("|") or
                    next_line.startswith("```") or
                    re.match(r'^(\s*)([-*+]|\d+\.) ', next_line) or
                    re.match(r'^[-─]{3,}$', next_line.strip())):
                break
            para_lines.append(next_line)
            j += 1

        para = " ".join(para_lines).strip()
        if para:
            para = clean_inline(para)
            pdf.body_text(para)
        i = j

    # Cerrar tabla si quedó abierta
    if in_table and table_rows:
        pdf.table_from_md(table_rows, has_header=True)


def clean_inline(text: str) -> str:
    """Limpia formateo inline de Markdown para texto plano."""
    # Negrita
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    # Cursiva
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    # Código inline
    text = re.sub(r'`(.+?)`', r'[\1]', text)
    # Links
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    # HTML comments
    text = re.sub(r'<!--.+?-->', '', text)
    # Iconos emoji problemáticos — simplificar
    return text.strip()


def generate_pdf(md_path: Path, pdf_path: Path, is_student_guide: bool = True):
    """Genera un PDF a partir de un archivo Markdown."""
    print(f"  📄 Procesando: {md_path.name}")

    content = md_path.read_text(encoding="utf-8")

    # Extraer metadatos de las primeras líneas
    lines = content.split("\n")
    title = "Guía de Estudio"
    subtitle = ""
    university = "Universidad Nacional de Tierra del Fuego — Instituto IDEI"
    docente = "Prof. Matias Gel"
    details = []

    for line in lines[:10]:
        if line.startswith("# "):
            title = clean_inline(line[2:])
        elif line.startswith("## ") and not subtitle:
            subtitle = clean_inline(line[3:])
        elif "> **Docente:**" in line:
            docente = re.sub(r'.*\*\*Docente:\*\*\s*(.+)', r'\1', line).strip()
        elif "> **Para:**" in line:
            docente_match = re.search(r'Para:\*\*\s*(.+)', line)
            if docente_match:
                details.append(docente_match.group(1).strip())
        elif "> **Dirigida a:**" in line or "> **TP asociado:**" in line or "> **Deadline" in line:
            detail = re.sub(r'> \*\*[^:]+:\*\*\s*', '', line).strip()
            if detail:
                details.append(detail)

    pdf = GuiaPDF(titulo_doc=clean_inline(title), docente=docente)

    # Portada
    pdf.cover_page(
        title=clean_inline(title),
        subtitle=clean_inline(subtitle),
        university=university,
        details=details
    )

    # Contenido
    pdf.add_page()

    # Saltar las primeras líneas de metadatos (cabecera del doc)
    # Encontrar el primer --- y empezar después
    try:
        first_sep = content.index("\n---\n")
        body_content = content[first_sep + 5:]
    except ValueError:
        body_content = content

    parse_md_to_pdf(pdf, body_content)

    pdf.output(str(pdf_path))
    print(f"  ✅ PDF generado: {pdf_path.name} ({pdf_path.stat().st_size // 1024} KB)")


# ─── CLI ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Genera PDFs de guías EDU")
    parser.add_argument("--tema", help="Slug del tema (ej: 01-diseno-agil-python)")
    parser.add_argument("archivo", nargs="?", help="Archivo .md específico")
    parser.add_argument("--salida", help="Archivo PDF de salida")
    args = parser.parse_args()

    if args.tema:
        tema_dir = PROJECT_ROOT / "salida" / "cursadas" / "2026" / "temas" / args.tema
        if not tema_dir.exists():
            print(f"ERROR: No existe el directorio del tema: {tema_dir}")
            sys.exit(1)

        guias = [
            (tema_dir / "guia-estudio.md", tema_dir / "guia-estudio.pdf", True),
            (tema_dir / "guiaprofesor.md", tema_dir / "guiaprofesor.pdf", False),
        ]

        print(f"\n🎓 Generando PDFs para tema: {args.tema}")
        for md_path, pdf_path, is_student in guias:
            if md_path.exists():
                generate_pdf(md_path, pdf_path, is_student)
            else:
                print(f"  ⚠️  No encontrado: {md_path.name}")

    elif args.archivo:
        md_path = Path(args.archivo)
        if not md_path.exists():
            print(f"ERROR: No existe el archivo: {md_path}")
            sys.exit(1)
        pdf_path = Path(args.salida) if args.salida else md_path.with_suffix(".pdf")
        generate_pdf(md_path, pdf_path)

    else:
        parser.print_help()
        sys.exit(1)

    print("\n✅ Proceso completado.")


if __name__ == "__main__":
    main()
