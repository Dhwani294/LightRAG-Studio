from pathlib import Path

from schemas.document_metadata import (
    DocumentMetadata,
)


class MetadataExtractor:

    @staticmethod
    def extract(
        file_path: Path,
    ) -> DocumentMetadata:

        stats = file_path.stat()

        return DocumentMetadata(
            filename=file_path.name,
            extension=file_path.suffix.lower(),
            size=stats.st_size,
        )