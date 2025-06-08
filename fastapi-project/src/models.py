from pydantic import BaseModel

class BaseResponseModel(BaseModel):
    success: bool = True
    message: str | None = None
