from pathlib import Path

import pytest

from services.ingestion.ingestion_service import (
    IngestionService,
)
from core.exceptions.ingestion import (
    DuplicateDocumentError,
)


@pytest.mark.asyncio
async def test_duplicate_document(
    tmp_path: Path,
) -> None:

    file_path = (
        tmp_path / "sample.txt"
    )

    file_path.write_text(
        "duplicate"
    )

    service = IngestionService()

    await service.ingest_document(
        file_path
    )

    with pytest.raises(
        DuplicateDocumentError
    ):
        await service.ingest_document(
            file_path
        )