from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pipeline_common


class PipelineCommonRuntimeTests(unittest.TestCase):
    def test_resolve_git_ignored_path_isolates_outputs_by_branch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            git_dir = root / ".git"
            git_dir.mkdir()
            (git_dir / "HEAD").write_text(
                "ref: refs/heads/feature/slides-prod\n",
                encoding="utf-8",
            )

            topic = root / "salida" / "cursadas" / "2026" / "temas" / "08-demo"
            topic.mkdir(parents=True)

            runtime_path = pipeline_common.resolve_git_ignored_path(
                topic,
                Path("slides") / "assets" / "F-01.png",
            )

            self.assertEqual(
                runtime_path,
                git_dir
                / "edu-runtime"
                / "feature_slides-prod"
                / "salida"
                / "cursadas"
                / "2026"
                / "temas"
                / "08-demo"
                / "slides"
                / "assets"
                / "F-01.png",
            )

    def test_ensure_git_ignored_path_copies_legacy_output_once(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            git_dir = root / ".git"
            git_dir.mkdir()
            (git_dir / "HEAD").write_text("ref: refs/heads/main\n", encoding="utf-8")

            topic = root / "salida" / "cursadas" / "2026" / "temas" / "08-demo"
            legacy_path = topic / "slides" / "slides-url.txt"
            legacy_path.parent.mkdir(parents=True)
            legacy_path.write_text("https://example.test/slides/demo", encoding="utf-8")

            runtime_path = pipeline_common.ensure_git_ignored_path(
                topic,
                Path("slides") / "slides-url.txt",
            )

            self.assertTrue(runtime_path.exists())
            self.assertEqual(
                runtime_path.read_text(encoding="utf-8"),
                "https://example.test/slides/demo",
            )
            self.assertTrue(legacy_path.exists())
            self.assertNotEqual(runtime_path, legacy_path)


if __name__ == "__main__":
    unittest.main()
