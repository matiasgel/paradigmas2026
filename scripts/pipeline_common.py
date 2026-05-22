"""
pipeline_common.py — Módulo compartido del pipeline EDU (v3)
============================================================
Centraliza utilidades de I/O, localización de archivos, y tipos monádicos
para composición funcional con manejo de errores.

Paradigma funcional:
  - Result[T]: mónada para encadenar operaciones que pueden fallar
  - pipe(): composición secuencial de funciones
  - collect_results(): acumulación monádica de errores

Todas las funciones de I/O y localización del proyecto están aquí
como fuente única de verdad — los scripts importan desde este módulo.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Generic, TypeVar

import yaml

T = TypeVar("T")
U = TypeVar("U")


# ═══════════════════════════════════════════════════════════════════════
# RESULT MONAD
# ═══════════════════════════════════════════════════════════════════════


@dataclass(frozen=True)
class Result(Generic[T]):
    """Mónada Result para composición funcional con manejo de errores."""

    value: T | None
    errors: tuple[str, ...]

    @staticmethod
    def ok(value: T) -> Result[T]:
        return Result(value=value, errors=())

    @staticmethod
    def fail(*errors: str) -> Result[Any]:
        return Result(value=None, errors=errors)

    @property
    def is_ok(self) -> bool:
        return len(self.errors) == 0

    def bind(self, f: Callable[[T], Result[U]]) -> Result[U]:
        if not self.is_ok:
            return Result(value=None, errors=self.errors)
        return f(self.value)  # type: ignore[arg-type]

    def map(self, f: Callable[[T], U]) -> Result[U]:
        if not self.is_ok:
            return Result(value=None, errors=self.errors)
        return Result.ok(f(self.value))  # type: ignore[arg-type]

    def unwrap(self) -> T:
        if not self.is_ok:
            raise ValueError(
                "Result.unwrap() en Err:\n- " + "\n- ".join(self.errors)
            )
        return self.value  # type: ignore[return-value]

    def unwrap_or(self, default: T) -> T:
        return self.value if self.is_ok else default  # type: ignore[return-value]

    def __or__(self, f: Callable[[T], Result[U]]) -> Result[U]:
        return self.bind(f)


def collect_results(results: list[Result[T]]) -> Result[list[T]]:
    all_errors: list[str] = []
    values: list[T] = []
    for r in results:
        if r.is_ok:
            values.append(r.unwrap())
        else:
            all_errors.extend(r.errors)
    if all_errors:
        return Result.fail(*all_errors)
    return Result.ok(values)


def pipe(value: T, *fns: Callable) -> Any:
    result = value
    for fn in fns:
        result = fn(result)
    return result


# ═══════════════════════════════════════════════════════════════════════
# FILE I/O
# ═══════════════════════════════════════════════════════════════════════


def find_project_root(start: Path) -> Path:
    cur = start.resolve()
    while True:
        if (cur / ".git").exists() or (cur / "module.yaml").exists():
            return cur
        if (cur / "_edu").exists() and (cur / "scripts").exists():
            return cur
        if cur == cur.parent:
            break
        cur = cur.parent
    raise FileNotFoundError(f"No se encontró la raíz del proyecto desde {start}.")


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_registry(project_root: Path) -> dict:
    registry_path = project_root / "_edu" / "schemas" / "schema-registry.json"
    if registry_path.exists():
        return load_json(registry_path)
    return {}


def load_config(project_root: Path) -> dict:
    config_path = project_root / "_edu" / "slides-config.yaml"
    if config_path.exists():
        return load_yaml(config_path)
    return {}


def find_plan(topic_folder: Path) -> Result[Path]:
    """Busca el plan JSON v3 del tema. Retorna Result con el path."""
    slides_dir = topic_folder / "slides"
    topic_id = topic_folder.name

    json_path = slides_dir / f"plan-filminas-{topic_id}.json"
    if json_path.exists():
        return Result.ok(json_path)

    json_candidates = (
        sorted(slides_dir.glob("plan-filminas-*.json"))
        if slides_dir.exists()
        else []
    )
    if json_candidates:
        return Result.ok(json_candidates[0])

    return Result.fail(
        f"No se encontró plan-filminas-*.json en {slides_dir}. "
        "Ejecutar primero: python scripts/parse_filminas.py <topic_folder>"
    )
