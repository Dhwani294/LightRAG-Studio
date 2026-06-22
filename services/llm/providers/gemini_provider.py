from schemas.llm_request import (
    LLMRequest,
)
from schemas.llm_response import (
    LLMResponse,
)
from services.llm.providers.base import (
    LLMProvider,
)


class GeminiProvider(
    LLMProvider,
):

    def __init__(
        self,
        api_key: str,
        model: str,
    ) -> None:

        self.api_key = api_key

        self.model_name = model

    async def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:

        raise NotImplementedError(
            (
                "Gemini implementation "
                "will be completed "
                "in provider hardening phase."
            )
        )