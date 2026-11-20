"""SQLite manifest — delta detection and checkpoints (spec sections 4.1 and 5.2)."""

from __future__ import annotations

import hashlib
import sqlite3
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path

from .models import FileRecord, FileStatus

SCHEMA = """
CREATE TABLE IF NOT EXISTS files (
    path_hash        TEXT PRIMARY KEY,
    relative_path    TEXT NOT NULL UNIQUE,
    size             INTEGER NOT NULL,
    mtime            REAL NOT NULL,
    content_hash     TEXT,
    status           TEXT NOT NULL,
    chunk_count      INTEGER NOT NULL DEFAULT 0,
    last_ingested_at TEXT,
    error_message    TEXT
);
CREATE INDEX IF NOT EXISTS idx_files_status ON files(status);
"""


def path_hash(relative_path: str) -> str:
    """Stable 16-char key derived from the relative path."""
    return hashlib.sha256(relative_path.encode("utf-8")).hexdigest()[:16]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _to_record(row: sqlite3.Row) -> FileRecord:
    return FileRecord(
        path_hash=row["path_hash"],
        relative_path=row["relative_path"],
        size=row["size"],
        mtime=row["mtime"],
        content_hash=row["content_hash"],
        status=FileStatus(row["status"]),
        chunk_count=row["chunk_count"],
        last_ingested_at=row["last_ingested_at"],
        error_message=row["error_message"],
    )


class Manifest:
    """Persistence layer for file signatures and processing state."""

    def __init__(self, db_path: Path | str) -> None:
        self.db_path = str(db_path)
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        self.initialize()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def initialize(self) -> None:
        """Create tables and indexes. Safe to call on every startup."""
        with closing(self._connect()) as conn, conn:
            conn.executescript(SCHEMA)

    # ------------------------------------------------------------------
    # Cheap signature check — must run BEFORE hashing (speed priority #1)
    # ------------------------------------------------------------------
    def needs_hash(self, relative_path: str, size: int, mtime: float) -> bool:
        """Return True for new/changed/failed files; False for unchanged ones."""
        with closing(self._connect()) as conn:
            row = conn.execute(
                "SELECT size, mtime, status FROM files WHERE path_hash = ?",
                (path_hash(relative_path),),
            ).fetchone()
        if row is None:
            return True
        if FileStatus(row["status"]) is FileStatus.FAILED:
            return True
        return row["size"] != int(size) or abs(float(row["mtime"]) - float(mtime)) > 1e-6

    def register(
        self, relative_path: str, size: int, mtime: float, content_hash: str
    ) -> FileRecord | None:
        """Record a (possibly changed) file.

        Returns a FileRecord when work is needed, or None when the content hash
        is identical to the stored one and the previous run succeeded.
        """
        key = path_hash(relative_path)
        with closing(self._connect()) as conn, conn:
            existing = conn.execute(
                "SELECT content_hash, status FROM files WHERE path_hash = ?", (key,)
            ).fetchone()
            if (
                existing is not None
                and existing["content_hash"] == content_hash
                and FileStatus(existing["status"]) is not FileStatus.FAILED
            ):
                return None

            conn.execute(
                """
                INSERT INTO files (
                    path_hash, relative_path, size, mtime, content_hash,
                    status, chunk_count, last_ingested_at, error_message
                ) VALUES (?, ?, ?, ?, ?, ?, 0, NULL, NULL)
                ON CONFLICT(path_hash) DO UPDATE SET
                    relative_path    = excluded.relative_path,
                    size             = excluded.size,
                    mtime            = excluded.mtime,
                    content_hash     = excluded.content_hash,
                    status           = excluded.status,
                    chunk_count      = 0,
                    last_ingested_at = NULL,
                    error_message    = NULL
                """,
                (
                    key,
                    relative_path,
                    int(size),
                    float(mtime),
                    content_hash,
                    FileStatus.PENDING.value,
                ),
            )
            row = conn.execute("SELECT * FROM files WHERE path_hash = ?", (key,)).fetchone()
            return _to_record(row)

    def mark(
        self,
        relative_path: str,
        status: FileStatus,
        *,
        content_hash: str | None = None,
        chunk_count: int | None = None,
        error_message: str | None = None,
    ) -> None:
        """Update a file's status and optional checkpoint fields."""
        fields = ["status = ?"]
        params: list[object] = [status.value]
        if content_hash is not None:
            fields.append("content_hash = ?")
            params.append(content_hash)
        if chunk_count is not None:
            fields.append("chunk_count = ?")
            params.append(int(chunk_count))
        if error_message is not None:
            fields.append("error_message = ?")
            params.append(error_message)
        else:
            fields.append("error_message = NULL")
        if status in (FileStatus.EMBEDDED, FileStatus.FAILED, FileStatus.DELETED):
            fields.append("last_ingested_at = ?")
            params.append(_now())
        params.append(path_hash(relative_path))
        with closing(self._connect()) as conn, conn:
            conn.execute(
                f"UPDATE files SET {', '.join(fields)} WHERE path_hash = ?",
                params,
            )

    def mark_missing(self, present_paths: set[str]) -> list[str]:
        """Mark records whose source file disappeared as DELETED; return their paths."""
        with closing(self._connect()) as conn, conn:
            rows = conn.execute(
                "SELECT path_hash, relative_path FROM files WHERE status != ?",
                (FileStatus.DELETED.value,),
            ).fetchall()
            missing = [row["relative_path"] for row in rows if row["relative_path"] not in present_paths]
            for row in rows:
                if row["relative_path"] not in present_paths:
                    conn.execute(
                        "UPDATE files SET status = ?, error_message = NULL, last_ingested_at = ? "
                        "WHERE path_hash = ?",
                        (FileStatus.DELETED.value, _now(), row["path_hash"]),
                    )
        return missing

    # ------------------------------------------------------------------
    # Read helpers (used by CLI / API status endpoints)
    # ------------------------------------------------------------------
    def get(self, relative_path: str) -> FileRecord | None:
        with closing(self._connect()) as conn:
            row = conn.execute(
                "SELECT * FROM files WHERE path_hash = ?", (path_hash(relative_path),)
            ).fetchone()
        return _to_record(row) if row is not None else None

    def records(self, status: FileStatus | None = None) -> list[FileRecord]:
        with closing(self._connect()) as conn:
            if status is None:
                rows = conn.execute("SELECT * FROM files ORDER BY relative_path").fetchall()
            else:
                rows = conn.execute(
                    "SELECT * FROM files WHERE status = ? ORDER BY relative_path",
                    (status.value,),
                ).fetchall()
        return [_to_record(row) for row in rows]

    def summary(self) -> dict[str, int]:
        """Counts per status, e.g. ``{'pending': 3, 'embedded': 10}``."""
        with closing(self._connect()) as conn:
            rows = conn.execute("SELECT status, COUNT(*) AS n FROM files GROUP BY status").fetchall()
        return {row["status"]: row["n"] for row in rows}
