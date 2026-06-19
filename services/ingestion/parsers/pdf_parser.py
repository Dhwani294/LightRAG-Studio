from pathlib import Path

from pypdf import PdfReader

from services.ingestion.parsers.base import (
    BaseParser,
)
from services.ingestion.retry import (
    retry_policy,
)


class PdfParser(BaseParser):

    @retry_policy()
    async def parse(
        self,
        file_path: Path,
    ) -> str:

        reader = PdfReader(
            str(file_path)
        )

        pages: list[str] = []

        for page in reader.pages:
            pages.append(
                page.extract_text()
                or ""
            )

        return "\n".join(
            pages
        )