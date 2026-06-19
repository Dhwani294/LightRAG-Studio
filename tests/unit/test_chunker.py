from services.ingestion.chunker import (
    TextChunker,
)


def test_chunk_generation() -> None:

    text = "A" * 3000

    chunker = TextChunker(
        chunk_size=1000,
        overlap=200,
    )

    chunks = chunker.chunk(text)

    assert len(chunks) > 1


def test_empty_text() -> None:

    chunker = TextChunker()

    chunks = chunker.chunk("")

    assert chunks == []


def test_chunk_count() -> None:

    text = "A" * 3000

    chunker = TextChunker()

    count = chunker.count_chunks(text)

    assert count > 1


def test_token_estimation() -> None:

    text = "A" * 2000

    chunker = TextChunker()

    total_tokens = chunker.total_tokens(text)

    assert total_tokens > 0