from pydantic import BaseModel


class DocumentMetadata(BaseModel):
    filename: str
    extension: str
    size: int