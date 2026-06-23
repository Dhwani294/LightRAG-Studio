from typing import Any

from pydantic import BaseModel


class VectorDocument(BaseModel):
    id: str
    content: str
    embedding: list[float]
    metadata: dict[str, Any]