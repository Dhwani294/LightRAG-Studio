from pathlib import Path

from core.exceptions.ingestion import (
    FileTooLargeError,
)
from core.exceptions.ingestion import (
    UnsupportedFileTypeError,
)


class FileValidator:

    ALLOWED_EXTENSIONS = {
        ".pdf",
        ".docx",
        ".txt",
        ".md",
    }

    MAX_FILE_SIZE_MB = 50

    @classmethod
    def validate(
        cls,
        file_path: Path,
    ) -> None:

        extension = (
            file_path.suffix.lower()
        )

        if (
            extension
            not in cls.ALLOWED_EXTENSIONS
        ):
            raise (
                UnsupportedFileTypeError(
                    extension
                )
            )

        size_mb = (
            file_path.stat().st_size
            / (1024 * 1024)
        )

        if (
            size_mb
            > cls.MAX_FILE_SIZE_MB
        ):
            raise FileTooLargeError(
                f"{size_mb:.2f} MB"
            )