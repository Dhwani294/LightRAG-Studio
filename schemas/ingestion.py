from pathlib import Path

from pydantic import BaseModel


class IngestionRequest(BaseModel):
    file_path: Path