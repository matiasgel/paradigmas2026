#!/usr/bin/env python3
"""
student_analytics.py — Motor de analytics + importadores CSV (S5.1)

Importa notas de GitHub Classroom y Moodle, detecta alumnos en riesgo
con alertas semáforo, y genera dashboards Markdown.

Tablas nuevas en memory.db (CREATE IF NOT EXISTS):
- students, grades, attendance, risk_alerts

Uso:
    python scripts/student_analytics.py import-grades --csv grades.csv --course leng-2026
    python scripts/student_analytics.py dashboard --course leng-2026

Exit codes:
    0 — OK
    1 — error de entrada
"""
from __future__ import annotations

import argparse
import csv
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

from pipeline_common import find_project_root, load_yaml


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS students (
    student_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    course_id TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    course_id TEXT NOT NULL,
    topic_id TEXT,
    tp_type TEXT,
    score REAL NOT NULL,
    max_score REAL NOT NULL DEFAULT 100,
    submitted_at TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    course_id TEXT NOT NULL,
    date TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'present',
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE IF NOT EXISTS risk_alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    course_id TEXT NOT NULL,
    alert_date TEXT NOT NULL,
    risk_level TEXT NOT NULL,
    reason TEXT,
    suggested_action TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
"""


def init_db(db_path: Path) -> sqlite3.Connection:
    """Inicializa las tablas de analytics en memory.db."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.executescript(SCHEMA_SQL)
    conn.commit()
    return conn


def import_grades_csv(conn: sqlite3.Connection, csv_path: Path, course_id: str) -> int:
    """Importa notas desde CSV (formato: student_id,name,email,topic_id,tp_type,score,max_score)."""
    if not csv_path.exists():
        print(f"❌ Archivo CSV no encontrado: {csv_path}")
        return 0

    count = 0
    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            student_id = row.get("student_id", "").strip()
            if not student_id:
                continue

            # Upsert student
            conn.execute(
                "INSERT OR IGNORE INTO students (student_id, name, email, course_id) VALUES (?, ?, ?, ?)",
                (student_id, row.get("name", ""), row.get("email", ""), course_id),
            )

            score = float(row.get("score", 0))
            max_score = float(row.get("max_score", 100))
            conn.execute(
                "INSERT INTO grades (student_id, course_id, topic_id, tp_type, score, max_score, submitted_at) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (student_id, course_id, row.get("topic_id", ""),
                 row.get("tp_type", ""), score, max_score,
                 row.get("submitted_at", datetime.now().isoformat())),
            )
            count += 1

    conn.commit()
    return count


def compute_risk_alerts(conn: sqlite3.Connection, course_id: str) -> list[dict]:
    """Calcula alertas de riesgo basadas en notas y asistencia."""
    alerts = []
    now = datetime.now().isoformat()

    # Alumnos con promedio < 40%
    rows = conn.execute("""
        SELECT student_id, AVG(score * 100.0 / max_score) as avg_pct
        FROM grades WHERE course_id = ?
        GROUP BY student_id
        HAVING avg_pct < 40
    """, (course_id,)).fetchall()

    for student_id, avg_pct in rows:
        risk = "alto" if avg_pct < 25 else "medio"
        reason = f"Promedio {avg_pct:.0f}% — por debajo del umbral mínimo"
        action = "Contactar al alumno para tutoría personalizada" if risk == "alto" else "Monitorear próximas entregas"
        alerts.append({
            "student_id": student_id, "risk_level": risk,
            "reason": reason, "action": action,
        })
        conn.execute(
            "INSERT INTO risk_alerts (student_id, course_id, alert_date, risk_level, reason, suggested_action) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (student_id, course_id, now, risk, reason, action),
        )

    # Alumnos con >2 TPs sin entregar (score = 0)
    rows = conn.execute("""
        SELECT student_id, COUNT(*) as zeros
        FROM grades WHERE course_id = ? AND score = 0
        GROUP BY student_id HAVING zeros > 2
    """, (course_id,)).fetchall()

    for student_id, zeros in rows:
        reason = f"{zeros} entregas con score 0 — posible abandono"
        alerts.append({
            "student_id": student_id, "risk_level": "alto",
            "reason": reason, "action": "Verificar situación del alumno",
        })
        conn.execute(
            "INSERT INTO risk_alerts (student_id, course_id, alert_date, risk_level, reason, suggested_action) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (student_id, course_id, now, "alto", reason, "Verificar situación del alumno"),
        )

    conn.commit()
    return alerts


