from pathlib import Path

import pytest

from services.ingestion.file_validator import (
    FileValidator,
)


def test_valid_file(
    tmp_path: Path,
) -> None:

    file_path = (
        tmp_path / "sample.txt"
    )

    file_path.write_text(
        "hello"
    )

    FileValidator.validate(
        file_path
    )


def test_invalid_extension(
    tmp_path: Path,
) -> None:

    file_path = (
        tmp_path / "sample.exe"
    )

    file_path.write_text(
        "bad"
    )

    with pytest.raises(
        Exception
    ):
        FileValidator.validate(
            file_path
        )