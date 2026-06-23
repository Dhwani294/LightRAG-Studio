from pathlib import Path

import pytest

from repositories.vector.chroma_repository import (
    ChromaRepository,
)
from schemas.vector_document import (
    VectorDocument,
)


@pytest.mark.asyncio
async def test_chroma_add_and_search(
    tmp_path: Path,
) -> None:

    repository = (
        ChromaRepository(
            persist_directory=
            str(tmp_path),
            collection_name=
            "test",
        )
    )

    document = (
        VectorDocument(
            id="1",
            content="hello",
            embedding=[
                1.0,
                0.0,
                0.0,
            ],
            metadata={
                "source": "test"
            },
        )
    )

    await repository.add_documents(
        [document]
    )

    results = (
        await repository.search(
            [
                1.0,
                0.0,
                0.0,
            ]
        )
    )

    assert (
        len(results)
        >= 1
    )