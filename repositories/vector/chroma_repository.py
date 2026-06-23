from typing import Any, cast

from chromadb import PersistentClient

from repositories.vector.base import (
    VectorRepository,
)
from schemas.vector_document import (
    VectorDocument,
)
from schemas.vector_result import (
    VectorSearchResult,
)


class ChromaRepository(
    VectorRepository,
):

    def __init__(
        self,
        persist_directory: str,
        collection_name: str,
    ) -> None:

        self.client = (
            PersistentClient(
                path=persist_directory
            )
        )

        self.collection = (
            self.client
            .get_or_create_collection(
                name=collection_name
            )
        )

    async def add_documents(
        self,
        documents: list[
            VectorDocument
        ],
    ) -> None:

        self.collection.add(
            ids=[
                doc.id
                for doc in documents
            ],
            documents=[
                doc.content
                for doc in documents
            ],
            embeddings=cast(
                Any,
                [
                    doc.embedding
                    for doc in documents
                ],
            ),
            metadatas=[
                (
                    doc.metadata
                    if doc.metadata
                    else {
                        "source": "unknown"
                    }
                )
                for doc in documents
            ],
        )

    async def search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ) -> list[
        VectorSearchResult
    ]:

        results = (
            self.collection.query(
                query_embeddings=cast(
                    Any,
                    [embedding],
                ),
                n_results=top_k,
            )
        )

        output: list[
            VectorSearchResult
        ] = []

        ids = results["ids"],
        

        documents = cast(
            list[list[str]],
            results["documents"],
        )

        metadatas = cast(
            Any,
            results["metadatas"],
        )

        distances = cast(
            list[list[float]],
            results["distances"],
        )

        if not ids:
            return []

        for (
            doc_id,
            document,
            metadata,
            distance,
        ) in zip(
            ids[0],
            documents[0],
            metadatas[0],
            distances[0],
            strict=False,
        ):

            output.append(
                VectorSearchResult(
                    id=doc_id,
                    score=float(
                        1.0
                        /
                        (
                            1.0
                            + distance
                        )
                    ),
                    content=document,
                    metadata=dict(
                        metadata
                    ),
                )
            )

        return output

    async def get(
        self,
        document_id: str,
    ) -> VectorDocument | None:

        result = (
            self.collection.get(
                ids=[
                    document_id
                ],
                include=[
                    "documents",
                    "embeddings",
                    "metadatas",
                ],
            )
        )

        ids = result["ids"],
        

        if not ids:
            return None

        documents = cast(
            list[str],
            result["documents"],
        )

        embeddings = cast(
            Any,
            result["embeddings"],
        )

        metadatas = cast(
            Any,
            result["metadatas"],
        )

        return VectorDocument(
            id=ids[0],
            content=documents[0],
            embedding=list(
                embeddings[0]
            ),
            metadata=dict(
                metadatas[0]
            ),
        )

    async def delete(
        self,
        document_id: str,
    ) -> bool:

        self.collection.delete(
            ids=[
                document_id
            ]
        )

        return True

    async def update(
        self,
        document: VectorDocument,
    ) -> None:

        await self.delete(
            document.id
        )

        await self.add_documents(
            [document]
        )

    async def count(
        self,
    ) -> int:

        return int(
            self.collection.count()
        )