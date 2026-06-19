from pydantic import BaseModel

from schemas.ingestion_metrics import (
    IngestionMetrics,
)


class IngestionResult(
    BaseModel
):
    document_id: str
    filename: str
    sha256_hash: str
    chunk_count: int
    status: str

    metrics: (
        IngestionMetrics
        | None
    ) = None