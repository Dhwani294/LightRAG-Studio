from datetime import UTC, datetime
from pathlib import Path
from time import perf_counter
from uuid import uuid4

from core.exceptions.ingestion import (
    DuplicateDocumentError,
)
from models.document import Document
from repositories.document.in_memory_document_repository import (
    InMemoryDocumentRepository,
)
from schemas.ingestion_metrics import (
    IngestionMetrics,
)
from schemas.ingestion_result import (
    IngestionResult,
)
from services.ingestion.chunker import (
    TextChunker,
)
from services.ingestion.file_validator import (
    FileValidator,
)
from services.ingestion.hash_service import (
    HashService,
)
from services.ingestion.ingestion_logger import (
    logger,
)
from services.ingestion.metadata_extractor import (
    MetadataExtractor,
)
from services.ingestion.parser_registry import (
    ParserRegistry,
)


class IngestionService:

    def __init__(
        self,
    ) -> None:

        self.repository = (
            InMemoryDocumentRepository()
        )

        self.chunker = TextChunker()

        self.registry = ParserRegistry()

    async def ingest_document(
        self,
        file_path: Path,
    ) -> IngestionResult:

        start_time = perf_counter()

        FileValidator.validate(
            file_path
        )

        metadata = (
            MetadataExtractor.extract(
                file_path
            )
        )

        sha256_hash = (
            HashService.calculate_sha256(
                file_path
            )
        )

        exists = (
            await self.repository
            .exists_by_hash(
                sha256_hash
            )
        )

        if exists:
            raise DuplicateDocumentError(
                "Document already exists"
            )

        parser = (
            self.registry.get_parser(
                file_path
            )
        )

        text = await parser.parse(
            file_path
        )

        chunks = self.chunker.chunk(
            text
        )

        document = Document(
            id=uuid4(),
            filename=metadata.filename,
            file_type=metadata.extension,
            file_size=metadata.size,
            sha256_hash=sha256_hash,
            chunk_count=len(chunks),
            created_at=datetime.now(
                UTC
            ),
        )

        saved_document = (
            await self.repository.save(
                document
            )
        )

        elapsed_ms = (
            perf_counter()
            - start_time
        ) * 1000

        logger.info(
            "Document ingested",
            extra={
                "filename":
                saved_document.filename,
                "chunks":
                saved_document.chunk_count,
            },
        )

        metrics = (
            IngestionMetrics(
                file_size=
                saved_document.file_size,
                chunk_count=
                saved_document.chunk_count,
                processing_time_ms=
                elapsed_ms,
            )
        )

        return IngestionResult(
            document_id=str(
                saved_document.id
            ),
            filename=
            saved_document.filename,
            sha256_hash=
            saved_document.sha256_hash,
            chunk_count=
            saved_document.chunk_count,
            status="processed",
            metrics=metrics,
        )