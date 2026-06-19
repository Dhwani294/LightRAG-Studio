from abc import ABC
from abc import abstractmethod

from schemas.llm_request import LLMRequest
from schemas.llm_response import LLMResponse


class LLMProvider(ABC):

    @abstractmethod
    async def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:
        """
        Generate a response from an LLM.
        """
        raise NotImplementedError