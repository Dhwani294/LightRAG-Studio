from core.config.settings import (
    settings,
)

from repositories.vector.base import (
    VectorRepository,
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

class VectorRepositoryFactory:

    @staticmethod
    def create(
        dimension: int,
    ) -> VectorRepository:

        if (
            settings.vector_store
            == "faiss"
        ):

            return (
                FaissRepository(
                    dimension=
                    dimension,
                    index_path=
                    settings.faiss_index_path,
                    metadata_path=
                    settings.faiss_metadata_path,
                )
            )

        if (
            settings.vector_store
            == "chroma"
        ):

            return (
                ChromaRepository(
                    persist_directory=
                    settings.chroma_path,
                    collection_name=
                    settings.chroma_collection,
                )
            )

        if (
            settings.vector_store
            == "qdrant"
        ):

            return (
                QdrantRepository(
                    collection_name=
                    settings.qdrant_collection,
                    dimension=
                    dimension,
                    host=
                    settings.qdrant_host,
                    port=
                    settings.qdrant_port,
                )
            )

        raise ValueError(
            (
                "Unsupported "
                "vector store"
            )
        )