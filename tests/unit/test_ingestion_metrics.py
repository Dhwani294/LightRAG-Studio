from schemas.ingestion_metrics import (
    IngestionMetrics,
)


def test_metrics_creation() -> None:

    metrics = (
        IngestionMetrics(
            file_size=100,
            chunk_count=5,
            processing_time_ms=12.5,
        )
    )

    assert (
        metrics.chunk_count
        == 5
    )