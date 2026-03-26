#!/usr/bin/env python3
"""EDU Collective Memory — SQLite FTS5 backend.

Provides persistent, searchable memory across courses, years, topics and agents.
Used by EDU agents to store and retrieve errors, corrections, pedagogical
insights and retrospective notes.

Usage:
    python scripts/edu_memory.py add --course leng-2026 --category agent-error ...
    python scripts/edu_memory.py search "coherencia filminas"
    python scripts/edu_memory.py list --course leng-2026 --topic 03
    python scripts/edu_memory.py resolve 42
    python scripts/edu_memory.py export --course leng-2026
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import textwrap
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

VALID_CATEGORIES = {
    "agent-error",
    "agent-correction",
    "quality-finding",
    "pedagogy-insight",
    "student-feedback",
    "cross-topic",
    "retrospective",
    "tool-issue",
}

DB_RELATIVE = Path("_edu-memory") / "memory.db"

# ---------------------------------------------------------------------------
# DB helpers
# ---------------------------------------------------------------------------


def _find_project_root() -> Path:
    """Walk up from CWD until we find ``_edu/config.yaml``."""
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if (parent / "_edu" / "config.yaml").exists():
            return parent
    return current  # fallback


def _db_path(root: Optional[Path] = None) -> Path:
    root = root or _find_project_root()
    return root / DB_RELATIVE


def _connect(root: Optional[Path] = None) -> sqlite3.Connection:
    path = _db_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    _ensure_schema(conn)
    return conn


def _ensure_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(textwrap.dedent("""\
        CREATE TABLE IF NOT EXISTS memory_entries (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id   TEXT NOT NULL,
            course_year TEXT NOT NULL,
            topic_num   TEXT,
            category    TEXT NOT NULL,
            agent       TEXT,
            summary     TEXT NOT NULL,
            detail      TEXT,
            source_file TEXT,
            created_at  TEXT DEFAULT (datetime('now')),
            resolved    INTEGER DEFAULT 0
        );

        CREATE VIRTUAL TABLE IF NOT EXISTS memory_fts USING fts5(
            summary, detail, category, agent, course_id,
            content='memory_entries',
            content_rowid='id'
        );

        CREATE TRIGGER IF NOT EXISTS memory_ai AFTER INSERT ON memory_entries BEGIN
            INSERT INTO memory_fts(rowid, summary, detail, category, agent, course_id)
            VALUES (new.id, new.summary, new.detail, new.category, new.agent, new.course_id);
        END;

        CREATE TRIGGER IF NOT EXISTS memory_ad AFTER DELETE ON memory_entries BEGIN
            INSERT INTO memory_fts(memory_fts, rowid, summary, detail, category, agent, course_id)
            VALUES ('delete', old.id, old.summary, old.detail, old.category, old.agent, old.course_id);
        END;
    """))
    conn.commit()


# ---------------------------------------------------------------------------
# Public API  (importable by other scripts / agents)
# ---------------------------------------------------------------------------


def add_entry(
    *,
    course_id: str,
    category: str,
    summary: str,
    topic_num: Optional[str] = None,
    agent: Optional[str] = None,
    detail: Optional[str] = None,
    source_file: Optional[str] = None,
    root: Optional[Path] = None,
) -> int:
    """Insert a memory entry. Returns the new row id."""
    if category not in VALID_CATEGORIES:
        raise ValueError(f"Invalid category '{category}'. Valid: {sorted(VALID_CATEGORIES)}")
    year = course_id.rsplit("-", 1)[-1] if "-" in course_id else course_id
    conn = _connect(root)
    try:
        cur = conn.execute(
            """INSERT INTO memory_entries
               (course_id, course_year, topic_num, category, agent, summary, detail, source_file)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (course_id, year, topic_num, category, agent, summary, detail, source_file),
        )
        conn.commit()
        return cur.lastrowid  # type: ignore[return-value]
    finally:
        conn.close()


def search_memory(
    query: str,
    *,
    course_id: Optional[str] = None,
    category: Optional[str] = None,
    topic_num: Optional[str] = None,
    limit: int = 20,
    root: Optional[Path] = None,
) -> list[dict]:
    """Full-text search across memory entries."""
    conn = _connect(root)
    try:
        # Build FTS query with optional filters
        fts_query = query
        if course_id:
            fts_query += f' AND course_id:"{course_id}"'
        if category:
            fts_query += f' AND category:"{category}"'

        sql = """
            SELECT e.*, rank
            FROM memory_fts f
            JOIN memory_entries e ON e.id = f.rowid
            WHERE memory_fts MATCH ?
        """
        params: list = [fts_query]

        if topic_num:
            sql += " AND e.topic_num = ?"
            params.append(topic_num)

        sql += " ORDER BY rank LIMIT ?"
        params.append(limit)

        rows = conn.execute(sql, params).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def list_entries(
    *,
    course_id: Optional[str] = None,
    topic_num: Optional[str] = None,
    category: Optional[str] = None,
    unresolved_only: bool = False,
    limit: int = 50,
    root: Optional[Path] = None,
) -> list[dict]:
    """List entries with optional filters (no full-text, just column filters)."""
    conn = _connect(root)
    try:
        clauses: list[str] = []
        params: list = []
        if course_id:
            clauses.append("course_id = ?")
            params.append(course_id)
        if topic_num:
            clauses.append("topic_num = ?")
            params.append(topic_num)
        if category:
            clauses.append("category = ?")
            params.append(category)
        if unresolved_only:
            clauses.append("resolved = 0")

        where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
        sql = f"SELECT * FROM memory_entries {where} ORDER BY created_at DESC LIMIT ?"
        params.append(limit)

        rows = conn.execute(sql, params).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def resolve_entry(entry_id: int, *, root: Optional[Path] = None) -> bool:
    """Mark an entry as resolved."""
    conn = _connect(root)
    try:
        cur = conn.execute("UPDATE memory_entries SET resolved = 1 WHERE id = ?", (entry_id,))
        conn.commit()
        return cur.rowcount > 0
    finally:
        conn.close()


