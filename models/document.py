from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class Document:
    id: UUID
    filename: str
    file_type: str
    file_size: int
    sha256_hash: str
    chunk_count: int
    created_at: datetime