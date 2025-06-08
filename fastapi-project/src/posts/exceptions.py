from fastapi import HTTPException, status

class PostNotFoundException(HTTPException):
    def __init__(self, detail: str = "Post not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
