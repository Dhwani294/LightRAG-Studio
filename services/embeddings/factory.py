from core.config.settings import (
    settings,
)

from services.embeddings.base import (
    EmbeddingProvider,
)
from services.embeddings.ollama_embeddings import (
    OllamaEmbeddingProvider,
)
from services.embeddings.openai_embeddings import (
    OpenAIEmbeddingProvider,
)


class EmbeddingFactory:

    @staticmethod
    def create(
        provider: str,
    ) -> EmbeddingProvider:

        if provider == "openai":

            return (
                OpenAIEmbeddingProvider(
                    api_key=(
                        settings.openai_api_key
                    ),
                )
            )

        if provider == "ollama":

            return (
                OllamaEmbeddingProvider(
                    host=(
                        settings.ollama_host
                    ),
                    model=(
                        settings.ollama_model
                    ),
                )
            )

        raise ValueError(
            f"Unknown provider: {provider}"
        )