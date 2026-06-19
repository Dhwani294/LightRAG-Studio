from typing import Any
from typing import Callable

from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_exponential


def retry_policy() -> Callable[..., Any]:

    return retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(
            multiplier=1,
            min=1,
            max=10,
        ),
        reraise=True,
    )