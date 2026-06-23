from services.embeddings.factory import (
    EmbeddingFactory,
)


def test_factory_creation(
) -> None:

    provider = (
        EmbeddingFactory.create(
            "ollama"
        )
    )

    assert provider is not None