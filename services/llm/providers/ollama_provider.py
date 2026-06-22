import httpx

from schemas.llm_request import (
    LLMRequest,
)
from schemas.llm_response import (
    LLMResponse,
)
from services.llm.exceptions import (
    LLMProviderError,
)
from services.llm.providers.base import (
    LLMProvider,
)
from services.llm.retry_handler import (
    RetryHandler,
)


class OllamaProvider(
    LLMProvider,
):

    def __init__(
        self,
        host: str,
        model: str,
    ) -> None:

        self.host = host

        self.model_name = model

    async def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:

        async def call_ollama(
        ) -> LLMResponse:

            try:

                async with (
                    httpx.AsyncClient()
                ) as client:

                    response = (
                        await client.post(
                            (
                                f"{self.host}"
                                "/api/generate"
                            ),
                            json={
                                "model":
                                self.model_name,
                                "prompt":
                                request.prompt,
                                "stream":
                                False,
                            },
                            timeout=60,
                        )
                    )

                    response.raise_for_status()

                    data = (
                        response.json()
                    )

                    return LLMResponse(
                        content=data.get(
                            "response",
                            "",
                        ),
                        provider="ollama",
                        model=self.model_name,
                        prompt_tokens=0,
                        completion_tokens=0,
                    )

            except Exception as exc:
                raise (
                    LLMProviderError(
                        str(exc)
                    )
                ) from exc

        return await (
            RetryHandler.execute(
                call_ollama,
                retries=3,
                delay=1,
            )
        )