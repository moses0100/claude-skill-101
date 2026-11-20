"""FR-01 / FR-02 — folder scan and delta detection.

Speed rule: stat (size + mtime) first, sha256 only for files that actually changed.
"""

from __future__ import annotations

import hashlib
import logging
from dataclasses import dataclass
from pathlib import Path

from .manifest import Manifest
from .models import FileRecord

logger = logging.getLogger(__name__)
_HASH_CHUNK_SIZE = 1024 * 1024


@dataclass(slots=True, frozen=True)
class FileCandidate:
    """A discovered source file with its cheap signature."""

    relative_path: str
    path: Path
    size: int
    mtime: float


def scan_source(root: Path, include: list[str]) -> list[FileCandidate]:
    """FR-01 — recursively list files matching the configured glob patterns."""
    root = Path(root)
    if not root.is_dir():
        raise FileNotFoundError(f"source root ไม่มีอยู่: {root}")
    candidates = [
        FileCandidate(
            relative_path=path.relative_to(root).as_posix(),
            path=path,
            size=stat.st_size,
            mtime=stat.st_mtime,
        )
        for path in root.rglob("*")
        if path.is_file()
        and any(path.match(pattern) for pattern in include)
        for stat in (path.stat(),)
    ]
    return sorted(candidates, key=lambda candidate: candidate.relative_path)


def sha256_file(path: Path) -> str:
    """Stream a file through sha256 without loading it into memory."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(_HASH_CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def detect_changes(
    manifest: Manifest, candidates: list[FileCandidate]
) -> tuple[list[FileRecord], list[str]]:
    """FR-02 — return files that need processing and paths that disappeared."""
    to_process: list[FileRecord] = []
    present: set[str] = set()
    for candidate in candidates:
        present.add(candidate.relative_path)
        if not manifest.needs_hash(candidate.relative_path, candidate.size, candidate.mtime):
            continue
        content_hash = sha256_file(candidate.path)
        record = manifest.register(
            candidate.relative_path, candidate.size, candidate.mtime, content_hash
        )
        if record is not None:
            logger.info("queued %s (%s bytes)", record.relative_path, record.size)
            to_process.append(record)

    missing = manifest.mark_missing(present)
    for relative_path in missing:
        logger.info("source disappeared: %s (mark as deleted)", relative_path)
    return to_process, missing
