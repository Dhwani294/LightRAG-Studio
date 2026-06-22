from services.llm.provider_loader import (
    ProviderLoader,
)


def test_loader() -> None:

    registry = (
        ProviderLoader
        .load_default_registry()
    )

    assert registry is not None