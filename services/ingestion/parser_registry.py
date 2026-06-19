from pathlib import Path

from services.ingestion.parsers.base import BaseParser
from services.ingestion.parsers.docx_parser import (
DocxParser,
)
from services.ingestion.parsers.markdown_parser import (
MarkdownParser,
)
from services.ingestion.parsers.pdf_parser import (
PdfParser,
)
from services.ingestion.parsers.txt_parser import (
TxtParser,
)

class ParserRegistry:

    def __init__(self) -> None:
        self._parsers: dict[str, BaseParser] = {
            ".pdf": PdfParser(),
            ".docx": DocxParser(),
            ".txt": TxtParser(),
            ".md": MarkdownParser(),
        }

    def get_parser(
        self,
        file_path: Path,
    ) -> BaseParser:
        extension = file_path.suffix.lower()

        if extension not in self._parsers:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        return self._parsers[extension]

