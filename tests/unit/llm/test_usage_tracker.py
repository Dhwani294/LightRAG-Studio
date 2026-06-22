from services.llm.usage_tracker import (
    UsageRecord,
)


def test_usage_record() -> None:

    usage = UsageRecord(
        provider="openai",
        model="gpt-4o-mini",
        prompt_tokens=10,
        completion_tokens=20,
        total_tokens=30,
    )

    assert (
        usage.total_tokens
        == 30
    )