from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("slides_pipeline.py")
SPEC = importlib.util.spec_from_file_location("slides_pipeline_contract", MODULE_PATH)
slides_pipeline = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(slides_pipeline)


class SlidesContractTests(unittest.TestCase):
    def test_generate_plan_exposes_schema_metadata(self) -> None:
        fixture = Path(__file__).parents[1] / "informe" / "filminas.md"
        config = {
            "palette": {},
            "typography": {},
            "gemini_image_strategy": {"max_per_presentation": 0},
        }

        plan = slides_pipeline.generate_plan(fixture, config, "template-id")

        self.assertEqual(plan["meta"]["schema_version"], "filminas/v1")
        self.assertEqual(plan["meta"]["schema_path"], "_edu/templates/filminas-schema.yaml")

    def test_image_prompt_excludes_slide_text_and_hex_palette(self) -> None:
        slide = {
            "type": "concepto-abstracto",
            "title": "Continuidad con Tema 01",
            "subtitle": "",
            "body_blocks": [
                {
                    "type": "list",
                    "ordered": False,
                    "items": [
                        {"content": "TypeScript compila a JavaScript", "level": 0},
                        {"content": "JavaScript corre sobre una máquina de ejecución real", "level": 0},
                    ],
                }
            ],
            "directives": {},
            "asset_hints": [],
        }
        config = {
            "palette": {
                "primary": "#8B0000",
                "secondary": "#FFFFFF",
                "text": "#1A1A1A",
            }
        }

        prompt = slides_pipeline._image_prompt(slide, config)

        self.assertIn("Continuidad con Tema 01", prompt)
        self.assertNotIn("Conceptos clave", prompt)
        self.assertNotIn("TypeScript compila a JavaScript", prompt)
        self.assertNotIn("#8B0000", prompt)
        self.assertIn("No incluir texto legible dentro de la imagen", prompt)

    def test_generate_plan_accepts_legacy_and_current_image_budget_keys(self) -> None:
        fixture = Path(__file__).parents[1] / "informe" / "filminas.md"
        config = {
            "palette": {},
            "typography": {},
            "gemini_image_strategy": {"max_images_per_presentation": 0},
        }

        plan = slides_pipeline.generate_plan(fixture, config, "template-id")
        images = [
            slide for slide in plan["slides"]
            if slide["background_image"]["strategy"] == "gemini"
            or slide["content_image"]["strategy"] == "gemini"
        ]

        self.assertEqual(images, [])

    def test_parse_filminas_applies_directive_overrides(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            topic = Path(tmp) / "tema-demo"
            scripts = Path(tmp) / "scripts"
            edu = Path(tmp) / "_edu"
            topic.mkdir(parents=True)
            scripts.mkdir(parents=True)
            edu.mkdir(parents=True)

            filminas = topic / "filminas.md"
            filminas.write_text(
                """### [F-01] Arquitectura\n\n@tipo: diagrama\n@layout: diagrama\n@imagen: content\n@asset: kind=diagram position=right-half prompt=\"flujo\"\n\n# Idea central\n\n- Punto A\n- Punto B\n""",
                encoding="utf-8",
            )

            slides = slides_pipeline.parse_filminas(filminas)

            self.assertEqual(slides[0]["type"], "diagrama")
            self.assertEqual(slides[0]["directives"]["layout"], "diagrama")
            self.assertEqual(slides[0]["directives"]["image"], "content")
            self.assertEqual(slides[0]["asset_hints"][0]["kind"], "diagram")

    def test_invalid_directive_fails_fast(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            topic = Path(tmp) / "tema-demo"
            scripts = Path(tmp) / "scripts"
            edu = Path(tmp) / "_edu"
            topic.mkdir(parents=True)
            scripts.mkdir(parents=True)
            edu.mkdir(parents=True)

            filminas = topic / "filminas.md"
            filminas.write_text(
                """### [F-01] Titulo\n\n@tipo: inventado\n\n# Subtitulo\n\nTexto.\n""",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "@tipo inválido"):
                slides_pipeline.parse_filminas(filminas)


if __name__ == "__main__":
    unittest.main()