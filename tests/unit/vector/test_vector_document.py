from schemas.vector_document import (
    VectorDocument,
)


def test_vector_document() -> None:

    doc = VectorDocument(
        id="1",
        content="hello",
        embedding=[0.1, 0.2],
        metadata={},
    )

    assert doc.id == "1"