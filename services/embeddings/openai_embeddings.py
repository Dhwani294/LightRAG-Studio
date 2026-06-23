from typing import Any

from openai import AsyncOpenAI

from services.embeddings.base import (
    EmbeddingProvider,
)
from services.embeddings.exceptions import (
    EmbeddingError,
)


class OpenAIEmbeddingProvider(
    EmbeddingProvider,
):

    def __init__(
        self,
        api_key: str,
        model: str = (
            "text-embedding-3-small"
        ),
    ) -> None:

        self.client = AsyncOpenAI(
            api_key=api_key,
        )

        self.model = model

    async def embed(
        self,
        text: str,
    ) -> list[float]:

        try:

            response: Any = (
                await self.client.embeddings.create(
                    model=self.model,
                    input=text,
                )
            )

            return list(
                response.data[0].embedding
            )

        except Exception as exc:
            raise EmbeddingError(
                str(exc)
            ) from exc

    async def embed_batch(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        try:

            response: Any = (
                await self.client.embeddings.create(
                    model=self.model,
                    input=texts,
                )
            )

            return [
                list(item.embedding)
                for item in response.data
            ]

        except Exception as exc:
            raise EmbeddingError(
                str(exc)
            ) from exc