#!/usr/bin/env python3
"""
spaced_repetition.py — Motor de Spaced Repetition FSRS v4 para EDU (S2.1)

Implementa el algoritmo FSRS v4 (Free Spaced Repetition Scheduler, Ye 2023-2024)
con modelo DSR (Difficulty, Stability, Retrievability) para generar calendarios
de repaso distribuidos y combatir la curva del olvido.

Solo dependencias stdlib: math, datetime, json, sqlite3.

Uso:
    python scripts/spaced_repetition.py --course leng-2026 generate
    python scripts/spaced_repetition.py --course leng-2026 --topic 01-intro record --score 0.7
    python scripts/spaced_repetition.py --course leng-2026 status

Exit codes:
    0 — operación exitosa
    1 — error de entrada
"""
from __future__ import annotations

import argparse
import json
import math
import sqlite3
import sys
from datetime import datetime, timedelta
from pathlib import Path

from pipeline_common import find_project_root, load_yaml


# ═══════════════════════════════════════════════════════════════════════
# FSRS v4 — FREE SPACED REPETITION SCHEDULER
# ═══════════════════════════════════════════════════════════════════════
# Basado en: Ye (2023-2024) "A Stochastic Shortest Path Algorithm for
# Optimizing Spaced Repetition Scheduling" — Open Spaced Repetition

# Parámetros por defecto (FSRS-4.5 defaults)
FSRS_PARAMS = {
    "w0": 0.4,      # initial stability after first review
    "w1": 0.6,      # initial stability modifier
    "w2": 2.4,      # initial difficulty
    "w3": 5.8,      # difficulty modifier
    "w4": 4.93,     # stability increase base
    "w5": 0.94,     # stability increase modifier for difficulty
    "w6": 0.86,     # stability increase modifier for stability
    "w7": 0.01,     # stability increase modifier for retrievability
    "w8": 1.49,     # stability decrease base (for failed reviews)
    "w9": 0.14,     # stability decrease modifier
    "w10": 0.94,    # stability decrease modifier for difficulty
    "w11": 2.18,    # stability decrease modifier for stability
    "w12": 0.05,    # stability decrease modifier for retrievability
    "w13": 0.34,    # initial difficulty modifier
    "w14": 1.26,    # difficulty mean reversion
    "w15": 0.29,    # difficulty mean reversion rate
    "w16": 2.61,    # fuzz factor
    "desired_retention": 0.9,  # target retrievability
}


class FSRSCard:
    """Representa el estado FSRS de un concepto/topic."""

    def __init__(self, difficulty: float = 0.0, stability: float = 0.0,
                 last_review: str | None = None, review_count: int = 0):
        self.difficulty = difficulty or FSRS_PARAMS["w2"]
        self.stability = stability or FSRS_PARAMS["w0"]
        self.last_review = last_review
        self.review_count = review_count

    def retrievability(self, elapsed_days: float) -> float:
        """Calcula la probabilidad de recuperación (curva del olvido)."""
        if self.stability <= 0 or elapsed_days <= 0:
            return 1.0
        return math.exp(math.log(0.9) * elapsed_days / self.stability)

    def next_interval(self) -> float:
        """Calcula el intervalo óptimo para mantener desired_retention."""
        r = FSRS_PARAMS["desired_retention"]
        if self.stability <= 0:
            return 1.0
        return self.stability * math.log(r) / math.log(0.9)

    def update_after_review(self, score: float) -> None:
        """Actualiza dificultad y estabilidad tras un repaso.

        score: 0.0-1.0 donde 1.0 = recordó perfectamente
        """
        w = FSRS_PARAMS
        self.review_count += 1

        # Actualizar dificultad (mean reversion)
        new_d = w["w2"] + (score - 0.5) * w["w14"]
        self.difficulty = self.difficulty * (1 - w["w15"]) + new_d * w["w15"]
        self.difficulty = max(1.0, min(10.0, self.difficulty))

        # Actualizar estabilidad
        if score >= 0.6:  # aprobado
            self.stability = self.stability * (
                1 + math.exp(w["w4"]) *
                (11 - self.difficulty) * self.stability ** (-w["w6"]) *
                (math.exp((1 - score) * w["w7"]) - 1)
            )
        else:  # reprobado
            self.stability = w["w8"] * (
                self.difficulty ** (-w["w10"]) *
                ((self.stability + 1) ** w["w11"] - 1) *
                math.exp((1 - score) * w["w12"])
            )
            self.stability = max(0.1, self.stability)

        self.last_review = datetime.now().strftime("%Y-%m-%d")


