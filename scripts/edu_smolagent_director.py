#!/usr/bin/env python3
"""
edu_smolagent_director.py — Director Agent con smolagents (S12.2)
=================================================================
Orquestador inteligente que usa LLMs (Qwen/Llama vía HF Inference API)
para decidir qué hacer cuando pasos fallan o hay feedback inesperado.

Uso:
    python scripts/edu_smolagent_director.py --topic 05-sorting --course leng-2026

Requisitos:
    - pip install smolagents
    - HF_TOKEN en variables de entorno (gratuito vía HuggingFace Inference API)

Si no hay HF_TOKEN, usa edu_director.py (modo minimal) como fallback.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

_this = Path(__file__).resolve()
_scripts = _this.parent
_root = _scripts.parent
if str(_scripts) not in sys.path:
    sys.path.insert(0, str(_scripts))

from pipeline_common import find_project_root, load_config


# ═══════════════════════════════════════════════════════════════════════
# TOOL WRAPPERS (for smolagents)
# ═══════════════════════════════════════════════════════════════════════

def _make_tool_functions() -> dict:
    """Crea wrappers de herramientas EDU como funciones simples."""

    def search_knowledge_base(query: str) -> str:
        """Busca en la base de conocimiento ChromaDB del curso."""
        result = subprocess.run(
            [sys.executable, str(_scripts / "knowledge_base.py"), "search", query],
            capture_output=True, text=True, timeout=30, cwd=str(_root),
        )
        return result.stdout[:1000] if result.returncode == 0 else f"Error: {result.stderr[:500]}"

    def validate_plan(topic: str, course: str) -> str:
        """Valida el plan de filminas de un tema."""
        result = subprocess.run(
            [sys.executable, str(_scripts / "validate_plan.py"), "--topic", topic, "--course", course],
            capture_output=True, text=True, timeout=60, cwd=str(_root),
        )
        return result.stdout[:1000] if result.returncode == 0 else f"Error: {result.stderr[:500]}"

    def run_slides_pipeline(topic: str, course: str) -> str:
        """Ejecuta el pipeline de generación de slides."""
        result = subprocess.run(
            [sys.executable, str(_scripts / "slides_pipeline.py"), "--topic", topic, "--course", course],
            capture_output=True, text=True, timeout=600, cwd=str(_root),
        )
        return result.stdout[:1000] if result.returncode == 0 else f"Error: {result.stderr[:500]}"

    def check_facts(topic: str, course: str) -> str:
        """Verifica hechos del contenido generado con NLI."""
        script = _scripts / "fact_verifier.py"
        if not script.exists():
            return "Script fact_verifier.py no disponible"
        result = subprocess.run(
            [sys.executable, str(script), "--topic", topic, "--course", course],
            capture_output=True, text=True, timeout=120, cwd=str(_root),
        )
        return result.stdout[:1000] if result.returncode == 0 else f"Error: {result.stderr[:500]}"

    def check_bloom_coverage(topic: str, course: str) -> str:
        """Clasifica preguntas por nivel de Bloom."""
        script = _scripts / "bloom_classifier.py"
        if not script.exists():
            return "Script bloom_classifier.py no disponible"
        result = subprocess.run(
            [sys.executable, str(script), "--topic", topic, "--course", course],
            capture_output=True, text=True, timeout=120, cwd=str(_root),
        )
        return result.stdout[:1000] if result.returncode == 0 else f"Error: {result.stderr[:500]}"

    return {
        "search_knowledge_base": search_knowledge_base,
        "validate_plan": validate_plan,
        "run_slides_pipeline": run_slides_pipeline,
        "check_facts": check_facts,
        "check_bloom_coverage": check_bloom_coverage,
    }


# ═══════════════════════════════════════════════════════════════════════
# SMOLAGENTS DIRECTOR
# ═══════════════════════════════════════════════════════════════════════

def run_smolagent_director(topic: str, course: str, config: dict) -> int:
    """Ejecuta el director inteligente con smolagents."""
    try:
        from smolagents import CodeAgent, HfApiModel, tool
    except ImportError:
        print("❌ smolagents no instalado. Ejecute: pip install smolagents")
        print("   Cayendo a modo minimal...")
        return _fallback_minimal(topic, course)

    hf_token = os.environ.get("HF_TOKEN")
    if not hf_token:
        print("⚠️  HF_TOKEN no configurado. Usando modo minimal como fallback.")
        return _fallback_minimal(topic, course)

    model_name = config.get("orchestrator_model", "Qwen/Qwen2.5-72B-Instruct")

    # Crear herramientas como @tool decorados
    tools_dict = _make_tool_functions()

    @tool
    def search_kb(query: str) -> str:
        """Busca en la base de conocimiento ChromaDB."""
        return tools_dict["search_knowledge_base"](query)

    @tool
    def validate(topic: str, course: str) -> str:
        """Valida el plan de filminas."""
        return tools_dict["validate_plan"](topic, course)

    @tool
    def generate_slides(topic: str, course: str) -> str:
        """Genera las slides del tema."""
        return tools_dict["run_slides_pipeline"](topic, course)

    @tool
    def verify_facts(topic: str, course: str) -> str:
        """Verifica hechos con NLI."""
        return tools_dict["check_facts"](topic, course)

    model = HfApiModel(model_id=model_name, token=hf_token)

    agent = CodeAgent(
        tools=[search_kb, validate, generate_slides, verify_facts],
        model=model,
        max_steps=10,
    )

    prompt = f"""Eres un director de producción académica. Tu objetivo es producir
el material completo del tema '{topic}' del curso '{course}'.

Pasos a seguir:
1. Validar el plan con validate()
2. Generar las slides con generate_slides()
3. Verificar hechos con verify_facts()
4. Si algo falla, buscar en la KB con search_kb() para encontrar soluciones.

Ejecuta cada paso y reporta el resultado."""

    try:
        result = agent.run(prompt)
        print(f"\n✅ Director Agent completó: {result}")
        return 0
    except Exception as e:
        print(f"❌ Error en smolagent: {e}")
        return 1


def _fallback_minimal(topic: str, course: str) -> int:
    """Fallback al director minimal (edu_director.py)."""
    cmd = [
        sys.executable,
        str(_scripts / "edu_director.py"),
        "--topic", topic,
        "--course", course,
    ]
    return subprocess.run(cmd, cwd=str(_root)).returncode


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def main() -> int:
    parser = argparse.ArgumentParser(description="EDU smolagents Director (S12.2)")
    parser.add_argument("--topic", required=True, help="ID del tema")
    parser.add_argument("--course", required=True, help="ID del curso")
    args = parser.parse_args()

    project_root = find_project_root(Path.cwd())
    config = load_config(project_root)

    if not config.get("orchestrator_enabled", False):
        print("ℹ️  orchestrator_enabled no está habilitado en config. Saliendo.")
        return 0

    mode = config.get("orchestrator_mode", "minimal")
    if mode == "minimal":
        print("ℹ️  Modo minimal — ejecutando edu_director.py")
        return _fallback_minimal(args.topic, args.course)

    return run_smolagent_director(args.topic, args.course, config)


if __name__ == "__main__":
    raise SystemExit(main())
