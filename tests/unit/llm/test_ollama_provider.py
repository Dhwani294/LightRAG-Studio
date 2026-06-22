from services.llm.providers.ollama_provider import (
    OllamaProvider,
)


def test_provider_creation(
) -> None:

    provider = (
        OllamaProvider(
            host="http://localhost:11434",
            model="llama3",
        )
    )

    assert (
        provider.model_name
        == "llama3"
    )