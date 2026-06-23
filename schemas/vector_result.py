from typing import Any

from pydantic import BaseModel


class VectorSearchResult(BaseModel):
    id: str
    score: float
    content: str
    metadata: dict[str, Any]