def export_memory(
    *,
    course_id: Optional[str] = None,
    fmt: str = "md",
    root: Optional[Path] = None,
) -> str:
    """Export memory entries as Markdown or JSON."""
    entries = list_entries(course_id=course_id, limit=9999, root=root)
    if fmt == "json":
        return json.dumps(entries, indent=2, ensure_ascii=False, default=str)

    # Markdown
    lines = [f"# Memoria Colectiva — {course_id or 'todas las clases'}\n"]
    by_cat: dict[str, list[dict]] = {}
    for e in entries:
        by_cat.setdefault(e["category"], []).append(e)
    for cat in sorted(by_cat):
        lines.append(f"\n## {cat}\n")
        for e in by_cat[cat]:
            status = "✅" if e["resolved"] else "⏳"
            topic = f" [T{e['topic_num']}]" if e.get("topic_num") else ""
            agent_s = f" ({e['agent']})" if e.get("agent") else ""
            lines.append(f"- {status}{topic}{agent_s} {e['summary']}")
            if e.get("detail"):
                for dl in e["detail"].split("\n"):
                    lines.append(f"  > {dl}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="EDU Collective Memory — SQLite FTS5",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # add
    add_p = sub.add_parser("add", help="Add a memory entry")
    add_p.add_argument("--course", required=True, help="Course ID (e.g. leng-2026)")
    add_p.add_argument("--category", required=True, choices=sorted(VALID_CATEGORIES))
    add_p.add_argument("--summary", required=True)
    add_p.add_argument("--topic", default=None, help="Topic number (e.g. 01)")
    add_p.add_argument("--agent", default=None)
    add_p.add_argument("--detail", default=None)
    add_p.add_argument("--source", default=None, help="Source file path")

    # search
    search_p = sub.add_parser("search", help="Full-text search")
    search_p.add_argument("query", help="Search query")
    search_p.add_argument("--course", default=None)
    search_p.add_argument("--category", default=None)
    search_p.add_argument("--topic", default=None)
    search_p.add_argument("--all", action="store_true", help="Search across all courses")
    search_p.add_argument("--limit", type=int, default=20)

    # list
    list_p = sub.add_parser("list", help="List entries with filters")
    list_p.add_argument("--course", default=None)
    list_p.add_argument("--topic", default=None)
    list_p.add_argument("--category", default=None)
    list_p.add_argument("--unresolved", action="store_true")
    list_p.add_argument("--limit", type=int, default=50)

    # resolve
    resolve_p = sub.add_parser("resolve", help="Mark entry as resolved")
    resolve_p.add_argument("id", type=int)

    # export
    export_p = sub.add_parser("export", help="Export entries")
    export_p.add_argument("--course", default=None)
    export_p.add_argument("--format", choices=["md", "json"], default="md")

    return parser


def _print_entries(entries: list[dict]) -> None:
    if not entries:
        print("No entries found.")
        return
    for e in entries:
        status = "✅" if e.get("resolved") else "⏳"
        topic = f"T{e['topic_num']}" if e.get("topic_num") else "—"
        agent_s = e.get("agent") or "—"
        print(f"  [{e['id']:>4}] {status} {e['course_id']:<12} {topic:<5} "
              f"{e['category']:<20} {agent_s:<18} {e['summary']}")


def main(argv: Optional[list[str]] = None) -> int:
    args = _build_parser().parse_args(argv)

    if args.command == "add":
        rid = add_entry(
            course_id=args.course,
            category=args.category,
            summary=args.summary,
            topic_num=args.topic,
            agent=args.agent,
            detail=args.detail,
            source_file=args.source,
        )
        print(f"✅ Entry #{rid} added.")
        return 0

    if args.command == "search":
        course = None if getattr(args, "all", False) else args.course
        results = search_memory(
            args.query,
            course_id=course,
            category=args.category,
            topic_num=args.topic,
            limit=args.limit,
        )
        print(f"Found {len(results)} result(s):")
        _print_entries(results)
        return 0

    if args.command == "list":
        results = list_entries(
            course_id=args.course,
            topic_num=args.topic,
            category=args.category,
            unresolved_only=args.unresolved,
            limit=args.limit,
        )
        print(f"{len(results)} entries:")
        _print_entries(results)
        return 0

    if args.command == "resolve":
        if resolve_entry(args.id):
            print(f"✅ Entry #{args.id} marked as resolved.")
            return 0
        print(f"❌ Entry #{args.id} not found.")
        return 1

    if args.command == "export":
        output = export_memory(course_id=args.course, fmt=args.format)
        print(output)
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
