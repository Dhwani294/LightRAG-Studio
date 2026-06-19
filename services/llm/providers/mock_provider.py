from schemas.llm_request import LLMRequest
from schemas.llm_response import LLMResponse
from services.llm.providers.base import LLMProvider

class MockProvider(LLMProvider):
    async def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:
        return LLMResponse(
            content=f"Mock response: {request.prompt}",
            provider="mock",
            model="mock-model",
            prompt_tokens=10,
            completion_tokens=20,
        )
