import pytest

from services.llm.retry_handler import (
    RetryHandler,
)


@pytest.mark.asyncio
async def test_retry_handler(
) -> None:

    counter = 0

    async def failing(
    ) -> str:

        nonlocal counter

        counter += 1

        if counter < 3:
            raise ValueError()

        return "success"

    result = (
        await RetryHandler.execute(
            failing
        )
    )

    assert result == "success"