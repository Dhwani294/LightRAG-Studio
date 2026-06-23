import json
from pathlib import Path

import faiss  # type: ignore[import-untyped]
import numpy as np

from repositories.vector.base import (
    VectorRepository,
)
from schemas.vector_document import (
    VectorDocument,
)
from schemas.vector_result import (
    VectorSearchResult,
)


class FaissRepository(
    VectorRepository,
):

    def __init__(
        self,
        dimension: int,
        index_path: str,
        metadata_path: str,
    ) -> None:

        self.dimension = dimension

        self.index_path = Path(
            index_path
        )

        self.metadata_path = Path(
            metadata_path
        )

        self.index = (
            faiss.IndexFlatL2(
                dimension
            )
        )

        self.documents: dict[
            str,
            VectorDocument
        ] = {}

        self._load()

    def _load(
        self,
    ) -> None:

        if (
            self.index_path.exists()
        ):

            self.index = (
                faiss.read_index(
                    str(
                        self.index_path
                    )
                )
            )

        if (
            self.metadata_path.exists()
        ):

            with open(
                self.metadata_path,
                "r",
                encoding="utf-8",
            ) as file:

                data = json.load(
                    file
                )

            self.documents = {
                item["id"]:
                VectorDocument(
                    **item
                )
                for item in data
            }

    def _save(
        self,
    ) -> None:

        self.index_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        faiss.write_index(
            self.index,
            str(self.index_path),
        )

        with open(
            self.metadata_path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                [
                    document.model_dump()
                    for document in (
                        self.documents.values()
                    )
                ],
                file,
                indent=2,
            )

    async def add_documents(
        self,
        documents: list[
            VectorDocument
        ],
    ) -> None:

        vectors = np.array(
            [
                document.embedding
                for document in documents
            ],
            dtype=np.float32,
        )

        self.index.add(
            vectors
        )

        for document in documents:

            self.documents[
                document.id
            ] = document

        self._save()

    async def search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ) -> list[
        VectorSearchResult
    ]:

        if (
            self.index.ntotal == 0
        ):
            return []

        query = np.array(
            [embedding],
            dtype=np.float32,
        )

        distances, indices = (
            self.index.search(
                query,
                top_k,
            )
        )

        docs = list(
            self.documents.values()
        )

        results: list[
            VectorSearchResult
        ] = []

        for distance, index in zip(
            distances[0],
            indices[0],
            strict=False,
        ):

            if (
                index < 0
                or index >= len(docs)
            ):
                continue

            document = docs[index]

            results.append(
                VectorSearchResult(
                    id=document.id,
                    score=float(
                        1
                        /
                        (
                            1
                            + distance
                        )
                    ),
                    content=document.content,
                    metadata=document.metadata,
                )
            )

        return results

    async def get(
        self,
        document_id: str,
    ) -> VectorDocument | None:

        return self.documents.get(
            document_id
        )

    async def delete(
        self,
        document_id: str,
    ) -> bool:

        if (
            document_id
            not in self.documents
        ):
            return False

        del self.documents[
            document_id
        ]

        remaining = list(
            self.documents.values()
        )

        self.index = (
            faiss.IndexFlatL2(
                self.dimension
            )
        )

        if remaining:

            vectors = np.array(
                [
                    doc.embedding
                    for doc in remaining
                ],
                dtype=np.float32,
            )

            self.index.add(
                vectors
            )

        self._save()

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

        return len(
            self.documents
        )