# ═══════════════════════════════════════════════════════════════════════
# BASE DE DATOS (SQLite — CREATE IF NOT EXISTS)
# ═══════════════════════════════════════════════════════════════════════


def init_db(db_path: Path) -> sqlite3.Connection:
    """Inicializa la tabla spaced_reviews si no existe."""
    conn = sqlite3.connect(str(db_path))
    conn.execute("""
        CREATE TABLE IF NOT EXISTS spaced_reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id TEXT NOT NULL,
            topic_id TEXT NOT NULL,
            review_date TEXT NOT NULL,
            review_number INTEGER NOT NULL,
            score REAL NOT NULL,
            difficulty REAL NOT NULL,
            stability REAL NOT NULL,
            next_review TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_spaced_course_topic
        ON spaced_reviews (course_id, topic_id)
    """)
    conn.commit()
    return conn


def get_card_state(conn: sqlite3.Connection, course_id: str,
                   topic_id: str) -> FSRSCard:
    """Recupera el último estado FSRS para un topic, o crea uno nuevo."""
    row = conn.execute(
        """SELECT difficulty, stability, review_date, review_number
           FROM spaced_reviews
           WHERE course_id = ? AND topic_id = ?
           ORDER BY id DESC LIMIT 1""",
        (course_id, topic_id),
    ).fetchone()

    if row:
        return FSRSCard(
            difficulty=row[0], stability=row[1],
            last_review=row[2], review_count=row[3],
        )
    return FSRSCard()


