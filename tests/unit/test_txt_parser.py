from pathlib import Path

import pytest

from services.ingestion.parsers.txt_parser import (
    TxtParser,
)


@pytest.mark.asyncio
async def test_txt_parser(
    tmp_path: Path,
) -> None:

    file_path = tmp_path / "sample.txt"

    file_path.write_text(
        "hello world"
    )

    parser = TxtParser()

    result = await parser.parse(
        file_path
    )

    assert result == "hello world"