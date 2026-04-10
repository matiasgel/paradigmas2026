import glob, re, os

BASE = r"c:\Users\matia\paradigmas2026\salida\cursadas\iapjn-2026\temas"

REMOVE_PATTERNS = [
    # HTML comments with BORRADOR or PROVISIONAL
    re.compile(r'^\s*<!--.*?(BORRADOR|PROVISIONAL).*?-->\s*$', re.IGNORECASE),
    # HTML comments with agent names (Study Guide Writer, Class Writer, etc.)
    re.compile(r'^\s*<!--.*?(Study Guide Writer|Class Writer|Sofía|Roberto|Valeria|Carlos|Marcos|Elena|Ana).*?-->\s*$', re.IGNORECASE),
    # Footer lines: *Algo generada/o por ... (Writer) ... *
    re.compile(r'^\s*\*[^*]*(generad[ao]\s+por|Study Guide Writer|Class Writer)[^*]*\*\s*$', re.IGNORECASE),
]

files = sorted(
    glob.glob(os.path.join(BASE, "**", "guia-*.md"), recursive=True) +
    glob.glob(os.path.join(BASE, "**", "minuta.md"), recursive=True)
)

changed = 0
for fpath in files:
    with open(fpath, encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if any(p.match(line) for p in REMOVE_PATTERNS):
            continue
        new_lines.append(line)

    # Remove trailing blank lines at end of file, keep one newline
    while new_lines and new_lines[-1].strip() == "":
        new_lines.pop()
    if new_lines:
        new_lines.append("\n")

    if new_lines != lines:
        with open(fpath, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        rel = os.path.relpath(fpath, BASE)
        print(f"  cleaned: {rel}")
        changed += 1

print(f"\nDone: {changed}/{len(files)} files modified.")
