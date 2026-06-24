from schemas.vector_document import (
    VectorDocument,
)


def test_qdrant_import() -> None:

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
                "source":
                "test"
            },
        )
    )

    assert (
        document.id
        == "1"
    )