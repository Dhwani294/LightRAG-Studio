class LLMProviderError(
    Exception,
):
    pass


class LLMRateLimitError(
    LLMProviderError,
):
    pass


class LLMTimeoutError(
    LLMProviderError,
):
    pass


class LLMAuthenticationError(
    LLMProviderError,
):
    pass