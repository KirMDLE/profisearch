from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
from jwt import decode, InvalidTokenError

SECRET_KEY = 'mySK'
ALGORITHM = 'HS256'

class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
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
                payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                request.state.user = payload
            except InvalidTokenError:
                raise HTTPException(status_code=401, detail='invalid JWT token')
        else:
            return JSONResponse(status_code=401, content={"detail": "Unauthorized"})

        response = await call_next(request)
        return response