from pydantic import BaseModel


class ModelConfig(BaseModel):
    provider: str
    model_name: str
    temperature: float = 0.0
    max_tokens: int = 512