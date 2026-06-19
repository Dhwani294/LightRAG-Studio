from pydantic import BaseModel


class IngestionMetrics(
    BaseModel
):
    file_size: int
    chunk_count: int
    processing_time_ms: float