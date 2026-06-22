import asyncio
from collections.abc import Awaitable
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


class RetryHandler:

    @staticmethod
    async def execute(
        operation: Callable[
            [],
            Awaitable[T],
        ],
        retries: int = 3,
        delay: float = 1.0,
    ) -> T:

        last_error: Exception | None = None

        for attempt in range(
            retries
        ):

            try:
                return await operation()

            except Exception as exc:
                last_error = exc

                if (
                    attempt
                    < retries - 1
                ):
                    await asyncio.sleep(
                        delay
                    )

        assert last_error is not None

        raise last_error