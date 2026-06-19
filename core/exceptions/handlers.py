from fastapi import Request
from fastapi.responses import JSONResponse

from core.exceptions.base import LightRAGException


async def lightrag_exception_handler(
    request: Request,
    exc: LightRAGException,
) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )