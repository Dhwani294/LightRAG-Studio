from services.llm.providers.mock_provider import MockProvider
from services.llm.registry import ProviderRegistry

def test_registry() -> None:
    registry = ProviderRegistry()
    registry.register("mock", MockProvider())
    provider = registry.get("mock")
    assert provider is not None
