"""Contract every extractor must satisfy (Phase 1 implementations go here)."""

from __future__ import annotations

from pathlib import Path
from typing import Protocol, runtime_checkable

from ..models import RawDocument


class ExtractionError(Exception):
    """Raised when a source file cannot be read or parsed."""


@runtime_checkable
class Extractor(Protocol):
    def extract(self, path: Path) -> RawDocument: ...
