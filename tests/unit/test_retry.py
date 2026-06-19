from typing import Any

from services.ingestion.retry import (
    retry_policy,
)


def test_retry_policy_exists() -> None:

    decorator: Any = (
        retry_policy()
    )

    assert decorator is not None