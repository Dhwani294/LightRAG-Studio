from pydantic import BaseModel


class LLMResponse(BaseModel):
	content: str
	provider: str
	model: str
	prompt_tokens: int = 0
	completion_tokens: int = 0