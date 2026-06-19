from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: UUID
    filename: str
    file_type: str
    file_size: int
    sha256_hash: str
    created_at: datetime