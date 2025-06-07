from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
from jwt import decode, InvalidTokenError
from src.auth.config import settings

class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        public_paths = [
            "/docs",
            "/redoc",
            "/openapi.json",
            "/favicon.ico"
        ]

        if request.url.path in public_paths:
            return await call_next(request)
        
        token = request.headers.get("Authorization")

        if token:
            try:
                if token.startswith('Bearer '):
                    token = token[7:]
                payload = decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
                request.state.user = payload
            except InvalidTokenError:
                raise HTTPException(status_code=401, detail='Invalid JWT token')
        else:
            return JSONResponse(status_code=401, content={"detail": "Unauthorized"})

        return await call_next(request)
