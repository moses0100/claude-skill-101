"""EmbeddingProvider contract.

Two implementations will live here: fastembed_local (default) and openai_api
(only after explicit approval — see CLAUDE.md rule 5).
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class EmbeddingProvider(Protocol):
    @property
    def dimension(self) -> int: ...

    def embed(self, texts: list[str]) -> list[list[float]]: ...
