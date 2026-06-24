from repositories.vector.factory import (
    VectorRepositoryFactory,
)

from repositories.vector.base import (
    VectorRepository,
)


def test_factory_returns_repo() -> None:

    repo = (
        VectorRepositoryFactory
        .create()
    )

    assert isinstance(
        repo,
        VectorRepository,
    )