from pathlib import Path

import pytest

from services.ingestion.ingestion_service import (
    IngestionService,
)


@pytest.mark.asyncio
async def test_ingestion_pipeline(
    tmp_path: Path,
) -> None:

    file_path = (
        tmp_path / "sample.txt"
    )

    file_path.write_text(
        "hello world " * 500
    )

    service = IngestionService()

    result = (
        await service.ingest_document(
            file_path
        )
    )

    assert (
        result.status
        == "processed"
    )

    assert (
        result.chunk_count > 0
    )