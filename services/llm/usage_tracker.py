from dataclasses import dataclass


@dataclass
class UsageRecord:

    provider: str

    model: str

    prompt_tokens: int

    completion_tokens: int

    total_tokens: int