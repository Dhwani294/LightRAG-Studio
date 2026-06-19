from schemas.model_config import (
    ModelConfig,
)
from services.llm.model_registry import (
    ModelRegistry,
)


def test_model_registry() -> None:

    registry = ModelRegistry()

    registry.register(
        "mock-model",
        ModelConfig(
            provider="mock",
            model_name="mock-model",
        ),
    )

    model = registry.get(
        "mock-model"
    )

    assert (
        model.provider
        == "mock"
    )