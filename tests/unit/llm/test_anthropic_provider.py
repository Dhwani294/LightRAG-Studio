from services.llm.providers.anthropic_provider import (
    AnthropicProvider,
)


def test_provider_creation(
) -> None:

    provider = (
        AnthropicProvider(
            api_key="dummy",
            model="claude-3-5-sonnet-latest",
        )
    )

    assert (
        provider.model_name
        == "claude-3-5-sonnet-latest"
    )