def generate_dashboard(conn: sqlite3.Connection, course_id: str, output_path: Path) -> str:
    """Genera dashboard Markdown con estadísticas y alertas."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Estadísticas generales
    total_students = conn.execute(
        "SELECT COUNT(DISTINCT student_id) FROM students WHERE course_id = ?",
        (course_id,),
    ).fetchone()[0]

    total_grades = conn.execute(
        "SELECT COUNT(*) FROM grades WHERE course_id = ?", (course_id,),
    ).fetchone()[0]

    avg_score = conn.execute(
        "SELECT AVG(score * 100.0 / max_score) FROM grades WHERE course_id = ?",
        (course_id,),
    ).fetchone()[0] or 0

    # Distribución por rango
    ranges = conn.execute("""
        SELECT
            CASE
                WHEN score * 100.0 / max_score >= 80 THEN '🟢 80-100%'
                WHEN score * 100.0 / max_score >= 60 THEN '🟡 60-79%'
                WHEN score * 100.0 / max_score >= 40 THEN '🟠 40-59%'
                ELSE '🔴 0-39%'
            END as rango,
            COUNT(*) as n
        FROM grades WHERE course_id = ?
        GROUP BY rango ORDER BY rango DESC
    """, (course_id,)).fetchall()

    # Alertas activas
    alerts = conn.execute("""
        SELECT s.name, r.risk_level, r.reason, r.suggested_action
        FROM risk_alerts r JOIN students s ON r.student_id = s.student_id
        WHERE r.course_id = ? ORDER BY r.alert_date DESC LIMIT 20
    """, (course_id,)).fetchall()

    lines = [
        f"# Dashboard Analytics — {course_id}",
        f"\n> Generado: {now}\n",
        "## Resumen\n",
        f"| Métrica | Valor |",
        f"|---------|-------|",
        f"| Alumnos registrados | {total_students} |",
        f"| Total de evaluaciones | {total_grades} |",
        f"| Promedio general | {avg_score:.1f}% |",
        "",
        "## Distribución de notas\n",
        "| Rango | Cantidad |",
        "|-------|----------|",
    ]
    for rango, n in ranges:
        lines.append(f"| {rango} | {n} |")

    if alerts:
        lines.extend([
            "",
            "## ⚠️ Alertas de riesgo\n",
            "| Alumno | Nivel | Razón | Acción sugerida |",
            "|--------|-------|-------|-----------------|",
        ])
        for name, level, reason, action in alerts:
            emoji = "🔴" if level == "alto" else "🟡"
            lines.append(f"| {name} | {emoji} {level} | {reason} | {action} |")

    report = "\n".join(lines) + "\n"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    return str(output_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Student Analytics Engine")
    sub = parser.add_subparsers(dest="command")

    imp = sub.add_parser("import-grades", help="Importar notas desde CSV")
    imp.add_argument("--csv", required=True, help="Ruta al archivo CSV")
    imp.add_argument("--course", required=True, help="ID del curso")

    dash = sub.add_parser("dashboard", help="Generar dashboard")
    dash.add_argument("--course", required=True, help="ID del curso")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 1

    root = find_project_root(Path(__file__).parent)
    config = load_yaml(root / "_edu" / "config.yaml")
    db_path = root / "_edu-memory" / "memory.db"
    conn = init_db(db_path)

    try:
        if args.command == "import-grades":
            csv_path = Path(args.csv)
            count = import_grades_csv(conn, csv_path, args.course)
            if count == 0:
                print("ℹ️  No se importaron registros.")
                return 0
            print(f"✅ {count} registros importados para {args.course}")
            alerts = compute_risk_alerts(conn, args.course)
            if alerts:
                print(f"⚠️  {len(alerts)} alertas de riesgo generadas")
            return 0

        elif args.command == "dashboard":
            output = root / "salida" / "cursadas" / args.course / "analytics" / f"dashboard-{datetime.now().strftime('%Y%m%d')}.md"
            compute_risk_alerts(conn, args.course)
            path = generate_dashboard(conn, args.course, output)
            print(f"✅ Dashboard generado: {path}")
            return 0
    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
