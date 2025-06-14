from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ReviewCreate(BaseModel):
    order_id: int = Field(..., description="")
    recipient_id: int = Field(..., description="")
    rating: float = Field(..., ge=1, le=5, description="")
    comment: Optional[str] = Field(None, description="")

class ReviewRead(BaseModel):
    id: int
    order_id: int
    author_id: int
    recipient_id: int
    rating: float
    comment: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
