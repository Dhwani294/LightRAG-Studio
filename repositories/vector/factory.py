from repositories.vector.base import (
    VectorRepository,
)

from repositories.vector.in_memory_vector_repository import (
    InMemoryVectorRepository,
)


from repositories.vector.chroma_repository import (
    ChromaRepository,
)

from repositories.vector.faiss_repository import (
    FaissRepository,
)

from repositories.vector.qdrant_repository import (
    QdrantRepository,
)

from core.config.settings import (
    settings,
)


class VectorRepositoryFactory:

    @staticmethod
    def create() -> VectorRepository:

        backend = (
            settings.vector_backend
            .lower()
        )

        dimension = (
            settings.embedding_dimension
        )

        if backend == "memory":

            return (
                InMemoryVectorRepository()
            )

        if backend == "faiss":

            return (
                FaissRepository(
                    dimension=dimension,
                    index_path="data/faiss/index.bin",
                    metadata_path="data/faiss/metadata.json",
                )
            )

        if backend == "chroma":

            return (
                ChromaRepository(
                    persist_directory=
                    settings.chroma_path,
                    collection_name=
                    settings.chroma_collection,
                )
            )

        if backend == "qdrant":

            return (
                QdrantRepository(
                    collection_name=
                    settings.qdrant_collection,
                    dimension=dimension,
                    host=
                    settings.qdrant_host,
                    port=
                    settings.qdrant_port,
                )
            )

        raise ValueError(
            f"Unsupported vector backend: "
            f"{backend}"
        )