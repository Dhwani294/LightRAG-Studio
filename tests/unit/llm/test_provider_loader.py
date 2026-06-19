from services.llm.provider_loader import (
    ProviderLoader,
)


def test_loader() -> None:

    registry = (
        ProviderLoader
        .load_default_registry()
    )

    provider = registry.get(
        "mock"
    )

    assert provider is not None