"""Shared data structures used across pipeline layers.

Layer rule: these are plain dataclasses so no layer needs to import another
layer's implementation. Chroma metadata only accepts scalar values.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar

Scalar = str | int | float | bool
Metadata = dict[str, Scalar]


class FileStatus(str, Enum):
    """Lifecycle of a source file in the manifest."""

    PENDING = "pending"
    EXTRACTED = "extracted"
    CHUNKED = "chunked"
    EMBEDDED = "embedded"
    FAILED = "failed"
    DELETED = "deleted"


@dataclass(slots=True)
class RawPage:
    """One PDF page as produced by the extraction layer."""

    number: int
    text: str
    is_scanned: bool = False
    tables: list[str] = field(default_factory=list)


@dataclass(slots=True)
class RawSection:
    """A DOCX section identified by its heading path."""

    heading_path: str
    blocks: list[str] = field(default_factory=list)


@dataclass(slots=True)
class RawDocument:
    """Layer-neutral result of extracting a source file."""

    doc_id: str
    source: str
    file_type: str
    pages: list[RawPage] = field(default_factory=list)
    sections: list[RawSection] = field(default_factory=list)
    tables: list[str] = field(default_factory=list)
    metadata: Metadata = field(default_factory=dict)


@dataclass(slots=True)
class Chunk:
    """A retrievable unit. ``chunk_id`` is deterministic for idempotent upsert."""

    doc_id: str
    text: str
    metadata: Metadata
    chunk_index: int

    REQUIRED_METADATA: ClassVar[tuple[str, ...]] = (
        "source",
        "file_type",
        "content_hash",
        "ingested_at",
    )

    def __post_init__(self) -> None:
        missing = [key for key in self.REQUIRED_METADATA if key not in self.metadata]
        if missing:
            raise ValueError(f"Chunk metadata missing required keys: {missing}")
        if self.chunk_index < 0:
            raise ValueError("chunk_index must be >= 0")

    @property
    def chunk_id(self) -> str:
        """Format: ``{content_hash[:16]}_{chunk_index:04d}`` (see spec section 4.3)."""
        content_hash = str(self.metadata["content_hash"])
        return f"{content_hash[:16]}_{self.chunk_index:04d}"


@dataclass(slots=True)
class FileRecord:
    """A row of the SQLite manifest."""

    path_hash: str
    relative_path: str
    size: int
    mtime: float
    content_hash: str | None
    status: FileStatus
    chunk_count: int = 0
    last_ingested_at: str | None = None
    error_message: str | None = None


@dataclass(slots=True)
class SearchHit:
    """Retrieval result, ready to be formatted as a citation."""

    text: str
    metadata: Metadata
    score: float

    @property
    def citation(self) -> str:
        """Format: ``source • หน้า X • section • แถว A-B`` (spec section 5.7)."""
        parts = [str(self.metadata.get("source", "unknown"))]
        if "page" in self.metadata:
            parts.append(f"หน้า {self.metadata['page']}")
        if "section" in self.metadata:
            parts.append(str(self.metadata["section"]))
        if "row_range" in self.metadata:
            parts.append(f"แถว {self.metadata['row_range']}")
        return " • ".join(parts)
