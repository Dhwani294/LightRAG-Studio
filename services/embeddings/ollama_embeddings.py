import httpx

from services.embeddings.base import (
    EmbeddingProvider,
)
from services.embeddings.exceptions import (
    EmbeddingError,
)


class OllamaEmbeddingProvider(
    EmbeddingProvider,
):

    def __init__(
        self,
        host: str,
        model: str,
    ) -> None:

        self.host = host

        self.model = model

    async def embed(
        self,
        text: str,
    ) -> list[float]:

        try:

            async with (
                httpx.AsyncClient()
            ) as client:

                response = (
                    await client.post(
                        (
                            f"{self.host}"
                            "/api/embeddings"
                        ),
                        json={
                            "model":
                            self.model,
                            "prompt":
                            text,
                        },
                        timeout=60,
                    )
                )

                response.raise_for_status()

                data = (
                    response.json()
                )

                return list(
                    data["embedding"]
                )

        except Exception as exc:
            raise EmbeddingError(
                str(exc)
            ) from exc

    async def embed_batch(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        results: list[
            list[float]
        ] = []

        for text in texts:

            embedding = (
                await self.embed(
                    text
                )
            )

            results.append(
                embedding
            )

        return results