from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

class AppException(HTTPException):
    def __init__(self, status_code: int = HTTP_400_BAD_REQUEST, detail: str = "Application error"):
        super().__init__(status_code=status_code, detail=detail)

class NotFoundException(AppException):
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(status_code=HTTP_404_NOT_FOUND, detail=detail)

