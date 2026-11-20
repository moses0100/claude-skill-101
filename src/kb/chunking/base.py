"""Contract every chunker must satisfy (Phase 1 implementations go here)."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from ..models import Chunk, RawDocument


@runtime_checkable
class Chunker(Protocol):
    def chunk(self, document: RawDocument) -> list[Chunk]: ...
