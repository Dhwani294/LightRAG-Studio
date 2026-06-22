from services.llm.cost_tracker import (
    CostTracker,
)
from services.llm.usage_tracker import (
    UsageRecord,
)


class UsageService:

    @staticmethod
    def calculate_cost(
        usage: UsageRecord,
    ) -> float:

        return (
            CostTracker
            .calculate_cost(
                model=usage.model,
                prompt_tokens=(
                    usage.prompt_tokens
                ),
                completion_tokens=(
                    usage.completion_tokens
                ),
            )
        )