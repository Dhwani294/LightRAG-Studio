from core.config.settings import (
    settings,
)
from services.llm.providers.gemini_provider import (
    GeminiProvider,
)
from services.llm.providers.mock_provider import (
    MockProvider,
)
from services.llm.providers.openai_provider import (
    OpenAIProvider,
)
from services.llm.registry import (
    ProviderRegistry,
)


class ProviderLoader:

    @staticmethod
    def load_default_registry(
    ) -> ProviderRegistry:

        registry = (
            ProviderRegistry()
        )

        registry.register(
            "mock",
            MockProvider(),
        )

        if settings.openai_api_key:

            registry.register(
                "openai",
                OpenAIProvider(
                    api_key=settings.openai_api_key,
                    model=settings.openai_model,
                ),
            )

        if settings.gemini_api_key:

            registry.register(
                "gemini",
                GeminiProvider(
                    api_key=settings.gemini_api_key,
                    model=settings.gemini_model,
                ),
            )

        return registry