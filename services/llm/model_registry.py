from schemas.model_config import (
    ModelConfig,
)


class ModelRegistry:

    def __init__(self) -> None:

        self._models: dict[
            str,
            ModelConfig,
        ] = {}

    def register(
        self,
        name: str,
        config: ModelConfig,
    ) -> None:

        self._models[name] = config

    def get(
        self,
        name: str,
    ) -> ModelConfig:

        if name not in self._models:
            raise ValueError(
                f"Model not found: {name}"
            )

        return self._models[name]

    def list_models(
        self,
    ) -> list[str]:

        return list(
            self._models.keys()
        )