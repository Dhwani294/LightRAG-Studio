from pathlib import Path

import pytest

from repositories.vector.faiss_repository import (
    FaissRepository,
)
from schemas.vector_document import (
    VectorDocument,
)


@pytest.mark.asyncio
async def test_faiss_add_and_search(
    tmp_path: Path,
) -> None:

    repository = FaissRepository(
        dimension=3,
        index_path=str(
            tmp_path / "index.bin"
        ),
        metadata_path=str(
            tmp_path / "metadata.json"
        ),
    )

    document = VectorDocument(
        id="1",
        content="hello",
        embedding=[
            1.0,
            0.0,
            0.0,
        ],
        metadata={},
    )

    await repository.add_documents(
        [document]
    )

    results = await repository.search(
        [
            1.0,
            0.0,
            0.0,
        ]
    )

    assert len(results) == 1

    assert results[0].id == "1"