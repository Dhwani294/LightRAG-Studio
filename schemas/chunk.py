from pydantic import BaseModel


class Chunk(BaseModel):
    chunk_id: str
    content: str
    chunk_index: int
    start_char: int
    end_char: int
    token_estimate: int