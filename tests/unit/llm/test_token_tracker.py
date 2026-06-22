from services.llm.token_tracker import (
    TokenTracker,
)


def test_total_tokens() -> None:

    total = (
        TokenTracker
        .total_tokens(
            100,
            50,
        )
    )

    assert total == 150