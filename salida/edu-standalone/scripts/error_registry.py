#!/usr/bin/env python3
"""
error_registry.py — Registro persistente de errores de publicación (EDU Standalone)
======================================================================================
Almacena, consulta y expone reglas de prevención de errores cometidos en ciclos
anteriores de publicación. El archivo de almacenamiento (error-registry.jsonl) usa
formato JSONL (una entrada JSON compacta por línea) con estrategia git merge=union,
lo que permite que todas las ramas contribuyan entradas sin conflictos de merge.

OBLIGATORIO:
  ANTES de generar el plan:   python scripts/error_registry.py rules
  DESPUÉS de un error:        python scripts/error_registry.py record --phase FASE2 ...

Comandos:
  rules   [--phase FASE1|FASE2|...] [--type TIPO]    Reglas de prevención ordenadas
  query   [--phase ...] [--type ...] [--last N]       Consultar entradas históricas
  record  --phase FASE2 --type schema --desc "..."    Registrar nuevo error
          [--topic TEMA] [--course ID] [--cause "..."] [--prevention "..."]
          [--context '{"clave":"valor"}']
  resolve --id UUID --resolution "cómo se resolvió"  Marcar como resuelto
  stats                                               Estadísticas globales

Uso como módulo Python:
  from error_registry import ErrorRegistry
  reg = ErrorRegistry()
  reg.record(phase="FASE2", error_type="schema_violation", description="...", topic="tema-01")
  rules = reg.get_prevention_rules(phase="FASE2")
"""
from __future__ import annotations

import argparse
import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ──────────────────────────────────────────────────────────────────────────────
# Configuración de rutas
# ──────────────────────────────────────────────────────────────────────────────

_THIS = Path(__file__).resolve()
_SCRIPTS = _THIS.parent
_ROOT = _SCRIPTS.parent

# Ruta al registro persistente — en la raíz del módulo edu-standalone
# Este archivo usa merge=union en .gitattributes → todas las ramas acumulan entradas
_REGISTRY_PATH = _ROOT / "error-registry.jsonl"

# ──────────────────────────────────────────────────────────────────────────────
# Constantes del dominio
# ──────────────────────────────────────────────────────────────────────────────

VALID_PHASES = ["FASE0", "FASE1", "FASE2", "FASE3", "FASE4", "agent"]

VALID_TYPES = [
    "schema_violation",   # Violación del contrato JSON Schema v3
    "accessibility",      # WCAG AA: contraste, alt_text, tipografía
    "layout_cognition",   # Reglas cognitivas Mayer/Garner
    "composition",        # Densidad visual, márgenes, superposiciones
    "fact_check",         # Verificación factual NLI
    "semantic_drift",     # Coherencia semántica inter-clases
    "pipeline",           # Fallo en slides_pipeline.py / API Google
    "thumbnails",         # Fallo en captura de thumbnails
    "agent_edit",         # Agente intentó modificar archivo protegido
    "repair_exhausted",   # repair_plan agotó intentos máximos
    "other",              # Otro
]

