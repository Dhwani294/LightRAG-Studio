from pathlib import Path

from services.ingestion.hash_service import HashService


def test_hash_generation(
    tmp_path: Path,
) -> None:

    file_path = tmp_path / "sample.txt"

    file_path.write_text("hello world")

    digest = HashService.calculate_sha256(
        file_path,
    )

    assert len(digest) == 64