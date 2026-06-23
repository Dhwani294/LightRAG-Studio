from schemas.embedding_record import (
    EmbeddingRecord,
)


def test_embedding_record() -> None:

    record = EmbeddingRecord(
        text="hello",
        embedding=[0.1],
    )

    assert len(record.embedding) == 1