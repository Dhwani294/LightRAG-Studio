from core.config.settings import settings


def test_settings_loaded() -> None:
    assert settings.app_name == "LightRAG Studio"
    assert isinstance(settings.debug, bool)