from typing import Any
from typing import cast

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)

from repositories.vector.base import VectorRepository
from schemas.vector_document import VectorDocument
from schemas.vector_result import VectorSearchResult


class QdrantRepository(VectorRepository):

    def __init__(
        self,
        collection_name: str,
        dimension: int,
        host: str = "localhost",
        port: int = 6333,
    ) -> None:

        self.client = QdrantClient(
            host=host,
            port=port,
        )

        self.collection_name = collection_name

        collections = self.client.get_collections()

        existing = {
            collection.name
            for collection in collections.collections
        }

        if collection_name not in existing:

            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(
                    size=dimension,
                    distance=Distance.COSINE,
                ),
            )

    async def add_documents(
        self,
        documents: list[VectorDocument],
    ) -> None:

        points = [
            PointStruct(
                id=doc.id,
                vector=doc.embedding,
                payload={
                    "content": doc.content,
                    **doc.metadata,
                },
            )
            for doc in documents
        ]

        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )

    async def search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ) -> list[VectorSearchResult]:

        results = cast(
            Any,
            getattr(
                self.client,
                "search",
            )(
                collection_name=self.collection_name,
                query_vector=embedding,
                limit=top_k,
            ),
        )

        output: list[VectorSearchResult] = []

        for result in results:

            payload = result.payload or {}

            output.append(
                VectorSearchResult(
                    id=str(result.id),
                    score=float(result.score),
                    content=str(
                        payload.get(
                            "content",
                            "",
                        )
                    ),
                    metadata={
                        k: str(v)
                        for k, v in payload.items()
                        if k != "content"
                    },
                )
            )

        return output

    async def get(
        self,
        document_id: str,
    ) -> VectorDocument | None:

        results = self.client.retrieve(
            collection_name=self.collection_name,
            ids=[document_id],
            with_vectors=True,
        )

        if not results:
            return None

        point = results[0]

        payload = point.payload or {}

        return VectorDocument(
            id=str(point.id),
            content=str(
                payload.get(
                    "content",
                    "",
                )
            ),
            embedding=cast(
                list[float],
                point.vector,
            ),
            metadata={
                k: str(v)
                for k, v in payload.items()
                if k != "content"
            },
        )

    async def delete(
        self,
        document_id: str,
    ) -> bool:

        self.client.delete(
            collection_name=self.collection_name,
            points_selector=[
                document_id
            ],
        )

        return True

    async def update(
        self,
        document: VectorDocument,
    ) -> None:

        await self.add_documents(
            [document]
        )

    async def count(
        self,
    ) -> int:

        info = self.client.get_collection(
            self.collection_name
        )

        return int(
            info.points_count
            or 0
        )