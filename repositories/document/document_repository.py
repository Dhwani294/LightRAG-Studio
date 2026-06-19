from abc import ABC, abstractmethod

from models.document import Document


class DocumentRepository(ABC):

    @abstractmethod
    async def save(
        self,
        document: Document,
    ) -> Document:
        raise NotImplementedError

    @abstractmethod
    async def exists_by_hash(
        self,
        sha256_hash: str,
    ) -> bool:
        raise NotImplementedError