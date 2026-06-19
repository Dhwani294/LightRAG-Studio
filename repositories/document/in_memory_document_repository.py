from models.document import Document
from repositories.document.document_repository import (
    DocumentRepository,
)


class InMemoryDocumentRepository(
    DocumentRepository,
):
    def __init__(self) -> None:
        self._documents: list[Document] = []

    async def save(
        self,
        document: Document,
    ) -> Document:

        self._documents.append(
            document
        )

        return document

    async def exists_by_hash(
        self,
        sha256_hash: str,
    ) -> bool:

        return any(
            document.sha256_hash
            == sha256_hash
            for document in self._documents
        )