from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
from jwt import decode, InvalidTokenError

SECRET_KEY = 'mySK'
ALGORITHM = 'HS256'

class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):

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
            request.state.user = None

        response = await call_next(request)
        return response