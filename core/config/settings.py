from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "LightRAG Studio"
    debug: bool = True

    tesseract_cmd: str = ""

    # Default LLM
    default_provider: str = "mock"
    default_model: str = "mock-model"

    # OpenAI
    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"

    # Gemini
    gemini_api_key: str = ""
    gemini_model: str = "gemini-2.5-flash"

    # Anthropic
    anthropic_api_key: str = ""
    anthropic_model: str = "claude-3-5-sonnet-latest"

    # Ollama
    ollama_host: str = "http://localhost:11434"
    ollama_model: str = "llama3"

    # Embeddings
    embedding_provider: str = "ollama"

    openai_embedding_model: str = (
        "text-embedding-3-small"
    )

    ollama_embedding_model: str = (
        "nomic-embed-text"
    )

    # Vector Store
    vector_store: str = "chroma"

    # FAISS
    faiss_index_path: str = (
        "data/faiss/index.bin"
    )

    faiss_metadata_path: str = (
        "data/faiss/metadata.json"
    )

    # Chroma
    chroma_path: str = (
        "data/chroma"
    )

    chroma_collection: str = (
        "documents"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()