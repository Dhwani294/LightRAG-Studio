from pathlib import Path

import aiofiles

from services.ingestion.parsers.base import (
    BaseParser,
)


class MarkdownParser(BaseParser):

    async def parse(
        self,
        file_path: Path,
    ) -> str:

        async with aiofiles.open(
            file_path,
            mode="r",
            encoding="utf-8",
        ) as file:

            content: str = await file.read()

        return content