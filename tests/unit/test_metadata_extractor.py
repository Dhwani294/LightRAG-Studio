from pathlib import Path

from services.ingestion.metadata_extractor import (
    MetadataExtractor,
)


def test_metadata_extraction(
    tmp_path: Path,
) -> None:

    file_path = tmp_path / "test.txt"

    file_path.write_text("abc")

    metadata = MetadataExtractor.extract(
        file_path,
    )

    assert metadata.filename == "test.txt"
    assert metadata.extension == ".txt"
    assert metadata.size > 0