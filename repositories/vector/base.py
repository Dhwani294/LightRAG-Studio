from abc import ABC
from abc import abstractmethod

from schemas.vector_document import (
    VectorDocument,
)
from schemas.vector_result import (
    VectorSearchResult,
)


class VectorRepository(
    ABC,
):

    @abstractmethod
    async def add_documents(
        self,
        documents: list[VectorDocument],
    ) -> None:
        pass

    @abstractmethod
    async def search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ) -> list[VectorSearchResult]:
        pass

    @abstractmethod
    async def get(
        self,
        document_id: str,
    ) -> VectorDocument | None:
        pass

    @abstractmethod
    async def delete(
        self,
        document_id: str,
    ) -> bool:
        pass

    @abstractmethod
    async def update(
        self,
        document: VectorDocument,
    ) -> None:
        pass

    @abstractmethod
    async def count(
        self,
    ) -> int:
        pass