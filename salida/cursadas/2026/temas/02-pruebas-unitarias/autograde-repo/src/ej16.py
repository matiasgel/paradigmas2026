def contar_lineas(ruta: str) -> int:
    """Abre el archivo en ruta y retorna la cantidad de líneas."""
    with open(ruta, 'r') as f:
        return len(f.readlines())


def primera_linea(ruta: str) -> str:
    """Retorna la primera línea del archivo (sin salto de línea). Lanza FileNotFoundError si no existe."""
    with open(ruta, 'r') as f:
        linea = f.readline()
        return linea.rstrip('\n')
