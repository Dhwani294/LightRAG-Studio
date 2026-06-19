from services.llm.providers.mock_provider import (
    MockProvider,
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

        return registry