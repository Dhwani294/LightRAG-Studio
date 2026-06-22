from services.llm.usage_service import (
    UsageService,
)
from services.llm.usage_tracker import (
    UsageRecord,
)


def test_cost_calculation(
) -> None:

    usage = UsageRecord(
        provider="openai",
        model="gpt-4o-mini",
        prompt_tokens=1000,
        completion_tokens=500,
        total_tokens=1500,
    )

    cost = (
        UsageService
        .calculate_cost(
            usage
        )
    )

    assert cost > 0