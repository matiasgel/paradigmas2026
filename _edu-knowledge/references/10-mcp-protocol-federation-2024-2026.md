# MCP Protocol & Cross-Campus Federation — Anthropic, 1EdTech, UNESCO (2024-2026)

**Fuentes:**
- Anthropic (2024-2025). *Model Context Protocol (MCP) Specification*, open-source
- 1EdTech (2024). *LTI 1.3 + LTI Advantage* + *CLR 2.0*
- UNESCO (2023). *Global Education Monitoring Report: Technology in Education*
**Relevancia Sprint:** S6.2

## MCP — Model Context Protocol

### Overview
- Protocolo estándar para que agentes AI consuman y provean servicios
- Open-source, specification-first
- Soporte nativo en VS Code, Cursor, Windsurf

### Tipos de Transporte
1. **stdio:** proceso local, comunicación por stdin/stdout (más simple)
2. **HTTP/SSE:** servidor remoto con Server-Sent Events
3. **Streamable HTTP:** nuevo en 2025, reemplaza SSE para bidireccional

### Componentes MCP
- **Tools:** funciones invocables (ej: `edu.search_memory(query)`)
- **Resources:** datos consultables (ej: `edu://schemas/filmina-slide`)
- **Prompts:** templates de prompts (ej: `edu://prompts/validate-plan`)

### Python SDK (mcp-python-sdk)
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("edu-server")

@mcp.tool()
def search_memory(query: str, course_id: str = None) -> str:
    """Busca en la memoria colectiva EDU."""
    # Implementación usa edu_memory.py existente
    ...

@mcp.resource("edu://schemas/{name}")
def get_schema(name: str) -> str:
    """Retorna un schema JSON del registry."""
    ...
```

### Configuración en VS Code
```json
// .vscode/mcp.json
{
  "servers": {
    "edu": {
      "type": "stdio",
      "command": "python",
      "args": ["edu-mcp-server/server.py"],
      "env": {}
    }
  }
}
```

## 1EdTech (antes IMS Global)

### LTI 1.3 + LTI Advantage (2024)
- Estándar de facto para herramientas educativas
- >5000 instituciones
- Permite single sign-on + grade passback entre LMS y tools externos
- **Relevancia EDU:** si EDU se expone como MCP server, podría eventualmente conectar con LTI

### CLR 2.0 — Comprehensive Learner Record (2024)
- Portabilidad de logros entre instituciones
- JSON-LD format
- **Relevancia EDU:** los analytics podrían exportar en CLR format

## UNESCO GEM Report (2023)
- 83 países adoptaron estándares de contenido educativo abierto
- Recomienda interoperabilidad como política pública
- Open Educational Resources (OER): >250k recursos compartidos
- **Relevancia EDU:** el MCP server podría federar contenido como OER

## Arquitectura MCP Server para EDU

### Tools Expuestos
```
edu.search_memory(query, course_id?) → resultados FTS5
edu.validate_plan(plan_json) → reporte de validación
edu.get_slide_template(type, profile) → template JSON
edu.compare_curricula(topic, universities[]) → tabla comparativa
edu.generate_quiz(topic, format, count) → preguntas GIFT/Forms
edu.check_accessibility(plan_json) → reporte WCAG
edu.cognitive_budget(filminas_md) → reporte de carga
edu.spaced_review(course_id) → calendario de repasos
```

### Resources Expuestos
```
edu://schemas/{schema_name} → JSON Schema
edu://templates/{template_name} → Markdown template
edu://memory/{course_id}/entries → entradas de memoria
edu://knowledge/{topic} → documentos de referencia
```

### Despliegue
1. **Local (stdio):** uso personal del docente en su VS Code
2. **HTTP:** para consumo desde otros workspaces/universidades
3. **Docker:** imagen autocontenida con SQLite + ChromaDB embebido

### Federación entre Universidades
- Cada universidad expone `edu.search_memory` públicamente (opt-in)
- Un índice central (DNS-like) resuelve qué universidades tienen contenido sobre un tema
- El `academic-researcher` consulta no solo papers sino también curricula de otras instancias EDU
