import pytest

from repositories.vector.in_memory_vector_repository import (
    InMemoryVectorRepository,
)
from schemas.vector_document import (
    VectorDocument,
)


@pytest.mark.asyncio
async def test_add_document(
) -> None:

    repository = (
        InMemoryVectorRepository()
    )

    document = (
        VectorDocument(
            id="1",
            content="hello",
            embedding=[0.1, 0.2],
            metadata={},
        )
    )

    await repository.add_documents(
        [document]
    )

    count = (
        await repository.count()
    )

    assert count == 1


@pytest.mark.asyncio
async def test_get_document(
) -> None:

    repository = (
        InMemoryVectorRepository()
    )

    document = (
        VectorDocument(
            id="1",
            content="hello",
            embedding=[0.1],
            metadata={},
        )
    )

    await repository.add_documents(
        [document]
    )

    result = (
        await repository.get("1")
    )

    assert result is not None

    assert result.id == "1"


@pytest.mark.asyncio
async def test_delete_document(
) -> None:

    repository = (
        InMemoryVectorRepository()
    )

    document = (
        VectorDocument(
            id="1",
            content="hello",
            embedding=[0.1],
            metadata={},
        )
    )

    await repository.add_documents(
        [document]
    )

    deleted = (
        await repository.delete(
            "1"
        )
    )

    assert deleted