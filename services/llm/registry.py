from services.llm.providers.base import LLMProvider

class ProviderRegistry:
    def __init__(self) -> None:
        self._providers: dict[str, LLMProvider] = {}

    def register(
        self,
        name: str,
        provider: LLMProvider,
    ) -> None:
        self._providers[name] = provider

    def get(
        self,
        name: str,
    ) -> LLMProvider:
        if name not in self._providers:
            raise ValueError(f"Provider not found: {name}")
        return self._providers[name]