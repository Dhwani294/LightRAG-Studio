from pathlib import Path

from docx import Document

from services.ingestion.parsers.base import BaseParser


class DocxParser(BaseParser):

    async def parse(
        self,
        file_path: Path,
    ) -> str:

        document = Document(str(file_path))

        return "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )