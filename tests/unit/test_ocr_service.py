from services.ingestion.ocr_service import (
    OCRService,
)


def test_ocr_service_creation() -> None:

    service = OCRService()

    assert service is not None