# Reglas de prevención predeterminadas del sistema por (phase, error_type).
# Se muestran siempre, incluso si el registro histórico está vacío.
_DEFAULT_RULES: dict[tuple[str, str], str] = {
    ("FASE1", "schema_violation"): (
        "Verificar que todos los campos requeridos del schema v3 estén presentes ANTES "
        "de ejecutar repair_plan.py. Los campos más frecuentemente omitidos: "
        "table_assets (debe ser lista vacía [] si no hay tablas), "
        "image.layer (nunca null, siempre string del registry), "
        "body_blocks (lista, nunca null). Usar repair_plan.py —nunca editar JSON manualmente."
    ),
    ("FASE1", "repair_exhausted"): (
        "Cuando repair_plan agota los 3 intentos, el plan tiene un error estructural "
        "profundo. Revisar filminas.md: ¿hay slides sin título? ¿tipos de slide que no "
        "existen en canonical_types del schema-registry.json? Regenerar el plan desde "
        "cero con FASE 1 completa antes de reintentar repair."
    ),
    ("FASE2", "schema_violation"): (
        "validate_plan.py detecta campos ausentes o nulos que repair_plan no corrigió. "
        "Síntomas más comunes: id no sigue patrón F-NN, $schema_version ausente, "
        "summary.total_slides no coincide con len(slides). "
        "Ejecutar validate_plan.py localmente antes de llamar publish_loop para diagnóstico."
    ),
    ("FASE2", "accessibility"): (
        "WCAG AA mínimo: contraste 4.5:1 texto normal, 3:1 texto grande (≥18pt). "
        "alt_text obligatorio en TODAS las imágenes (nunca vacío ni 'imagen'). "
        "Tamaño mínimo cuerpo: 18pt. Los colores del design system ya cumplen WCAG — "
        "no inventar paletas propias."
    ),
    ("FASE2", "layout_cognition"): (
        "Principio assertion-evidence (Sweller/Mayer): título = afirmación concisa, "
        "cuerpo = evidencia visual o dato. Max 5 bullets por slide. "
        "No superponer texto sobre imagen principal. "
        "Slides tipo 'content' sin imagen decorativa innecesaria."
    ),
    ("FASE2", "composition"): (
        "Densidad visual objetivo: 35-55%. Márgenes mínimos 48px todos los lados. "
        "No superponer elementos. Verificar densidad con validate_slide_composition.py "
        "—dry-run antes de publicar. Slides con >6 elementos visuales fallan el check."
    ),
    ("FASE2", "fact_check"): (
        "fact_verifier.py marca afirmaciones sin soporte en ChromaDB (edu_knowledge). "
        "Si una afirmación es correcta pero no está en el corpus: agregar [claim] al "
        "bullet o citar fuente bibliográfica. Si está mal → corregir en filminas.md. "
        "Para omitir en publicaciones urgentes: --skip-facts."
    ),
    ("FASE2", "semantic_drift"): (
        "semantic_drift_detector.py detecta cambio de terminología entre clases "
        "(cosine MiniLM > 0.35). Síntoma: un concepto llamado X en clase 1 y Y en clase 3. "
        "Solución: usar glosario del curso (glossary.json) y consistencia terminológica. "
        "Para omitir: --skip-drift."
    ),
    ("FASE3", "pipeline"): (
        "slides_pipeline.py falla por: (1) credenciales vencidas — regenerar token con "
        "python scripts/slides_pipeline.py --reauth, (2) Drive ID del template inaccesible "
        "— verificar slides-config.yaml.template_id, (3) timeout API — reintentar con "
        "--max-attempts 5. NUNCA hardcodear API keys."
    ),
    ("FASE4", "thumbnails"): (
        "capture_thumbnails.py requiere que la presentación esté publicada y accesible "
        "vía API. Causas comunes de fallo: (1) presentación en borrador, (2) permisos "
        "insuficientes, (3) timeout — la presentación puede tardar 30s en estar disponible "
        "tras publicar. El fallo de thumbnails NO revierte la publicación."
    ),
    ("agent", "agent_edit"): (
        "Los agentes NO pueden editar scripts/*.py ni _edu/schemas/*.json ni _edu/templates/*. "
        "Solo leer y ejecutar. Si el agente detecta que un script o schema necesita cambio, "
        "debe reportarlo al docente y escalar al Arquitecto. "
        "Modificar scripts sin versión controlada rompe la reproducibilidad del pipeline."
    ),
}


# ──────────────────────────────────────────────────────────────────────────────
# Clase principal
# ──────────────────────────────────────────────────────────────────────────────

