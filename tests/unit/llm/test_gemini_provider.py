from services.llm.providers.gemini_provider import (
    GeminiProvider,
)


def test_provider_creation(
) -> None:

    provider = (
        GeminiProvider(
            api_key="dummy",
            model="gemini-2.5-flash",
        )
    )

    assert (
        provider.model_name
        == "gemini-2.5-flash"
    )