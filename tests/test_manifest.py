"""Manifest schema, delta detection and checkpoint behaviour."""

from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from kb.manifest import Manifest, path_hash
from kb.models import FileStatus


class TestManifest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = TemporaryDirectory()
        self.db_path = Path(self.tmp.name) / "manifest.db"
        self.manifest = Manifest(self.db_path)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_initialize_creates_table(self) -> None:
        self.assertEqual(self.manifest.summary(), {})

    def test_creates_missing_parent_directory(self) -> None:
        nested = Path(self.tmp.name) / "new" / "deep" / "manifest.db"
        Manifest(nested)
        self.assertTrue(nested.is_file())

    def test_needs_hash_for_new_changed_unchanged_and_failed(self) -> None:
        self.assertTrue(self.manifest.needs_hash("a.pdf", 10, 100.0))

        self.manifest.register("a.pdf", 10, 100.0, "hash1")
        self.assertFalse(self.manifest.needs_hash("a.pdf", 10, 100.0))
        self.assertTrue(self.manifest.needs_hash("a.pdf", 11, 100.0))
        self.assertTrue(self.manifest.needs_hash("a.pdf", 10, 101.0))

        self.manifest.mark("a.pdf", FileStatus.FAILED, error_message="boom")
        self.assertTrue(self.manifest.needs_hash("a.pdf", 10, 100.0))

    def test_register_is_idempotent_on_same_content_hash(self) -> None:
        first = self.manifest.register("a.pdf", 10, 100.0, "hash1")
        self.assertIsNotNone(first)
        self.assertEqual(first.relative_path, "a.pdf")
        self.assertEqual(first.path_hash, path_hash("a.pdf"))
        self.assertIs(first.status, FileStatus.PENDING)

        second = self.manifest.register("a.pdf", 12, 101.0, "hash1")
        self.assertIsNone(second)

    def test_register_after_failed_retries_even_with_same_hash(self) -> None:
        self.manifest.register("a.pdf", 10, 100.0, "hash1")
        self.manifest.mark("a.pdf", FileStatus.FAILED)
        retry = self.manifest.register("a.pdf", 10, 100.0, "hash1")
        self.assertIsNotNone(retry)
        self.assertIsNone(retry.error_message)

    def test_mark_updates_checkpoint_fields_and_summary(self) -> None:
        self.manifest.register("a.pdf", 10, 100.0, "hash1")
        self.manifest.mark("a.pdf", FileStatus.EMBEDDED, chunk_count=7)

        record = self.manifest.get("a.pdf")
        self.assertIsNotNone(record)
        self.assertIs(record.status, FileStatus.EMBEDDED)
        self.assertEqual(record.chunk_count, 7)
        self.assertIsNotNone(record.last_ingested_at)
        self.assertEqual(self.manifest.summary(), {"embedded": 1})
        self.assertEqual([r.relative_path for r in self.manifest.records(FileStatus.EMBEDDED)], ["a.pdf"])

    def test_mark_missing_marks_deleted_and_returns_paths(self) -> None:
        self.manifest.register("a.pdf", 10, 100.0, "h1")
        self.manifest.register("b.docx", 20, 200.0, "h2")

        missing = self.manifest.mark_missing({"a.pdf"})
        self.assertEqual(missing, ["b.docx"])
        self.assertIs(self.manifest.get("b.docx").status, FileStatus.DELETED)
        self.assertIs(self.manifest.get("a.pdf").status, FileStatus.PENDING)

        self.assertEqual(self.manifest.mark_missing({"a.pdf"}), [])


if __name__ == "__main__":
    unittest.main()