class ErrorRegistry:
    """
    Registro persistente de errores de publicación.

    Formato de almacenamiento: JSONL (una entrada JSON compacta por línea).
    Estrategia git: merge=union → merges entre ramas acumulan entradas en lugar
    de generar conflictos. Esto asegura que el historial de errores de producción,
    main, lenguajes y otras ramas se unifique automáticamente.

    Esquema de cada entrada:
    {
      "id": "<uuid4>",
      "timestamp": "<ISO8601 UTC>",
      "schema_version": "1",
      "topic": "<nombre del tema o vacío>",
      "course": "<course_id o vacío>",
      "phase": "FASE1|FASE2|FASE3|FASE4|agent",
      "error_type": "<tipo del enum VALID_TYPES>",
      "description": "<descripción del error>",
      "root_cause": "<causa raíz identificada>",
      "context": {<datos adicionales del contexto>},
      "prevention_rule": "<regla para evitarlo a futuro>",
      "resolution": null | "<cómo se resolvió>",
      "resolved_at": null | "<ISO8601>",
      "status": "open|resolved",
      "recurrence_count": <int, cuántas veces ocurrió este error>
    }
    """

    def __init__(self, registry_path: Path | None = None) -> None:
        self.path = Path(registry_path or _REGISTRY_PATH)

    # ── I/O ───────────────────────────────────────────────────────────────────

    def _load_all(self) -> list[dict[str, Any]]:
        """Carga todas las entradas del registro. Tolerante a líneas vacías."""
        if not self.path.exists():
            return []
        entries: list[dict[str, Any]] = []
        with self.path.open(encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    print(
                        f"  ⚠️  Línea {lineno} inválida en registry ({exc}) — omitida",
                        file=sys.stderr,
                    )
        return entries

    def _append(self, entry: dict[str, Any]) -> None:
        """Agrega una entrada al final del archivo (append-only — amigable con merge=union)."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")

    def _rewrite(self, entries: list[dict[str, Any]]) -> None:
        """Reescribe el archivo completo (para operaciones de resolve/update)."""
        with self.path.open("w", encoding="utf-8") as fh:
            for entry in entries:
                fh.write(json.dumps(entry, ensure_ascii=False) + "\n")

    # ── Operaciones ───────────────────────────────────────────────────────────

    def record(
        self,
        phase: str,
        error_type: str,
        description: str,
        topic: str = "",
        course: str = "",
        root_cause: str = "",
        prevention_rule: str = "",
        context: dict[str, Any] | None = None,
    ) -> str:
        """
        Registra un error. Retorna el ID asignado (UUID4).

        Si ya existe un error abierto del mismo (phase, error_type, topic),
        incrementa su recurrence_count en lugar de crear una entrada nueva.
        La entrada nueva siempre se escribe al final (merge=union compatible).
        """
        entry_id = str(uuid.uuid4())

        # Calcular recurrencia basada en historial existente
        existing = self._load_all()
        recurrence = 1
        for e in existing:
            if (
                e.get("phase") == phase
                and e.get("error_type") == error_type
                and e.get("topic") == topic
                and e.get("status") != "resolved"
            ):
                recurrence = e.get("recurrence_count", 1) + 1
                break

        # Regla de prevención: usar la proporcionada, o buscar en defaults
        if not prevention_rule:
            prevention_rule = _DEFAULT_RULES.get(
                (phase, error_type),
                _DEFAULT_RULES.get(("agent", error_type), ""),
            )

        entry: dict[str, Any] = {
            "id": entry_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "schema_version": "1",
            "topic": topic,
            "course": course,
            "phase": phase,
            "error_type": error_type,
            "description": description,
            "root_cause": root_cause,
            "context": context or {},
            "prevention_rule": prevention_rule,
            "resolution": None,
            "resolved_at": None,
            "status": "open",
            "recurrence_count": recurrence,
        }
        self._append(entry)
        return entry_id

    def resolve(self, entry_id: str, resolution: str) -> bool:
        """
        Marca una entrada como resuelta. Retorna True si la encontró.
        Acepta ID completo (UUID) o prefijo (≥8 caracteres).
        """
        entries = self._load_all()
        found = False
        for entry in entries:
            eid = entry.get("id", "")
            if eid == entry_id or eid.startswith(entry_id):
                entry["status"] = "resolved"
                entry["resolution"] = resolution
                entry["resolved_at"] = datetime.now(timezone.utc).isoformat()
                found = True
                break
        if found:
            self._rewrite(entries)
        return found

    def query(
        self,
        phase: str | None = None,
        error_type: str | None = None,
        topic: str | None = None,
        course: str | None = None,
        status: str | None = None,
        last: int | None = None,
    ) -> list[dict[str, Any]]:
        """Consulta entradas con filtros opcionales. Retorna lista ordenada por timestamp."""
        entries = self._load_all()
        if phase and phase != "all":
            entries = [e for e in entries if e.get("phase") == phase]
        if error_type and error_type != "all":
            entries = [e for e in entries if e.get("error_type") == error_type]
        if topic:
            entries = [e for e in entries if e.get("topic") == topic]
        if course:
            entries = [e for e in entries if e.get("course") == course]
        if status and status != "all":
            entries = [e for e in entries if e.get("status") == status]
        if last:
            entries = entries[-last:]
        return entries

    def get_prevention_rules(
        self,
        phase: str | None = None,
        error_type: str | None = None,
    ) -> list[dict[str, Any]]:
        """
        Retorna reglas de prevención únicas combinando:
        1. Reglas aprendidas del historial real (mayor prioridad)
        2. Reglas predeterminadas del sistema

        Ordenadas por (phase, error_type).
        """
        # Extraer reglas del historial (la más reciente por clave gana)
        seen: dict[tuple[str, str], str] = {}
        for e in self._load_all():
            key = (e.get("phase", ""), e.get("error_type", ""))
            if e.get("prevention_rule"):
                seen[key] = e["prevention_rule"]

        # Completar con defaults no cubiertos por historial
        for (ph, et), rule in _DEFAULT_RULES.items():
            key = (ph, et)
            if key not in seen:
                seen[key] = rule

        rules = [
            {"phase": ph, "error_type": et, "rule": rule}
            for (ph, et), rule in seen.items()
        ]

        # Aplicar filtros
        if phase and phase != "all":
            rules = [r for r in rules if r["phase"] == phase]
        if error_type and error_type != "all":
            rules = [r for r in rules if r["error_type"] == error_type]

        return sorted(rules, key=lambda r: (r["phase"], r["error_type"]))

    def stats(self) -> dict[str, Any]:
        """Estadísticas globales del registro."""
        entries = self._load_all()
        if not entries:
            return {
                "total": 0, "open": 0, "resolved": 0,
                "resolution_rate": "0%",
                "by_phase": {}, "by_type": {},
                "top_error_types": [],
            }

        by_phase: dict[str, int] = {}
        by_type: dict[str, int] = {}
        open_count = 0
        resolved_count = 0

        for e in entries:
            ph = e.get("phase", "?")
            et = e.get("error_type", "?")
            by_phase[ph] = by_phase.get(ph, 0) + 1
            by_type[et] = by_type.get(et, 0) + 1
            if e.get("status") == "resolved":
                resolved_count += 1
            else:
                open_count += 1

        top = sorted(by_type.items(), key=lambda x: -x[1])[:3]
        rate = f"{resolved_count / len(entries) * 100:.0f}%" if entries else "0%"

        return {
            "total": len(entries),
            "open": open_count,
            "resolved": resolved_count,
            "resolution_rate": rate,
            "by_phase": by_phase,
            "by_type": by_type,
            "top_error_types": [{"type": t, "count": c} for t, c in top],
        }


# ──────────────────────────────────────────────────────────────────────────────
# Helpers de presentación para CLI
# ──────────────────────────────────────────────────────────────────────────────

def _wrap(text: str, width: int = 78, indent: str = "    ") -> str:
    """Envuelve texto a ancho máximo con indentación."""
    words = text.split()
    lines: list[str] = []
    line = indent
    for word in words:
        if len(line) + len(word) + 1 > width:
            lines.append(line.rstrip())
            line = indent + word
        else:
            line += (" " if line.strip() else "") + word
    if line.strip():
        lines.append(line.rstrip())
    return "\n".join(lines)


def _print_rules(rules: list[dict[str, Any]]) -> None:
    if not rules:
        print("  (sin reglas de prevención registradas)")
        return
    for r in rules:
        print(f"\n  ▶  [{r['phase']} / {r['error_type']}]")
        print(_wrap(r["rule"]))


def _print_entries(entries: list[dict[str, Any]]) -> None:
    if not entries:
        print("  (sin entradas)")
        return
    for e in entries:
        status_icon = "✅" if e.get("status") == "resolved" else "⚠️ "
        ts = (e.get("timestamp") or "?")[:19].replace("T", " ")
        eid = (e.get("id") or "?")[:8]
        print(f"\n  {status_icon} [{ts}] ID: {eid}...")
        print(f"     Fase: {e.get('phase')}  │  Tipo: {e.get('error_type')}  │  "
              f"Recurrencia: {e.get('recurrence_count', 1)}")
        if e.get("topic"):
            print(f"     Tema: {e.get('topic')}  │  Curso: {e.get('course', '?')}")
        desc = (e.get("description") or "")[:120]
        print(f"     Error: {desc}")
        if e.get("root_cause"):
            print(f"     Causa: {(e.get('root_cause') or '')[:120]}")
        if e.get("prevention_rule"):
            print(f"     Prevención: {(e.get('prevention_rule') or '')[:120]}")
        if e.get("resolution"):
            print(f"     Resolución: {(e.get('resolution') or '')[:120]}")


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="error_registry.py — Registro persistente de errores de publicación EDU",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # ── rules ─────────────────────────────────────────────────────────────────
    p_rules = sub.add_parser("rules", help="Mostrar reglas de prevención (consultar ANTES de generar)")
    p_rules.add_argument("--phase", choices=VALID_PHASES + ["all"], default="all",
                         help="Filtrar por fase (default: all)")
    p_rules.add_argument("--type", dest="error_type", choices=VALID_TYPES + ["all"], default="all",
                         help="Filtrar por tipo de error (default: all)")

    # ── query ─────────────────────────────────────────────────────────────────
    p_query = sub.add_parser("query", help="Consultar errores registrados")
    p_query.add_argument("--phase", choices=VALID_PHASES + ["all"], default=None)
    p_query.add_argument("--type", dest="error_type", choices=VALID_TYPES + ["all"], default=None)
    p_query.add_argument("--topic", default=None)
    p_query.add_argument("--course", default=None)
    p_query.add_argument("--status", choices=["open", "resolved", "all"], default="all")
    p_query.add_argument("--last", type=int, default=None, help="Últimas N entradas")

    # ── record ────────────────────────────────────────────────────────────────
    p_record = sub.add_parser("record", help="Registrar un error (OBLIGATORIO tras cada fallo)")
    p_record.add_argument("--phase", required=True, choices=VALID_PHASES,
                          help="Fase donde ocurrió el error")
    p_record.add_argument("--type", dest="error_type", required=True, choices=VALID_TYPES,
                          help="Tipo de error")
    p_record.add_argument("--desc", required=True,
                          help="Descripción del error (qué pasó exactamente)")
    p_record.add_argument("--topic", default="", help="Nombre del tema (ej: tema-01)")
    p_record.add_argument("--course", default="", help="ID del curso (ej: leng-2026)")
    p_record.add_argument("--cause", default="",
                          help="Causa raíz identificada (por qué ocurrió)")
    p_record.add_argument("--prevention", default="",
                          help="Regla de prevención personalizada (sobrescribe el default)")
    p_record.add_argument("--context", default="{}",
                          help='JSON con contexto adicional (ej: \'{"slide_index": 3}\')')

    # ── resolve ───────────────────────────────────────────────────────────────
    p_resolve = sub.add_parser("resolve", help="Marcar un error como resuelto")
    p_resolve.add_argument("--id", required=True,
                           help="UUID completo o prefijo (≥8 chars) de la entrada")
    p_resolve.add_argument("--resolution", required=True,
                           help="Descripción de cómo se resolvió el error")

    # ── stats ─────────────────────────────────────────────────────────────────
    sub.add_parser("stats", help="Estadísticas globales del registro")

    args = parser.parse_args()
    registry = ErrorRegistry()
    sep = "═" * 72

    if args.command == "rules":
        phase_f = None if args.phase == "all" else args.phase
        type_f = None if args.error_type == "all" else args.error_type
        rules = registry.get_prevention_rules(phase=phase_f, error_type=type_f)
        print(f"\n{sep}")
        print(f"  REGLAS DE PREVENCIÓN — Consulta obligatoria antes de generar")
        print(f"  Registro: {registry.path}")
        print(f"  Total reglas: {len(rules)}")
        print(f"{sep}")
        _print_rules(rules)
        print()

    elif args.command == "query":
        phase_f = None if (args.phase or "all") == "all" else args.phase
        type_f = None if (args.error_type or "all") == "all" else args.error_type
        status_f = None if args.status == "all" else args.status
        entries = registry.query(
            phase=phase_f,
            error_type=type_f,
            topic=args.topic,
            course=args.course,
            status=status_f,
            last=args.last,
        )
        print(f"\n{sep}")
        print(f"  ERRORES REGISTRADOS  ({len(entries)} entradas)")
        print(f"{sep}")
        _print_entries(entries)
        print()

    elif args.command == "record":
        try:
            ctx = json.loads(args.context)
        except json.JSONDecodeError:
            ctx = {"raw_context": args.context}
        entry_id = registry.record(
            phase=args.phase,
            error_type=args.error_type,
            description=args.desc,
            topic=args.topic,
            course=args.course,
            root_cause=args.cause,
            prevention_rule=args.prevention,
            context=ctx,
        )
        print(f"✅ Error registrado: {entry_id}")
        print(f"   Archivo: {registry.path}")
        print(f"   Recurrencia acumulada para este tipo en este tema.")
        print(f"\n   Próximo paso: resolver con:")
        print(f"   python scripts/error_registry.py resolve --id {entry_id[:8]} --resolution \"...\"")

    elif args.command == "resolve":
        ok = registry.resolve(args.id, args.resolution)
        if ok:
            print(f"✅ Entrada {args.id[:8]}... marcada como resuelta.")
            print(f"   La resolución queda registrada para referencia futura.")
        else:
            print(f"❌ No se encontró entrada con ID: {args.id}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "stats":
        s = registry.stats()
        print(f"\n{sep}")
        print(f"  ESTADÍSTICAS — Registro de errores EDU")
        print(f"  Archivo: {registry.path}")
        print(f"{sep}")
        print(f"  Total: {s['total']}  │  Abiertos: {s['open']}  │  "
              f"Resueltos: {s['resolved']}  │  Tasa resolución: {s.get('resolution_rate', '0%')}")
        if s.get("by_phase"):
            print(f"\n  Por fase:")
            for ph, count in sorted(s["by_phase"].items()):
                print(f"    {ph}: {count}")
        if s.get("top_error_types"):
            print(f"\n  Top tipos de error:")
            for item in s["top_error_types"]:
                print(f"    {item['type']}: {item['count']}")
        print()


if __name__ == "__main__":
    main()
