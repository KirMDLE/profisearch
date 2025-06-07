import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from src.logger import logger

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        start = time.time()
        response = await call_next(request)
        duration = time.time() - start

        logger.info(
            f'{request.method} {request.url.path} -> Status: {response.status_code} | Time: {duration:.4f}s'
        )
        return response
