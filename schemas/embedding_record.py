from pydantic import BaseModel


class EmbeddingRecord(
    BaseModel,
):

    text: str

    embedding: list[float]