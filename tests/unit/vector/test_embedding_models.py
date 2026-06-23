from services.embeddings.ollama_embeddings import (
    OllamaEmbeddingProvider,
)


def test_provider_init(
) -> None:

    provider = (
        OllamaEmbeddingProvider(
            host="http://localhost",
            model="nomic-embed-text",
        )
    )

    assert (
        provider.model
        == "nomic-embed-text"
    )