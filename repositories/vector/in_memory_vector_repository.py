from schemas.vector_document import (
    VectorDocument,
)
from schemas.vector_result import (
    VectorSearchResult,
)

from repositories.vector.base import (
    VectorRepository,
)


class InMemoryVectorRepository(
    VectorRepository,
):

    def __init__(
        self,
    ) -> None:

        self._documents: dict[
            str,
            VectorDocument,
        ] = {}

    async def add_documents(
        self,
        documents: list[VectorDocument],
    ) -> None:

        for document in documents:
            self._documents[
                document.id
            ] = document

    async def search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ) -> list[VectorSearchResult]:

        results: list[
            VectorSearchResult
        ] = []

        for document in (
            self._documents.values()
        ):

            results.append(
                VectorSearchResult(
                    id=document.id,
                    score=1.0,
                    content=document.content,
                    metadata=document.metadata,
                )
            )

        return results[:top_k]

    async def get(
        self,
        document_id: str,
    ) -> VectorDocument | None:

        return self._documents.get(
            document_id
        )

    async def delete(
        self,
        document_id: str,
    ) -> bool:

        if (
            document_id
            not in self._documents
        ):
            return False

        del self._documents[
            document_id
        ]

        return True

    async def update(
        self,
        document: VectorDocument,
    ) -> None:

        self._documents[
            document.id
        ] = document

    async def count(
        self,
    ) -> int:

        return len(
            self._documents
        )