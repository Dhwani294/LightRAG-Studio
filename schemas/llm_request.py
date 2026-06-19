from pydantic import BaseModel 
class LLMRequest(BaseModel): 
    prompt: str 
    temperature: float = 0.0 
    max_tokens: int = 512