class CostTracker:

    MODEL_PRICING = {
        "gpt-4o-mini": {
            "input": 0.15,
            "output": 0.60,
        },
        "gemini-2.5-flash": {
            "input": 0.30,
            "output": 2.50,
        },
    }

    @classmethod
    def calculate_cost(
        cls,
        model: str,
        prompt_tokens: int,
        completion_tokens: int,
    ) -> float:

        pricing = cls.MODEL_PRICING.get(
            model
        )

        if pricing is None:
            return 0.0

        input_cost = (
            prompt_tokens
            / 1_000_000
        ) * pricing["input"]

        output_cost = (
            completion_tokens
            / 1_000_000
        ) * pricing["output"]

        return (
            input_cost
            + output_cost
        )