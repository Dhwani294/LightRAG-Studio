from services.llm.cost_tracker import (
    CostTracker,
)


def test_cost() -> None:

    cost = (
        CostTracker
        .calculate_cost(
            "gpt-4o-mini",
            1000,
            500,
        )
    )

    assert cost > 0