def save_review(conn: sqlite3.Connection, course_id: str, topic_id: str,
                card: FSRSCard, score: float) -> None:
    """Guarda un registro de repaso."""
    next_interval = max(1, round(card.next_interval()))
    next_date = (datetime.now() + timedelta(days=next_interval)).strftime("%Y-%m-%d")

    conn.execute(
        """INSERT INTO spaced_reviews
           (course_id, topic_id, review_date, review_number, score,
            difficulty, stability, next_review)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            course_id, topic_id,
            datetime.now().strftime("%Y-%m-%d"),
            card.review_count, score,
            round(card.difficulty, 4), round(card.stability, 4),
            next_date,
        ),
    )
    conn.commit()


# ═══════════════════════════════════════════════════════════════════════
# GENERACIÓN DE CALENDARIO
# ═══════════════════════════════════════════════════════════════════════


def discover_topics(project_root: Path, course_id: str) -> list[str]:
    """Descubre los temas del curso desde la estructura de carpetas."""
    parts = course_id.split("-", 1)
    course_prefix = parts[0] if parts else course_id
    course_year = parts[1] if len(parts) > 1 else "2026"
    topics_dir = project_root / "salida" / "cursadas" / course_id / "temas"
    if not topics_dir.exists():
        return []
    return sorted(
        d.name for d in topics_dir.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    )


def generate_calendar(conn: sqlite3.Connection, project_root: Path,
                      course_id: str) -> str:
    """Genera calendario Markdown de repasos distribuidos."""
    topics = discover_topics(project_root, course_id)
    now = datetime.now()
    lines = [
        f"# Calendario de Repasos — {course_id}",
        f"**Generado:** {now.strftime('%Y-%m-%d %H:%M')}",
        f"**Algoritmo:** FSRS v4 (Ye 2023-2024)",
        f"**Retención objetivo:** {FSRS_PARAMS['desired_retention'] * 100:.0f}%",
        "",
    ]

    if not topics:
        lines.append("ℹ️ No se encontraron temas. Crear temas primero con `/edu-design-topic`.")
        return "\n".join(lines) + "\n"

    # Próximos repasos pendientes
    rows = conn.execute(
        """SELECT topic_id, MAX(next_review) as next_r, 
                  MAX(review_number) as rev_n, 
                  AVG(score) as avg_score
           FROM spaced_reviews
           WHERE course_id = ?
           GROUP BY topic_id
           ORDER BY next_r""",
        (course_id,),
    ).fetchall()

    reviewed_topics = {r[0] for r in rows}
    upcoming = [r for r in rows if r[1] >= now.strftime("%Y-%m-%d")]
    overdue = [r for r in rows if r[1] < now.strftime("%Y-%m-%d")]
    never_reviewed = [t for t in topics if t not in reviewed_topics]

    if overdue:
        lines.extend([
            "## ⚠️ Repasos Atrasados",
            "",
            "| Tema | Vencido | Repasos | Score Promedio |",
            "|------|---------|---------|---------------|",
        ])
        for r in overdue:
            lines.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]:.0%} |")
        lines.append("")

    if upcoming:
        lines.extend([
            "## 📅 Próximos Repasos",
            "",
            "| Tema | Fecha | Repaso # | Score Promedio |",
            "|------|-------|----------|---------------|",
        ])
        for r in upcoming:
            lines.append(f"| {r[0]} | {r[1]} | {r[2] + 1} | {r[3]:.0%} |")
        lines.append("")

    if never_reviewed:
        lines.extend([
            "## 🆕 Temas Sin Repaso",
            "",
            "| Tema | Primer repaso sugerido |",
            "|------|-----------------------|",
        ])
        for t in never_reviewed:
            # Sugerir 3 días después de la clase (heurística)
            suggested = (now + timedelta(days=3)).strftime("%Y-%m-%d")
            lines.append(f"| {t} | {suggested} |")
        lines.append("")

    # Estadísticas
    total_reviews = conn.execute(
        "SELECT COUNT(*) FROM spaced_reviews WHERE course_id = ?",
        (course_id,),
    ).fetchone()[0]

    lines.extend([
        "## Estadísticas",
        "",
        f"- **Temas totales:** {len(topics)}",
        f"- **Con repasos registrados:** {len(reviewed_topics)}",
        f"- **Total de sesiones de repaso:** {total_reviews}",
    ])

    return "\n".join(lines) + "\n"


# ═══════════════════════════════════════════════════════════════════════
# GENERACIÓN DE SLIDES DE REPASO
# ═══════════════════════════════════════════════════════════════════════


def generate_review_slides(conn: sqlite3.Connection, course_id: str,
                           topic_id: str, topic_folder: Path) -> str | None:
    """Genera template de slides de repaso para un tema (2-3 slides socráticas)."""
    card = get_card_state(conn, course_id, topic_id)
    if card.review_count == 0:
        return None

    r = card.retrievability(
        (datetime.now() - datetime.strptime(card.last_review, "%Y-%m-%d")).days
        if card.last_review else 0
    )

    content = f"""# Slides de Repaso — {topic_id}
**Repaso #{card.review_count + 1}** | Retrievability estimada: {r:.0%}

---

## Filmina de Repaso 1 — Recuperación Activa (Socrática)

**Tipo:** pregunta-socrática  
**Título:** ¿Qué recuerdan de {topic_id.replace('-', ' ')}?  
**Body:** Tómense 60 segundos para escribir los 3 conceptos principales del tema.

> **Nota para el docente:** Esta filmina activa la recuperación activa (testing effect).
> No dar la respuesta inmediatamente — esperar a que los alumnos generen sus propias respuestas.

---

## Filmina de Repaso 2 — Conexión con Nuevo Material

**Tipo:** concepto-abstracto  
**Título:** Conexión: {topic_id.replace('-', ' ')} → Tema actual  
**Body:** [Completar con la conexión concreta entre este tema y el material nuevo]

> **Nota para el docente:** Interleaving — mezclar temas viejos con nuevos
> mejora la retención a largo plazo (Roediger & Butler, 2011).

---

## Filmina de Repaso 3 — Aplicación Rápida

**Tipo:** demo  
**Título:** Mini-ejercicio relámpago (2 min)  
**Body:** [Completar con un ejercicio corto que aplique conceptos del tema]

> **Nota para el docente:** Desirable difficulty — el ejercicio debe ser
> ligeramente difícil para maximizar la retención (Bjork & Bjork, 2011).
"""
    return content


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Motor de Spaced Repetition FSRS v4 para EDU"
    )
    parser.add_argument("--course", required=True, help="ID del curso (ej: leng-2026)")
    parser.add_argument("--topic", help="ID del tema (ej: 01-intro)")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # generate
    gen_parser = subparsers.add_parser("generate", help="Generar calendario de repasos")

    # record
    rec_parser = subparsers.add_parser("record", help="Registrar resultado de repaso")
    rec_parser.add_argument("--score", type=float, required=True,
                            help="Score 0.0-1.0 (1.0 = recordó todo)")

    # status
    status_parser = subparsers.add_parser("status", help="Ver estado de repasos")

    args = parser.parse_args()

    project_root = find_project_root(Path(__file__).parent)

    # Determinar path a memory.db
    edu_config_path = project_root / "_edu" / "config.yaml"
    edu_config = load_yaml(edu_config_path) if edu_config_path.exists() else {}
    memory_folder = project_root / "_edu-memory"
    db_path = memory_folder / "memory.db"
    memory_folder.mkdir(parents=True, exist_ok=True)

    conn = init_db(db_path)

    try:
        if args.command == "generate":
            calendar = generate_calendar(conn, project_root, args.course)
            output_dir = project_root / "salida" / "cursadas" / args.course
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / "repaso-calendario.md"
            output_path.write_text(calendar, encoding="utf-8")
            print(f"✅ Calendario generado: {output_path}")

            # Generar slides de repaso para cada tema con repasos
            topics = discover_topics(project_root, args.course)
            for topic_id in topics:
                topic_folder = (
                    project_root / "salida" / "cursadas" / args.course / "temas" / topic_id
                )
                review_md = generate_review_slides(conn, args.course, topic_id, topic_folder)
                if review_md:
                    review_path = topic_folder / "slides-repaso.md"
                    review_path.parent.mkdir(parents=True, exist_ok=True)
                    review_path.write_text(review_md, encoding="utf-8")
                    print(f"  📋 Slides de repaso: {review_path}")

        elif args.command == "record":
            if not args.topic:
                parser.error("--topic requerido para record")
            if not 0.0 <= args.score <= 1.0:
                parser.error("--score debe estar entre 0.0 y 1.0")

            card = get_card_state(conn, args.course, args.topic)
            card.update_after_review(args.score)
            save_review(conn, args.course, args.topic, card, args.score)

            interval = max(1, round(card.next_interval()))
            next_date = (datetime.now() + timedelta(days=interval)).strftime("%Y-%m-%d")
            print(f"✅ Repaso registrado: {args.topic} (score={args.score:.0%})")
            print(f"   Próximo repaso: {next_date} (en {interval} días)")
            print(f"   Estabilidad: {card.stability:.2f} | Dificultad: {card.difficulty:.2f}")

        elif args.command == "status":
            topics = discover_topics(project_root, args.course)
            if not topics:
                print(f"ℹ️ No se encontraron temas para {args.course}.")
                sys.exit(0)

            print(f"Estado de repasos — {args.course}")
            print(f"{'Tema':<30} {'Repasos':<10} {'Último':<12} {'Próximo':<12} {'Score':<8}")
            print("-" * 72)

            for topic_id in topics:
                card = get_card_state(conn, args.course, topic_id)
                if card.review_count > 0:
                    row = conn.execute(
                        """SELECT AVG(score), MAX(next_review)
                           FROM spaced_reviews
                           WHERE course_id = ? AND topic_id = ?""",
                        (args.course, topic_id),
                    ).fetchone()
                    avg_score = row[0] if row else 0
                    next_r = row[1] if row else "—"
                    print(
                        f"{topic_id:<30} {card.review_count:<10} "
                        f"{card.last_review or '—':<12} {next_r:<12} "
                        f"{avg_score:.0%}"
                    )
                else:
                    print(f"{topic_id:<30} {'0':<10} {'—':<12} {'—':<12} {'—':<8}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
