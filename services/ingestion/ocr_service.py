from pathlib import Path
from typing import cast

import pytesseract  # type: ignore
from PIL import Image


class OCRService:

    def extract_text(
        self,
        image_path: Path,
    ) -> str:

        image = Image.open(
            image_path
        )

        text = cast(
            str,
            pytesseract.image_to_string(
                image
            ),
        )

        return text