from schemas.vector_result import (
    VectorSearchResult,
)


def test_vector_result() -> None:

    result = VectorSearchResult(
        id="1",
        score=0.95,
        content="hello",
        metadata={},
    )

    assert result.score > 0