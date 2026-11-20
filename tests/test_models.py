"""Data-model invariants that later phases rely on."""

from __future__ import annotations

import unittest

from kb.models import Chunk, SearchHit

BASE = {
    "source": "docs/course.pdf",
    "file_type": "pdf",
    "content_hash": "abcdef0123456789" + "0" * 48,
    "ingested_at": "2026-11-20T00:00:00+00:00",
}


class TestChunk(unittest.TestCase):
    def test_chunk_id_is_deterministic_and_formatted(self) -> None:
        chunk = Chunk(doc_id="doc-1", text="hello", metadata=dict(BASE), chunk_index=3)
        self.assertEqual(chunk.chunk_id, "abcdef0123456789_0003")
        self.assertEqual(chunk.chunk_id, Chunk("doc-1", "hello", dict(BASE), 3).chunk_id)

    def test_missing_required_metadata_is_rejected(self) -> None:
        broken = {key: value for key, value in BASE.items() if key != "ingested_at"}
        with self.assertRaises(ValueError):
            Chunk(doc_id="doc-1", text="hello", metadata=broken, chunk_index=0)

    def test_negative_chunk_index_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Chunk(doc_id="doc-1", text="hello", metadata=dict(BASE), chunk_index=-1)


class TestSearchHit(unittest.TestCase):
    def test_citation_for_pdf(self) -> None:
        hit = SearchHit(
            text="...",
            metadata={**BASE, "page": 12, "section": "3.2 > 3.2.1"},
            score=0.87,
        )
        self.assertEqual(
            hit.citation,
            "docs/course.pdf • หน้า 12 • 3.2 > 3.2.1",
        )

    def test_citation_for_csv_row_range(self) -> None:
        hit = SearchHit(text="...", metadata={**BASE, "row_range": "12-61"}, score=0.5)
        self.assertEqual(hit.citation, "docs/course.pdf • แถว 12-61")


if __name__ == "__main__":
    unittest.main()
