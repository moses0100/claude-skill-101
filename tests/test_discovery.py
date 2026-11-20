"""FR-01 / FR-02 — scan and delta detection against a temporary folder."""

from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from kb.discovery import detect_changes, scan_source, sha256_file
from kb.manifest import Manifest
from kb.models import FileStatus

INCLUDE = ["*.pdf", "*.docx", "*.csv"]


class TestDiscovery(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "sub").mkdir()
        (self.root / "a.pdf").write_bytes(b"a" * 10)
        (self.root / "sub" / "b.docx").write_bytes(b"b" * 20)
        (self.root / "ignore.txt").write_bytes(b"x" * 5)
        self.manifest = Manifest(Path(self.tmp.name) / "manifest.db")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_scan_source_filters_and_sorts(self) -> None:
        candidates = scan_source(self.root, INCLUDE)
        self.assertEqual([c.relative_path for c in candidates], ["a.pdf", "sub/b.docx"])
        self.assertEqual(candidates[0].size, 10)

    def test_scan_source_rejects_missing_root(self) -> None:
        with self.assertRaises(FileNotFoundError):
            scan_source(self.root / "nope", INCLUDE)

    def test_sha256_file_is_stable(self) -> None:
        digest = sha256_file(self.root / "a.pdf")
        self.assertEqual(len(digest), 64)
        self.assertEqual(digest, sha256_file(self.root / "a.pdf"))

    def test_detect_changes_then_noop_on_second_run(self) -> None:
        candidates = scan_source(self.root, INCLUDE)
        records, missing = detect_changes(self.manifest, candidates)
        self.assertEqual([r.relative_path for r in records], ["a.pdf", "sub/b.docx"])
        self.assertEqual(missing, [])

        again, missing_again = detect_changes(self.manifest, scan_source(self.root, INCLUDE))
        self.assertEqual(again, [])
        self.assertEqual(missing_again, [])

    def test_changed_file_is_queued_again(self) -> None:
        detect_changes(self.manifest, scan_source(self.root, INCLUDE))
        (self.root / "a.pdf").write_bytes(b"a" * 99)

        records, _ = detect_changes(self.manifest, scan_source(self.root, INCLUDE))
        self.assertEqual([r.relative_path for r in records], ["a.pdf"])

    def test_deleted_file_is_reported(self) -> None:
        detect_changes(self.manifest, scan_source(self.root, INCLUDE))
        (self.root / "a.pdf").unlink()

        records, missing = detect_changes(self.manifest, scan_source(self.root, INCLUDE))
        self.assertEqual(records, [])
        self.assertEqual(missing, ["a.pdf"])
        self.assertIs(self.manifest.get("a.pdf").status, FileStatus.DELETED)


if __name__ == "__main__":
    unittest.main()
