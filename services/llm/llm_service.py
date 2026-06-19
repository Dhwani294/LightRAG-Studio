from schemas.llm_request import LLMRequest
from schemas.llm_response import LLMResponse
from services.llm.registry import ProviderRegistry


class LLMService:
    def __init__(
        self,
        registry: ProviderRegistry,
    ) -> None:
        self.registry = registry

    async def generate(
        self,
        provider_name: str,
        request: LLMRequest,
    ) -> LLMResponse:
        provider = self.registry.get(provider_name)
        return await provider.generate(request)
