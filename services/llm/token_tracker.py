class TokenTracker:

    @staticmethod
    def total_tokens(
        prompt_tokens: int,
        completion_tokens: int,
    ) -> int:

        return (
            prompt_tokens
            + completion_tokens
        )