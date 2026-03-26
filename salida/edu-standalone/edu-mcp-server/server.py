#!/usr/bin/env python3
"""
EDU MCP Server — Expone funcionalidades core de EDU como tools MCP (stdio).

Uso:
  python edu-mcp-server/server.py

Configurar en .vscode/mcp.json:
  {
    "servers": {
      "edu": {
        "type": "stdio",
        "command": "python",
        "args": ["edu-mcp-server/server.py"]
      }
    }
  }

Tools expuestos:
  - edu.search_memory: Buscar en la memoria colectiva (SQLite FTS5)
  - edu.validate_plan: Validar un plan de filminas
  - edu.get_slide_template: Obtener template de slide por tipo
  - edu.search_knowledge: Buscar en ChromaDB knowledge base
"""

from __future__ import annotations

import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
except ImportError:
    print(
        "Error: mcp-sdk no instalado. Ejecutar:\n"
        "  pip install mcp\n"
        "Luego reiniciar el servidor.",
        file=sys.stderr,
    )
    sys.exit(1)


def _find_project_root() -> Path:
    """Busca la raíz del proyecto subiendo desde el directorio actual."""
    current = Path(__file__).resolve().parent.parent
    for candidate in [current, current.parent]:
        if (candidate / "salida" / "edu-standalone").exists():
            return candidate
    return current


PROJECT_ROOT = _find_project_root()
EDU_ROOT = PROJECT_ROOT / "salida" / "edu-standalone"
MEMORY_DB = PROJECT_ROOT / "_edu-memory" / "memory.db"

server = Server("edu-mcp-server")


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="edu.search_memory",
            description="Buscar en la memoria colectiva EDU (SQLite FTS5). Retorna entries que matchean la query.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Texto a buscar"},
                    "limit": {"type": "integer", "default": 10},
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="edu.validate_plan",
            description="Validar un plan de filminas JSON contra el schema EDU.",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "ID del tema (ej: 01-intro)"},
                    "course": {"type": "string", "description": "ID del curso (ej: leng-2026)"},
                },
                "required": ["topic", "course"],
            },
        ),
        Tool(
            name="edu.get_slide_template",
            description="Obtener el template de slide por tipo de filmina.",
            inputSchema={
                "type": "object",
                "properties": {
                    "slide_type": {
                        "type": "string",
                        "enum": [
                            "titulo", "concepto-abstracto", "codigo",
                            "diagrama", "socratica", "cierre",
                        ],
                    },
                },
                "required": ["slide_type"],
            },
        ),
        Tool(
            name="edu.search_knowledge",
            description="Buscar en la knowledge base ChromaDB de EDU (referencias académicas + herramientas).",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Texto a buscar"},
                    "n_results": {"type": "integer", "default": 5},
                    "doc_type": {
                        "type": "string",
                        "enum": ["reference", "tool", "all"],
                        "default": "all",
                    },
                },
                "required": ["query"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "edu.search_memory":
        return _search_memory(arguments["query"], arguments.get("limit", 10))
    elif name == "edu.validate_plan":
        return _validate_plan(arguments["topic"], arguments["course"])
    elif name == "edu.get_slide_template":
        return _get_slide_template(arguments["slide_type"])
    elif name == "edu.search_knowledge":
        return _search_knowledge(
            arguments["query"],
            arguments.get("n_results", 5),
            arguments.get("doc_type", "all"),
        )
    else:
        return [TextContent(type="text", text=f"Tool desconocido: {name}")]


def _search_memory(query: str, limit: int) -> list[TextContent]:
    if not MEMORY_DB.exists():
        return [TextContent(type="text", text="memory.db no encontrado.")]
    conn = sqlite3.connect(str(MEMORY_DB))
    try:
        cursor = conn.execute(
            "SELECT category, content, timestamp FROM memory_entries "
            "WHERE content MATCH ? ORDER BY rank LIMIT ?",
            (query, limit),
        )
        rows = cursor.fetchall()
        if not rows:
            return [TextContent(type="text", text=f"Sin resultados para: {query}")]
        results = []
        for cat, content, ts in rows:
            results.append(f"[{cat}] ({ts})\n{content[:300]}")
        return [TextContent(type="text", text="\n---\n".join(results))]
    except sqlite3.OperationalError:
        return [TextContent(type="text", text="Tabla memory_entries no existe aún.")]
    finally:
        conn.close()


def _validate_plan(topic: str, course: str) -> list[TextContent]:
    script = EDU_ROOT / "scripts" / "validate_plan.py"
    if not script.exists():
        return [TextContent(type="text", text="validate_plan.py no encontrado.")]
    result = subprocess.run(
        [sys.executable, str(script), "--topic", topic, "--course", course],
        capture_output=True,
        text=True,
        cwd=str(PROJECT_ROOT),
        timeout=60,
    )
    output = result.stdout or result.stderr or "Sin output"
    return [TextContent(type="text", text=output[:2000])]


def _get_slide_template(slide_type: str) -> list[TextContent]:
    templates = {
        "titulo": "# {title}\n\n**Subtítulo:** {subtitle}\n**Imagen:** {image_description}",
        "concepto-abstracto": "# {title}\n\n{body}\n\n**Imagen:** {image_description}\n**Alt text:** {alt_text}",
        "codigo": "# {title}\n\n```{language}\n{code}\n```\n\n**Notas:** {notes}",
        "diagrama": "# {title}\n\n**Diagrama:** {diagram_description}\n**Nodos:** max 7 (Miller)\n**Flechas:** con labels",
        "socratica": "# {title} ← pregunta\n\n1. {opcion_1}\n2. {opcion_2}\n3. {opcion_3}\n\n**Pausa sugerida:** 30 seg",
        "cierre": "# {title}\n\n**Resumen:** {key_points}\n**Próxima clase:** {next_topic}",
    }
    template = templates.get(slide_type, "Tipo de slide no reconocido.")
    return [TextContent(type="text", text=template)]


def _search_knowledge(query: str, n_results: int, doc_type: str) -> list[TextContent]:
    script = EDU_ROOT / "scripts" / "knowledge_base.py"
    if not script.exists():
        return [TextContent(type="text", text="knowledge_base.py no encontrado.")]
    args = [sys.executable, str(script), "search", query, "--n", str(n_results)]
    if doc_type != "all":
        args.extend(["--type", doc_type])
    result = subprocess.run(
        args, capture_output=True, text=True, cwd=str(PROJECT_ROOT), timeout=60
    )
    output = result.stdout or result.stderr or "Sin resultados"
    return [TextContent(type="text", text=output[:3000])]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
