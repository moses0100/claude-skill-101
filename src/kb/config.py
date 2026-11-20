"""Single source of configuration (spec section 7).

No path, model name or chunk size is hardcoded elsewhere in the codebase.
Secrets are never read from config.yaml; providers read them from the environment.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator


class ConfigurationError(Exception):
    """Config is missing, malformed, or violates a project rule.

    Inherits from Exception (not ValueError) so pydantic does not wrap it into
    ValidationError — callers get one predictable exception type.
    """


class SourceConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    root: Path
    include: list[str] = Field(default_factory=lambda: ["*.pdf", "*.docx", "*.csv"])


class ManifestConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    path: Path


class OcrConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    enabled: bool = True
    lang: str = "tha+eng"
    min_text_chars_per_page: int = 50


class ExtractionConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    ocr: OcrConfig = Field(default_factory=OcrConfig)
    workers: int = 4


class ChunkingConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    min_tokens: int = 600
    max_tokens: int = 1000
    overlap: int = 100
    csv_row_group_size: int = 50


class LocalEmbeddingConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    model: str = "intfloat/multilingual-e5-small"
    backend: str = "onnx"
    quantize: bool = True


class FastEmbeddingConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    model: str = "text-embedding-3-small"


class EmbeddingConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    profile: Literal["local", "fast"] = "local"
    # Programmatic guard for CLAUDE.md rule 5 / spec NFR-05.
    allow_external: bool = False
    local: LocalEmbeddingConfig = Field(default_factory=LocalEmbeddingConfig)
    fast: FastEmbeddingConfig = Field(default_factory=FastEmbeddingConfig)
    batch_size: int = 64


class VectorStoreConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    backend: Literal["chroma"] = "chroma"
    path: Path
    collection: str = "internal_kb"


class RetrievalConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    top_k: int = 5


class LoggingConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    level: str = "INFO"
    path: Path


class Settings(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source: SourceConfig
    manifest: ManifestConfig
    extraction: ExtractionConfig = Field(default_factory=ExtractionConfig)
    chunking: ChunkingConfig = Field(default_factory=ChunkingConfig)
    embedding: EmbeddingConfig = Field(default_factory=EmbeddingConfig)
    vectorstore: VectorStoreConfig
    retrieval: RetrievalConfig = Field(default_factory=RetrievalConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)

    @model_validator(mode="after")
    def _guard_external_embedding(self) -> Settings:
        if self.embedding.profile == "fast" and not self.embedding.allow_external:
            raise ConfigurationError(
                'embedding.profile="fast" ต้องการ allow_external=true '
                "และต้องได้รับอนุมัติให้ส่งข้อมูลออกนอกเครื่องก่อน (CLAUDE.md ข้อ 5 / spec ข้อ 10)"
            )
        return self

    def ensure_dirs(self) -> None:
        """Create parent folders for runtime artifacts (never called at import time)."""
        for path in (self.manifest.path, self.vectorstore.path, self.logging.path):
            path.parent.mkdir(parents=True, exist_ok=True)


def load_settings(path: Path | str | None = None) -> Settings:
    """Load and validate config.yaml. Override the path with ``KB_CONFIG`` env var."""
    config_path = Path(path) if path is not None else Path(os.getenv("KB_CONFIG", "config.yaml"))
    if not config_path.is_file():
        raise ConfigurationError(f"ไม่พบไฟล์ config: {config_path}")
    try:
        raw = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        raise ConfigurationError(f"อ่าน config ไม่ได้: {exc}") from exc
    try:
        return Settings.model_validate(raw)
    except ValidationError as exc:
        raise ConfigurationError(f"config ไม่ถูกต้อง: {exc}") from exc
