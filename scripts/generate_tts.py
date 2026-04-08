#!/usr/bin/env python3
"""
generate_tts.py — Generador de audio TTS desde minuta (S7.3)

Lee la minuta del tema y genera audio MP3 por filmina usando edge-tts
(gratuito, offline, Microsoft Neural Voices).

Uso:
    python scripts/generate_tts.py --topic 01-intro --course leng-2026
    python scripts/generate_tts.py --topic 01-intro --course leng-2026 --provider edge-tts

Exit codes:
    0 — audio generado (o feature desactivada)
    1 — error de entrada
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from pathlib import Path

from pipeline_common import find_project_root, load_yaml


def extract_slide_scripts(minuta_path: Path) -> list[dict]:
    """Extrae el guión por filmina desde minuta.md."""
    if not minuta_path.exists():
        return []

    text = minuta_path.read_text(encoding="utf-8")
    slides = []
    # Buscar secciones que corresponden a filminas
    pattern = re.compile(r"###\s*\[?F-?(\d+)\]?\s*(.*?)(?=\n###|\Z)", re.DOTALL)

    for match in pattern.finditer(text):
        num = int(match.group(1))
        title = match.group(2).strip().split("\n")[0]
        body = match.group(2).strip()

        # Extraer texto útil como guión (limpiar markdown)
        script_text = re.sub(r"[#*`\[\]|]", "", body)
        script_text = re.sub(r"\n{3,}", "\n\n", script_text).strip()

        if len(script_text) > 20:  # Solo si hay contenido sustancial
            slides.append({
                "number": num,
                "title": title,
                "script": script_text[:2000],  # Limitar a 2000 chars por slide
            })

    return slides


async def generate_edge_tts(text: str, output_path: Path, voice: str, rate: str) -> bool:
    """Genera audio con edge-tts."""
    try:
        import edge_tts  # type: ignore
    except ImportError:
        print("❌ edge-tts no instalado. Ejecutar: pip install edge-tts")
        return False

    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(str(output_path))
    return True


def generate_manifest(slides: list[dict], audio_dir: Path, provider: str) -> dict:
    """Genera el manifiesto de audio."""
    entries = []
    for slide in slides:
        mp3_path = audio_dir / f"filmina-{slide['number']:02d}.mp3"
        entries.append({
            "filmina_number": slide["number"],
            "title": slide["title"],
            "file": mp3_path.name,
            "text_length": len(slide["script"]),
            "provider": provider,
            "exists": mp3_path.exists(),
        })

    return {
        "generated_at": __import__("datetime").datetime.now().isoformat(),
        "provider": provider,
        "total_slides": len(entries),
        "entries": entries,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generador TTS por filmina")
    parser.add_argument("--topic", required=True, help="ID del tema")
    parser.add_argument("--course", required=True, help="ID del curso")
    parser.add_argument("--provider", default=None, help="Provider TTS (edge-tts por defecto)")
    args = parser.parse_args()

    root = find_project_root(Path(__file__).parent)
    config = load_yaml(root / "_edu" / "config.yaml")

    if not config.get("tts_enabled", False):
        print("ℹ️  TTS desactivado (tts_enabled: false en config.yaml)")
        return 0

    provider = args.provider or config.get("tts_provider", "edge-tts")
    voice = config.get("tts_voice", "es-AR-TomasNeural")
    rate = config.get("tts_rate", "+0%")

    topic_folder = root / "salida" / "cursadas" / args.course / "temas" / args.topic
    minuta_path = topic_folder / "minuta.md"

    if not minuta_path.exists():
        print(f"❌ minuta.md no encontrada: {minuta_path}")
        return 1

    slides = extract_slide_scripts(minuta_path)
    if not slides:
        print("ℹ️  No se encontraron guiones de filminas en minuta.md")
        return 0

    audio_dir = topic_folder / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    if provider == "edge-tts":
        print(f"🔊 Generando {len(slides)} audios con edge-tts (voz: {voice})...")
        for slide in slides:
            output = audio_dir / f"filmina-{slide['number']:02d}.mp3"
            success = asyncio.run(generate_edge_tts(slide["script"], output, voice, rate))
            if success:
                print(f"  ✅ filmina-{slide['number']:02d}.mp3")
            else:
                return 1
    elif provider in ("gcloud-tts", "elevenlabs"):
        confirm = input(f"⚠️  {provider} es un servicio pago. ¿Continuar? [s/N] ")
        if confirm.lower() != "s":
            print("Cancelado.")
            return 0
        print(f"❌ Provider {provider} requiere implementación adicional.")
        return 1
    else:
        print(f"❌ Provider no soportado: {provider}")
        return 1

    # Generar manifiesto
    manifest = generate_manifest(slides, audio_dir, provider)
    manifest_path = audio_dir / "audio-manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ Manifiesto: {manifest_path}")
    print(f"✅ {len(slides)} audios generados en {audio_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
