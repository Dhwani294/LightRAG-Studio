from fastapi import FastAPI

from core.config.settings import settings

app = FastAPI(
    title=settings.app_name,
)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "message": "LightRAG Studio API"
    }


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {
        "status": "healthy"
    }