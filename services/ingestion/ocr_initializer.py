import pytesseract  # type: ignore

from core.config.settings import (
    settings,
)


def initialize_ocr() -> None:

    if settings.tesseract_cmd:

        pytesseract.pytesseract.tesseract_cmd = (
            settings.tesseract_cmd
        )