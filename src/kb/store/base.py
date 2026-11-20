"""VectorStore contract — keeps Chroma swappable if chunk count explodes."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

from ..models import Chunk, SearchHit


@runtime_checkable
class VectorStore(Protocol):
    def upsert(self, chunks: list[Chunk]) -> None: ...

    def delete_by_doc(self, doc_id: str) -> None: ...

    def search(
        self, vector: list[float], k: int, where: dict[str, Any] | None = None
    ) -> list[SearchHit]: ...
