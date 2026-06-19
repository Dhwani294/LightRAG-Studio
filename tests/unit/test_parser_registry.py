from pathlib import Path

from services.ingestion.parser_registry import (
    ParserRegistry,
)


def test_txt_parser_selected() -> None:

    registry = ParserRegistry()

    parser = registry.get_parser(
        Path("test.txt")
    )

    assert parser is not None