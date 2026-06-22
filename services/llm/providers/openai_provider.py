from openai import (
    APITimeoutError,
)
from openai import (
    AsyncOpenAI,
)
from openai import (
    AuthenticationError,
)
from openai import (
    RateLimitError,
)

from schemas.llm_request import (
    LLMRequest,
)
from schemas.llm_response import (
    LLMResponse,
)
from services.llm.exceptions import (
    LLMAuthenticationError,
)
from services.llm.exceptions import (
    LLMProviderError,
)
from services.llm.exceptions import (
    LLMRateLimitError,
)
from services.llm.exceptions import (
    LLMTimeoutError,
)
from services.llm.providers.base import (
    LLMProvider,
)
from services.llm.retry_handler import (
    RetryHandler,
)


class OpenAIProvider(
    LLMProvider,
):

    def __init__(
        self,
        api_key: str,
        model: str,
    ) -> None:

        self.client = AsyncOpenAI(
            api_key=api_key,
        )

        self.model = model

    async def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:

        async def call_openai(
        ) -> LLMResponse:

            try:

                response = (
                    await self.client.chat.completions.create(
                        model=self.model,
                        messages=[
                            {
                                "role": "user",
                                "content":
                                request.prompt,
                            }
                        ],
                        temperature=(
                            request.temperature
                        ),
                        max_tokens=(
                            request.max_tokens
                        ),
                    )
                )

                usage = (
                    response.usage
                )

                prompt_tokens = 0
                completion_tokens = 0

                if (
                    usage
                    is not None
                ):
                    prompt_tokens = (
                        usage.prompt_tokens
                    )

                    completion_tokens = (
                        usage.completion_tokens
                    )

                content = ""

                if (
                    response.choices
                    and response
                    .choices[0]
                    .message.content
                ):
                    content = (
                        response
                        .choices[0]
                        .message.content
                    )

                return LLMResponse(
                    content=content,
                    provider="openai",
                    model=self.model,
                    prompt_tokens=(
                        prompt_tokens
                    ),
                    completion_tokens=(
                        completion_tokens
                    ),
                )

            except RateLimitError as exc:
                raise (
                    LLMRateLimitError(
                        str(exc)
                    )
                ) from exc

            except APITimeoutError as exc:
                raise (
                    LLMTimeoutError(
                        str(exc)
                    )
                ) from exc

            except AuthenticationError as exc:
                raise (
                    LLMAuthenticationError(
                        str(exc)
                    )
                ) from exc

            except Exception as exc:
                raise (
                    LLMProviderError(
                        str(exc)
                    )
                ) from exc

        return await (
            RetryHandler.execute(
                call_openai,
                retries=3,
                delay=1,
            )
        )