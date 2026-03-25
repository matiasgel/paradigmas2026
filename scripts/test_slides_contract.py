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
        """Backwards compat: generate_plan() (deprecated) aún expone metadata de schema."""
        fixture = Path(__file__).parents[3] / "informe" / "filminas.md"
        config = {
            "palette": {},
            "typography": {},
            "gemini_image_strategy": {"max_per_presentation": 0},
        }

        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            plan = slides_pipeline.generate_plan(fixture, config, "template-id")

        # El schema_version depende de qué filminas-schema.yaml encuentra find_project_root.
        # Lo importante es que el campo exista y el path sea el esperado.
        self.assertIn("schema_version", plan["meta"])
        self.assertEqual(plan["meta"]["schema_path"], "_edu/templates/filminas-schema.yaml")

    def test_parse_filminas_returns_pending_without_directive(self) -> None:
        """v2 (Sprint 2): slides sin @tipo: explícito deben tener type='pending', no inferido."""
        with tempfile.TemporaryDirectory() as tmp:
            topic = Path(tmp) / "tema-demo"
            scripts = Path(tmp) / "scripts"   # necesario para find_project_root()
            edu = Path(tmp) / "_edu" / "templates"
            topic.mkdir(parents=True)
            scripts.mkdir(parents=True)
            edu.mkdir(parents=True)

            (edu / "filminas-schema.yaml").write_text(
                (Path(__file__).parents[1] / "_edu" / "templates" / "filminas-schema.yaml").read_text(encoding="utf-8"),
                encoding="utf-8",
            )

            filminas = topic / "filminas.md"
            # Slide sin @tipo: — antes se inferia como concepto-abstracto, ahora debe ser pending
            filminas.write_text(
                "### [F-00] Introduccion\n\n# Bienvenida\n\n- Punto A\n- Punto B\n",
                encoding="utf-8",
            )

            slides = slides_pipeline.parse_filminas(filminas)

            # v2: sin @tipo: → type debe ser 'pending', nunca inferido del contenido
            self.assertEqual(slides[0]["type"], "pending")

    def test_parse_filminas_applies_directive_overrides(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            topic = Path(tmp) / "tema-demo"
            scripts = Path(tmp) / "scripts"
            edu = Path(tmp) / "_edu" / "templates"
            topic.mkdir(parents=True)
            scripts.mkdir(parents=True)
            edu.mkdir(parents=True)

            (edu / "filminas-schema.yaml").write_text(
                (Path(__file__).parents[1] / "_edu" / "templates" / "filminas-schema.yaml").read_text(encoding="utf-8"),
                encoding="utf-8",
            )

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
            edu = Path(tmp) / "_edu" / "templates"
            topic.mkdir(parents=True)
            scripts.mkdir(parents=True)
            edu.mkdir(parents=True)

            (edu / "filminas-schema.yaml").write_text(
                (Path(__file__).parents[1] / "_edu" / "templates" / "filminas-schema.yaml").read_text(encoding="utf-8"),
                encoding="utf-8",
            )

            filminas = topic / "filminas.md"
            filminas.write_text(
                """### [F-01] Titulo\n\n@tipo: inventado\n\n# Subtitulo\n\nTexto.\n""",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "@tipo inválido"):
                slides_pipeline.parse_filminas(filminas)


if __name__ == "__main__":
    unittest.main()