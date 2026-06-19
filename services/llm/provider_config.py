from pydantic import BaseModel


class ProviderConfig(
    BaseModel
):
    provider_name: str
    enabled: bool = True