"""Phase 0 exit criterion: config.yaml loads and the privacy guard works."""

from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import yaml

from kb.config import ConfigurationError, load_settings

ROOT = Path(__file__).resolve().parents[1]


class TestLoadSettings(unittest.TestCase):
    def test_default_config_loads(self) -> None:
        settings = load_settings(ROOT / "config.yaml")

        self.assertEqual(settings.embedding.profile, "local")
        self.assertFalse(settings.embedding.allow_external)
        self.assertEqual(settings.embedding.local.model, "intfloat/multilingual-e5-small")
        self.assertEqual(settings.extraction.ocr.lang, "tha+eng")
        self.assertEqual(settings.chunking.max_tokens, 1000)
        self.assertEqual(settings.chunking.overlap, 100)
        self.assertEqual(settings.vectorstore.collection, "internal_kb")
        self.assertEqual(settings.embedding.batch_size, 64)

    def test_fast_profile_blocked_without_approval(self) -> None:
        with TemporaryDirectory() as tmp:
            raw = yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8"))
            raw["embedding"]["profile"] = "fast"
            config_path = Path(tmp) / "config.yaml"
            config_path.write_text(yaml.safe_dump(raw, allow_unicode=True), encoding="utf-8")

            with self.assertRaises(ConfigurationError):
                load_settings(config_path)

    def test_fast_profile_allowed_after_approval(self) -> None:
        with TemporaryDirectory() as tmp:
            raw = yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8"))
            raw["embedding"]["profile"] = "fast"
            raw["embedding"]["allow_external"] = True
            config_path = Path(tmp) / "config.yaml"
            config_path.write_text(yaml.safe_dump(raw, allow_unicode=True), encoding="utf-8")

            settings = load_settings(config_path)
            self.assertEqual(settings.embedding.profile, "fast")

    def test_unknown_key_is_rejected(self) -> None:
        with TemporaryDirectory() as tmp:
            raw = yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8"))
            raw["typo_key"] = 1
            config_path = Path(tmp) / "config.yaml"
            config_path.write_text(yaml.safe_dump(raw, allow_unicode=True), encoding="utf-8")

            with self.assertRaises(ConfigurationError):
                load_settings(config_path)

    def test_missing_file_raises(self) -> None:
        with self.assertRaises(ConfigurationError):
            load_settings(ROOT / "does-not-exist.yaml")


if __name__ == "__main__":
    unittest.main()
