import pytest
from schemas.llm_request import LLMRequest
from services.llm.providers.mock_provider import MockProvider


@pytest.mark.asyncio
async def test_mock_provider() -> None:
    provider = MockProvider()
    response = await provider.generate(LLMRequest(prompt="hello"))

    assert response.provider == "mock"
    assert response.model == "mock-model"
    assert "hello" in response.content
